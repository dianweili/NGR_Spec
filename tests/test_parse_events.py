import pathlib
from ngr.parse.docx import parse_docx, Document, Block
from ngr.parse.events import extract_events
from ngr.models import Heading

def doc_of(*blocks_and_headings):
    """blocks_and_headings: (kind, text, style) 三元组序列。"""
    d = Document()
    para_i = 0
    for kind, text, style in blocks_and_headings:
        d.blocks.append(Block(kind, text, style, len(d.blocks)))
        if kind == "para":
            if style and style.lower().startswith("heading"):
                d.headings.append(Heading(level=int(style[-1]), text=text, para_index=para_i))
            para_i += 1
    return d

def test_single_agreement_captures_following_paragraphs():
    d = doc_of(("para", "Agreement:", None),
               ("para", "Adopt option 1.", None),
               ("para", "Adopt option 2.", None))
    evs = extract_events(d)
    assert len(evs) == 1
    assert evs[0].kind == "agreement"
    assert "option 1" in evs[0].text_en and "option 2" in evs[0].text_en

def test_block_stops_at_next_marker():
    d = doc_of(("para", "Agreement:", None), ("para", "A", None),
               ("para", "Conclusion:", None), ("para", "B", None))
    evs = extract_events(d)
    assert [e.kind for e in evs] == ["agreement", "conclusion"]
    assert "B" not in evs[0].text_en

def test_block_stops_at_next_heading():
    d = doc_of(("para", "Agreement:", None), ("para", "A", None),
               ("para", "Next topic", "Heading2"), ("para", "B", None))
    evs = extract_events(d)
    assert len(evs) == 1 and "B" not in evs[0].text_en

def test_table_inside_block_is_kept():
    d = doc_of(("para", "Agreement:", None),
               ("table", "| a | b |\n| --- | --- |\n| 1 | 2 |", None))
    assert "| a | b |" in extract_events(d)[0].text_en

def test_marker_inside_table_cell_is_extracted():
    """实测 RAN1#126 有 14 条标记装在"用表格画的框"里（12 agreement + 2 working assumption）。
    只看表格的 markdown 整块会让它们不可见，约 4% 的 agreement 被静默丢弃。"""
    d = Document()
    d.blocks.append(Block("table", "| Agreement: |\n| --- |\n| Adopt X |", None, 0,
                          cell_paras=["Agreement:", "Adopt X"]))
    evs = extract_events(d)
    assert [e.kind for e in evs] == ["agreement"]
    assert evs[0].text_en == "Adopt X"

def test_data_table_without_marker_stays_a_continuation():
    """没有标记的真数据表仍整块并入上一条事件 —— 单元格扫描不得改变这个行为。"""
    d = Document()
    d.blocks.append(Block("para", "Agreement:", None, 0))
    d.blocks.append(Block("para", "see table", None, 1))
    d.blocks.append(Block("table", "| a | b |\n| --- | --- |\n| 1 | 2 |", None, 2,
                          cell_paras=["a", "b", "1", "2"]))
    evs = extract_events(d)
    assert len(evs) == 1 and "| a | b |" in evs[0].text_en

def test_marker_with_parenthetical_qualifier():
    """"Conclusion (RAN#112)" 是引用上级会议结论的真实写法，必须认。"""
    d = doc_of(("para", "Conclusion (RAN#112)", None), ("para", "X", None))
    assert [e.kind for e in extract_events(d)] == ["conclusion"]

def test_table_column_header_is_not_a_marker():
    """Annex E 的表头列名 "Conclusion/Decision" 不是结论。全文仅此一处，
    若为了它放宽正则去认 "/词"，就会凭空多出一条假事件。"""
    d = doc_of(("para", "Conclusion/Decision", None), ("para", "Y", None))
    assert extract_events(d) == []

def test_all_marker_kinds_recognised():
    d = doc_of(("para", "Agreement: x", None), ("para", "Conclusion: y", None),
               ("para", "Working assumption: z", None), ("para", "Observation: w", None),
               ("para", "Proposal: v", None))
    assert [e.kind for e in extract_events(d)] == [
        "agreement", "conclusion", "working_assumption", "observation", "proposal"]

def test_marker_inline_text_is_kept():
    """'Agreement: 直接跟内容' 这种写法，内容不能丢。"""
    d = doc_of(("para", "Agreement: adopt X", None))
    assert "adopt X" in extract_events(d)[0].text_en

def test_heading_path_is_recorded():
    d = doc_of(("para", "Rel-20 Study of 6GR", "Heading1"),
               ("para", "Waveform for 6GR air interface", "Heading2"),
               ("para", "Agreement:", None), ("para", "X", None))
    ev = extract_events(d)[0]
    assert ev.heading_path == ["Rel-20 Study of 6GR", "Waveform for 6GR air interface"]

def test_heading_path_pops_on_shallower_heading():
    d = doc_of(("para", "A", "Heading1"), ("para", "B", "Heading2"),
               ("para", "C", "Heading1"), ("para", "Agreement:", None), ("para", "X", None))
    assert extract_events(d)[0].heading_path == ["C"]

def test_word_agreements_not_matched_mid_sentence():
    """'The agreement was reached' 不是一条 agreement。"""
    d = doc_of(("para", "The agreement was reached last meeting.", None))
    assert extract_events(d) == []

def test_real_fixture_counts():
    doc = parse_docx(pathlib.Path("tests/fixtures/RAN1_126/minutes.docx"))
    evs = extract_events(doc)
    kinds = [e.kind for e in evs]
    assert kinds.count("agreement") == 320
    assert kinds.count("conclusion") == 28
    assert kinds.count("working_assumption") == 13
    # 320/28/13 是在 Task 8 的 _text_of 修复（w:tab/w:br 补分隔符）之后实测的，
    # 且已包含藏在表格单元格里的 14 条（12 agreement + 2 working assumption）。
    assert all(e.text_en.strip() for e in evs), "不允许出现空正文的事件"

def test_real_fixture_6g_events_have_heading_path():
    doc = parse_docx(pathlib.Path("tests/fixtures/RAN1_126/minutes.docx"))
    evs = extract_events(doc)
    sixg = [e for e in evs if "Rel-20 Study of 6GR" in e.heading_path]
    assert sixg, "6GR 子树下应有事件"
