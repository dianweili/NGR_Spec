from __future__ import annotations
import time
from pathlib import Path
from ngr.models import Feature
from ngr.render.markdown import render_dashboard, render_feature_page, render_report
from ngr.render.site import render_site


def _report_date(events: list[dict], wg: str, meeting: int, suffix: str,
                 fallback: str) -> str:
    """Choose a stable report date for one meeting.

    Meeting end dates are preferred.  Older records do not carry them, so use
    their immutable first_seen date rather than the current render date; the
    latter would create a duplicate report for every historical meeting on
    each remap.
    """
    mine = [event for event in events if event["wg"] == wg and event["meeting"] == meeting
            and event.get("meeting_suffix", "") == suffix]
    for field in ("meeting_end", "first_seen"):
        dates = [event.get(field) for event in mine if event.get(field)]
        if dates:
            return min(dates)
    return fallback


def render_all(events: list[dict], features: list[Feature], feat_state: dict,
               out_dir: Path, *, banner: str | None = None,
               unmapped: list[str] | None = None,
               generated: str | None = None) -> list[Path]:
    generated = generated or time.strftime("%Y-%m-%d")
    out_dir = Path(out_dir)
    (out_dir / "features").mkdir(parents=True, exist_ok=True)
    (out_dir / "reports").mkdir(parents=True, exist_ok=True)
    (out_dir / "site").mkdir(parents=True, exist_ok=True)
    written: list[Path] = []

    def write(rel: str, text: str) -> None:
        p = out_dir / rel
        # 浏览器或预览器短暂占用旧文件时，直接截断写入会使整轮摘要在最后
        # 一步失败。先写同目录临时文件，再原子替换；Windows 上遇到短暂句柄
        # 占用时重试，旧页面始终保持完整。
        tmp = p.with_name(f".{p.name}.tmp")
        tmp.write_text(text, encoding="utf-8", newline="\n")
        for attempt in range(5):
            try:
                tmp.replace(p)
                break
            except OSError:
                if attempt == 4:
                    raise
                time.sleep(0.2 * (attempt + 1))
        written.append(p)

    write("dashboard.md", render_dashboard(events, features, feat_state,
                                           banner=banner, unmapped=unmapped,
                                           generated=generated))
    write("ALERTS.md", (banner + "\n") if banner else "")

    for feat in features:
        write(f"features/{feat.slug}.md",
              render_feature_page(feat.slug, events, feat, feat_state.get(feat.slug, {})))

    names = {f.slug: f.name_zh for f in features}
    for wg, meeting, suffix in sorted({(e["wg"], e["meeting"], e.get("meeting_suffix", "")) for e in events}):
        date = _report_date(events, wg, meeting, suffix, generated)
        write(f"reports/{date}-{wg}-{meeting}{suffix}.md",
              render_report(wg, meeting, events, names, suffix))

    write("site/index.html", render_site(events, features, feat_state, generated=generated))
    return written
