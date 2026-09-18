from unittest.mock import Mock
from ngr.config import WgConfig
from ngr.models import Feature, LineageSegment
from ngr.fetch.discover import discover_meetings, fetch_window

WG = WgConfig(path="tsg_ran/WG1_RL1", dir_re=r"TSGR1_(\d+)([a-z]*)",
              hard_floor=112, agenda_csv_since=124,
              minutes_re=r"(?i)minutes.*\.(docx|zip)$", artifacts=["agenda_csv"])

def _feature(slug, segs):
    return Feature(slug=slug, name_zh=slug, lineage=segs)

def _seg(lo, hi, wg="RAN1"):
    return LineageSegment(era="6G", release="Rel-20", depth="full",
                          agenda=["RAN1:10"], title_re=None, meetings={wg: (lo, hi)})

def test_fetch_window_is_union_of_lineage():
    feats = [_feature("a", [_seg(116, 126)]), _feature("b", [_seg(124, None)])]
    assert fetch_window(feats, "RAN1", WG) == (116, None)

def test_fetch_window_clamped_by_hard_floor():
    feats = [_feature("a", [_seg(100, 120)])]
    assert fetch_window(feats, "RAN1", WG) == (112, 120)

def test_fetch_window_none_when_wg_not_covered():
    feats = [_feature("a", [_seg(116, 126, wg="RAN2")])]
    assert fetch_window(feats, "RAN1", WG) is None

def test_fetch_window_closed_range_when_all_bounded():
    feats = [_feature("a", [_seg(116, 120)]), _feature("b", [_seg(118, 126)])]
    assert fetch_window(feats, "RAN1", WG) == (116, 126)

def test_discover_meetings_parses_and_sorts():
    http = Mock()
    http.get.return_value = (
        b'<a href="https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120">x</a>'
        b'<a href="https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126">x</a>'
        b'<a href="https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b">x</a>'
        b'<a href="https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/Templates">x</a>')
    got = discover_meetings(http, "RAN1", WG)
    assert [(m.number, m.suffix) for m in got] == [(120, ""), (126, ""), (126, "b")]
    assert got[0].url.endswith("TSGR1_120/")

def test_discover_meetings_ignores_non_meeting_dirs():
    http = Mock()
    http.get.return_value = b'<a href="https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/Tdoc_index">x</a>'
    assert discover_meetings(http, "RAN1", WG) == []
