import pathlib, zipfile, io
from ngr.parse.docx import parse_docx

def make_docx(body_xml: str) -> bytes:
    """构造最小 docx：只需要 word/document.xml。"""
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        z.writestr("word/document.xml",
            '<?xml version="1.0"?><w:document '
            'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
            f'<w:body>{body_xml}</w:body></w:document>')
    return buf.getvalue()

def para(text, style=None):
    s = f'<w:pPr><w:pStyle w:val="{style}"/></w:pPr>' if style else ""
    return f'<w:p>{s}<w:r><w:t>{text}</w:t></w:r></w:p>'

def test_extracts_paragraph_text():
    doc = parse_docx(make_docx(para("Hello world")))
    assert doc.paragraphs == ["Hello world"]

def test_joins_multiple_runs_in_one_paragraph():
    xml = '<w:p><w:r><w:t>Agree</w:t></w:r><w:r><w:t>ment</w:t></w:r></w:p>'
    assert parse_docx(make_docx(xml)).paragraphs == ["Agreement"]

def test_tab_and_break_become_separators():
    """w:tab / w:br 是独立元素，不补分隔符会把两侧文本焊死。
    实测 RAN1#126 有 3795 处 tab、48 处 br 落在两段无空白的文本之间。"""
    xml = ('<w:p><w:r><w:t>Opening of the meeting</w:t><w:tab/><w:t>5</w:t></w:r></w:p>'
           '<w:p><w:r><w:t>OLLA enabled</w:t><w:br/><w:t>Target BLER 10%</w:t></w:r></w:p>'
           '<w:p><w:r><w:t>Case 1</w:t><w:cr/><w:t>Case 2</w:t></w:r></w:p>')
    assert parse_docx(make_docx(xml)).paragraphs == [
        "Opening of the meeting\t5", "OLLA enabled\nTarget BLER 10%",
        "Case 1\nCase 2"]

def test_alternate_content_is_not_counted_twice():
    """Word 对同一个图形给出 mc:Choice 与 mc:Fallback 两份等价表示。
    两份都收会让文本原样重复一遍 —— 实测 Annex A-2 的日程表图示被拼成
    "RAN1 Brk 2RAN1 Brk 2RAN1 Brk 1RAN1 Brk 1..."。"""
    mc = "http://schemas.openxmlformats.org/markup-compatibility/2006"
    xml = (f'<w:p xmlns:mc="{mc}"><w:r><mc:AlternateContent>'
           '<mc:Choice Requires="wps"><w:p><w:r><w:t>Brk 2</w:t></w:r></w:p></mc:Choice>'
           '<mc:Fallback><w:p><w:r><w:t>Brk 2</w:t></w:r></w:p></mc:Fallback>'
           '</mc:AlternateContent></w:r><w:r><w:t>Annex A-2</w:t></w:r></w:p>')
    assert parse_docx(make_docx(xml)).paragraphs == ["Brk 2\nAnnex A-2"]

def test_nested_paragraphs_are_separated_from_surrounding_text():
    """文本框里的 w:p 各自成段，前后都要断开，否则与外层文本焊成一串
    （实测 "RAN1 MainAnnex A-2:"）。"""
    xml = ('<w:p><w:r><w:t>before</w:t></w:r>'
           '<w:r><w:p><w:r><w:t>boxed</w:t></w:r></w:p></w:r>'
           '<w:r><w:t>after</w:t></w:r></w:p>')
    assert parse_docx(make_docx(xml)).paragraphs == ["before\nboxed\nafter"]

def test_tab_stop_definition_is_not_a_tab_character():
    """<w:pPr><w:tabs><w:tab/></w:tabs></w:pPr> 是制表位定义，与制表符同名但不是字符。"""
    xml = ('<w:p><w:pPr><w:tabs><w:tab w:val="left" w:pos="720"/></w:tabs></w:pPr>'
           '<w:r><w:t>Agreement:</w:t></w:r></w:p>')
    assert parse_docx(make_docx(xml)).paragraphs == ["Agreement:"]

def test_cell_text_flattens_whitespace_for_markdown():
    """单元格里的换行必须压成空格，否则一个单元格就能撑断整张表的行结构。"""
    xml = ('<w:tbl><w:tr><w:tc><w:p><w:r><w:t>line1</w:t><w:br/><w:t>line2</w:t></w:r>'
           '</w:p></w:tc></w:tr></w:tbl>')
    blk = parse_docx(make_docx(xml)).blocks[0]
    assert blk.kind == "table"
    assert blk.text.splitlines()[0] == "| line1 line2 |"

def test_headings_carry_level_and_index():
    doc = parse_docx(make_docx(para("Top", "Heading1") + para("body") + para("Sub", "Heading2")))
    assert [(h.level, h.text) for h in doc.headings] == [(1, "Top"), (2, "Sub")]
    assert doc.headings[1].para_index == 2

def test_non_heading_styles_are_not_headings():
    doc = parse_docx(make_docx(para("x", "BodyText")))
    assert doc.headings == []

def test_table_becomes_markdown_block_in_document_order():
    tbl = ('<w:tbl>'
           '<w:tr><w:tc><w:p><w:r><w:t>SCS</w:t></w:r></w:p></w:tc>'
           '<w:tc><w:p><w:r><w:t>BW</w:t></w:r></w:p></w:tc></w:tr>'
           '<w:tr><w:tc><w:p><w:r><w:t>30</w:t></w:r></w:p></w:tc>'
           '<w:tc><w:p><w:r><w:t>100</w:t></w:r></w:p></w:tc></w:tr>'
           '</w:tbl>')
    doc = parse_docx(make_docx(para("Agreement:") + tbl + para("after")))
    kinds = [b.kind for b in doc.blocks]
    assert kinds == ["para", "table", "para"]
    assert doc.blocks[1].text == "| SCS | BW |\n| --- | --- |\n| 30 | 100 |"

def test_table_cell_with_multiple_paragraphs_is_joined():
    tbl = ('<w:tbl><w:tr><w:tc>'
           '<w:p><w:r><w:t>a</w:t></w:r></w:p><w:p><w:r><w:t>b</w:t></w:r></w:p>'
           '</w:tc></w:tr></w:tbl>')
    assert "a b" in parse_docx(make_docx(tbl)).blocks[0].text

def test_pipe_in_cell_is_escaped():
    tbl = '<w:tbl><w:tr><w:tc><w:p><w:r><w:t>a|b</w:t></w:r></w:p></w:tc></w:tr></w:tbl>'
    assert r"a\|b" in parse_docx(make_docx(tbl)).blocks[0].text

def test_empty_paragraphs_are_dropped():
    assert parse_docx(make_docx('<w:p></w:p>' + para("x"))).paragraphs == ["x"]

def test_real_fixture_structure():
    """实测 RAN1#126 v010 的确切数字 —— 3GPP 换纪要模板时这里第一个炸。

    注意 paragraphs 只数 body 的**直接子**段落：表格内的段落归到 table 块，
    不计入这里。（计划初稿写的 7803 是用正则匹配 <w:p> 量的，而正则处理不了
    表格内嵌套的 <w:p>，那个数字本身就是错的。）"""
    doc = parse_docx(pathlib.Path("tests/fixtures/RAN1_126/minutes.docx"))
    assert len(doc.paragraphs) == 5061
    assert len(doc.headings) == 83
    assert any(h.text == "Rel-20 Study of 6GR" and h.level == 1 for h in doc.headings)
    assert any(h.text == "Waveform for 6GR air interface" for h in doc.headings)

def test_real_fixture_marker_counts():
    doc = parse_docx(pathlib.Path("tests/fixtures/RAN1_126/minutes.docx"))
    assert sum(1 for p in doc.paragraphs if p.startswith("Agreement")) == 308
    assert sum(1 for p in doc.paragraphs if p.startswith("Conclusion")) == 26
    assert sum(1 for p in doc.paragraphs if p.lower().startswith("working assumption")) == 11

def test_real_fixture_table_wrapped_markers():
    """首个单元格就是标记的表格 —— 这些是"用表格画的框"，框里装着一条决议。
    parse 层必须把单元格段落带出来，否则 Task 9 看不到这些标记，约 4% 的
    agreement 会被静默丢弃。

    实测：12 张表格的自有单元格里带标记、共 15 条（11 agreement + 2 conclusion
    + 2 working assumption）；其中 11 张的**首个**单元格就是标记，即下面断言的 8/2/1。"""
    doc = parse_docx(pathlib.Path("tests/fixtures/RAN1_126/minutes.docx"))
    tables = [b for b in doc.blocks if b.kind == "table"]
    assert len(tables) == 82
    lead = [t.cell_paras[0] for t in tables if t.cell_paras]
    assert sum(1 for x in lead if x.startswith("Agreement")) == 8
    assert sum(1 for x in lead if x.startswith("Conclusion")) == 2
    assert sum(1 for x in lead if x.lower().startswith("working assumption")) == 1
    # 注意 tables 只含 body 的**直接子**表格。嵌套子表不单独成块，其段落进
    # nested_paras 而非 cell_paras —— 两者语义不同：自有单元格里的标记是一条决议
    # 本身，而嵌套子表出现在 CR 封面表里，它的 "Agreement:" 只是这份 CR 的标签。
    # 实测全文只有 1 张表有子表，正是那张 CR 封面表。
