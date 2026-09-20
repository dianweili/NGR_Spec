import json, re
from ngr.models import Feature, LineageSegment
from ngr.render.site import render_site
from ngr.render.runner import render_all

def seg(era): return LineageSegment(era=era, release="Rel-20", depth="full",
                                    agenda=["RAN1:10.2"], title_re=None,
                                    meetings={"RAN1": (124, None)})
WAVE = Feature(slug="waveform", name_zh="6GR 波形", lineage=[seg("6G")])
FS = {"waveform": {"stage": "收敛中", "open_issues": [], "summary": "s"}}

def E(**kw):
    base = dict(id="RAN1-126-10.2-a001", wg="RAN1", meeting=126, agenda_item="10.2",
                agenda_title="Waveform", kind="agreement", era="6G", release="Rel-20",
                depth="full", feature="waveform", text_en="Adopt X.",
                summary_zh="采纳 X。", tags=[], impact="high", llm_status="ok",
                first_seen="2026-08-25", meeting_end="2026-08-21", source={})
    base.update(kw); return base

def test_site_is_self_contained():
    html = render_site([E()], [WAVE], FS, generated="2026-09-17")
    assert html.lstrip().startswith("<!DOCTYPE html>")
    assert "<script src=" not in html and "<link rel=\"stylesheet\"" not in html

def test_site_embeds_data_as_json():
    html = render_site([E()], [WAVE], FS, generated="2026-09-17")
    m = re.search(r'id="ngr-data"[^>]*>(.*?)</script>', html, re.S)
    assert m, "数据必须内联为 JSON"
    data = json.loads(m.group(1))
    assert data["events"][0]["id"] == "RAN1-126-10.2-a001"
    assert data["features"][0]["slug"] == "waveform"

def test_site_escapes_html_in_event_text():
    html = render_site([E(text_en="<script>alert(1)</script>")], [WAVE], FS,
                       generated="2026-09-17")
    assert "<script>alert(1)</script>" not in html

def test_site_declares_dark_mode():
    html = render_site([E()], [WAVE], FS, generated="2026-09-17")
    assert "prefers-color-scheme: dark" in html

def test_site_has_viewport_for_mobile():
    html = render_site([E()], [WAVE], FS, generated="2026-09-17")
    assert 'name="viewport"' in html

def test_site_renders_with_zero_events():
    html = render_site([], [WAVE], FS, generated="2026-09-17")
    assert "<!DOCTYPE html>" in html.lstrip()[:20]

def test_render_all_writes_expected_files(tmp_path):
    paths = render_all([E()], [WAVE], FS, tmp_path)
    names = {p.relative_to(tmp_path).as_posix() for p in paths}
    assert "dashboard.md" in names
    assert "features/waveform.md" in names
    assert "site/index.html" in names
    assert any(n.startswith("reports/") for n in names)

def test_render_all_is_deterministic(tmp_path):
    render_all([E()], [WAVE], FS, tmp_path, generated="2026-09-17")
    first = (tmp_path / "dashboard.md").read_bytes()
    render_all([E()], [WAVE], FS, tmp_path, generated="2026-09-17")
    assert (tmp_path / "dashboard.md").read_bytes() == first

def test_render_all_writes_empty_alerts_when_no_banner(tmp_path):
    render_all([E()], [WAVE], FS, tmp_path)
    assert (tmp_path / "ALERTS.md").read_text(encoding="utf-8").strip() == ""


# —— 以下四条守的是审查实测出来的缺陷 ——

def test_feat_state_value_none_does_not_crash():
    """`.get(slug, {})` 的默认值只在键**不存在**时生效；键在但值为 None
    （state 文件里写了 null）时返回 None，紧接着的 .get 就炸。

    渲染是管线最后一站，崩在这里等于整轮跑白，而且崩之前已经落了一半文件 ——
    哪些写了哪些没写取决于崩在第几步。
    """
    from ngr.render.markdown import render_dashboard
    html = render_site([], [WAVE], {"waveform": None}, generated="2026-09-20")
    assert "6G (Rel-20) RAN" in html
    assert render_dashboard([], [WAVE], {"waveform": None})      # markdown 层同一模式


def test_accent_colour_is_actually_used():
    """`--accent` 只定义不引用时，Step 1 那道"先读 dataviz 规范再选色"的工序
    对最终产物零影响 —— 无论选什么色值，字节都不变。"""
    html = render_site([], [WAVE], {}, generated="2026-09-20")
    assert "var(--accent)" in html, "选了色就要真的用上，否则配色工序没有意义"


def test_meeting_goes_through_esc():
    """纵深防御：`Event.meeting: int` 是类型约定而非运行时强制，事件到渲染层时
    已经是 dict、不再过 dataclass 校验。对数字套 esc() 无副作用。"""
    html = render_site([], [WAVE], {}, generated="2026-09-20")
    assert "esc(e.meeting)" in html


def test_feature_order_is_preserved_not_sorted():
    """`features` 顺序来自 features.yaml 的书写顺序，那是人工编排的优先级。

    排成字典序等于把这个信息丢掉 —— 所以"打乱输入→输出不变"这条**有意**只对
    events 与 feat_state 成立，features 顺序是调用方契约，不是要防御的抖动。
    """
    import json as _json
    import re as _re
    isac = Feature(slug="isac", name_zh="ISAC 通感一体", lineage=[seg("6G")])
    a = render_site([], [WAVE, isac], {}, generated="2026-09-20")
    b = render_site([], [isac, WAVE], {}, generated="2026-09-20")
    assert a != b, "features 顺序必须如实反映到产物里"
    slugs = lambda h: [f["slug"] for f in _json.loads(
        _re.search(r'id="ngr-data">(.*?)</script>', h, _re.S).group(1)
        .replace(chr(92) + "u003c", "<"))["features"]]
    assert slugs(a) == ["waveform", "isac"] and slugs(b) == ["isac", "waveform"]
