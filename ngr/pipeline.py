from __future__ import annotations

import json
import time
from collections import defaultdict
from dataclasses import dataclass, field
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
from ngr.parse.runner import parse_meeting, write_parsed
from ngr.paths import P
from ngr.render.runner import render_all

EXIT_OK, EXIT_PARSE, EXIT_LLM, EXIT_GIT = 0, 2, 3, 4
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
    runs = load_runs(P.state / "run_history.json")
    banner = build_banner(result.alerts, runs, today)
    from ngr.mapping.unmapped import collect_unmapped
    parsed = [payload for path in sorted(P.parsed.rglob("events.json")) if (payload := _load(path, {}))]
    render_all(events, features, feature_state, P.out, banner=banner,
               unmapped=collect_unmapped(features, parsed, sixg_roots=["10"]))
    result.stats_by_meeting = {key: dict(value) for key, value in stats.items()}
    append_run(P.state / "run_history.json", RunRecord(time.strftime("%Y-%m-%dT%H:%M:%S"), round(time.time()-started, 1), result.new_events, result.llm_calls, result.exit_code, "; ".join(result.alerts)))


def _enrich(events, features, state, cfg, result):
    if cfg.backend != "codex":
        return state
    budget, cache = Budget(cfg.max_calls_per_run), LlmCache(P.state / "llm_cache")
    factory = lambda model, effort: CodexExec(model, effort)
    summary = extract_all(events, cfg, cli_factory=factory, cache=cache, budget=budget)
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
            result.alerts.append(f"{wg} 会议发现被限流: {exc}"); continue
        parsed_numbers = []
        for meeting in discovered:
            if meeting.number < lo or (hi is not None and meeting.number > hi): continue
            raw = P.raw_dir(wg, meeting.number)
            try: fetched = fetch_meeting(http, meeting, wgcfg, raw_dir=raw, force=force)
            except RateLimited as exc:
                result.alerts.append(f"{meeting.label} 抓取被限流: {exc}"); continue
            if fetched.skipped_reason == "frozen" or "minutes_docx" in fetched.missing: continue
            parsed = parse_meeting(raw, meeting, agenda_required=bool(wgcfg.agenda_csv_since and meeting.number >= wgcfg.agenda_csv_since))
            write_parsed(parsed, P.parsed_dir(wg, meeting.number))
            payload = _load(P.parsed_dir(wg, meeting.number) / "events.json", {})
            events, merge = merge_events(events, map_meeting(payload, features), today, scope={(wg, meeting.number)})
            result.new_events += merge.added
            if merge.stale_ids: result.alerts.append(f"{meeting.label}: {len(merge.stale_ids)} 条历史事件本次未再出现")
            for key, per in merge.added_by_feature.items():
                for feature, count in per.items(): stats[key][feature] += count
            parsed_numbers.append(meeting.number)
        for number in sorted(parsed_numbers)[:-2]:
            manifest = Manifest(P.raw_dir(wg, number)); manifest.mark_frozen(); manifest.save()
    feature_state = _load(P.state / "features_state.json", {})
    if use_llm: feature_state = _enrich(events, features, feature_state, cfg.extract, result)
    _write_state(events, features, feature_state, result, stats, started)
    if not manual and result.new_events:
        commit_outputs(P.root, ["data/state", "out"], build_commit_message(result.stats_by_meeting))
    return result


def run_pipeline_remap() -> PipelineResult:
    started, result, features, today = time.time(), PipelineResult(), load_features(), time.strftime("%Y-%m-%d")
    events, stats = [], defaultdict(lambda: defaultdict(int))
    for path in sorted(P.parsed.rglob("events.json")):
        payload = _load(path, {})
        if not payload: continue
        events, merge = merge_events(events, map_meeting(payload, features), today, scope={(payload["wg"], payload["meeting"])})
        result.new_events += merge.added
        for key, per in merge.added_by_feature.items():
            for feature, count in per.items(): stats[key][feature] += count
    _write_state(events, features, _load(P.state / "features_state.json", {}), result, stats, started)
    return result


def run_pipeline_enrich() -> PipelineResult:
    started, result, cfg, features = time.time(), PipelineResult(), load_sources(), load_features()
    events, state = _load(P.state / "events.json", []), _load(P.state / "features_state.json", {})
    state = _enrich(events, features, state, cfg.extract, result)
    _write_state(events, features, state, result, defaultdict(dict), started)
    return result

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
