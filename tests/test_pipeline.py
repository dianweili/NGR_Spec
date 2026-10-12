import json
import time

from ngr import pipeline
from ngr.config import ExtractConfig
from ngr.extract.runner import ExtractStats
from ngr.models import Feature, LineageSegment
from ngr.paths import Paths


def test_enrich_timeout_skips_feature_digest(monkeypatch):
    cfg = ExtractConfig(backend="codex", max_calls_per_run=1, batch_size=1,
                        model_bulk="gpt-6-astra", model_digest="gpt-6-astra")
    monkeypatch.setattr(pipeline, "extract_all", lambda *args, **kwargs: ExtractStats(timed_out=True))
    monkeypatch.setattr(pipeline, "digest_features",
                        lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError("must not digest")))

    result = pipeline.PipelineResult()
    assert pipeline._enrich([], [], {}, cfg, result) == {}
    assert result.exit_code == pipeline.EXIT_LLM
    assert "调用超时" in result.alerts[0]


def test_first_successful_run_is_visible_to_heartbeat(monkeypatch, tmp_path):
    """The dashboard must not report 'never succeeded' during its first success."""
    seen = {}
    monkeypatch.setattr(pipeline, "P", Paths(tmp_path))
    monkeypatch.setattr(pipeline, "render_all", lambda *args, **kwargs: seen.update(kwargs))

    result = pipeline.PipelineResult()
    pipeline._write_state([], [], {}, result, {}, time.time())

    assert seen["banner"] is None
    assert pipeline.load_runs(tmp_path / "data" / "state" / "run_history.json")[0]["exit_code"] == 0


def test_remap_counts_only_events_absent_from_prior_state(monkeypatch, tmp_path):
    """Remap replays the corpus; the run log must not call that a full addition."""
    paths = Paths(tmp_path)
    monkeypatch.setattr(pipeline, "P", paths)
    monkeypatch.setattr(pipeline, "render_all", lambda *args, **kwargs: None)
    feature = Feature("waveform", "Waveform", [LineageSegment(
        era="6G", release="Rel-20", depth="full", agenda=["RAN1:10.2"],
        title_re=None, meetings={"RAN1": (124, None)},
    )])
    monkeypatch.setattr(pipeline, "load_features", lambda: [feature])

    paths.state.mkdir(parents=True)
    (paths.state / "events.json").write_text(json.dumps([
        {"id": "RAN1-124-10.2-a001", "first_seen": "2026-09-01",
         "wg": "RAN1", "meeting": 124, "meeting_suffix": "",
         "agenda_item": "10.2", "kind": "agreement"},
    ]), encoding="utf-8")
    parsed_dir = paths.parsed_dir("RAN1", 124)
    parsed_dir.mkdir(parents=True)
    (parsed_dir / "events.json").write_text(json.dumps({
        "wg": "RAN1", "meeting": 124, "meeting_suffix": "", "events": [
            {"kind": "agreement", "text_en": "old", "agenda_item": "10.2",
             "agenda_title": "Waveform", "heading_path": [], "para_index": 1},
            {"kind": "agreement", "text_en": "new", "agenda_item": "10.2",
             "agenda_title": "Waveform", "heading_path": [], "para_index": 2},
        ],
    }), encoding="utf-8")

    result = pipeline.run_pipeline_remap()

    assert result.new_events == 1
    assert result.stats_by_meeting == {("RAN1", 124, ""): {"waveform": 1}}
    assert pipeline.load_runs(paths.state / "run_history.json")[-1]["new_events"] == 1
    saved = json.loads((paths.state / "events.json").read_text(encoding="utf-8"))
    assert next(event for event in saved if event["id"].endswith("a001"))["first_seen"] == "2026-09-01"
