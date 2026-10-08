import io, json, pathlib, pytest, shutil, zipfile
from ngr.models import Meeting
from ngr.parse.runner import parse_meeting, write_parsed, ParseError

FIX126 = pathlib.Path("tests/fixtures/RAN1_126")
MTG = Meeting(wg="RAN1", number=126, suffix="", url="https://x/TSGR1_126/")


def _zip_bytes(entries: dict[str, bytes]) -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        for name, data in entries.items():
            z.writestr(name, data)
    return buf.getvalue()

def test_parse_meeting_on_fixture(tmp_path):
    shutil.copytree(FIX126, tmp_path / "raw")
    p = parse_meeting(tmp_path / "raw", MTG, agenda_required=True)
    # 实测值，按 kind 拆开写以便出错时一眼看出是哪类变了。
    # 注意 observation 也在 events 里 —— 旧公式 320+29+13 漏了它，
    # 而 320/29 本身又是缺陷期的虚高值（详见 Task 9 的 test_real_fixture_counts 注释）。
    assert len(p.events) == 319 + 28 + 13 + 9
    assert p.unmatched_ratio < 0.20
    assert p.minutes_version == 10

def test_events_carry_agenda_item_when_aligned(tmp_path):
    shutil.copytree(FIX126, tmp_path / "raw")
    p = parse_meeting(tmp_path / "raw", MTG, agenda_required=True)
    # agenda_item 这个键**总是存在**，未对齐时值为 None ——
    # 所以 .get(k, "") 返回的是 None 而不是 ""，直接 .startswith 会抛 AttributeError。
    sixg = [e for e in p.events if (e.get("agenda_item") or "").startswith("10")]
    assert sixg, "6GR 议程项下应有事件"
    assert all("heading_path" in e and "text_en" in e for e in p.events)

def test_events_keep_heading_path_when_agenda_absent(tmp_path):
    """5G-A 老会议没有 agenda.csv：事件照常产出，只是没有 agenda_item。"""
    raw = tmp_path / "raw"; raw.mkdir()
    shutil.copy(FIX126 / "minutes.docx", raw / "minutes.docx")
    p = parse_meeting(raw, MTG, agenda_required=False)
    assert len(p.events) == 319 + 28 + 13 + 9   # 对齐与否不改变事件数
    assert all(e["agenda_item"] is None for e in p.events)
    assert any(e["heading_path"] for e in p.events)

def test_missing_agenda_warns_but_does_not_raise(tmp_path):
    """实测 agenda_csv_since 只表示最早出现（RAN2 #131 有缺口），
    缺 agenda.csv 是正常现象，不得以退出码 2 中止整条管线。"""
    raw = tmp_path / "raw"; raw.mkdir()
    shutil.copy(FIX126 / "minutes.docx", raw / "minutes.docx")
    p = parse_meeting(raw, MTG, agenda_required=True)
    assert p.events and any("agenda.csv" in w for w in p.warnings)

def test_missing_minutes_raises(tmp_path):
    raw = tmp_path / "raw"; raw.mkdir()
    with pytest.raises(ParseError, match="minutes"):
        parse_meeting(raw, MTG, agenda_required=False)

def test_zero_headings_raises(tmp_path, monkeypatch):
    shutil.copytree(FIX126, tmp_path / "raw")
    from ngr.parse import runner
    monkeypatch.setattr(runner, "parse_docx",
                        lambda p: type("D", (), {"headings": [], "blocks": [], "paragraphs": []})())
    with pytest.raises(ParseError, match="heading"):
        parse_meeting(tmp_path / "raw", MTG, agenda_required=True)

def test_zero_events_raises(tmp_path, monkeypatch):
    shutil.copytree(FIX126, tmp_path / "raw")
    from ngr.parse import runner
    monkeypatch.setattr(runner, "extract_events", lambda doc: [])
    with pytest.raises(ParseError, match="事件"):
        parse_meeting(tmp_path / "raw", MTG, agenda_required=True)

def test_no_eligible_heading_also_raises(tmp_path, monkeypatch):
    """**一条都没参与对齐**时门禁也必须开火。

    这条与下面那条走的是 unmatched_ratio 的**两个不同分支**：这里 by_heading 与
    unaligned 都空（total==0，比如 heading 全是 Annex 结构性标题），
    下面那条是 unaligned 撑满（total==1）。total==0 曾经返回 0.0 被门禁放行 ——
    比正常值 12.2% 还好看，是本项目遇到过最隐蔽的一次静默失败。
    """
    shutil.copytree(FIX126, tmp_path / "raw")
    from ngr.parse import runner
    from ngr.parse.align import Alignment
    from ngr.models import Heading
    degenerate = Alignment(by_heading={}, unaligned=[],
                           skipped=[Heading(1, "Annex A-1: List of Tdocs", 0)])
    assert degenerate.unmatched_ratio == 1.0
    monkeypatch.setattr(runner, "align", lambda a, h: degenerate)
    with pytest.raises(ParseError, match="未对齐"):
        parse_meeting(tmp_path / "raw", MTG, agenda_required=True)

def test_high_unmatched_ratio_raises(tmp_path, monkeypatch):
    shutil.copytree(FIX126, tmp_path / "raw")
    from ngr.parse import runner
    from ngr.parse.align import Alignment
    from ngr.models import Heading
    bad = Alignment(by_heading={}, unaligned=[Heading(1, "x", 0)])
    monkeypatch.setattr(runner, "align", lambda a, h: bad)
    with pytest.raises(ParseError, match="未对齐"):
        parse_meeting(tmp_path / "raw", MTG, agenda_required=True)

def test_missing_body_raises_parse_error_with_context(tmp_path):
    """word/document.xml 存在但没有 <w:body> 时，docx.py 原本裸抛
    TypeError: 'NoneType' object is not iterable —— 对定位毫无帮助。
    runner 必须捕获并补上是哪个文件解析失败的上下文。"""
    raw = tmp_path / "raw"; raw.mkdir()
    doc_xml = (
        b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        b'<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        b'</w:document>'
    )
    (raw / "minutes.docx").write_bytes(_zip_bytes({"word/document.xml": doc_xml}))
    with pytest.raises(ParseError, match="minutes.docx"):
        parse_meeting(raw, MTG, agenda_required=False)


@pytest.mark.parametrize("label, data", [
    ("missing word/document.xml (KeyError)",
     _zip_bytes({"word/other.xml": b"<x/>"})),
    ("not a zip at all (BadZipFile)",
     b"this is not a zip file"),
    ("corrupt XML content (ParseError)",
     _zip_bytes({"word/document.xml": b"<w:document><unclosed"})),
])
def test_malformed_docx_raises_parse_error_with_context(tmp_path, label, data):
    """zip 缺 word/document.xml、docx 被二次 zip 包裹（表现为顶层找不到该条目，
    与"缺文件"同一种失败）、zip 本身不是合法 zip、XML 内容本身损坏 ——
    这些原本分别裸抛 KeyError / zipfile.BadZipFile / ElementTree.ParseError，
    都不带"是哪个文件解析失败"的上下文。runner 必须统一包成带路径的 ParseError。"""
    raw = tmp_path / "raw"; raw.mkdir()
    (raw / "minutes.docx").write_bytes(data)
    with pytest.raises(ParseError, match="minutes.docx"):
        parse_meeting(raw, MTG, agenda_required=False)


def test_write_parsed_is_deterministic(tmp_path):
    shutil.copytree(FIX126, tmp_path / "raw")
    p = parse_meeting(tmp_path / "raw", MTG, agenda_required=True)
    a = write_parsed(p, tmp_path / "out1").read_bytes()
    b = write_parsed(p, tmp_path / "out2").read_bytes()
    assert a == b, "同一输入必须产出逐字节相同的 JSON（幂等性前提）"
    assert json.loads(a)["wg"] == "RAN1"


def test_write_parsed_preserves_meeting_suffix(tmp_path):
    shutil.copytree(FIX126, tmp_path / "raw")
    special = Meeting(wg="RAN1", number=126, suffix="b", url="https://x/TSGR1_126b/")
    payload = json.loads(write_parsed(parse_meeting(tmp_path / "raw", special, agenda_required=True),
                                      tmp_path / "out").read_text(encoding="utf-8"))
    assert payload["meeting"] == 126 and payload["meeting_suffix"] == "b"
