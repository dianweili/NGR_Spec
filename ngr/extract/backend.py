from __future__ import annotations

import os
from dataclasses import dataclass, field


class LlmError(Exception):
    """OpenAI Responses API 调用失败。"""


class LlmRateLimited(LlmError):
    """OpenAI API 配额或请求速率受限。"""


@dataclass
class CliResult:
    text: str
    usage: dict = field(default_factory=dict)
    cost_usd: float = 0.0


class OpenAIResponses:
    """通过 OpenAI Responses API 调用 ChatGPT 模型。

    API 凭据仅从 ``OPENAI_API_KEY`` 读取；ChatGPT 网页订阅不被写入文件，
    也不被当作本地脚本的凭据。client 参数仅用于测试注入。
    """

    def __init__(self, model: str, effort: str, *, client=None):
        self.model = model
        self.effort = effort
        self._client = client

    def _get_client(self):
        if self._client is not None:
            return self._client
        if not os.environ.get("OPENAI_API_KEY"):
            raise LlmError("未设置 OPENAI_API_KEY，无法调用 OpenAI Responses API")
        try:
            from openai import OpenAI
        except ImportError as exc:
            raise LlmError("未安装 openai SDK；请安装项目依赖后重试") from exc
        self._client = OpenAI()
        return self._client

    def call(self, prompt: str) -> CliResult:
        try:
            response = self._get_client().responses.create(
                model=self.model,
                input=prompt,
                reasoning={"effort": self.effort},
            )
        except LlmError:
            raise
        except Exception as exc:
            status = getattr(exc, "status_code", None)
            if status == 429 or "ratelimit" in type(exc).__name__.lower():
                raise LlmRateLimited(f"OpenAI API 额度受限: {exc}") from exc
            raise LlmError(f"OpenAI Responses API 调用失败: {exc}") from exc

        usage = getattr(response, "usage", None) or {}
        if hasattr(usage, "model_dump"):
            usage = usage.model_dump()
        elif not isinstance(usage, dict):
            usage = dict(usage)

        return CliResult(
            text=getattr(response, "output_text", "") or "",
            usage=usage,
            # Responses API 不返回逐请求账单金额；用量字段由 Budget 记录。
            cost_usd=0.0,
        )
