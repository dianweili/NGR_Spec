from __future__ import annotations

import json
import time
from collections import defaultdict
from dataclasses import asdict, dataclass, field, replace
from pathlib import Path

from ngr.config import load_features, load_sources
from ngr.extract.backend import CodexExec, LlmRateLimited
from ngr.extract.budget import Budget
from ngr.extract.cache import LlmCache
from ngr.extract.digest import digest_features
from ngr.extract.runner import extract_all
from ngr.fetch.client import Http, RateLimited
from ngr.fetch.discover import discover_meetings, fetch_window
from ngr.fetch.manifest import Manifest
from ngr.fetch.runner import fetch_meeting
from ngr.mapping.runner import map_meeting, merge_events, write_state
from ngr.ops.alerts import RunRecord, append_run, build_banner, load_runs
from ngr.ops.gitio import build_commit_message, commit_outputs, has_manual_changes
from ngr.ops.lock import ExclusiveRunLock
from ngr.parse.runner import parse_meeting, write_parsed
from ngr.paths import P
from ngr.render.runner import render_all

EXIT_OK, EXIT_FETCH, EXIT_PARSE, EXIT_LLM, EXIT_GIT = 0, 1, 2, 3, 4
GUARDED = ["config"]


@dataclass
class PipelineResult:
    exit_code: int = EXIT_OK
    alerts: list[str] = field(default_factory=list)
    new_events: int = 0
    llm_calls: int = 0
    stats_by_meeting: dict = field(default_factory=dict)


def _load(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default
    except json.JSONDecodeError:
        return default


def _write_state(events, features, feature_state, result, stats, started):
    today = time.strftime("%Y-%m-%d")
    write_state(events, P.state / "events.json")
    P.state.mkdir(parents=True, exist_ok=True)
    (P.state / "features_state.json").write_text(json.dumps(feature_state, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    record = RunRecord(time.strftime("%Y-%m-%dT%H:%M:%S"), round(time.time()-started, 1),
                       result.new_events, result.llm_calls, result.exit_code, "; ".join(result.alerts))
    # Render against the run that is about to be persisted.  Loading history before
    # append made every first successful run render as "从未成功"; appending only
    # after rendering still keeps a failed render out of the recorded history.
    runs = [*load_runs(P.state / "run_history.json"), asdict(record)]
    banner = build_banner(result.alerts, runs, today)
    from ngr.mapping.unmapped import collect_unmapped
    parsed = [payload for path in sorted(P.parsed.rglob("events.json")) if (payload := _load(path, {}))]
    render_all(events, features, feature_state, P.out, banner=banner,
               unmapped=collect_unmapped(features, parsed))
    result.stats_by_meeting = {key: dict(value) for key, value in stats.items()}
    append_run(P.state / "run_history.json", record)


def _enrich(events, features, state, cfg, result, *, checkpoint=None):
    if cfg.backend != "codex":
        return state
    budget, cache = Budget(cfg.max_calls_per_run), LlmCache(P.state / "llm_cache")
    factory = lambda model, effort: CodexExec(model, effort)
    summary = extract_all(events, cfg, cli_factory=factory, cache=cache, budget=budget,
                          checkpoint=checkpoint)
    # 逐条摘要通道已无响应时，不能再进入会使用同一 CLI 的特性综述阶段；
    # 否则一次超时会被放大为几十次额外调用，既无产出又长期占锁。
    if summary.timed_out:
        result.alerts.append("ChatGPT/Codex 调用超时，已暂停本轮并保留待处理事件")
        result.exit_code = max(result.exit_code, EXIT_LLM)
        return state
    state = digest_features(features, events, state, cfg, cli_factory=factory, cache=cache, budget=budget)
    budget.log(P.state / "usage_log.jsonl")
    result.llm_calls = budget.calls
    if summary.rate_limited:
        result.alerts.append("Codex 用量受限，部分摘要留待下次")
        result.exit_code = max(result.exit_code, EXIT_LLM)
    if summary.failed:
        result.alerts.append(f"{summary.failed} 条摘要生成失败")
    return state


def run_pipeline(*, wgs=None, use_llm=True, force=False, meetings=None) -> PipelineResult:
    started, result = time.time(), PipelineResult()
    cfg, features = load_sources(), load_features()
    manual = has_manual_changes(P.root, GUARDED)
    if manual:
        result.alerts.append(f"{', '.join(manual)} 有未提交的手工改动，已跳过自动提交")
        result.exit_code = EXIT_GIT
    events, stats, today = _load(P.state / "events.json", []), defaultdict(lambda: defaultdict(int)), time.strftime("%Y-%m-%d")
    http = Http(cfg.http)
    for wg, wgcfg in cfg.wgs.items():
        if wgs and wg not in wgs: continue
        window = meetings or fetch_window(features, wg, wgcfg)
        if window is None: continue
        lo, hi = window
        try: discovered = discover_meetings(http, wg, wgcfg)
        except RateLimited as exc:
            result.alerts.append(f"{wg} 会议发现被限流: {exc}")
            result.exit_code = max(result.exit_code, EXIT_FETCH)
            continue
        parsed_meetings = []
        for meeting in discovered:
            if meeting.number < lo or (hi is not None and meeting.number > hi): continue
            raw = P.raw_dir(wg, meeting.number, meeting.suffix)
            try: fetched = fetch_meeting(http, meeting, wgcfg, raw_dir=raw, force=force)
            except RateLimited as exc:
                result.alerts.append(f"{meeting.label} 抓取被限流: {exc}")
                result.exit_code = max(result.exit_code, EXIT_FETCH)
                continue
            if fetched.skipped_reason == "frozen" or "minutes_docx" in fetched.missing: continue
            parsed = parse_meeting(raw, meeting, agenda_required=bool(wgcfg.agenda_csv_since and meeting.number >= wgcfg.agenda_csv_since))
            parsed_dir = P.parsed_dir(wg, meeting.number, meeting.suffix)
            write_parsed(parsed, parsed_dir)
            payload = _load(parsed_dir / "events.json", {})
            events, merge = merge_events(events, map_meeting(payload, features), today,
                                         scope={(wg, meeting.number, meeting.suffix)})
            result.new_events += merge.added
            if merge.stale_ids: result.alerts.append(f"{meeting.label}: {len(merge.stale_ids)} 条历史事件本次未再出现")
            for key, per in merge.added_by_feature.items():
                for feature, count in per.items(): stats[key][feature] += count
            parsed_meetings.append((meeting.number, meeting.suffix))
        for number, suffix in sorted(parsed_meetings)[:-2]:
            manifest = Manifest(P.raw_dir(wg, number, suffix)); manifest.mark_frozen(); manifest.save()
    feature_state = _load(P.state / "features_state.json", {})
    if use_llm: feature_state = _enrich(events, features, feature_state, cfg.extract, result)
    _write_state(events, features, feature_state, result, stats, started)
    if not manual and result.new_events:
        commit_outputs(P.root, ["data/state", "out"], build_commit_message(result.stats_by_meeting))
    return result


def run_pipeline_remap() -> PipelineResult:
    started, result, features, today = time.time(), PipelineResult(), load_features(), time.strftime("%Y-%m-%d")
    previous_events = _load(P.state / "events.json", [])
    previous_ids = {event["id"] for event in previous_events}
    events, stats, parsed_scopes = [], defaultdict(lambda: defaultdict(int)), set()
    for path in sorted(P.parsed.rglob("events.json")):
        payload = _load(path, {})
        if not payload: continue
        scope = (payload["wg"], payload["meeting"], payload.get("meeting_suffix", ""))
        parsed_scopes.add(scope)
        # Merge against the pre-remap state to retain first_seen and any completed
        # LLM work for unchanged source text.  Only active_ids are retained below:
        # stale records from an anchor that was intentionally removed must not
        # survive a remap.
        merged, merge = merge_events(previous_events, map_meeting(payload, features), today,
                                     scope={scope})
        by_id = {event["id"]: event for event in merged}
        events.extend(by_id[event_id] for event_id in merge.active_ids)
    # State can contain meetings whose raw material is no longer available
    # locally.  A remap cannot judge those, so preserve them unchanged.
    events.extend(event for event in previous_events
                  if (event.get("wg"), event.get("meeting"), event.get("meeting_suffix", "")) not in parsed_scopes)
    # Remap reconstructs state from all parsed meetings, so merge.added is the
    # whole reconstructed corpus, not this run's increment.  Report only ids
    # absent from the prior state; otherwise a one-line feature-anchor change
    # masquerades as thousands of new protocol decisions.
    for event in events:
        if event["id"] in previous_ids:
            continue
        result.new_events += 1
        key = (event["wg"], event["meeting"], event.get("meeting_suffix", ""))
        stats[key][event["feature"]] += 1
    _write_state(events, features, _load(P.state / "features_state.json", {}), result, stats, started)
    return result


def run_pipeline_enrich(*, max_calls: int | None = None,
                        batch_size: int | None = None) -> PipelineResult:
    started, result, cfg, features = time.time(), PipelineResult(), load_sources(), load_features()
    lock = ExclusiveRunLock(P.state / "enrich.lock")
    if not lock.acquire():
        result.alerts.append("已有摘要任务在运行，已跳过本次以避免覆盖状态")
        return result
    try:
        extract_cfg = replace(
            cfg.extract,
            max_calls_per_run=max_calls if max_calls is not None else cfg.extract.max_calls_per_run,
            batch_size=batch_size if batch_size is not None else cfg.extract.batch_size,
        )
        events, state = _load(P.state / "events.json", []), _load(P.state / "features_state.json", {})
        state = _enrich(events, features, state, extract_cfg, result,
                        checkpoint=lambda: write_state(events, P.state / "events.json"))
        _write_state(events, features, state, result, defaultdict(dict), started)
        return result
    finally:
        lock.release()

def run_fetch_docs(*, wg, meeting, agenda):
    from ngr.fetch.docs import fetch_docs
    cfg = load_sources(); wgcfg = cfg.wgs[wg]; http = Http(cfg.http)
    target = next(item for item in discover_meetings(http, wg, wgcfg) if item.number == meeting)
    payload = _load(P.parsed_dir(wg, meeting) / "events.json", {})
    agenda_by_tdoc = {}
    for event in payload.get("events", []):
        for token in event.get("text_en", "").split():
            token = token.strip("(),.;:[]")
            if token.startswith(("R1-", "R2-", "R3-", "R4-")) and event.get("agenda_item"):
                agenda_by_tdoc.setdefault(token + ".zip", event["agenda_item"])
    return len(fetch_docs(http, target, wgcfg, agenda_prefix=agenda,
                          out_dir=P.raw_dir(wg, meeting) / "docs", tdoc_agenda=agenda_by_tdoc))
