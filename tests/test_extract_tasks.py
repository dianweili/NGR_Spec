import json

import pytest

from ngr.extract.tasks import (
    VALID_IMPACT,
    SchemaError,
    build_summary_prompt,
    hallucination_flags,
    parse_summary_response,
)


BATCH = [
    {"id": "RAN1-126-10.2-a001", "agenda_title": "Waveform",
     "text_en": "Adopt DFT-s-OFDM for uplink in R1-2605180."},
    {"id": "RAN1-126-10.2-a002", "agenda_title": "Waveform", "text_en": "Confirm 480 kHz SCS."},
]


def test_prompt_contains_all_ids_and_texts():
    prompt = build_summary_prompt(BATCH)
    for event in BATCH:
        assert event["id"] in prompt and event["text_en"] in prompt


def test_prompt_forbids_rewriting_original():
    prompt = build_summary_prompt(BATCH)
    assert "不要改写" in prompt or "不得改写" in prompt


def test_prompt_pins_enum_values():
    prompt = build_summary_prompt(BATCH)
    for value in VALID_IMPACT:
        assert value in prompt


def test_parse_valid_response():
    body = json.dumps({"results": [
        {"id": "RAN1-126-10.2-a001", "summary_zh": "采纳上行 DFT-s-OFDM。",
         "tags": ["DFT-s-OFDM"], "impact": "high"},
        {"id": "RAN1-126-10.2-a002", "summary_zh": "确认 480 kHz SCS。", "tags": [], "impact": "medium"},
    ]})
    result = parse_summary_response(body, [event["id"] for event in BATCH])
    assert result["RAN1-126-10.2-a001"]["impact"] == "high"


def test_parse_tolerates_markdown_fence():
    body = '```json\n{"results":[{"id":"RAN1-126-10.2-a001","summary_zh":"x","tags":[],"impact":"low"}]}\n```'
    result = parse_summary_response(body, ["RAN1-126-10.2-a001"])
    assert result["RAN1-126-10.2-a001"]["summary_zh"] == "x"


def test_parse_rejects_invalid_impact():
    body = json.dumps({"results": [{"id": "RAN1-126-10.2-a001", "summary_zh": "x", "tags": [], "impact": "critical"}]})
    with pytest.raises(SchemaError, match="impact"):
        parse_summary_response(body, ["RAN1-126-10.2-a001"])


def test_parse_rejects_unknown_id():
    body = json.dumps({"results": [{"id": "BOGUS", "summary_zh": "x", "tags": [], "impact": "low"}]})
    with pytest.raises(SchemaError, match="id"):
        parse_summary_response(body, ["RAN1-126-10.2-a001"])


def test_parse_rejects_non_json():
    with pytest.raises(SchemaError, match="JSON"):
        parse_summary_response("对不起，我无法处理。", ["x"])


def test_parse_allows_partial_results():
    body = json.dumps({"results": [{"id": "RAN1-126-10.2-a001", "summary_zh": "x", "tags": [], "impact": "low"}]})
    result = parse_summary_response(body, [event["id"] for event in BATCH])
    assert set(result) == {"RAN1-126-10.2-a001"}


def test_flags_tdoc_number_not_in_source():
    flags = hallucination_flags("参见 R1-2699999 的提案。", "Adopt X. See R1-2605180.")
    assert any("R1-2699999" in flag for flag in flags)


def test_no_flag_when_tdoc_present_in_source():
    assert hallucination_flags("参见 R1-2605180。", "See R1-2605180.") == []


def test_flags_number_not_in_source():
    flags = hallucination_flags("确认 960 kHz SCS。", "Confirm 480 kHz SCS.")
    assert any("960" in flag for flag in flags)


def test_does_not_flag_numbers_present_in_source():
    assert hallucination_flags("确认 480 kHz。", "Confirm 480 kHz SCS.") == []


def test_does_not_flag_small_ordinals():
    assert hallucination_flags("有 2 个选项待定。", "Options A and B are FFS.") == []
