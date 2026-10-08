import time

from ngr import pipeline
from ngr.paths import Paths


def test_first_successful_run_is_visible_to_heartbeat(monkeypatch, tmp_path):
    """The dashboard must not report 'never succeeded' during its first success."""
    seen = {}
    monkeypatch.setattr(pipeline, "P", Paths(tmp_path))
    monkeypatch.setattr(pipeline, "render_all", lambda *args, **kwargs: seen.update(kwargs))

    result = pipeline.PipelineResult()
    pipeline._write_state([], [], {}, result, {}, time.time())

    assert seen["banner"] is None
    assert pipeline.load_runs(tmp_path / "data" / "state" / "run_history.json")[0]["exit_code"] == 0
