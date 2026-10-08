import json

from ngr.config import ExtractConfig
from ngr.extract.backend import CliResult, LlmRateLimited
from ngr.extract.budget import Budget
from ngr.extract.cache import LlmCache
from ngr.extract.runner import extract_all


CFG = ExtractConfig(backend="openai", max_calls_per_run=10, batch_size=2,
                    model_bulk="gpt-6-astra", model_digest="gpt-6-astra")


def ev(index, depth="full", status="pending"):
    return {"id": f"RAN1-126-10.2-a{index:03d}", "text_en": f"Adopt option {index}.",
            "agenda_title": "Waveform", "depth": depth, "llm_status": status,
            "feature": "waveform", "summary_zh": None, "tags": [], "impact": None}


class FakeCli:
    def __init__(self, replies):
        self.replies, self.calls = list(replies), []

    def call(self, prompt):
        self.calls.append(prompt)
        reply = self.replies.pop(0)
        if isinstance(reply, Exception):
            raise reply
        return CliResult(text=reply, usage={"output_tokens": 5}, cost_usd=0.01)


def reply(ids):
    return json.dumps({"results": [
        {"id": event_id, "summary_zh": "采纳该选项。", "tags": [], "impact": "low"}
        for event_id in ids
    ]})


def test_summaries_are_written_back(tmp_path):
    events = [ev(1), ev(2)]
    cli = FakeCli([reply([event["id"] for event in events])])
    extract_all(events, CFG, cli_factory=lambda model, effort: cli, cache=LlmCache(tmp_path), budget=Budget(10))
    assert events[0]["summary_zh"].startswith("采纳")
    assert events[0]["llm_status"] == "ok"


def test_origin_depth_events_are_skipped(tmp_path):
    events, cli = [ev(1, depth="origin", status="skipped_by_depth")], FakeCli([])
    stats = extract_all(events, CFG, cli_factory=lambda model, effort: cli, cache=LlmCache(tmp_path), budget=Budget(10))
    assert cli.calls == [] and stats.skipped == 1


def test_batches_respect_batch_size(tmp_path):
    events = [ev(index) for index in range(1, 6)]
    cli = FakeCli([reply([event["id"] for event in events[0:2]]), reply([event["id"] for event in events[2:4]]), reply([event["id"] for event in events[4:5]])])
    extract_all(events, CFG, cli_factory=lambda model, effort: cli, cache=LlmCache(tmp_path), budget=Budget(10))
    assert len(cli.calls) == 3


def test_cache_hit_avoids_call(tmp_path):
    events, cache = [ev(1), ev(2)], LlmCache(tmp_path)
    cli1 = FakeCli([reply([event["id"] for event in events])])
    extract_all(events, CFG, cli_factory=lambda model, effort: cli1, cache=cache, budget=Budget(10))
    for event in events:
        event.update(summary_zh=None, llm_status="pending")
    cli2 = FakeCli([])
    extract_all(events, CFG, cli_factory=lambda model, effort: cli2, cache=cache, budget=Budget(10))
    assert cli2.calls == [] and events[0]["summary_zh"].startswith("采纳")


def test_malformed_json_retries_once_then_marks_failed(tmp_path):
    events, cli = [ev(1)], FakeCli(["не json", "still not json"])
    stats = extract_all(events, CFG, cli_factory=lambda model, effort: cli, cache=LlmCache(tmp_path), budget=Budget(10))
    assert len(cli.calls) == 2
    assert events[0]["llm_status"] == "failed" and events[0]["summary_zh"] is None
    assert stats.failed == 1


def test_rate_limit_stops_cleanly_keeping_done_work(tmp_path):
    events = [ev(index) for index in range(1, 5)]
    cli = FakeCli([reply([events[0]["id"], events[1]["id"]]), LlmRateLimited("limit")])
    stats = extract_all(events, CFG, cli_factory=lambda model, effort: cli, cache=LlmCache(tmp_path), budget=Budget(10))
    assert events[0]["llm_status"] == "ok"
    assert events[2]["llm_status"] == "pending"
    assert stats.rate_limited is True


def test_budget_exhaustion_stops_cleanly(tmp_path):
    events = [ev(index) for index in range(1, 7)]
    cli = FakeCli([reply([events[0]["id"], events[1]["id"]])])
    stats = extract_all(events, CFG, cli_factory=lambda model, effort: cli, cache=LlmCache(tmp_path), budget=Budget(1))
    assert stats.budget_exhausted is True
    assert events[4]["llm_status"] == "pending"


def test_hallucination_flags_recorded(tmp_path):
    events = [ev(1)]
    body = json.dumps({"results": [{"id": events[0]["id"], "summary_zh": "参见 R1-2699999。", "tags": [], "impact": "low"}]})
    cli = FakeCli([body])
    extract_all(events, CFG, cli_factory=lambda model, effort: cli, cache=LlmCache(tmp_path), budget=Budget(10))
    assert events[0]["llm_status"] == "needs_review"
    assert events[0]["review_flags"]
