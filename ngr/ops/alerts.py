from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import date, datetime
from pathlib import Path


MAX_HISTORY = 100
STALE_DAYS = 7


@dataclass
class RunRecord:
    started: str
    duration_s: float
    new_events: int
    llm_calls: int
    exit_code: int
    message: str = ""


def load_runs(path: Path) -> list[dict]:
    path = Path(path)
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    return data if isinstance(data, list) else []


def append_run(path: Path, record: RunRecord) -> None:
    path = Path(path)
    runs = load_runs(path)
    runs.append(asdict(record))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(runs[-MAX_HISTORY:], ensure_ascii=False, indent=2), encoding="utf-8")


def _as_date(value: str) -> date | None:
    try:
        return datetime.fromisoformat(value).date()
    except (TypeError, ValueError):
        return None


def heartbeat_banner(runs: list[dict], today: str, *, stale_days: int = STALE_DAYS) -> str | None:
    """连续 stale_days 天没有成功运行时提示，避免静默停更。"""
    today_date = _as_date(today) or date.today()
    successes = [
        parsed for parsed in (_as_date(run.get("started", "")) for run in runs if run.get("exit_code") == 0)
        if parsed is not None
    ]
    if not successes:
        return f"⚠️ **调度可能已失效** —— 从未记录到成功运行（检查日期 {today}）"
    latest = max(successes)
    gap = (today_date - latest).days
    if gap >= stale_days:
        return f"⚠️ **调度可能已失效** —— 距上次成功运行已 {gap} 天（{latest}）。请检查计划任务与 `logs/`。"
    return None


def build_banner(alerts: list[str], runs: list[dict], today: str) -> str | None:
    parts = list(alerts)
    heartbeat = heartbeat_banner(runs, today)
    if heartbeat:
        parts.append(heartbeat)
    if not parts:
        return None
    return "\n".join(part if part.startswith("⚠️") else f"⚠️ {part}" for part in parts)
