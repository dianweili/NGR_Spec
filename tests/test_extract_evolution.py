import json

import pytest

from ngr.config import ExtractConfig
from ngr.extract.backend import CliResult, LlmRateLimited
from ngr.extract.budget import Budget
from ngr.extract.cache import LlmCache
from ngr.extract.evolution import (current_evolutions, digest_evolutions, evolution_inputs,
                                   parse_response)
from ngr.extract.tasks import SchemaError
from ngr.models import Feature


FEATURE = Feature(slug="rrc", name_zh="RRC", lineage=[])
CFG = ExtractConfig(backend="codex", max_calls_per_run=5, batch_size=1,
                    model_bulk="bulk", model_digest="global", model_meeting_digest="meeting-model")


def event(wg, meeting, identifier, suffix=""):
    return {"wg": wg, "meeting": meeting, "meeting_suffix": suffix, "id": identifier,
            "feature": "rrc", "era": "6G", "summary_zh": "事件摘要"}


def sample():
    events = [event("RAN1", 126, "a"), event("RAN2", 134, "b")]
    state = {"RAN1-126": {"rrc": {"summary": "八月会议", "event_ids": ["a"]}},
             "RAN2-134": {"rrc": {"summary": "五月会议", "event_ids": ["b"]}}}
    periods = {("RAN1", 126, ""): ("2026-08-24", "2026-08-28"),
               ("RAN2", 134, ""): ("2026-05-18", "2026-05-22")}
    return events, state, periods


def reply(meetings):
    return json.dumps({"overview": "有进展", "developments": [{"text": "确认 X", "meetings": meetings}],
                       "open_issues": []}, ensure_ascii=False)


class FakeCli:
    def __init__(self, text):
        self.text, self.calls = text, 0

    def call(self, prompt, *, output_schema=None):
        self.calls += 1
        assert output_schema is not None
        return CliResult(text=self.text)


def test_chronology_uses_dates_not_cross_workgroup_meeting_numbers():
    events, state, periods = sample()
    source = evolution_inputs([FEATURE], events, state, periods)["rrc"]
    assert [row["meeting"] for row in source["meetings"]] == ["RAN2-134", "RAN1-126"]
    del periods[("RAN2", 134, "")]
    source = evolution_inputs([FEATURE], events, state, periods)["rrc"]
    assert [row["meeting"] for row in source["meetings"]] == ["RAN1-126", "RAN2-134"]
    assert source["meetings"][-1]["start"] is None


def test_missing_or_stale_meeting_digest_blocks_partial_synthesis():
    events, state, periods = sample()
    state["RAN2-134"]["rrc"]["event_ids"] = ["outdated"]
    assert evolution_inputs([FEATURE], events, state, periods) == {}
    del state["RAN2-134"]
    assert evolution_inputs([FEATURE], events, state, periods) == {}


def test_invalid_or_missing_citations_are_rejected():
    for refs in ([], ["RAN2-999"]):
        with pytest.raises(SchemaError, match="会议"):
            parse_response(reply(refs), {"RAN2-134"})


def test_checkpoint_resume_and_source_change_invalidation(tmp_path):
    events, meetings, periods = sample()
    inputs = evolution_inputs([FEATURE], events, meetings, periods)
    checkpoints, client = [], FakeCli(reply(["RAN2-134"]))
    cache = LlmCache(tmp_path)
    first = digest_evolutions(inputs, {}, CFG, cli_factory=lambda *_: client, cache=cache,
                              budget=Budget(1), checkpoint=lambda value: checkpoints.append(dict(value)))
    assert client.calls == 1 and len(checkpoints) == 1
    assert list(current_evolutions(inputs, first)) == ["rrc"]
    again = FakeCli("")
    assert digest_evolutions(inputs, first, CFG, cli_factory=lambda *_: again, cache=cache,
                             budget=Budget(1)) == first
    assert again.calls == 0
    meetings["RAN2-134"]["rrc"]["summary"] = "更新后的会议摘要"
    changed = evolution_inputs([FEATURE], events, meetings, periods)
    assert current_evolutions(changed, first) == {}
    newer = FakeCli(reply(["RAN2-134"]))
    result = digest_evolutions(changed, first, CFG, cli_factory=lambda *_: newer,
                               cache=cache, budget=Budget(1))
    assert newer.calls == 1 and result["rrc"]["source_hash"] != first["rrc"]["source_hash"]


def test_rate_limit_stops_without_overwriting_completed_state(tmp_path):
    events, meetings, periods = sample()
    inputs = evolution_inputs([FEATURE], events, meetings, periods)
    class Limited:
        def call(self, *args, **kwargs):
            raise LlmRateLimited("limit")
    problems = []
    state = {"rrc": {"overview": "previous", "source_hash": "old"}}
    result = digest_evolutions(inputs, state, CFG, cli_factory=lambda *_: Limited(),
                               cache=LlmCache(tmp_path), budget=Budget(1), problems=problems)
    assert result == state and len(problems) == 1


def test_interrupted_run_resumes_at_next_feature(tmp_path):
    events, meetings, periods = sample()
    source = evolution_inputs([FEATURE], events, meetings, periods)["rrc"]
    inputs = {"first": source, "second": source}
    saved = []
    class Interrupting:
        def __init__(self): self.calls = 0
        def call(self, *args, **kwargs):
            self.calls += 1
            if self.calls == 2: raise KeyboardInterrupt()
            return CliResult(text=reply(["RAN2-134"]))
    first = Interrupting()
    with pytest.raises(KeyboardInterrupt):
        digest_evolutions(inputs, {}, CFG, cli_factory=lambda *_: first, cache=LlmCache(tmp_path),
                          budget=Budget(2), checkpoint=lambda state: saved.append(dict(state)))
    assert list(saved[-1]) == ["first"]
    second = FakeCli(reply(["RAN1-126"]))
    resumed = digest_evolutions(inputs, saved[-1], CFG, cli_factory=lambda *_: second,
                                cache=LlmCache(tmp_path), budget=Budget(1))
    assert set(resumed) == {"first", "second"} and second.calls == 1
