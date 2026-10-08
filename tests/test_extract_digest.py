import json

import pytest

from ngr.config import ExtractConfig
from ngr.extract.backend import CliResult
from ngr.extract.budget import Budget
from ngr.extract.cache import LlmCache
from ngr.extract.digest import build_feature_prompt, build_legacy_chunks, digest_features, parse_feature_response
from ngr.extract.tasks import SchemaError
from ngr.models import Feature, LineageSegment


CFG = ExtractConfig(backend="codex", max_calls_per_run=20, batch_size=40,
                    model_bulk="gpt-6-astra", model_digest="gpt-6-astra")


def segment(era, depth):
    return LineageSegment(era=era, release="Rel-19" if era == "5G-A" else "Rel-20", depth=depth,
                          agenda=[], title_re="(?i)x", meetings={"RAN1": (110, None)})


ISAC = Feature(slug="isac", name_zh="ISAC 通感一体", lineage=[segment("5G-A", "origin"), segment("6G", "full")])
WAVE = Feature(slug="waveform", name_zh="波形", lineage=[segment("6G", "full")])
FEAT_REPLY = json.dumps({"stage": "收敛中", "summary": "正在收敛。", "open_issues": ["波形未定"]})


def event(index, era="6G", meeting=126, summary="摘要", text="Adopt X.", feature="isac"):
    return {"id": f"RAN1-{meeting}-10.8-a{index:03d}", "wg": "RAN1", "meeting": meeting, "era": era,
            "feature": feature, "kind": "agreement", "text_en": text, "summary_zh": summary,
            "depth": "full" if era == "6G" else "origin", "agenda_title": "ISAC"}


class FakeCli:
    def __init__(self, replies):
        self.replies, self.calls = list(replies), []

    def call(self, prompt, *, output_schema=None):
        self.calls.append((prompt, output_schema))
        return CliResult(text=self.replies.pop(0), usage={}, cost_usd=0.02)


def test_feature_prompt_uses_summaries_and_pins_stage_enum():
    prompt = build_feature_prompt(ISAC, [event(1, summary="采纳 X")])
    assert "采纳 X" in prompt and "ISAC 通感一体" in prompt
    assert all(stage in prompt for stage in ("未启动", "讨论中", "收敛中", "已定稿"))


def test_legacy_prompt_uses_english_original_not_summary():
    prompt = build_feature_prompt(ISAC, [], [event(1, era="5G-A", meeting=118, summary=None, text="Rel-19 decision.")])
    assert "Rel-19 decision." in prompt


def test_parse_feature_response_checks_schema():
    assert parse_feature_response(FEAT_REPLY)["stage"] == "收敛中"
    with pytest.raises(SchemaError, match="stage"):
        parse_feature_response(json.dumps({"stage": "快好了", "summary": "s", "open_issues": []}))
    with pytest.raises(SchemaError, match="summary"):
        parse_feature_response(json.dumps({"stage": "讨论中", "open_issues": []}))


def test_legacy_chunks_group_by_meeting_count():
    events = [event(index, "5G-A", meeting) for index, meeting in enumerate((112, 114, 116, 118, 120, 122))]
    chunks = build_legacy_chunks(events, meetings_per_chunk=4)
    assert len(chunks) == 2
    assert {item["meeting"] for item in chunks[0]} == {112, 114, 116, 118}
    assert build_legacy_chunks([], meetings_per_chunk=4) == []


def test_digest_writes_stage_and_legacy_summary(tmp_path):
    legacy = [event(index, "5G-A", 112 + index, summary=None, text=f"Legacy {index}.") for index in range(3)]
    cli = FakeCli(["Rel-19 阶段只做了信道建模。", FEAT_REPLY])
    state = digest_features([ISAC], legacy + [event(9)], {}, CFG,
                            cli_factory=lambda model, effort: cli, cache=LlmCache(tmp_path), budget=Budget(10))
    assert state["isac"]["stage"] == "收敛中"
    assert "信道建模" in state["isac"]["legacy_summary"]
    assert cli.calls[1][1] is not None


def test_digest_reuses_cached_legacy_and_skips_without_events(tmp_path):
    legacy, cache = [event(1, "5G-A", 112, summary=None, text="Legacy.")], LlmCache(tmp_path)
    first = FakeCli(["历史归纳。", FEAT_REPLY])
    digest_features([ISAC], legacy + [event(9)], {}, CFG, cli_factory=lambda model, effort: first, cache=cache, budget=Budget(10))
    second = FakeCli([FEAT_REPLY])
    state = digest_features([ISAC, WAVE], legacy + [event(9)], {}, CFG,
                            cli_factory=lambda model, effort: second, cache=cache, budget=Budget(10))
    assert len(second.calls) == 0
    assert state["isac"]["legacy_summary"] == "历史归纳。"
    assert state["isac"]["stage"] == "收敛中"
