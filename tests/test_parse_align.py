from ngr.models import AgendaItem, Heading
from ngr.parse.align import align, normalize


def A(item, title):
    return AgendaItem(item=item, title=title)


def H(level, text, i=0):
    return Heading(level=level, text=text, para_index=i)


def test_normalize_strips_case_punct_and_space():
    assert normalize("  Waveform for 6GR  air-interface! ") == normalize(
        "waveform for 6gr airinterface"
    )


def test_exact_match():
    ag = [A("10.2", "Waveform for 6GR air interface")]
    al = align(ag, [H(2, "Waveform for 6GR air interface", 5)])
    assert al.by_heading[5].item == "10.2"
    assert al.unmatched_ratio == 0.0


def test_fuzzy_match_above_threshold():
    ag = [A("10.3", "Channel coding and modulation for 6GR interface")]
    al = align(ag, [H(2, "Channel coding and modulation for 6GR  interface", 7)])
    assert al.by_heading[7].item == "10.3"


def test_fuzzy_below_threshold_is_rejected():
    ag = [A("10.2", "Waveform for 6GR air interface")]
    al = align(ag, [H(2, "Totally different topic", 3)])
    assert 3 not in al.by_heading
    assert al.unaligned[0].text == "Totally different topic"


def test_depth_mismatch_is_rejected():
    """标题对得上但层级对不上 —— 拒绝，这是模板变动的信号。"""
    ag = [A("10.2", "Waveform")]  # depth 2
    al = align(ag, [H(4, "Waveform", 1)])  # Heading4
    assert 1 not in al.by_heading


def test_depth_match_allows_one_level_offset():
    """纪要常把 Heading1 用在 depth-1 议程项上，允许 ±1 的偏移。"""
    ag = [A("10.2", "Waveform")]
    al = align(ag, [H(3, "Waveform", 1)])
    assert al.by_heading[1].item == "10.2"


def test_same_title_headings_share_one_agenda_item():
    """同名 heading 是同一个议程项的重复出现（分组标题 + 同名子标题），两处都要对上。
    实测 RAN1#126 的 "GNSS resilient NR-NTN operation" 就是 L2/L3 各一次。"""
    ag = [A("10.2", "Waveform")]
    al = align(ag, [H(2, "Waveform", 1), H(3, "Waveform", 9)])
    assert len(al.by_heading) == 2
    assert {v.item for v in al.by_heading.values()} == {"10.2"}
    assert al.unaligned == []


def test_different_titles_cannot_claim_same_item():
    """标题不同的两个小节不得抢同一个议程项 —— used 守的是这个。
    "Waveforms" 与 "Waveform" 的 difflib 相似度 0.94，会越过模糊阈值。"""
    ag = [A("10.2", "Waveform")]
    al = align(ag, [H(2, "Waveform", 1), H(2, "Waveforms", 9)])
    assert len(al.by_heading) == 1
    assert [h.text for h in al.unaligned] == ["Waveforms"]


def test_unmatched_ratio_computed():
    ag = [A("1", "Opening")]
    al = align(ag, [H(1, "Opening", 0), H(1, "Mystery", 1)])
    assert al.unmatched_ratio == 0.5


def test_empty_agenda_marks_all_unaligned():
    al = align([], [H(1, "X", 0)])
    assert al.unmatched_ratio == 1.0 and al.by_heading == {}


def test_real_fixture_alignment():
    import pathlib

    from ngr.parse.agenda import parse_agenda
    from ngr.parse.docx import parse_docx

    ag = parse_agenda(pathlib.Path("tests/fixtures/RAN1_126/agenda.csv").read_bytes())
    doc = parse_docx(pathlib.Path("tests/fixtures/RAN1_126/minutes.docx"))
    al = align(ag, doc.headings)
    assert al.unmatched_ratio < 0.20, f"未对齐率过高: {al.unmatched_ratio:.0%}"
    # 9 条 Annex 标题被跳过而非判为未对齐；若把它们算进去，未对齐率是 23%，
    # 探针常年报警等于没有探针。
    assert len(al.skipped) == 9
    assert all(h.text.lower().startswith("annex") for h in al.skipped)
    items = {v.item for v in al.by_heading.values()}
    assert "10" in items and "10.2" in items
