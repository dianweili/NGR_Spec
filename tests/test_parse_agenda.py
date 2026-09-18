import pathlib
import logging

from ngr.parse.agenda import parse_agenda

def test_parse_agenda_basic():
    data = b'"1","Opening of the meeting"\n"10","Rel-20 Study of 6GR"\n"10.2","Waveform for 6GR air interface"\n'
    items = parse_agenda(data)
    assert [i.item for i in items] == ["1", "10", "10.2"]
    assert items[2].title == "Waveform for 6GR air interface"
    assert items[2].depth == 2

def test_parse_agenda_strips_whitespace_in_item_number():
    """实测 RAN1#126 的 agenda.csv 里有 '10.4.1 ' 这种带尾空格的条目。"""
    items = parse_agenda(b'"10.4.1 ","Operation in idle mode"\n')
    assert items[0].item == "10.4.1"
    assert items[0].depth == 3

def test_parse_agenda_keeps_quotes_inside_title():
    items = parse_agenda(b'"9.1.1","CSI compression (\xe2\x80\x9cCase 0\xe2\x80\x9d)"\n')
    assert "Case 0" in items[0].title

def test_parse_agenda_skips_blank_lines():
    assert len(parse_agenda(b'"1","A"\n\n"2","B"\n')) == 2

def test_parse_agenda_on_real_fixture():
    data = pathlib.Path("tests/fixtures/RAN1_126/agenda.csv").read_bytes()
    items = parse_agenda(data)
    by_item = {i.item: i.title for i in items}
    assert by_item["10"] == "Rel-20 Study of 6GR"
    assert by_item["10.2"] == "Waveform for 6GR air interface"
    assert by_item["9"] == "Release 20 NR"     # Rel-20 ≠ 6G，两者并列
    assert len(items) > 50


def test_utf8_agenda_decodes_without_warning(caplog):
    """正常 UTF-8 文件不得产生任何告警 —— 探针的价值来自平时沉默。"""
    data = '"9.1","波形 Waveform"\n'.encode("utf-8")
    with caplog.at_level(logging.WARNING):
        items = parse_agenda(data)
    assert items[0].title == "波形 Waveform"
    assert caplog.text == ""


def test_non_utf8_agenda_warns_instead_of_silently_mangling(caplog):
    """非 UTF-8 文件会被解成乱码标题，对不上任何 heading。

    原来一上来就 errors="replace"，这种失真**毫无痕迹** —— 表现出来只是"对齐率低"。
    下游门禁能兜住全面乱码，但兜不住"只乱几条、比率仍在 20% 阈值内"那种错误却不显眼
    的结果。所以退让可以，不出声不行。
    """
    data = '"9.1","波形"\n'.encode("gbk")
    with caplog.at_level(logging.WARNING):
        items = parse_agenda(data)
    assert items[0].item == "9.1"          # 议程号是 ASCII，照常解析
    assert items[0].title != "波形"         # 标题已失真
    assert "不是 UTF-8" in caplog.text
