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
