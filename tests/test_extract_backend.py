import pytest

from ngr.extract.backend import LlmError, LlmRateLimited, OpenAIResponses


class FakeResponse:
    def __init__(self, text='{"ok":true}', usage=None):
        self.output_text = text
        self.usage = usage or {"input_tokens": 2, "output_tokens": 8}


class FakeResponses:
    def __init__(self, answer):
        self.answer, self.calls = answer, []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        if isinstance(self.answer, Exception):
            raise self.answer
        return self.answer


class FakeClient:
    def __init__(self, answer):
        self.responses = FakeResponses(answer)


def test_call_uses_responses_api_with_prompt_input():
    client = FakeClient(FakeResponse())
    OpenAIResponses("gpt-6-astra", "low", client=client).call("PROMPT")
    assert client.responses.calls[0]["input"] == "PROMPT"


def test_call_uses_model_and_reasoning_effort():
    client = FakeClient(FakeResponse())
    OpenAIResponses("gpt-6-astra", "low", client=client).call("x")
    assert client.responses.calls[0]["model"] == "gpt-6-astra"
    assert client.responses.calls[0]["reasoning"] == {"effort": "low"}


def test_missing_api_key_raises(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    with pytest.raises(LlmError, match="OPENAI_API_KEY"):
        OpenAIResponses("gpt-6-astra", "low").call("x")


def test_call_returns_text_and_usage():
    client = FakeClient(FakeResponse(usage={"input_tokens": 2, "output_tokens": 8}))
    result = OpenAIResponses("gpt-6-astra", "low", client=client).call("x")
    assert result.text == '{"ok":true}'
    assert result.cost_usd == 0.0
    assert result.usage["output_tokens"] == 8


def test_api_error_raises():
    client = FakeClient(RuntimeError("boom"))
    with pytest.raises(LlmError, match="boom"):
        OpenAIResponses("gpt-6-astra", "low", client=client).call("x")


def test_rate_limit_raises_ratelimited():
    error = RuntimeError("limit")
    error.status_code = 429
    client = FakeClient(error)
    with pytest.raises(LlmRateLimited):
        OpenAIResponses("gpt-6-astra", "low", client=client).call("x")
