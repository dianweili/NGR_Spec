import logging, pathlib
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
    """实测 RAN1#126 有 15 条标记装在"用表格画的框"里（11 agreement + 2 conclusion + 2 working assumption）。
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

def test_nested_table_marker_is_content_not_a_new_event():
    """CR 封面表里嵌套的子表，其 "Agreement:" 是这份 CR 的标签，不是一条新决议。
    让它开新事件会把一份 CR 拆成两条互相借用正文的 agreement，而事件总数照样对得上 ——
    这类缺陷计数类测试发现不了，所以要专门守住。"""
    d = Document()
    d.blocks.append(Block("para", "Agreement:", None, 0))
    d.blocks.append(Block("para", "The following TP is endorsed.", None, 1))
    # 真数据表的 markdown 本就含自有单元格的文字，所以这里照实构造
    d.blocks.append(Block("table", "| Reason for change | priority rule unclear |", None, 2,
                          cell_paras=["Reason for change", "priority rule unclear"],
                          nested_paras=["Agreement:", "TP body text"]))
    evs = extract_events(d)
    assert len(evs) == 1
    assert "priority rule unclear" in evs[0].text_en
    assert "TP body text" in evs[0].text_en

def test_empty_text_event_is_dropped_with_a_warning(caplog):
    """正文为空的事件（标记后紧跟 heading / 另一个标记 / 文档结尾）丢弃是对的，
    但必须留痕 —— 本项目里静默丢数据比崩溃更严重。"""
    d = Document()
    d.blocks.append(Block("para", "Agreement:", None, 0))
    with caplog.at_level(logging.WARNING):
        assert extract_events(d) == []
    assert "正文为空" in caplog.text

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
    assert kinds.count("agreement") == 319
    assert kinds.count("conclusion") == 28
    assert kinds.count("working_assumption") == 13
    # 319/28/13 是实测值，含藏在表格自有单元格里的 15 条标记
    # （11 agreement + 2 conclusion + 2 working assumption）。
    #
    # agreement 曾一度是 320：当时 CR 封面表里**嵌套子表**的 "Agreement:" 会另开一条事件，
    # 把一份 CR 拆成两条互相借用正文的 agreement。那个 320 是缺陷造成的虚高，不是基准。
    # 现在嵌套子表的段落只当内容，那份 CR 合回一条 —— 详见 extract_events 表格分支第 3 点。
    assert all(e.text_en.strip() for e in evs), "不允许出现空正文的事件"

def test_real_fixture_6g_events_have_heading_path():
    doc = parse_docx(pathlib.Path("tests/fixtures/RAN1_126/minutes.docx"))
    evs = extract_events(doc)
    sixg = [e for e in evs if "Rel-20 Study of 6GR" in e.heading_path]
    assert sixg, "6GR 子树下应有事件"
