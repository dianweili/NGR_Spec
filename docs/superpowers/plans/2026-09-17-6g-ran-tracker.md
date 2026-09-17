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

<!-- APPEND-HERE -->
