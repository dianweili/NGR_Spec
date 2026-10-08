from __future__ import annotations

import difflib
import logging
import re
import unicodedata
from dataclasses import dataclass, field

from ngr.models import AgendaItem, Heading

log = logging.getLogger(__name__)

FUZZY_THRESHOLD = 0.90
DEPTH_TOLERANCE = 1  # heading 层级与议程深度允许 ±1 偏移

_PUNCT = re.compile(r"[^\w\s]", re.UNICODE)
_SPACE = re.compile(r"\s+")
_ABBREVIATION = re.compile(r"\b[A-Z][A-Z0-9-]{1,}\b")


def normalize(text: str) -> str:
    t = unicodedata.normalize("NFKC", text).lower()
    t = _PUNCT.sub("", t)
    return _SPACE.sub(" ", t).strip()


# "Annex A-1:"…"Annex H:" 是纪要的结构性附录（Tdoc 清单、参会者名单、会议日程表），
# 不是议程项，永远不会出现在 agenda.csv 里。实测 RAN1#126 有 9 条。
# 把它们计入未对齐率，会让这个"静默失败探针"常年停在 20%+ 的高位 ——
# 真正的对齐崩溃反而淹没在固定噪声里，探针就白设了。
ANNEX_RE = re.compile(r"(?i)^annex\b")

# RAN1 minutes have a fixed opening/schedule block that is intentionally absent
# from agenda.csv.  These are not technical agenda items, so counting them as
# a failed alignment turns a harmless template difference into a false gate.
# Keep this list exact: a broad "opening"/"meeting" match would hide genuine
# agenda-template changes.
NON_AGENDA_RE = re.compile(
    r"(?i)^(?:call for ipr|competition law statement|network usage conditions|"
    r"consensus principles reminder|streamlined standards|"
    r"check-in for registered delegates|recording of ran1 meeting|ran1 brk\b)"
)


@dataclass
class Alignment:
    by_heading: dict[int, AgendaItem] = field(default_factory=dict)
    unaligned: list[Heading] = field(default_factory=list)
    skipped: list[Heading] = field(default_factory=list)

    @property
    def unmatched_ratio(self) -> float:
        """未对上的比例，分母只含**参与对齐**的 heading（不含 skipped 的结构标题）。

        分母为 0 时返回 **1.0 而不是 0.0**。0/0 在数学上无定义，这里是一个刻意的
        策略选择：分母为 0 意味着"一条都没对上"，而不是"全对上了"。
        Task 11 用 `ratio > MAX_UNMATCHED_RATIO` 当质量门禁，若此时返回 0.0，
        一份 heading 抽取彻底失效（或只剩 Annex）的纪要会拿到比正常值（12.2%）
        **还要好看**的分数被放行 —— 探针被自己的边界条件反噬。

        也不要改用 `float("nan")` 当哨兵：`nan > 0.20` 恒为 False，
        门禁照样放行，比返回 0.0 更隐蔽。
        """
        total = len(self.by_heading) + len(self.unaligned)
        return len(self.unaligned) / total if total else 1.0


def align(agenda: list[AgendaItem], headings: list[Heading]) -> Alignment:
    """把纪要 heading 对回议程号。三道关：标题归一化精确匹配 →
    difflib 相似度 ≥ 0.90 → heading 层级与议程深度互校。全过才算数。"""
    result = Alignment()
    exact: dict[str, list[AgendaItem]] = {}
    abbreviations: dict[str, list[AgendaItem]] = {}
    for item in agenda:
        exact.setdefault(normalize(item.title), []).append(item)
        for token in _ABBREVIATION.findall(item.title):
            abbreviations.setdefault(normalize(token), []).append(item)
    # 两个议程项归一化后撞成同一个 key 时，下面的候选池会"先到先得"，
    # 后一个议程项永远拿不到 heading —— 这违背"宁可少归类，不可错归类"。
    # 实测 RAN1#126 的 66 条议程项无冲突，所以不改行为，只出声：
    # 探针的价值来自平时沉默，真出现了才好顺着日志查。
    dup = {k: [i.item for i in v] for k, v in exact.items() if len(v) > 1}
    if dup:
        log.warning("议程标题归一化后重名，可能错归类: %s", dup)
    used: set[str] = set()
    seen: dict[str, AgendaItem] = {}  # 归一化标题 -> 已分配给它的议程项
    norm_keys = list(exact.keys())

    for h in headings:
        if ANNEX_RE.match(h.text.strip()) or NON_AGENDA_RE.match(h.text.strip()):
            result.skipped.append(h)
            continue

        key = normalize(h.text)
        cands = [i for i in exact.get(key, []) if i.item not in used]

        # A minute may use an acronym ("ISAC") where the agenda spells out the
        # full title ("Integrated Sensing And Communication (ISAC)").  Only a
        # unique agenda acronym is evidence strong enough to use; terms such as
        # NR or AI appear in several items and must remain unaligned.
        if not cands and len(abbreviations.get(key, [])) == 1:
            cands = [i for i in abbreviations[key] if i.item not in used]

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
