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
MEETINGS_PER_CHUNK = 4

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
        budget.check()
        response = cli.call(build_feature_prompt(feature, [], chunk))
        text = response.text.strip()
        if not text:
            raise LlmError("5G-A 历史归纳返回空文本")
        budget.spend(response, task="legacy_chunk")
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
    budget.check()
    response = cli.call(LEGACY_SYSTEM + "\n\n把下面几段归纳合并成一段连贯的中文：\n\n" + merged)
    text = response.text.strip()
    if not text:
        raise LlmError("5G-A 历史合并返回空文本")
    budget.spend(response, task="legacy_merge")
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
                budget.check()
                response = cli.call(build_feature_prompt(feature, six_events), output_schema=FEATURE_SCHEMA)
                budget.spend(response, task="feature_digest")
                parsed = parse_feature_response(response.text)
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
