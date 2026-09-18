from __future__ import annotations
from collections import Counter
from ngr.mapping.lineage import match_event
from ngr.models import Feature

def lineage_report(features: list[Feature], parsed_meetings: list[dict]) -> str:
    """打印每个血统段命中了哪些 heading、各多少条事件。
    这是校准 5G-A title_re 的主要工具：改正则 → remap → 看这张表。"""
    hits: dict[tuple[str, int], Counter] = {}
    for feat in features:
        for i, _ in enumerate(feat.lineage):
            hits[(feat.slug, i)] = Counter()

    for parsed in parsed_meetings:
        wg, meeting = parsed["wg"], parsed["meeting"]
        for raw in parsed["events"]:
            m = match_event(features, wg, meeting,
                            raw.get("agenda_item"), raw.get("heading_path") or [])
            if m is None:
                continue
            feat = next(f for f in features if f.slug == m.feature_slug)
            idx = feat.lineage.index(m.segment)
            head = (raw.get("heading_path") or ["(无)"])[-1]
            hits[(m.feature_slug, idx)][head] += 1

    lines = ["# 血统命中对照表", ""]
    for feat in features:
        lines.append(f"## {feat.slug} — {feat.name_zh}")
        for i, seg in enumerate(feat.lineage):
            c = hits[(feat.slug, i)]
            total = sum(c.values())
            rng = ", ".join(f"{w} {lo}–{hi if hi is not None else '至今'}"
                            for w, (lo, hi) in seg.meetings.items())
            flag = "  ⚠️ 命中为 0" if total == 0 else ""
            lines.append(f"- [{seg.era}/{seg.release}] depth={seg.depth} ({rng}) "
                         f"→ **{total}** 条{flag}")
            for head, n in c.most_common(8):
                lines.append(f"    - {n:4d}  {head}")
        lines.append("")
    return "\n".join(lines)
