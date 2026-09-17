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

<!-- APPEND-HERE -->
