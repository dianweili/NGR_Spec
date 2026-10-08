# tests/test_fetch_runner.py
import pytest
from unittest.mock import Mock
from urllib.parse import quote
from ngr.config import WgConfig
from ngr.models import Meeting
from ngr.fetch.manifest import Manifest
from ngr.fetch.runner import fetch_meeting

WG = WgConfig(path="tsg_ran/WG1_RL1", dir_re=r"TSGR1_(\d+)([a-z]*)", hard_floor=112,
              agenda_csv_since=124, minutes_re=r"(?i)minutes.*\.(docx|zip)$", 
              artifacts=["agenda_csv", "minutes_docx", "docs_listing"])
MTG = Meeting(wg="RAN1", number=126, suffix="",
              url="https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/")

def _http(listings: dict[str, bytes], files: dict[str, bytes]):
    http = Mock()
    def get(url):
        if url in listings: return listings[url]
        if url in files:    return files[url]
        raise AssertionError(f"未预期的 GET {url}")
    http.get.side_effect = get
    http.head.return_value = {"etag": '"e"', "length": 3}
    return http

def _listing(dir_url, names):
    """模拟真实 IIS 目录列表：href 里的文件名是百分号转义的。

    实测 3GPP 的 Report 目录 HTML 写的是
    `href=".../Final_Minutes_report_RAN1%23112_v100.zip"` —— `#` 是 `%23`，
    因为 `#` 在 URL 里是片段分隔符。parse_listing 的捕获类排除 `#` 正是为此，
    随后用 unquote() 还原。助手若不转义，文件名会在 `#` 处被截断，
    这条链路就测不到真实行为了。"""
    return b"".join(
        f'<a href="{dir_url}{quote(n)}">{n}</a>'.encode() for n in names)

def test_fetch_meeting_downloads_agenda_and_latest_minutes(tmp_path):
    base = MTG.url
    http = _http(
        listings={
            base: _listing(base, ["Agenda", "Report", "Docs"]),
            base + "Agenda/": _listing(base + "Agenda/", ["agenda.csv"]),
            base + "Report/": _listing(base + "Report/",
                ["Draft_Minutes_report_RAN1#126_v010.docx",
                 "Draft_Minutes_report_RAN1#126_v100.docx"]),
            base + "Docs/": _listing(base + "Docs/", ["R1-1.zip"]),
        },
        files={base + "Agenda/agenda.csv": b"csv",
               base + "Report/Draft_Minutes_report_RAN1%23126_v100.docx": b"doc"})
    res = fetch_meeting(http, MTG, WG, raw_dir=tmp_path)
    assert res.changed
    assert (tmp_path / "agenda.csv").read_bytes() == b"csv"
    assert (tmp_path / "minutes.docx").read_bytes() == b"doc"
    assert (tmp_path / "docs_listing.html").exists()
    assert base + "Report/Draft_Minutes_report_RAN1%23126_v100.docx" in [
        call.args[0] for call in http.head.call_args_list]

def test_fetch_meeting_skips_agenda_when_absent(tmp_path):
    """老会议的 Agenda/ 里只有 TDoc zip —— 靠目录列表判断，不靠 GET 状态码。"""
    base = MTG.url
    http = _http(
        listings={
            base: _listing(base, ["Agenda", "Report", "Docs"]),
            base + "Agenda/": _listing(base + "Agenda/", ["R1-2500001.zip"]),
            base + "Report/": _listing(base + "Report/",
                                       ["Draft_Minutes_report_RAN1#120_v100.docx"]),
            base + "Docs/": _listing(base + "Docs/", ["R1-1.zip"]),
        },
        files={base + "Report/Draft_Minutes_report_RAN1%23120_v100.docx": b"doc"})
    res = fetch_meeting(http, MTG, WG, raw_dir=tmp_path)
    assert not (tmp_path / "agenda.csv").exists()
    assert (tmp_path / "minutes.docx").exists()
    assert "agenda_csv" in res.missing

def test_fetch_meeting_skips_frozen(tmp_path):
    m = Manifest(tmp_path); m.mark_frozen(); m.save()
    http = Mock()
    res = fetch_meeting(http, MTG, WG, raw_dir=tmp_path)
    assert not res.changed and res.skipped_reason == "frozen"
    http.get.assert_not_called()
    http.head.assert_not_called()

def test_fetch_meeting_force_ignores_frozen(tmp_path):
    base = MTG.url
    m = Manifest(tmp_path); m.mark_frozen(); m.save()
    http = _http(
        listings={base: _listing(base, ["Report"]),
                  base + "Report/": _listing(base + "Report/", ["Minutes_v010.docx"])},
        files={base + "Report/Minutes_v010.docx": b"doc"})
    res = fetch_meeting(http, MTG, WG, raw_dir=tmp_path, force=True)
    assert res.changed

def test_manifest_saved_when_rate_limited_midway(tmp_path):
    """限流中断时，本次已成功抓到的 artifact 必须落进 manifest。
    否则文件在磁盘上却查不到记录，下次重试会重新下载 —— 限流引发重复下载、
    重复下载又加剧限流。"""
    from ngr.fetch.client import RateLimited
    base = MTG.url
    listings = {
        base: _listing(base, ["Agenda", "Report"]),
        base + "Agenda/": _listing(base + "Agenda/", ["agenda.csv"]),
        base + "Report/": _listing(base + "Report/", ["Draft_Minutes_report_RAN1#126_v010.docx"]),
    }
    files = {base + "Agenda/agenda.csv": b"csv"}
    http = _http(listings, files)
    calls = {"n": 0}
    def head(url):
        calls["n"] += 1
        if calls["n"] > 1:                      # 第二个 artifact 撞限流
            raise RateLimited("rate limited")
        return {"etag": '"e"', "length": 3}
    http.head.side_effect = head

    with pytest.raises(RateLimited):
        fetch_meeting(http, MTG, WG, raw_dir=tmp_path)

    assert (tmp_path / "agenda.csv").exists()
    assert (tmp_path / "_manifest.json").exists(), "已成功的 artifact 必须落盘"
    assert "agenda.csv" in Manifest(tmp_path).load()["files"]

def test_report_dirs_picks_first_existing_candidate(tmp_path):
    """report_dirs 是**有序**候选列表：两个都存在时取列表里排前面的那个。
    实测 RAN4 老会议用复数 Reports、新会议用单数 Report。"""
    from dataclasses import replace
    base = MTG.url
    wg = replace(WG, report_dirs=["Reports", "Report"], artifacts=["minutes_docx"])
    listings = {
        base: _listing(base, ["Report", "Reports"]),
        base + "Reports/": _listing(base + "Reports/", ["Draft_Minutes_report_RAN1#126_v100.docx"]),
        base + "Report/": _listing(base + "Report/", ["Draft_Minutes_report_RAN1#126_v010.docx"]),
    }
    files = {base + "Reports/Draft_Minutes_report_RAN1%23126_v100.docx": b"doc"}
    res = fetch_meeting(_http(listings, files), MTG, wg, raw_dir=tmp_path)
    assert res.changed and "minutes_docx" in res.files

def test_fetch_meeting_no_redownload_when_unchanged(tmp_path):
    base = MTG.url
    listings = {base: _listing(base, ["Report"]),
                base + "Report/": _listing(base + "Report/", ["Minutes_v010.docx"])}
    files = {base + "Report/Minutes_v010.docx": b"doc"}
    http = _http(listings, files)
    fetch_meeting(http, MTG, WG, raw_dir=tmp_path)
    http2 = _http(listings, files)
    res = fetch_meeting(http2, MTG, WG, raw_dir=tmp_path)
    assert not res.changed
    assert base + "Report/Minutes_v010.docx" not in [c.args[0] for c in http2.get.call_args_list]
