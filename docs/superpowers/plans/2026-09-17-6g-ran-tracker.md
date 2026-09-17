# 6G RAN 进展跟踪工具 实现计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 构建 `ngr` 命令行工具，每日自动抓取 3GPP RAN 会议纪要，按特性血统归集 6G 与相关 5G-A 的 agreement，产出可 diff 的 Markdown 看板与网页。

**Architecture:** 五层落盘管线 `fetch → parse → map → extract → render`，层间只通过 JSON 通信。fetch 是唯一联网层，extract 是唯一调 LLM 层（走 `claude -p` CLI），其余为纯函数，可离线重跑。

**Tech Stack:** Python 3.14 / requests / PyYAML / pytest / responses；stdlib 的 zipfile、csv、difflib、subprocess。无编译型依赖。

**Spec:** `docs/superpowers/specs/2026-09-17-6g-ran-tracker-design.md`

## Global Constraints

- **HTTP UA 必须伪装浏览器**：`Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36`。默认 UA 被 WAF 挡成 403。
- **403 不得被解释为"文件不存在"**：WAF 限流与文件缺失都返回 403。判断文件存在性一律先读目录列表。
- **并发 2、请求间隔 0.5s、退避 [2,8,30]、超时 (连接 10s, 读取 300s)**。
- **LLM 只能走 `claude -p`**，禁用 `--bare`（该模式不读 OAuth，会绕开 Max 订阅认证）。prompt 走 stdin 不走 argv。
- **`text_en` 逐字保留，永不让 LLM 改写。**
- **特性归类由规则决定**，LLM 只产出 `summary_zh`/`tags`/`impact`/`stage`/`legacy_summary`。
- **`data/raw/`、`data/parsed/`、`logs/` 不进 git；`data/state/`、`out/` 进 git。**
- **测试中绝不联网、绝不调真实 LLM。**
- 所有 commit 消息末尾加：`Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>`

---

## 文件结构

| 文件 | 职责 |
|---|---|
| `ngr/paths.py` | 仓库内所有路径的唯一来源 |
| `ngr/models.py` | 数据类：`Meeting` `AgendaItem` `Heading` `RawEvent` `Event` `LineageSegment` `Feature` |
| `ngr/config.py` | `sources.yaml` / `features.yaml` 加载与校验 |
| `ngr/fetch/client.py` | HTTP 客户端：UA、限流退避、403 语义 |
| `ngr/fetch/listing.py` | 目录列表 HTML → 文件名/子目录 |
| `ngr/fetch/discover.py` | 会议发现 + 抓取区间（血统并集 ∩ hard_floor） |
| `ngr/fetch/manifest.py` | 增量 manifest、frozen 标记 |
| `ngr/fetch/runner.py` | 单次会议抓取编排 |
| `ngr/parse/agenda.py` | `agenda.csv` → `AgendaItem[]` |
| `ngr/parse/docx.py` | docx → 段落、heading、表格 |
| `ngr/parse/events.py` | agreement 块提取 |
| `ngr/parse/align.py` | heading ↔ 议程号对齐 |
| `ngr/parse/runner.py` | parse 编排 + 断言防线 |
| `ngr/mapping/lineage.py` | 血统段匹配引擎 |
| `ngr/mapping/runner.py` | map 编排 + `state/events.json` 写入 |
| `ngr/mapping/report.py` | `lineage-report` 命中对照表 |
| `ngr/extract/backend.py` | `claude -p` 子进程调用 |
| `ngr/extract/cache.py` | LLM 结果缓存 |
| `ngr/extract/budget.py` | 配额守护 + `usage_log.jsonl` |
| `ngr/extract/tasks.py` | 四项 LLM 任务的 prompt 与 schema 校验 |
| `ngr/extract/runner.py` | extract 编排 |
| `ngr/render/markdown.py` | dashboard / features / reports |
| `ngr/render/site.py` | 单文件 HTML 看板 |
| `ngr/ops/alerts.py` | `ALERTS.md`、dashboard 横幅、心跳检查 |
| `ngr/ops/gitio.py` | 自动 commit |
| `ngr/ops/doctor.py` | 自检 |
| `ngr/cli.py` | argparse 命令面与退出码 |

> 包名用 `ngr/mapping/` 而非 `ngr/map/` —— `map` 是 Python 内置函数名，做包名会在 `from ngr import map` 时造成混淆。

## 任务顺序说明

渲染层（Task 14–15）排在 LLM 层（Task 16–17）**之前**。这样 Task 15 结束时就得到一个完全可用的无 LLM 工具：能抓、能解析、能出看板，只是没有中文摘要。先拿到可用产物再加增强，比反过来更早验证整条链路。

**两个里程碑：**
- **Task 13 完成** → `ngr run --no-llm` 能把 agreement 填进 `state/events.json`
- **Task 15 完成** → 完整看板可读，工具已经有用

---

## Phase 0：侦察与地基

### Task 1: 站点侦察，填实配置与测试 fixture

Spec §10 列出三项未经实测的假设。先探明再写代码 —— 后面所有测试断言都依赖这里的产出。

**Files:**
- Create: `config/sources.yaml`
- Create: `docs/superpowers/recon-2026-09-17.md`
- Create: `tests/fixtures/RAN1_126/{agenda.csv,minutes.docx,docs_listing.html}`
- Create: `tests/fixtures/RAN1_120/{minutes.docx,agenda_listing.html}`
- Create: `scripts/recon.py`

**Interfaces:**
- Consumes: 无（首个任务）
- Produces: `config/sources.yaml`，键为 `RAN1/RAN2/RAN3/RAN4/RANP`，每项含 `path` `dir_re` `hard_floor` `artifacts` `agenda_csv_since`；测试 fixture 文件

- [ ] **Step 1: 写侦察脚本**

```python
# scripts/recon.py
"""一次性侦察脚本：探明各工作组目录布局，抓取测试 fixture。
限速严格 —— 3GPP 的 WAF 会在密集请求下返回 403。"""
import time, pathlib, re, sys, requests

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36")
BASE = "https://www.3gpp.org/ftp/"
S = requests.Session()
S.headers["User-Agent"] = UA

def get(path: str, tries: int = 3) -> bytes | None:
    """返回内容；403 一律当限流，退避重试；最终失败返回 None。"""
    for i, backoff in enumerate([2, 8, 30][:tries]):
        r = S.get(BASE + path, timeout=(10, 300))
        if r.status_code == 200:
            time.sleep(3)          # 侦察阶段用 3s，比生产的 0.5s 更保守
            return r.content
        print(f"  {path} -> {r.status_code}, 退避 {backoff}s", file=sys.stderr)
        time.sleep(backoff)
    return None

def entries(html: bytes, prefix: str) -> list[str]:
    """从目录列表 HTML 抽出该目录下的条目名。"""
    pat = re.escape(prefix.rstrip("/")) + r'/([^"/]+)'
    return sorted(set(re.findall(pat, html.decode("utf-8", "ignore"))))

if __name__ == "__main__":
    for wg, path in [("RAN1", "tsg_ran/WG1_RL1/"), ("RAN2", "tsg_ran/WG2_RL2/"),
                     ("RAN3", "tsg_ran/WG3_Iu/"), ("RAN4", "tsg_ran/WG4_Radio/"),
                     ("RANP", "tsg_ran/TSG_RAN/")]:
        html = get(path)
        print(f"\n=== {wg}  {path}  {'OK' if html else 'FAILED'}")
        if html:
            dirs = [e for e in entries(html, path) if re.match(r"TSGR", e)]
            print("  最近 5 个会议目录:", dirs[-5:])
```

- [ ] **Step 2: 跑侦察脚本，记录五个工作组的真实路径**

Run: `python scripts/recon.py`

对每个返回 FAILED 的工作组，手工试探正确路径（3GPP 的目录名不完全规则，例如 RAN3 可能是 `WG3_Iu`、RAN4 可能是 `WG4_Radio`），把确认结果写进 `docs/superpowers/recon-2026-09-17.md`。

- [ ] **Step 3: 确定 `agenda.csv` 的起始会议号**

对 RAN1 从 #118 到 #126 逐个探 `TSGR1_<n>/Agenda/`（**读目录列表，不要直接 GET `agenda.csv`** —— 403 分不清缺文件与限流），记录哪些目录里有 `agenda.csv`。每次请求间隔 ≥ 5 秒。结果写进侦察报告，并填入 `sources.yaml` 的 `agenda_csv_since`。

- [ ] **Step 4: 抓取 5G-A 时代的 heading 清单**

对 RAN1 #112–#122 各下载一份纪要 docx，抽出全部 heading 文本（用 spec §5 的 `w:pStyle` 方法），汇总成一张表写进侦察报告。这张表是 Task 12 里 5G-A `title_re` 的唯一依据 —— 没有它，血统正则只能靠猜。

- [ ] **Step 5: 保存测试 fixture**

```bash
mkdir -p tests/fixtures/RAN1_126 tests/fixtures/RAN1_120
# RAN1_126：6GR 时代，有 agenda.csv
#   agenda.csv, minutes.docx (Draft_Minutes_report_RAN1#126_v010.docx), docs_listing.html
# RAN1_120：5G-A 时代，无 agenda.csv
#   minutes.docx, agenda_listing.html (证明该目录下只有 TDoc zip)
```

`docs_listing.html` 裁到前 50 个条目即可，保留完整的 HTML 表格结构。

- [ ] **Step 6: 写 `config/sources.yaml`**

用 Step 2–3 的实测结果填写。下面是结构示例，**`path` 与数字必须换成实测值**：

```yaml
sources:
  RAN1:
    path: tsg_ran/WG1_RL1
    dir_re: 'TSGR1_(\d+)([a-z]*)'
    hard_floor: 112
    agenda_csv_since: 124
    artifacts: [agenda_csv, minutes_docx, docs_listing, ls_listing]
  # RAN2/RAN3/RAN4/RANP 同构，值由 Step 2 实测填入
http:
  user_agent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
  concurrency: 2
  delay_seconds: 0.5
  retry_backoff: [2, 8, 30]
  timeout: { connect: 10, read: 300 }
extract:
  backend: cli
  max_calls_per_run: 60
  batch_size: 40
  model_bulk: sonnet
  model_digest: opus
```

- [ ] **Step 7: Commit**

```bash
git add config/sources.yaml docs/superpowers/recon-2026-09-17.md scripts/recon.py tests/fixtures
git commit -m "chore: 站点侦察结果、sources.yaml、测试 fixture"
```

---

### Task 2: 项目骨架、路径与数据模型

**Files:**
- Create: `pyproject.toml`, `.gitignore`（已存在则补充）
- Create: `ngr/__init__.py`, `ngr/__main__.py`, `ngr/paths.py`, `ngr/models.py`
- Test: `tests/test_models.py`

**Interfaces:**
- Consumes: 无
- Produces: `ngr.paths.P`（路径单例，属性 `root/raw/parsed/state/out/logs/config`，方法 `raw_dir(wg, meeting) -> Path`）；`ngr.models` 的全部数据类

- [ ] **Step 1: 建虚拟环境并装依赖**

```bash
python -m venv .venv
.venv/Scripts/python.exe -m pip install --upgrade pip
.venv/Scripts/python.exe -m pip install requests PyYAML pytest responses
```

- [ ] **Step 2: 写 `pyproject.toml`**

```toml
[project]
name = "ngr"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = ["requests>=2.32", "PyYAML>=6.0"]

[project.optional-dependencies]
dev = ["pytest>=8.0", "responses>=0.25"]

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-q"
```

- [ ] **Step 3: 写失败的测试**

```python
# tests/test_models.py
from ngr.models import Event, Meeting, LineageSegment
from ngr.paths import P

def test_meeting_label():
    m = Meeting(wg="RAN1", number=126, suffix="", url="https://x/")
    assert m.label == "RAN1#126"
    assert Meeting(wg="RAN1", number=126, suffix="b", url="").label == "RAN1#126b"

def test_event_id_is_stable():
    e = Event(wg="RAN1", meeting=126, agenda_item="10.2", seq=17, kind="agreement",
              text_en="X", agenda_title="Waveform")
    assert e.id == "RAN1-126-10.2-a017"

def test_event_id_prefix_varies_by_kind():
    e = Event(wg="RAN1", meeting=126, agenda_item="10.2", seq=3, kind="conclusion",
              text_en="X", agenda_title="W")
    assert e.id == "RAN1-126-10.2-c003"

def test_lineage_segment_covers_meeting():
    seg = LineageSegment(era="6G", release="Rel-20", depth="full",
                         agenda=["RAN1:10.2"], title_re=None,
                         meetings={"RAN1": (124, None)})
    assert seg.covers("RAN1", 124) and seg.covers("RAN1", 999)
    assert not seg.covers("RAN1", 123)
    assert not seg.covers("RAN2", 200)

def test_paths_raw_dir():
    assert P.raw_dir("RAN1", 126) == P.raw / "RAN1" / "126"
```

- [ ] **Step 4: 跑测试确认失败**

Run: `.venv/Scripts/python.exe -m pytest tests/test_models.py -v`
Expected: FAIL，`ModuleNotFoundError: No module named 'ngr'`

- [ ] **Step 5: 写 `ngr/paths.py`**

```python
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Paths:
    root: Path

    @property
    def config(self) -> Path: return self.root / "config"
    @property
    def raw(self) -> Path: return self.root / "data" / "raw"
    @property
    def parsed(self) -> Path: return self.root / "data" / "parsed"
    @property
    def state(self) -> Path: return self.root / "data" / "state"
    @property
    def out(self) -> Path: return self.root / "out"
    @property
    def logs(self) -> Path: return self.root / "logs"

    def raw_dir(self, wg: str, meeting: int) -> Path:
        return self.raw / wg / str(meeting)

    def parsed_dir(self, wg: str, meeting: int) -> Path:
        return self.parsed / wg / str(meeting)

P = Paths(root=Path(__file__).resolve().parent.parent)
```

- [ ] **Step 6: 写 `ngr/models.py`**

```python
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
        return f"{self.wg}-{self.meeting}-{self.agenda_item}-{KIND_PREFIX[self.kind]}{self.seq:03d}"

@dataclass(frozen=True)
class LineageSegment:
    era: str                       # "6G" | "5G-A"
    release: str
    depth: str                     # "full" | "origin" | "milestone"
    agenda: list[str]              # ["RAN1:10.2", "RAN1:10.2.*"]
    title_re: str | None
    meetings: dict[str, tuple[int, int | None]]   # {"RAN1": (124, None)}

    def covers(self, wg: str, meeting: int) -> bool:
        rng = self.meetings.get(wg)
        if rng is None:
            return False
        lo, hi = rng
        return lo <= meeting and (hi is None or meeting <= hi)

@dataclass(frozen=True)
class Feature:
    slug: str
    name_zh: str
    lineage: list[LineageSegment]

    @property
    def has_legacy(self) -> bool:
        return any(s.era == "5G-A" for s in self.lineage)
```

- [ ] **Step 7: 写 `ngr/__init__.py` 与 `ngr/__main__.py`**

```python
# ngr/__init__.py
__version__ = "0.1.0"
```

```python
# ngr/__main__.py
from ngr.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
```

注意：`ngr/cli.py` 到 Task 18 才写。在此之前 `python -m ngr` 会报 ImportError，这是预期的 —— 先建立可测的内核，命令面最后收口。

- [ ] **Step 8: 跑测试确认通过**

Run: `.venv/Scripts/python.exe -m pytest tests/test_models.py -v`
Expected: 5 passed

- [ ] **Step 9: 补 `.gitignore` 并 commit**

```bash
printf 'data/raw/\ndata/parsed/\nlogs/\n.venv/\n__pycache__/\n*.pyc\n.pytest_cache/\n' > .gitignore
git add .gitignore pyproject.toml ngr/ tests/test_models.py
git commit -m "feat: 项目骨架、路径单例与数据模型"
```

---

### Task 3: 配置加载与校验

配置写错必须在启动时炸，而不是跑到一半才发现血统区间是空的。

**Files:**
- Create: `ngr/config.py`, `config/features.yaml`
- Test: `tests/test_config.py`

**Interfaces:**
- Consumes: `ngr.models.{LineageSegment, Feature}`
- Produces:
  - `load_sources(path=None) -> SourcesConfig`，含 `.wgs: dict[str, WgConfig]`、`.http: HttpConfig`、`.extract: ExtractConfig`
  - `load_features(path=None) -> list[Feature]`
  - `ConfigError(Exception)`

- [ ] **Step 1: 写失败的测试**

```python
# tests/test_config.py
import pytest, textwrap
from ngr.config import load_sources, load_features, ConfigError

def write(tmp_path, name, body):
    p = tmp_path / name
    p.write_text(textwrap.dedent(body), encoding="utf-8")
    return p

SOURCES_OK = """
    sources:
      RAN1:
        path: tsg_ran/WG1_RL1
        dir_re: 'TSGR1_(\\d+)([a-z]*)'
        hard_floor: 112
        agenda_csv_since: 124
        artifacts: [agenda_csv, minutes_docx]
    http:
      user_agent: "UA"
      concurrency: 2
      delay_seconds: 0.5
      retry_backoff: [2, 8, 30]
      timeout: { connect: 10, read: 300 }
    extract:
      backend: cli
      max_calls_per_run: 60
      batch_size: 40
      model_bulk: sonnet
      model_digest: opus
"""

def test_load_sources(tmp_path):
    cfg = load_sources(write(tmp_path, "s.yaml", SOURCES_OK))
    assert cfg.wgs["RAN1"].hard_floor == 112
    assert cfg.http.concurrency == 2
    assert cfg.extract.batch_size == 40

def test_sources_rejects_unknown_backend(tmp_path):
    bad = SOURCES_OK.replace("backend: cli", "backend: api")
    with pytest.raises(ConfigError, match="backend"):
        load_sources(write(tmp_path, "s.yaml", bad))

FEATURES_OK = """
    features:
      - slug: isac
        name_zh: ISAC 通感一体
        lineage:
          - era: 5G-A
            release: Rel-19
            anchor: { title_re: "(?i)ISAC" }
            meetings: { RAN1: [116, 126] }
            depth: origin
          - era: 6G
            release: Rel-20
            anchor: { agenda: ["RAN1:10.8", "RAN1:10.8.*"] }
            meetings: { RAN1: [124, null] }
            depth: full
    default_depth: origin
"""

def test_load_features(tmp_path):
    feats = load_features(write(tmp_path, "f.yaml", FEATURES_OK))
    assert len(feats) == 1
    f = feats[0]
    assert f.slug == "isac" and f.has_legacy
    assert f.lineage[1].meetings["RAN1"] == (124, None)
    assert f.lineage[0].depth == "origin"

def test_features_rejects_bad_depth(tmp_path):
    bad = FEATURES_OK.replace("depth: origin", "depth: deep")
    with pytest.raises(ConfigError, match="depth"):
        load_features(write(tmp_path, "f.yaml", bad))

def test_features_rejects_segment_with_no_anchor(tmp_path):
    bad = FEATURES_OK.replace('anchor: { title_re: "(?i)ISAC" }', "anchor: {}")
    with pytest.raises(ConfigError, match="anchor"):
        load_features(write(tmp_path, "f.yaml", bad))

def test_features_rejects_invalid_regex(tmp_path):
    bad = FEATURES_OK.replace('"(?i)ISAC"', '"(?i)ISAC("')
    with pytest.raises(ConfigError, match="正则"):
        load_features(write(tmp_path, "f.yaml", bad))

def test_features_rejects_duplicate_slug(tmp_path):
    bad = FEATURES_OK + FEATURES_OK.split("features:")[1]
    with pytest.raises(ConfigError, match="slug"):
        load_features(write(tmp_path, "f.yaml", bad))
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/Scripts/python.exe -m pytest tests/test_config.py -v`
Expected: FAIL，`No module named 'ngr.config'`

- [ ] **Step 3: 写 `ngr/config.py`**

```python
from __future__ import annotations
import re
from dataclasses import dataclass
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
    agenda_csv_since: int | None
    artifacts: list[str]

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
        wgs[name] = WgConfig(
            path=_require(raw, "path", where),
            dir_re=raw["dir_re"],
            hard_floor=int(_require(raw, "hard_floor", where)),
            agenda_csv_since=raw.get("agenda_csv_since"),
            artifacts=list(_require(raw, "artifacts", where)),
        )
    if not wgs:
        raise ConfigError("sources.yaml 未定义任何工作组")

    h = _require(data, "http", "sources.yaml")
    http = HttpConfig(
        user_agent=_require(h, "user_agent", "http"),
        concurrency=int(h.get("concurrency", 2)),
        delay_seconds=float(h.get("delay_seconds", 0.5)),
        retry_backoff=list(h.get("retry_backoff", [2, 8, 30])),
        connect_timeout=float(h.get("timeout", {}).get("connect", 10)),
        read_timeout=float(h.get("timeout", {}).get("read", 300)),
    )
    if "Mozilla" not in http.user_agent:
        raise ConfigError("http.user_agent 必须伪装浏览器，否则 3GPP 返回 403")

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
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/Scripts/python.exe -m pytest tests/test_config.py -v`
Expected: 7 passed

- [ ] **Step 5: 写首版 `config/features.yaml`**

用 spec §3.3 的示例作为起点，但 **5G-A 段的 `title_re` 必须改用 Task 1 Step 4 侦察到的真实 heading 文本**，不要照抄 spec 里的推测值。首版先只写 `waveform`、`channel_coding`、`isac`、`ai_air_interface` 四个特性 —— 其余等 Task 13 的 `lineage-report` 跑出来看到未归类清单后再补。

- [ ] **Step 6: 验证真实配置能加载**

Run: `.venv/Scripts/python.exe -c "from ngr.config import load_sources, load_features; s=load_sources(); f=load_features(); print(len(s.wgs), '个工作组,', len(f), '个特性')"`
Expected: 打印工作组数与特性数，无异常

- [ ] **Step 7: Commit**

```bash
git add ngr/config.py config/features.yaml tests/test_config.py
git commit -m "feat: 配置加载与校验"
```

---

## Phase 1：fetch 层

### Task 4: HTTP 客户端

本任务的核心不是"会发请求"，而是**403 的语义处理**。3GPP 对限流和文件缺失都返回 403，客户端必须把 403 一律当限流退避，绝不向上层报告"不存在"。

**Files:**
- Create: `ngr/fetch/__init__.py`, `ngr/fetch/client.py`
- Test: `tests/test_fetch_client.py`

**Interfaces:**
- Consumes: `ngr.config.HttpConfig`
- Produces:
  - `Http(cfg: HttpConfig)` 客户端类
  - `.get(url) -> bytes`（失败抛 `FetchError`）
  - `.head(url) -> dict`（返回 `{"etag": str|None, "length": int|None}`）
  - `FetchError(Exception)`、`RateLimited(FetchError)`

- [ ] **Step 1: 写失败的测试**

```python
# tests/test_fetch_client.py
import pytest, responses
from ngr.config import HttpConfig
from ngr.fetch.client import Http, FetchError, RateLimited

CFG = HttpConfig(user_agent="Mozilla/5.0 test", concurrency=2, delay_seconds=0,
                 retry_backoff=[0, 0, 0], connect_timeout=1, read_timeout=5)
URL = "https://www.3gpp.org/ftp/x/"

@responses.activate
def test_get_sends_browser_ua():
    responses.add(responses.GET, URL, body=b"hi", status=200)
    assert Http(CFG).get(URL) == b"hi"
    assert "Mozilla" in responses.calls[0].request.headers["User-Agent"]

@responses.activate
def test_403_is_retried_then_succeeds():
    responses.add(responses.GET, URL, status=403)
    responses.add(responses.GET, URL, status=403)
    responses.add(responses.GET, URL, body=b"ok", status=200)
    assert Http(CFG).get(URL) == b"ok"
    assert len(responses.calls) == 3

@responses.activate
def test_403_exhausted_raises_ratelimited_not_notfound():
    """403 耗尽重试后必须是 RateLimited —— 绝不能让上层以为文件不存在。"""
    for _ in range(4):
        responses.add(responses.GET, URL, status=403)
    with pytest.raises(RateLimited):
        Http(CFG).get(URL)

@responses.activate
def test_404_raises_fetcherror_immediately():
    responses.add(responses.GET, URL, status=404)
    with pytest.raises(FetchError):
        Http(CFG).get(URL)
    assert len(responses.calls) == 1        # 404 不重试

@responses.activate
def test_429_is_treated_as_rate_limit():
    for _ in range(4):
        responses.add(responses.GET, URL, status=429)
    with pytest.raises(RateLimited):
        Http(CFG).get(URL)

@responses.activate
def test_head_returns_etag_and_length():
    responses.add(responses.HEAD, URL, status=200,
                  headers={"ETag": '"abc"', "Content-Length": "123"})
    assert Http(CFG).head(URL) == {"etag": '"abc"', "length": 123}

@responses.activate
def test_head_tolerates_missing_headers():
    responses.add(responses.HEAD, URL, status=200)
    assert Http(CFG).head(URL) == {"etag": None, "length": None}

@responses.activate
def test_delay_is_applied(monkeypatch):
    slept = []
    monkeypatch.setattr("ngr.fetch.client.time.sleep", lambda s: slept.append(s))
    cfg = HttpConfig(**{**CFG.__dict__, "delay_seconds": 0.5})
    responses.add(responses.GET, URL, body=b"x", status=200)
    Http(cfg).get(URL)
    assert 0.5 in slept
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/Scripts/python.exe -m pytest tests/test_fetch_client.py -v`
Expected: FAIL，`No module named 'ngr.fetch'`

- [ ] **Step 3: 写 `ngr/fetch/client.py`**

```python
from __future__ import annotations
import logging, time
import requests
from ngr.config import HttpConfig

log = logging.getLogger(__name__)

RATE_LIMIT_CODES = {403, 429, 503}
"""3GPP 的 WAF 对限流返回 403，文件缺失同样返回 403 —— 因此 403 一律按限流处理。
把 403 当成 404 会让 fetch 静默跳过整次会议，在血统段里留下无声的空洞。"""

class FetchError(Exception):
    pass

class RateLimited(FetchError):
    pass

class Http:
    def __init__(self, cfg: HttpConfig):
        self.cfg = cfg
        self.session = requests.Session()
        self.session.headers["User-Agent"] = cfg.user_agent
        self.session.headers["Accept-Language"] = "en-US,en;q=0.9"

    @property
    def _timeout(self) -> tuple[float, float]:
        return (self.cfg.connect_timeout, self.cfg.read_timeout)

    def get(self, url: str) -> bytes:
        last = None
        for backoff in [*self.cfg.retry_backoff, None]:
            try:
                r = self.session.get(url, timeout=self._timeout)
            except requests.RequestException as exc:
                last = exc
                if backoff is None:
                    raise FetchError(f"{url} 网络错误: {exc}") from exc
                time.sleep(backoff)
                continue

            if r.status_code == 200:
                time.sleep(self.cfg.delay_seconds)
                return r.content
            if r.status_code not in RATE_LIMIT_CODES:
                raise FetchError(f"{url} 返回 HTTP {r.status_code}")

            last = r.status_code
            if backoff is None:
                break
            log.warning("%s 返回 %s（按限流处理），退避 %ss", url, r.status_code, backoff)
            time.sleep(backoff)

        raise RateLimited(
            f"{url} 重试耗尽，最后状态 {last}。"
            "注意：这不代表文件不存在 —— 3GPP 对限流和缺失都返回 403。")

    def head(self, url: str) -> dict:
        try:
            r = self.session.head(url, timeout=self._timeout, allow_redirects=True)
        except requests.RequestException as exc:
            raise FetchError(f"{url} HEAD 网络错误: {exc}") from exc
        if r.status_code in RATE_LIMIT_CODES:
            raise RateLimited(f"{url} HEAD 返回 {r.status_code}")
        if r.status_code != 200:
            raise FetchError(f"{url} HEAD 返回 HTTP {r.status_code}")
        length = r.headers.get("Content-Length")
        time.sleep(self.cfg.delay_seconds)
        return {"etag": r.headers.get("ETag"),
                "length": int(length) if length and length.isdigit() else None}
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/Scripts/python.exe -m pytest tests/test_fetch_client.py -v`
Expected: 8 passed

- [ ] **Step 5: Commit**

```bash
git add ngr/fetch/ tests/test_fetch_client.py
git commit -m "feat(fetch): HTTP 客户端，403 一律按限流处理"
```

---

### Task 5: 目录列表解析与会议发现

**Files:**
- Create: `ngr/fetch/listing.py`, `ngr/fetch/discover.py`
- Test: `tests/test_fetch_listing.py`, `tests/test_fetch_discover.py`

**Interfaces:**
- Consumes: `ngr.fetch.client.Http`、`ngr.config.{SourcesConfig, WgConfig}`、`ngr.models.{Meeting, Feature}`
- Produces:
  - `parse_listing(html: bytes, dir_url: str) -> list[str]`（该目录下的直接条目名）
  - `discover_meetings(http, wg, wgcfg) -> list[Meeting]`
  - `fetch_window(features, wg, wgcfg) -> tuple[int, int | None]`（血统并集 ∩ hard_floor）

- [ ] **Step 1: 写目录列表解析的失败测试**

```python
# tests/test_fetch_listing.py
from ngr.fetch.listing import parse_listing

DIR = "https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/"
HTML = b"""<html><body><table>
<tr><td><a href="https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/">..</a></td></tr>
<tr><td><a href="https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Agenda">Agenda</a></td></tr>
<tr><td><a href="https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs">Docs</a></td></tr>
<tr><td><a href="https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Report">Report</a></td></tr>
<tr><td><a href="?sortby=name">name</a></td></tr>
</table></body></html>"""

def test_parse_listing_returns_direct_children():
    assert parse_listing(HTML, DIR) == ["Agenda", "Docs", "Report"]

def test_parse_listing_excludes_parent_and_sort_links():
    got = parse_listing(HTML, DIR)
    assert ".." not in got and not any(g.startswith("?") for g in got)

def test_parse_listing_ignores_deeper_paths():
    html = HTML.replace(b"TSGR1_126/Report", b"TSGR1_126/Report/Archive")
    assert "Archive" not in parse_listing(html, DIR)

def test_parse_listing_tolerates_trailing_slash_in_dir_url():
    assert parse_listing(HTML, DIR.rstrip("/")) == ["Agenda", "Docs", "Report"]

def test_parse_listing_on_fixture_docs():
    """真实 fixture：RAN1#126 的 Docs 目录列表全是 R1-*.zip。"""
    import pathlib
    p = pathlib.Path("tests/fixtures/RAN1_126/docs_listing.html")
    names = parse_listing(p.read_bytes(), DIR + "Docs/")
    assert names, "fixture 解析出 0 条，检查 fixture 或解析逻辑"
    assert all(n.startswith("R1-") and n.endswith(".zip") for n in names)
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/Scripts/python.exe -m pytest tests/test_fetch_listing.py -v`
Expected: FAIL，`No module named 'ngr.fetch.listing'`

- [ ] **Step 3: 写 `ngr/fetch/listing.py`**

```python
from __future__ import annotations
import re
from urllib.parse import unquote

def parse_listing(html: bytes, dir_url: str) -> list[str]:
    """从 3GPP 的 HTML 目录列表中取出该目录的直接子条目名（不含更深层路径）。"""
    base = dir_url.rstrip("/") + "/"
    pattern = re.compile(re.escape(base) + r'([^"/?#]+)(?=["/])')
    text = html.decode("utf-8", "ignore")
    seen, out = set(), []
    for name in pattern.findall(text):
        name = unquote(name)
        if name in ("..", ".") or name.startswith("?"):
            continue
        if name not in seen:
            seen.add(name)
            out.append(name)
    return sorted(out)
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/Scripts/python.exe -m pytest tests/test_fetch_listing.py -v`
Expected: 5 passed

- [ ] **Step 5: 写会议发现与抓取区间的失败测试**

```python
# tests/test_fetch_discover.py
from unittest.mock import Mock
from ngr.config import WgConfig
from ngr.models import Feature, LineageSegment
from ngr.fetch.discover import discover_meetings, fetch_window

WG = WgConfig(path="tsg_ran/WG1_RL1", dir_re=r"TSGR1_(\d+)([a-z]*)",
              hard_floor=112, agenda_csv_since=124, artifacts=["agenda_csv"])

def _feature(slug, segs):
    return Feature(slug=slug, name_zh=slug, lineage=segs)

def _seg(lo, hi, wg="RAN1"):
    return LineageSegment(era="6G", release="Rel-20", depth="full",
                          agenda=["RAN1:10"], title_re=None, meetings={wg: (lo, hi)})

def test_fetch_window_is_union_of_lineage():
    feats = [_feature("a", [_seg(116, 126)]), _feature("b", [_seg(124, None)])]
    assert fetch_window(feats, "RAN1", WG) == (116, None)

def test_fetch_window_clamped_by_hard_floor():
    feats = [_feature("a", [_seg(100, 120)])]
    assert fetch_window(feats, "RAN1", WG) == (112, 120)

def test_fetch_window_none_when_wg_not_covered():
    feats = [_feature("a", [_seg(116, 126, wg="RAN2")])]
    assert fetch_window(feats, "RAN1", WG) is None

def test_fetch_window_closed_range_when_all_bounded():
    feats = [_feature("a", [_seg(116, 120)]), _feature("b", [_seg(118, 126)])]
    assert fetch_window(feats, "RAN1", WG) == (116, 126)

def test_discover_meetings_parses_and_sorts():
    http = Mock()
    http.get.return_value = (
        b'<a href="https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120">x</a>'
        b'<a href="https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126">x</a>'
        b'<a href="https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b">x</a>'
        b'<a href="https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/Templates">x</a>')
    got = discover_meetings(http, "RAN1", WG)
    assert [(m.number, m.suffix) for m in got] == [(120, ""), (126, ""), (126, "b")]
    assert got[0].url.endswith("TSGR1_120/")

def test_discover_meetings_ignores_non_meeting_dirs():
    http = Mock()
    http.get.return_value = b'<a href="https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/Tdoc_index">x</a>'
    assert discover_meetings(http, "RAN1", WG) == []
```

- [ ] **Step 6: 跑测试确认失败**

Run: `.venv/Scripts/python.exe -m pytest tests/test_fetch_discover.py -v`
Expected: FAIL，`No module named 'ngr.fetch.discover'`

- [ ] **Step 7: 写 `ngr/fetch/discover.py`**

```python
from __future__ import annotations
import re
from ngr.config import WgConfig
from ngr.fetch.listing import parse_listing
from ngr.models import Feature, Meeting

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
    return (low, None) if unbounded else (low, max(highs))
```

- [ ] **Step 8: 跑测试确认通过**

Run: `.venv/Scripts/python.exe -m pytest tests/test_fetch_discover.py -v`
Expected: 6 passed

- [ ] **Step 9: Commit**

```bash
git add ngr/fetch/listing.py ngr/fetch/discover.py tests/test_fetch_listing.py tests/test_fetch_discover.py
git commit -m "feat(fetch): 目录列表解析、会议发现、血统抓取区间"
```

---

### Task 6: manifest 增量、frozen 跳过、会议抓取编排

**Files:**
- Create: `ngr/fetch/manifest.py`, `ngr/fetch/runner.py`
- Test: `tests/test_fetch_manifest.py`, `tests/test_fetch_runner.py`

**Interfaces:**
- Consumes: `Http`、`parse_listing`、`discover_meetings`、`fetch_window`、`P.raw_dir`
- Produces:
  - `Manifest(dir: Path)`，方法 `.load()` `.save()` `.needs_fetch(name, head) -> bool` `.record(name, url, head, data)` `.is_frozen() -> bool` `.mark_frozen()`
  - `minutes_version(filename: str) -> int | None`（`..._v010.docx` → `10`）
  - `pick_latest_minutes(names: list[str]) -> str | None`
  - `fetch_meeting(http, meeting, cfg, force=False) -> FetchResult`（`.changed: bool`、`.files: dict[str, Path]`、`.skipped_reason: str | None`）

- [ ] **Step 1: 写 manifest 的失败测试**

```python
# tests/test_fetch_manifest.py
from ngr.fetch.manifest import Manifest, minutes_version, pick_latest_minutes

def test_minutes_version_parsing():
    assert minutes_version("Draft_Minutes_report_RAN1#126_v010.docx") == 10
    assert minutes_version("Draft_Minutes_report_RAN1#126_v100.docx") == 100
    assert minutes_version("Welcome.docx") is None

def test_pick_latest_minutes_prefers_higher_version():
    names = ["Draft_Minutes_report_RAN1#126_v010.docx",
             "Draft_Minutes_report_RAN1#126_v100.docx", "Archive"]
    assert pick_latest_minutes(names) == "Draft_Minutes_report_RAN1#126_v100.docx"

def test_pick_latest_minutes_returns_none_when_absent():
    assert pick_latest_minutes(["Archive", "notes.txt"]) is None

def test_needs_fetch_true_when_unknown(tmp_path):
    assert Manifest(tmp_path).needs_fetch("a.docx", {"etag": '"x"', "length": 5})

def test_needs_fetch_false_when_etag_matches(tmp_path):
    m = Manifest(tmp_path)
    m.record("a.docx", "http://u", {"etag": '"x"', "length": 5}, b"hello")
    m.save()
    assert not Manifest(tmp_path).needs_fetch("a.docx", {"etag": '"x"', "length": 5})

def test_needs_fetch_true_when_length_changed(tmp_path):
    m = Manifest(tmp_path)
    m.record("a.docx", "http://u", {"etag": None, "length": 5}, b"hello")
    m.save()
    assert Manifest(tmp_path).needs_fetch("a.docx", {"etag": None, "length": 9})

def test_needs_fetch_true_when_head_has_no_validators(tmp_path):
    """HEAD 什么都没给时必须重抓 —— 宁可多下一次也不要漏掉更新。"""
    m = Manifest(tmp_path)
    m.record("a.docx", "http://u", {"etag": '"x"', "length": 5}, b"hello")
    m.save()
    assert Manifest(tmp_path).needs_fetch("a.docx", {"etag": None, "length": None})

def test_record_writes_file_and_sha(tmp_path):
    m = Manifest(tmp_path)
    m.record("a.docx", "http://u", {"etag": None, "length": 5}, b"hello")
    m.save()
    assert (tmp_path / "a.docx").read_bytes() == b"hello"
    entry = Manifest(tmp_path).load()["files"]["a.docx"]
    assert entry["sha256"].startswith("sha256:")

def test_frozen_roundtrip(tmp_path):
    m = Manifest(tmp_path)
    assert not m.is_frozen()
    m.mark_frozen(); m.save()
    assert Manifest(tmp_path).is_frozen()
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/Scripts/python.exe -m pytest tests/test_fetch_manifest.py -v`
Expected: FAIL，`No module named 'ngr.fetch.manifest'`

- [ ] **Step 3: 写 `ngr/fetch/manifest.py`**

```python
from __future__ import annotations
import hashlib, json, re, time
from pathlib import Path

MINUTES_RE = re.compile(r"(?i)minutes.*_v(\d{3})\.docx$")

def minutes_version(filename: str) -> int | None:
    m = MINUTES_RE.search(filename)
    return int(m.group(1)) if m else None

def pick_latest_minutes(names: list[str]) -> str | None:
    """纪要有 v010 → v100 的版本演进，永远取最高版本。"""
    cands = [(minutes_version(n), n) for n in names]
    cands = [(v, n) for v, n in cands if v is not None]
    return max(cands)[1] if cands else None

class Manifest:
    """记录每个已抓文件的 etag/长度/哈希，用于增量判定。"""

    def __init__(self, directory: Path):
        self.dir = Path(directory)
        self.path = self.dir / "_manifest.json"
        self._data: dict | None = None

    def load(self) -> dict:
        if self._data is None:
            if self.path.exists():
                self._data = json.loads(self.path.read_text(encoding="utf-8"))
            else:
                self._data = {"files": {}, "frozen": False}
            self._data.setdefault("files", {})
            self._data.setdefault("frozen", False)
        return self._data

    def save(self) -> None:
        self.dir.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.load(), ensure_ascii=False, indent=2,
                                        sort_keys=True), encoding="utf-8")

    def needs_fetch(self, name: str, head: dict) -> bool:
        entry = self.load()["files"].get(name)
        if entry is None or not (self.dir / name).exists():
            return True
        # HEAD 没给任何校验信息时无法判断，一律重抓
        if head.get("etag") is None and head.get("length") is None:
            return True
        if head.get("etag") is not None:
            return head["etag"] != entry.get("etag")
        return head.get("length") != entry.get("length")

    def record(self, name: str, url: str, head: dict, data: bytes) -> None:
        self.dir.mkdir(parents=True, exist_ok=True)
        (self.dir / name).write_bytes(data)
        self.load()["files"][name] = {
            "url": url,
            "etag": head.get("etag"),
            "length": head.get("length") if head.get("length") is not None else len(data),
            "sha256": "sha256:" + hashlib.sha256(data).hexdigest(),
            "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        }

    def is_frozen(self) -> bool:
        return bool(self.load()["frozen"])

    def mark_frozen(self) -> None:
        self.load()["frozen"] = True
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/Scripts/python.exe -m pytest tests/test_fetch_manifest.py -v`
Expected: 9 passed

- [ ] **Step 5: 写抓取编排的失败测试**

```python
# tests/test_fetch_runner.py
from unittest.mock import Mock
from ngr.config import WgConfig
from ngr.models import Meeting
from ngr.fetch.manifest import Manifest
from ngr.fetch.runner import fetch_meeting

WG = WgConfig(path="tsg_ran/WG1_RL1", dir_re=r"TSGR1_(\d+)([a-z]*)", hard_floor=112,
              agenda_csv_since=124, artifacts=["agenda_csv", "minutes_docx", "docs_listing"])
MTG = Meeting(wg="RAN1", number=126, suffix="",
              url="https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/")

def _http(listings: dict[str, bytes], files: dict[str, bytes]):
    http = Mock()
    def get(url):
        if url in listings: return listings[url]
        if url in files:    return files[url]
        raise AssertionError(f"未预期的 GET {url}")
    http.get.side_effect = get
    http.head.return_value = {"etag": '"e"', "length": 3}
    return http

def _listing(dir_url, names):
    return b"".join(f'<a href="{dir_url}{n}">{n}</a>'.encode() for n in names)

def test_fetch_meeting_downloads_agenda_and_latest_minutes(tmp_path):
    base = MTG.url
    http = _http(
        listings={
            base: _listing(base, ["Agenda", "Report", "Docs"]),
            base + "Agenda/": _listing(base + "Agenda/", ["agenda.csv"]),
            base + "Report/": _listing(base + "Report/",
                ["Draft_Minutes_report_RAN1#126_v010.docx",
                 "Draft_Minutes_report_RAN1#126_v100.docx"]),
            base + "Docs/": _listing(base + "Docs/", ["R1-1.zip"]),
        },
        files={base + "Agenda/agenda.csv": b"csv",
               base + "Report/Draft_Minutes_report_RAN1#126_v100.docx": b"doc"})
    res = fetch_meeting(http, MTG, WG, raw_dir=tmp_path)
    assert res.changed
    assert (tmp_path / "agenda.csv").read_bytes() == b"csv"
    assert (tmp_path / "minutes.docx").read_bytes() == b"doc"
    assert (tmp_path / "docs_listing.html").exists()

def test_fetch_meeting_skips_agenda_when_absent(tmp_path):
    """老会议的 Agenda/ 里只有 TDoc zip —— 靠目录列表判断，不靠 GET 状态码。"""
    base = MTG.url
    http = _http(
        listings={
            base: _listing(base, ["Agenda", "Report", "Docs"]),
            base + "Agenda/": _listing(base + "Agenda/", ["R1-2500001.zip"]),
            base + "Report/": _listing(base + "Report/",
                                       ["Draft_Minutes_report_RAN1#120_v100.docx"]),
            base + "Docs/": _listing(base + "Docs/", ["R1-1.zip"]),
        },
        files={base + "Report/Draft_Minutes_report_RAN1#120_v100.docx": b"doc"})
    res = fetch_meeting(http, MTG, WG, raw_dir=tmp_path)
    assert not (tmp_path / "agenda.csv").exists()
    assert (tmp_path / "minutes.docx").exists()
    assert "agenda_csv" in res.missing

def test_fetch_meeting_skips_frozen(tmp_path):
    m = Manifest(tmp_path); m.mark_frozen(); m.save()
    http = Mock()
    res = fetch_meeting(http, MTG, WG, raw_dir=tmp_path)
    assert not res.changed and res.skipped_reason == "frozen"
    http.get.assert_not_called()
    http.head.assert_not_called()

def test_fetch_meeting_force_ignores_frozen(tmp_path):
    base = MTG.url
    m = Manifest(tmp_path); m.mark_frozen(); m.save()
    http = _http(
        listings={base: _listing(base, ["Report"]),
                  base + "Report/": _listing(base + "Report/", ["Minutes_v010.docx"])},
        files={base + "Report/Minutes_v010.docx": b"doc"})
    res = fetch_meeting(http, MTG, WG, raw_dir=tmp_path, force=True)
    assert res.changed

def test_fetch_meeting_no_redownload_when_unchanged(tmp_path):
    base = MTG.url
    listings = {base: _listing(base, ["Report"]),
                base + "Report/": _listing(base + "Report/", ["Minutes_v010.docx"])}
    files = {base + "Report/Minutes_v010.docx": b"doc"}
    http = _http(listings, files)
    fetch_meeting(http, MTG, WG, raw_dir=tmp_path)
    http2 = _http(listings, files)
    res = fetch_meeting(http2, MTG, WG, raw_dir=tmp_path)
    assert not res.changed
    assert base + "Report/Minutes_v010.docx" not in [c.args[0] for c in http2.get.call_args_list]
```

- [ ] **Step 6: 跑测试确认失败**

Run: `.venv/Scripts/python.exe -m pytest tests/test_fetch_runner.py -v`
Expected: FAIL，`No module named 'ngr.fetch.runner'`

- [ ] **Step 7: 写 `ngr/fetch/runner.py`**

```python
from __future__ import annotations
import logging
from dataclasses import dataclass, field
from pathlib import Path
from ngr.config import WgConfig
from ngr.fetch.listing import parse_listing
from ngr.fetch.manifest import Manifest, pick_latest_minutes
from ngr.models import Meeting
from ngr.paths import P

log = logging.getLogger(__name__)

# artifact 名 → (子目录, 落地文件名, 在子目录里怎么选文件)
def _pick_exact(name):
    return lambda names: name if name in names else None

ARTIFACTS = {
    "agenda_csv":    ("Agenda/", "agenda.csv",        _pick_exact("agenda.csv")),
    "minutes_docx":  ("Report/", "minutes.docx",      pick_latest_minutes),
}
LISTING_ARTIFACTS = {
    "docs_listing":  ("Docs/", "docs_listing.html"),
    "ls_listing":    ("LS/",   "ls_listing.html"),
}

@dataclass
class FetchResult:
    changed: bool = False
    files: dict[str, Path] = field(default_factory=dict)
    missing: list[str] = field(default_factory=list)
    skipped_reason: str | None = None

def fetch_meeting(http, meeting: Meeting, cfg: WgConfig,
                  raw_dir: Path | None = None, force: bool = False) -> FetchResult:
    """抓一次会议的全部约定产物。所有文件存在性判断都走目录列表，
    绝不用 GET 的状态码判断 —— 403 分不清限流与缺失。"""
    raw_dir = raw_dir or P.raw_dir(meeting.wg, meeting.number)
    man = Manifest(raw_dir)

    if man.is_frozen() and not force:
        return FetchResult(skipped_reason="frozen")

    res = FetchResult()
    root_names = parse_listing(http.get(meeting.url), meeting.url)

    for art in cfg.artifacts:
        if art in ARTIFACTS:
            subdir, local, chooser = ARTIFACTS[art]
            if subdir.rstrip("/") not in root_names:
                res.missing.append(art)
                continue
            sub_url = meeting.url + subdir
            names = parse_listing(http.get(sub_url), sub_url)
            chosen = chooser(names)
            if chosen is None:
                res.missing.append(art)
                continue
            url = sub_url + chosen
            head = http.head(url)
            if man.needs_fetch(local, head):
                man.record(local, url, head, http.get(url))
                res.changed = True
            res.files[art] = raw_dir / local

        elif art in LISTING_ARTIFACTS:
            subdir, local = LISTING_ARTIFACTS[art]
            if subdir.rstrip("/") not in root_names:
                res.missing.append(art)
                continue
            sub_url = meeting.url + subdir
            data = http.get(sub_url)
            head = {"etag": None, "length": len(data)}
            if man.needs_fetch(local, head):
                man.record(local, sub_url, head, data)
                res.changed = True
            res.files[art] = raw_dir / local
        else:
            log.warning("未知 artifact 类型: %s", art)

    man.save()
    return res
```

> 目录列表本身没有稳定的 ETag（内容随排序参数变化），所以对它用长度做增量判据。这会带来偶发的无谓重写，但列表只有 2 MB 且不进 git，代价可以接受。

- [ ] **Step 8: 跑测试确认通过**

Run: `.venv/Scripts/python.exe -m pytest tests/test_fetch_runner.py -v`
Expected: 5 passed

- [ ] **Step 9: 跑全部测试**

Run: `.venv/Scripts/python.exe -m pytest -v`
Expected: 全绿（Task 2–6 的所有测试）

- [ ] **Step 10: Commit**

```bash
git add ngr/fetch/manifest.py ngr/fetch/runner.py tests/test_fetch_manifest.py tests/test_fetch_runner.py
git commit -m "feat(fetch): manifest 增量、frozen 跳过、会议抓取编排"
```

---

## Phase 2：parse 层

### Task 7: agenda.csv 解析

**Files:**
- Create: `ngr/parse/__init__.py`, `ngr/parse/agenda.py`
- Test: `tests/test_parse_agenda.py`

**Interfaces:**
- Consumes: `ngr.models.AgendaItem`
- Produces: `parse_agenda(data: bytes) -> list[AgendaItem]`

- [ ] **Step 1: 写失败的测试**

```python
# tests/test_parse_agenda.py
import pathlib
from ngr.parse.agenda import parse_agenda

def test_parse_agenda_basic():
    data = b'"1","Opening of the meeting"\n"10","Rel-20 Study of 6GR"\n"10.2","Waveform for 6GR air interface"\n'
    items = parse_agenda(data)
    assert [i.item for i in items] == ["1", "10", "10.2"]
    assert items[2].title == "Waveform for 6GR air interface"
    assert items[2].depth == 2

def test_parse_agenda_strips_whitespace_in_item_number():
    """实测 RAN1#126 的 agenda.csv 里有 '10.4.1 ' 这种带尾空格的条目。"""
    items = parse_agenda(b'"10.4.1 ","Operation in idle mode"\n')
    assert items[0].item == "10.4.1"
    assert items[0].depth == 3

def test_parse_agenda_keeps_quotes_inside_title():
    items = parse_agenda(b'"9.1.1","CSI compression (\xe2\x80\x9cCase 0\xe2\x80\x9d)"\n')
    assert "Case 0" in items[0].title

def test_parse_agenda_skips_blank_lines():
    assert len(parse_agenda(b'"1","A"\n\n"2","B"\n')) == 2

def test_parse_agenda_on_real_fixture():
    data = pathlib.Path("tests/fixtures/RAN1_126/agenda.csv").read_bytes()
    items = parse_agenda(data)
    by_item = {i.item: i.title for i in items}
    assert by_item["10"] == "Rel-20 Study of 6GR"
    assert by_item["10.2"] == "Waveform for 6GR air interface"
    assert by_item["9"] == "Release 20 NR"     # Rel-20 ≠ 6G，两者并列
    assert len(items) > 50
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/Scripts/python.exe -m pytest tests/test_parse_agenda.py -v`
Expected: FAIL，`No module named 'ngr.parse'`

- [ ] **Step 3: 写 `ngr/parse/agenda.py`**

```python
from __future__ import annotations
import csv, io
from ngr.models import AgendaItem

def parse_agenda(data: bytes) -> list[AgendaItem]:
    """解析 3GPP 的 Agenda/agenda.csv，格式为 "<议程号>","<标题>" 两列无表头。"""
    text = data.decode("utf-8-sig", "replace")
    out = []
    for row in csv.reader(io.StringIO(text)):
        if len(row) < 2:
            continue
        item, title = row[0].strip(), row[1].strip()
        if not item:
            continue
        out.append(AgendaItem(item=item, title=title))
    return out
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/Scripts/python.exe -m pytest tests/test_parse_agenda.py -v`
Expected: 5 passed

- [ ] **Step 5: Commit**

```bash
git add ngr/parse/ tests/test_parse_agenda.py
git commit -m "feat(parse): agenda.csv 解析"
```

---

### Task 8: docx 段落、heading 与表格抽取

不用 `python-docx`：它把表格和段落分成两棵树，拿不到二者的**原始先后顺序**，而 agreement 块的边界恰恰依赖顺序。直接读 `word/document.xml` 反而更简单可靠。

**Files:**
- Create: `ngr/parse/docx.py`
- Test: `tests/test_parse_docx.py`

**Interfaces:**
- Consumes: `ngr.models.Heading`
- Produces:
  - `Block` 数据类：`.kind: str`（`"para"` | `"table"`）、`.text: str`、`.style: str | None`、`.index: int`
  - `parse_docx(path_or_bytes) -> Document`
  - `Document` 数据类：`.blocks: list[Block]`、`.headings: list[Heading]`、`.paragraphs: list[str]`

- [ ] **Step 1: 写失败的测试**

```python
# tests/test_parse_docx.py
import pathlib, zipfile, io
from ngr.parse.docx import parse_docx

def make_docx(body_xml: str) -> bytes:
    """构造最小 docx：只需要 word/document.xml。"""
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        z.writestr("word/document.xml",
            '<?xml version="1.0"?><w:document '
            'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
            f'<w:body>{body_xml}</w:body></w:document>')
    return buf.getvalue()

def para(text, style=None):
    s = f'<w:pPr><w:pStyle w:val="{style}"/></w:pPr>' if style else ""
    return f'<w:p>{s}<w:r><w:t>{text}</w:t></w:r></w:p>'

def test_extracts_paragraph_text():
    doc = parse_docx(make_docx(para("Hello world")))
    assert doc.paragraphs == ["Hello world"]

def test_joins_multiple_runs_in_one_paragraph():
    xml = '<w:p><w:r><w:t>Agree</w:t></w:r><w:r><w:t>ment</w:t></w:r></w:p>'
    assert parse_docx(make_docx(xml)).paragraphs == ["Agreement"]

def test_headings_carry_level_and_index():
    doc = parse_docx(make_docx(para("Top", "Heading1") + para("body") + para("Sub", "Heading2")))
    assert [(h.level, h.text) for h in doc.headings] == [(1, "Top"), (2, "Sub")]
    assert doc.headings[1].para_index == 2

def test_non_heading_styles_are_not_headings():
    doc = parse_docx(make_docx(para("x", "BodyText")))
    assert doc.headings == []

def test_table_becomes_markdown_block_in_document_order():
    tbl = ('<w:tbl>'
           '<w:tr><w:tc><w:p><w:r><w:t>SCS</w:t></w:r></w:p></w:tc>'
           '<w:tc><w:p><w:r><w:t>BW</w:t></w:r></w:p></w:tc></w:tr>'
           '<w:tr><w:tc><w:p><w:r><w:t>30</w:t></w:r></w:p></w:tc>'
           '<w:tc><w:p><w:r><w:t>100</w:t></w:r></w:p></w:tc></w:tr>'
           '</w:tbl>')
    doc = parse_docx(make_docx(para("Agreement:") + tbl + para("after")))
    kinds = [b.kind for b in doc.blocks]
    assert kinds == ["para", "table", "para"]
    assert doc.blocks[1].text == "| SCS | BW |\n| --- | --- |\n| 30 | 100 |"

def test_table_cell_with_multiple_paragraphs_is_joined():
    tbl = ('<w:tbl><w:tr><w:tc>'
           '<w:p><w:r><w:t>a</w:t></w:r></w:p><w:p><w:r><w:t>b</w:t></w:r></w:p>'
           '</w:tc></w:tr></w:tbl>')
    assert "a b" in parse_docx(make_docx(tbl)).blocks[0].text

def test_pipe_in_cell_is_escaped():
    tbl = '<w:tbl><w:tr><w:tc><w:p><w:r><w:t>a|b</w:t></w:r></w:p></w:tc></w:tr></w:tbl>'
    assert r"a\|b" in parse_docx(make_docx(tbl)).blocks[0].text

def test_empty_paragraphs_are_dropped():
    assert parse_docx(make_docx('<w:p></w:p>' + para("x"))).paragraphs == ["x"]

def test_real_fixture_structure():
    """实测 RAN1#126 v010 的确切数字 —— 3GPP 换纪要模板时这里第一个炸。"""
    doc = parse_docx(pathlib.Path("tests/fixtures/RAN1_126/minutes.docx"))
    assert len(doc.paragraphs) == 7803
    assert len(doc.headings) == 83
    assert any(h.text == "Rel-20 Study of 6GR" and h.level == 1 for h in doc.headings)
    assert any(h.text == "Waveform for 6GR air interface" for h in doc.headings)

def test_real_fixture_marker_counts():
    doc = parse_docx(pathlib.Path("tests/fixtures/RAN1_126/minutes.docx"))
    assert sum(1 for p in doc.paragraphs if p.startswith("Agreement")) == 320
    assert sum(1 for p in doc.paragraphs if p.startswith("Conclusion")) == 29
    assert sum(1 for p in doc.paragraphs if p.lower().startswith("working assumption")) == 13
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/Scripts/python.exe -m pytest tests/test_parse_docx.py -v`
Expected: FAIL，`No module named 'ngr.parse.docx'`

- [ ] **Step 3: 写 `ngr/parse/docx.py`**

```python
from __future__ import annotations
import re, zipfile
from dataclasses import dataclass, field
from pathlib import Path
from ngr.models import Heading

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
HEADING_RE = re.compile(r"(?i)^heading\s*(\d+)$")

@dataclass
class Block:
    kind: str            # "para" | "table"
    text: str
    style: str | None
    index: int           # 在 blocks 中的下标

@dataclass
class Document:
    blocks: list[Block] = field(default_factory=list)
    headings: list[Heading] = field(default_factory=list)

    @property
    def paragraphs(self) -> list[str]:
        return [b.text for b in self.blocks if b.kind == "para"]

def _text_of(el) -> str:
    return "".join(t.text or "" for t in el.iter(W + "t"))

def _cell_text(tc) -> str:
    parts = [_text_of(p).strip() for p in tc.findall(W + "p")]
    return " ".join(x for x in parts if x).replace("|", r"\|")

def _table_to_markdown(tbl) -> str:
    rows = []
    for tr in tbl.findall(W + "tr"):
        rows.append([_cell_text(tc) for tc in tr.findall(W + "tc")])
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    lines = ["| " + " | ".join(rows[0]) + " |",
             "| " + " | ".join(["---"] * width) + " |"]
    lines += ["| " + " | ".join(r) + " |" for r in rows[1:]]
    return "\n".join(lines)

def parse_docx(source: Path | bytes) -> Document:
    """按文档顺序抽出段落与表格。用 ElementTree 而非 python-docx，
    因为后者拿不到段落与表格的原始交错顺序，而 agreement 块的边界依赖它。"""
    import xml.etree.ElementTree as ET

    data = source.read_bytes() if isinstance(source, Path) else source
    with zipfile.ZipFile(__import__("io").BytesIO(data)) as z:
        xml = z.read("word/document.xml")
    body = ET.fromstring(xml).find(W + "body")

    doc = Document()
    para_index = 0
    for el in list(body):
        tag = el.tag
        if tag == W + "p":
            text = _text_of(el).strip()
            if not text:
                continue
            pstyle = el.find(f"{W}pPr/{W}pStyle")
            style = pstyle.get(W + "val") if pstyle is not None else None
            doc.blocks.append(Block("para", text, style, len(doc.blocks)))
            if style:
                m = HEADING_RE.match(style)
                if m:
                    doc.headings.append(
                        Heading(level=int(m.group(1)), text=text, para_index=para_index))
            para_index += 1
        elif tag == W + "tbl":
            md = _table_to_markdown(el)
            if md:
                doc.blocks.append(Block("table", md, None, len(doc.blocks)))
    return doc
```

> `Heading.para_index` 是**段落序号**（只数 `para` 块），而 `Block.index` 是**块序号**（段落与表格统一编号）。两者不同，不要混用：对齐用前者，块边界用后者。

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/Scripts/python.exe -m pytest tests/test_parse_docx.py -v`
Expected: 10 passed

如果 `test_real_fixture_structure` 的数字对不上，先检查 fixture 是否是 `Draft_Minutes_report_RAN1#126_v010.docx` 本身（而非其他版本），再调解析逻辑 —— 不要直接改断言数字。

- [ ] **Step 5: Commit**

```bash
git add ngr/parse/docx.py tests/test_parse_docx.py
git commit -m "feat(parse): docx 段落/heading/表格抽取"
```

---

### Task 9: agreement 块提取

Agreement 是**块**不是行：标记段之后可能跟若干段落、项目符号和表格。吃到下一个标记或下一个 heading 为止。

**Files:**
- Create: `ngr/parse/events.py`
- Test: `tests/test_parse_events.py`

**Interfaces:**
- Consumes: `ngr.parse.docx.{Document, Block}`、`ngr.models.RawEvent`
- Produces: `extract_events(doc: Document) -> list[RawEvent]`（`RawEvent.heading_path` 为该事件所在的 heading 文本栈）

- [ ] **Step 1: 写失败的测试**

```python
# tests/test_parse_events.py
import pathlib
from ngr.parse.docx import parse_docx, Document, Block
from ngr.parse.events import extract_events
from ngr.models import Heading

def doc_of(*blocks_and_headings):
    """blocks_and_headings: (kind, text, style) 三元组序列。"""
    d = Document()
    para_i = 0
    for kind, text, style in blocks_and_headings:
        d.blocks.append(Block(kind, text, style, len(d.blocks)))
        if kind == "para":
            if style and style.lower().startswith("heading"):
                d.headings.append(Heading(level=int(style[-1]), text=text, para_index=para_i))
            para_i += 1
    return d

def test_single_agreement_captures_following_paragraphs():
    d = doc_of(("para", "Agreement:", None),
               ("para", "Adopt option 1.", None),
               ("para", "Adopt option 2.", None))
    evs = extract_events(d)
    assert len(evs) == 1
    assert evs[0].kind == "agreement"
    assert "option 1" in evs[0].text_en and "option 2" in evs[0].text_en

def test_block_stops_at_next_marker():
    d = doc_of(("para", "Agreement:", None), ("para", "A", None),
               ("para", "Conclusion:", None), ("para", "B", None))
    evs = extract_events(d)
    assert [e.kind for e in evs] == ["agreement", "conclusion"]
    assert "B" not in evs[0].text_en

def test_block_stops_at_next_heading():
    d = doc_of(("para", "Agreement:", None), ("para", "A", None),
               ("para", "Next topic", "Heading2"), ("para", "B", None))
    evs = extract_events(d)
    assert len(evs) == 1 and "B" not in evs[0].text_en

def test_table_inside_block_is_kept():
    d = doc_of(("para", "Agreement:", None),
               ("table", "| a | b |\n| --- | --- |\n| 1 | 2 |", None))
    assert "| a | b |" in extract_events(d)[0].text_en

def test_all_marker_kinds_recognised():
    d = doc_of(("para", "Agreement: x", None), ("para", "Conclusion: y", None),
               ("para", "Working assumption: z", None), ("para", "Observation: w", None),
               ("para", "Proposal: v", None))
    assert [e.kind for e in extract_events(d)] == [
        "agreement", "conclusion", "working_assumption", "observation", "proposal"]

def test_marker_inline_text_is_kept():
    """'Agreement: 直接跟内容' 这种写法，内容不能丢。"""
    d = doc_of(("para", "Agreement: adopt X", None))
    assert "adopt X" in extract_events(d)[0].text_en

def test_heading_path_is_recorded():
    d = doc_of(("para", "Rel-20 Study of 6GR", "Heading1"),
               ("para", "Waveform for 6GR air interface", "Heading2"),
               ("para", "Agreement:", None), ("para", "X", None))
    ev = extract_events(d)[0]
    assert ev.heading_path == ["Rel-20 Study of 6GR", "Waveform for 6GR air interface"]

def test_heading_path_pops_on_shallower_heading():
    d = doc_of(("para", "A", "Heading1"), ("para", "B", "Heading2"),
               ("para", "C", "Heading1"), ("para", "Agreement:", None), ("para", "X", None))
    assert extract_events(d)[0].heading_path == ["C"]

def test_word_agreements_not_matched_mid_sentence():
    """'The agreement was reached' 不是一条 agreement。"""
    d = doc_of(("para", "The agreement was reached last meeting.", None))
    assert extract_events(d) == []

def test_real_fixture_counts():
    doc = parse_docx(pathlib.Path("tests/fixtures/RAN1_126/minutes.docx"))
    evs = extract_events(doc)
    kinds = [e.kind for e in evs]
    assert kinds.count("agreement") == 320
    assert kinds.count("conclusion") == 29
    assert kinds.count("working_assumption") == 13
    assert all(e.text_en.strip() for e in evs), "不允许出现空正文的事件"

def test_real_fixture_6g_events_have_heading_path():
    doc = parse_docx(pathlib.Path("tests/fixtures/RAN1_126/minutes.docx"))
    evs = extract_events(doc)
    sixg = [e for e in evs if "Rel-20 Study of 6GR" in e.heading_path]
    assert sixg, "6GR 子树下应有事件"
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/Scripts/python.exe -m pytest tests/test_parse_events.py -v`
Expected: FAIL，`No module named 'ngr.parse.events'`

- [ ] **Step 3: 写 `ngr/parse/events.py`**

```python
from __future__ import annotations
import re
from ngr.models import RawEvent
from ngr.parse.docx import Document

MARKERS = {
    "agreement": r"agreements?",
    "conclusion": r"conclusions?",
    "working_assumption": r"working\s+assumptions?",
    "observation": r"observations?",
    "proposal": r"proposals?",
}
# 标记必须在段首，后跟冒号/句点/行末 —— 避免 "The agreement was reached" 被误判
MARKER_RE = re.compile(
    r"^\s*(?:" + "|".join(f"(?P<{k}>{v})" for k, v in MARKERS.items()) + r")"
    r"\s*(?:\d+[\.\):]?)?\s*(?::|\.\s|$)", re.IGNORECASE)

HEADING_STYLE_RE = re.compile(r"(?i)^heading\s*(\d+)$")

def _marker_kind(text: str) -> str | None:
    m = MARKER_RE.match(text)
    if not m:
        return None
    return next(k for k, v in m.groupdict().items() if v)

def extract_events(doc: Document) -> list[RawEvent]:
    """扫描块序列，把每个标记段及其后续内容收成一个事件。"""
    events: list[RawEvent] = []
    stack: list[tuple[int, str]] = []      # (level, text)
    current: RawEvent | None = None

    for block in doc.blocks:
        is_heading = False
        if block.kind == "para" and block.style:
            hm = HEADING_STYLE_RE.match(block.style)
            if hm:
                is_heading = True
                level = int(hm.group(1))
                while stack and stack[-1][0] >= level:
                    stack.pop()
                stack.append((level, block.text))

        if is_heading:
            current = None                  # heading 终结当前块
            continue

        kind = _marker_kind(block.text) if block.kind == "para" else None
        if kind:
            body = MARKER_RE.sub("", block.text, count=1).strip()
            current = RawEvent(kind=kind, text_en=body, para_index=block.index,
                               heading_path=[t for _, t in stack])
            events.append(current)
        elif current is not None:
            current.text_en = (current.text_en + "\n" + block.text).strip()

    return [e for e in events if e.text_en.strip()]
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/Scripts/python.exe -m pytest tests/test_parse_events.py -v`
Expected: 11 passed

若真实 fixture 的计数对不上 320/29/13，最可能的原因是 `MARKER_RE` 太严或太松。用下面的命令看看哪些段落被漏掉/多收：

```bash
.venv/Scripts/python.exe -c "
from ngr.parse.docx import parse_docx; from ngr.parse.events import _marker_kind
import pathlib
doc = parse_docx(pathlib.Path('tests/fixtures/RAN1_126/minutes.docx'))
miss = [p for p in doc.paragraphs if p.startswith('Agreement') and not _marker_kind(p)]
print('漏判:', miss[:5])"
```

- [ ] **Step 5: Commit**

```bash
git add ngr/parse/events.py tests/test_parse_events.py
git commit -m "feat(parse): agreement 块提取"
```

---

### Task 10: heading ↔ 议程号对齐

纪要标题是 Word 自动编号，正文里没有议程号。靠 `agenda.csv` 的标题文本对齐回去。**三重校验都通过才落库** —— 宁可少归类，不可错归类。

**Files:**
- Create: `ngr/parse/align.py`
- Test: `tests/test_parse_align.py`

**Interfaces:**
- Consumes: `ngr.models.{AgendaItem, Heading}`
- Produces:
  - `Alignment` 数据类：`.by_heading: dict[int, AgendaItem]`（键为 `Heading.para_index`）、`.unaligned: list[Heading]`、`.unmatched_ratio: float`
  - `align(agenda: list[AgendaItem], headings: list[Heading]) -> Alignment`
  - `normalize(text: str) -> str`

- [ ] **Step 1: 写失败的测试**

```python
# tests/test_parse_align.py
from ngr.models import AgendaItem, Heading
from ngr.parse.align import align, normalize

def A(item, title): return AgendaItem(item=item, title=title)
def H(level, text, i=0): return Heading(level=level, text=text, para_index=i)

def test_normalize_strips_case_punct_and_space():
    assert normalize("  Waveform for 6GR  air-interface! ") == normalize("waveform for 6gr airinterface")

def test_exact_match():
    ag = [A("10.2", "Waveform for 6GR air interface")]
    al = align(ag, [H(2, "Waveform for 6GR air interface", 5)])
    assert al.by_heading[5].item == "10.2"
    assert al.unmatched_ratio == 0.0

def test_fuzzy_match_above_threshold():
    ag = [A("10.3", "Channel coding and modulation for 6GR interface")]
    al = align(ag, [H(2, "Channel coding and modulation for 6GR  interface", 7)])
    assert al.by_heading[7].item == "10.3"

def test_fuzzy_below_threshold_is_rejected():
    ag = [A("10.2", "Waveform for 6GR air interface")]
    al = align(ag, [H(2, "Totally different topic", 3)])
    assert 3 not in al.by_heading
    assert al.unaligned[0].text == "Totally different topic"

def test_depth_mismatch_is_rejected():
    """标题对得上但层级对不上 —— 拒绝，这是模板变动的信号。"""
    ag = [A("10.2", "Waveform")]                  # depth 2
    al = align(ag, [H(4, "Waveform", 1)])         # Heading4
    assert 1 not in al.by_heading

def test_depth_match_allows_one_level_offset():
    """纪要常把 Heading1 用在 depth-1 议程项上，允许 ±1 的偏移。"""
    ag = [A("10.2", "Waveform")]
    al = align(ag, [H(3, "Waveform", 1)])
    assert al.by_heading[1].item == "10.2"

def test_each_agenda_item_used_at_most_once():
    ag = [A("10.2", "Waveform")]
    al = align(ag, [H(2, "Waveform", 1), H(2, "Waveform", 9)])
    assert len(al.by_heading) == 1

def test_unmatched_ratio_computed():
    ag = [A("1", "Opening")]
    al = align(ag, [H(1, "Opening", 0), H(1, "Mystery", 1)])
    assert al.unmatched_ratio == 0.5

def test_empty_agenda_marks_all_unaligned():
    al = align([], [H(1, "X", 0)])
    assert al.unmatched_ratio == 1.0 and al.by_heading == {}

def test_real_fixture_alignment():
    import pathlib
    from ngr.parse.agenda import parse_agenda
    from ngr.parse.docx import parse_docx
    ag = parse_agenda(pathlib.Path("tests/fixtures/RAN1_126/agenda.csv").read_bytes())
    doc = parse_docx(pathlib.Path("tests/fixtures/RAN1_126/minutes.docx"))
    al = align(ag, doc.headings)
    assert al.unmatched_ratio < 0.20, f"未对齐率过高: {al.unmatched_ratio:.0%}"
    items = {v.item for v in al.by_heading.values()}
    assert "10" in items and "10.2" in items
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/Scripts/python.exe -m pytest tests/test_parse_align.py -v`
Expected: FAIL，`No module named 'ngr.parse.align'`

- [ ] **Step 3: 写 `ngr/parse/align.py`**

```python
from __future__ import annotations
import difflib, re, unicodedata
from dataclasses import dataclass, field
from ngr.models import AgendaItem, Heading

FUZZY_THRESHOLD = 0.90
DEPTH_TOLERANCE = 1          # heading 层级与议程深度允许 ±1 偏移

_PUNCT = re.compile(r"[^\w\s]", re.UNICODE)
_SPACE = re.compile(r"\s+")

def normalize(text: str) -> str:
    t = unicodedata.normalize("NFKC", text).lower()
    t = _PUNCT.sub("", t)
    return _SPACE.sub(" ", t).strip()

@dataclass
class Alignment:
    by_heading: dict[int, AgendaItem] = field(default_factory=dict)
    unaligned: list[Heading] = field(default_factory=list)

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
    norm_keys = list(exact.keys())

    for h in headings:
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
            result.unaligned.append(h)
        else:
            result.by_heading[h.para_index] = chosen
            used.add(chosen.item)

    return result
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/Scripts/python.exe -m pytest tests/test_parse_align.py -v`
Expected: 10 passed

若真实 fixture 的未对齐率超过 20%，先打印未对齐清单看是什么：

```bash
.venv/Scripts/python.exe -c "
import pathlib
from ngr.parse.agenda import parse_agenda
from ngr.parse.docx import parse_docx
from ngr.parse.align import align
ag = parse_agenda(pathlib.Path('tests/fixtures/RAN1_126/agenda.csv').read_bytes())
doc = parse_docx(pathlib.Path('tests/fixtures/RAN1_126/minutes.docx'))
al = align(ag, doc.headings)
print(f'{al.unmatched_ratio:.0%} 未对齐'); [print(' ', h.level, h.text) for h in al.unaligned[:15]]"
```

- [ ] **Step 5: Commit**

```bash
git add ngr/parse/align.py tests/test_parse_align.py
git commit -m "feat(parse): heading 与议程号三重校验对齐"
```

---

### Task 11: parse 编排与沉默失败防线

这一层最重要的不是解析，是**拒绝在解析退化时装作成功**。3GPP 换纪要模板是迟早的事，届时解析器会安静返回 0 条，而定时任务照常"成功"，几个月后才被发现。

**Files:**
- Create: `ngr/parse/runner.py`
- Test: `tests/test_parse_runner.py`

**Interfaces:**
- Consumes: `parse_agenda`、`parse_docx`、`extract_events`、`align`、`P.parsed_dir`
- Produces:
  - `ParseError(Exception)`
  - `parse_meeting(raw_dir, meeting, *, agenda_required: bool) -> ParsedMeeting`
  - `ParsedMeeting` 数据类：`.wg` `.meeting` `.events: list[dict]` `.unaligned: list[str]` `.unmatched_ratio: float` `.minutes_version: int | None`
  - `write_parsed(parsed, out_dir) -> Path`

- [ ] **Step 1: 写失败的测试**

```python
# tests/test_parse_runner.py
import json, pathlib, pytest, shutil
from ngr.models import Meeting
from ngr.parse.runner import parse_meeting, write_parsed, ParseError

FIX126 = pathlib.Path("tests/fixtures/RAN1_126")
MTG = Meeting(wg="RAN1", number=126, suffix="", url="https://x/TSGR1_126/")

def test_parse_meeting_on_fixture(tmp_path):
    shutil.copytree(FIX126, tmp_path / "raw")
    p = parse_meeting(tmp_path / "raw", MTG, agenda_required=True)
    assert len(p.events) == 320 + 29 + 13
    assert p.unmatched_ratio < 0.20
    assert p.minutes_version == 10

def test_events_carry_agenda_item_when_aligned(tmp_path):
    shutil.copytree(FIX126, tmp_path / "raw")
    p = parse_meeting(tmp_path / "raw", MTG, agenda_required=True)
    sixg = [e for e in p.events if e.get("agenda_item", "").startswith("10")]
    assert sixg, "6GR 议程项下应有事件"
    assert all("heading_path" in e and "text_en" in e for e in p.events)

def test_events_keep_heading_path_when_agenda_absent(tmp_path):
    """5G-A 老会议没有 agenda.csv：事件照常产出，只是没有 agenda_item。"""
    raw = tmp_path / "raw"; raw.mkdir()
    shutil.copy(FIX126 / "minutes.docx", raw / "minutes.docx")
    p = parse_meeting(raw, MTG, agenda_required=False)
    assert len(p.events) == 362
    assert all(e["agenda_item"] is None for e in p.events)
    assert any(e["heading_path"] for e in p.events)

def test_missing_agenda_raises_when_required(tmp_path):
    raw = tmp_path / "raw"; raw.mkdir()
    shutil.copy(FIX126 / "minutes.docx", raw / "minutes.docx")
    with pytest.raises(ParseError, match="agenda"):
        parse_meeting(raw, MTG, agenda_required=True)

def test_missing_minutes_raises(tmp_path):
    raw = tmp_path / "raw"; raw.mkdir()
    with pytest.raises(ParseError, match="minutes"):
        parse_meeting(raw, MTG, agenda_required=False)

def test_zero_headings_raises(tmp_path, monkeypatch):
    shutil.copytree(FIX126, tmp_path / "raw")
    from ngr.parse import runner
    monkeypatch.setattr(runner, "parse_docx",
                        lambda p: type("D", (), {"headings": [], "blocks": [], "paragraphs": []})())
    with pytest.raises(ParseError, match="heading"):
        parse_meeting(tmp_path / "raw", MTG, agenda_required=True)

def test_zero_events_raises(tmp_path, monkeypatch):
    shutil.copytree(FIX126, tmp_path / "raw")
    from ngr.parse import runner
    monkeypatch.setattr(runner, "extract_events", lambda doc: [])
    with pytest.raises(ParseError, match="事件"):
        parse_meeting(tmp_path / "raw", MTG, agenda_required=True)

def test_high_unmatched_ratio_raises(tmp_path, monkeypatch):
    shutil.copytree(FIX126, tmp_path / "raw")
    from ngr.parse import runner
    from ngr.parse.align import Alignment
    from ngr.models import Heading
    bad = Alignment(by_heading={}, unaligned=[Heading(1, "x", 0)])
    monkeypatch.setattr(runner, "align", lambda a, h: bad)
    with pytest.raises(ParseError, match="未对齐"):
        parse_meeting(tmp_path / "raw", MTG, agenda_required=True)

def test_write_parsed_is_deterministic(tmp_path):
    shutil.copytree(FIX126, tmp_path / "raw")
    p = parse_meeting(tmp_path / "raw", MTG, agenda_required=True)
    a = write_parsed(p, tmp_path / "out1").read_bytes()
    b = write_parsed(p, tmp_path / "out2").read_bytes()
    assert a == b, "同一输入必须产出逐字节相同的 JSON（幂等性前提）"
    assert json.loads(a)["wg"] == "RAN1"
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/Scripts/python.exe -m pytest tests/test_parse_runner.py -v`
Expected: FAIL，`No module named 'ngr.parse.runner'`

- [ ] **Step 3: 写 `ngr/parse/runner.py`**

```python
from __future__ import annotations
import json
from dataclasses import dataclass, field
from pathlib import Path
from ngr.models import Meeting
from ngr.parse.agenda import parse_agenda
from ngr.parse.align import align
from ngr.parse.docx import parse_docx
from ngr.parse.events import extract_events
from ngr.parse.manifest_helpers import read_minutes_version   # 见 Step 4
from ngr.paths import P

MAX_UNMATCHED_RATIO = 0.20

class ParseError(Exception):
    """解析退化。必须硬失败：保留 raw、不写 state、不 commit。"""

@dataclass
class ParsedMeeting:
    wg: str
    meeting: int
    events: list[dict] = field(default_factory=list)
    unaligned: list[str] = field(default_factory=list)
    unmatched_ratio: float = 0.0
    minutes_version: int | None = None

def parse_meeting(raw_dir: Path, meeting: Meeting, *,
                  agenda_required: bool) -> ParsedMeeting:
    raw_dir = Path(raw_dir)
    minutes = raw_dir / "minutes.docx"
    if not minutes.exists():
        raise ParseError(f"{meeting.label}: 缺少 minutes.docx，无法解析")

    agenda_path = raw_dir / "agenda.csv"
    if agenda_required and not agenda_path.exists():
        raise ParseError(
            f"{meeting.label}: 缺少 agenda.csv，但该会议被标记为应有议程锚点。"
            "若这是 5G-A 老会议，请把 sources.yaml 的 agenda_csv_since 调对。")

    doc = parse_docx(minutes)
    if not doc.headings:
        raise ParseError(f"{meeting.label}: 纪要解析出 0 个 heading —— 模板很可能变了")

    raw_events = extract_events(doc)
    if not raw_events:
        raise ParseError(f"{meeting.label}: 解析出 0 条事件 —— 标记正则很可能失效了")

    alignment = None
    if agenda_path.exists():
        agenda = parse_agenda(agenda_path.read_bytes())
        alignment = align(agenda, doc.headings)
        if alignment.unmatched_ratio > MAX_UNMATCHED_RATIO:
            raise ParseError(
                f"{meeting.label}: 未对齐议程项占比 {alignment.unmatched_ratio:.0%} "
                f"超过阈值 {MAX_UNMATCHED_RATIO:.0%} —— 议程或纪要模板已变")

    # heading 文本 → 议程项（由 para_index 反查）
    head_by_text: dict[str, object] = {}
    if alignment:
        for h in doc.headings:
            item = alignment.by_heading.get(h.para_index)
            if item is not None:
                head_by_text[h.text] = item

    events = []
    for ev in raw_events:
        item = None
        for text in reversed(ev.heading_path):     # 取最深的已对齐祖先
            if text in head_by_text:
                item = head_by_text[text]
                break
        events.append({
            "kind": ev.kind,
            "text_en": ev.text_en,
            "para_index": ev.para_index,
            "heading_path": list(ev.heading_path),
            "agenda_item": item.item if item else None,
            "agenda_title": item.title if item else (ev.heading_path[-1] if ev.heading_path else ""),
        })

    return ParsedMeeting(
        wg=meeting.wg, meeting=meeting.number, events=events,
        unaligned=[h.text for h in (alignment.unaligned if alignment else [])],
        unmatched_ratio=alignment.unmatched_ratio if alignment else 0.0,
        minutes_version=read_minutes_version(raw_dir),
    )

def write_parsed(parsed: ParsedMeeting, out_dir: Path | None = None) -> Path:
    out_dir = Path(out_dir) if out_dir else P.parsed_dir(parsed.wg, parsed.meeting)
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "events.json"
    payload = {
        "wg": parsed.wg, "meeting": parsed.meeting,
        "minutes_version": parsed.minutes_version,
        "unmatched_ratio": round(parsed.unmatched_ratio, 4),
        "unaligned": parsed.unaligned,
        "events": parsed.events,
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True),
                    encoding="utf-8")
    return path
```

- [ ] **Step 4: 写 `ngr/parse/manifest_helpers.py`**

从 manifest 里读回纪要的版本号，避免 parse 层反向依赖 fetch 层的内部结构。

```python
from __future__ import annotations
import json
from pathlib import Path
from ngr.fetch.manifest import minutes_version

def read_minutes_version(raw_dir: Path) -> int | None:
    """从 _manifest.json 记录的原始 URL 里还原纪要版本号。"""
    man = Path(raw_dir) / "_manifest.json"
    if not man.exists():
        return None
    entry = json.loads(man.read_text(encoding="utf-8")).get("files", {}).get("minutes.docx")
    return minutes_version(entry["url"]) if entry and entry.get("url") else None
```

- [ ] **Step 5: 跑测试确认通过**

Run: `.venv/Scripts/python.exe -m pytest tests/test_parse_runner.py -v`
Expected: 9 passed

- [ ] **Step 6: 跑全部测试**

Run: `.venv/Scripts/python.exe -m pytest -v`
Expected: 全绿

- [ ] **Step 7: Commit**

```bash
git add ngr/parse/runner.py ngr/parse/manifest_helpers.py tests/test_parse_runner.py
git commit -m "feat(parse): 编排与沉默失败防线"
```

---

## Phase 3：map 层（血统归集）

### Task 12: 血统段匹配引擎

纯规则、无 LLM。给定一条 parsed 事件，判断它命中了哪个特性的哪个血统段。

**Files:**
- Create: `ngr/mapping/__init__.py`, `ngr/mapping/lineage.py`
- Test: `tests/test_mapping_lineage.py`

**Interfaces:**
- Consumes: `ngr.models.{Feature, LineageSegment}`
- Produces:
  - `Match` 数据类：`.feature_slug: str`、`.segment: LineageSegment`
  - `agenda_matches(patterns: list[str], wg: str, agenda_item: str | None) -> bool`
  - `match_event(features, wg, meeting, agenda_item, heading_path) -> Match | None`

- [ ] **Step 1: 写失败的测试**

```python
# tests/test_mapping_lineage.py
from ngr.models import Feature, LineageSegment
from ngr.mapping.lineage import agenda_matches, match_event

def seg(era="6G", depth="full", agenda=None, title_re=None, meetings=None):
    return LineageSegment(era=era, release="Rel-20", depth=depth,
                          agenda=agenda or [], title_re=title_re,
                          meetings=meetings or {"RAN1": (124, None)})

def feat(slug, *segs):
    return Feature(slug=slug, name_zh=slug, lineage=list(segs))

# —— agenda 通配 ——
def test_agenda_exact():
    assert agenda_matches(["RAN1:10.2"], "RAN1", "10.2")
    assert not agenda_matches(["RAN1:10.2"], "RAN1", "10.3")

def test_agenda_wildcard_matches_children():
    assert agenda_matches(["RAN1:10.2.*"], "RAN1", "10.2.1")
    assert agenda_matches(["RAN1:10.2.*"], "RAN1", "10.2.1.3")

def test_agenda_wildcard_does_not_match_self():
    assert not agenda_matches(["RAN1:10.2.*"], "RAN1", "10.2")

def test_agenda_wildcard_does_not_match_sibling_prefix():
    """10.2.* 不该命中 10.20 —— 前缀匹配必须按点分段。"""
    assert not agenda_matches(["RAN1:10.2.*"], "RAN1", "10.20")

def test_agenda_respects_wg():
    assert not agenda_matches(["RAN1:10.2"], "RAN2", "10.2")

def test_agenda_none_never_matches():
    assert not agenda_matches(["RAN1:10.2"], "RAN1", None)

# —— 事件匹配 ——
def test_match_by_agenda():
    f = feat("waveform", seg(agenda=["RAN1:10.2"]))
    m = match_event([f], "RAN1", 126, "10.2", ["Rel-20 Study of 6GR", "Waveform"])
    assert m.feature_slug == "waveform" and m.segment.depth == "full"

def test_match_by_title_re_when_no_agenda():
    """5G-A 老会议没有议程号，只能靠标题正则。"""
    f = feat("isac", seg(era="5G-A", depth="origin", title_re="(?i)ISAC",
                         meetings={"RAN1": (116, 123)}))
    m = match_event([f], "RAN1", 120, None, ["Rel-19 NR", "ISAC channel model"])
    assert m.feature_slug == "isac" and m.segment.era == "5G-A"

def test_title_re_checks_whole_heading_path():
    f = feat("isac", seg(title_re="(?i)6GR"))
    assert match_event([f], "RAN1", 126, None, ["Rel-20 Study of 6GR", "Evaluations"])

def test_no_match_outside_meeting_range():
    f = feat("isac", seg(agenda=["RAN1:10.8"], meetings={"RAN1": (124, 126)}))
    assert match_event([f], "RAN1", 127, "10.8", []) is None

def test_no_match_for_other_wg():
    f = feat("isac", seg(agenda=["RAN1:10.8"]))
    assert match_event([f], "RAN2", 126, "10.8", []) is None

def test_agenda_wins_over_title_re_within_same_segment():
    f = feat("x", seg(agenda=["RAN1:10.2"], title_re="(?i)nothing"))
    assert match_event([f], "RAN1", 126, "10.2", ["Waveform"])

def test_first_feature_in_file_order_wins_on_tie():
    """两个特性都命中时取 features.yaml 中靠前的 —— 结果必须可复现。"""
    a = feat("aaa", seg(title_re="(?i)ISAC"))
    b = feat("bbb", seg(title_re="(?i)ISAC"))
    assert match_event([a, b], "RAN1", 126, None, ["ISAC"]).feature_slug == "aaa"

def test_six_g_segment_preferred_over_legacy_when_both_hit():
    """同一特性内 6G 段与 5G-A 段同时覆盖某次会议时，取 6G 段。"""
    f = feat("isac",
             seg(era="5G-A", depth="origin", title_re="(?i)ISAC", meetings={"RAN1": (116, 130)}),
             seg(era="6G", depth="full", title_re="(?i)ISAC", meetings={"RAN1": (124, None)}))
    assert match_event([f], "RAN1", 126, None, ["ISAC"]).segment.era == "6G"
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/Scripts/python.exe -m pytest tests/test_mapping_lineage.py -v`
Expected: FAIL，`No module named 'ngr.mapping'`

- [ ] **Step 3: 写 `ngr/mapping/lineage.py`**

```python
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
                  agenda_item: str | None, heading_path: list[str]) -> bool:
    if not seg.covers(wg, meeting):
        return False
    if seg.agenda and agenda_matches(seg.agenda, wg, agenda_item):
        return True
    if seg.title_re:
        rx = _compiled(seg.title_re)
        return any(rx.search(text) for text in heading_path)
    return False

def match_event(features: list[Feature], wg: str, meeting: int,
                agenda_item: str | None, heading_path: list[str]) -> Match | None:
    """返回首个命中的 (特性, 血统段)。
    顺序规则（保证结果可复现）：
      1. 按 features.yaml 中特性的书写顺序；
      2. 同一特性内，6G 段优先于 5G-A 段 —— 会议进入 6G 阶段后不应再算作历史。"""
    for feat in features:
        segs = sorted(feat.lineage, key=lambda s: 0 if s.era == "6G" else 1)
        for seg in segs:
            if _segment_hits(seg, wg, meeting, agenda_item, heading_path):
                return Match(feature_slug=feat.slug, segment=seg)
    return None
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/Scripts/python.exe -m pytest tests/test_mapping_lineage.py -v`
Expected: 14 passed

- [ ] **Step 5: Commit**

```bash
git add ngr/mapping/ tests/test_mapping_lineage.py
git commit -m "feat(map): 血统段匹配引擎"
```

---

### Task 13: map 编排、state 写入与 lineage-report

> **里程碑：本任务完成后，`parsed → state` 全链路打通，agreement 已按血统归集入库。**

`lineage-report` 不是锦上添花 —— 5G-A 段的 `title_re` 必然要反复调，没有这个"改正则 → remap → 看命中"的秒级闭环，血统追溯根本做不下去。

**Files:**
- Create: `ngr/mapping/runner.py`, `ngr/mapping/report.py`
- Test: `tests/test_mapping_runner.py`

**Interfaces:**
- Consumes: `match_event`、`ngr.models.Event`、`ngr.config.load_features`
- Produces:
  - `map_meeting(parsed: dict, features, meeting_end=None) -> list[Event]`
  - `merge_events(existing: list[dict], incoming: list[Event], today: str) -> tuple[list[dict], MergeStats]`
  - `MergeStats`：`.added` `.changed` `.unchanged`
  - `write_state(events: list[dict], path) -> Path`
  - `lineage_report(features, parsed_meetings) -> str`

- [ ] **Step 1: 写失败的测试**

```python
# tests/test_mapping_runner.py
import json
from ngr.models import Feature, LineageSegment
from ngr.mapping.runner import map_meeting, merge_events, write_state
from ngr.mapping.report import lineage_report

def seg(era, depth, **kw):
    return LineageSegment(era=era, release=kw.get("release", "Rel-20"), depth=depth,
                          agenda=kw.get("agenda", []), title_re=kw.get("title_re"),
                          meetings=kw.get("meetings", {"RAN1": (124, None)}))

FEATS = [
    Feature(slug="waveform", name_zh="波形",
            lineage=[seg("6G", "full", agenda=["RAN1:10.2", "RAN1:10.2.*"])]),
    Feature(slug="isac", name_zh="ISAC",
            lineage=[seg("5G-A", "origin", release="Rel-19", title_re="(?i)ISAC",
                         meetings={"RAN1": (116, 123)}),
                     seg("6G", "full", agenda=["RAN1:10.8"])]),
]

def parsed(events):
    return {"wg": "RAN1", "meeting": 126, "minutes_version": 10,
            "unmatched_ratio": 0.0, "unaligned": [], "events": events}

def ev(kind="agreement", item="10.2", text="X", path=None):
    return {"kind": kind, "text_en": text, "para_index": 1,
            "heading_path": path or ["Rel-20 Study of 6GR", "Waveform"],
            "agenda_item": item, "agenda_title": "Waveform"}

def test_map_assigns_feature_era_and_depth():
    out = map_meeting(parsed([ev()]), FEATS)
    assert len(out) == 1
    e = out[0]
    assert e.feature == "waveform" and e.era == "6G" and e.depth == "full"

def test_unmatched_events_are_dropped():
    out = map_meeting(parsed([ev(item="8.1", path=["Maintenance"])]), FEATS)
    assert out == []

def test_seq_numbers_restart_per_agenda_item_and_kind():
    out = map_meeting(parsed([ev(), ev(), ev(kind="conclusion")]), FEATS)
    ids = [e.id for e in out]
    assert ids == ["RAN1-126-10.2-a001", "RAN1-126-10.2-a002", "RAN1-126-10.2-c001"]

def test_legacy_segment_marks_origin_depth():
    p = {"wg": "RAN1", "meeting": 120, "minutes_version": 100, "unmatched_ratio": 0.0,
         "unaligned": [], "events": [ev(item=None, path=["Rel-19 NR", "ISAC channel model"])]}
    out = map_meeting(p, FEATS)
    assert out[0].feature == "isac" and out[0].era == "5G-A" and out[0].depth == "origin"

def test_events_without_agenda_item_get_synthetic_key():
    """无议程号时用 heading 路径末节做 id 段，保证 id 仍然稳定。"""
    p = {"wg": "RAN1", "meeting": 120, "minutes_version": 100, "unmatched_ratio": 0.0,
         "unaligned": [], "events": [ev(item=None, path=["Rel-19 NR", "ISAC channel model"])]}
    out = map_meeting(p, FEATS)
    assert out[0].id.startswith("RAN1-120-")
    assert " " not in out[0].id

def test_content_hash_is_set():
    out = map_meeting(parsed([ev()]), FEATS)
    assert out[0].content_hash.startswith("sha256:")

# —— 合并 ——
def test_merge_adds_new_events():
    new = map_meeting(parsed([ev()]), FEATS)
    merged, stats = merge_events([], new, today="2026-09-17")
    assert stats.added == 1 and merged[0]["first_seen"] == "2026-09-17"

def test_merge_preserves_first_seen_and_llm_fields():
    new = map_meeting(parsed([ev()]), FEATS)
    existing = [{**new[0].__dict__, "id": new[0].id, "first_seen": "2026-01-01",
                 "summary_zh": "旧摘要", "llm_status": "ok"}]
    merged, stats = merge_events(existing, new, today="2026-09-17")
    assert stats.unchanged == 1
    assert merged[0]["first_seen"] == "2026-01-01"
    assert merged[0]["summary_zh"] == "旧摘要"

def test_merge_detects_text_change_and_invalidates_summary():
    """纪要 v010→v100 措辞微调：同一条 id，但摘要要重算。"""
    new = map_meeting(parsed([ev(text="NEW TEXT")]), FEATS)
    existing = [{**new[0].__dict__, "id": new[0].id, "text_en": "OLD TEXT",
                 "content_hash": "sha256:old", "first_seen": "2026-01-01",
                 "summary_zh": "旧摘要", "llm_status": "ok"}]
    merged, stats = merge_events(existing, new, today="2026-09-17")
    assert stats.changed == 1
    assert merged[0]["text_en"] == "NEW TEXT"
    assert merged[0]["summary_zh"] is None and merged[0]["llm_status"] == "pending"
    assert merged[0]["first_seen"] == "2026-01-01"

def test_merge_keeps_events_from_other_meetings():
    new = map_meeting(parsed([ev()]), FEATS)
    existing = [{"id": "RAN1-120-9.1-a001", "wg": "RAN1", "meeting": 120,
                 "text_en": "x", "first_seen": "2026-01-01"}]
    merged, _ = merge_events(existing, new, today="2026-09-17")
    assert len(merged) == 2

def test_write_state_is_sorted_and_deterministic(tmp_path):
    new = map_meeting(parsed([ev(), ev()]), FEATS)
    merged, _ = merge_events([], new, today="2026-09-17")
    a = write_state(merged, tmp_path / "a.json").read_bytes()
    b = write_state(list(reversed(merged)), tmp_path / "b.json").read_bytes()
    assert a == b, "事件顺序不同也必须产出相同字节 —— 否则 git diff 全是噪声"

# —— 血统报告 ——
def test_lineage_report_lists_hits_and_misses():
    txt = lineage_report(FEATS, [parsed([ev()])])
    assert "waveform" in txt and "6G" in txt
    assert "isac" in txt
    assert "0" in txt          # isac 的两段在本次会议都没命中
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/Scripts/python.exe -m pytest tests/test_mapping_runner.py -v`
Expected: FAIL，`No module named 'ngr.mapping.runner'`

- [ ] **Step 3: 写 `ngr/mapping/runner.py`**

```python
from __future__ import annotations
import hashlib, json, re
from collections import defaultdict
from dataclasses import dataclass, asdict
from pathlib import Path
from ngr.mapping.lineage import match_event
from ngr.models import Event, Feature

_SLUG_RE = re.compile(r"[^A-Za-z0-9.]+")

def _agenda_key(agenda_item: str | None, heading_path: list[str]) -> str:
    """没有议程号时（5G-A 老会议）用 heading 末节造一个稳定的 key。"""
    if agenda_item:
        return agenda_item
    tail = heading_path[-1] if heading_path else "unknown"
    return _SLUG_RE.sub("-", tail).strip("-").lower()[:40] or "unknown"

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

# 事件变更时要作废的 LLM 产物
_LLM_FIELDS = {"summary_zh": None, "tags": [], "impact": None, "llm_status": "pending"}

def merge_events(existing: list[dict], incoming: list[Event],
                 today: str) -> tuple[list[dict], MergeStats]:
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

    return list(by_id.values()), stats

def write_state(events: list[dict], path: Path) -> Path:
    """按 id 排序后写出。顺序稳定是幂等性的前提 —— 否则 git diff 全是噪声。"""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = sorted(events, key=lambda e: e["id"])
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True),
                    encoding="utf-8")
    return path
```

- [ ] **Step 4: 写 `ngr/mapping/report.py`**

```python
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
```

- [ ] **Step 5: 跑测试确认通过**

Run: `.venv/Scripts/python.exe -m pytest tests/test_mapping_runner.py -v`
Expected: 13 passed

- [ ] **Step 6: 端到端手动验证（真实 fixture 走完 parse → map）**

```bash
.venv/Scripts/python.exe -c "
import pathlib, json
from ngr.models import Meeting
from ngr.config import load_features
from ngr.parse.runner import parse_meeting
from ngr.mapping.runner import map_meeting, merge_events, write_state
from ngr.mapping.report import lineage_report
mtg = Meeting(wg='RAN1', number=126, suffix='', url='')
p = parse_meeting(pathlib.Path('tests/fixtures/RAN1_126'), mtg, agenda_required=True)
feats = load_features()
evs = map_meeting({'wg':'RAN1','meeting':126,'minutes_version':10,'unmatched_ratio':p.unmatched_ratio,'unaligned':p.unaligned,'events':p.events}, feats)
print(f'解析 {len(p.events)} 条，归集 {len(evs)} 条')
print(lineage_report(feats, [{'wg':'RAN1','meeting':126,'events':p.events}]))"
```

Expected: 解析出 362 条，归集数 > 0；血统报告中 6G 段有命中。**若某个 6G 段命中为 0，先调 `features.yaml` 的锚点，不要改代码。**

- [ ] **Step 7: Commit**

```bash
git add ngr/mapping/runner.py ngr/mapping/report.py tests/test_mapping_runner.py
git commit -m "feat(map): 血统归集、state 合并、lineage-report"
```

---

## Phase 4：render 层

### Task 14: Markdown 渲染

**Files:**
- Create: `ngr/render/__init__.py`, `ngr/render/markdown.py`
- Test: `tests/test_render_markdown.py`

**Interfaces:**
- Consumes: `state/events.json`、`state/features_state.json`、`ngr.models.Feature`
- Produces:
  - `render_dashboard(events, features, feat_state, *, banner=None, generated=...) -> str`
  - `render_feature_page(slug, events, feature, feat_state) -> str`
  - `render_report(wg, meeting, events, feature_names) -> str`
  - `tdoc_url(wg, meeting, filename) -> str`

- [ ] **Step 1: 写失败的测试**

```python
# tests/test_render_markdown.py
from ngr.models import Feature, LineageSegment
from ngr.render.markdown import render_dashboard, render_feature_page, render_report

def seg(era, depth="full"):
    return LineageSegment(era=era, release="Rel-20", depth=depth, agenda=["RAN1:10.2"],
                          title_re=None, meetings={"RAN1": (124, None)})

WAVE = Feature(slug="waveform", name_zh="6GR 波形与帧结构", lineage=[seg("6G")])
ISAC = Feature(slug="isac", name_zh="ISAC 通感一体",
               lineage=[seg("5G-A", "origin"), seg("6G")])

def E(**kw):
    base = dict(id="RAN1-126-10.2-a001", wg="RAN1", meeting=126, agenda_item="10.2",
                agenda_title="Waveform", kind="agreement", era="6G", release="Rel-20",
                depth="full", feature="waveform", text_en="Adopt X.",
                summary_zh="采纳 X。", tags=["OFDM"], impact="high", llm_status="ok",
                first_seen="2026-08-25", meeting_end="2026-08-21",
                source={"minutes_version": 10, "para": 10})
    base.update(kw)
    return base

FS = {"waveform": {"stage": "收敛中", "open_issues": ["A", "B"], "summary": "正在收敛。"},
      "isac": {"stage": "讨论中", "open_issues": [], "summary": "刚起步。",
               "legacy_summary": "Rel-19 只做了信道建模，波形未定。"}}

def test_dashboard_has_table_row_per_feature():
    md = render_dashboard([E()], [WAVE, ISAC], FS)
    assert "6GR 波形与帧结构" in md and "ISAC 通感一体" in md
    assert "收敛中" in md

def test_dashboard_marks_lineage_column():
    md = render_dashboard([E()], [WAVE, ISAC], FS)
    assert "6G 原生" in md and "5G-A→6G" in md

def test_dashboard_splits_counts_by_era():
    evs = [E(), E(id="x2", era="5G-A", depth="origin", feature="isac", meeting=120)]
    md = render_dashboard(evs, [WAVE, ISAC], FS)
    assert "1 / 0" in md or "1/0" in md      # waveform: 6G 1 条, 5G-A 0 条

def test_dashboard_open_issue_count():
    md = render_dashboard([E()], [WAVE], FS)
    assert "| 2 |" in md

def test_dashboard_banner_is_first_line_when_present():
    md = render_dashboard([E()], [WAVE], FS, banner="⚠️ 解析失败")
    assert md.splitlines()[0].startswith("⚠️")

def test_dashboard_lists_unmapped_section():
    md = render_dashboard([E()], [WAVE], FS, unmapped=["RAN1:10.7 NTN"])
    assert "待归类" in md and "10.7" in md

def test_feature_page_orders_sections():
    evs = [E(), E(id="x2", era="5G-A", depth="origin", meeting=120,
                  summary_zh=None, llm_status="skipped_by_depth")]
    md = render_feature_page("waveform", evs, WAVE, FS["waveform"])
    i_now = md.index("当前进展")
    i_6g = md.index("6GR 演进")
    i_leg = md.index("5G-A 历史事件")
    assert i_now < i_6g < i_leg

def test_feature_page_shows_legacy_summary_only_when_present():
    md_isac = render_feature_page("isac", [E(feature="isac")], ISAC, FS["isac"])
    assert "5G-A 源头" in md_isac
    md_wave = render_feature_page("waveform", [E()], WAVE, FS["waveform"])
    assert "5G-A 源头" not in md_wave

def test_feature_page_marks_era_on_each_event():
    md = render_feature_page("waveform", [E()], WAVE, FS["waveform"])
    assert "[6G/Rel-20 RAN1#126]" in md

def test_feature_page_always_shows_english_original():
    md = render_feature_page("waveform", [E(summary_zh=None, llm_status="failed")],
                             WAVE, FS["waveform"])
    assert "Adopt X." in md, "摘要可以缺，原文绝不能丢"

def test_feature_page_legacy_events_have_no_summary_but_have_text():
    evs = [E(id="x2", era="5G-A", depth="origin", meeting=120, summary_zh=None,
             llm_status="skipped_by_depth", text_en="Legacy decision.")]
    md = render_feature_page("waveform", evs, WAVE, FS["waveform"])
    assert "Legacy decision." in md

def test_report_groups_by_feature():
    md = render_report("RAN1", 126, [E()], {"waveform": "6GR 波形与帧结构"})
    assert "RAN1 #126" in md and "6GR 波形与帧结构" in md and "采纳 X。" in md

def test_report_includes_source_link():
    md = render_report("RAN1", 126, [E()], {"waveform": "6GR 波形与帧结构"})
    assert "3gpp.org" in md
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/Scripts/python.exe -m pytest tests/test_render_markdown.py -v`
Expected: FAIL，`No module named 'ngr.render'`

- [ ] **Step 3: 写 `ngr/render/markdown.py`**

```python
from __future__ import annotations
import time
from collections import defaultdict
from ngr.models import Feature

WG_PATH = {"RAN1": "tsg_ran/WG1_RL1/TSGR1_%d", "RAN2": "tsg_ran/WG2_RL2/TSGR2_%d",
           "RAN3": "tsg_ran/WG3_Iu/TSGR3_%d", "RAN4": "tsg_ran/WG4_Radio/TSGR4_%d",
           "RANP": "tsg_ran/TSG_RAN/TSGR_%d"}

def meeting_url(wg: str, meeting: int) -> str:
    tmpl = WG_PATH.get(wg)
    return f"https://www.3gpp.org/ftp/{tmpl % meeting}/" if tmpl else ""

def _era_tag(e: dict) -> str:
    return f"[{e.get('era')}/{e.get('release')} {e['wg']}#{e['meeting']}]"

def _by_feature(events: list[dict]) -> dict[str, list[dict]]:
    out = defaultdict(list)
    for e in events:
        out[e.get("feature")].append(e)
    return out

def feat_wg(events: list[dict]) -> str:
    """该特性最近活动所在的工作组；多组时取最新会议那条的组。"""
    if not events:
        return ""
    return max(events, key=lambda e: e["meeting"])["wg"]

def render_dashboard(events: list[dict], features: list[Feature],
                     feat_state: dict, *, banner: str | None = None,
                     unmapped: list[str] | None = None,
                     generated: str | None = None) -> str:
    generated = generated or time.strftime("%Y-%m-%d")
    grouped = _by_feature(events)
    latest_meeting = max((e["meeting"] for e in events), default=None)

    lines: list[str] = []
    if banner:
        lines += [banner, ""]
    lines += ["# 6G (Rel-20) RAN 进展看板", "",
              f"> 生成于 {generated}"
              + (f" · 最新会议 RAN1#{latest_meeting}" if latest_meeting else ""), "",
              "| 特性 | 阶段 | 血统 | 累计 Agr. (6G/5G-A) | 本期新增 | 最近活动 | 未决 |",
              "|---|---|---|---|---|---|---|"]

    for feat in features:
        evs = grouped.get(feat.slug, [])
        st = feat_state.get(feat.slug, {})
        agr = [e for e in evs if e["kind"] == "agreement"]
        n6 = sum(1 for e in agr if e.get("era") == "6G")
        nl = sum(1 for e in agr if e.get("era") == "5G-A")
        this = sum(1 for e in evs if e["meeting"] == latest_meeting) if latest_meeting else 0
        last = max((e["meeting"] for e in evs), default=None)
        lineage = "5G-A→6G" if feat.has_legacy else "6G 原生"
        last_cell = f"{feat_wg(evs)}#{last}" if last is not None else "—"
        lines.append(
            f"| [{feat.name_zh}](features/{feat.slug}.md) | {st.get('stage', '—')} "
            f"| {lineage} | {n6} / {nl} | **+{this}** | {last_cell} "
            f"| {len(st.get('open_issues', []))} |")

    if latest_meeting is not None:
        lines += ["", f"## 本期新增（最近一次会议 #{latest_meeting}）", ""]
        fresh = [e for e in events if e["meeting"] == latest_meeting]
        if not fresh:
            lines.append("_无_")
        for feat in features:
            items = [e for e in fresh if e.get("feature") == feat.slug]
            if not items:
                continue
            lines.append(f"- **{feat.name_zh}**：新增 {len(items)} 条")
            for e in items[:3]:
                lines.append(f"  - {e.get('summary_zh') or e['text_en'][:80]}")

    if unmapped:
        lines += ["", f"## ⚠️ 待归类议程项（{len(unmapped)} 个）", ""]
        lines += [f"- `{u}` — 请在 `config/features.yaml` 中确认归属" for u in unmapped]

    return "\n".join(lines) + "\n"

def render_feature_page(slug: str, events: list[dict], feature: Feature,
                        state: dict) -> str:
    mine = [e for e in events if e.get("feature") == slug]
    six = sorted([e for e in mine if e.get("era") == "6G"],
                 key=lambda e: (-e["meeting"], e["id"]))
    legacy = sorted([e for e in mine if e.get("era") == "5G-A"],
                    key=lambda e: (-e["meeting"], e["id"]))

    lines = [f"# {feature.name_zh}", "",
             f"**当前进展** · 阶段：{state.get('stage', '—')}", "",
             state.get("summary", "_尚无综述_"), ""]

    issues = state.get("open_issues") or []
    if issues:
        lines += ["**未决问题**", ""] + [f"- {i}" for i in issues] + [""]

    if feature.has_legacy and state.get("legacy_summary"):
        lines += ["## 5G-A 源头", "", state["legacy_summary"], ""]

    lines += ["## 6GR 演进", ""]
    lines += _render_events(six, with_summary=True) or ["_暂无_", ""]

    if legacy:
        lines += ["## 5G-A 历史事件", "",
                  "<details><summary>展开（原文，无中文摘要）</summary>", ""]
        lines += _render_events(legacy, with_summary=False)
        lines += ["</details>", ""]

    return "\n".join(lines) + "\n"

def _render_events(events: list[dict], *, with_summary: bool) -> list[str]:
    lines = []
    for e in events:
        lines.append(f"### {_era_tag(e)} `{e['kind']}` {e['agenda_item']} {e['agenda_title']}")
        if with_summary and e.get("summary_zh"):
            lines += ["", e["summary_zh"]]
        elif with_summary and e.get("llm_status") == "failed":
            lines += ["", "_（摘要生成失败，见下方原文）_"]
        lines += ["", "```text", e["text_en"], "```",
                  f"[原文出处]({meeting_url(e['wg'], e['meeting'])}) · `{e['id']}`", ""]
    return lines

def render_report(wg: str, meeting: int, events: list[dict],
                  feature_names: dict[str, str]) -> str:
    mine = [e for e in events if e["wg"] == wg and e["meeting"] == meeting]
    grouped = _by_feature(mine)
    lines = [f"# {wg} #{meeting} 增量简报", "",
             f"> 共 {len(mine)} 条事件 · [会议目录]({meeting_url(wg, meeting)})", ""]
    for slug, evs in sorted(grouped.items(), key=lambda kv: kv[0] or ""):
        lines += [f"## {feature_names.get(slug, slug)}（{len(evs)} 条）", ""]
        for e in evs:
            lines.append(f"- **{e['kind']}** {e['agenda_item']} — "
                         f"{e.get('summary_zh') or e['text_en'][:100]}")
        lines.append("")
    return "\n".join(lines) + "\n"
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/Scripts/python.exe -m pytest tests/test_render_markdown.py -v`
Expected: 13 passed

- [ ] **Step 5: Commit**

```bash
git add ngr/render/ tests/test_render_markdown.py
git commit -m "feat(render): dashboard / 特性页 / 会议简报"
```

---

### Task 15: 单文件 HTML 看板

> **里程碑：本任务完成后，`ngr run --no-llm` 能产出完整可读的看板 —— 工具已经有用了，只是没有中文摘要。**

**Files:**
- Create: `ngr/render/site.py`, `ngr/render/runner.py`
- Test: `tests/test_render_site.py`

**Interfaces:**
- Consumes: `render_dashboard`、`render_feature_page`、`render_report`
- Produces:
  - `render_site(events, features, feat_state, *, generated) -> str`（完整 HTML 文本）
  - `render_all(events, features, feat_state, out_dir, *, banner=None, unmapped=None) -> list[Path]`

- [ ] **Step 1: 开始写代码前先读配色与图表规范**

本任务要画热力图、状态表和筛选器。**先调用 `dataviz` skill 读取规范，再写第一行图表代码或选定任何颜色。** 不要凭感觉配色 —— 看板要在浅色/深色两种主题下都可读。

- [ ] **Step 2: 写失败的测试**

```python
# tests/test_render_site.py
import json, re
from ngr.models import Feature, LineageSegment
from ngr.render.site import render_site
from ngr.render.runner import render_all

def seg(era): return LineageSegment(era=era, release="Rel-20", depth="full",
                                    agenda=["RAN1:10.2"], title_re=None,
                                    meetings={"RAN1": (124, None)})
WAVE = Feature(slug="waveform", name_zh="6GR 波形", lineage=[seg("6G")])
FS = {"waveform": {"stage": "收敛中", "open_issues": [], "summary": "s"}}

def E(**kw):
    base = dict(id="RAN1-126-10.2-a001", wg="RAN1", meeting=126, agenda_item="10.2",
                agenda_title="Waveform", kind="agreement", era="6G", release="Rel-20",
                depth="full", feature="waveform", text_en="Adopt X.",
                summary_zh="采纳 X。", tags=[], impact="high", llm_status="ok",
                first_seen="2026-08-25", meeting_end="2026-08-21", source={})
    base.update(kw); return base

def test_site_is_self_contained():
    html = render_site([E()], [WAVE], FS, generated="2026-09-17")
    assert html.lstrip().startswith("<!DOCTYPE html>")
    assert "<script src=" not in html and "<link rel=\"stylesheet\"" not in html

def test_site_embeds_data_as_json():
    html = render_site([E()], [WAVE], FS, generated="2026-09-17")
    m = re.search(r'id="ngr-data"[^>]*>(.*?)</script>', html, re.S)
    assert m, "数据必须内联为 JSON"
    data = json.loads(m.group(1))
    assert data["events"][0]["id"] == "RAN1-126-10.2-a001"
    assert data["features"][0]["slug"] == "waveform"

def test_site_escapes_html_in_event_text():
    html = render_site([E(text_en="<script>alert(1)</script>")], [WAVE], FS,
                       generated="2026-09-17")
    assert "<script>alert(1)</script>" not in html

def test_site_declares_dark_mode():
    html = render_site([E()], [WAVE], FS, generated="2026-09-17")
    assert "prefers-color-scheme: dark" in html

def test_site_has_viewport_for_mobile():
    html = render_site([E()], [WAVE], FS, generated="2026-09-17")
    assert 'name="viewport"' in html

def test_site_renders_with_zero_events():
    html = render_site([], [WAVE], FS, generated="2026-09-17")
    assert "<!DOCTYPE html>" in html.lstrip()[:20]

def test_render_all_writes_expected_files(tmp_path):
    paths = render_all([E()], [WAVE], FS, tmp_path)
    names = {p.relative_to(tmp_path).as_posix() for p in paths}
    assert "dashboard.md" in names
    assert "features/waveform.md" in names
    assert "site/index.html" in names
    assert any(n.startswith("reports/") for n in names)

def test_render_all_is_deterministic(tmp_path):
    render_all([E()], [WAVE], FS, tmp_path, generated="2026-09-17")
    first = (tmp_path / "dashboard.md").read_bytes()
    render_all([E()], [WAVE], FS, tmp_path, generated="2026-09-17")
    assert (tmp_path / "dashboard.md").read_bytes() == first

def test_render_all_writes_empty_alerts_when_no_banner(tmp_path):
    render_all([E()], [WAVE], FS, tmp_path)
    assert (tmp_path / "ALERTS.md").read_text(encoding="utf-8").strip() == ""
```

- [ ] **Step 3: 跑测试确认失败**

Run: `.venv/Scripts/python.exe -m pytest tests/test_render_site.py -v`
Expected: FAIL，`No module named 'ngr.render.site'`

- [ ] **Step 4: 写 `ngr/render/site.py`**

按 Step 1 读到的 dataviz 规范确定配色与图表形式。骨架如下，**颜色 token 用规范里的值替换 `PLACEHOLDER` 注释处**：

```python
from __future__ import annotations
import html as html_mod, json
from dataclasses import asdict
from ngr.models import Feature

def _payload(events: list[dict], features: list[Feature], feat_state: dict,
             generated: str) -> dict:
    return {
        "generated": generated,
        "features": [{"slug": f.slug, "name_zh": f.name_zh,
                      "has_legacy": f.has_legacy,
                      "stage": feat_state.get(f.slug, {}).get("stage"),
                      "open_issues": feat_state.get(f.slug, {}).get("open_issues", [])}
                     for f in features],
        "events": events,
    }

def render_site(events: list[dict], features: list[Feature], feat_state: dict,
                *, generated: str) -> str:
    data = json.dumps(_payload(events, features, feat_state, generated),
                      ensure_ascii=False, sort_keys=True)
    # </script> 出现在数据里会提前闭合脚本标签
    data = data.replace("</", r"<\/")
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>6G RAN 进展看板</title>
<style>
  :root {{
    --bg: #ffffff; --fg: #1a1a1a; --muted: #666; --line: #e0e0e0;
    --accent: #2563eb;   /* 按 dataviz 规范替换为品牌色 */
  }}
  @media (prefers-color-scheme: dark) {{
    :root:not([data-theme="light"]) {{
      --bg: #141414; --fg: #eaeaea; --muted: #999; --line: #303030;
    }}
  }}
  :root[data-theme="dark"] {{
    --bg: #141414; --fg: #eaeaea; --muted: #999; --line: #303030;
  }}
  body {{ background: var(--bg); color: var(--fg); margin: 0;
         padding: 0 16px 48px; font: 15px/1.6 system-ui, sans-serif; }}
  table {{ border-collapse: collapse; width: 100%; }}
  th, td {{ border-bottom: 1px solid var(--line); padding: 8px 10px; text-align: left; }}
  details {{ border-bottom: 1px solid var(--line); padding: 6px 0; }}
  pre {{ overflow-x: auto; background: color-mix(in srgb, var(--fg) 5%, transparent);
         padding: 10px; border-radius: 6px; }}
  .filters {{ display: flex; gap: 8px; flex-wrap: wrap; margin: 16px 0; }}
</style>
</head>
<body>
<h1>6G (Rel-20) RAN 进展看板</h1>
<div class="filters" id="filters"></div>
<div id="board"></div>
<script type="application/json" id="ngr-data">{data}</script>
<script>
const DATA = JSON.parse(document.getElementById('ngr-data').textContent);
const esc = s => String(s ?? '').replace(/[&<>"']/g, c =>
  ({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}})[c]);
let filterFeature = null;

function render() {{
  const rows = DATA.features.map(f => {{
    const evs = DATA.events.filter(e => e.feature === f.slug);
    const agr = evs.filter(e => e.kind === 'agreement');
    const n6 = agr.filter(e => e.era === '6G').length;
    const nl = agr.filter(e => e.era === '5G-A').length;
    return `<tr><td><a href="#" data-slug="${{esc(f.slug)}}">${{esc(f.name_zh)}}</a></td>
      <td>${{esc(f.stage || '—')}}</td>
      <td>${{f.has_legacy ? '5G-A→6G' : '6G 原生'}}</td>
      <td>${{n6}} / ${{nl}}</td>
      <td>${{(f.open_issues || []).length}}</td></tr>`;
  }}).join('');

  const shown = DATA.events.filter(e => !filterFeature || e.feature === filterFeature);
  const items = shown.sort((a, b) => b.meeting - a.meeting).map(e =>
    `<details><summary>[${{esc(e.era)}} ${{esc(e.wg)}}#${{e.meeting}}]
       ${{esc(e.agenda_item)}} — ${{esc(e.summary_zh || e.text_en.slice(0, 90))}}</summary>
     <pre>${{esc(e.text_en)}}</pre></details>`).join('');

  document.getElementById('board').innerHTML =
    `<table><thead><tr><th>特性</th><th>阶段</th><th>血统</th>
     <th>累计 Agr. (6G/5G-A)</th><th>未决</th></tr></thead><tbody>${{rows}}</tbody></table>
     <h2>事件（${{shown.length}} 条）</h2>${{items || '<p>无</p>'}}`;

  document.querySelectorAll('[data-slug]').forEach(a => a.onclick = ev => {{
    ev.preventDefault();
    filterFeature = filterFeature === a.dataset.slug ? null : a.dataset.slug;
    render();
  }});
}}
render();
</script>
</body>
</html>
"""
```

- [ ] **Step 5: 写 `ngr/render/runner.py`**

```python
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
```

- [ ] **Step 6: 跑测试确认通过**

Run: `.venv/Scripts/python.exe -m pytest tests/test_render_site.py -v`
Expected: 9 passed

- [ ] **Step 7: 肉眼验收**

用 fixture 跑一遍并在浏览器里打开 `out/site/index.html`：点击特性名能筛选、展开能看到英文原文、切换系统深色主题后仍可读。

- [ ] **Step 8: Commit**

```bash
git add ngr/render/site.py ngr/render/runner.py tests/test_render_site.py
git commit -m "feat(render): 单文件 HTML 看板与渲染编排"
```

---

## Phase 5：extract 层（LLM）

### Task 16: claude CLI 后端、缓存与配额守护

**Files:**
- Create: `ngr/extract/__init__.py`, `ngr/extract/backend.py`, `ngr/extract/cache.py`, `ngr/extract/budget.py`
- Test: `tests/test_extract_backend.py`, `tests/test_extract_cache.py`, `tests/test_extract_budget.py`

**Interfaces:**
- Consumes: `ngr.config.ExtractConfig`
- Produces:
  - `ClaudeCli(model: str, effort: str)`，方法 `.call(prompt: str) -> CliResult`
  - `CliResult`：`.text: str`、`.usage: dict`、`.cost_usd: float`
  - `LlmError`、`LlmRateLimited(LlmError)`
  - `cache_key(model, prompt_version, effort, text) -> str`、`LlmCache(dir)` 带 `.get(key)` `.put(key, value)`
  - `Budget(max_calls)`，`.check()`（超限抛 `BudgetExhausted`）、`.spend(result)`、`.log(path)`

- [ ] **Step 1: 写后端的失败测试**

```python
# tests/test_extract_backend.py
import json, subprocess, pytest
from ngr.extract.backend import ClaudeCli, LlmError, LlmRateLimited

def fake_run(stdout="", returncode=0, stderr=""):
    def _run(cmd, **kw):
        _run.cmd, _run.input = cmd, kw.get("input")
        return subprocess.CompletedProcess(cmd, returncode, stdout, stderr)
    return _run

OK = json.dumps({"result": '{"ok":true}',
                 "total_cost_usd": 0.0095,
                 "usage": {"input_tokens": 2, "output_tokens": 8,
                           "cache_read_input_tokens": 14936,
                           "cache_creation_input_tokens": 1400}})

def test_call_passes_prompt_via_stdin(monkeypatch):
    run = fake_run(OK)
    monkeypatch.setattr(subprocess, "run", run)
    ClaudeCli("sonnet", "low").call("PROMPT")
    assert run.input == "PROMPT"
    assert "PROMPT" not in run.cmd, "prompt 绝不能走 argv —— Windows 命令行上限约 32K"

def test_call_uses_required_flags(monkeypatch):
    run = fake_run(OK)
    monkeypatch.setattr(subprocess, "run", run)
    ClaudeCli("sonnet", "low").call("x")
    cmd = run.cmd
    assert cmd[:2] == ["claude", "-p"]
    for flag in ["--output-format", "json", "--model", "sonnet",
                 "--effort", "low", "--restricted", "--disable-slash-commands"]:
        assert flag in cmd

def test_call_never_uses_bare(monkeypatch):
    """--bare 只认 ANTHROPIC_API_KEY，会绕开 Max 订阅的 OAuth 认证。"""
    run = fake_run(OK)
    monkeypatch.setattr(subprocess, "run", run)
    ClaudeCli("sonnet", "low").call("x")
    assert "--bare" not in run.cmd

def test_call_returns_text_and_usage(monkeypatch):
    monkeypatch.setattr(subprocess, "run", fake_run(OK))
    res = ClaudeCli("sonnet", "low").call("x")
    assert res.text == '{"ok":true}'
    assert res.cost_usd == 0.0095
    assert res.usage["cache_read_input_tokens"] == 14936

def test_nonzero_exit_raises(monkeypatch):
    monkeypatch.setattr(subprocess, "run", fake_run("", 1, "boom"))
    with pytest.raises(LlmError, match="boom"):
        ClaudeCli("sonnet", "low").call("x")

def test_rate_limit_message_raises_ratelimited(monkeypatch):
    monkeypatch.setattr(subprocess, "run",
                        fake_run("", 1, "Claude usage limit reached. Try again later"))
    with pytest.raises(LlmRateLimited):
        ClaudeCli("sonnet", "low").call("x")

def test_unparseable_stdout_raises(monkeypatch):
    monkeypatch.setattr(subprocess, "run", fake_run("not json"))
    with pytest.raises(LlmError, match="JSON"):
        ClaudeCli("sonnet", "low").call("x")

def test_timeout_raises_llm_error(monkeypatch):
    def boom(cmd, **kw): raise subprocess.TimeoutExpired(cmd, 600)
    monkeypatch.setattr(subprocess, "run", boom)
    with pytest.raises(LlmError, match="超时"):
        ClaudeCli("sonnet", "low").call("x")
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/Scripts/python.exe -m pytest tests/test_extract_backend.py -v`
Expected: FAIL，`No module named 'ngr.extract'`

- [ ] **Step 3: 写 `ngr/extract/backend.py`**

```python
from __future__ import annotations
import json, subprocess
from dataclasses import dataclass, field

TIMEOUT_SECONDS = 900
RATE_LIMIT_HINTS = ("usage limit", "rate limit", "too many requests", "429")

class LlmError(Exception):
    pass

class LlmRateLimited(LlmError):
    pass

@dataclass
class CliResult:
    text: str
    usage: dict = field(default_factory=dict)
    cost_usd: float = 0.0

class ClaudeCli:
    """通过 `claude -p` 调用，消耗 Max 订阅额度。

    三条硬约束：
      1. prompt 走 stdin —— Windows argv 上限约 32K，一批 40 条 agreement 远超；
      2. 禁用 --bare —— 该模式只认 ANTHROPIC_API_KEY，不读 OAuth，会绕开订阅认证；
      3. 带 --restricted 与 --disable-slash-commands —— 这是纯文本变换，
         不需要工具，也不能让 skills 插手批处理。
    """

    def __init__(self, model: str, effort: str):
        self.model, self.effort = model, effort

    @property
    def cmd(self) -> list[str]:
        return ["claude", "-p", "--output-format", "json",
                "--model", self.model, "--effort", self.effort,
                "--restricted", "--disable-slash-commands"]

    def call(self, prompt: str) -> CliResult:
        try:
            proc = subprocess.run(self.cmd, input=prompt, capture_output=True,
                                  text=True, encoding="utf-8",
                                  timeout=TIMEOUT_SECONDS)
        except subprocess.TimeoutExpired as exc:
            raise LlmError(f"claude -p 超时（{TIMEOUT_SECONDS}s）") from exc

        if proc.returncode != 0:
            err = (proc.stderr or "").strip()
            if any(h in err.lower() for h in RATE_LIMIT_HINTS):
                raise LlmRateLimited(f"额度受限: {err}")
            raise LlmError(f"claude -p 退出码 {proc.returncode}: {err}")

        try:
            payload = json.loads(proc.stdout)
        except json.JSONDecodeError as exc:
            raise LlmError(f"claude -p 输出不是 JSON: {proc.stdout[:200]}") from exc

        return CliResult(text=payload.get("result", ""),
                         usage=payload.get("usage", {}),
                         cost_usd=float(payload.get("total_cost_usd", 0.0)))
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/Scripts/python.exe -m pytest tests/test_extract_backend.py -v`
Expected: 8 passed

- [ ] **Step 5: 写缓存与配额的失败测试**

```python
# tests/test_extract_cache.py
from ngr.extract.cache import cache_key, LlmCache

def test_key_depends_on_all_inputs():
    a = cache_key("sonnet", "v1", "low", "TEXT")
    assert a != cache_key("opus", "v1", "low", "TEXT")
    assert a != cache_key("sonnet", "v2", "low", "TEXT")
    assert a != cache_key("sonnet", "v1", "high", "TEXT")
    assert a != cache_key("sonnet", "v1", "low", "OTHER")

def test_key_is_stable_across_runs():
    assert cache_key("sonnet", "v1", "low", "T") == cache_key("sonnet", "v1", "low", "T")

def test_cache_roundtrip(tmp_path):
    c = LlmCache(tmp_path)
    k = cache_key("sonnet", "v1", "low", "T")
    assert c.get(k) is None
    c.put(k, {"summary_zh": "摘要"})
    assert LlmCache(tmp_path).get(k) == {"summary_zh": "摘要"}

def test_cache_tolerates_corrupt_file(tmp_path):
    c = LlmCache(tmp_path)
    k = cache_key("sonnet", "v1", "low", "T")
    c.put(k, {"a": 1})
    next(tmp_path.glob("*.json")).write_text("{ broken", encoding="utf-8")
    assert LlmCache(tmp_path).get(k) is None
```

```python
# tests/test_extract_budget.py
import json, pytest
from ngr.extract.backend import CliResult
from ngr.extract.budget import Budget, BudgetExhausted

def test_check_passes_under_limit():
    b = Budget(max_calls=2)
    b.check(); b.spend(CliResult("x", {"output_tokens": 5}, 0.01))
    b.check()

def test_check_raises_when_exhausted():
    b = Budget(max_calls=1)
    b.check(); b.spend(CliResult("x", {}, 0.01))
    with pytest.raises(BudgetExhausted):
        b.check()

def test_totals_accumulate():
    b = Budget(max_calls=5)
    b.spend(CliResult("x", {"output_tokens": 5}, 0.01))
    b.spend(CliResult("y", {"output_tokens": 7}, 0.02))
    assert b.calls == 2
    assert round(b.cost_usd, 4) == 0.03

def test_log_appends_jsonl(tmp_path):
    b = Budget(max_calls=5)
    b.spend(CliResult("x", {"output_tokens": 5}, 0.01), task="summary")
    p = tmp_path / "usage.jsonl"
    b.log(p); b.log(p)
    lines = p.read_text(encoding="utf-8").strip().splitlines()
    assert len(lines) == 2
    assert json.loads(lines[0])["task"] == "summary"
```

- [ ] **Step 6: 跑测试确认失败**

Run: `.venv/Scripts/python.exe -m pytest tests/test_extract_cache.py tests/test_extract_budget.py -v`
Expected: FAIL，模块不存在

- [ ] **Step 7: 写 `ngr/extract/cache.py`**

```python
from __future__ import annotations
import hashlib, json, logging
from pathlib import Path

log = logging.getLogger(__name__)

def cache_key(model: str, prompt_version: str, effort: str, text: str) -> str:
    """把模型、prompt 版本、effort 一并计入 —— 任一变化都应重算。"""
    blob = "\x00".join([model, prompt_version, effort, text])
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()

class LlmCache:
    """按输入哈希缓存 LLM 结果，进 git —— 换台机器也能复用，不重复消耗额度。"""

    def __init__(self, directory: Path):
        self.dir = Path(directory)

    def _path(self, key: str) -> Path:
        return self.dir / f"{key}.json"

    def get(self, key: str) -> dict | None:
        p = self._path(key)
        if not p.exists():
            return None
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            log.warning("缓存文件损坏，忽略: %s", p)
            return None

    def put(self, key: str, value: dict) -> None:
        self.dir.mkdir(parents=True, exist_ok=True)
        self._path(key).write_text(
            json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True),
            encoding="utf-8")
```

- [ ] **Step 8: 写 `ngr/extract/budget.py`**

```python
from __future__ import annotations
import json, time
from pathlib import Path
from ngr.extract.backend import CliResult

class BudgetExhausted(Exception):
    """本次运行的调用上限已用尽。属正常结束，不是错误。"""

class Budget:
    """配额守护。额度是订阅制下的稀缺资源，一次运行绝不允许无限制消耗。"""

    def __init__(self, max_calls: int):
        self.max_calls = max_calls
        self.calls = 0
        self.cost_usd = 0.0
        self.input_tokens = 0
        self.output_tokens = 0
        self._entries: list[dict] = []

    def check(self) -> None:
        if self.calls >= self.max_calls:
            raise BudgetExhausted(
                f"已达本次运行上限 {self.max_calls} 次调用，剩余工作留到下次")

    def spend(self, result: CliResult, task: str = "") -> None:
        self.calls += 1
        self.cost_usd += result.cost_usd
        u = result.usage or {}
        self.input_tokens += int(u.get("input_tokens", 0)) \
            + int(u.get("cache_read_input_tokens", 0)) \
            + int(u.get("cache_creation_input_tokens", 0))
        self.output_tokens += int(u.get("output_tokens", 0))
        self._entries.append({
            "ts": time.strftime("%Y-%m-%dT%H:%M:%S"), "task": task,
            "cost_usd": result.cost_usd, "usage": u,
        })

    def log(self, path: Path) -> None:
        """追加写 usage_log.jsonl。注意：订阅模式下 cost_usd 是按 list price
        折算的用量代理值，不是账单。"""
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as fh:
            for entry in self._entries:
                fh.write(json.dumps(entry, ensure_ascii=False) + "\n")
        self._entries.clear()
```

- [ ] **Step 9: 跑测试确认通过**

Run: `.venv/Scripts/python.exe -m pytest tests/test_extract_cache.py tests/test_extract_budget.py -v`
Expected: 8 passed

- [ ] **Step 10: Commit**

```bash
git add ngr/extract/ tests/test_extract_backend.py tests/test_extract_cache.py tests/test_extract_budget.py
git commit -m "feat(extract): claude CLI 后端、结果缓存、配额守护"
```

---

### Task 17: LLM 任务、schema 校验与幻觉拦截

CLI 没有 API 的 `output_config.format`，所以 JSON 只能靠提示词约束 + 自己校验 + 一次修复重试。

**Files:**
- Create: `ngr/extract/tasks.py`, `ngr/extract/runner.py`
- Test: `tests/test_extract_tasks.py`, `tests/test_extract_runner.py`

**Interfaces:**
- Consumes: `ClaudeCli`、`LlmCache`、`Budget`
- Produces:
  - `PROMPT_VERSION: str`
  - `build_summary_prompt(batch: list[dict]) -> str`
  - `parse_summary_response(text, expected_ids) -> dict[str, dict]`（抛 `SchemaError`）
  - `hallucination_flags(summary_zh: str, text_en: str) -> list[str]`
  - `extract_all(events, features, cfg, *, cli_factory, cache, budget) -> ExtractStats`

- [ ] **Step 1: 写 prompt 与校验的失败测试**

```python
# tests/test_extract_tasks.py
import json, pytest
from ngr.extract.tasks import (build_summary_prompt, parse_summary_response,
                               hallucination_flags, SchemaError, VALID_IMPACT, VALID_STAGE)

BATCH = [{"id": "RAN1-126-10.2-a001", "agenda_title": "Waveform",
          "text_en": "Adopt DFT-s-OFDM for uplink in R1-2605180."},
         {"id": "RAN1-126-10.2-a002", "agenda_title": "Waveform",
          "text_en": "Confirm 480 kHz SCS."}]

def test_prompt_contains_all_ids_and_texts():
    p = build_summary_prompt(BATCH)
    for e in BATCH:
        assert e["id"] in p and e["text_en"] in p

def test_prompt_forbids_rewriting_original():
    p = build_summary_prompt(BATCH)
    assert "不要改写" in p or "不得改写" in p

def test_prompt_pins_enum_values():
    p = build_summary_prompt(BATCH)
    for v in VALID_IMPACT:
        assert v in p

def test_parse_valid_response():
    body = json.dumps({"results": [
        {"id": "RAN1-126-10.2-a001", "summary_zh": "采纳上行 DFT-s-OFDM。",
         "tags": ["DFT-s-OFDM"], "impact": "high"},
        {"id": "RAN1-126-10.2-a002", "summary_zh": "确认 480 kHz SCS。",
         "tags": [], "impact": "medium"}]})
    got = parse_summary_response(body, [e["id"] for e in BATCH])
    assert got["RAN1-126-10.2-a001"]["impact"] == "high"

def test_parse_tolerates_markdown_fence():
    body = '```json\n{"results":[{"id":"RAN1-126-10.2-a001","summary_zh":"x",' \
           '"tags":[],"impact":"low"}]}\n```'
    got = parse_summary_response(body, ["RAN1-126-10.2-a001"])
    assert got["RAN1-126-10.2-a001"]["summary_zh"] == "x"

def test_parse_rejects_invalid_impact():
    body = json.dumps({"results": [{"id": "RAN1-126-10.2-a001", "summary_zh": "x",
                                    "tags": [], "impact": "critical"}]})
    with pytest.raises(SchemaError, match="impact"):
        parse_summary_response(body, ["RAN1-126-10.2-a001"])

def test_parse_rejects_unknown_id():
    body = json.dumps({"results": [{"id": "BOGUS", "summary_zh": "x",
                                    "tags": [], "impact": "low"}]})
    with pytest.raises(SchemaError, match="id"):
        parse_summary_response(body, ["RAN1-126-10.2-a001"])

def test_parse_rejects_non_json():
    with pytest.raises(SchemaError, match="JSON"):
        parse_summary_response("对不起，我无法处理。", ["x"])

def test_parse_allows_partial_results():
    """少返回几条不算错 —— 缺的会在下次运行补上，不能因此丢弃整批。"""
    body = json.dumps({"results": [{"id": "RAN1-126-10.2-a001", "summary_zh": "x",
                                    "tags": [], "impact": "low"}]})
    got = parse_summary_response(body, [e["id"] for e in BATCH])
    assert set(got) == {"RAN1-126-10.2-a001"}

# —— 幻觉拦截 ——
def test_flags_tdoc_number_not_in_source():
    f = hallucination_flags("参见 R1-2699999 的提案。", "Adopt X. See R1-2605180.")
    assert any("R1-2699999" in x for x in f)

def test_no_flag_when_tdoc_present_in_source():
    assert hallucination_flags("参见 R1-2605180。", "See R1-2605180.") == []

def test_flags_number_not_in_source():
    f = hallucination_flags("确认 960 kHz SCS。", "Confirm 480 kHz SCS.")
    assert any("960" in x for x in f)

def test_does_not_flag_numbers_present_in_source():
    assert hallucination_flags("确认 480 kHz。", "Confirm 480 kHz SCS.") == []

def test_does_not_flag_small_ordinals():
    """'第 1 点''两三条'这类小数字不该触发告警。"""
    assert hallucination_flags("有 2 个选项待定。", "Options A and B are FFS.") == []
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/Scripts/python.exe -m pytest tests/test_extract_tasks.py -v`
Expected: FAIL，`No module named 'ngr.extract.tasks'`

- [ ] **Step 3: 写 `ngr/extract/tasks.py`**

```python
from __future__ import annotations
import json, re

PROMPT_VERSION = "v1"
VALID_IMPACT = ("high", "medium", "low")
VALID_STAGE = ("未启动", "讨论中", "收敛中", "已定稿")

TDOC_RE = re.compile(r"\bR[1-4]-\d{6,7}\b")
NUM_RE = re.compile(r"\d{3,}")          # 三位以上才检查，避免误伤序数词

class SchemaError(Exception):
    pass

SUMMARY_SYSTEM = f"""你在为 3GPP 6G (Rel-20) RAN 协议跟踪工具生成中文摘要。

规则：
1. 只依据我给你的英文原文，**不要改写原文**，也不要补充原文里没有的信息。
2. 不确定的地方宁可不写，绝不猜测。
3. 摘要 2–3 句，讲清"定了什么"，保留关键技术术语的英文原词。
4. tags 取 0–4 个技术关键词（英文原词）。
5. impact 只能是 {list(VALID_IMPACT)} 之一。

只输出 JSON，不要任何解释文字，格式：
{{"results": [{{"id": "...", "summary_zh": "...", "tags": ["..."], "impact": "high"}}]}}
"""

def build_summary_prompt(batch: list[dict]) -> str:
    parts = [SUMMARY_SYSTEM, "", "以下是需要摘要的条目：", ""]
    for e in batch:
        parts += [f"--- id: {e['id']}",
                  f"议程: {e.get('agenda_title', '')}",
                  "原文:", e["text_en"], ""]
    return "\n".join(parts)

def _strip_fence(text: str) -> str:
    t = text.strip()
    if t.startswith("```"):
        t = re.sub(r"^```[a-zA-Z]*\s*", "", t)
        t = re.sub(r"\s*```$", "", t)
    return t.strip()

def parse_summary_response(text: str, expected_ids: list[str]) -> dict[str, dict]:
    try:
        data = json.loads(_strip_fence(text))
    except json.JSONDecodeError as exc:
        raise SchemaError(f"响应不是合法 JSON: {text[:160]}") from exc

    results = data.get("results")
    if not isinstance(results, list):
        raise SchemaError("JSON 缺少 results 数组")

    allowed, out = set(expected_ids), {}
    for item in results:
        eid = item.get("id")
        if eid not in allowed:
            raise SchemaError(f"返回了未请求的 id: {eid!r}")
        impact = item.get("impact")
        if impact not in VALID_IMPACT:
            raise SchemaError(f"{eid} 的 impact 非法: {impact!r}")
        summary = item.get("summary_zh")
        if not isinstance(summary, str) or not summary.strip():
            raise SchemaError(f"{eid} 的 summary_zh 为空")
        tags = item.get("tags", [])
        if not isinstance(tags, list):
            raise SchemaError(f"{eid} 的 tags 不是数组")
        out[eid] = {"summary_zh": summary.strip(),
                    "tags": [str(t) for t in tags][:4], "impact": impact}
    return out

def hallucination_flags(summary_zh: str, text_en: str) -> list[str]:
    """摘要里出现、原文里没有的 TDoc 号与大数字 —— 标出来等人工核对。
    摘要是索引不是事实来源，这道防线保证索引错了也能一眼跳回原文。"""
    flags = []
    for tdoc in set(TDOC_RE.findall(summary_zh)):
        if tdoc not in text_en:
            flags.append(f"摘要中的 {tdoc} 未出现在原文")
    src_nums = set(NUM_RE.findall(text_en))
    for num in set(NUM_RE.findall(summary_zh)):
        if num not in src_nums:
            flags.append(f"摘要中的数字 {num} 未出现在原文")
    return flags
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/Scripts/python.exe -m pytest tests/test_extract_tasks.py -v`
Expected: 14 passed

- [ ] **Step 5: 写 extract 编排的失败测试**

```python
# tests/test_extract_runner.py
import json
from ngr.config import ExtractConfig
from ngr.extract.backend import CliResult, LlmRateLimited
from ngr.extract.budget import Budget
from ngr.extract.cache import LlmCache
from ngr.extract.runner import extract_all

CFG = ExtractConfig(backend="cli", max_calls_per_run=10, batch_size=2,
                    model_bulk="sonnet", model_digest="opus")

def ev(i, depth="full", status="pending"):
    return {"id": f"RAN1-126-10.2-a{i:03d}", "text_en": f"Adopt option {i}.",
            "agenda_title": "Waveform", "depth": depth, "llm_status": status,
            "feature": "waveform", "summary_zh": None, "tags": [], "impact": None}

class FakeCli:
    def __init__(self, replies): self.replies, self.calls = list(replies), []
    def call(self, prompt):
        self.calls.append(prompt)
        r = self.replies.pop(0)
        if isinstance(r, Exception): raise r
        return CliResult(text=r, usage={"output_tokens": 5}, cost_usd=0.01)

def reply(ids):
    return json.dumps({"results": [{"id": i, "summary_zh": f"摘要{i}",
                                    "tags": [], "impact": "low"} for i in ids]})

def test_summaries_are_written_back(tmp_path):
    evs = [ev(1), ev(2)]
    cli = FakeCli([reply([e["id"] for e in evs])])
    extract_all(evs, CFG, cli_factory=lambda m, e: cli,
                cache=LlmCache(tmp_path), budget=Budget(10))
    assert evs[0]["summary_zh"].startswith("摘要")
    assert evs[0]["llm_status"] == "ok"

def test_origin_depth_events_are_skipped(tmp_path):
    evs = [ev(1, depth="origin", status="skipped_by_depth")]
    cli = FakeCli([])
    stats = extract_all(evs, CFG, cli_factory=lambda m, e: cli,
                        cache=LlmCache(tmp_path), budget=Budget(10))
    assert cli.calls == [] and stats.skipped == 1

def test_batches_respect_batch_size(tmp_path):
    evs = [ev(i) for i in range(1, 6)]     # 5 条，batch_size=2 → 3 次调用
    cli = FakeCli([reply([e["id"] for e in evs[0:2]]),
                   reply([e["id"] for e in evs[2:4]]),
                   reply([e["id"] for e in evs[4:5]])])
    extract_all(evs, CFG, cli_factory=lambda m, e: cli,
                cache=LlmCache(tmp_path), budget=Budget(10))
    assert len(cli.calls) == 3

def test_cache_hit_avoids_call(tmp_path):
    evs = [ev(1), ev(2)]
    cache = LlmCache(tmp_path)
    cli1 = FakeCli([reply([e["id"] for e in evs])])
    extract_all(evs, CFG, cli_factory=lambda m, e: cli1, cache=cache, budget=Budget(10))
    for e in evs:
        e.update(summary_zh=None, llm_status="pending")
    cli2 = FakeCli([])
    extract_all(evs, CFG, cli_factory=lambda m, e: cli2, cache=cache, budget=Budget(10))
    assert cli2.calls == [] and evs[0]["summary_zh"].startswith("摘要")

def test_malformed_json_retries_once_then_marks_failed(tmp_path):
    evs = [ev(1)]
    cli = FakeCli(["не json", "still not json"])
    stats = extract_all(evs, CFG, cli_factory=lambda m, e: cli,
                        cache=LlmCache(tmp_path), budget=Budget(10))
    assert len(cli.calls) == 2
    assert evs[0]["llm_status"] == "failed" and evs[0]["summary_zh"] is None
    assert stats.failed == 1

def test_rate_limit_stops_cleanly_keeping_done_work(tmp_path):
    evs = [ev(i) for i in range(1, 5)]
    cli = FakeCli([reply([evs[0]["id"], evs[1]["id"]]), LlmRateLimited("limit")])
    stats = extract_all(evs, CFG, cli_factory=lambda m, e: cli,
                        cache=LlmCache(tmp_path), budget=Budget(10))
    assert evs[0]["llm_status"] == "ok"
    assert evs[2]["llm_status"] == "pending"     # 未处理的留待下次
    assert stats.rate_limited is True

def test_budget_exhaustion_stops_cleanly(tmp_path):
    evs = [ev(i) for i in range(1, 7)]
    cli = FakeCli([reply([evs[0]["id"], evs[1]["id"]])])
    stats = extract_all(evs, CFG, cli_factory=lambda m, e: cli,
                        cache=LlmCache(tmp_path), budget=Budget(1))
    assert stats.budget_exhausted is True
    assert evs[4]["llm_status"] == "pending"

def test_hallucination_flags_recorded(tmp_path):
    evs = [ev(1)]
    body = json.dumps({"results": [{"id": evs[0]["id"],
                                    "summary_zh": "参见 R1-2699999。",
                                    "tags": [], "impact": "low"}]})
    cli = FakeCli([body])
    extract_all(evs, CFG, cli_factory=lambda m, e: cli,
                cache=LlmCache(tmp_path), budget=Budget(10))
    assert evs[0]["llm_status"] == "needs_review"
    assert evs[0]["review_flags"]
```

- [ ] **Step 6: 跑测试确认失败**

Run: `.venv/Scripts/python.exe -m pytest tests/test_extract_runner.py -v`
Expected: FAIL，`No module named 'ngr.extract.runner'`

- [ ] **Step 7: 写 `ngr/extract/runner.py`**

```python
from __future__ import annotations
import logging
from dataclasses import dataclass
from ngr.config import ExtractConfig
from ngr.extract.backend import LlmError, LlmRateLimited
from ngr.extract.budget import BudgetExhausted
from ngr.extract.cache import cache_key
from ngr.extract.tasks import (PROMPT_VERSION, SchemaError, build_summary_prompt,
                               hallucination_flags, parse_summary_response)

log = logging.getLogger(__name__)
EFFORT_BULK = "low"

@dataclass
class ExtractStats:
    summarized: int = 0
    cached: int = 0
    skipped: int = 0
    failed: int = 0
    rate_limited: bool = False
    budget_exhausted: bool = False

def _apply(event: dict, payload: dict) -> None:
    flags = hallucination_flags(payload["summary_zh"], event["text_en"])
    event["summary_zh"] = payload["summary_zh"]
    event["tags"] = payload["tags"]
    event["impact"] = payload["impact"]
    if flags:
        event["review_flags"] = flags
        event["llm_status"] = "needs_review"
    else:
        event.pop("review_flags", None)
        event["llm_status"] = "ok"

def extract_all(events: list[dict], cfg: ExtractConfig, *,
                cli_factory, cache, budget) -> ExtractStats:
    """只为 depth == 'full' 且尚未成功摘要的事件调用 LLM。

    失败绝不阻断管线：schema 错重试一次，仍失败就标 failed、摘要留空，
    事件本身照常留在库里。摘要可以缺，agreement 不能丢。"""
    stats = ExtractStats()
    pending = []
    for e in events:
        if e.get("depth") != "full":
            stats.skipped += 1
            continue
        if e.get("llm_status") in ("ok", "needs_review"):
            continue
        key = cache_key(cfg.model_bulk, PROMPT_VERSION, EFFORT_BULK, e["text_en"])
        hit = cache.get(key)
        if hit:
            _apply(e, hit)
            stats.cached += 1
            continue
        pending.append((key, e))

    if not pending:
        return stats

    cli = cli_factory(cfg.model_bulk, EFFORT_BULK)
    for i in range(0, len(pending), cfg.batch_size):
        chunk = pending[i:i + cfg.batch_size]
        batch = [e for _, e in chunk]
        ids = [e["id"] for e in batch]
        prompt = build_summary_prompt(batch)

        try:
            budget.check()
        except BudgetExhausted:
            stats.budget_exhausted = True
            log.info("配额用尽，剩余 %d 条留待下次", len(pending) - i)
            break

        result = None
        for attempt in (1, 2):
            try:
                res = cli.call(prompt if attempt == 1 else
                               prompt + "\n\n上一次回复不是合法 JSON，请只输出 JSON。")
                budget.spend(res, task="summary")
                result = parse_summary_response(res.text, ids)
                break
            except LlmRateLimited:
                stats.rate_limited = True
                log.warning("额度受限，本次运行到此为止；已完成的结果已保存")
                return stats
            except (SchemaError, LlmError) as exc:
                log.warning("批次 %d 第 %d 次失败: %s", i // cfg.batch_size, attempt, exc)
                try:
                    budget.check()
                except BudgetExhausted:
                    stats.budget_exhausted = True
                    return stats

        if result is None:
            for e in batch:
                e["llm_status"] = "failed"
                stats.failed += 1
            continue

        for key, e in chunk:
            payload = result.get(e["id"])
            if payload is None:
                continue          # 少返回的条目保持 pending，下次补
            _apply(e, payload)
            cache.put(key, payload)
            stats.summarized += 1

    return stats
```

- [ ] **Step 8: 跑测试确认通过**

Run: `.venv/Scripts/python.exe -m pytest tests/test_extract_runner.py -v`
Expected: 8 passed

> 特性综述与 `legacy_summary`（spec §6.2 任务 ②③）在 Task 18 接入 —— 它们依赖已完成的事件摘要，放在编排层按特性触发更自然。本任务先把量最大、最需要缓存与配额保护的逐条摘要打通。

- [ ] **Step 9: Commit**

```bash
git add ngr/extract/tasks.py ngr/extract/runner.py tests/test_extract_tasks.py tests/test_extract_runner.py
git commit -m "feat(extract): 摘要 prompt、schema 校验、幻觉拦截、批次编排"
```

---

<!-- APPEND-HERE -->
