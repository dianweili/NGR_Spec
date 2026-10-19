"""Print one concise summary-enrichment status line."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from ngr.config import load_features
from ngr.extract.evolution import current_evolutions, evolution_inputs
from ngr.render.site import MEETING_PERIODS
EVENTS_PATH = ROOT / "data" / "state" / "events.json"
MEETING_FEATURE_STATE_PATH = ROOT / "data" / "state" / "meeting_feature_state.json"
LOCK_PATH = ROOT / "data" / "state" / "enrich.lock"
EVOLUTION_PATH = ROOT / "data" / "state" / "feature_evolution_state.json"


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
    try:
        meeting_feature_state = json.loads(MEETING_FEATURE_STATE_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        meeting_feature_state = {}
    targets = {
        f"{event.get('wg')}-{event.get('meeting')}{event.get('meeting_suffix') or ''}:{event.get('feature')}"
        for event in events
        if event.get("era") == "6G" and event.get("feature") and event.get("summary_zh")
    }
    completed = {
        f"{meeting_key}:{slug}"
        for meeting_key, digests in meeting_feature_state.items()
        if isinstance(digests, dict)
        for slug, digest in digests.items()
        if isinstance(digest, dict) and digest.get("summary")
    }
    meeting_completed = len(targets & completed)
    try:
        evolution_state = json.loads(EVOLUTION_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        evolution_state = {}
    sources = evolution_inputs(load_features(), events, meeting_feature_state, MEETING_PERIODS)
    evolution_completed = len(current_evolutions(sources, evolution_state))
    known = {feature.slug for feature in load_features()}
    evolution_targets = {event.get("feature") for event in events if event.get("era") == "6G"
                         and event.get("summary_zh") and event.get("feature") in known}
    evolution_blocked = len(evolution_targets - set(sources))
    task = "running" if LOCK_PATH.exists() else "idle"
    print(
        f"summarized={len(summarized)}/{len(full)}; "
        f"pending={len(full) - len(summarized)}; "
        f"review={len(review)}; failed={len(failed)}; "
        f"meeting_digests={meeting_completed}/{len(targets)}; "
        f"feature_evolution={evolution_completed}/{len(evolution_targets)}; "
        f"evolution_blocked={evolution_blocked}; task={task}"
    )


if __name__ == "__main__":
    main()
