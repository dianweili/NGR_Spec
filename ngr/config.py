from __future__ import annotations
import re
from dataclasses import dataclass, field
from pathlib import Path
import yaml
from ngr.models import Feature, LineageSegment
from ngr.paths import P

VALID_DEPTHS = {"full", "origin", "milestone"}
VALID_BACKENDS = {"cli", "none"}

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class WgConfig:
    path: str
    dir_re: str
    hard_floor: int
    """允许回溯的最早会议号，安全钳位 —— 防止血统段配错导致失控回溯。
    **不是**语义边界：实测 RAN4/plenary 的频谱 WI 与新 WI/SI 提案远早于版本开工就上议程，
    "Rel-18 起始会议"这个定义对它们不成立。取值宁宽勿窄，真正的范围由血统段决定。"""
    agenda_csv_since: int | None
    """agenda.csv **最早出现**的会议号；不表示此后每次都有。
    实测 RAN2 #131 无 agenda.csv 而 #130/#132 都有 —— 缺口是正常现象，不得据此硬失败。"""
    minutes_re: str
    """该组纪要文件名的正则。必须按组配置：实测 RAN1 是 Draft_Minutes_report_RAN1#N_v###.docx，
    而 RAN2 就是个 TDoc 号 R2-2604502.zip（文件名里没有 minutes 字样），RAN3 三种形态并存。
    用一条全局正则会让除 RAN1 外的所有组零匹配、静默产出空结果。"""
    artifacts: list[str]
    report_dirs: list[str] = field(default_factory=lambda: ["Report"])
    """纪要所在子目录的候选名，按顺序取第一个在会议根目录列表中出现的。
    必须是列表：实测 RAN4 老会议用复数 "Reports"、新会议用单数 "Report"，
    单值字段会让回填到老会议时整段抓不到纪要。"""
    ls_dirs: list[str] = field(default_factory=lambda: ["LS"])
    """LS 目录名，实测有 LS / LSin+LSout / Reports 等多种写法。"""
    latest_meeting_with_content: int | None = None
    """最新的**已召开**会议号。实测四组的最新目录常常只有 Invitation（会议未召开），
    用目录列表的最大值会让冻结逻辑把最新的有内容会议提前冻住（见 Task 20）。"""

@dataclass(frozen=True)
class HttpConfig:
    user_agent: str
    concurrency: int
    delay_seconds: float
    retry_backoff: list[int]
    connect_timeout: float
    read_timeout: float

@dataclass(frozen=True)
class ExtractConfig:
    backend: str
    max_calls_per_run: int
    batch_size: int
    model_bulk: str
    model_digest: str

@dataclass(frozen=True)
class SourcesConfig:
    wgs: dict[str, WgConfig]
    http: HttpConfig
    extract: ExtractConfig

def _require(d: dict, key: str, where: str):
    if key not in d:
        raise ConfigError(f"{where} 缺少必填项 '{key}'")
    return d[key]

def load_sources(path: Path | None = None) -> SourcesConfig:
    path = path or P.config / "sources.yaml"
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}

    wgs = {}
    for name, raw in _require(data, "sources", "sources.yaml").items():
        where = f"sources.{name}"
        try:
            re.compile(_require(raw, "dir_re", where))
        except re.error as exc:
            raise ConfigError(f"{where}.dir_re 不是合法正则: {exc}") from exc
        minutes_re = _require(raw, "minutes_re", where)
        try:
            re.compile(minutes_re)
        except re.error as exc:
            raise ConfigError(f"{where}.minutes_re 不是合法正则: {exc}") from exc
        wgs[name] = WgConfig(
            path=_require(raw, "path", where),
            dir_re=raw["dir_re"],
            hard_floor=int(_require(raw, "hard_floor", where)),
            agenda_csv_since=raw.get("agenda_csv_since"),
            minutes_re=minutes_re,
            artifacts=list(_require(raw, "artifacts", where)),
            report_dirs=list(raw.get("report_dirs", [raw.get("report_dir", "Report")])),
            ls_dirs=list(raw.get("ls_dirs", ["LS"])),
            latest_meeting_with_content=raw.get("latest_meeting_with_content"),
        )
    if not wgs:
        raise ConfigError("sources.yaml 未定义任何工作组")

    h = _require(data, "http", "sources.yaml")
    http = HttpConfig(
        user_agent=_require(h, "user_agent", "http"),
        concurrency=int(h.get("concurrency", 1)),
        delay_seconds=float(h.get("delay_seconds", 2.0)),
        retry_backoff=list(h.get("retry_backoff", [2, 8, 30])),
        connect_timeout=float(h.get("timeout", {}).get("connect", 10)),
        read_timeout=float(h.get("timeout", {}).get("read", 300)),
    )
    if "Mozilla" not in http.user_agent:
        raise ConfigError(
            "http.user_agent 必须伪装浏览器（含 Mozilla），否则 3GPP 的 WAF 返回 403")

    e = _require(data, "extract", "sources.yaml")
    backend = _require(e, "backend", "extract")
    if backend not in VALID_BACKENDS:
        raise ConfigError(f"extract.backend 只能是 {sorted(VALID_BACKENDS)}，得到 '{backend}'")
    extract = ExtractConfig(
        backend=backend,
        max_calls_per_run=int(e.get("max_calls_per_run", 60)),
        batch_size=int(e.get("batch_size", 40)),
        model_bulk=e.get("model_bulk", "sonnet"),
        model_digest=e.get("model_digest", "opus"),
    )
    return SourcesConfig(wgs=wgs, http=http, extract=extract)

def _parse_segment(raw: dict, where: str, default_depth: str) -> LineageSegment:
    anchor = raw.get("anchor") or {}
    agenda = list(anchor.get("agenda", []))
    title_re = anchor.get("title_re")
    if not agenda and not title_re:
        raise ConfigError(f"{where}.anchor 必须至少给出 agenda 或 title_re 之一")
    if title_re:
        try:
            re.compile(title_re)
        except re.error as exc:
            raise ConfigError(f"{where}.anchor.title_re 不是合法正则: {exc}") from exc

    depth = raw.get("depth", default_depth)
    if depth not in VALID_DEPTHS:
        raise ConfigError(f"{where}.depth 只能是 {sorted(VALID_DEPTHS)}，得到 '{depth}'")

    meetings_raw = _require(raw, "meetings", where)
    meetings: dict[str, tuple[int, int | None]] = {}
    for wg, rng in meetings_raw.items():
        if not isinstance(rng, list) or len(rng) != 2:
            raise ConfigError(f"{where}.meetings.{wg} 必须是 [起, 止] 两元列表，止可为 null")
        lo, hi = rng
        if hi is not None and int(hi) < int(lo):
            raise ConfigError(f"{where}.meetings.{wg} 区间倒置: [{lo}, {hi}]")
        meetings[wg] = (int(lo), None if hi is None else int(hi))
    if not meetings:
        raise ConfigError(f"{where}.meetings 不能为空")

    return LineageSegment(
        era=_require(raw, "era", where), release=_require(raw, "release", where),
        depth=depth, agenda=agenda, title_re=title_re, meetings=meetings,
    )

def load_features(path: Path | None = None) -> list[Feature]:
    path = path or P.config / "features.yaml"
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    default_depth = data.get("default_depth", "origin")
    if default_depth not in VALID_DEPTHS:
        raise ConfigError(f"default_depth 只能是 {sorted(VALID_DEPTHS)}")

    feats, seen = [], set()
    for i, raw in enumerate(_require(data, "features", "features.yaml")):
        slug = _require(raw, "slug", f"features[{i}]")
        if slug in seen:
            raise ConfigError(f"重复的特性 slug: '{slug}'")
        seen.add(slug)
        segs_raw = _require(raw, "lineage", f"features[{slug}]")
        if not segs_raw:
            raise ConfigError(f"features[{slug}].lineage 不能为空")
        segs = [_parse_segment(s, f"features[{slug}].lineage[{j}]", default_depth)
                for j, s in enumerate(segs_raw)]
        feats.append(Feature(slug=slug, name_zh=_require(raw, "name_zh", f"features[{slug}]"),
                             lineage=segs))
    return feats
