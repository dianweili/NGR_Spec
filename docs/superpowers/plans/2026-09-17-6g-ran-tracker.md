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
- **修缺陷时改源头，不用追加打补丁。** 发现某处代码、注释或文档有错，就地改正那一处；不要保留错误内容、另在文末/别处追加一段说明来"覆盖"它。留下两处互相矛盾的表述，比原来那一处错误更糟 —— 读者不一定读到后加的那段，而先读到的那段会让他停止怀疑。需要保留修订痕迹时，源头改正 + 别处记"改了什么、为什么改"，而不是源头不动、别处打补丁。
  （此约束来自 Task 1 的实测教训：首轮漏报两条数据，二轮补了数据却没改声明，两次都是"证据本身没错、呈现方式在骗人"。）

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
  concurrency: 1          # 实测可用值；spec §4 的 2 为未验证上限
  delay_seconds: 2.0      # 实测 Task 1 全程 5s 串行无限流；0.5 未验证
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

注意：`ngr/cli.py` 到 Task 20 才写。在此之前 `python -m ngr` 会报 ImportError，这是预期的 —— 先建立可测的内核，命令面最后收口。

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
        minutes_re: '(?i)^Draft_Minutes.*\.(docx|zip)$'
        report_dirs: [Report, Reports]
        ls_dirs: [LSin, LSout]
        latest_meeting_with_content: 126
        artifacts: [agenda_csv, minutes_docx]
    http:
      user_agent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/140.0.0.0"
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

def test_load_sources_reads_per_group_fields(tmp_path):
    """这四个字段是实测后加的：各组纪要命名毫无共性，目录名还随年代变。"""
    wg = load_sources(write(tmp_path, "s.yaml", SOURCES_OK)).wgs["RAN1"]
    assert wg.minutes_re.startswith("(?i)")
    assert wg.report_dirs == ["Report", "Reports"]
    assert wg.ls_dirs == ["LSin", "LSout"]
    assert wg.latest_meeting_with_content == 126

def test_report_dirs_defaults_to_report(tmp_path):
    body = SOURCES_OK.replace("        report_dirs: [Report, Reports]
", "")
    assert load_sources(write(tmp_path, "s.yaml", body)).wgs["RAN1"].report_dirs == ["Report"]

def test_sources_requires_minutes_re(tmp_path):
    """缺 minutes_re 必须在启动时炸 —— 否则该组会静默产出空结果。"""
    body = SOURCES_OK.replace("        minutes_re: '(?i)^Draft_Minutes.*\\.(docx|zip)$'
", "")
    with pytest.raises(ConfigError, match="minutes_re"):
        load_sources(write(tmp_path, "s.yaml", body))

def test_sources_rejects_invalid_minutes_re(tmp_path):
    body = SOURCES_OK.replace("(?i)^Draft_Minutes.*", "(?i)^Draft_Minutes(.*")
    with pytest.raises(ConfigError, match="minutes_re"):
        load_sources(write(tmp_path, "s.yaml", body))

def test_sources_rejects_non_browser_user_agent(tmp_path):
    """默认 UA 会被 3GPP 的 WAF 挡成 403，配置写错必须在启动时就炸。"""
    bad = SOURCES_OK.replace("Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/140.0.0.0",
                             "python-requests/2.32")
    with pytest.raises(ConfigError, match="user_agent"):
        load_sources(write(tmp_path, "s.yaml", bad))

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

FEATURES_DUP_SLUG = """
    features:
      - slug: isac
        name_zh: ISAC 甲
        lineage:
          - { era: 6G, release: Rel-20, anchor: { agenda: ["RAN1:10.8"] },
              meetings: { RAN1: [124, null] }, depth: full }
      - slug: isac
        name_zh: ISAC 乙
        lineage:
          - { era: 6G, release: Rel-20, anchor: { agenda: ["RAN1:10.9"] },
              meetings: { RAN1: [124, null] }, depth: full }
    default_depth: origin
"""

def test_features_rejects_duplicate_slug(tmp_path):
    with pytest.raises(ConfigError, match="slug"):
        load_features(write(tmp_path, "f.yaml", FEATURES_DUP_SLUG))
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

def test_parse_listing_ignores_url_outside_href():
    """页面正文/注释里出现同一个目录 URL 时不得被当成条目 —— 实测 fixture 里就有这种文字。"""
    html = (b'<p>note: ' + DIR.encode() + b' retrieved 2026-09-17</p>'
            b'<a href="' + DIR.encode() + b'R1-1.zip">R1-1.zip</a>')
    assert parse_listing(html, DIR) == ["R1-1.zip"]

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
    """从 3GPP 的 HTML 目录列表中取出该目录的直接子条目名（不含更深层路径）。

    必须锚定到 href 属性，不能在全文里裸匹配 URL —— 页面正文、注释、
    脚本里都可能出现同一个目录 URL，裸匹配会把它们周围的文字当成文件名。
    实测 RAN1#126 的 Docs 列表用裸匹配得到 51 条（多出一条是页面里的说明文字），
    锚定 href 后恰好 50 条且全部是 R1-*.zip。
    """
    base = dir_url.rstrip("/") + "/"
    pattern = re.compile(r'href=["']' + re.escape(base) + r'([^"'/?#]+)')
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
              hard_floor=112, agenda_csv_since=124,
              minutes_re=r"(?i)minutes.*\.(docx|zip)$", artifacts=["agenda_csv"])

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

def test_fetch_window_none_when_all_segments_below_hard_floor():
    """全部血统段被 hard_floor 钳没时必须返回 None，不能返回 lo > hi 的倒置区间 ——
    倒置区间类型合法但语义非法，下游分不清是"没覆盖"还是"被钳没了"。"""
    feats = [_feature("a", [_seg(90, 100)])]          # hard_floor = 112
    assert fetch_window(feats, "RAN1", WG) is None

def test_fetch_window_survives_when_one_segment_reaches_above_floor():
    feats = [_feature("a", [_seg(90, 100)]), _feature("b", [_seg(95, 120)])]
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
  - `pick_latest_minutes(names: list[str], minutes_re: str) -> str | None`
  - `unwrap_docx(data: bytes) -> bytes`
  - `fetch_meeting(http, meeting, cfg, force=False) -> FetchResult`（`.changed: bool`、`.files: dict[str, Path]`、`.skipped_reason: str | None`）

- [ ] **Step 1: 写 manifest 的失败测试**

```python
# tests/test_fetch_manifest.py
from ngr.fetch.manifest import Manifest, minutes_version, pick_latest_minutes, unwrap_docx

RAN1_RE = r"(?i)^(Draft|Final)_Minutes_report_RAN1#\d+.*\.(zip|docx)$"
RAN2_RE = r"(?i)^R2-\d+\.zip$"

def test_minutes_version_parsing():
    assert minutes_version("Draft_Minutes_report_RAN1#126_v010.docx") == 10
    assert minutes_version("Draft_Minutes_report_RAN1#126_v100.docx") == 100
    assert minutes_version("Welcome.docx") is None

def test_minutes_version_accepts_zip():
    """实测：RAN1 ≤#122 的纪要以 zip 分发，只认 .docx 会让 5G-A 全线静默跳过。"""
    assert minutes_version("Final_Minutes_report_RAN1#112_v100.zip") == 100

def test_pick_latest_minutes_prefers_higher_version():
    names = ["Draft_Minutes_report_RAN1#126_v010.docx",
             "Draft_Minutes_report_RAN1#126_v100.docx", "Archive"]
    assert pick_latest_minutes(names, RAN1_RE) == "Draft_Minutes_report_RAN1#126_v100.docx"

def test_pick_latest_minutes_finds_zip_only_meeting():
    names = ["Final_Minutes_report_RAN1#112_v100.zip", "Archive"]
    assert pick_latest_minutes(names, RAN1_RE) == "Final_Minutes_report_RAN1#112_v100.zip"

def test_pick_latest_minutes_prefers_docx_over_zip_at_same_version():
    names = ["Draft_Minutes_report_RAN1#123_v100.zip",
             "Draft_Minutes_report_RAN1#123_v100.docx"]
    assert pick_latest_minutes(names, RAN1_RE) == "Draft_Minutes_report_RAN1#123_v100.docx"

def test_pick_latest_minutes_version_beats_format():
    names = ["Draft_Minutes_report_RAN1#123_v100.zip",
             "Draft_Minutes_report_RAN1#123_v010.docx"]
    assert pick_latest_minutes(names, RAN1_RE) == "Draft_Minutes_report_RAN1#123_v100.zip"

def test_pick_latest_minutes_returns_none_when_absent():
    assert pick_latest_minutes(["Archive", "notes.txt"], RAN1_RE) is None

def test_pick_latest_minutes_ran2_tdoc_naming():
    """实测 RAN2 的纪要就是个 TDoc 号 zip，文件名里没有 minutes 字样。
    用 RAN1 的正则会零匹配 —— 这正是必须按组配置的原因。"""
    names = ["R2-2604502.zip", "Skeleton_Report_v001.zip", "TDoc_List.xlsx"]
    assert pick_latest_minutes(names, RAN2_RE) == "R2-2604502.zip"
    assert pick_latest_minutes(names, RAN1_RE) is None

def test_pick_latest_minutes_no_version_falls_back_to_name_order():
    names = ["R2-2604502.zip", "R2-2604999.zip"]
    assert pick_latest_minutes(names, RAN2_RE) == "R2-2604999.zip"

def test_unwrap_docx_picks_largest_inner_docx():
    """RAN2 的纪要 zip 内含 PartList / TDoc_List 等小文件，正文是最大的那个。"""
    import io as _io, zipfile as _zf, pathlib
    real = pathlib.Path("tests/fixtures/RAN1_126/minutes.docx").read_bytes()
    buf = _io.BytesIO()
    with _zf.ZipFile(buf, "w") as z:
        z.writestr("PartList.docx", b"x" * 100)
        z.writestr("R2-2604502.docx", real)
    out = unwrap_docx(buf.getvalue())
    assert _zf.ZipFile(_io.BytesIO(out)).namelist().count("word/document.xml") == 1

def test_unwrap_docx_passes_through_real_docx():
    import pathlib
    data = pathlib.Path("tests/fixtures/RAN1_126/minutes.docx").read_bytes()
    assert unwrap_docx(data) is data

def test_unwrap_docx_extracts_inner_docx():
    import io as _io, zipfile as _zf, pathlib
    inner = pathlib.Path("tests/fixtures/RAN1_126/minutes.docx").read_bytes()
    buf = _io.BytesIO()
    with _zf.ZipFile(buf, "w") as z:
        z.writestr("Final_Minutes_report_RAN1#112_v100.docx", inner)
    out = unwrap_docx(buf.getvalue())
    assert _zf.ZipFile(_io.BytesIO(out)).namelist().count("word/document.xml") == 1

def test_unwrap_docx_raises_when_no_docx_inside():
    import io as _io, zipfile as _zf, pytest as _pytest
    buf = _io.BytesIO()
    with _zf.ZipFile(buf, "w") as z:
        z.writestr("readme.txt", b"nothing here")
    with _pytest.raises(ValueError, match="docx"):
        unwrap_docx(buf.getvalue())

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
import hashlib, io, json, re, time, zipfile
from pathlib import Path

VERSION_RE = re.compile(r"(?i)_v(\d{3})\b")

def minutes_version(filename: str) -> int | None:
    """从文件名抽版本号。实测多数组的纪要文件名里根本没有 _v###
    （RAN2 的就是个 TDoc 号 R2-2604502.zip），此时返回 None 而非报错。"""
    m = VERSION_RE.search(filename)
    return int(m.group(1)) if m else None

def pick_latest_minutes(names: list[str], minutes_re: str) -> str | None:
    """纪要有 v010 → v100 的版本演进，永远取最高版本。

    候选由**该工作组配置的 `minutes_re`** 决定，不用全局正则 —— 实测各组命名毫无共性：
      RAN1  `Draft_Minutes_report_RAN1#126_v010.docx`（≤#122 为 .zip 包裹）
      RAN2  `R2-2604502.zip`  ← 纯 TDoc 号，文件名里没有 "minutes" 字样
      RAN3  三种形态并存（TDoc 号 / RP-…_draft_report_RAN3_133_… / draft_RAN3#131_…）
    用一条全局正则会让除 RAN1 外所有组零匹配、静默产出空结果。

    排序：有 `_v###` 的按版本号降序优先；都没有版本号时按文件名降序（TDoc 号越大越新）。
    同等次序下取 .docx 而非 .zip（省一次解压）。"""
    rx = re.compile(minutes_re)
    cands = [n for n in names if rx.search(n)]
    if not cands:
        return None
    def rank(n: str):
        v = minutes_version(n)
        fmt = 0 if n.lower().endswith(".docx") else -1
        # 次序：有版本号 > 无版本号 → 版本号大 > 小 → docx > zip → 文件名大 > 小。
        # 格式偏好必须排在文件名之前：同版本号的候选只差扩展名，
        # 若先比文件名，'...v100.docx' < '...v100.zip'（'d' < 'z'）会让 max() 选中 zip，
        # 格式偏好永远轮不到生效。文件名只作最后兜底（无版本号时按 TDoc 号取新）。
        return (0 if v is None else 1, v or 0, fmt, n)
    return max(cands, key=rank)

def unwrap_docx(data: bytes) -> bytes:
    """纪要常以 zip 分发；剥掉外层返回真正的 docx 字节。本身就是 docx 时原样返回。

    zip 内常有多个文件（实测 RAN2 的纪要 zip 含 `R2-2604502.docx` +
    PartList + TDoc_List），取**体积最大**的 docx —— 纪要正文远大于名单类附件。"""
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        infos = z.infolist()
        if any(i.filename == "word/document.xml" for i in infos):
            return data
        inner = [i for i in infos if i.filename.lower().endswith(".docx")]
        if not inner:
            raise ValueError(f"zip 内未找到 docx，条目: {[i.filename for i in infos][:10]}")
        return z.read(max(inner, key=lambda i: i.file_size).filename)

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
Expected: 19 passed

- [ ] **Step 5: 写抓取编排的失败测试**

```python
# tests/test_fetch_runner.py
import pytest
from unittest.mock import Mock
from urllib.parse import quote
from ngr.config import WgConfig
from ngr.models import Meeting
from ngr.fetch.manifest import Manifest
from ngr.fetch.runner import fetch_meeting

WG = WgConfig(path="tsg_ran/WG1_RL1", dir_re=r"TSGR1_(\d+)([a-z]*)", hard_floor=112,
              agenda_csv_since=124, minutes_re=r"(?i)minutes.*\.(docx|zip)$", 
              artifacts=["agenda_csv", "minutes_docx", "docs_listing"])
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
    """模拟真实 IIS 目录列表：href 里的文件名是百分号转义的。

    实测 3GPP 的 Report 目录 HTML 写的是
    `href=".../Final_Minutes_report_RAN1%23112_v100.zip"` —— `#` 是 `%23`，
    因为 `#` 在 URL 里是片段分隔符。parse_listing 的捕获类排除 `#` 正是为此，
    随后用 unquote() 还原。助手若不转义，文件名会在 `#` 处被截断，
    这条链路就测不到真实行为了。"""
    return b"".join(
        f'<a href="{dir_url}{quote(n)}">{n}</a>'.encode() for n in names)

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

def test_manifest_saved_when_rate_limited_midway(tmp_path):
    """限流中断时，本次已成功抓到的 artifact 必须落进 manifest。
    否则文件在磁盘上却查不到记录，下次重试会重新下载 —— 限流引发重复下载、
    重复下载又加剧限流。"""
    from ngr.fetch.client import RateLimited
    base = MTG.url
    listings = {
        base: _listing(base, ["Agenda", "Report"]),
        base + "Agenda/": _listing(base + "Agenda/", ["agenda.csv"]),
        base + "Report/": _listing(base + "Report/", ["Draft_Minutes_report_RAN1#126_v010.docx"]),
    }
    files = {base + "Agenda/agenda.csv": b"csv"}
    http = _http(listings, files)
    calls = {"n": 0}
    def head(url):
        calls["n"] += 1
        if calls["n"] > 1:                      # 第二个 artifact 撞限流
            raise RateLimited("rate limited")
        return {"etag": '"e"', "length": 3}
    http.head.side_effect = head

    with pytest.raises(RateLimited):
        fetch_meeting(http, MTG, WG, raw_dir=tmp_path)

    assert (tmp_path / "agenda.csv").exists()
    assert (tmp_path / "_manifest.json").exists(), "已成功的 artifact 必须落盘"
    assert "agenda.csv" in Manifest(tmp_path).load()["files"]

def test_report_dirs_picks_first_existing_candidate(tmp_path):
    """report_dirs 是**有序**候选列表：两个都存在时取列表里排前面的那个。
    实测 RAN4 老会议用复数 Reports、新会议用单数 Report。"""
    from dataclasses import replace
    base = MTG.url
    wg = replace(WG, report_dirs=["Reports", "Report"], artifacts=["minutes_docx"])
    listings = {
        base: _listing(base, ["Report", "Reports"]),
        base + "Reports/": _listing(base + "Reports/", ["Draft_Minutes_report_RAN1#126_v100.docx"]),
        base + "Report/": _listing(base + "Report/", ["Draft_Minutes_report_RAN1#126_v010.docx"]),
    }
    files = {base + "Reports/Draft_Minutes_report_RAN1#126_v100.docx": b"doc"}
    res = fetch_meeting(_http(listings, files), MTG, wg, raw_dir=tmp_path)
    assert res.changed and "minutes_docx" in res.files

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
from ngr.fetch.manifest import Manifest, pick_latest_minutes, unwrap_docx
from ngr.models import Meeting
from ngr.paths import P

log = logging.getLogger(__name__)

# artifact 名 → (子目录, 落地文件名, 在子目录里怎么选文件)
def _pick_exact(name):
    return lambda names: name if name in names else None

# minutes 的选择器需要该组的 minutes_re，故在 fetch_meeting 里按组构造
ARTIFACTS = {
    "agenda_csv":    ("Agenda/", "agenda.csv",   _pick_exact("agenda.csv")),
    "minutes_docx":  (None,      "minutes.docx", None),   # 子目录与选择器按组决定
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

    # 循环体用 try/finally 包住：中途抛 RateLimited 时，本次已 record() 成功的
    # artifact 必须落进 manifest。否则文件虽在磁盘上却查不到记录，下次重试会重新
    # 下载一遍 —— 限流引发重复下载、重复下载又加剧限流，方向正好反了。
    try:
        for art in cfg.artifacts:
            if art in ARTIFACTS:
                subdir, local, chooser = ARTIFACTS[art]
                if art == "minutes_docx":
                    # 纪要的子目录名与识别正则都按组配置：实测各组命名毫无共性，
                    # 且同一组的目录名会随年代变（RAN4 老会议 Reports / 新会议 Report）
                    hit = next((d for d in cfg.report_dirs if d.rstrip("/") in root_names), None)
                    if hit is None:
                        res.missing.append(art)
                        continue
                    subdir = hit.rstrip("/") + "/"
                    chooser = lambda names: pick_latest_minutes(names, cfg.minutes_re)
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
                    data = http.get(url)
                    if art == "minutes_docx" and chosen.lower().endswith(".zip"):
                        # 只有 zip 才需要剥壳，裸 .docx 直通。
                        # 无条件调用在真实数据上也能跑（.docx 本身就是合法 zip，
                        # unwrap_docx 检测到 word/document.xml 会原样返回），但
                        # "只有 zip 需要剥壳"语义更准确，也让测试不必为每个
                        # .docx 场景构造合法 zip 字节。
                        data = unwrap_docx(data)
                    man.record(local, url, head, data)
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
    finally:
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
import logging

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


def test_utf8_agenda_decodes_without_warning(caplog):
    """正常 UTF-8 文件不得产生任何告警 —— 探针的价值来自平时沉默。"""
    data = '"9.1","波形 Waveform"\n'.encode("utf-8")
    with caplog.at_level(logging.WARNING):
        items = parse_agenda(data)
    assert items[0].title == "波形 Waveform"
    assert caplog.text == ""


def test_non_utf8_agenda_warns_instead_of_silently_mangling(caplog):
    """非 UTF-8 文件会被解成乱码标题，对不上任何 heading。

    原来一上来就 errors="replace"，这种失真**毫无痕迹** —— 表现出来只是"对齐率低"。
    下游门禁能兜住全面乱码，但兜不住"只乱几条、比率仍在 20% 阈值内"那种错误却不显眼
    的结果。所以退让可以，不出声不行。
    """
    data = '"9.1","波形"\n'.encode("gbk")
    with caplog.at_level(logging.WARNING):
        items = parse_agenda(data)
    assert items[0].item == "9.1"          # 议程号是 ASCII，照常解析
    assert items[0].title != "波形"         # 标题已失真
    assert "不是 UTF-8" in caplog.text
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/Scripts/python.exe -m pytest tests/test_parse_agenda.py -v`
Expected: FAIL，`No module named 'ngr.parse'`

- [ ] **Step 3: 写 `ngr/parse/agenda.py`**

```python
from __future__ import annotations
import csv, io, logging
from ngr.models import AgendaItem

log = logging.getLogger(__name__)

def _decode(data: bytes) -> str:
    """按 UTF-8 → cp1252 的顺序解码，任何一次退让都要出声。

    原来一上来就 `errors="replace"`，把编码错误静默吞成 "�"：标题变乱码后对不上
    任何 heading，表现出来只是"这次对齐率有点低"，而真正的原因（文件不是 UTF-8）
    一点痕迹都没有。下游的 unmatched_ratio 门禁能兜住**全面**乱码（比率触顶 100%），
    但兜不住"只乱几条、比率仍在 20% 阈值内" —— 那会产出错误却不显眼的对齐结果。

    不直接抛错，是因为 3GPP 的 CSV 确实可能是 cp1252，硬失败会把正常文件挡在门外。
    退让本身可以接受，**不出声才是缺陷**。
    """
    try:
        return data.decode("utf-8-sig")
    except UnicodeDecodeError:
        pass
    try:
        text = data.decode("cp1252")
    except UnicodeDecodeError:
        log.warning("agenda.csv 既非 UTF-8 也非 cp1252，退到替换模式解码，标题很可能失真")
        return data.decode("utf-8-sig", "replace")
    log.warning("agenda.csv 不是 UTF-8，已按 cp1252 解码，标题可能失真")
    return text

def parse_agenda(data: bytes) -> list[AgendaItem]:
    """解析 3GPP 的 Agenda/agenda.csv，格式为 "<议程号>","<标题>" 两列无表头。"""
    text = _decode(data)
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
  - `Block` 数据类：`.kind: str`（`"para"` | `"table"`）、`.text: str`、`.style: str | None`、`.index: int`、
    `.cell_paras: list[str]`（仅 table 块有值：表格内各单元格段落的纯文本，按出现顺序。
    实测有 16 条标记藏在表格里：自有单元格 15 条 + 嵌套子表 1 条，不带出来下游就看不到。
    两者分开放是有意的 —— 详见 Step 3 的字段注释）、
    `.nested_paras: list[str]`（嵌套在单元格内的子表格段落，只当内容不开新事件）
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

def test_tab_and_break_become_separators():
    """w:tab / w:br 是独立元素，不补分隔符会把两侧文本焊死。
    实测 RAN1#126 有 3795 处 tab、48 处 br 落在两段无空白的文本之间。"""
    xml = ('<w:p><w:r><w:t>Opening of the meeting</w:t><w:tab/><w:t>5</w:t></w:r></w:p>'
           '<w:p><w:r><w:t>OLLA enabled</w:t><w:br/><w:t>Target BLER 10%</w:t></w:r></w:p>'
           '<w:p><w:r><w:t>Case 1</w:t><w:cr/><w:t>Case 2</w:t></w:r></w:p>')
    assert parse_docx(make_docx(xml)).paragraphs == [
        "Opening of the meeting\t5", "OLLA enabled\nTarget BLER 10%",
        "Case 1\nCase 2"]

def test_alternate_content_is_not_counted_twice():
    """Word 对同一个图形给出 mc:Choice 与 mc:Fallback 两份等价表示。
    两份都收会让文本原样重复一遍 —— 实测 Annex A-2 的日程表图示被拼成
    "RAN1 Brk 2RAN1 Brk 2RAN1 Brk 1RAN1 Brk 1..."。"""
    mc = "http://schemas.openxmlformats.org/markup-compatibility/2006"
    xml = (f'<w:p xmlns:mc="{mc}"><w:r><mc:AlternateContent>'
           '<mc:Choice Requires="wps"><w:p><w:r><w:t>Brk 2</w:t></w:r></w:p></mc:Choice>'
           '<mc:Fallback><w:p><w:r><w:t>Brk 2</w:t></w:r></w:p></mc:Fallback>'
           '</mc:AlternateContent></w:r><w:r><w:t>Annex A-2</w:t></w:r></w:p>')
    assert parse_docx(make_docx(xml)).paragraphs == ["Brk 2\nAnnex A-2"]

def test_nested_paragraphs_are_separated_from_surrounding_text():
    """文本框里的 w:p 各自成段，前后都要断开，否则与外层文本焊成一串
    （实测 "RAN1 MainAnnex A-2:"）。"""
    xml = ('<w:p><w:r><w:t>before</w:t></w:r>'
           '<w:r><w:p><w:r><w:t>boxed</w:t></w:r></w:p></w:r>'
           '<w:r><w:t>after</w:t></w:r></w:p>')
    assert parse_docx(make_docx(xml)).paragraphs == ["before\nboxed\nafter"]

def test_tab_stop_definition_is_not_a_tab_character():
    """<w:pPr><w:tabs><w:tab/></w:tabs></w:pPr> 是制表位定义，与制表符同名但不是字符。"""
    xml = ('<w:p><w:pPr><w:tabs><w:tab w:val="left" w:pos="720"/></w:tabs></w:pPr>'
           '<w:r><w:t>Agreement:</w:t></w:r></w:p>')
    assert parse_docx(make_docx(xml)).paragraphs == ["Agreement:"]

def test_cell_text_flattens_whitespace_for_markdown():
    """单元格里的换行必须压成空格，否则一个单元格就能撑断整张表的行结构。"""
    xml = ('<w:tbl><w:tr><w:tc><w:p><w:r><w:t>line1</w:t><w:br/><w:t>line2</w:t></w:r>'
           '</w:p></w:tc></w:tr></w:tbl>')
    blk = parse_docx(make_docx(xml)).blocks[0]
    assert blk.kind == "table"
    assert blk.text.splitlines()[0] == "| line1 line2 |"

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
    """实测 RAN1#126 v010 的确切数字 —— 3GPP 换纪要模板时这里第一个炸。

    注意 paragraphs 只数 body 的**直接子**段落：表格内的段落归到 table 块，
    不计入这里。（计划初稿写的 7803 是用正则匹配 <w:p> 量的，而正则处理不了
    表格内嵌套的 <w:p>，那个数字本身就是错的。）"""
    doc = parse_docx(pathlib.Path("tests/fixtures/RAN1_126/minutes.docx"))
    assert len(doc.paragraphs) == 5061
    assert len(doc.headings) == 83
    assert any(h.text == "Rel-20 Study of 6GR" and h.level == 1 for h in doc.headings)
    assert any(h.text == "Waveform for 6GR air interface" for h in doc.headings)

def test_real_fixture_marker_counts():
    doc = parse_docx(pathlib.Path("tests/fixtures/RAN1_126/minutes.docx"))
    assert sum(1 for p in doc.paragraphs if p.startswith("Agreement")) == 308
    assert sum(1 for p in doc.paragraphs if p.startswith("Conclusion")) == 26
    assert sum(1 for p in doc.paragraphs if p.lower().startswith("working assumption")) == 11

def test_real_fixture_table_wrapped_markers():
    """首个单元格就是标记的表格 —— 这些是"用表格画的框"，框里装着一条决议。
    parse 层必须把单元格段落带出来，否则 Task 9 看不到这些标记，约 4% 的
    agreement 会被静默丢弃。

    实测：12 张表格的自有单元格里带标记、共 15 条（11 agreement + 2 conclusion
    + 2 working assumption）；其中 11 张的**首个**单元格就是标记，即下面断言的 8/2/1。"""
    doc = parse_docx(pathlib.Path("tests/fixtures/RAN1_126/minutes.docx"))
    tables = [b for b in doc.blocks if b.kind == "table"]
    assert len(tables) == 82
    lead = [t.cell_paras[0] for t in tables if t.cell_paras]
    assert sum(1 for x in lead if x.startswith("Agreement")) == 8
    assert sum(1 for x in lead if x.startswith("Conclusion")) == 2
    assert sum(1 for x in lead if x.lower().startswith("working assumption")) == 1
    # 注意 tables 只含 body 的**直接子**表格。嵌套子表不单独成块，其段落进
    # nested_paras 而非 cell_paras —— 两者语义不同：自有单元格里的标记是一条决议
    # 本身，而嵌套子表出现在 CR 封面表里，它的 "Agreement:" 只是这份 CR 的标签。
    # 实测全文只有 1 张表有子表，正是那张 CR 封面表。
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/Scripts/python.exe -m pytest tests/test_parse_docx.py -v`
Expected: FAIL，`No module named 'ngr.parse.docx'`

- [ ] **Step 3: 写 `ngr/parse/docx.py`**

```python
from __future__ import annotations
import io, re, zipfile
import xml.etree.ElementTree as ET
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
    cell_paras: list[str] = field(default_factory=list)
    """仅 table 块有值：本表**自有**单元格里各段落的纯文本，按出现顺序。

    实测 RAN1#126 有 12 张表格的自有单元格里带标记，共 15 条
    （11 Agreement、2 Conclusion、2 Working assumption）—— 它们是"用表格画的框"，
    框里装着一条决议。若只把表格转成 markdown 整块，这些标记对 extract_events
    不可见，约 4% 的 agreement 会被静默丢弃。
    标记识别仍留在 parse/events.py（不在本层做）。"""
    nested_paras: list[str] = field(default_factory=list)
    """仅 table 块有值：嵌套在单元格内的**子表格**里的段落，按文档顺序。

    与 cell_paras 分开，是因为两者语义不同：自有单元格里的标记是一条决议本身，
    而子表格出现在 CR 封面表里，它的 "Agreement:" 只是这份 CR 的标签。
    混为一谈会把一份 CR 拆成两条互相借用正文的事件，且总数仍然对得上 ——
    这类错误测试发现不了。实测只有 1 张表有子表，正是那张 CR 封面表。"""

@dataclass
class Document:
    blocks: list[Block] = field(default_factory=list)
    headings: list[Heading] = field(default_factory=list)

    @property
    def paragraphs(self) -> list[str]:
        return [b.text for b in self.blocks if b.kind == "para"]

# w:tab / w:br / w:cr 在 Word 里是独立元素，不是 w:t 里的字符。只收集 w:t 会把两侧
# 文本焊死：实测 RAN1#126 有 3795 处 tab、48 处 br 落在两段无空白的文本之间，
# "Opening of the meeting" + "5" 被拼成 "...meeting5"。这类错误不报错也不返回空，
# 只是产出与原文本意不符的段落 —— 必须在这一处补分隔符，不能留给下游猜词边界。
_SEP = {W + "tab": "\t", W + "br": "\n", W + "cr": "\n"}

# Word 对同一个图形给出 mc:Choice 与 mc:Fallback 两份**等价**表示。两份都收会让
# 文本原样重复一遍 —— 实测 Annex A-2 的日程表图示被拼成
# "RAN1 Brk 2RAN1 Brk 2RAN1 Brk 1RAN1 Brk 1RAN1 MainRAN1 Main..."。只取其一。
MC = "{http://schemas.openxmlformats.org/markup-compatibility/2006}"

def _text_of(el) -> str:
    """段落纯文本。按文档顺序收集 w:t，并为结构性断点补分隔符。

    分隔符不是即时写入的，而是先挂起、等到下一段真实文本出现时才落下 ——
    这样嵌套段落的前后断点不会在段首/段尾留下多余空行，也不会连出 "\n\n"。
    """
    out: list[str] = []
    pending = False

    def emit(s: str) -> None:
        nonlocal pending
        if pending and out:
            out.append("\n")
        pending = False
        out.append(s)

    def walk(node) -> None:
        nonlocal pending
        for child in node:
            tag = child.tag
            if tag == W + "pPr":
                continue            # 段落属性里的 <w:tab> 是制表位定义，不是制表符
            if tag == MC + "AlternateContent":
                pick = child.find(MC + "Choice")
                if pick is None:
                    pick = child.find(MC + "Fallback")
                # 显式 is None：空 Element 的布尔值是 False，`a or b` 会选错
                if pick is not None:
                    walk(pick)
                continue
            if tag == W + "t":
                emit(child.text or "")
            elif tag in _SEP:
                emit(_SEP[tag])
            else:
                # 文本框（w:txbxContent）等结构里嵌套着独立的 w:p，它们各自成段。
                # 前后都要断开，否则会和外层文本首尾相连焊成一串 ——
                # 与 w:br 那个坑同源（实测 "RAN1 MainAnnex A-2:"）。
                nested_para = tag == W + "p"
                if nested_para:
                    pending = True
                walk(child)
                if nested_para:
                    pending = True

    walk(el)
    return "".join(out)

def _cell_text(tc) -> str:
    # 单元格文本要塞进 markdown 表格的一行，制表/换行必须压成空格，
    # 否则一个单元格就能把整张表的行结构撑断。
    parts = [re.sub(r"\s+", " ", _text_of(p)).strip() for p in tc.findall(W + "p")]
    return " ".join(x for x in parts if x).replace("|", r"\|")

def _cell_paragraphs(tbl) -> list[str]:
    """表格内所有单元格段落的纯文本，按文档顺序，跳过空段。

    这里**有意不做空白压平**，与 _cell_text 不同：_cell_text 的产物要塞进 markdown
    表格的一行，残留换行会撑断整张表；而 cell_paras 是给下游做标记识别和正文拼接的，
    text_en 要逐字保留（全局约束），在这里压平就等于改写原文。
    需要单行呈现的场合（如喂 LLM 的逐行 blob）由使用方自己压平。

    只取本表自有单元格（tr/tc 的直接子段落），**不递归进嵌套子表** ——
    子表段落由 _nested_paragraphs 单独取出，理由见 Block.nested_paras。"""
    out: list[str] = []
    for tr in tbl.findall(W + "tr"):
        for tc in tr.findall(W + "tc"):
            out += [t for t in (_text_of(p).strip() for p in tc.findall(W + "p")) if t]
    return out

def _nested_paragraphs(tbl) -> list[str]:
    """嵌套在单元格内的子表格里的段落纯文本，按文档顺序。

    _table_to_markdown 只走 findall（非递归），子表内容在 block.text 里完全不可见；
    这里若也不取，那些文本会整体静默消失。用"全部段落减去自有段落"而不是
    findall('.//tbl') 逐个展开，是为了避免多层嵌套时同一段落被重复计入。"""
    own = {p for tr in tbl.findall(W + "tr")
             for tc in tr.findall(W + "tc")
             for p in tc.findall(W + "p")}
    return [t for t in (_text_of(p).strip() for p in tbl.iter(W + "p")
                        if p not in own) if t]

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
    data = source.read_bytes() if isinstance(source, Path) else source
    with zipfile.ZipFile(io.BytesIO(data)) as z:
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
                doc.blocks.append(Block("table", md, None, len(doc.blocks),
                                        cell_paras=_cell_paragraphs(el),
                                        nested_paras=_nested_paragraphs(el)))
    return doc
```

> `Heading.para_index` 是**段落序号**（只数 `para` 块），而 `Block.index` 是**块序号**（段落与表格统一编号）。两者不同，不要混用：对齐用前者，块边界用后者。

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/Scripts/python.exe -m pytest tests/test_parse_docx.py -v`
Expected: 14 passed

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
import logging, pathlib
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

def test_marker_inside_table_cell_is_extracted():
    """实测 RAN1#126 有 15 条标记装在"用表格画的框"里（11 agreement + 2 conclusion + 2 working assumption）。
    只看表格的 markdown 整块会让它们不可见，约 4% 的 agreement 被静默丢弃。"""
    d = Document()
    d.blocks.append(Block("table", "| Agreement: |\n| --- |\n| Adopt X |", None, 0,
                          cell_paras=["Agreement:", "Adopt X"]))
    evs = extract_events(d)
    assert [e.kind for e in evs] == ["agreement"]
    assert evs[0].text_en == "Adopt X"

def test_data_table_without_marker_stays_a_continuation():
    """没有标记的真数据表仍整块并入上一条事件 —— 单元格扫描不得改变这个行为。"""
    d = Document()
    d.blocks.append(Block("para", "Agreement:", None, 0))
    d.blocks.append(Block("para", "see table", None, 1))
    d.blocks.append(Block("table", "| a | b |\n| --- | --- |\n| 1 | 2 |", None, 2,
                          cell_paras=["a", "b", "1", "2"]))
    evs = extract_events(d)
    assert len(evs) == 1 and "| a | b |" in evs[0].text_en

def test_marker_with_parenthetical_qualifier():
    """"Conclusion (RAN#112)" 是引用上级会议结论的真实写法，必须认。"""
    d = doc_of(("para", "Conclusion (RAN#112)", None), ("para", "X", None))
    assert [e.kind for e in extract_events(d)] == ["conclusion"]

def test_table_column_header_is_not_a_marker():
    """Annex E 的表头列名 "Conclusion/Decision" 不是结论。全文仅此一处，
    若为了它放宽正则去认 "/词"，就会凭空多出一条假事件。"""
    d = doc_of(("para", "Conclusion/Decision", None), ("para", "Y", None))
    assert extract_events(d) == []

def test_nested_table_marker_is_content_not_a_new_event():
    """CR 封面表里嵌套的子表，其 "Agreement:" 是这份 CR 的标签，不是一条新决议。
    让它开新事件会把一份 CR 拆成两条互相借用正文的 agreement，而事件总数照样对得上 ——
    这类缺陷计数类测试发现不了，所以要专门守住。"""
    d = Document()
    d.blocks.append(Block("para", "Agreement:", None, 0))
    d.blocks.append(Block("para", "The following TP is endorsed.", None, 1))
    # 真数据表的 markdown 本就含自有单元格的文字，所以这里照实构造
    d.blocks.append(Block("table", "| Reason for change | priority rule unclear |", None, 2,
                          cell_paras=["Reason for change", "priority rule unclear"],
                          nested_paras=["Agreement:", "TP body text"]))
    evs = extract_events(d)
    assert len(evs) == 1
    assert "priority rule unclear" in evs[0].text_en
    assert "TP body text" in evs[0].text_en

def test_empty_text_event_is_dropped_with_a_warning(caplog):
    """正文为空的事件（标记后紧跟 heading / 另一个标记 / 文档结尾）丢弃是对的，
    但必须留痕 —— 本项目里静默丢数据比崩溃更严重。"""
    d = Document()
    d.blocks.append(Block("para", "Agreement:", None, 0))
    with caplog.at_level(logging.WARNING):
        assert extract_events(d) == []
    assert "正文为空" in caplog.text

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
    assert kinds.count("agreement") == 319
    assert kinds.count("conclusion") == 28
    assert kinds.count("working_assumption") == 13
    # 319/28/13 是实测值，含藏在表格自有单元格里的 15 条标记
    # （11 agreement + 2 conclusion + 2 working assumption）。
    #
    # agreement 曾一度是 320：当时 CR 封面表里**嵌套子表**的 "Agreement:" 会另开一条事件，
    # 把一份 CR 拆成两条互相借用正文的 agreement。那个 320 是缺陷造成的虚高，不是基准。
    # 现在嵌套子表的段落只当内容，那份 CR 合回一条 —— 详见 extract_events 表格分支第 3 点。
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
import logging, re
from ngr.models import KIND_PREFIX, RawEvent
from ngr.parse.docx import Document

MARKERS = {
    "agreement": r"agreements?",
    "conclusion": r"conclusions?",
    "working_assumption": r"working\s+assumptions?",
    "observation": r"observations?",
    "proposal": r"proposals?",
}
# MARKERS 与 KIND_PREFIX 必须同步：前者决定能解析出哪些 kind，后者决定 Event.id 的前缀。
# 任一方新增而另一方漏改，会在 Event.id 上炸成运行期 KeyError —— 宁可在导入期就失败。
assert set(MARKERS) == set(KIND_PREFIX), (
    f"MARKERS 与 KIND_PREFIX 不同步: {set(MARKERS) ^ set(KIND_PREFIX)}")
# 标记必须在段首，后跟冒号/句点/行末 —— 避免 "The agreement was reached" 被误判
MARKER_RE = re.compile(
    r"^\s*(?:" + "|".join(f"(?P<{k}>{v})" for k, v in MARKERS.items()) + r")"
    r"\s*(?:\d+[\.\):]?)?"
    # 括号限定：实测 RAN1#126 里有 "Conclusion (RAN#112)"、"Agreement (RAN1#124bis)"
    # 这样引用上级会议结论的写法，不认它们会静默漏掉 3 条真标记。
    # 不要再加 "/\w+" 去认 "Conclusion/Decision" —— 全文唯一一处是 Annex E 表格的列标题
    # （"Tdoc Number | Title | Source | Conclusion/Decision"），认了就多一条假阳性。
    r"\s*(?:\([^)]*\))?"
    r"\s*(?::|\.\s|$)", re.IGNORECASE)

HEADING_STYLE_RE = re.compile(r"(?i)^heading\s*(\d+)$")

log = logging.getLogger(__name__)

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

        # 表格有三种角色：
        #   1) 真的数据表 —— 整块 markdown 并入上一条事件。
        #   2) "用表格画的框" —— 自有单元格里就是标记，框本身装着一条决议。实测
        #      RAN1#126 有 12 张这样的表、共 15 条标记（11 agreement + 2 conclusion
        #      + 2 working assumption）。只看 block.text 就看不见它们，约 4% 的
        #      agreement 会被静默丢弃：管线不报错，产出物上也看不出任何异常。
        #   3) CR 封面表里**嵌套的子表** —— 它的 "Agreement:" 是这份 CR 的标签，
        #      不是一条新决议。实测只有 1 处；若让它开新事件，一份 CR 会被拆成两条
        #      互相借用正文的 agreement，而事件总数照样对得上，计数类测试发现不了。
        if block.kind == "table":
            if any(_marker_kind(c) for c in block.cell_paras):
                for cell in block.cell_paras:
                    k = _marker_kind(cell)
                    if k:
                        body = MARKER_RE.sub("", cell, count=1).strip()
                        # 同一张表里的多条事件共用 block.index：它们本就在同一个块内
                        current = RawEvent(kind=k, text_en=body, para_index=block.index,
                                           heading_path=[t for _, t in stack])
                        events.append(current)
                    elif current is not None:
                        current.text_en = (current.text_en + "\n" + cell).strip()
            elif current is not None:
                # 真数据表：整块 markdown 并入上一条事件，保持原行为
                current.text_en = (current.text_en + "\n" + block.text).strip()

            # 嵌套子表的段落一律当内容：它们在 block.text 里不可见，不带出来就整体
            # 静默消失；但也不许开新事件（见上面第 3 点）。
            for para in block.nested_paras:
                if current is not None:
                    current.text_en = (current.text_en + "\n" + para).strip()
            continue

        kind = _marker_kind(block.text)
        if kind:
            body = MARKER_RE.sub("", block.text, count=1).strip()
            current = RawEvent(kind=kind, text_en=body, para_index=block.index,
                               heading_path=[t for _, t in stack])
            events.append(current)
        elif current is not None:
            current.text_en = (current.text_en + "\n" + block.text).strip()

    kept = [e for e in events if e.text_en.strip()]
    if len(kept) != len(events):
        # 标记后紧跟另一个标记 / heading / 文档结尾时正文为空。丢弃本身是对的
        # （没有内容可用），但必须留痕 —— 本项目里静默丢数据比崩溃更严重。
        # 实测 RAN1#126 命中 0 条，这是为将来的纪要留的探针。
        dropped = [e for e in events if not e.text_en.strip()]
        log.warning("丢弃 %d 条正文为空的事件: %s", len(dropped),
                    ", ".join(f"{e.kind}@块{e.para_index}" for e in dropped[:5]))
    return kept
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
texts = [x for b in doc.blocks for x in ([b.text] if b.kind == 'para' else b.cell_paras)]
miss = [x for x in texts if x.startswith('Agreement') and not _marker_kind(x)]
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
  - `Alignment` 数据类：`.by_heading: dict[int, AgendaItem]`（键为 `Heading.para_index`）、`.unaligned: list[Heading]`、
    `.skipped: list[Heading]`（结构性附录标题，不参与对齐也不计入未对齐率）、`.unmatched_ratio: float`
  - `align(agenda: list[AgendaItem], headings: list[Heading]) -> Alignment`
  - `normalize(text: str) -> str`

- [ ] **Step 1: 写失败的测试**

```python
# tests/test_parse_align.py
import logging

from ngr.models import AgendaItem, Heading
from ngr.parse.align import align, normalize


def A(item, title):
    return AgendaItem(item=item, title=title)


def H(level, text, i=0):
    return Heading(level=level, text=text, para_index=i)


def test_normalize_strips_case_punct_and_space():
    assert normalize("  Waveform for 6GR  air-interface! ") == normalize(
        "waveform for 6gr airinterface"
    )


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
    ag = [A("10.2", "Waveform")]  # depth 2
    al = align(ag, [H(4, "Waveform", 1)])  # Heading4
    assert 1 not in al.by_heading


def test_depth_match_allows_one_level_offset():
    """纪要常把 Heading1 用在 depth-1 议程项上，允许 ±1 的偏移。"""
    ag = [A("10.2", "Waveform")]
    al = align(ag, [H(3, "Waveform", 1)])
    assert al.by_heading[1].item == "10.2"


def test_same_title_headings_share_one_agenda_item():
    """同名 heading 是同一个议程项的重复出现（分组标题 + 同名子标题），两处都要对上。
    实测 RAN1#126 的 "GNSS resilient NR-NTN operation" 就是 L2/L3 各一次。"""
    ag = [A("10.2", "Waveform")]
    al = align(ag, [H(2, "Waveform", 1), H(3, "Waveform", 9)])
    assert len(al.by_heading) == 2
    assert {v.item for v in al.by_heading.values()} == {"10.2"}
    assert al.unaligned == []


def test_different_titles_cannot_claim_same_item():
    """标题不同的两个小节不得抢同一个议程项 —— used 守的是这个。
    "Waveforms" 与 "Waveform" 的 difflib 相似度 0.94，会越过模糊阈值。"""
    ag = [A("10.2", "Waveform")]
    al = align(ag, [H(2, "Waveform", 1), H(2, "Waveforms", 9)])
    assert len(al.by_heading) == 1
    assert [h.text for h in al.unaligned] == ["Waveforms"]


def test_unmatched_ratio_computed():
    ag = [A("1", "Opening")]
    al = align(ag, [H(1, "Opening", 0), H(1, "Mystery", 1)])
    assert al.unmatched_ratio == 0.5


def test_empty_agenda_marks_all_unaligned():
    al = align([], [H(1, "X", 0)])
    assert al.unmatched_ratio == 1.0 and al.by_heading == {}


def test_no_eligible_heading_reads_as_fully_unmatched():
    """分母为 0 时必须是 1.0 而不是 0.0。

    heading 抽取彻底失效、或纪要里只剩 Annex 结构性标题时，"一条都没对上"
    绝不能被报成"全对上了" —— Task 11 用 `ratio > 0.20` 当质量门禁，
    返回 0.0 会让这类纪要拿到比正常值（12.2%）还好看的分数被放行。
    也不能用 nan 当哨兵：`nan > 0.20` 恒为 False，门禁照样放行。"""
    ag = [A("10.2", "Waveform")]
    assert align(ag, []).unmatched_ratio == 1.0
    only_annex = align(ag, [H(1, "Annex A-1:	List of Tdocs", 0)])
    assert len(only_annex.skipped) == 1
    assert only_annex.by_heading == {} and only_annex.unaligned == []
    assert only_annex.unmatched_ratio == 1.0
    assert align([], []).unmatched_ratio == 1.0

def test_duplicate_normalised_agenda_titles_warn(caplog):
    """两个议程项归一化后重名时会"先到先得"，后一个永远拿不到 heading。
    实测 RAN1#126 的 66 条议程项无冲突，所以不改行为，只出声。"""
    ag = [A("10.2", "Waveform - Air Interface"), A("10.3", "Waveform Air Interface")]
    with caplog.at_level(logging.WARNING):
        align(ag, [H(2, "Waveform Air Interface", 0)])
    assert "归一化后重名" in caplog.text

def test_real_fixture_alignment():
    import pathlib

    from ngr.parse.agenda import parse_agenda
    from ngr.parse.docx import parse_docx

    ag = parse_agenda(pathlib.Path("tests/fixtures/RAN1_126/agenda.csv").read_bytes())
    doc = parse_docx(pathlib.Path("tests/fixtures/RAN1_126/minutes.docx"))
    al = align(ag, doc.headings)
    assert al.unmatched_ratio < 0.20, f"未对齐率过高: {al.unmatched_ratio:.0%}"
    # 9 条 Annex 标题被跳过而非判为未对齐；若把它们算进去，未对齐率是 23%，
    # 探针常年报警等于没有探针。
    assert len(al.skipped) == 9
    assert all(h.text.lower().startswith("annex") for h in al.skipped)
    items = {v.item for v in al.by_heading.values()}
    assert "10" in items and "10.2" in items
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/Scripts/python.exe -m pytest tests/test_parse_align.py -v`
Expected: FAIL，`No module named 'ngr.parse.align'`

- [ ] **Step 3: 写 `ngr/parse/align.py`**

```python
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
        """未对上的比例，分母只含**参与对齐**的 heading（不含 skipped 的 Annex）。

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
    for item in agenda:
        exact.setdefault(normalize(item.title), []).append(item)
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
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/Scripts/python.exe -m pytest tests/test_parse_align.py -v`
Expected: 13 passed

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
    # 实测值，按 kind 拆开写以便出错时一眼看出是哪类变了。
    # 注意 observation 也在 events 里 —— 旧公式 320+29+13 漏了它，
    # 而 320/29 本身又是缺陷期的虚高值（详见 Task 9 的 test_real_fixture_counts 注释）。
    assert len(p.events) == 319 + 28 + 13 + 9
    assert p.unmatched_ratio < 0.20
    assert p.minutes_version == 10

def test_events_carry_agenda_item_when_aligned(tmp_path):
    shutil.copytree(FIX126, tmp_path / "raw")
    p = parse_meeting(tmp_path / "raw", MTG, agenda_required=True)
    # agenda_item 这个键**总是存在**，未对齐时值为 None ——
    # 所以 .get(k, "") 返回的是 None 而不是 ""，直接 .startswith 会抛 AttributeError。
    sixg = [e for e in p.events if (e.get("agenda_item") or "").startswith("10")]
    assert sixg, "6GR 议程项下应有事件"
    assert all("heading_path" in e and "text_en" in e for e in p.events)

def test_events_keep_heading_path_when_agenda_absent(tmp_path):
    """5G-A 老会议没有 agenda.csv：事件照常产出，只是没有 agenda_item。"""
    raw = tmp_path / "raw"; raw.mkdir()
    shutil.copy(FIX126 / "minutes.docx", raw / "minutes.docx")
    p = parse_meeting(raw, MTG, agenda_required=False)
    assert len(p.events) == 319 + 28 + 13 + 9   # 对齐与否不改变事件数
    assert all(e["agenda_item"] is None for e in p.events)
    assert any(e["heading_path"] for e in p.events)

def test_missing_agenda_warns_but_does_not_raise(tmp_path):
    """实测 agenda_csv_since 只表示最早出现（RAN2 #131 有缺口），
    缺 agenda.csv 是正常现象，不得以退出码 2 中止整条管线。"""
    raw = tmp_path / "raw"; raw.mkdir()
    shutil.copy(FIX126 / "minutes.docx", raw / "minutes.docx")
    p = parse_meeting(raw, MTG, agenda_required=True)
    assert p.events and any("agenda.csv" in w for w in p.warnings)

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

def test_no_eligible_heading_also_raises(tmp_path, monkeypatch):
    """**一条都没参与对齐**时门禁也必须开火。

    这条与下面那条走的是 unmatched_ratio 的**两个不同分支**：这里 by_heading 与
    unaligned 都空（total==0，比如 heading 全是 Annex 结构性标题），
    下面那条是 unaligned 撑满（total==1）。total==0 曾经返回 0.0 被门禁放行 ——
    比正常值 12.2% 还好看，是本项目遇到过最隐蔽的一次静默失败。
    """
    shutil.copytree(FIX126, tmp_path / "raw")
    from ngr.parse import runner
    from ngr.parse.align import Alignment
    from ngr.models import Heading
    degenerate = Alignment(by_heading={}, unaligned=[],
                           skipped=[Heading(1, "Annex A-1: List of Tdocs", 0)])
    assert degenerate.unmatched_ratio == 1.0
    monkeypatch.setattr(runner, "align", lambda a, h: degenerate)
    with pytest.raises(ParseError, match="未对齐"):
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
    warnings: list[str] = field(default_factory=list)

def parse_meeting(raw_dir: Path, meeting: Meeting, *,
                  agenda_required: bool) -> ParsedMeeting:
    raw_dir = Path(raw_dir)
    minutes = raw_dir / "minutes.docx"
    if not minutes.exists():
        raise ParseError(f"{meeting.label}: 缺少 minutes.docx，无法解析")

    agenda_path = raw_dir / "agenda.csv"
    warnings: list[str] = []
    if agenda_required and not agenda_path.exists():
        # 不硬失败：实测 agenda_csv_since 只表示"最早出现"，不表示此后每次都有
        # （RAN2 #131 无 agenda.csv 而 #130/#132 都有）。缺口是正常现象，
        # 降级到 title_re 锚定即可，但必须让人看见。
        warnings.append(
            f"{meeting.label}: 预期有 agenda.csv 但该会议没有，已降级为仅按标题锚定 —— "
            "该次会议的议程号归属会缺失")

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
        wg=meeting.wg, meeting=meeting.number, events=events, warnings=warnings,
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
        "warnings": parsed.warnings,
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
Expected: 10 passed

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
import logging
import json
from ngr.models import Feature, LineageSegment
from ngr.mapping.runner import _agenda_key, map_meeting, merge_events, write_state
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
    merged, stats = merge_events([], new, today="2026-09-17", scope={("RAN1", 126)})
    assert stats.added == 1 and merged[0]["first_seen"] == "2026-09-17"
    assert stats.added_ids == [new[0].id]

def test_merge_added_ids_excludes_unchanged():
    """未变更的事件不能混进'本次新增'。

    注意 added_ids 是**合并后 state 侧**的 id，不要拿它去 join incoming 的 Event.id ——
    要每特性新增数请用 added_by_feature，见 test_added_ids_are_state_side_not_incoming。"""
    new = map_meeting(parsed([ev()]), FEATS)
    existing = [{**new[0].__dict__, "id": new[0].id, "first_seen": "2026-01-01"}]
    _, stats = merge_events(existing, new, today="2026-09-17", scope={("RAN1", 126)})
    assert stats.added_ids == [] and stats.unchanged == 1

def test_merge_preserves_first_seen_and_llm_fields():
    new = map_meeting(parsed([ev()]), FEATS)
    existing = [{**new[0].__dict__, "id": new[0].id, "first_seen": "2026-01-01",
                 "summary_zh": "旧摘要", "llm_status": "ok"}]
    merged, stats = merge_events(existing, new, today="2026-09-17",
                                 scope={("RAN1", 126)})
    assert stats.unchanged == 1
    assert merged[0]["first_seen"] == "2026-01-01"
    assert merged[0]["summary_zh"] == "旧摘要"

def test_merge_detects_text_change_and_invalidates_summary():
    """纪要 v010→v100 措辞微调：同一条 id，但摘要要重算。"""
    new = map_meeting(parsed([ev(text="NEW TEXT")]), FEATS)
    existing = [{**new[0].__dict__, "id": new[0].id, "text_en": "OLD TEXT",
                 "content_hash": "sha256:old", "first_seen": "2026-01-01",
                 "summary_zh": "旧摘要", "llm_status": "ok"}]
    merged, stats = merge_events(existing, new, today="2026-09-17",
                                 scope={("RAN1", 126)})
    assert stats.changed == 1
    assert merged[0]["text_en"] == "NEW TEXT"
    assert merged[0]["summary_zh"] is None and merged[0]["llm_status"] == "pending"
    assert merged[0]["first_seen"] == "2026-01-01"

def test_merge_keeps_events_from_other_meetings():
    new = map_meeting(parsed([ev()]), FEATS)
    existing = [{"id": "RAN1-120-9.1-a001", "wg": "RAN1", "meeting": 120,
                 "text_en": "x", "first_seen": "2026-01-01"}]
    merged, _ = merge_events(existing, new, today="2026-09-17", scope={("RAN1", 126)})
    assert len(merged) == 2

def test_write_state_is_sorted_and_deterministic(tmp_path):
    new = map_meeting(parsed([ev(), ev()]), FEATS)
    merged, _ = merge_events([], new, today="2026-09-17", scope={("RAN1", 126)})
    a = write_state(merged, tmp_path / "a.json").read_bytes()
    b = write_state(list(reversed(merged)), tmp_path / "b.json").read_bytes()
    assert a == b, "事件顺序不同也必须产出相同字节 —— 否则 git diff 全是噪声"

# —— 血统报告 ——
def test_lineage_report_lists_hits_and_misses():
    txt = lineage_report(FEATS, [parsed([ev()])])
    assert "waveform" in txt and "6G" in txt
    assert "isac" in txt
    assert "0" in txt          # isac 的两段在本次会议都没命中


def test_missing_event_is_reported_not_deleted(caplog):
    """纪要出新版本、删掉一条 agreement 时，末位 id 从此无人认领。

    事件 id 是位置式的，被删那条对应的 id **永久留在 state 里**，看板上会一直显示
    一条实际已不存在的 agreement。只报告不删除：若某次 parse 回归让事件暂时缺失，
    删除就是永久数据丢失。缺失是信号，不是指令。
    """
    feats = [Feature(slug="waveform", name_zh="波形",
                     lineage=[seg("6G", "full", agenda=["RAN1:10.2"],
                                  meetings={"RAN1": (124, None)})])]
    def parsed(texts):
        return {"wg": "RAN1", "meeting": 126, "minutes_version": 10,
                "events": [{"kind": "agreement", "text_en": x, "para_index": i,
                            "heading_path": ["Waveform"], "agenda_item": "10.2",
                            "agenda_title": "Waveform"} for i, x in enumerate(texts)]}

    state, _ = merge_events([], map_meeting(parsed(["AAA", "BBB", "CCC"]), feats),
                            "2026-09-18", scope={("RAN1", 126)})
    with caplog.at_level(logging.WARNING):
        merged, stats = merge_events(state, map_meeting(parsed(["AAA", "BBB"]), feats),
                                     "2026-09-19", scope={("RAN1", 126)})
    assert stats.stale_ids == ["RAN1-126-10.2-a003"]
    assert len(merged) == 3, "缺失的事件必须保留在 state 里，不许删"
    assert "不再出现" in caplog.text


def test_other_meetings_are_not_reported_as_stale(caplog):
    """incoming 只覆盖本次跑的会议，而 existing 是全量 state。
    比较不限定 (wg, meeting) 的话，所有历史会议的事件都会被当成"本次缺失"。"""
    feats = [Feature(slug="waveform", name_zh="波形",
                     lineage=[seg("6G", "full", agenda=["RAN1:10.2"],
                                  meetings={"RAN1": (124, None)})])]
    def parsed(meeting, texts):
        return {"wg": "RAN1", "meeting": meeting, "minutes_version": 10,
                "events": [{"kind": "agreement", "text_en": x, "para_index": i,
                            "heading_path": ["Waveform"], "agenda_item": "10.2",
                            "agenda_title": "Waveform"} for i, x in enumerate(texts)]}

    state, _ = merge_events([], map_meeting(parsed(126, ["AAA", "BBB"]), feats),
                            "2026-09-18", scope={("RAN1", 126)})
    with caplog.at_level(logging.WARNING):
        merged, stats = merge_events(state, map_meeting(parsed(127, ["XXX"]), feats),
                                     "2026-09-19", scope={("RAN1", 127)})
    assert stats.stale_ids == []
    assert len(merged) == 3
    assert caplog.text == ""


def test_legacy_keys_do_not_collide():
    """不同议题拿到同一个回退 key，后果是历史张冠李戴：seq 按遍历顺序分配，
    两次纪要修订间先后一换，同一个 id 就指向另一个议题，merge 判成普通内容变更，
    把 A 的历史安到 B 头上 —— 既不报错也不进 stale_ids，彻底静默。

    两类撞车都要守住：标点变体，以及**末节同名但上级路径不同**。
    后者更常见 —— "Overview"/"General"/"Way forward" 在 3GPP 纪要里跨 Release 反复出现。"""
    for a, b in [(["ISAC channel model"], ["ISAC channel-model"]),
                 (["CSI enhancement: further study"], ["CSI enhancement further study"]),
                 (["Rel-17 NR", "Overview"], ["Rel-18 NR", "Overview"]),
                 (["Rel-19 NR", "Way forward"], ["Rel-20 6GR", "Way forward"]),
                 # 标题原文含字面 "/" 时，用 "/".join 拼接会让不同层级结构撞出同一个串。
                 # 3GPP 标题里 "UL/DL"、"Tx/Rx"、"PDCCH/PDSCH" 很常见，所以哈希输入
                 # 必须是长度前缀编码那种可证单射的写法，而不是赌某个分隔符不出现在内容里。
                 (["UL/DL switching", "Way forward"], ["UL", "DL switching", "Way forward"]),
                 (["a/b", "c"], ["a", "b", "c"])]:
        assert _agenda_key(None, a) != _agenda_key(None, b), f"{a} 与 {b} 撞 key"
    # 同一段路径必须每次都得到同一个 key，否则 id 不稳定
    assert _agenda_key(None, ["Rel-17 NR", "Overview"]) == _agenda_key(None, ["Rel-17 NR", "Overview"])


def test_whole_meeting_wipeout_is_reported_when_scope_given():
    """整场会议归集归零（features.yaml 改坏、正则回归）是最该报警的情形。

    scope 若从 incoming 反推，这场会议根本不在 scope 里，它的全部历史一条都不会被
    比较，stale_ids 恒为空 —— 局部缺失报警、全部缺失反而不报警，探针在最该响的时候哑火。
    """
    feats = [Feature(slug="waveform", name_zh="波形",
                     lineage=[seg("6G", "full", agenda=["RAN1:10.2"],
                                  meetings={"RAN1": (124, None)})])]
    def parsed(item):
        return {"wg": "RAN1", "meeting": 126, "minutes_version": 10,
                "events": [{"kind": "agreement", "text_en": x, "para_index": i,
                            "heading_path": ["Waveform"], "agenda_item": item,
                            "agenda_title": "Waveform"} for i, x in enumerate("AB")]}

    state, _ = merge_events([], map_meeting(parsed("10.2"), feats), "2026-09-18",
                            scope={("RAN1", 126)})
    wiped = map_meeting(parsed("99.9"), feats)          # 一条都归集不上
    assert wiped == []

    merged, stats = merge_events(state, wiped, "2026-09-19", scope={("RAN1", 126)})
    assert len(stats.stale_ids) == 2, "整场归零必须被报出来"
    assert len(merged) == 2, "报告归报告，历史一条都不许删"

    # 对照：若按"归集结果里有哪几场会议"来定 scope，归零的这场根本不在里面，
    # 什么都查不到 —— 这正是它不能当默认行为、也不该提供成现成函数的原因。
    inferred_scope = {(e.wg, e.meeting) for e in wiped}
    assert inferred_scope == set()
    _, inferred = merge_events(state, wiped, "2026-09-19", scope=inferred_scope)
    assert inferred.stale_ids == []


def test_scope_has_no_default():
    """scope 必须显式传。给它留默认值就等于允许静默反推 ——
    某场会议归零时它不在反推结果里，那场的历史一条都不会被检查。"""
    import inspect
    p = inspect.signature(merge_events).parameters["scope"]
    assert p.default is inspect.Parameter.empty, "scope 不得有默认值"
    assert p.kind is inspect.Parameter.KEYWORD_ONLY, "scope 应为关键字参数，避免位置传错"


def _wf_feats():
    return [Feature(slug="waveform", name_zh="波形",
                    lineage=[seg("6G", "full", agenda=["RAN1:10.2"],
                                 meetings={"RAN1": (124, None)})])]


def _wf_parsed(texts):
    return {"wg": "RAN1", "meeting": 126, "minutes_version": 10,
            "events": [{"kind": "agreement", "text_en": x, "para_index": i,
                        "heading_path": ["Waveform"], "agenda_item": "10.2",
                        "agenda_title": "Waveform"} for i, x in enumerate(texts)]}


def test_inserted_event_does_not_steal_history():
    """纪要改版在开头补录一条，其余逐字未变 —— 不得有任何一条被判成变更。

    id 是位置式的，只按 id 认亲的话后续 seq 整体位移，每条存活事件都会接管别人的
    first_seen，而 stale_ids 探不到（那些 id 没消失，只是被顶替了）。实测过一次
    "开头补录一条"就让 3 条未变事件被判 changed、摘要全部作废、一条 first_seen 被
    写成今天，全程无声。所以认亲必须先按正文哈希，并沿用历史的 seq。
    """
    feats = _wf_feats()
    scope = {("RAN1", 126)}
    base, _ = merge_events([], map_meeting(_wf_parsed(["AAA", "BBB", "CCC"]), feats),
                           "2026-09-01", scope=scope)
    merged, stats = merge_events(base, map_meeting(_wf_parsed(["NEW", "AAA", "BBB", "CCC"]), feats),
                                 "2026-09-19", scope=scope)
    assert (stats.added, stats.changed, stats.unchanged) == (1, 0, 3)
    assert stats.stale_ids == []
    by_text = {e["text_en"]: e for e in merged}
    # 原有三条的 id 与 first_seen 都不许动 —— id 稳定，LLM 缓存键和看板链接才稳定
    assert by_text["AAA"]["id"] == "RAN1-126-10.2-a001"
    assert all(by_text[x]["first_seen"] == "2026-09-01" for x in ("AAA", "BBB", "CCC"))
    assert by_text["NEW"]["first_seen"] == "2026-09-19"


def test_deleted_event_keeps_its_id_and_survivors_keep_theirs():
    """删掉中间一条：幸存者的 id 不动，被删那条保留在 state 里并报进 stale_ids。

    若幸存者跟着位移，被顶替的历史记录会被覆盖掉 —— "只报告不删除"这条承诺
    在删除场景下就根本守不住了。
    """
    feats = _wf_feats()
    scope = {("RAN1", 126)}
    base, _ = merge_events([], map_meeting(_wf_parsed(["AAA", "BBB", "CCC"]), feats),
                           "2026-09-01", scope=scope)
    merged, stats = merge_events(base, map_meeting(_wf_parsed(["AAA", "CCC"]), feats),
                                 "2026-09-19", scope=scope)
    assert stats.stale_ids == ["RAN1-126-10.2-a002"]
    assert len(merged) == 3, "被删那条必须仍在 state 里"
    ids = {e["text_en"]: e["id"] for e in merged}
    assert ids["AAA"] == "RAN1-126-10.2-a001"
    assert ids["CCC"] == "RAN1-126-10.2-a003", "幸存者不得因前面少了一条而位移"
    assert ids["BBB"] == "RAN1-126-10.2-a002"


def test_empty_and_blank_heading_paths_differ():
    """[] 与 [""] 必须得到不同的 key。给空路径加 `or "0:"` 兜底会让两者相撞，
    把长度前缀编码的单射性破坏掉。"""
    assert _agenda_key(None, []) != _agenda_key(None, [""])


def test_added_ids_are_state_side_not_incoming():
    """merge 会重新定序，incoming 上的 Event.id 只是 map 阶段的位置式草稿值。

    纪要改版在开头插一条，两侧 id 就整体错位（实测 0/4 对得上）。此时按
    `ev.id in added_ids` 去 join 会把"本次新增"记到另一条事件头上，还不报错 ——
    这正是 Task 20 计划稿里原本的写法。每特性新增数必须用 added_by_feature。
    """
    feats = _wf_feats()
    scope = {("RAN1", 126)}
    base, _ = merge_events([], map_meeting(_wf_parsed(["AAA", "BBB", "CCC"]), feats),
                           "2026-09-01", scope=scope)
    incoming = map_meeting(_wf_parsed(["NEW", "AAA", "BBB", "CCC"]), feats)
    merged, stats = merge_events(base, incoming, "2026-09-19", scope=scope)

    # 两侧 id 确实错位 —— 这就是不能 join 的原因
    state_pairs = {(e["id"], e["text_en"]) for e in merged}
    assert not any((ev.id, ev.text_en) in state_pairs for ev in incoming)

    # 按草稿 id join 会认错人
    joined = [ev.text_en for ev in incoming if ev.id in set(stats.added_ids)]
    assert joined == ["CCC"], "这条断言记录的是错误行为，用来说明为什么不能这么 join"

    # 权威结果：新增的是 NEW，且统计由 merge 算好
    assert [e["text_en"] for e in merged if e["id"] in set(stats.added_ids)] == ["NEW"]
    assert stats.added_by_feature == {("RAN1", 126): {"waveform": 1}}


def test_history_without_seq_field_is_not_overwritten():
    """老格式的 state 记录没有 seq 字段时，它的 id 仍然占位。

    若占用判据取自可缺失的 seq，新事件会落到一条活着的历史 id 上把它覆盖掉，
    而 stale_ids 还宣称那条"已保留" —— 占用必须按恒存在且权威的 id 判。
    """
    feats = _wf_feats()
    scope = {("RAN1", 126)}
    legacy = [{"id": "RAN1-126-10.2-a002", "wg": "RAN1", "meeting": 126,
               "agenda_item": "10.2", "kind": "agreement", "text_en": "BBB",
               "first_seen": "2026-01-01"}]          # 无 seq、无 content_hash
    merged, stats = merge_events(legacy, map_meeting(_wf_parsed(["NEW"]), feats),
                                 "2026-09-19", scope=scope)
    texts = {e["text_en"]: e["id"] for e in merged}
    assert "BBB" in texts, "老记录不得被覆盖"
    assert texts["BBB"] == "RAN1-126-10.2-a002"
    assert texts["NEW"] != "RAN1-126-10.2-a002", "新事件必须绕开已占用的 id"
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/Scripts/python.exe -m pytest tests/test_mapping_runner.py -v`
Expected: FAIL，`No module named 'ngr.mapping.runner'`

- [ ] **Step 3: 写 `ngr/mapping/runner.py`**

```python
from __future__ import annotations
import hashlib, json, logging, re
from collections import defaultdict
from dataclasses import dataclass, asdict, field, replace
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
    # 不要给空路径加兜底串：`or "0:"` 会让 [] 与 [""] 得到同一个编码，
    # 把上面论证的单射性破坏掉。空路径编码成空串即可，sha256("") 合法。
    full = "".join(f"{len(h)}:{h}" for h in heading_path)
    return f"{slug}-{hashlib.sha256(full.encode('utf-8')).hexdigest()[:8]}"

_SEQ_TAIL_RE = re.compile(r"(\d+)$")

def _seq_from_id(event_id: str) -> int | None:
    """从事件 id 尾部反解 seq。老格式的 state 记录可能没有 seq 字段，
    但 id 一定有 —— 认亲认到它时要沿用它自己的号，不能另给一个。"""
    m = _SEQ_TAIL_RE.search(event_id or "")
    return int(m.group(1)) if m else None

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
    """新增事件的 id，**取自合并后的 state（权威侧）**。

    ⚠️ 不要拿它去 join `incoming` 里的 `Event.id`。merge 会重新定序，
    `incoming` 上的 id 只是 map 阶段按位置生成的**草稿值** —— 纪要改版插入一条时，
    两侧的 id 会整体错位（实测开头插一条后 incoming 与 state **0/4 对得上**），
    join 的结果会安到另一条事件头上，还不报错。
    要"每特性新增数"请直接用 `added_by_feature`，不要自己 join。"""
    added_by_feature: dict[tuple[str, int], dict[str, int]] = field(default_factory=dict)
    """`(wg, meeting) -> {特性 slug: 本次新增条数}`，在 merge 内部按权威 id 算好。

    存在的理由就是取消调用方的 join：契约只写在 docstring 里约束不住人 ——
    本项目已经证明过两次（`scope_of()` 有警告仍被自己的测试绕过 6 次；
    这条 join 指引直接把 Task 20 的统计写错）。能算好就别让调用方算。"""
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
    """把本次归集的事件并入历史 state。

    **认亲分两轮：先按正文哈希，再按 id 兜底；认到之后沿用历史的 seq。**

    事件 id 是位置式的。只按 id 认亲，纪要一改版就会出错：中间插入或删掉一条，
    后续事件的 seq 整体位移，每一条存活事件都会**接管别人的 first_seen**，
    而 stale_ids 探不到 —— 那些 id 并没有消失，只是被顶替了。实测一次"开头补录一条"
    就让 3 条逐字未变的事件被判成 changed、摘要全部白白作废、其中一条的 first_seen
    被写成今天，全程无声。

    正文哈希配对解决认亲；**沿用旧 seq** 解决另一半：否则被顶替的历史记录会被覆盖掉，
    "只报告不删除"这条承诺在删除场景下根本守不住。沿用之后 id 在改版间保持稳定，
    LLM 缓存键与看板链接也跟着稳定。

    新事件取组内尚未占用的最小编号，**包括绕开那些已消失但仍保留的历史 id** ——
    缺失是信号不是指令，它们的号不能被回收。
    """
    by_id = {e["id"]: dict(e) for e in existing}
    stats = MergeStats()

    def gkey(wg, meeting, agenda_item, kind):
        return (wg, meeting, agenda_item, kind)

    pool: dict[tuple, list[dict]] = defaultdict(list)
    for e in existing:
        pool[gkey(e.get("wg"), e.get("meeting"),
                  e.get("agenda_item"), e.get("kind"))].append(e)

    taken: set[int] = set()          # 已被认走的历史记录（按对象身份去重）
    pairs: list[list] = []           # [事件, 认到的历史记录 | None]

    # 第一轮：正文哈希。纯插入/删除全靠这一轮认对。
    for ev in incoming:
        g = pool.get(gkey(ev.wg, ev.meeting, ev.agenda_item, ev.kind), ())
        hit = next((o for o in g if id(o) not in taken and o.get("content_hash")
                    and o["content_hash"] == ev.content_hash), None)
        if hit is not None:
            taken.add(id(hit))
        pairs.append([ev, hit])

    # 第二轮：id 兜底。正文同时被改写的那条走这里，行为与改动前一致。
    for pair in pairs:
        ev, hit = pair
        if hit is not None:
            continue
        g = pool.get(gkey(ev.wg, ev.meeting, ev.agenda_item, ev.kind), ())
        hit = next((o for o in g if id(o) not in taken and o["id"] == ev.id), None)
        if hit is not None:
            taken.add(id(hit))
            pair[1] = hit

    # 定序：认到历史的沿用旧 seq；其余取尚未占用的最小号。
    #
    # 占用判据取自 **by_id 的键（权威 id）**，不是历史记录里的 `seq` 字段 ——
    # `seq` 可能缺失或被手工改成字符串，那样它就不计入占用，新事件会落到一条
    # 活着的历史 id 上把它覆盖掉，而 stale_ids 还宣称那条"已保留"。
    # id 是恒存在且权威的，用它判占用不需要任何关于字段完整性的假设。
    taken_ids = set(by_id)

    resolved: list[tuple[Event, dict | None]] = []
    for ev, hit in pairs:
        old_seq = hit.get("seq") if hit is not None else None
        if not isinstance(old_seq, int) and hit is not None:
            old_seq = _seq_from_id(hit.get("id", ""))     # 老格式没有 seq 字段时从 id 反解
        if old_seq is not None:
            resolved.append((replace(ev, seq=old_seq), hit))
            continue
        n = 1
        while True:
            cand = replace(ev, seq=n)
            if cand.id not in taken_ids:
                break
            n += 1
        taken_ids.add(cand.id)
        resolved.append((cand, hit))

    for ev, old in resolved:
        new = asdict(ev)
        new["id"] = ev.id
        if old is None:
            new["first_seen"] = today
            by_id[ev.id] = new
            stats.added += 1
            stats.added_ids.append(ev.id)
            per = stats.added_by_feature.setdefault((ev.wg, ev.meeting), {})
            per[ev.feature] = per.get(ev.feature, 0) + 1
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
    for e in existing:
        if (e.get("wg"), e.get("meeting")) in scope and id(e) not in taken:
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

Expected: 解析出 369 条（319 agreement + 28 conclusion + 13 WA + 9 observation，Task 9/10 修复后的实测值），归集数 > 0；血统报告中 6G 段有命中。**若某个 6G 段命中为 0，先调 `features.yaml` 的锚点，不要改代码。**

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
  - `extract_all(events, cfg, *, cli_factory, cache, budget) -> ExtractStats`

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

def strip_fence(text: str) -> str:
    t = text.strip()
    if t.startswith("```"):
        t = re.sub(r"^```[a-zA-Z]*\s*", "", t)
        t = re.sub(r"\s*```$", "", t)
    return t.strip()

def parse_summary_response(text: str, expected_ids: list[str]) -> dict[str, dict]:
    try:
        data = json.loads(strip_fence(text))
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

### Task 18: 特性综述与 5G-A 源头归纳

`legacy_summary` 是 `depth: origin` 这个选择的唯一出口 —— 5G-A 段不做逐条摘要，全部价值都压在这一段归纳里。

**Files:**
- Create: `ngr/extract/digest.py`
- Test: `tests/test_extract_digest.py`

**Interfaces:**
- Consumes: `ClaudeCli`、`LlmCache`、`Budget`、`ngr.models.Feature`
- Produces:
  - `build_feature_prompt(feature, six_events, legacy_chunk=None) -> str`
  - `parse_feature_response(text) -> dict`（键 `stage` `summary` `open_issues`，抛 `SchemaError`）
  - `build_legacy_chunks(legacy_events, meetings_per_chunk=4) -> list[list[dict]]`
  - `digest_features(features, events, feat_state, cfg, *, cli_factory, cache, budget) -> dict`

- [ ] **Step 1: 写失败的测试**

```python
# tests/test_extract_digest.py
import json, pytest
from ngr.config import ExtractConfig
from ngr.models import Feature, LineageSegment
from ngr.extract.backend import CliResult
from ngr.extract.budget import Budget
from ngr.extract.cache import LlmCache
from ngr.extract.tasks import SchemaError
from ngr.extract.digest import (build_feature_prompt, parse_feature_response,
                                build_legacy_chunks, digest_features)

CFG = ExtractConfig(backend="cli", max_calls_per_run=20, batch_size=40,
                    model_bulk="sonnet", model_digest="opus")

def seg(era, depth):
    return LineageSegment(era=era, release="Rel-19" if era == "5G-A" else "Rel-20",
                          depth=depth, agenda=[], title_re="(?i)x",
                          meetings={"RAN1": (110, None)})

ISAC = Feature(slug="isac", name_zh="ISAC 通感一体",
               lineage=[seg("5G-A", "origin"), seg("6G", "full")])
WAVE = Feature(slug="waveform", name_zh="波形", lineage=[seg("6G", "full")])

def ev(i, era="6G", meeting=126, summary="摘要", text="Adopt X."):
    return {"id": f"RAN1-{meeting}-10.8-a{i:03d}", "wg": "RAN1", "meeting": meeting,
            "era": era, "feature": "isac", "kind": "agreement",
            "text_en": text, "summary_zh": summary,
            "depth": "full" if era == "6G" else "origin",
            "agenda_title": "ISAC"}

class FakeCli:
    def __init__(self, replies): self.replies, self.calls = list(replies), []
    def call(self, prompt):
        self.calls.append(prompt)
        return CliResult(text=self.replies.pop(0), usage={}, cost_usd=0.02)

FEAT_REPLY = json.dumps({"stage": "收敛中", "summary": "正在收敛。",
                         "open_issues": ["波形未定"]})

def test_feature_prompt_uses_summaries_for_6g():
    p = build_feature_prompt(ISAC, [ev(1, summary="采纳 X")], None)
    assert "采纳 X" in p and "ISAC 通感一体" in p

def test_feature_prompt_pins_stage_enum():
    p = build_feature_prompt(WAVE, [ev(1)], None)
    for s in ("未启动", "讨论中", "收敛中", "已定稿"):
        assert s in p

def test_legacy_prompt_uses_english_original_not_summary():
    """5G-A 事件没有中文摘要，只能喂原文。"""
    p = build_feature_prompt(ISAC, [], [ev(1, era="5G-A", meeting=118,
                                           summary=None, text="Rel-19 decision.")])
    assert "Rel-19 decision." in p

def test_parse_feature_response_ok():
    got = parse_feature_response(FEAT_REPLY)
    assert got["stage"] == "收敛中" and got["open_issues"] == ["波形未定"]

def test_parse_feature_rejects_bad_stage():
    bad = json.dumps({"stage": "快好了", "summary": "s", "open_issues": []})
    with pytest.raises(SchemaError, match="stage"):
        parse_feature_response(bad)

def test_parse_feature_rejects_missing_summary():
    with pytest.raises(SchemaError, match="summary"):
        parse_feature_response(json.dumps({"stage": "讨论中", "open_issues": []}))

def test_legacy_chunks_group_by_meeting_count():
    evs = [ev(1, "5G-A", m) for m in (112, 114, 116, 118, 120, 122)]
    chunks = build_legacy_chunks(evs, meetings_per_chunk=4)
    assert len(chunks) == 2
    assert {e["meeting"] for e in chunks[0]} == {112, 114, 116, 118}

def test_legacy_chunks_empty_input():
    assert build_legacy_chunks([], meetings_per_chunk=4) == []

def test_digest_writes_stage_and_summary(tmp_path):
    cli = FakeCli([FEAT_REPLY])
    state = digest_features([WAVE], [ev(1)], {}, CFG,
                            cli_factory=lambda m, e: cli, cache=LlmCache(tmp_path),
                            budget=Budget(10))
    assert state["waveform"]["stage"] == "收敛中"
    assert state["waveform"]["open_issues"] == ["波形未定"]

def test_digest_produces_legacy_summary_for_legacy_feature(tmp_path):
    legacy = [ev(i, "5G-A", 112 + i, summary=None, text=f"Legacy {i}.") for i in range(3)]
    cli = FakeCli(["Rel-19 阶段只做了信道建模。", FEAT_REPLY])
    state = digest_features([ISAC], legacy + [ev(9)], {}, CFG,
                            cli_factory=lambda m, e: cli, cache=LlmCache(tmp_path),
                            budget=Budget(10))
    assert "信道建模" in state["isac"]["legacy_summary"]

def test_digest_skips_feature_without_legacy(tmp_path):
    cli = FakeCli([FEAT_REPLY])
    state = digest_features([WAVE], [ev(1)], {}, CFG,
                            cli_factory=lambda m, e: cli, cache=LlmCache(tmp_path),
                            budget=Budget(10))
    assert "legacy_summary" not in state["waveform"]
    assert len(cli.calls) == 1

def test_digest_reuses_cached_legacy_summary(tmp_path):
    """5G-A 会议已冻结，legacy_summary 应当只算一次。"""
    legacy = [ev(1, "5G-A", 112, summary=None, text="Legacy.")]
    cache = LlmCache(tmp_path)
    cli1 = FakeCli(["历史归纳。", FEAT_REPLY])
    digest_features([ISAC], legacy + [ev(9)], {}, CFG, cli_factory=lambda m, e: cli1,
                    cache=cache, budget=Budget(10))
    cli2 = FakeCli([FEAT_REPLY])          # 只剩特性综述一次调用
    state = digest_features([ISAC], legacy + [ev(9)], {}, CFG,
                            cli_factory=lambda m, e: cli2, cache=cache, budget=Budget(10))
    assert len(cli2.calls) == 1
    assert state["isac"]["legacy_summary"] == "历史归纳。"

def test_digest_skips_feature_with_no_events(tmp_path):
    cli = FakeCli([])
    state = digest_features([WAVE], [], {}, CFG, cli_factory=lambda m, e: cli,
                            cache=LlmCache(tmp_path), budget=Budget(10))
    assert cli.calls == [] and state == {}
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/Scripts/python.exe -m pytest tests/test_extract_digest.py -v`
Expected: FAIL，`No module named 'ngr.extract.digest'`

- [ ] **Step 3: 写 `ngr/extract/digest.py`**

```python
from __future__ import annotations
import json, logging, re
from ngr.config import ExtractConfig
from ngr.extract.backend import LlmError, LlmRateLimited
from ngr.extract.budget import BudgetExhausted
from ngr.extract.cache import cache_key
from ngr.extract.tasks import PROMPT_VERSION, VALID_STAGE, SchemaError, strip_fence
from ngr.models import Feature

log = logging.getLogger(__name__)
EFFORT_DIGEST = "high"
MEETINGS_PER_CHUNK = 4

def _one_line(s: str) -> str:
    """把事件正文压成一行，供 "id:正文" 的逐行 blob 使用。

    blob 的隐含约定是"一行一个事件"。而 text_en 内部**可能本来就有换行** ——
    parse 层给 w:br/w:cr 补了换行符（实测该 fixture 有 48 处），表格单元格拼进来的
    文本也可能带换行。一旦某条事件跨占多行，续行就不带 "id:" 前缀，LLM 会把它
    误归到相邻的下一个 id，产出张冠李戴的摘要 —— 而且看不出任何异常。

    注意这只改变**喂给 LLM 的呈现形式**，不修改落盘的 text_en
    （全局约束：text_en 逐字保留）。"""
    return re.sub(r"\s+", " ", s).strip()

LEGACY_SYSTEM = """你在归纳一个 3GPP 特性在 5G-A（Rel-18/19）阶段的历史脉络。

只依据下面给出的英文 agreement 原文，回答三件事：
1. 这个阶段实际定下了什么；
2. 哪些问题当时**没有做充分**或被推迟；
3. 为什么它会延续到 6G。

用中文写 3–6 句，保留关键技术术语的英文原词。不要编造原文里没有的结论。
直接输出正文，不要 JSON，不要标题。"""

FEATURE_SYSTEM = f"""你在为一个 3GPP 6G 特性写"当前进展"综述。

只输出 JSON，不要任何解释文字：
{{"stage": "<{'|'.join(VALID_STAGE)}>", "summary": "<3-5 句中文综述>",
  "open_issues": ["<尚未解决的争议点>", "..."]}}

stage 只能取给定的四个值之一。open_issues 取 0–6 条，没有就给空数组。
只依据给出的材料，不要编造。"""

def build_legacy_chunks(legacy_events: list[dict],
                        meetings_per_chunk: int = MEETINGS_PER_CHUNK) -> list[list[dict]]:
    """按会议分组切块 —— 一个特性十几次会议的原文可能上千条，一次喂不下。"""
    if not legacy_events:
        return []
    meetings = sorted({e["meeting"] for e in legacy_events})
    chunks = []
    for i in range(0, len(meetings), meetings_per_chunk):
        group = set(meetings[i:i + meetings_per_chunk])
        chunks.append([e for e in legacy_events if e["meeting"] in group])
    return chunks

def build_feature_prompt(feature: Feature, six_events: list[dict],
                         legacy_chunk: list[dict] | None) -> str:
    if legacy_chunk is not None:
        parts = [LEGACY_SYSTEM, "", f"特性：{feature.name_zh}", ""]
        for e in sorted(legacy_chunk, key=lambda x: (x["meeting"], x["id"])):
            parts += [f"[{e['wg']}#{e['meeting']}] {e['kind']}", e["text_en"], ""]
        return "\n".join(parts)

    parts = [FEATURE_SYSTEM, "", f"特性：{feature.name_zh}", "", "6GR 阶段的进展："]
    for e in sorted(six_events, key=lambda x: (x["meeting"], x["id"])):
        line = e.get("summary_zh") or e["text_en"][:200]
        parts.append(f"- [{e['wg']}#{e['meeting']}] {line}")
    return "\n".join(parts)

def parse_feature_response(text: str) -> dict:
    try:
        data = json.loads(strip_fence(text))
    except json.JSONDecodeError as exc:
        raise SchemaError(f"特性综述不是合法 JSON: {text[:160]}") from exc
    stage = data.get("stage")
    if stage not in VALID_STAGE:
        raise SchemaError(f"stage 非法: {stage!r}，只能是 {list(VALID_STAGE)}")
    summary = data.get("summary")
    if not isinstance(summary, str) or not summary.strip():
        raise SchemaError("缺少 summary")
    issues = data.get("open_issues", [])
    if not isinstance(issues, list):
        raise SchemaError("open_issues 不是数组")
    return {"stage": stage, "summary": summary.strip(),
            "open_issues": [str(i) for i in issues][:6]}

def _legacy_summary(feature: Feature, legacy: list[dict], cli, cache, budget) -> str | None:
    """分块预归纳后合并。5G-A 会议已冻结，结果缓存后永不重算。"""
    chunks = build_legacy_chunks(legacy)
    if not chunks:
        return None

    pieces = []
    for chunk in chunks:
        blob = "\n".join(f"{e['id']}:{_one_line(e['text_en'])}" for e in
                         sorted(chunk, key=lambda x: x["id"]))
        key = cache_key("legacy:" + feature.slug, PROMPT_VERSION, EFFORT_DIGEST, blob)
        hit = cache.get(key)
        if hit:
            pieces.append(hit["text"])
            continue
        budget.check()
        res = cli.call(build_feature_prompt(feature, [], chunk))
        budget.spend(res, task="legacy_chunk")
        cache.put(key, {"text": res.text.strip()})
        pieces.append(res.text.strip())

    if len(pieces) == 1:
        return pieces[0]

    merged_blob = "\n\n".join(pieces)
    key = cache_key("legacy-merge:" + feature.slug, PROMPT_VERSION,
                    EFFORT_DIGEST, merged_blob)
    hit = cache.get(key)
    if hit:
        return hit["text"]
    budget.check()
    res = cli.call(LEGACY_SYSTEM + "\n\n把下面几段归纳合并成一段连贯的中文：\n\n"
                   + merged_blob)
    budget.spend(res, task="legacy_merge")
    cache.put(key, {"text": res.text.strip()})
    return res.text.strip()

def digest_features(features: list[Feature], events: list[dict], feat_state: dict,
                    cfg: ExtractConfig, *, cli_factory, cache, budget) -> dict:
    cli = cli_factory(cfg.model_digest, EFFORT_DIGEST)
    out = dict(feat_state)

    for feat in features:
        mine = [e for e in events if e.get("feature") == feat.slug]
        if not mine:
            continue
        six = [e for e in mine if e.get("era") == "6G"]
        legacy = [e for e in mine if e.get("era") == "5G-A"]
        entry = dict(out.get(feat.slug, {}))

        try:
            if feat.has_legacy and legacy:
                text = _legacy_summary(feat, legacy, cli, cache, budget)
                if text:
                    entry["legacy_summary"] = text

            blob = "\n".join(
                f"{e['id']}:{_one_line(e.get('summary_zh') or e['text_en'][:200])}"
                for e in sorted(six, key=lambda x: x["id"]))
            key = cache_key("feature:" + feat.slug, PROMPT_VERSION, EFFORT_DIGEST, blob)
            hit = cache.get(key)
            if hit:
                entry.update(hit)
            else:
                budget.check()
                res = cli.call(build_feature_prompt(feat, six, None))
                budget.spend(res, task="feature_digest")
                parsed = parse_feature_response(res.text)
                cache.put(key, parsed)
                entry.update(parsed)
        except (BudgetExhausted, LlmRateLimited) as exc:
            log.info("%s 的综述未完成（%s），下次继续", feat.slug, type(exc).__name__)
            if entry:
                out[feat.slug] = entry
            break
        except (SchemaError, LlmError) as exc:
            log.warning("%s 的综述失败: %s", feat.slug, exc)

        if entry:
            out[feat.slug] = entry

    return out
```

> `strip_fence` 在 Task 17 的 `tasks.py` 里已定义，这里直接复用 —— 不要再抄一份。

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/Scripts/python.exe -m pytest tests/test_extract_digest.py -v`
Expected: 13 passed

- [ ] **Step 5: Commit**

```bash
git add ngr/extract/digest.py tests/test_extract_digest.py
git commit -m "feat(extract): 特性综述与 5G-A 源头归纳"
```

---

## Phase 6：运维与编排

### Task 19: 告警、心跳与自动提交

一个每天 07:00 静默跑的任务，失败了没人知道，三个月后你才发现看板停在六月 —— 这是这类工具最典型的死法。本任务就是防这个。

**Files:**
- Create: `ngr/ops/__init__.py`, `ngr/ops/alerts.py`, `ngr/ops/gitio.py`
- Test: `tests/test_ops_alerts.py`, `tests/test_ops_gitio.py`

**Interfaces:**
- Consumes: `state/run_history.json`
- Produces:
  - `RunRecord`：`.started` `.duration_s` `.new_events` `.llm_calls` `.exit_code` `.message`
  - `append_run(path, record)`、`load_runs(path) -> list[dict]`
  - `heartbeat_banner(runs, today, *, stale_days=7) -> str | None`
  - `build_banner(alerts, runs, today) -> str | None`
  - `commit_outputs(repo, paths, message) -> bool`、`has_manual_changes(repo, guarded) -> list[str]`
  - `build_commit_message(stats_by_meeting) -> str`

- [ ] **Step 1: 写告警与心跳的失败测试**

```python
# tests/test_ops_alerts.py
from ngr.ops.alerts import RunRecord, append_run, load_runs, heartbeat_banner, build_banner

def rec(day, code=0, msg=""):
    return RunRecord(started=f"2026-09-{day:02d}T07:00:00", duration_s=12.5,
                     new_events=3, llm_calls=4, exit_code=code, message=msg)

def test_append_and_load(tmp_path):
    p = tmp_path / "run_history.json"
    append_run(p, rec(10)); append_run(p, rec(11))
    runs = load_runs(p)
    assert len(runs) == 2 and runs[-1]["exit_code"] == 0

def test_load_missing_file_returns_empty(tmp_path):
    assert load_runs(tmp_path / "nope.json") == []

def test_load_tolerates_corrupt_file(tmp_path):
    p = tmp_path / "run_history.json"
    p.write_text("{ broken", encoding="utf-8")
    assert load_runs(p) == []

def test_history_is_capped(tmp_path):
    p = tmp_path / "run_history.json"
    for d in range(1, 30):
        append_run(p, rec(d))
    assert len(load_runs(p)) <= 100

def test_heartbeat_silent_when_recent_success(tmp_path):
    runs = [rec(16).__dict__]
    assert heartbeat_banner(runs, today="2026-09-17") is None

def test_heartbeat_fires_after_stale_days():
    runs = [rec(1).__dict__]
    b = heartbeat_banner(runs, today="2026-09-17")
    assert b and "调度可能已失效" in b

def test_heartbeat_fires_when_no_runs_at_all():
    assert heartbeat_banner([], today="2026-09-17") is not None

def test_heartbeat_ignores_failed_runs_when_counting_success():
    runs = [rec(1, 0).__dict__, rec(16, 2, "解析失败").__dict__]
    assert heartbeat_banner(runs, today="2026-09-17") is not None

def test_build_banner_combines_alerts_and_heartbeat():
    b = build_banner(["解析断言失败: RAN1#127"], [rec(1).__dict__], today="2026-09-17")
    assert "RAN1#127" in b and "调度可能已失效" in b

def test_build_banner_none_when_all_clear():
    assert build_banner([], [rec(16).__dict__], today="2026-09-17") is None
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/Scripts/python.exe -m pytest tests/test_ops_alerts.py -v`
Expected: FAIL，`No module named 'ngr.ops'`

- [ ] **Step 3: 写 `ngr/ops/alerts.py`**

```python
from __future__ import annotations
import json
from dataclasses import asdict, dataclass
from datetime import date, datetime
from pathlib import Path

MAX_HISTORY = 100
STALE_DAYS = 7

@dataclass
class RunRecord:
    started: str
    duration_s: float
    new_events: int
    llm_calls: int
    exit_code: int
    message: str = ""

def load_runs(path: Path) -> list[dict]:
    path = Path(path)
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    return data if isinstance(data, list) else []

def append_run(path: Path, record: RunRecord) -> None:
    path = Path(path)
    runs = load_runs(path)
    runs.append(asdict(record))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(runs[-MAX_HISTORY:], ensure_ascii=False, indent=2),
                    encoding="utf-8")

def _as_date(ts: str) -> date | None:
    try:
        return datetime.fromisoformat(ts).date()
    except (ValueError, TypeError):
        return None

def heartbeat_banner(runs: list[dict], today: str,
                     *, stale_days: int = STALE_DAYS) -> str | None:
    """连续 stale_days 天没有成功运行就报警。
    即使计划任务被 Windows 停掉，打开看板也能立刻发现。"""
    today_d = _as_date(today) or date.today()
    ok_dates = [d for d in (_as_date(r.get("started", "")) for r in runs
                            if r.get("exit_code") == 0) if d]
    if not ok_dates:
        return f"⚠️ **调度可能已失效** —— 从未记录到成功运行（检查日期 {today}）"
    gap = (today_d - max(ok_dates)).days
    if gap >= stale_days:
        return (f"⚠️ **调度可能已失效** —— 距上次成功运行已 {gap} 天"
                f"（{max(ok_dates)}）。请检查计划任务与 `logs/`。")
    return None

def build_banner(alerts: list[str], runs: list[dict], today: str) -> str | None:
    parts = list(alerts)
    hb = heartbeat_banner(runs, today)
    if hb:
        parts.append(hb)
    if not parts:
        return None
    return "\n".join(p if p.startswith("⚠️") else f"⚠️ {p}" for p in parts)
```

- [ ] **Step 4: 写 git 提交的失败测试**

```python
# tests/test_ops_gitio.py
import subprocess
from pathlib import Path
from ngr.ops.gitio import commit_outputs, has_manual_changes, build_commit_message

def init_repo(tmp_path: Path) -> Path:
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.email", "t@e"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.name", "t"], cwd=tmp_path, check=True)
    (tmp_path / "config").mkdir()
    (tmp_path / "config" / "features.yaml").write_text("features: []\n", encoding="utf-8")
    subprocess.run(["git", "add", "-A"], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-qm", "init"], cwd=tmp_path, check=True)
    return tmp_path

def test_commit_outputs_creates_commit(tmp_path):
    repo = init_repo(tmp_path)
    (repo / "out").mkdir()
    (repo / "out" / "dashboard.md").write_text("x", encoding="utf-8")
    assert commit_outputs(repo, ["out"], "RAN1#127: +3 agreements")
    log = subprocess.run(["git", "log", "--oneline"], cwd=repo,
                         capture_output=True, text=True).stdout
    assert "RAN1#127" in log

def test_commit_outputs_noop_when_nothing_changed(tmp_path):
    repo = init_repo(tmp_path)
    (repo / "out").mkdir()
    (repo / "out" / "dashboard.md").write_text("x", encoding="utf-8")
    commit_outputs(repo, ["out"], "first")
    assert commit_outputs(repo, ["out"], "second") is False

def test_has_manual_changes_detects_edited_config(tmp_path):
    repo = init_repo(tmp_path)
    (repo / "config" / "features.yaml").write_text("features: [a]\n", encoding="utf-8")
    assert "config/features.yaml" in has_manual_changes(repo, ["config"])

def test_has_manual_changes_empty_when_clean(tmp_path):
    repo = init_repo(tmp_path)
    assert has_manual_changes(repo, ["config"]) == []

def test_commit_message_summarises_per_feature():
    msg = build_commit_message({("RAN1", 127): {"waveform": 9, "channel_coding": 7,
                                                None: 2}})
    assert msg.startswith("RAN1#127:")
    assert "+18 events" in msg
    assert "waveform +9" in msg
    assert "未归类 +2" in msg

def test_commit_message_multiple_meetings():
    msg = build_commit_message({("RAN1", 127): {"waveform": 2},
                                ("RAN2", 131): {"isac": 1}})
    assert "RAN1#127" in msg and "RAN2#131" in msg
```

- [ ] **Step 5: 跑测试确认失败**

Run: `.venv/Scripts/python.exe -m pytest tests/test_ops_gitio.py -v`
Expected: FAIL，`No module named 'ngr.ops.gitio'`

- [ ] **Step 6: 写 `ngr/ops/gitio.py`**

```python
from __future__ import annotations
import subprocess
from pathlib import Path

ATTRIBUTION = "Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>"

def _git(repo: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=repo, capture_output=True,
                          text=True, encoding="utf-8")

def has_manual_changes(repo: Path, guarded: list[str]) -> list[str]:
    """检查受保护路径（config/ 等）是否有未提交的手工改动。
    有的话拒绝自动提交 —— 绝不覆盖用户手改的 features.yaml。"""
    proc = _git(repo, "status", "--porcelain", "--", *guarded)
    out = []
    for line in proc.stdout.splitlines():
        if len(line) > 3:
            out.append(line[3:].strip().replace("\\", "/"))
    return out

def commit_outputs(repo: Path, paths: list[str], message: str) -> bool:
    """暂存并提交指定路径。无变更时返回 False，不产生空提交。不 push。"""
    repo = Path(repo)
    _git(repo, "add", "--", *paths)
    if not _git(repo, "diff", "--cached", "--quiet").returncode:
        return False           # returncode 0 表示无差异
    # 提交信息走 stdin，避免其中的引号与中文在 Windows 上被 shell 吃掉
    body = f"{message}\n\n{ATTRIBUTION}\n"
    proc = subprocess.run(["git", "commit", "-q", "-F", "-"], cwd=repo,
                          input=body, capture_output=True, text=True,
                          encoding="utf-8")
    return proc.returncode == 0

def build_commit_message(stats: dict[tuple[str, int], dict[str | None, int]]) -> str:
    """生成 'RAN1#127: +23 events (waveform +9, coding +7, 未归类 +2)' 这样的提交信息。
    这样 git log --oneline 本身就是一份进展流水账。"""
    chunks = []
    for (wg, meeting), per_feature in sorted(stats.items()):
        total = sum(per_feature.values())
        parts = []
        for slug, n in sorted(per_feature.items(),
                              key=lambda kv: (-kv[1], kv[0] or "")):
            parts.append(f"{slug or '未归类'} +{n}")
        detail = f" ({', '.join(parts)})" if parts else ""
        chunks.append(f"{wg}#{meeting}: +{total} events{detail}")
    return "; ".join(chunks) if chunks else "chore: 无新增事件"
```

- [ ] **Step 7: 跑测试确认通过**

Run: `.venv/Scripts/python.exe -m pytest tests/test_ops_alerts.py tests/test_ops_gitio.py -v`
Expected: 16 passed

- [ ] **Step 8: Commit**

```bash
git add ngr/ops/ tests/test_ops_alerts.py tests/test_ops_gitio.py
git commit -m "feat(ops): 告警横幅、心跳检查、自动提交"
```

---

### Task 20: CLI 命令面与退出码

**Files:**
- Create: `ngr/cli.py`, `ngr/pipeline.py`
- Test: `tests/test_cli.py`

**Interfaces:**
- Consumes: 前面全部模块
- Produces:
  - `main(argv=None) -> int`
  - `run_pipeline(*, wgs=None, use_llm=True, force=False, meetings=None) -> PipelineResult`
  - `PipelineResult`：`.exit_code` `.alerts` `.new_events` `.llm_calls` `.stats_by_meeting`
  - 退出码常量 `EXIT_OK=0` `EXIT_PARSE=2` `EXIT_LLM=3` `EXIT_GIT=4`

- [ ] **Step 1: 写失败的测试**

```python
# tests/test_cli.py
import pytest
from ngr import cli
from ngr.cli import main, EXIT_OK, EXIT_PARSE, EXIT_LLM, EXIT_GIT
from ngr.parse.runner import ParseError

class FakeResult:
    def __init__(self, **kw):
        self.exit_code = kw.get("exit_code", EXIT_OK)
        self.alerts = kw.get("alerts", [])
        self.new_events = kw.get("new_events", 0)
        self.llm_calls = kw.get("llm_calls", 0)
        self.stats_by_meeting = kw.get("stats_by_meeting", {})

def test_run_returns_zero_on_success(monkeypatch):
    monkeypatch.setattr(cli, "run_pipeline", lambda **kw: FakeResult())
    assert main(["run"]) == EXIT_OK

def test_run_no_llm_flag_disables_llm(monkeypatch):
    seen = {}
    def fake(**kw): seen.update(kw); return FakeResult()
    monkeypatch.setattr(cli, "run_pipeline", fake)
    main(["run", "--no-llm"])
    assert seen["use_llm"] is False

def test_run_defaults_to_llm_enabled(monkeypatch):
    seen = {}
    monkeypatch.setattr(cli, "run_pipeline", lambda **kw: seen.update(kw) or FakeResult())
    main(["run"])
    assert seen["use_llm"] is True

def test_parse_error_exits_two(monkeypatch):
    def boom(**kw): raise ParseError("模板变了")
    monkeypatch.setattr(cli, "run_pipeline", boom)
    assert main(["run"]) == EXIT_PARSE

def test_llm_rate_limit_exits_three(monkeypatch):
    monkeypatch.setattr(cli, "run_pipeline",
                        lambda **kw: FakeResult(exit_code=EXIT_LLM))
    assert main(["run"]) == EXIT_LLM

def test_manual_config_changes_exit_four(monkeypatch):
    monkeypatch.setattr(cli, "run_pipeline",
                        lambda **kw: FakeResult(exit_code=EXIT_GIT,
                                                alerts=["config/features.yaml 有手工改动"]))
    assert main(["run"]) == EXIT_GIT

def test_backfill_passes_meeting_range(monkeypatch):
    seen = {}
    monkeypatch.setattr(cli, "run_pipeline", lambda **kw: seen.update(kw) or FakeResult())
    main(["backfill", "--wg", "RAN1", "--from", "112", "--to", "127"])
    assert seen["wgs"] == ["RAN1"] and seen["meetings"] == (112, 127)

def test_remap_skips_fetch_and_llm(monkeypatch):
    seen = {}
    monkeypatch.setattr(cli, "run_remap", lambda **kw: seen.update(kw) or FakeResult())
    assert main(["remap"]) == EXIT_OK
    assert seen == {}

def test_lineage_report_prints(monkeypatch, capsys):
    monkeypatch.setattr(cli, "build_lineage_report", lambda: "# 血统命中对照表\n- x")
    assert main(["lineage-report"]) == EXIT_OK
    assert "血统命中对照表" in capsys.readouterr().out

def test_enrich_runs_llm_only(monkeypatch):
    seen = {}
    monkeypatch.setattr(cli, "run_enrich", lambda **kw: seen.update(kw) or FakeResult())
    assert main(["enrich"]) == EXIT_OK

def test_doctor_returns_its_own_code(monkeypatch):
    monkeypatch.setattr(cli, "run_doctor", lambda: 1)
    assert main(["doctor"]) == 1

def test_unknown_command_errors():
    with pytest.raises(SystemExit):
        main(["nonsense"])

def test_no_command_shows_help(capsys):
    with pytest.raises(SystemExit):
        main([])
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/Scripts/python.exe -m pytest tests/test_cli.py -v`
Expected: FAIL，`No module named 'ngr.cli'`

- [ ] **Step 3: 写 `ngr/pipeline.py`**

```python
from __future__ import annotations
import json, logging, time
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from ngr.config import load_features, load_sources
from ngr.extract.backend import ClaudeCli
from ngr.extract.budget import Budget
from ngr.extract.cache import LlmCache
from ngr.extract.digest import digest_features
from ngr.extract.runner import extract_all
from ngr.fetch.client import Http, RateLimited
from ngr.fetch.discover import discover_meetings, fetch_window
from ngr.fetch.manifest import Manifest
from ngr.fetch.runner import fetch_meeting
from ngr.mapping.runner import map_meeting, merge_events, write_state
from ngr.parse.runner import ParseError, parse_meeting, write_parsed
from ngr.ops.alerts import RunRecord, append_run, build_banner, load_runs
from ngr.ops.gitio import build_commit_message, commit_outputs, has_manual_changes
from ngr.paths import P
from ngr.render.runner import render_all

log = logging.getLogger(__name__)
EXIT_OK, EXIT_PARSE, EXIT_LLM, EXIT_GIT = 0, 2, 3, 4
GUARDED = ["config"]
FREEZE_LAG = 2      # 落后最新会议 2 场以上且已成功解析 → 冻结

@dataclass
class PipelineResult:
    exit_code: int = EXIT_OK
    alerts: list[str] = field(default_factory=list)
    new_events: int = 0
    llm_calls: int = 0
    stats_by_meeting: dict = field(default_factory=dict)

def _load_json(path: Path, default):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return default

def run_pipeline(*, wgs=None, use_llm=True, force=False,
                 meetings: tuple[int, int] | None = None) -> PipelineResult:
    started = time.time()
    cfg = load_sources()
    features = load_features()
    res = PipelineResult()

    manual = has_manual_changes(P.root, GUARDED)
    if manual:
        res.alerts.append(f"{', '.join(manual)} 有未提交的手工改动，已跳过自动提交")
        res.exit_code = EXIT_GIT

    http = Http(cfg.http)
    events = _load_json(P.state / "events.json", [])
    today = time.strftime("%Y-%m-%d")
    stats_by_meeting: dict = defaultdict(lambda: defaultdict(int))

    for wg, wgcfg in cfg.wgs.items():
        if wgs and wg not in wgs:
            continue
        window = fetch_window(features, wg, wgcfg)
        if window is None:
            continue
        lo, hi = meetings if meetings else window

        try:
            all_meetings = discover_meetings(http, wg, wgcfg)
        except RateLimited as exc:
            res.alerts.append(f"{wg} 会议发现被限流: {exc}")
            continue

        latest_with_content = 0   # 本次真正抓到纪要的最大会议号，见下方冻结逻辑
        for mtg in all_meetings:
            if mtg.number < lo or (hi is not None and mtg.number > hi):
                continue
            raw_dir = P.raw_dir(wg, mtg.number)
            try:
                fetched = fetch_meeting(http, mtg, wgcfg, raw_dir=raw_dir, force=force)
            except RateLimited as exc:
                res.alerts.append(f"{mtg.label} 抓取被限流: {exc}")
                continue
            if fetched.skipped_reason == "frozen":
                continue
            if "minutes_docx" in fetched.missing:
                continue          # 会议尚未上传纪要，属正常

            agenda_required = (wgcfg.agenda_csv_since is not None
                               and mtg.number >= wgcfg.agenda_csv_since)
            parsed = parse_meeting(raw_dir, mtg, agenda_required=agenda_required)
            write_parsed(parsed, P.parsed_dir(wg, mtg.number))

            payload = _load_json(P.parsed_dir(wg, mtg.number) / "events.json", {})
            incoming = map_meeting(payload, features)
            # scope 必须显式给出：从 incoming 反推的话，这场会议一旦归集归零
            # （features.yaml 改坏、正则回归），它就不在 scope 里，其全部历史
            # 一条都不会被检查，stale_ids 恒为空 —— 探针在最该响时哑火。
            events, stats = merge_events(events, incoming, today=today,
                                         scope={(wg, mtg.number)})
            if stats.stale_ids:
                res.alerts.append(
                    f"{wg}#{mtg.number}: {len(stats.stale_ids)} 条历史事件本次未再出现")
            res.new_events += stats.added
            # 直接用 merge 算好的统计。**不要拿 added_ids 去 join incoming 的 Event.id**：
            # merge 会重新定序，incoming 上的 id 只是 map 阶段的位置式草稿值，
            # 纪要改版插一条就整体错位（实测 0/4 对得上），join 会把新增记到另一条头上。
            for (w, m), per in stats.added_by_feature.items():
                for feat, n in per.items():
                    stats_by_meeting[(w, m)][feat] += n

            # 仅在解析成功之后才冻结，且 latest 用"本次真正抓到纪要的最大会议号"。
            # 实测各组最新目录常常只有 Invitation（会议未召开），用目录列表的最大值
            # 会把最新的有内容会议提前冻住，其 v010→v100 的最终版纪要永远不会被抓到。
            latest_with_content = max(latest_with_content, mtg.number)
            if mtg.number <= latest_with_content - FREEZE_LAG:
                man = Manifest(raw_dir); man.mark_frozen(); man.save()

    feat_state = _load_json(P.state / "features_state.json", {})
    if use_llm and cfg.extract.backend == "cli":
        budget = Budget(cfg.extract.max_calls_per_run)
        cache = LlmCache(P.state / "llm_cache")
        factory = lambda model, effort: ClaudeCli(model, effort)
        ex = extract_all(events, cfg.extract, cli_factory=factory,
                         cache=cache, budget=budget)
        feat_state = digest_features(features, events, feat_state, cfg.extract,
                                     cli_factory=factory, cache=cache, budget=budget)
        budget.log(P.state / "usage_log.jsonl")
        res.llm_calls = budget.calls
        if ex.rate_limited:
            res.alerts.append("LLM 额度受限，部分摘要未完成，下次运行自动补")
            res.exit_code = max(res.exit_code, EXIT_LLM)
        if ex.failed:
            res.alerts.append(f"{ex.failed} 条摘要生成失败，事件本身已入库")

    write_state(events, P.state / "events.json")
    (P.state / "features_state.json").write_text(
        json.dumps(feat_state, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8")

    runs = load_runs(P.state / "run_history.json")
    banner = build_banner(res.alerts, runs, today)
    render_all(events, features, feat_state, P.out, banner=banner)

    res.stats_by_meeting = {k: dict(v) for k, v in stats_by_meeting.items()}
    if not manual and res.new_events:
        commit_outputs(P.root, ["data/state", "out"],
                       build_commit_message(res.stats_by_meeting))

    append_run(P.state / "run_history.json",
               RunRecord(started=time.strftime("%Y-%m-%dT%H:%M:%S"),
                         duration_s=round(time.time() - started, 1),
                         new_events=res.new_events, llm_calls=res.llm_calls,
                         exit_code=res.exit_code, message="; ".join(res.alerts)))
    return res
```

- [ ] **Step 4: 写 `ngr/cli.py`**

```python
from __future__ import annotations
import argparse, logging, sys, time
from ngr.config import load_features
from ngr.mapping.report import lineage_report
from ngr.parse.runner import ParseError
from ngr.paths import P
from ngr.pipeline import (EXIT_GIT, EXIT_LLM, EXIT_OK, EXIT_PARSE,
                          PipelineResult, run_pipeline)

def _setup_logging() -> None:
    P.logs.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        handlers=[logging.StreamHandler(sys.stderr),
                  logging.FileHandler(P.logs / f"ngr-{time.strftime('%Y-%m-%d')}.log",
                                      encoding="utf-8")])

def run_remap(**kwargs) -> PipelineResult:
    """只重跑 map + render：不联网、不调 LLM。改完 features.yaml 后用它。"""
    from ngr.pipeline import run_pipeline_remap
    return run_pipeline_remap(**kwargs)

def run_enrich(**kwargs) -> PipelineResult:
    """只补跑 extract：给积压的待摘要事件补摘要。"""
    from ngr.pipeline import run_pipeline_enrich
    return run_pipeline_enrich(**kwargs)

def run_doctor(**kwargs) -> int:
    """自检。惰性导入：doctor 模块在 Task 21 才创建，cli 不能在顶层依赖它。"""
    from ngr.ops.doctor import run_doctor as _run_doctor
    return _run_doctor(**kwargs)

def build_lineage_report() -> str:
    import json
    features = load_features()
    parsed = []
    for path in sorted(P.parsed.rglob("events.json")):
        parsed.append(json.loads(path.read_text(encoding="utf-8")))
    return lineage_report(features, parsed)

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="ngr", description="6G RAN 进展跟踪")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_run = sub.add_parser("run", help="抓取→解析→归集→摘要→渲染→提交")
    p_run.add_argument("--no-llm", action="store_true", help="跳过 LLM，零额度消耗")
    p_run.add_argument("--wg", action="append", help="只处理指定工作组，可重复")
    p_run.add_argument("--force", action="store_true", help="忽略 frozen 标记")

    p_bf = sub.add_parser("backfill", help="回填历史会议，可中断续跑")
    p_bf.add_argument("--wg", required=True)
    p_bf.add_argument("--from", dest="frm", type=int, required=True)
    p_bf.add_argument("--to", dest="to", type=int, required=True)
    p_bf.add_argument("--no-llm", action="store_true")

    sub.add_parser("remap", help="只重跑 map+render（改完 features.yaml 用）")
    sub.add_parser("lineage-report", help="打印血统命中对照表")
    sub.add_parser("enrich", help="只补跑 LLM 摘要")
    sub.add_parser("doctor", help="自检")

    args = parser.parse_args(argv)
    _setup_logging()

    try:
        if args.cmd == "run":
            res = run_pipeline(wgs=args.wg, use_llm=not args.no_llm, force=args.force)
        elif args.cmd == "backfill":
            res = run_pipeline(wgs=[args.wg], use_llm=not args.no_llm,
                               meetings=(args.frm, args.to))
        elif args.cmd == "remap":
            res = run_remap()
        elif args.cmd == "enrich":
            res = run_enrich()
        elif args.cmd == "lineage-report":
            print(build_lineage_report())
            return EXIT_OK
        elif args.cmd == "doctor":
            return run_doctor()
        else:
            parser.error(f"未知命令: {args.cmd}")
    except ParseError as exc:
        logging.error("解析断言失败，已保留 raw 且未写 state: %s", exc)
        return EXIT_PARSE

    for alert in res.alerts:
        logging.warning("%s", alert)
    logging.info("完成：新增 %d 条事件，LLM 调用 %d 次", res.new_events, res.llm_calls)
    return res.exit_code
```

- [ ] **Step 5: 补 `run_pipeline_remap` 与 `run_pipeline_enrich`**

在 `ngr/pipeline.py` 末尾追加。两者都是 `run_pipeline` 的裁剪版，共用同样的读写与渲染尾巴：

```python
def run_pipeline_remap() -> PipelineResult:
    """跳过 fetch 与 parse，直接从 data/parsed 重新归集。秒级完成，零额度。"""
    features = load_features()
    res = PipelineResult()
    today = time.strftime("%Y-%m-%d")
    events: list[dict] = []
    stats_by_meeting: dict = defaultdict(lambda: defaultdict(int))

    for path in sorted(P.parsed.rglob("events.json")):
        payload = _load_json(path, {})
        if not payload:
            continue
        incoming = map_meeting(payload, features)
        # 同上：scope 显式给出，否则归集归零的会议不会被检查（见 merge_events 注释）
        events, stats = merge_events(events, incoming, today=today,
                                     scope={(payload["wg"], payload["meeting"])})
        if stats.stale_ids:
            res.alerts.append(
                f"{payload['wg']}#{payload['meeting']}: "
                f"{len(stats.stale_ids)} 条历史事件本次未再出现")
        res.new_events += stats.added
        # 同上：用 merge 算好的统计，不要 join incoming 的 Event.id（那是草稿值）
        for (w, m), per in stats.added_by_feature.items():
            for feat, n in per.items():
                stats_by_meeting[(w, m)][feat] += n

    feat_state = _load_json(P.state / "features_state.json", {})
    write_state(events, P.state / "events.json")
    runs = load_runs(P.state / "run_history.json")
    render_all(events, features, feat_state, P.out,
               banner=build_banner(res.alerts, runs, today))
    res.stats_by_meeting = {k: dict(v) for k, v in stats_by_meeting.items()}
    return res

def run_pipeline_enrich() -> PipelineResult:
    """只补跑 LLM：给积压的 pending / failed 事件补摘要。"""
    cfg = load_sources()
    features = load_features()
    res = PipelineResult()
    events = _load_json(P.state / "events.json", [])
    feat_state = _load_json(P.state / "features_state.json", {})

    budget = Budget(cfg.extract.max_calls_per_run)
    cache = LlmCache(P.state / "llm_cache")
    factory = lambda model, effort: ClaudeCli(model, effort)
    ex = extract_all(events, cfg.extract, cli_factory=factory, cache=cache, budget=budget)
    feat_state = digest_features(features, events, feat_state, cfg.extract,
                                 cli_factory=factory, cache=cache, budget=budget)
    budget.log(P.state / "usage_log.jsonl")
    res.llm_calls = budget.calls
    if ex.rate_limited:
        res.alerts.append("LLM 额度受限，剩余摘要下次继续")
        res.exit_code = EXIT_LLM

    write_state(events, P.state / "events.json")
    (P.state / "features_state.json").write_text(
        json.dumps(feat_state, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8")
    today = time.strftime("%Y-%m-%d")
    runs = load_runs(P.state / "run_history.json")
    render_all(events, features, feat_state, P.out,
               banner=build_banner(res.alerts, runs, today))
    return res
```

- [ ] **Step 6: 跑测试确认通过**

Run: `.venv/Scripts/python.exe -m pytest tests/test_cli.py -v`
Expected: 13 passed

- [ ] **Step 7: 跑全部测试**

Run: `.venv/Scripts/python.exe -m pytest -v`
Expected: 全绿

- [ ] **Step 8: Commit**

```bash
git add ngr/cli.py ngr/pipeline.py tests/test_cli.py
git commit -m "feat(cli): 命令面、管线编排与退出码"
```

---

### Task 21: doctor、计划任务与首次回填

**Files:**
- Create: `ngr/ops/doctor.py`, `scripts/install-task.ps1`, `README.md`
- Test: `tests/test_ops_doctor.py`

**Interfaces:**
- Consumes: `load_sources`、`load_features`、`ClaudeCli`、`Http`
- Produces: `check_all(*, probe_network=False) -> list[Check]`、`run_doctor(probe_network=False) -> int`、`Check`：`.name` `.ok` `.detail`

- [ ] **Step 1: 写失败的测试**

```python
# tests/test_ops_doctor.py
from ngr.ops import doctor
from ngr.ops.doctor import check_all, run_doctor

def test_all_checks_have_names(monkeypatch):
    monkeypatch.setattr(doctor, "_which", lambda n: "C:/claude.exe")
    checks = check_all()
    assert checks and all(c.name for c in checks)

def test_reports_missing_claude_cli(monkeypatch):
    monkeypatch.setattr(doctor, "_which", lambda n: None)
    bad = [c for c in check_all() if not c.ok]
    assert any("claude" in c.name.lower() for c in bad)

def test_reports_bad_config(monkeypatch, tmp_path):
    monkeypatch.setattr(doctor, "_which", lambda n: "x")
    monkeypatch.setattr(doctor, "load_sources",
                        lambda: (_ for _ in ()).throw(RuntimeError("坏配置")))
    bad = [c for c in check_all() if not c.ok]
    assert any("配置" in c.name for c in bad)

def test_skips_network_probe_by_default(monkeypatch):
    monkeypatch.setattr(doctor, "_which", lambda n: "x")
    called = []
    monkeypatch.setattr(doctor, "_probe_3gpp", lambda: called.append(1) or True)
    check_all(probe_network=False)
    assert called == []

def test_runs_network_probe_when_asked(monkeypatch):
    monkeypatch.setattr(doctor, "_which", lambda n: "x")
    monkeypatch.setattr(doctor, "_probe_3gpp", lambda: True)
    assert any("3GPP" in c.name for c in check_all(probe_network=True))

def test_run_doctor_returns_zero_when_all_ok(monkeypatch, capsys):
    monkeypatch.setattr(doctor, "check_all",
                        lambda **kw: [doctor.Check("A", True, "ok")])
    assert run_doctor() == 0
    assert "A" in capsys.readouterr().out

def test_run_doctor_returns_one_on_failure(monkeypatch):
    monkeypatch.setattr(doctor, "check_all",
                        lambda **kw: [doctor.Check("A", False, "缺失")])
    assert run_doctor() == 1
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/Scripts/python.exe -m pytest tests/test_ops_doctor.py -v`
Expected: FAIL，`No module named 'ngr.ops.doctor'`

- [ ] **Step 3: 写 `ngr/ops/doctor.py`**

```python
from __future__ import annotations
import shutil
from dataclasses import dataclass
from ngr.config import load_features, load_sources
from ngr.ops.gitio import has_manual_changes
from ngr.paths import P

@dataclass
class Check:
    name: str
    ok: bool
    detail: str = ""

def _which(name: str) -> str | None:
    return shutil.which(name)

def _probe_3gpp() -> bool:
    from ngr.fetch.client import Http
    cfg = load_sources()
    Http(cfg.http).get("https://www.3gpp.org/ftp/tsg_ran/")
    return True

def check_all(*, probe_network: bool = False) -> list[Check]:
    checks: list[Check] = []

    path = _which("claude")
    checks.append(Check("claude CLI 可用", bool(path), path or "未在 PATH 中找到 claude"))

    try:
        cfg = load_sources()
        checks.append(Check("配置 sources.yaml", True, f"{len(cfg.wgs)} 个工作组"))
    except Exception as exc:
        checks.append(Check("配置 sources.yaml", False, str(exc)))
        cfg = None

    try:
        feats = load_features()
        legacy = sum(1 for f in feats if f.has_legacy)
        checks.append(Check("配置 features.yaml", True,
                            f"{len(feats)} 个特性，其中 {legacy} 个有 5G-A 血统"))
    except Exception as exc:
        checks.append(Check("配置 features.yaml", False, str(exc)))

    for label, d in [("state 目录", P.state), ("out 目录", P.out)]:
        checks.append(Check(label, d.exists(), str(d)))

    manual = has_manual_changes(P.root, ["config"])
    checks.append(Check("config/ 无未提交改动", not manual,
                        ", ".join(manual) if manual else "干净"))

    if probe_network and cfg is not None:
        try:
            _probe_3gpp()
            checks.append(Check("3GPP 站点可达", True, "HTTP 200"))
        except Exception as exc:
            checks.append(Check("3GPP 站点可达", False, str(exc)))

    return checks

def run_doctor(probe_network: bool = False) -> int:
    checks = check_all(probe_network=probe_network)
    for c in checks:
        print(f"[{'OK ' if c.ok else 'FAIL'}] {c.name}: {c.detail}")
    failed = [c for c in checks if not c.ok]
    if failed:
        print(f"\n{len(failed)} 项未通过")
        return 1
    print("\n全部通过")
    return 0
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/Scripts/python.exe -m pytest tests/test_ops_doctor.py -v`
Expected: 7 passed

- [ ] **Step 5: 写 `scripts/install-task.ps1`**

```powershell
# 注册每日 07:00 的计划任务。需在项目根目录下以普通用户身份运行。
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$python = Join-Path $root ".venv\Scripts\python.exe"

if (-not (Test-Path $python)) {
    throw "未找到 $python，请先创建虚拟环境并安装依赖"
}

$cmd = "cd '$root'; & '$python' -m ngr run"
$action = New-ScheduledTaskAction -Execute "powershell.exe" `
    -Argument "-NoProfile -WindowStyle Hidden -Command `"$cmd`""
$trigger = New-ScheduledTaskTrigger -Daily -At 7:00am
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable `
    -DontStopIfGoingOnBatteries -ExecutionTimeLimit (New-TimeSpan -Hours 3)

Register-ScheduledTask -TaskName "NGR_Spec" -Action $action -Trigger $trigger `
    -Settings $settings -Description "6G RAN 进展跟踪：每日抓取与渲染" -Force

Write-Host "已注册计划任务 NGR_Spec（每日 07:00）"
Write-Host "手动触发一次： Start-ScheduledTask -TaskName NGR_Spec"
Write-Host "查看上次结果： Get-ScheduledTaskInfo -TaskName NGR_Spec"
```

`-StartWhenAvailable` 很重要：笔记本 07:00 常在休眠，没有这个参数当天就整场跳过。

- [ ] **Step 6: 自检并试跑**

```bash
.venv/Scripts/python.exe -m ngr doctor
```

Expected: 全部通过。若 `claude CLI 可用` 失败，确认 `claude` 在 PATH 中。

- [ ] **Step 7: 首次回填（先不花额度）**

```bash
.venv/Scripts/python.exe -m ngr backfill --wg RAN1 --from 124 --to 127 --no-llm
.venv/Scripts/python.exe -m ngr lineage-report
```

对着血统报告检查：**每个 6G 血统段都应有命中**。有命中为 0 的段就去调 `config/features.yaml` 的锚点，然后 `ngr remap` 重看 —— 这一步不联网、不花额度，可以反复来。

- [ ] **Step 8: 回填 5G-A 血统段并校准正则**

```bash
.venv/Scripts/python.exe -m ngr backfill --wg RAN1 --from 112 --to 123 --no-llm
.venv/Scripts/python.exe -m ngr lineage-report > lineage.txt
```

这一步耗时最长（十几次会议、每次一份约 1 MB 的 docx，按 0.5 s 间隔限速）。看 `lineage.txt` 里 5G-A 各段命中的 heading 是否确实是你要的议题；不对就改 `title_re` → `ngr remap` → 再看。**反复到满意为止，然后才开 LLM。**

- [ ] **Step 9: 开 LLM 跑摘要**

```bash
.venv/Scripts/python.exe -m ngr enrich
```

`max_calls_per_run=60` 会在用满后干净退出。按 spec §6.4 估算，全量回填约需 72 次调用，所以**跑两次**即可完成。第二次跑时已完成的部分走缓存，不重复消耗。

跑完检查用量：

把下面的内容存成 `scripts/usage.py` 后运行 `.venv/Scripts/python.exe scripts/usage.py`：

```python
import json, pathlib
rows = [json.loads(line) for line in
        pathlib.Path("data/state/usage_log.jsonl").read_text(encoding="utf-8").splitlines()]
total = sum(r["cost_usd"] for r in rows)
by_task = {}
for r in rows:
    by_task[r["task"]] = by_task.get(r["task"], 0.0) + r["cost_usd"]
print(f"{len(rows)} 次调用，list 等价合计 ${total:.2f}")
for task, cost in sorted(by_task.items(), key=lambda kv: -kv[1]):
    print(f"  {task:16s} ${cost:.2f}")
```

提醒：订阅模式下 `cost_usd` 是按 list price 折算的**用量代理值，不是账单**。

- [ ] **Step 10: 写 `README.md`**

至少包含：一句话用途、安装步骤、六个命令各自什么时候用、`config/features.yaml` 怎么加特性和血统段、出问题先跑 `ngr doctor`、退出码含义表、以及"网页发布需要在 Claude Code 会话里手动要求"这条约束。

- [ ] **Step 11: 装计划任务并验证**

```powershell
powershell -ExecutionPolicy Bypass -File scripts/install-task.ps1
Start-ScheduledTask -TaskName NGR_Spec
Get-ScheduledTaskInfo -TaskName NGR_Spec     # LastTaskResult 应为 0
```

- [ ] **Step 12: 最终验收**

- `.venv/Scripts/python.exe -m pytest` 全绿
- `out/dashboard.md` 顶部无告警横幅，特性表有数据
- 至少一个有 5G-A 血统的特性页含「5G-A 源头」一节
- 浏览器打开 `out/site/index.html` 正常，深色模式可读
- `git log --oneline` 能看到自动生成的进展流水账

- [ ] **Step 13: Commit**

```bash
git add ngr/ops/doctor.py scripts/install-task.ps1 README.md tests/test_ops_doctor.py
git commit -m "feat(ops): doctor 自检、计划任务安装脚本、README"
```

---

### Task 22: 未归类议程项与按需深挖

补齐 spec 中两项尚未实现的要求：§3.3 的 `unmapped_policy: report`（未映射的 6GR 议程项要列出来等人确认）与 §4 的按需深挖命令。

**Files:**
- Create: `ngr/mapping/unmapped.py`, `ngr/fetch/docs.py`
- Modify: `ngr/cli.py`（加 `fetch-docs` 子命令）、`ngr/pipeline.py`（把 unmapped 传给渲染）
- Test: `tests/test_mapping_unmapped.py`, `tests/test_fetch_docs.py`

**Interfaces:**
- Consumes: `match_event`、`parse_listing`、`Http`
- Produces:
  - `collect_unmapped(features, parsed_meetings, *, sixg_roots) -> list[str]`
  - `fetch_docs(http, meeting, cfg, agenda_prefix, out_dir) -> list[Path]`

- [ ] **Step 1: 写未归类收集的失败测试**

```python
# tests/test_mapping_unmapped.py
from ngr.models import Feature, LineageSegment
from ngr.mapping.unmapped import collect_unmapped

def seg(agenda):
    return LineageSegment(era="6G", release="Rel-20", depth="full", agenda=agenda,
                          title_re=None, meetings={"RAN1": (124, None)})

FEATS = [Feature(slug="waveform", name_zh="波形",
                 lineage=[seg(["RAN1:10.2", "RAN1:10.2.*"])])]

def parsed(events):
    return {"wg": "RAN1", "meeting": 126, "events": events}

def ev(item, title, path=None):
    return {"kind": "agreement", "text_en": "x", "para_index": 1,
            "agenda_item": item, "agenda_title": title,
            "heading_path": path or ["Rel-20 Study of 6GR", title]}

def test_unmapped_6g_items_are_reported():
    out = collect_unmapped(FEATS, [parsed([ev("10.8", "ISAC")])], sixg_roots=["10"])
    assert out == ["RAN1:10.8 ISAC"]

def test_mapped_items_are_not_reported():
    assert collect_unmapped(FEATS, [parsed([ev("10.2", "Waveform")])],
                            sixg_roots=["10"]) == []

def test_non_6g_items_are_ignored():
    """第 9 章是 Rel-20 的 5G-A 演进，不算 6GR 未归类。"""
    out = collect_unmapped(FEATS, [parsed([ev("9.1", "AI/ML", ["Release 20 NR", "AI/ML"])])],
                           sixg_roots=["10"])
    assert out == []

def test_child_items_are_rolled_up_to_parent():
    out = collect_unmapped(FEATS, [parsed([ev("10.8.1", "Evaluations"),
                                           ev("10.8.2", "Integration")])],
                           sixg_roots=["10"])
    assert out == ["RAN1:10.8 (2 个子项未归类)"]

def test_result_is_sorted_and_deduped():
    out = collect_unmapped(FEATS, [parsed([ev("10.9", "NTN"), ev("10.7", "WUS"),
                                           ev("10.9", "NTN")])],
                           sixg_roots=["10"])
    assert out == ["RAN1:10.7 WUS", "RAN1:10.9 NTN"]

def test_events_without_agenda_item_are_skipped():
    """5G-A 老会议没有议程号，不进未归类清单（它们靠正则归集）。"""
    assert collect_unmapped(FEATS, [parsed([ev(None, "X", ["Rel-19", "X"])])],
                            sixg_roots=["10"]) == []
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/Scripts/python.exe -m pytest tests/test_mapping_unmapped.py -v`
Expected: FAIL，`No module named 'ngr.mapping.unmapped'`

- [ ] **Step 3: 写 `ngr/mapping/unmapped.py`**

```python
from __future__ import annotations
from collections import defaultdict
from ngr.mapping.lineage import match_event
from ngr.models import Feature

def _root_of(item: str) -> str:
    return item.split(".")[0]

def _parent_of(item: str) -> str:
    parts = item.split(".")
    return ".".join(parts[:2]) if len(parts) > 2 else item

def collect_unmapped(features: list[Feature], parsed_meetings: list[dict],
                     *, sixg_roots: list[str]) -> list[str]:
    """列出 6GR 议程下没有被任何特性归集的议程项。
    只报 6GR 根下的项 —— 第 9 章那类 Rel-20 5G-A 演进不在跟踪范围内，
    除非用户主动为它写了血统段。"""
    roots = set(sixg_roots)
    missing: dict[str, tuple[str, set[str]]] = defaultdict(lambda: ("", set()))

    for parsed in parsed_meetings:
        wg, meeting = parsed["wg"], parsed["meeting"]
        for raw in parsed["events"]:
            item = raw.get("agenda_item")
            if not item or _root_of(item) not in roots:
                continue
            if match_event(features, wg, meeting, item, raw.get("heading_path") or []):
                continue
            parent = _parent_of(item)
            key = f"{wg}:{parent}"
            title, children = missing[key]
            children.add(item)
            missing[key] = (title or raw.get("agenda_title", ""), children)

    out = []
    for key in sorted(missing):
        title, children = missing[key]
        if len(children) > 1:
            out.append(f"{key} ({len(children)} 个子项未归类)")
        else:
            out.append(f"{key} {title}".rstrip())
    return out
```

- [ ] **Step 4: 写按需深挖的失败测试**

```python
# tests/test_fetch_docs.py
import io, zipfile
from unittest.mock import Mock
from ngr.config import WgConfig
from ngr.models import Meeting
from ngr.fetch.docs import fetch_docs

WG = WgConfig(path="tsg_ran/WG1_RL1", dir_re=r"TSGR1_(\d+)([a-z]*)", hard_floor=112,
              agenda_csv_since=124, minutes_re=r"(?i)minutes.*\.(docx|zip)$", artifacts=[])
MTG = Meeting(wg="RAN1", number=127, suffix="",
              url="https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_127/")

def make_zip(name: str, body: bytes) -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        z.writestr(name, body)
    return buf.getvalue()

def docx_bytes(text: str) -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        z.writestr("word/document.xml",
            '<?xml version="1.0"?><w:document '
            'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
            f'<w:body><w:p><w:r><w:t>{text}</w:t></w:r></w:p></w:body></w:document>')
    return buf.getvalue()

def _http(listing_names, files):
    http = Mock()
    base = MTG.url + "Docs/"
    def get(url):
        if url == base:
            return b"".join(f'<a href="{base}{n}">{n}</a>'.encode() for n in listing_names)
        return files[url]
    http.get.side_effect = get
    return http

def test_downloads_only_matching_agenda_items(tmp_path):
    base = MTG.url + "Docs/"
    tdocs = {"R1-2700001.zip": "10.2", "R1-2700002.zip": "10.8"}
    files = {base + n: make_zip(n.replace(".zip", ".docx"), docx_bytes("body"))
             for n in tdocs}
    http = _http(list(tdocs), files)
    got = fetch_docs(http, MTG, WG, agenda_prefix="10.2",
                     out_dir=tmp_path, tdoc_agenda=tdocs)
    assert len(got) == 1 and "R1-2700001" in got[0].name

def test_extracts_text_from_zip(tmp_path):
    base = MTG.url + "Docs/"
    tdocs = {"R1-2700001.zip": "10.2"}
    files = {base + "R1-2700001.zip":
             make_zip("R1-2700001.docx", docx_bytes("Proposal 1 text"))}
    http = _http(list(tdocs), files)
    got = fetch_docs(http, MTG, WG, agenda_prefix="10.2",
                     out_dir=tmp_path, tdoc_agenda=tdocs)
    assert "Proposal 1 text" in got[0].read_text(encoding="utf-8")

def test_skips_already_downloaded(tmp_path):
    base = MTG.url + "Docs/"
    tdocs = {"R1-2700001.zip": "10.2"}
    files = {base + "R1-2700001.zip":
             make_zip("R1-2700001.docx", docx_bytes("x"))}
    fetch_docs(_http(list(tdocs), files), MTG, WG, agenda_prefix="10.2",
               out_dir=tmp_path, tdoc_agenda=tdocs)
    http2 = _http(list(tdocs), files)
    fetch_docs(http2, MTG, WG, agenda_prefix="10.2",
               out_dir=tmp_path, tdoc_agenda=tdocs)
    assert all("R1-2700001.zip" not in c.args[0] for c in http2.get.call_args_list)

def test_returns_empty_when_no_match(tmp_path):
    base = MTG.url + "Docs/"
    tdocs = {"R1-2700001.zip": "10.2"}
    files = {base + "R1-2700001.zip": make_zip("a.docx", docx_bytes("x"))}
    got = fetch_docs(_http(list(tdocs), files), MTG, WG, agenda_prefix="10.9",
                     out_dir=tmp_path, tdoc_agenda=tdocs)
    assert got == []
```

- [ ] **Step 5: 跑测试确认失败**

Run: `.venv/Scripts/python.exe -m pytest tests/test_fetch_docs.py -v`
Expected: FAIL，`No module named 'ngr.fetch.docs'`

- [ ] **Step 6: 写 `ngr/fetch/docs.py`**

```python
from __future__ import annotations
import io, logging, zipfile
from pathlib import Path
from ngr.config import WgConfig
from ngr.fetch.listing import parse_listing
from ngr.models import Meeting
from ngr.parse.docx import parse_docx

log = logging.getLogger(__name__)

def _matches(agenda_item: str | None, prefix: str) -> bool:
    if not agenda_item:
        return False
    return agenda_item == prefix or agenda_item.startswith(prefix + ".")

def fetch_docs(http, meeting: Meeting, cfg: WgConfig, *, agenda_prefix: str,
               out_dir: Path, tdoc_agenda: dict[str, str]) -> list[Path]:
    """按需深挖：只下载指定议程项下的 TDoc 正文，解压抽文本存盘。

    日常定时任务绝不走这条路径 —— 单次 RAN1 会议有 1700+ 个 zip。
    tdoc_agenda 把文件名映射到议程项，由调用方从会议文稿清单构造。
    """
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    docs_url = meeting.url + "Docs/"
    names = parse_listing(http.get(docs_url), docs_url)

    written: list[Path] = []
    for name in names:
        if not _matches(tdoc_agenda.get(name), agenda_prefix):
            continue
        target = out_dir / (name.removesuffix(".zip") + ".txt")
        if target.exists():
            continue
        try:
            blob = http.get(docs_url + name)
            with zipfile.ZipFile(io.BytesIO(blob)) as z:
                docx_names = [n for n in z.namelist() if n.lower().endswith(".docx")]
                if not docx_names:
                    continue
                doc = parse_docx(z.read(docx_names[0]))
            target.write_text("\n".join(doc.paragraphs), encoding="utf-8")
            written.append(target)
        except (zipfile.BadZipFile, KeyError) as exc:
            log.warning("%s 解压失败: %s", name, exc)
    return written
```

- [ ] **Step 7: 接进 CLI 与管线**

在 `ngr/cli.py` 里加子命令：

```python
    p_docs = sub.add_parser("fetch-docs", help="按需深挖：下载指定议程项的 TDoc 正文")
    p_docs.add_argument("--wg", required=True)
    p_docs.add_argument("--meeting", type=int, required=True)
    p_docs.add_argument("--agenda", required=True, help="议程项前缀，如 10.2")
```

在 `main()` 的分支里加：

```python
        elif args.cmd == "fetch-docs":
            from ngr.pipeline import run_fetch_docs
            n = run_fetch_docs(wg=args.wg, meeting=args.meeting, agenda=args.agenda)
            logging.info("已下载 %d 篇文稿正文", n)
            return EXIT_OK
```

在 `ngr/pipeline.py` 末尾加：

```python
def run_fetch_docs(*, wg: str, meeting: int, agenda: str) -> int:
    """从已抓取的 docs_listing.html 取文件名，按议程项过滤后下载正文。

    议程项映射来自纪要里每篇文稿的归属；当前实现按 TDoc 号在纪要正文中
    出现的位置推断其议程项 —— 这对深挖场景足够，不追求 100% 准确。
    """
    from ngr.fetch.docs import fetch_docs
    cfg = load_sources()
    wgcfg = cfg.wgs[wg]
    http = Http(cfg.http)
    mtg = next(m for m in discover_meetings(http, wg, wgcfg) if m.number == meeting)

    payload = _load_json(P.parsed_dir(wg, meeting) / "events.json", {})
    tdoc_agenda: dict[str, str] = {}
    for ev in payload.get("events", []):
        item = ev.get("agenda_item")
        if not item:
            continue
        for token in ev["text_en"].split():
            token = token.strip("(),.;:[]")
            if token.startswith(("R1-", "R2-", "R3-", "R4-")):
                tdoc_agenda.setdefault(token + ".zip", item)

    written = fetch_docs(http, mtg, wgcfg, agenda_prefix=agenda,
                         out_dir=P.raw_dir(wg, meeting) / "docs",
                         tdoc_agenda=tdoc_agenda)
    return len(written)
```

在 `run_pipeline` 的渲染调用前加入未归类收集：

```python
    from ngr.mapping.unmapped import collect_unmapped
    parsed_all = [_load_json(p, {}) for p in sorted(P.parsed.rglob("events.json"))]
    sixg_roots = ["10"]        # 与 features.yaml 中 6G 段的议程根一致
    unmapped = collect_unmapped(features, [p for p in parsed_all if p], sixg_roots=sixg_roots)
```

并把 `unmapped=unmapped` 传给 `render_all`（`run_pipeline_remap` 里同样处理）。

- [ ] **Step 8: 跑测试确认通过**

Run: `.venv/Scripts/python.exe -m pytest tests/test_mapping_unmapped.py tests/test_fetch_docs.py -v`
Expected: 10 passed

- [ ] **Step 9: 跑全部测试**

Run: `.venv/Scripts/python.exe -m pytest -v`
Expected: 全绿

- [ ] **Step 10: 验证未归类清单真的出现在看板上**

```bash
.venv/Scripts/python.exe -m ngr remap
```

打开 `out/dashboard.md`，应能看到「⚠️ 待归类议程项」一节，列出 6GR 议程下你还没写进 `features.yaml` 的议题（如 NTN、WUS、多载波等）。逐个决定加不加特性，加完 `ngr remap` 重看。

- [ ] **Step 11: Commit**

```bash
git add ngr/mapping/unmapped.py ngr/fetch/docs.py ngr/cli.py ngr/pipeline.py tests/test_mapping_unmapped.py tests/test_fetch_docs.py
git commit -m "feat: 未归类议程项收集与按需深挖命令"
```

---

## 计划自检结论

**spec 覆盖**：§1–§10 全部有对应任务。§3.3 `unmapped_policy` 与 §4 按需深挖由 Task 22 补齐（首次自检时发现的缺口）。

**一个贯穿全程的约束**（spec §6.3 优化 3，实现时别丢）：`extract` 阶段必须在单次进程内连续跑完，落在同一个 1 小时 ephemeral 缓存窗口里 —— 每次 `claude -p` 有约 16K token 的固定开销，跨窗口跑就是重复付。`run_pipeline` 与 `run_pipeline_enrich` 天然满足；**不要把 extract 拆成多次独立调用**。

**任务依赖链**：1 → 2 → 3 →（4 → 5 → 6）→（7 → 8 → 9 → 10 → 11）→（12 → 13）→（14 → 15）→（16 → 17 → 18）→（19 → 20）→ 21 → 22。括号内为同一 Phase，需顺序执行。

**两个可交付里程碑**：Task 13（事件入库）、Task 15（看板可读，工具已有用）。

