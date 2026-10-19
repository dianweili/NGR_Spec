import subprocess
import os

import pytest

from ngr.extract.backend import CodexExec, LlmError, LlmRateLimited, LlmTimedOut


def fake_popen(stdout="", returncode=0, stderr="", response='{"results":[]}'):
    def _popen(cmd, **kwargs):
        _popen.cmd, _popen.kwargs = cmd, kwargs
        output_path = cmd[cmd.index("--output-last-message") + 1]

        class Process:
            pid = 12345

            def __init__(self):
                self.returncode = returncode

            def communicate(self, input=None, timeout=None):
                _popen.input, _popen.timeout = input, timeout
                if returncode == 0:
                    with open(output_path, "w", encoding="utf-8") as output:
                        output.write(response)
                return stdout, stderr

            def kill(self):
                self.returncode = -9

        return Process()
    return _popen


def test_call_passes_prompt_via_stdin(monkeypatch):
    run = fake_popen()
    monkeypatch.setattr(subprocess, "Popen", run)
    CodexExec("gpt-6-astra", "low").call("PROMPT", output_schema={"type": "object"})
    assert "PROMPT" in run.input
    assert "PROMPT" not in run.cmd


def test_call_uses_safe_required_flags(monkeypatch):
    run = fake_popen()
    monkeypatch.setattr(subprocess, "Popen", run)
    CodexExec("gpt-6-astra", "low").call("x", output_schema={"type": "object"})
    command = run.cmd
    assert command[1] == "exec"
    for flag in ["--ephemeral", "--sandbox", "read-only", "--ignore-user-config", "--ignore-rules", "--output-schema", "--output-last-message"]:
        assert flag in command


def test_finds_desktop_codex_when_path_is_not_configured(monkeypatch, tmp_path):
    old = tmp_path / "OpenAI" / "Codex" / "bin" / "old" / "codex.exe"
    new = tmp_path / "OpenAI" / "Codex" / "bin" / "new" / "codex.exe"
    old.parent.mkdir(parents=True); old.touch()
    new.parent.mkdir(parents=True); new.touch()
    os.utime(new, (new.stat().st_atime + 1, new.stat().st_mtime + 1))
    monkeypatch.delenv("CODEX_CLI_PATH", raising=False)
    monkeypatch.setenv("LOCALAPPDATA", str(tmp_path))
    monkeypatch.setattr("ngr.extract.backend.shutil.which", lambda _: None)
    assert CodexExec._executable() == str(new)


def test_call_sets_model_and_effort(monkeypatch):
    run = fake_popen()
    monkeypatch.setattr(subprocess, "Popen", run)
    CodexExec("gpt-6-astra", "low").call("x", output_schema={"type": "object"})
    assert run.cmd[run.cmd.index("--model") + 1] == "gpt-6-astra"
    assert 'model_reasoning_effort="low"' in run.cmd


def test_call_returns_output_file_text(monkeypatch):
    monkeypatch.setattr(subprocess, "Popen", fake_popen(response='{"results":[]}'))
    result = CodexExec("gpt-6-astra", "low").call("x", output_schema={"type": "object"})
    assert result.text == '{"results":[]}'
    assert result.usage == {} and result.cost_usd == 0.0


def test_nonzero_exit_raises(monkeypatch):
    monkeypatch.setattr(subprocess, "Popen", fake_popen(returncode=1, stderr="boom"))
    with pytest.raises(LlmError, match="boom"):
        CodexExec("gpt-6-astra", "low").call("x", output_schema={"type": "object"})


def test_rate_limit_message_raises_ratelimited(monkeypatch):
    monkeypatch.setattr(subprocess, "Popen", fake_popen(returncode=1, stderr="usage limit reached"))
    with pytest.raises(LlmRateLimited):
        CodexExec("gpt-6-astra", "low").call("x", output_schema={"type": "object"})


def test_timeout_raises_llm_error(monkeypatch):
    class TimeoutProcess:
        pid = 12345
        returncode = None

        def communicate(self, input=None, timeout=None):
            raise subprocess.TimeoutExpired("codex", timeout)

        def kill(self):
            pass

    terminated = []
    monkeypatch.setattr(subprocess, "Popen", lambda *args, **kwargs: TimeoutProcess())
    monkeypatch.setattr(CodexExec, "_terminate_process_tree", staticmethod(lambda proc: terminated.append(proc)))
    with pytest.raises(LlmTimedOut, match="超时"):
        CodexExec("gpt-6-astra", "low").call("x", output_schema={"type": "object"})
    assert len(terminated) == 1
