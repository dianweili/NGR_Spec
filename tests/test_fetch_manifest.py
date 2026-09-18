from ngr.fetch.manifest import Manifest, minutes_version, pick_latest_minutes, unwrap_docx

RAN1_RE = r"(?i)^(Draft|Final)_Minutes_report_RAN1#\d+.*\.(zip|docx)$"
RAN2_RE = r"(?i)^R2-\d+\.zip$"

def test_minutes_version_parsing():
    assert minutes_version("Draft_Minutes_report_RAN1#126_v010.docx") == 10
    assert minutes_version("Draft_Minutes_report_RAN1#126_v100.docx") == 100
    assert minutes_version("Welcome.docx") is None

def test_minutes_version_accepts_zip():
    """实测：RAN1 ≤#122 的纪要以 zip 分发，只认 .docx 会让 5G-A 全线静默跳过。"""
    assert minutes_version("Final_Minutes_report_RAN1#112_v100.zip") == 100

def test_pick_latest_minutes_prefers_higher_version():
    names = ["Draft_Minutes_report_RAN1#126_v010.docx",
             "Draft_Minutes_report_RAN1#126_v100.docx", "Archive"]
    assert pick_latest_minutes(names, RAN1_RE) == "Draft_Minutes_report_RAN1#126_v100.docx"

def test_pick_latest_minutes_finds_zip_only_meeting():
    names = ["Final_Minutes_report_RAN1#112_v100.zip", "Archive"]
    assert pick_latest_minutes(names, RAN1_RE) == "Final_Minutes_report_RAN1#112_v100.zip"

def test_pick_latest_minutes_prefers_docx_over_zip_at_same_version():
    names = ["Draft_Minutes_report_RAN1#123_v100.zip",
             "Draft_Minutes_report_RAN1#123_v100.docx"]
    assert pick_latest_minutes(names, RAN1_RE) == "Draft_Minutes_report_RAN1#123_v100.docx"

def test_pick_latest_minutes_version_beats_format():
    names = ["Draft_Minutes_report_RAN1#123_v100.zip",
             "Draft_Minutes_report_RAN1#123_v010.docx"]
    assert pick_latest_minutes(names, RAN1_RE) == "Draft_Minutes_report_RAN1#123_v100.zip"

def test_pick_latest_minutes_returns_none_when_absent():
    assert pick_latest_minutes(["Archive", "notes.txt"], RAN1_RE) is None

def test_pick_latest_minutes_ran2_tdoc_naming():
    """实测 RAN2 的纪要就是个 TDoc 号 zip，文件名里没有 minutes 字样。
    用 RAN1 的正则会零匹配 —— 这正是必须按组配置的原因。"""
    names = ["R2-2604502.zip", "Skeleton_Report_v001.zip", "TDoc_List.xlsx"]
    assert pick_latest_minutes(names, RAN2_RE) == "R2-2604502.zip"
    assert pick_latest_minutes(names, RAN1_RE) is None

def test_pick_latest_minutes_no_version_falls_back_to_name_order():
    names = ["R2-2604502.zip", "R2-2604999.zip"]
    assert pick_latest_minutes(names, RAN2_RE) == "R2-2604999.zip"

def test_unwrap_docx_picks_largest_inner_docx():
    """RAN2 的纪要 zip 内含 PartList / TDoc_List 等小文件，正文是最大的那个。"""
    import io as _io, zipfile as _zf, pathlib
    real = pathlib.Path("tests/fixtures/RAN1_126/minutes.docx").read_bytes()
    buf = _io.BytesIO()
    with _zf.ZipFile(buf, "w") as z:
        z.writestr("PartList.docx", b"x" * 100)
        z.writestr("R2-2604502.docx", real)
    out = unwrap_docx(buf.getvalue())
    assert _zf.ZipFile(_io.BytesIO(out)).namelist().count("word/document.xml") == 1

def test_unwrap_docx_passes_through_real_docx():
    import pathlib
    data = pathlib.Path("tests/fixtures/RAN1_126/minutes.docx").read_bytes()
    assert unwrap_docx(data) is data

def test_unwrap_docx_extracts_inner_docx():
    import io as _io, zipfile as _zf, pathlib
    inner = pathlib.Path("tests/fixtures/RAN1_126/minutes.docx").read_bytes()
    buf = _io.BytesIO()
    with _zf.ZipFile(buf, "w") as z:
        z.writestr("Final_Minutes_report_RAN1#112_v100.docx", inner)
    out = unwrap_docx(buf.getvalue())
    assert _zf.ZipFile(_io.BytesIO(out)).namelist().count("word/document.xml") == 1

def test_unwrap_docx_raises_when_no_docx_inside():
    import io as _io, zipfile as _zf, pytest as _pytest
    buf = _io.BytesIO()
    with _zf.ZipFile(buf, "w") as z:
        z.writestr("readme.txt", b"nothing here")
    with _pytest.raises(ValueError, match="docx"):
        unwrap_docx(buf.getvalue())

def test_needs_fetch_true_when_unknown(tmp_path):
    assert Manifest(tmp_path).needs_fetch("a.docx", {"etag": '"x"', "length": 5})

def test_needs_fetch_false_when_etag_matches(tmp_path):
    m = Manifest(tmp_path)
    m.record("a.docx", "http://u", {"etag": '"x"', "length": 5}, b"hello")
    m.save()
    assert not Manifest(tmp_path).needs_fetch("a.docx", {"etag": '"x"', "length": 5})

def test_needs_fetch_true_when_length_changed(tmp_path):
    m = Manifest(tmp_path)
    m.record("a.docx", "http://u", {"etag": None, "length": 5}, b"hello")
    m.save()
    assert Manifest(tmp_path).needs_fetch("a.docx", {"etag": None, "length": 9})

def test_needs_fetch_true_when_head_has_no_validators(tmp_path):
    """HEAD 什么都没给时必须重抓 —— 宁可多下一次也不要漏掉更新。"""
    m = Manifest(tmp_path)
    m.record("a.docx", "http://u", {"etag": '"x"', "length": 5}, b"hello")
    m.save()
    assert Manifest(tmp_path).needs_fetch("a.docx", {"etag": None, "length": None})

def test_record_writes_file_and_sha(tmp_path):
    m = Manifest(tmp_path)
    m.record("a.docx", "http://u", {"etag": None, "length": 5}, b"hello")
    m.save()
    assert (tmp_path / "a.docx").read_bytes() == b"hello"
    entry = Manifest(tmp_path).load()["files"]["a.docx"]
    assert entry["sha256"].startswith("sha256:")

def test_frozen_roundtrip(tmp_path):
    m = Manifest(tmp_path)
    assert not m.is_frozen()
    m.mark_frozen(); m.save()
    assert Manifest(tmp_path).is_frozen()
