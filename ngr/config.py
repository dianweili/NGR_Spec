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

def _as_dict(value, path: str) -> dict:
    """显式的容器类型校验。父容器类型错了（`http: "fast"`、`extract: []`、
    某个工作组写成字符串……）不显式检查的话，会在后面 `.get()`/`.items()` 那一步
    抛一句与配置无关的裸 Python 异常（AttributeError 等），排查起来比类型错误更糟。
    宁可多写几行，也不用 `except Exception` 兜底 —— 那样会把加载器自身的真实 bug
    也一起伪装成配置错误。"""
    if not isinstance(value, dict):
        raise ConfigError(f"{path} 必须是映射，得到 {type(value).__name__}")
    return value

def _as_list(value, path: str) -> list:
    if not isinstance(value, list):
        raise ConfigError(f"{path} 必须是列表，得到 {type(value).__name__}")
    return value

def _to_int(value, path: str) -> int:
    """把 value 转成 int，转不动时抛 ConfigError 并带上完整字段路径，
    不让用户看着一句裸的 `invalid literal for int()` 猜是哪个字段。"""
    try:
        return int(value)
    except (TypeError, ValueError) as exc:
        raise ConfigError(f"{path} 必须是整数，得到 {value!r}") from exc

def _to_int_or_none(value, path: str) -> int | None:
    if value is None:
        return None
    return _to_int(value, path)

def _to_float(value, path: str) -> float:
    """同 _to_int，但用于允许小数的字段（int 写法也能转，例如 delay_seconds: 2）。"""
    try:
        return float(value)
    except (TypeError, ValueError) as exc:
        raise ConfigError(f"{path} 必须是数字，得到 {value!r}") from exc

def _to_int_min(value, path: str, minimum: int) -> int:
    """类型对但取值无意义的配置（如 concurrency: 0）同样是启动时就该炸的错误 ——
    concurrency: 0 会让抓取层一个请求都发不出去，却不会有任何异常提示。"""
    n = _to_int(value, path)
    if n < minimum:
        raise ConfigError(f"{path} 必须 >= {minimum}，得到 {n}")
    return n

def _to_float_min(value, path: str, minimum: float) -> float:
    n = _to_float(value, path)
    if n < minimum:
        raise ConfigError(f"{path} 必须 >= {minimum}，得到 {n}")
    return n

def _to_number_list(value, path: str) -> list[int]:
    if not isinstance(value, list):
        raise ConfigError(f"{path} 必须是数值列表，得到 {value!r}")
    return [_to_int(v, f"{path}[{i}]") for i, v in enumerate(value)]

def load_sources(path: Path | None = None) -> SourcesConfig:
    path = path or P.config / "sources.yaml"
    data = _as_dict(yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}, "sources.yaml")

    sources_raw = _as_dict(_require(data, "sources", "sources.yaml"), "sources")
    wgs = {}
    for name, raw in sources_raw.items():
        where = f"sources.{name}"
        raw = _as_dict(raw, where)
        try:
            re.compile(_require(raw, "dir_re", where))
        except (re.error, TypeError) as exc:
            raise ConfigError(f"{where}.dir_re 不是合法正则: {exc}") from exc
        minutes_re = _require(raw, "minutes_re", where)
        try:
            re.compile(minutes_re)
        except (re.error, TypeError) as exc:
            raise ConfigError(f"{where}.minutes_re 不是合法正则: {exc}") from exc

        artifacts = list(_as_list(_require(raw, "artifacts", where), f"{where}.artifacts"))
        report_dirs_raw = raw.get("report_dirs")
        report_dirs = ([raw.get("report_dir", "Report")] if report_dirs_raw is None
                        else list(_as_list(report_dirs_raw, f"{where}.report_dirs")))
        ls_dirs_raw = raw.get("ls_dirs")
        ls_dirs = ["LS"] if ls_dirs_raw is None else list(_as_list(ls_dirs_raw, f"{where}.ls_dirs"))

        wgs[name] = WgConfig(
            path=_require(raw, "path", where),
            dir_re=raw["dir_re"],
            hard_floor=_to_int(_require(raw, "hard_floor", where), f"{where}.hard_floor"),
            agenda_csv_since=_to_int_or_none(raw.get("agenda_csv_since"), f"{where}.agenda_csv_since"),
            minutes_re=minutes_re,
            artifacts=artifacts,
            report_dirs=report_dirs,
            ls_dirs=ls_dirs,
            latest_meeting_with_content=_to_int_or_none(
                raw.get("latest_meeting_with_content"), f"{where}.latest_meeting_with_content"),
        )
    if not wgs:
        raise ConfigError("sources.yaml 未定义任何工作组")

    h = _as_dict(_require(data, "http", "sources.yaml"), "http")
    timeout_raw = h.get("timeout")
    timeout = {} if timeout_raw is None else _as_dict(timeout_raw, "http.timeout")
    http = HttpConfig(
        user_agent=_require(h, "user_agent", "http"),
        concurrency=_to_int_min(h.get("concurrency", 1), "http.concurrency", 1),
        delay_seconds=_to_float_min(h.get("delay_seconds", 2.0), "http.delay_seconds", 0.0),
        retry_backoff=_to_number_list(h.get("retry_backoff", [2, 8, 30]), "http.retry_backoff"),
        connect_timeout=_to_float(timeout.get("connect", 10), "http.timeout.connect"),
        read_timeout=_to_float(timeout.get("read", 300), "http.timeout.read"),
    )
    if "Mozilla" not in http.user_agent:
        raise ConfigError(
            "http.user_agent 必须伪装浏览器（含 Mozilla），否则 3GPP 的 WAF 返回 403")

    e = _as_dict(_require(data, "extract", "sources.yaml"), "extract")
    backend = _require(e, "backend", "extract")
    if backend not in VALID_BACKENDS:
        raise ConfigError(f"extract.backend 只能是 {sorted(VALID_BACKENDS)}，得到 '{backend}'")
    extract = ExtractConfig(
        backend=backend,
        max_calls_per_run=_to_int_min(e.get("max_calls_per_run", 60), "extract.max_calls_per_run", 1),
        batch_size=_to_int_min(e.get("batch_size", 40), "extract.batch_size", 1),
        model_bulk=e.get("model_bulk", "sonnet"),
        model_digest=e.get("model_digest", "opus"),
    )
    return SourcesConfig(wgs=wgs, http=http, extract=extract)

def _parse_segment(raw: dict, where: str, default_depth: str) -> LineageSegment:
    anchor_raw = raw.get("anchor")
    anchor = {} if anchor_raw is None else _as_dict(anchor_raw, f"{where}.anchor")
    agenda = list(_as_list(anchor.get("agenda", []), f"{where}.anchor.agenda"))
    title_re = anchor.get("title_re")
    if not agenda and not title_re:
        raise ConfigError(f"{where}.anchor 必须至少给出 agenda 或 title_re 之一")
    if title_re:
        try:
            re.compile(title_re)
        except (re.error, TypeError) as exc:
            raise ConfigError(f"{where}.anchor.title_re 不是合法正则: {exc}") from exc

    depth = raw.get("depth", default_depth)
    if depth not in VALID_DEPTHS:
        raise ConfigError(f"{where}.depth 只能是 {sorted(VALID_DEPTHS)}，得到 '{depth}'")

    meetings_raw = _as_dict(_require(raw, "meetings", where), f"{where}.meetings")
    meetings: dict[str, tuple[int, int | None]] = {}
    for wg, rng in meetings_raw.items():
        if not isinstance(rng, list) or len(rng) != 2:
            raise ConfigError(f"{where}.meetings.{wg} 必须是 [起, 止] 两元列表，止可为 null")
        lo_raw, hi_raw = rng
        lo = _to_int(lo_raw, f"{where}.meetings.{wg}[0]")
        hi = _to_int_or_none(hi_raw, f"{where}.meetings.{wg}[1]")
        if hi is not None and hi < lo:
            raise ConfigError(f"{where}.meetings.{wg} 区间倒置: [{lo}, {hi}]")
        meetings[wg] = (lo, hi)
    if not meetings:
        raise ConfigError(f"{where}.meetings 不能为空")

    return LineageSegment(
        era=_require(raw, "era", where), release=_require(raw, "release", where),
        depth=depth, agenda=agenda, title_re=title_re, meetings=meetings,
    )

def load_features(path: Path | None = None) -> list[Feature]:
    path = path or P.config / "features.yaml"
    data = _as_dict(yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}, "features.yaml")
    default_depth = data.get("default_depth", "origin")
    if default_depth not in VALID_DEPTHS:
        raise ConfigError(f"default_depth 只能是 {sorted(VALID_DEPTHS)}")

    features_raw = _as_list(_require(data, "features", "features.yaml"), "features")

    feats, seen = [], set()
    for i, raw in enumerate(features_raw):
        raw = _as_dict(raw, f"features[{i}]")
        slug = _require(raw, "slug", f"features[{i}]")
        if slug in seen:
            raise ConfigError(f"重复的特性 slug: '{slug}'")
        seen.add(slug)
        segs_raw = _as_list(_require(raw, "lineage", f"features[{slug}]"), f"features[{slug}].lineage")
        if not segs_raw:
            raise ConfigError(f"features[{slug}].lineage 不能为空")
        segs = [_parse_segment(_as_dict(s, f"features[{slug}].lineage[{j}]"),
                                f"features[{slug}].lineage[{j}]", default_depth)
                for j, s in enumerate(segs_raw)]
        feats.append(Feature(slug=slug, name_zh=_require(raw, "name_zh", f"features[{slug}]"),
                             lineage=segs))
    if not feats:
        raise ConfigError("features.yaml 未定义任何特性")
    return feats
