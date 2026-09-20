from __future__ import annotations
import time
from pathlib import Path
from ngr.models import Feature
from ngr.render.markdown import render_dashboard, render_feature_page, render_report
from ngr.render.site import render_site

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
        p.write_text(text, encoding="utf-8", newline="\n")
        written.append(p)

    write("dashboard.md", render_dashboard(events, features, feat_state,
                                           banner=banner, unmapped=unmapped,
                                           generated=generated))
    write("ALERTS.md", (banner + "\n") if banner else "")

    for feat in features:
        write(f"features/{feat.slug}.md",
              render_feature_page(feat.slug, events, feat, feat_state.get(feat.slug, {})))

    names = {f.slug: f.name_zh for f in features}
    for wg, meeting in sorted({(e["wg"], e["meeting"]) for e in events}):
        date = next((e.get("meeting_end") for e in events
                     if e["wg"] == wg and e["meeting"] == meeting and e.get("meeting_end")),
                    generated)
        write(f"reports/{date}-{wg}-{meeting}.md",
              render_report(wg, meeting, events, names))

    write("site/index.html", render_site(events, features, feat_state, generated=generated))
    return written
