import subprocess

import pytest

from ngr.extract.backend import CodexExec, LlmError, LlmRateLimited


def fake_run(stdout="", returncode=0, stderr="", response='{"results":[]}'):
    def _run(cmd, **kwargs):
        _run.cmd, _run.input = cmd, kwargs.get("input")
        output_path = cmd[cmd.index("--output-last-message") + 1]
        if returncode == 0:
            with open(output_path, "w", encoding="utf-8") as output:
                output.write(response)
        return subprocess.CompletedProcess(cmd, returncode, stdout, stderr)
    return _run


def test_call_passes_prompt_via_stdin(monkeypatch):
    run = fake_run()
    monkeypatch.setattr(subprocess, "run", run)
    CodexExec("gpt-6-astra", "low").call("PROMPT", output_schema={"type": "object"})
    assert "PROMPT" in run.input
    assert "PROMPT" not in run.cmd


def test_call_uses_safe_required_flags(monkeypatch):
    run = fake_run()
    monkeypatch.setattr(subprocess, "run", run)
    CodexExec("gpt-6-astra", "low").call("x", output_schema={"type": "object"})
    command = run.cmd
    assert command[:2] == ["codex", "exec"]
    for flag in ["--ephemeral", "--sandbox", "read-only", "--ignore-user-config", "--ignore-rules", "--output-schema", "--output-last-message"]:
        assert flag in command


def test_call_sets_model_and_effort(monkeypatch):
    run = fake_run()
    monkeypatch.setattr(subprocess, "run", run)
    CodexExec("gpt-6-astra", "low").call("x", output_schema={"type": "object"})
    assert run.cmd[run.cmd.index("--model") + 1] == "gpt-6-astra"
    assert 'model_reasoning_effort="low"' in run.cmd


def test_call_returns_output_file_text(monkeypatch):
    monkeypatch.setattr(subprocess, "run", fake_run(response='{"results":[]}'))
    result = CodexExec("gpt-6-astra", "low").call("x", output_schema={"type": "object"})
    assert result.text == '{"results":[]}'
    assert result.usage == {} and result.cost_usd == 0.0


def test_nonzero_exit_raises(monkeypatch):
    monkeypatch.setattr(subprocess, "run", fake_run(returncode=1, stderr="boom"))
    with pytest.raises(LlmError, match="boom"):
        CodexExec("gpt-6-astra", "low").call("x", output_schema={"type": "object"})


def test_rate_limit_message_raises_ratelimited(monkeypatch):
    monkeypatch.setattr(subprocess, "run", fake_run(returncode=1, stderr="usage limit reached"))
    with pytest.raises(LlmRateLimited):
        CodexExec("gpt-6-astra", "low").call("x", output_schema={"type": "object"})


def test_timeout_raises_llm_error(monkeypatch):
    def timeout(cmd, **kwargs):
        raise subprocess.TimeoutExpired(cmd, 600)
    monkeypatch.setattr(subprocess, "run", timeout)
    with pytest.raises(LlmError, match="超时"):
        CodexExec("gpt-6-astra", "low").call("x", output_schema={"type": "object"})
