from __future__ import annotations

import json
import logging
import re

from ngr.config import ExtractConfig
from ngr.extract.backend import LlmError, LlmRateLimited
from ngr.extract.budget import BudgetExhausted
from ngr.extract.cache import cache_key
from ngr.extract.tasks import PROMPT_VERSION, SchemaError, VALID_STAGE, strip_fence
from ngr.models import Feature


log = logging.getLogger(__name__)
EFFORT_DIGEST = "high"
# A meeting digest only consolidates already-validated event summaries from a
# single meeting.  It does not need the slower, cross-meeting reasoning used
# by the global feature and legacy overviews; low effort keeps the 82-item
# backfill responsive for a ChatGPT subscription session.
EFFORT_MEETING_DIGEST = "low"
MEETINGS_PER_CHUNK = 4
MEETING_FEATURE_PROMPT_VERSION = "meeting-feature-v1"

FEATURE_SCHEMA = {
    "type": "object",
    "properties": {
        "stage": {"type": "string", "enum": list(VALID_STAGE)},
        "summary": {"type": "string"},
        "open_issues": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["stage", "summary", "open_issues"],
    "additionalProperties": False,
}

MEETING_FEATURE_SCHEMA = {
    "type": "object",
    "properties": {
        "summary": {"type": "string"},
        "key_points": {"type": "array", "items": {"type": "string"}},
        "open_issues": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["summary", "key_points", "open_issues"],
    "additionalProperties": False,
}


def _one_line(text: str) -> str:
    """保留原文，只将喂给模型的逐行 blob 压成单行。"""
    return re.sub(r"\s+", " ", text).strip()


def _meeting_label(event: dict) -> str:
    return f"{event['meeting']}{event.get('meeting_suffix') or ''}"


LEGACY_SYSTEM = """你在归纳一个 3GPP 特性在 5G-A（Rel-18/19）阶段的历史脉络。

只依据下面给出的英文 agreement 原文，说明这个阶段实际定下了什么、哪些问题没有做充分或被推迟，以及为什么会延续到 6G。
用中文写 3–6 句，保留关键技术术语的英文原词。不要编造原文里没有的结论。直接输出正文，不要 JSON，不要标题。"""

FEATURE_SYSTEM = f"""你在为一个 3GPP 6G 特性写“当前进展”综述。

只输出 JSON，不要任何解释文字：
{{"stage": "<{'|'.join(VALID_STAGE)}>", "summary": "<3-5 句中文综述>", "open_issues": ["<尚未解决的争议点>", "..."]}}

stage 只能取给定的四个值之一。open_issues 取 0–6 条，没有就给空数组。只依据给出的材料，不要编造。"""

MEETING_FEATURE_SYSTEM = """你在为一次 3GPP RAN 会议中的一个 6G（Rel-20）特性写进展综述。

输入是该会议已核验的逐条中文事件摘要。只归纳这一次会议中的材料；不得把会议外的历史、行业常识或推测写入。

只输出 JSON，不要任何解释文字：
{"summary": "<2-4 句中文综述，说明本会议推进了什么以及其协议含义>",
 "key_points": ["<本会议已明确的关键技术结论>", "..."],
 "open_issues": ["<本会议仍待后续处理的问题>", "..."]}

key_points 和 open_issues 各取 0–6 条。没有明确结论或未决问题时输出空数组。保留关键英文技术术语；不确定的内容宁可不写。"""


def build_legacy_chunks(legacy_events: list[dict], meetings_per_chunk: int = MEETINGS_PER_CHUNK) -> list[list[dict]]:
    """按会议数分块，避免将大量冻结历史一次性塞入模型上下文。"""
    if not legacy_events:
        return []
    meetings = sorted({event["meeting"] for event in legacy_events})
    return [
        [event for event in legacy_events if event["meeting"] in set(meetings[index:index + meetings_per_chunk])]
        for index in range(0, len(meetings), meetings_per_chunk)
    ]


def build_feature_prompt(feature: Feature, six_events: list[dict], legacy_chunk: list[dict] | None = None) -> str:
    if legacy_chunk is not None:
        parts = [LEGACY_SYSTEM, "", f"特性：{feature.name_zh}", ""]
        for event in sorted(legacy_chunk, key=lambda item: (item["meeting"], item.get("meeting_suffix") or "", item["id"])):
            parts.extend((f"[{event['wg']}#{_meeting_label(event)}] {event['kind']}", event["text_en"], ""))
        return "\n".join(parts)

    parts = [FEATURE_SYSTEM, "", f"特性：{feature.name_zh}", "", "6GR 阶段的进展："]
    for event in sorted(six_events, key=lambda item: (item["meeting"], item.get("meeting_suffix") or "", item["id"])):
        parts.append(f"- [{event['wg']}#{_meeting_label(event)}] {event.get('summary_zh') or event['text_en'][:200]}")
    return "\n".join(parts)


def parse_feature_response(text: str) -> dict:
    try:
        data = json.loads(strip_fence(text))
    except json.JSONDecodeError as exc:
        raise SchemaError(f"特性综述不是合法 JSON: {text[:160]}") from exc
    if not isinstance(data, dict):
        raise SchemaError("特性综述 JSON 根节点必须是对象")
    stage = data.get("stage")
    if stage not in VALID_STAGE:
        raise SchemaError(f"stage 非法: {stage!r}，只能是 {list(VALID_STAGE)}")
    summary = data.get("summary")
    if not isinstance(summary, str) or not summary.strip():
        raise SchemaError("缺少 summary")
    issues = data.get("open_issues", [])
    if not isinstance(issues, list):
        raise SchemaError("open_issues 不是数组")
    return {"stage": stage, "summary": summary.strip(), "open_issues": [str(item) for item in issues][:6]}


def meeting_state_key(wg: str, meeting: int, suffix: str = "") -> str:
    """The stable key shared by persisted meeting digests and the web UI."""
    return f"{wg}-{meeting}{suffix}"


def build_meeting_feature_prompt(feature: Feature, events: list[dict]) -> str:
    """Build one bounded, source-traceable meeting-feature prompt.

    Only completed 6G event summaries are admitted by the caller.  This keeps
    the prompt much smaller than re-sending raw minutes and avoids blending
    intentional 5G-A ``origin`` records into a Rel-20 meeting update.
    """
    if not events:
        raise ValueError("会议特性综述需要至少一条已摘要事件")
    first = events[0]
    parts = [
        MEETING_FEATURE_SYSTEM,
        "",
        f"会议：{first['wg']}#{_meeting_label(first)}",
        f"特性：{feature.name_zh}",
        "",
        "本会议事件摘要：",
    ]
    for event in sorted(events, key=lambda item: item["id"]):
        parts.append(f"- [{event['id']}] {_one_line(event['summary_zh'])}")
    return "\n".join(parts)


def parse_meeting_feature_response(text: str) -> dict:
    try:
        data = json.loads(strip_fence(text))
    except json.JSONDecodeError as exc:
        raise SchemaError(f"会议特性综述不是合法 JSON: {text[:160]}") from exc
    if not isinstance(data, dict):
        raise SchemaError("会议特性综述 JSON 根节点必须是对象")
    summary = data.get("summary")
    if not isinstance(summary, str) or not summary.strip():
        raise SchemaError("会议特性综述缺少 summary")
    output = {"summary": summary.strip()}
    for field in ("key_points", "open_issues"):
        items = data.get(field)
        if not isinstance(items, list):
            raise SchemaError(f"会议特性综述 {field} 不是数组")
        output[field] = [str(item).strip() for item in items if str(item).strip()][:6]
    return output


def _legacy_summary(feature: Feature, legacy: list[dict], cli, cache, budget) -> str | None:
    pieces: list[str] = []
    for chunk in build_legacy_chunks(legacy):
        blob = "\n".join(
            f"{event['id']}:{_one_line(event['text_en'])}"
            for event in sorted(chunk, key=lambda item: item["id"])
        )
        key = cache_key(f"legacy:{feature.slug}", PROMPT_VERSION, EFFORT_DIGEST, blob)
        hit = cache.get(key)
        if hit is not None:
            pieces.append(hit["text"])
            continue
        entry = budget.reserve(task="legacy_chunk")
        try:
            response = cli.call(build_feature_prompt(feature, [], chunk))
        except (LlmError, LlmRateLimited) as exc:
            budget.record_failure(entry, exc)
            raise
        text = response.text.strip()
        if not text:
            error = LlmError("5G-A 历史归纳返回空文本")
            budget.record_failure(entry, error)
            raise error
        budget.record_result(entry, response)
        cache.put(key, {"text": text})
        pieces.append(text)

    if not pieces:
        return None
    if len(pieces) == 1:
        return pieces[0]
    merged = "\n\n".join(pieces)
    key = cache_key(f"legacy-merge:{feature.slug}", PROMPT_VERSION, EFFORT_DIGEST, merged)
    hit = cache.get(key)
    if hit is not None:
        return hit["text"]
    entry = budget.reserve(task="legacy_merge")
    try:
        response = cli.call(LEGACY_SYSTEM + "\n\n把下面几段归纳合并成一段连贯的中文：\n\n" + merged)
    except (LlmError, LlmRateLimited) as exc:
        budget.record_failure(entry, exc)
        raise
    text = response.text.strip()
    if not text:
        error = LlmError("5G-A 历史合并返回空文本")
        budget.record_failure(entry, error)
        raise error
    budget.record_result(entry, response)
    cache.put(key, {"text": text})
    return text


def digest_features(features: list[Feature], events: list[dict], feat_state: dict,
                    cfg: ExtractConfig, *, cli_factory, cache, budget) -> dict:
    """更新已有事件特性的进展、未决问题及一次性 5G-A 血统综述。"""
    cli = cli_factory(cfg.model_digest, EFFORT_DIGEST)
    output = dict(feat_state)
    for feature in features:
        mine = [event for event in events if event.get("feature") == feature.slug]
        if not mine:
            continue
        six_events = [event for event in mine if event.get("era") == "6G"]
        legacy = [event for event in mine if event.get("era") == "5G-A"]
        entry = dict(output.get(feature.slug) or {})
        try:
            if feature.has_legacy and legacy:
                legacy_summary = _legacy_summary(feature, legacy, cli, cache, budget)
                if legacy_summary:
                    entry["legacy_summary"] = legacy_summary

            blob = "\n".join(
                f"{event['id']}:{_one_line(event.get('summary_zh') or event['text_en'][:200])}"
                for event in sorted(six_events, key=lambda item: item["id"])
            )
            key = cache_key(f"feature:{feature.slug}", PROMPT_VERSION, EFFORT_DIGEST, blob)
            hit = cache.get(key)
            if hit is not None:
                entry.update(hit)
            else:
                budget_entry = budget.reserve(task="feature_digest")
                try:
                    response = cli.call(build_feature_prompt(feature, six_events), output_schema=FEATURE_SCHEMA)
                except (LlmError, LlmRateLimited) as exc:
                    budget.record_failure(budget_entry, exc)
                    raise
                budget.record_result(budget_entry, response)
                try:
                    parsed = parse_feature_response(response.text)
                except SchemaError as exc:
                    budget.record_failure(budget_entry, exc)
                    raise
                cache.put(key, parsed)
                entry.update(parsed)
        except (BudgetExhausted, LlmRateLimited) as exc:
            log.info("%s 的综述未完成（%s），下次继续", feature.slug, type(exc).__name__)
            if entry:
                output[feature.slug] = entry
            break
        except (SchemaError, LlmError) as exc:
            log.warning("%s 的综述失败: %s", feature.slug, exc)
        if entry:
            output[feature.slug] = entry
    return output


def digest_meeting_features(features: list[Feature], events: list[dict], meeting_state: dict,
                            cfg: ExtractConfig, *, cli_factory, cache, budget,
                            problems: list[Exception] | None = None,
                            checkpoint=None) -> dict:
    """Write one digest for each populated 6G meeting-feature combination.

    The input is deliberately restricted to events that already have a Chinese
    summary.  ``origin`` records have no event-level translation by design;
    feeding their often very large English minutes here would silently turn a
    small, incremental digest task into a costly historical reprocessing job.
    """
    feature_by_slug = {feature.slug: feature for feature in features}
    groups: dict[tuple[str, int, str, str], list[dict]] = {}
    for event in events:
        slug = str(event.get("feature") or "")
        if (event.get("era") != "6G" or not event.get("summary_zh")
                or slug not in feature_by_slug):
            continue
        wg, meeting = str(event.get("wg") or ""), event.get("meeting")
        if not isinstance(meeting, int) or not wg:
            continue
        suffix = str(event.get("meeting_suffix") or "")
        groups.setdefault((wg, meeting, suffix, slug), []).append(event)

    output = {str(key): dict(value) for key, value in (meeting_state or {}).items()
              if isinstance(value, dict)}
    cli = cli_factory(cfg.model_meeting_digest, EFFORT_MEETING_DIGEST)
    # Prioritize the most recent meeting.  Within one meeting, features retain
    # the order supplied in features.yaml rather than accidental slug ordering.
    priority = {feature.slug: index for index, feature in enumerate(features)}
    ordered_groups = sorted(
        groups.items(),
        key=lambda item: (-item[0][1], item[0][0], item[0][2], priority[item[0][3]], item[0][3]),
    )
    for (wg, meeting, suffix, slug), group in ordered_groups:
        key = meeting_state_key(wg, meeting, suffix)
        per_meeting = dict(output.get(key) or {})
        event_ids = [event["id"] for event in sorted(group, key=lambda item: item["id"])]
        blob = "\n".join(
            f"{event['id']}:{_one_line(event['summary_zh'])}"
            for event in sorted(group, key=lambda item: item["id"])
        )
        cache_id = cache_key(f"meeting-feature:{key}:{slug}", MEETING_FEATURE_PROMPT_VERSION,
                             EFFORT_MEETING_DIGEST, blob)
        try:
            hit = cache.get(cache_id)
            if hit is None:
                budget_entry = budget.reserve(task="meeting_feature_digest")
                try:
                    response = cli.call(build_meeting_feature_prompt(feature_by_slug[slug], group),
                                        output_schema=MEETING_FEATURE_SCHEMA)
                except (LlmError, LlmRateLimited) as exc:
                    budget.record_failure(budget_entry, exc)
                    raise
                budget.record_result(budget_entry, response)
                try:
                    hit = parse_meeting_feature_response(response.text)
                except SchemaError as exc:
                    budget.record_failure(budget_entry, exc)
                    raise
                cache.put(cache_id, hit)
            entry = dict(hit)
            entry["event_ids"] = event_ids
            entry["event_count"] = len(event_ids)
            per_meeting[slug] = entry
            output[key] = per_meeting
            if checkpoint is not None:
                checkpoint(output)
        except BudgetExhausted as exc:
            log.info("%s#%s%s / %s 的会议综述未完成（%s），下次继续", wg, meeting,
                     suffix, slug, type(exc).__name__)
            break
        except LlmRateLimited as exc:
            if problems is not None:
                problems.append(exc)
            log.info("%s#%s%s / %s 的会议综述未完成（%s），下次继续", wg, meeting,
                     suffix, slug, type(exc).__name__)
            break
        except (SchemaError, LlmError) as exc:
            if problems is not None:
                problems.append(exc)
            log.warning("%s#%s%s / %s 的会议综述失败: %s", wg, meeting, suffix, slug, exc)
    return output
