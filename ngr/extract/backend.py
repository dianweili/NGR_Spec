from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
import threading
import time
from dataclasses import dataclass, field
from pathlib import Path


# 摘要批次正常应在一分钟量级结束。过长的超时会在服务无响应时占住
# ChatGPT 会话数小时，且随后重试同一请求没有任何恢复价值。
TIMEOUT_SECONDS = 120
RATE_LIMIT_HINTS = ("usage limit", "rate limit", "too many requests", "429")

SUMMARY_SCHEMA = {
    "type": "object",
    "properties": {
        "results": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "summary_zh": {"type": "string"},
                    "tags": {"type": "array", "items": {"type": "string"}},
                    "impact": {"type": "string", "enum": ["high", "medium", "low"]},
                },
                "required": ["id", "summary_zh", "tags", "impact"],
                "additionalProperties": False,
            },
        },
    },
    "required": ["results"],
    "additionalProperties": False,
}


class LlmError(Exception):
    """Codex CLI 调用失败。"""


class LlmRateLimited(LlmError):
    """ChatGPT/Codex 用量或请求速率受限。"""


class LlmTimedOut(LlmError):
    """调用未在可接受的交互窗口内返回。"""


@dataclass
class CliResult:
    text: str
    usage: dict = field(default_factory=dict)
    cost_usd: float = 0.0


class CodexExec:
    """通过 ``codex exec`` 调用当前 ChatGPT 登录态。

    Prompt 经 stdin 输入，最终消息由 ``--output-last-message`` 单独落盘；
    ``--output-schema`` 约束模型输出，任务层仍会二次校验。模型仅获 read-only
    sandbox，摘要任务不得读写项目文件或执行命令。
    """

    def __init__(self, model: str, effort: str):
        self.model = model
        self.effort = effort

    @staticmethod
    def _executable() -> str:
        """定位 ChatGPT Desktop 随附的 CLI，普通 PowerShell 不必预先配置 PATH。"""
        configured = os.environ.get("CODEX_CLI_PATH")
        if configured:
            return configured
        if found := shutil.which("codex"):
            return found
        local_app_data = os.environ.get("LOCALAPPDATA")
        if local_app_data:
            bundled = Path(local_app_data) / "OpenAI" / "Codex" / "bin"
            candidates = list(bundled.glob("*/codex.exe"))
            if candidates:
                return str(max(candidates, key=lambda path: path.stat().st_mtime))
        # 保留原命令，让未安装场景仍给出系统自己的明确错误信息。
        return "codex"

    def _cmd(self, output: Path, schema: Path | None = None) -> list[str]:
        command = [
            self._executable(), "exec", "--ephemeral", "--sandbox", "read-only",
            "--ignore-user-config", "--ignore-rules",
            "--color", "never", "--model", self.model,
            "--config", f'model_reasoning_effort="{self.effort}"',
            "--output-last-message", str(output),
        ]
        if schema is not None:
            command.extend(("--output-schema", str(schema)))
        return [*command, "-"]

    @staticmethod
    def _terminate_process_tree(proc: subprocess.Popen) -> None:
        """End a timed-out CLI together with descendants that retain its pipes.

        ``codex exec`` can leave its Node child alive after the wrapper is
        killed.  A plain ``subprocess.run(..., timeout=...)`` then waits forever
        while draining a pipe inherited by that orphan.  On Windows ``taskkill
        /T`` is the reliable way to close the complete tree.
        """
        if os.name == "nt":
            try:
                subprocess.run(
                    ["taskkill", "/PID", str(proc.pid), "/T", "/F"], check=False,
                    stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL, timeout=10,
                )
                return
            except (OSError, subprocess.SubprocessError):
                pass
        try:
            proc.kill()
        except OSError:
            pass

    def call(self, prompt: str, *, output_schema: dict | None = None) -> CliResult:
        instructions = "你是纯文本协议摘要器。不得调用工具、读取或写入文件；"
        instructions += ("仅按提供的 JSON schema 返回最终答案。\n\n" if output_schema is not None
                         else "仅返回最终答案，不要附加解释。\n\n")
        instructions += prompt
        with tempfile.TemporaryDirectory(prefix="ngr-codex-") as directory:
            temp_dir = Path(directory)
            schema_path = temp_dir / "output-schema.json"
            output_path = temp_dir / "response.json"
            if output_schema is not None:
                schema_path.write_text(json.dumps(output_schema, ensure_ascii=False), encoding="utf-8")
            popen_kwargs = {
                "stdin": subprocess.PIPE,
                "stdout": subprocess.PIPE,
                "stderr": subprocess.PIPE,
                "text": True,
                "encoding": "utf-8",
            }
            if os.name == "nt":
                popen_kwargs["creationflags"] = getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0)
            else:
                popen_kwargs["start_new_session"] = True
            try:
                proc = subprocess.Popen(
                    self._cmd(output_path, schema_path if output_schema is not None else None),
                    **popen_kwargs,
                )
                completed = threading.Event()
                captured: dict[str, object] = {}

                def collect_output() -> None:
                    try:
                        captured["stdout"], captured["stderr"] = proc.communicate(instructions)
                    except BaseException as exc:  # communicated below on the caller thread
                        captured["error"] = exc
                    finally:
                        completed.set()

                # ``codex exec`` writes the requested final response before it
                # occasionally lingers on analytics or a descendant holding a
                # pipe.  A separate collector keeps both output pipes drained,
                # while the response file is the authoritative completion
                # signal for this non-interactive protocol worker.
                thread = threading.Thread(target=collect_output, daemon=True)
                thread.start()
                deadline = time.monotonic() + TIMEOUT_SECONDS
                text: str | None = None
                while not completed.wait(0.2):
                    try:
                        candidate = output_path.read_text(encoding="utf-8")
                    except OSError:
                        candidate = ""
                    if candidate.strip():
                        text = candidate
                        # Let the normal exit win when it is imminent.  If a
                        # lingering child keeps the pipes open, clean it up;
                        # the final response is already safely on disk.
                        if not completed.wait(1):
                            self._terminate_process_tree(proc)
                            completed.wait(10)
                        break
                    if time.monotonic() >= deadline:
                        self._terminate_process_tree(proc)
                        completed.wait(10)
                        raise LlmTimedOut(f"codex exec 超时（{TIMEOUT_SECONDS}s）")

                if text is not None:
                    return CliResult(text=text)
                if error := captured.get("error"):
                    if isinstance(error, subprocess.TimeoutExpired):
                        self._terminate_process_tree(proc)
                        raise LlmTimedOut(f"codex exec 超时（{TIMEOUT_SECONDS}s）") from error
                    raise error
                stdout = str(captured.get("stdout") or "")
                stderr = str(captured.get("stderr") or "")
            except OSError as exc:
                raise LlmError(f"无法启动 codex exec: {exc}") from exc

            if proc.returncode != 0:
                error = (stderr or stdout or "").strip()
                if any(hint in error.lower() for hint in RATE_LIMIT_HINTS):
                    raise LlmRateLimited(f"ChatGPT/Codex 用量受限: {error}")
                raise LlmError(f"codex exec 退出码 {proc.returncode}: {error}")
            try:
                text = output_path.read_text(encoding="utf-8")
            except OSError as exc:
                raise LlmError("codex exec 没有生成最终响应文件") from exc
        return CliResult(text=text)
