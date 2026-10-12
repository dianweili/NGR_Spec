"""Print one concise summary-enrichment status line."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
EVENTS_PATH = ROOT / "data" / "state" / "events.json"
LOCK_PATH = ROOT / "data" / "state" / "enrich.lock"


def main() -> None:
    events = json.loads(EVENTS_PATH.read_text(encoding="utf-8"))
    full = [event for event in events if event.get("depth") == "full"]
    summarized = [
        event
        for event in full
        if event.get("llm_status") in {"ok", "needs_review"}
    ]
    review = [event for event in full if event.get("llm_status") == "needs_review"]
    failed = [event for event in full if event.get("llm_status") == "failed"]
    task = "running" if LOCK_PATH.exists() else "idle"
    print(
        f"summarized={len(summarized)}/{len(full)}; "
        f"pending={len(full) - len(summarized)}; "
        f"review={len(review)}; failed={len(failed)}; task={task}"
    )


if __name__ == "__main__":
    main()
