from __future__ import annotations

import json
import re


PROMPT_VERSION = "v1"
VALID_IMPACT = ("high", "medium", "low")
VALID_STAGE = ("未启动", "讨论中", "收敛中", "已定稿")

TDOC_RE = re.compile(r"\bR[1-4]-\d{6,7}\b")
NUM_RE = re.compile(r"\d{3,}")


class SchemaError(Exception):
    """模型输出未符合约定 JSON schema。"""


SUMMARY_SYSTEM = f"""你在为 3GPP 6G（Rel-20）RAN 协议跟踪工具生成中文摘要。

规则：
1. 只依据我给你的英文原文，**不要改写原文**，也不要补充原文里没有的信息。
2. 不确定的地方宁可不写，绝不猜测。
3. 摘要 2–3 句，讲清“定了什么”，保留关键技术术语的英文原词。
4. tags 取 0–4 个技术关键词（英文原词）。
5. impact 只能是 {list(VALID_IMPACT)} 之一。

只输出 JSON，不要任何解释文字，格式：
{{"results": [{{"id": "...", "summary_zh": "...", "tags": ["..."], "impact": "high"}}]}}
"""


def build_summary_prompt(batch: list[dict]) -> str:
    parts = [SUMMARY_SYSTEM, "", "以下是需要摘要的条目：", ""]
    for event in batch:
        parts.extend((
            f"--- id: {event['id']}",
            f"议程: {event.get('agenda_title', '')}",
            "原文:",
            event["text_en"],
            "",
        ))
    return "\n".join(parts)


def strip_fence(text: str) -> str:
    value = text.strip()
    if value.startswith("```"):
        value = re.sub(r"^```[a-zA-Z]*\s*", "", value)
        value = re.sub(r"\s*```$", "", value)
    return value.strip()


def parse_summary_response(text: str, expected_ids: list[str]) -> dict[str, dict]:
    try:
        data = json.loads(strip_fence(text))
    except json.JSONDecodeError as exc:
        raise SchemaError(f"响应不是合法 JSON: {text[:160]}") from exc
    if not isinstance(data, dict):
        raise SchemaError("JSON 根节点必须是对象")

    results = data.get("results")
    if not isinstance(results, list):
        raise SchemaError("JSON 缺少 results 数组")

    allowed, output = set(expected_ids), {}
    for item in results:
        if not isinstance(item, dict):
            raise SchemaError("results 中存在非对象条目")
        event_id = item.get("id")
        if event_id not in allowed:
            raise SchemaError(f"返回了未请求的 id: {event_id!r}")
        if event_id in output:
            raise SchemaError(f"重复返回 id: {event_id!r}")
        impact = item.get("impact")
        if impact not in VALID_IMPACT:
            raise SchemaError(f"{event_id} 的 impact 非法: {impact!r}")
        summary = item.get("summary_zh")
        if not isinstance(summary, str) or not summary.strip():
            raise SchemaError(f"{event_id} 的 summary_zh 为空")
        tags = item.get("tags", [])
        if not isinstance(tags, list):
            raise SchemaError(f"{event_id} 的 tags 不是数组")
        output[event_id] = {
            "summary_zh": summary.strip(),
            "tags": [str(tag) for tag in tags][:4],
            "impact": impact,
        }
    return output


def hallucination_flags(summary_zh: str, text_en: str) -> list[str]:
    """标出摘要凭空出现的 TDoc 编号与关键数字，供人工核对。"""
    flags = []
    for tdoc in set(TDOC_RE.findall(summary_zh)):
        if tdoc not in text_en:
            flags.append(f"摘要中的 {tdoc} 未出现在原文")
    source_numbers = set(NUM_RE.findall(text_en))
    for number in set(NUM_RE.findall(summary_zh)):
        if number not in source_numbers:
            flags.append(f"摘要中的数字 {number} 未出现在原文")
    return flags
