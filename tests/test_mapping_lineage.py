from pathlib import Path

from ngr.config import load_features
from ngr.models import Feature, LineageSegment
from ngr.mapping.lineage import agenda_matches, match_event


def seg(era="6G", depth="full", agenda=None, title_re=None, meetings=None):
    return LineageSegment(era=era, release="Rel-20", depth=depth,
                          agenda=agenda or [], title_re=title_re,
                          meetings=meetings or {"RAN1": (124, None)})

def feat(slug, *segs):
    return Feature(slug=slug, name_zh=slug, lineage=list(segs))

# —— agenda 通配 ——
def test_agenda_exact():
    assert agenda_matches(["RAN1:10.2"], "RAN1", "10.2")
    assert not agenda_matches(["RAN1:10.2"], "RAN1", "10.3")

def test_agenda_wildcard_matches_children():
    assert agenda_matches(["RAN1:10.2.*"], "RAN1", "10.2.1")
    assert agenda_matches(["RAN1:10.2.*"], "RAN1", "10.2.1.3")

def test_agenda_wildcard_does_not_match_self():
    assert not agenda_matches(["RAN1:10.2.*"], "RAN1", "10.2")

def test_agenda_wildcard_does_not_match_sibling_prefix():
    """10.2.* 不该命中 10.20 —— 前缀匹配必须按点分段。"""
    assert not agenda_matches(["RAN1:10.2.*"], "RAN1", "10.20")

def test_agenda_respects_wg():
    assert not agenda_matches(["RAN1:10.2"], "RAN2", "10.2")

def test_agenda_none_never_matches():
    assert not agenda_matches(["RAN1:10.2"], "RAN1", None)

# —— 事件匹配 ——
def test_match_by_agenda():
    f = feat("waveform", seg(agenda=["RAN1:10.2"]))
    m = match_event([f], "RAN1", 126, "10.2", ["Rel-20 Study of 6GR", "Waveform"])
    assert m.feature_slug == "waveform" and m.segment.depth == "full"

def test_match_by_title_re_when_no_agenda():
    """5G-A 老会议没有议程号，只能靠标题正则。"""
    f = feat("isac", seg(era="5G-A", depth="origin", title_re="(?i)ISAC",
                         meetings={"RAN1": (116, 123)}))
    m = match_event([f], "RAN1", 120, None, ["Rel-19 NR", "ISAC channel model"])
    assert m.feature_slug == "isac" and m.segment.era == "5G-A"

def test_title_re_checks_whole_heading_path():
    f = feat("isac", seg(title_re="(?i)6GR"))
    assert match_event([f], "RAN1", 126, None, ["Rel-20 Study of 6GR", "Evaluations"])

def test_no_match_outside_meeting_range():
    f = feat("isac", seg(agenda=["RAN1:10.8"], meetings={"RAN1": (124, 126)}))
    assert match_event([f], "RAN1", 127, "10.8", []) is None

def test_no_match_for_other_wg():
    f = feat("isac", seg(agenda=["RAN1:10.8"]))
    assert match_event([f], "RAN2", 126, "10.8", []) is None


def test_ran2_rrc_configuration_includes_parent_control_plane_only():
    """#132 的 RRC Modelling 结论挂在 10.3.2 Control plane 父标题下。"""
    features = load_features(Path(__file__).parents[1] / "config" / "features.yaml")
    rrc = next(feature for feature in features if feature.slug == "rrc")
    assert match_event([rrc], "RAN2", 132, "10.3.2", []).feature_slug == "rrc"
    assert match_event([rrc], "RAN2", 132, "10.3.2.3", []) is None

def test_agenda_wins_over_title_re_within_same_segment():
    f = feat("x", seg(agenda=["RAN1:10.2"], title_re="(?i)nothing"))
    assert match_event([f], "RAN1", 126, "10.2", ["Waveform"])

def test_first_feature_in_file_order_wins_on_tie():
    """两个特性都命中时取 features.yaml 中靠前的 —— 结果必须可复现。"""
    a = feat("aaa", seg(title_re="(?i)ISAC"))
    b = feat("bbb", seg(title_re="(?i)ISAC"))
    assert match_event([a, b], "RAN1", 126, None, ["ISAC"]).feature_slug == "aaa"

def test_six_g_segment_preferred_over_legacy_when_both_hit():
    """同一特性内 6G 段与 5G-A 段同时覆盖某次会议时，取 6G 段。"""
    f = feat("isac",
             seg(era="5G-A", depth="origin", title_re="(?i)ISAC", meetings={"RAN1": (116, 130)}),
             seg(era="6G", depth="full", title_re="(?i)ISAC", meetings={"RAN1": (124, None)}))
    assert match_event([f], "RAN1", 126, None, ["ISAC"]).segment.era == "6G"
