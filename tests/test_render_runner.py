from ngr.models import Feature, LineageSegment
from ngr.render.runner import render_all


def _feature():
    return Feature("rrc", "6GR RRC", [LineageSegment(
        era="6G", release="Rel-20", depth="full", agenda=["RAN2:10.3.2"],
        title_re=None, meetings={"RAN2": (132, None)},
    )])


def _event(**overrides):
    event = {
        "id": "RAN2-132-10.3.2-a001", "wg": "RAN2", "meeting": 132,
        "meeting_suffix": "", "agenda_item": "10.3.2", "agenda_title": "Control plane",
        "kind": "agreement", "era": "6G", "release": "Rel-20", "depth": "full",
        "feature": "rrc", "text_en": "Adopt a model.", "summary_zh": None,
        "tags": [], "impact": None, "llm_status": "pending", "first_seen": "2026-10-09",
        "meeting_end": None, "source": {"minutes_version": 1, "para": 1},
    }
    event.update(overrides)
    return event


def test_report_filename_uses_first_seen_when_meeting_end_is_missing(tmp_path):
    render_all([_event()], [_feature()], {}, tmp_path, generated="2026-10-10")

    assert (tmp_path / "reports" / "2026-10-09-RAN2-132.md").exists()
    assert not (tmp_path / "reports" / "2026-10-10-RAN2-132.md").exists()
