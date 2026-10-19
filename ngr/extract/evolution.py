"""Evidence-linked, resumable cross-meeting feature synthesis."""
from __future__ import annotations

import json
import logging
from collections import defaultdict

from ngr.extract.backend import LlmError, LlmRateLimited, LlmTimedOut
from ngr.extract.budget import BudgetExhausted
from ngr.extract.cache import cache_key
from ngr.extract.tasks import SchemaError, strip_fence

log = logging.getLogger(__name__)
VERSION = "feature-evolution-v1"
EFFORT = "medium"
SCHEMA = {
    "type": "object",
    "properties": {
        "overview": {"type": "string"},
        "developments": {"type": "array", "items": {"$ref": "#/$defs/point"}},
        "open_issues": {"type": "array", "items": {"$ref": "#/$defs/point"}},
    },
    "required": ["overview", "developments", "open_issues"],
    "additionalProperties": False,
    "$defs": {"point": {"type": "object", "properties": {
        "text": {"type": "string"},
        "meetings": {"type": "array", "items": {"type": "string"}},
    }, "required": ["text", "meetings"], "additionalProperties": False}},
}


def evolution_inputs(features, events, meeting_state, periods):
    """Only use meeting summaries with matching, currently active 6G events.

    Dates are verified calendar entries, not meeting numbers or first-seen
    dates. Missing dates sort last and are explicitly labelled as unknown.
    """
    active = defaultdict(set)
    metadata = {}
    for event in events:
        if event.get("era") != "6G" or not event.get("summary_zh") or not event.get("feature"):
            continue
        wg, number = event.get("wg"), event.get("meeting")
        if not isinstance(wg, str) or not isinstance(number, int) or not event.get("id"):
            continue
        suffix = event.get("meeting_suffix") or ""
        key = f"{wg}-{number}{suffix}"
        active[(key, event["feature"])].add(event["id"])
        metadata[key] = (wg, number, suffix)
    result = {}
    for feature in features:
        rows = []
        incomplete = False
        for (key, slug), ids in active.items():
            if slug != feature.slug:
                continue
            entry = (meeting_state.get(key) or {}).get(slug) or {}
            if not isinstance(entry, dict) or not entry.get("summary"):
                incomplete = True
                continue
            # A changed event membership makes the meeting digest stale; do
            # not quietly combine a previous digest with a new event set.
            if set(entry.get("event_ids") or []) != ids:
                incomplete = True
                continue
            wg, number, suffix = metadata[key]
            dates = periods.get((wg, number, suffix))
            rows.append({"meeting": key, "label": f"{wg}#{number}{suffix}",
                         "start": dates[0] if dates else None, "end": dates[1] if dates else None,
                         "summary": entry["summary"], "key_points": entry.get("key_points") or [],
                         "open_issues": entry.get("open_issues") or [], "event_ids": sorted(ids)})
        rows.sort(key=lambda row: (row["start"] is None, row["start"] or "", row["meeting"]))
        if rows and not incomplete:
            result[feature.slug] = {"name": feature.name_zh, "meetings": rows}
    return result


def source_hash(source):
    """Hash every source field and prompt version, so edits invalidate output."""
    return cache_key("feature-evolution-source", VERSION, "", json.dumps(
        source, ensure_ascii=False, sort_keys=True, separators=(",", ":")))


def current_evolutions(inputs, state):
    valid = {}
    for slug, source in inputs.items():
        entry = state.get(slug)
        if not isinstance(entry, dict) or entry.get("source_hash") != source_hash(source):
            continue
        try:
            parse_response(json.dumps(entry, ensure_ascii=False),
                           {row["meeting"] for row in source["meetings"]})
        except SchemaError:
            continue
        valid[slug] = entry
    return valid


def build_prompt(source):
    return ("你是 3GPP RAN 协议分析员。根据下列同一特性的 6G 会议综述整理跨会议演进。"
            "材料是已生成的会议级摘要，不是原始协议文本；不可引入材料之外的事实。"
            "按日期理解会议；不同工作组的会议编号不可跨组比较。日期未知时不可推测顺序。"
            "会议只有一场时明确说明不能判断跨会议变化；没有证据时不要编造结论、因果或争议已解决。"
            "输出中文 JSON：overview 为总体进展；developments 为重要技术进展；open_issues 为待决问题。"
            "每条 developments/open_issues 包含 text 和 meetings（支撑该条结论的会议标识数组），"
            "只能引用输入中的 meeting；各数组最多 6 项，没有明确依据就留空。保留英文术语。\n\n"
            + json.dumps(source, ensure_ascii=False, sort_keys=True))


def parse_response(text, allowed_meetings):
    try:
        data = json.loads(strip_fence(text))
    except json.JSONDecodeError as exc:
        raise SchemaError("特性演进不是合法 JSON") from exc
    if not isinstance(data, dict) or not isinstance(data.get("overview"), str) or not data["overview"].strip():
        raise SchemaError("特性演进缺少 overview")
    result = {"overview": data["overview"].strip()}
    for field in ("developments", "open_issues"):
        items = data.get(field)
        if not isinstance(items, list) or len(items) > 6:
            raise SchemaError(f"特性演进 {field} 必须是最多 6 项的数组")
        clean = []
        for item in items:
            if not isinstance(item, dict) or not isinstance(item.get("text"), str) or not item["text"].strip():
                raise SchemaError(f"特性演进 {field} 包含空条目")
            refs = item.get("meetings")
            if not isinstance(refs, list) or not refs or any(not isinstance(ref, str) or ref not in allowed_meetings for ref in refs):
                raise SchemaError(f"特性演进 {field} 引用了缺失或不存在的会议")
            clean.append({"text": item["text"].strip(), "meetings": list(dict.fromkeys(refs))})
        result[field] = clean
    return result


def digest_evolutions(inputs, state, cfg, *, cli_factory, cache, budget, checkpoint=None, problems=None):
    """Save each successful feature immediately; changed inputs are reprocessed."""
    output = dict(state or {})
    cli = cli_factory(cfg.model_meeting_digest, EFFORT)
    for slug, source in inputs.items():
        fingerprint = source_hash(source)
        if slug in current_evolutions({slug: source}, output):
            continue
        prompt = build_prompt(source)
        key = cache_key(f"{cfg.model_meeting_digest}:feature-evolution:{slug}", VERSION, EFFORT, prompt)
        try:
            hit = cache.get(key)
            if hit is not None:
                try:
                    hit = parse_response(json.dumps(hit, ensure_ascii=False),
                                         {row["meeting"] for row in source["meetings"]})
                except SchemaError:
                    log.warning("%s 的特性演进缓存无效，将重新生成", slug)
                    hit = None
            if hit is None:
                entry = budget.reserve(task="feature_evolution")
                try:
                    response = cli.call(prompt, output_schema=SCHEMA)
                    hit = parse_response(response.text, {row["meeting"] for row in source["meetings"]})
                except (LlmError, SchemaError) as exc:
                    budget.record_failure(entry, exc)
                    raise
                budget.record_result(entry, response)
                cache.put(key, hit)
            output[slug] = {**hit, "source_hash": fingerprint,
                            "model": cfg.model_meeting_digest, "effort": EFFORT}
            if checkpoint:
                checkpoint(output)
        except BudgetExhausted:
            break
        except (LlmRateLimited, LlmTimedOut) as exc:
            if problems is not None:
                problems.append(exc)
            log.warning("%s 的特性演进暂停: %s", slug, type(exc).__name__)
            break
        except (LlmError, SchemaError) as exc:
            if problems is not None:
                problems.append(exc)
            log.warning("%s 的特性演进失败: %s", slug, exc)
    return output
