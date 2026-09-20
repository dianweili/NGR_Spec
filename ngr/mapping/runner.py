from __future__ import annotations
import hashlib, json, logging, re
from collections import defaultdict
from dataclasses import dataclass, asdict, field
from pathlib import Path
from ngr.mapping.lineage import match_event
from ngr.models import Event, Feature

log = logging.getLogger(__name__)

_SLUG_RE = re.compile(r"[^A-Za-z0-9.]+")

def _agenda_key(agenda_item: str | None, heading_path: list[str]) -> str:
    """没有议程号时（5G-A 老会议）用 heading 末节造一个稳定的 key。

    回退 key 必须带上原始 heading 的短哈希。标点归一化会把不同议题撞成同一个 key ——
    实测 "ISAC channel model" 与 "ISAC channel-model" 都归一化成 `isac-channel-model`，
    "CSI enhancement: further study" 与去掉冒号的写法同理。撞 key 之后 seq 按遍历顺序
    分配，两次纪要修订之间只要这两个议题的先后调换，**同一个 id 就会指向另一个议题**：
    merge 会判成一次普通的内容变更，把 A 的历史（first_seen 等）安到 B 头上，
    既不报错也不进 stale_ids，**彻底静默**。

    哈希取自**未归一化的完整 heading 路径**，不是只取末节。只取末节的话，
    "Overview" / "General" / "Way forward" 这类通用小节名在不同 Release、不同上级章节下
    **100% 撞车**（实测 `["Rel-17 NR","Overview"]` 与 `["Rel-18 NR","Overview"]` 同 key），
    而它们在 3GPP 纪要里反复出现 —— 这比标点变体常见得多。

    编码用**长度前缀**而不是拼接分隔符。用 `"/".join(...)` 曾经撞过车：3GPP 标题里
    "UL/DL switching"、"Tx/Rx"、"PDCCH/PDSCH" 这类写法很常见，于是
    `["UL/DL switching", "Way forward"]` 与 `["UL", "DL switching", "Way forward"]`
    拼出同一个串、哈希相同、末节也相同 —— **完整 key 100% 撞车，且加长哈希位数毫无用处**
    （这是确定性字符串碰撞，不是随机碰撞）。换任何"内容里不会出现的分隔符"都是在赌，
    本项目已经为这个赌注付过两次代价（另一次见 Task 18 的逐行 blob）。
    长度前缀不需要任何关于内容的假设，可证单射。

    **注意**：改动这里的哈希算法会让所有 fallback key（无议程号的 5G-A 老会议）的事件 id
    整体变化。当前尚无 state 落盘，改动零代价；一旦 Task 20 跑出真实 state，
    再改就需要写迁移，否则旧 id 全部变成孤儿、新 id 全部被当成首次出现。"""
    if agenda_item:
        return agenda_item
    tail = heading_path[-1] if heading_path else "unknown"
    if not heading_path:
        # 没有任何标题路径时，所有此类事件共享同一个 key，身份只能靠组内 seq 区分。
        # 这是**已知限制**，不是漏修：用 text_en 入 key 能区分开，但正文被编辑一下
        # id 就变了 —— 换来的是更常见、更伤的那类故障（孤儿 + 假新增）。
        log.warning("legacy 事件缺 heading_path，回退 key 不具区分度（全部落到同一个 key）")
    slug = _SLUG_RE.sub("-", tail).strip("-").lower()[:40] or "unknown"
    # 长度前缀编码：每一级写成 "<长度>:<原文>"，无论原文含什么字符都能唯一还原
    full = "".join(f"{len(h)}:{h}" for h in heading_path) or "0:"
    return f"{slug}-{hashlib.sha256(full.encode('utf-8')).hexdigest()[:8]}"

def _hash(text: str) -> str:
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()

def map_meeting(parsed: dict, features: list[Feature],
                meeting_end: str | None = None) -> list[Event]:
    wg, meeting = parsed["wg"], parsed["meeting"]
    counters: dict[tuple[str, str], int] = defaultdict(int)
    out: list[Event] = []

    for raw in parsed["events"]:
        m = match_event(features, wg, meeting,
                        raw.get("agenda_item"), raw.get("heading_path") or [])
        if m is None:
            continue
        if m.segment.depth == "milestone" and raw["kind"] == "agreement":
            continue          # milestone 段只收转折点

        key = _agenda_key(raw.get("agenda_item"), raw.get("heading_path") or [])
        counters[(key, raw["kind"])] += 1
        out.append(Event(
            wg=wg, meeting=meeting, agenda_item=key,
            seq=counters[(key, raw["kind"])], kind=raw["kind"],
            text_en=raw["text_en"], agenda_title=raw.get("agenda_title", ""),
            meeting_end=meeting_end,
            era=m.segment.era, release=m.segment.release, depth=m.segment.depth,
            feature=m.feature_slug,
            source={"minutes_version": parsed.get("minutes_version"),
                    "para": raw.get("para_index")},
            llm_status="pending" if m.segment.depth == "full" else "skipped_by_depth",
            content_hash=_hash(raw["text_en"]),
        ))
    return out

@dataclass
class MergeStats:
    added: int = 0
    changed: int = 0
    unchanged: int = 0
    added_ids: list[str] = field(default_factory=list)
    """新增事件的 id。提交信息按它统计每特性新增数 —— 不能用整批 incoming，
    否则未变更的事件也会被计进'本次新增'。"""
    stale_ids: list[str] = field(default_factory=list)
    """本次解析中不再出现、但仍留在 state 里的事件 id。

    事件 id 是位置式的（`RAN1-126-10.2-a003`），纪要出新版本、中间插入或删掉一条
    agreement 时，后续事件的 seq 会整体位移。被删掉的那条对应的末位 id 从此无人认领，
    **永久留在 state 里**，看板上会一直显示一条实际已不存在的 agreement。

    **只报告不删除**：若某次 parse 回归（比如正则改动）让事件暂时缺失，删除就是永久
    数据丢失 —— 那正是本项目最怕的。缺失是信号，不是指令。"""

# 事件变更时要作废的 LLM 产物
_LLM_FIELDS = {"summary_zh": None, "tags": [], "impact": None, "llm_status": "pending"}

def merge_events(existing: list[dict], incoming: list[Event], today: str,
                 *, scope: set[tuple[str, int]]) -> tuple[list[dict], MergeStats]:
    by_id = {e["id"]: dict(e) for e in existing}
    stats = MergeStats()

    for ev in incoming:
        new = asdict(ev)
        new["id"] = ev.id
        old = by_id.get(ev.id)
        if old is None:
            new["first_seen"] = today
            by_id[ev.id] = new
            stats.added += 1
            stats.added_ids.append(ev.id)
            continue

        new["first_seen"] = old.get("first_seen", today)
        if old.get("content_hash") == new["content_hash"]:
            # 正文未变：保留既有 LLM 产物
            for k in ("summary_zh", "tags", "impact", "llm_status"):
                if k in old:
                    new[k] = old[k]
            stats.unchanged += 1
        else:
            if new["depth"] == "full":
                new.update(_LLM_FIELDS)
            stats.changed += 1
        by_id[ev.id] = new

    # scope = 本次处理了哪几场会议，**必填**。existing 是全量 state，比较必须限定在
    # 同一 (wg, meeting) 范围内，否则所有历史会议的事件都会被当成"本次缺失"。
    #
    # 不给默认值、不做隐式反推：某场会议一旦归集归零（features.yaml 改坏、正则回归），
    # 它就不在反推出的 scope 里，那场的全部历史一条都不会被比较，stale_ids 恒为空 ——
    # 局部缺失会报警、全部缺失反而不报警，探针恰好在最该响的时候哑火。
    # 确实需要反推时，在**调用点内联**写出 {(ev.wg, ev.meeting) for ev in incoming}。
    # 不提供现成的反推函数：上一轮我加过一个 scope_of()，结果自己的测试里 9 处调用
    # 有 6 处图省事用了它 —— 一个"看起来官方、有文档警告但无强制力"的旁路，
    # 等于把盲区从签名默认值搬到了函数名上。让反推每次都得手写，风险才在每个调用点可见。
    seen = {ev.id for ev in incoming}
    for e in existing:
        if (e.get("wg"), e.get("meeting")) in scope and e["id"] not in seen:
            stats.stale_ids.append(e["id"])
    if stats.stale_ids:
        log.warning("state 里有 %d 条事件在本次解析中不再出现（保留不删，仅报告）: %s",
                    len(stats.stale_ids), ", ".join(sorted(stats.stale_ids)[:5]))

    return list(by_id.values()), stats

def write_state(events: list[dict], path: Path) -> Path:
    """按 id 排序后写出。顺序稳定是幂等性的前提 —— 否则 git diff 全是噪声。"""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = sorted(events, key=lambda e: e["id"])
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True),
                    encoding="utf-8")
    return path
