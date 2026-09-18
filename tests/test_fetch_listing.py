from ngr.fetch.listing import parse_listing

DIR = "https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/"
HTML = b"""<html><body><table>
<tr><td><a href="https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/">..</a></td></tr>
<tr><td><a href="https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Agenda">Agenda</a></td></tr>
<tr><td><a href="https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs">Docs</a></td></tr>
<tr><td><a href="https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Report">Report</a></td></tr>
<tr><td><a href="?sortby=name">name</a></td></tr>
</table></body></html>"""

def test_parse_listing_returns_direct_children():
    assert parse_listing(HTML, DIR) == ["Agenda", "Docs", "Report"]

def test_parse_listing_excludes_parent_and_sort_links():
    got = parse_listing(HTML, DIR)
    assert ".." not in got and not any(g.startswith("?") for g in got)

def test_parse_listing_ignores_deeper_paths():
    html = HTML.replace(b"TSGR1_126/Report", b"TSGR1_126/Report/Archive")
    assert "Archive" not in parse_listing(html, DIR)

def test_parse_listing_tolerates_trailing_slash_in_dir_url():
    assert parse_listing(HTML, DIR.rstrip("/")) == ["Agenda", "Docs", "Report"]

def test_parse_listing_ignores_url_outside_href():
    """页面正文/注释里出现同一个目录 URL 时不得被当成条目 —— 实测 fixture 里就有这种文字。"""
    html = (b'<p>note: ' + DIR.encode() + b' retrieved 2026-09-17</p>'
            b'<a href="' + DIR.encode() + b'R1-1.zip">R1-1.zip</a>')
    assert parse_listing(html, DIR) == ["R1-1.zip"]

def test_parse_listing_on_fixture_docs():
    """真实 fixture：RAN1#126 的 Docs 目录列表全是 R1-*.zip。"""
    import pathlib
    p = pathlib.Path("tests/fixtures/RAN1_126/docs_listing.html")
    names = parse_listing(p.read_bytes(), DIR + "Docs/")
    assert names, "fixture 解析出 0 条，检查 fixture 或解析逻辑"
    assert all(n.startswith("R1-") and n.endswith(".zip") for n in names)
