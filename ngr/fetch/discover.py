from __future__ import annotations
import logging, re
from ngr.config import WgConfig
from ngr.fetch.listing import parse_listing
from ngr.models import Feature, Meeting

log = logging.getLogger(__name__)
BASE = "https://www.3gpp.org/ftp/"

def discover_meetings(http, wg: str, cfg: WgConfig) -> list[Meeting]:
    """列出该工作组下全部会议目录。新会议自动被发现，无需手工登记。"""
    dir_url = BASE + cfg.path.strip("/") + "/"
    names = parse_listing(http.get(dir_url), dir_url)
    pat = re.compile(rf"^{cfg.dir_re}$")
    out = []
    for name in names:
        m = pat.match(name)
        if not m:
            continue
        out.append(Meeting(wg=wg, number=int(m.group(1)), suffix=m.group(2) or "",
                           url=dir_url + name + "/"))
    return sorted(out, key=lambda m: (m.number, m.suffix))

def fetch_window(features: list[Feature], wg: str,
                 cfg: WgConfig) -> tuple[int, int | None] | None:
    """抓取区间 = 所有血统段在该工作组上的并集，再被 hard_floor 截断。
    返回 None 表示没有任何特性关心这个工作组。"""
    lows, highs, unbounded = [], [], False
    for feat in features:
        for seg in feat.lineage:
            rng = seg.meetings.get(wg)
            if rng is None:
                continue
            lo, hi = rng
            lows.append(lo)
            if hi is None:
                unbounded = True
            else:
                highs.append(hi)
    if not lows:
        return None
    low = max(min(lows), cfg.hard_floor)
    if unbounded:
        return (low, None)
    high = max(highs)
    if high < low:
        # 该组的血统段全部落在 hard_floor 之下，被钳位成空。
        # 必须归一化为 None，不能返回 (low, high) 这种 lo > hi 的倒置区间 ——
        # 类型合法但语义非法，下游按 range(lo, hi+1) 消费会得到空循环或负数统计，
        # 且分不清是"没有特性覆盖这个组"还是"被 hard_floor 钳没了"。
        log.warning("%s 的血统段全部低于 hard_floor=%d（最高 %d），本组无可抓取区间",
                    wg, cfg.hard_floor, high)
        return None
    return (low, high)
