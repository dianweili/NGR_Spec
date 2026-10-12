import pytest

from ngr import cli
from ngr.pipeline import EXIT_GIT, EXIT_LLM, EXIT_OK, EXIT_PARSE, PipelineResult
from ngr.parse.runner import ParseError


def test_run_forwards_flags(monkeypatch):
    seen = {}
    monkeypatch.setattr(cli, "run_pipeline", lambda **kwargs: seen.update(kwargs) or PipelineResult())
    assert cli.main(["run", "--no-llm", "--wg", "RAN1", "--force"]) == EXIT_OK
    assert seen == {"wgs": ["RAN1"], "use_llm": False, "force": True}


def test_backfill_forwards_range(monkeypatch):
    seen = {}
    monkeypatch.setattr(cli, "run_pipeline", lambda **kwargs: seen.update(kwargs) or PipelineResult())
    cli.main(["backfill", "--wg", "RAN1", "--from", "112", "--to", "127"])
    assert seen["wgs"] == ["RAN1"] and seen["meetings"] == (112, 127)


def test_error_and_special_commands(monkeypatch, capsys):
    monkeypatch.setattr(cli, "run_pipeline", lambda **kwargs: (_ for _ in ()).throw(ParseError("bad")))
    assert cli.main(["run"]) == EXIT_PARSE
    monkeypatch.setattr(cli, "build_lineage_report", lambda: "# 血统命中对照表")
    assert cli.main(["lineage-report"]) == EXIT_OK
    assert "血统" in capsys.readouterr().out
    monkeypatch.setattr(cli, "run_doctor", lambda **kwargs: 1)
    assert cli.main(["doctor"]) == 1


def test_remap_enrich_and_argparse_error(monkeypatch):
    monkeypatch.setattr(cli, "run_remap", lambda: PipelineResult(exit_code=EXIT_GIT))
    assert cli.main(["remap"]) == EXIT_GIT
    monkeypatch.setattr(cli, "run_enrich", lambda: PipelineResult(exit_code=EXIT_LLM))
    assert cli.main(["enrich"]) == EXIT_LLM
    with pytest.raises(SystemExit):
        cli.main([])


def test_enrich_forwards_temporary_batch_overrides(monkeypatch):
    seen = {}
    monkeypatch.setattr(cli, "run_enrich", lambda **kwargs: seen.update(kwargs) or PipelineResult())
    assert cli.main(["enrich", "--max-calls", "20", "--batch-size", "10"]) == EXIT_OK
    assert seen == {"max_calls": 20, "batch_size": 10}
