from __future__ import annotations

import difflib
import re
import unicodedata
from dataclasses import dataclass, field

from ngr.models import AgendaItem, Heading

FUZZY_THRESHOLD = 0.90
DEPTH_TOLERANCE = 1  # heading 层级与议程深度允许 ±1 偏移

_PUNCT = re.compile(r"[^\w\s]", re.UNICODE)
_SPACE = re.compile(r"\s+")


def normalize(text: str) -> str:
    t = unicodedata.normalize("NFKC", text).lower()
    t = _PUNCT.sub("", t)
    return _SPACE.sub(" ", t).strip()


# "Annex A-1:"…"Annex H:" 是纪要的结构性附录（Tdoc 清单、参会者名单、会议日程表），
# 不是议程项，永远不会出现在 agenda.csv 里。实测 RAN1#126 有 9 条。
# 把它们计入未对齐率，会让这个"静默失败探针"常年停在 20%+ 的高位 ——
# 真正的对齐崩溃反而淹没在固定噪声里，探针就白设了。
ANNEX_RE = re.compile(r"(?i)^annex\b")


@dataclass
class Alignment:
    by_heading: dict[int, AgendaItem] = field(default_factory=dict)
    unaligned: list[Heading] = field(default_factory=list)
    skipped: list[Heading] = field(default_factory=list)

    @property
    def unmatched_ratio(self) -> float:
        total = len(self.by_heading) + len(self.unaligned)
        return len(self.unaligned) / total if total else 0.0


def align(agenda: list[AgendaItem], headings: list[Heading]) -> Alignment:
    """把纪要 heading 对回议程号。三道关：标题归一化精确匹配 →
    difflib 相似度 ≥ 0.90 → heading 层级与议程深度互校。全过才算数。"""
    result = Alignment()
    exact: dict[str, list[AgendaItem]] = {}
    for item in agenda:
        exact.setdefault(normalize(item.title), []).append(item)
    used: set[str] = set()
    seen: dict[str, AgendaItem] = {}  # 归一化标题 -> 已分配给它的议程项
    norm_keys = list(exact.keys())

    for h in headings:
        if ANNEX_RE.match(h.text.strip()):
            result.skipped.append(h)
            continue

        key = normalize(h.text)
        cands = [i for i in exact.get(key, []) if i.item not in used]

        if not cands and norm_keys:
            close = difflib.get_close_matches(key, norm_keys, n=1, cutoff=FUZZY_THRESHOLD)
            if close:
                cands = [i for i in exact[close[0]] if i.item not in used]

        chosen = None
        for cand in cands:
            if abs(cand.depth - h.level) <= DEPTH_TOLERANCE:
                chosen = cand
                break

        if chosen is None:
            # 同一个议程项常以"分组标题 + 同名子标题"出现两次（实测 RAN1#126 的
            # "GNSS resilient NR-NTN operation" 就是 L2/L3 各一次）。used 是为了阻止
            # 两个**标题不同**的小节抢同一个议程项；标题逐字相同时它们本就是同一项，
            # 判成未对齐只会凭空推高未对齐率，让探针失真。此处不再校验层级：
            # 标题完全相同已是足够强的证据，而分组标题与子标题的层级本就会差。
            chosen = seen.get(key)

        if chosen is None:
            result.unaligned.append(h)
        else:
            result.by_heading[h.para_index] = chosen
            used.add(chosen.item)
            seen[key] = chosen

    return result
