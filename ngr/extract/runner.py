from __future__ import annotations

import logging
from dataclasses import dataclass

from ngr.config import ExtractConfig
from ngr.extract.backend import LlmError, LlmRateLimited, SUMMARY_SCHEMA
from ngr.extract.budget import BudgetExhausted
from ngr.extract.cache import cache_key
from ngr.extract.tasks import (
    PROMPT_VERSION,
    SchemaError,
    build_summary_prompt,
    hallucination_flags,
    parse_summary_response,
)


log = logging.getLogger(__name__)
EFFORT_BULK = "low"


@dataclass
class ExtractStats:
    summarized: int = 0
    cached: int = 0
    skipped: int = 0
    failed: int = 0
    rate_limited: bool = False
    budget_exhausted: bool = False


def _apply(event: dict, payload: dict) -> None:
    flags = hallucination_flags(payload["summary_zh"], event["text_en"])
    event["summary_zh"] = payload["summary_zh"]
    event["tags"] = payload["tags"]
    event["impact"] = payload["impact"]
    if flags:
        event["review_flags"] = flags
        event["llm_status"] = "needs_review"
    else:
        event.pop("review_flags", None)
        event["llm_status"] = "ok"


def extract_all(events: list[dict], cfg: ExtractConfig, *, cli_factory, cache, budget) -> ExtractStats:
    """补全 full 深度事件的逐条摘要，失败不影响英文原文或后续渲染。"""
    stats = ExtractStats()
    pending: list[tuple[str, dict]] = []
    for event in events:
        if event.get("depth") != "full":
            stats.skipped += 1
            continue
        if event.get("llm_status") in ("ok", "needs_review"):
            continue
        key = cache_key(cfg.model_bulk, PROMPT_VERSION, EFFORT_BULK, event["text_en"])
        hit = cache.get(key)
        if hit is not None:
            _apply(event, hit)
            stats.cached += 1
            continue
        pending.append((key, event))

    if not pending:
        return stats

    cli = cli_factory(cfg.model_bulk, EFFORT_BULK)
    for offset in range(0, len(pending), cfg.batch_size):
        chunk = pending[offset:offset + cfg.batch_size]
        batch = [event for _, event in chunk]
        ids = [event["id"] for event in batch]
        prompt = build_summary_prompt(batch)
        result = None
        for attempt in (1, 2):
            try:
                entry = budget.reserve(task="summary")
            except BudgetExhausted:
                stats.budget_exhausted = True
                log.info("配额用尽，剩余 %d 条留待下次", len(pending) - offset)
                return stats
            try:
                response = cli.call(
                    prompt if attempt == 1 else prompt + "\n\n上一次回复不是合法 JSON，请只输出 JSON。",
                    output_schema=SUMMARY_SCHEMA,
                )
                budget.record_result(entry, response)
                result = parse_summary_response(response.text, ids)
                break
            except LlmRateLimited as exc:
                budget.record_failure(entry, exc)
                stats.rate_limited = True
                log.warning("额度受限，本次运行到此为止；已完成的结果已保存")
                return stats
            except (SchemaError, LlmError) as exc:
                budget.record_failure(entry, exc)
                log.warning("批次 %d 第 %d 次失败: %s", offset // cfg.batch_size, attempt, exc)

        if result is None:
            for event in batch:
                event["llm_status"] = "failed"
                stats.failed += 1
            continue

        for key, event in chunk:
            payload = result.get(event["id"])
            if payload is None:
                continue
            _apply(event, payload)
            cache.put(key, payload)
            stats.summarized += 1
    return stats
