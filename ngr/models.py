from __future__ import annotations
from dataclasses import dataclass, field

KIND_PREFIX = {"agreement": "a", "conclusion": "c",
               "working_assumption": "w", "observation": "o", "proposal": "p"}

@dataclass(frozen=True)
class Meeting:
    wg: str
    number: int
    suffix: str
    url: str

    @property
    def label(self) -> str:
        return f"{self.wg}#{self.number}{self.suffix}"

    @property
    def key(self) -> str:
        """Directory and identity-safe meeting key, for example ``124b``."""
        return f"{self.number}{self.suffix}"

@dataclass(frozen=True)
class AgendaItem:
    item: str          # "10.2"
    title: str

    @property
    def depth(self) -> int:
        return self.item.count(".") + 1

@dataclass(frozen=True)
class Heading:
    level: int         # Heading1 -> 1
    text: str
    para_index: int

@dataclass
class RawEvent:
    """parse 层产物：尚未归属特性。"""
    kind: str
    text_en: str
    para_index: int
    heading_path: list[str] = field(default_factory=list)

@dataclass
class Event:
    """state 层产物：已归属特性与血统。"""
    wg: str
    meeting: int
    agenda_item: str
    seq: int
    kind: str
    text_en: str
    agenda_title: str
    meeting_suffix: str = ""
    meeting_end: str | None = None
    era: str | None = None
    release: str | None = None
    depth: str = "full"
    feature: str | None = None
    source: dict = field(default_factory=dict)
    summary_zh: str | None = None
    tags: list[str] = field(default_factory=list)
    impact: str | None = None
    llm_status: str = "pending"
    first_seen: str | None = None
    content_hash: str | None = None

    @property
    def id(self) -> str:
        return f"{self.wg}-{self.meeting}{self.meeting_suffix}-{self.agenda_item}-{KIND_PREFIX[self.kind]}{self.seq:03d}"

@dataclass(frozen=True)
class LineageSegment:
    era: str                       # "6G" | "5G-A"
    release: str
    depth: str                     # "full" | "origin" | "milestone"
    agenda: list[str]              # ["RAN1:10.2", "RAN1:10.2.*"]
    title_re: str | None
    meetings: dict[str, tuple[int, int | None]]   # {"RAN1": (124, None)}
    meeting_suffixes: tuple[str, ...] | None = None
    """Optional suffix filter applying across the entire meeting range.

    ``("",)`` selects ordinary sessions only, letting an old agenda chapter
    stop before a same-number special session changes its meaning.
    """
    meeting_start_suffixes: tuple[str, ...] | None = None
    """Suffixes eligible at the range's first meeting, e.g. ``("bis",)``.

    RAN2#133bis introduced the new 6GR chapter numbering while ordinary #133
    still used the old tree.  This selector restricts only the lower boundary;
    later meetings in the same range are eligible regardless of suffix.
    """

    def covers(self, wg: str, meeting: int, suffix: str = "") -> bool:
        rng = self.meetings.get(wg)
        if rng is None:
            return False
        lo, hi = rng
        if not (lo <= meeting and (hi is None or meeting <= hi)):
            return False
        if self.meeting_suffixes is not None and suffix not in self.meeting_suffixes:
            return False
        return meeting != lo or self.meeting_start_suffixes is None or suffix in self.meeting_start_suffixes

@dataclass(frozen=True)
class Feature:
    slug: str
    name_zh: str
    lineage: list[LineageSegment]

    @property
    def has_legacy(self) -> bool:
        return any(s.era == "5G-A" for s in self.lineage)
