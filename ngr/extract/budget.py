from __future__ import annotations

import json
import time
from pathlib import Path

from ngr.extract.backend import CliResult


class BudgetExhausted(Exception):
    """本轮的调用上限已用尽。"""


class Budget:
    """限制单轮 LLM 调用并记录可审计的用量。"""

    def __init__(self, max_calls: int):
        self.max_calls = max_calls
        self.calls = 0
        self.cost_usd = 0.0
        self.input_tokens = 0
        self.output_tokens = 0
        self._entries: list[dict] = []

    def check(self) -> None:
        if self.calls >= self.max_calls:
            raise BudgetExhausted(
                f"已达本次运行上限 {self.max_calls} 次调用，剩余工作留到下次"
            )

    def reserve(self, task: str = "") -> dict:
        """在发起外部请求前占用一个调用名额。

        额度按实际请求数而非成功响应数限制，所以格式错误后的重试也必须
        消耗一个名额；这能保证 ``max_calls_per_run`` 是严格上限。
        """
        self.check()
        self.calls += 1
        entry = {
            "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "task": task,
            "status": "started",
            "cost_usd": 0.0,
            "usage": {},
        }
        self._entries.append(entry)
        return entry

    def record_result(self, entry: dict, result: CliResult) -> None:
        self.cost_usd += result.cost_usd
        usage = result.usage or {}
        self.input_tokens += sum(
            int(usage.get(key, 0))
            for key in ("input_tokens", "cache_read_input_tokens", "cache_creation_input_tokens")
        )
        self.output_tokens += int(usage.get("output_tokens", 0))
        entry.update(status="completed", cost_usd=result.cost_usd, usage=usage)

    def record_failure(self, entry: dict, error: Exception) -> None:
        entry.update(status="failed", error=str(error)[:500])

    def spend(self, result: CliResult, task: str = "") -> None:
        """兼容一次性记账调用；新代码应先 ``reserve`` 再 ``record_result``。"""
        entry = self.reserve(task)
        self.record_result(entry, result)

    def log(self, path: Path) -> None:
        """追加 usage JSONL；cost 是列表价换算的用量代理，并非订阅账单。"""
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as file:
            for entry in self._entries:
                file.write(json.dumps(entry, ensure_ascii=False) + "\n")
        self._entries.clear()
