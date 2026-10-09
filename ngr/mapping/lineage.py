from __future__ import annotations
import re
from dataclasses import dataclass
from functools import lru_cache
from ngr.models import Feature, LineageSegment

@dataclass(frozen=True)
class Match:
    feature_slug: str
    segment: LineageSegment

@lru_cache(maxsize=512)
def _compiled(pattern: str) -> re.Pattern:
    return re.compile(pattern)

def agenda_matches(patterns: list[str], wg: str, agenda_item: str | None) -> bool:
    """模式形如 'RAN1:10.2'（精确）或 'RAN1:10.2.*'（严格后代）。
    通配按点分段比较，'10.2.*' 不会误命中 '10.20'。"""
    if agenda_item is None:
        return False
    for pat in patterns:
        pat_wg, _, pat_item = pat.partition(":")
        if pat_wg != wg:
            continue
        if pat_item.endswith(".*"):
            prefix = pat_item[:-2]
            if agenda_item != prefix and agenda_item.startswith(prefix + "."):
                return True
        elif pat_item == agenda_item:
            return True
    return False

def _segment_hits(seg: LineageSegment, wg: str, meeting: int,
                  agenda_item: str | None, heading_path: list[str], suffix: str = "") -> bool:
    if not seg.covers(wg, meeting, suffix):
        return False
    if seg.agenda and agenda_matches(seg.agenda, wg, agenda_item):
        return True
    if seg.title_re:
        rx = _compiled(seg.title_re)
        return any(rx.search(text) for text in heading_path)
    return False

def match_event(features: list[Feature], wg: str, meeting: int,
                agenda_item: str | None, heading_path: list[str],
                meeting_suffix: str = "") -> Match | None:
    """返回首个命中的 (特性, 血统段)。
    顺序规则（保证结果可复现）：
      1. 按 features.yaml 中特性的书写顺序；
      2. 同一特性内，6G 段优先于 5G-A 段 —— 会议进入 6G 阶段后不应再算作历史。"""
    for feat in features:
        segs = sorted(feat.lineage, key=lambda s: 0 if s.era == "6G" else 1)
        for seg in segs:
            if _segment_hits(seg, wg, meeting, agenda_item, heading_path, meeting_suffix):
                return Match(feature_slug=feat.slug, segment=seg)
    return None
