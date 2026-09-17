# 6G (Rel-20) RAN 协议进展跟踪工具 — 设计文档

- 日期：2026-09-17
- 状态：设计已确认，待转实现计划
- 项目根：`D:\Project\NGR_Spec`

## 1. 目标与范围

自动定期跟踪 3GPP 6G (Rel-20 起) RAN 侧协议进展，产出两类互补的东西：

1. **特性状态看板** —— 以特性为主键的持续演进状态，回答"这个特性定到哪一步了、是怎么一步步定成这样的"。
2. **会议增量简报** —— 每次会议后的"发生了什么"，回答"这次比上次多了什么"。

**范围**：TSG RAN plenary + RAN1 / RAN2 / RAN3 / RAN4，Rel-20 起的 6G 相关议程。

**不在范围**：5G-A（Rel-19/20 的非 6G 部分）、SA/CT 各组、RAN5。

**非目标**（明确不做，避免范围蔓延）：

- 不做全量 TDoc 语料库与向量检索（深挖走按需命令）。
- 不做公司立场分析、投票统计。
- 不做多用户、不做 Web 服务、不做数据库。

## 2. 关键约束（实测确认，2026-09-17）

这些是设计的事实基础，不是假设：

| 项 | 实测结果 |
|---|---|
| 站点访问 | 默认 curl UA 返回 **403**（WAF）；带浏览器 UA 返回 200。必须伪装 UA |
| 目录结构 | `www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_<n>/{Agenda,Docs,Inbox,Invitation,LS,Report}`，纯 HTML 目录列表 |
| 议程骨架 | `Agenda/agenda.csv`，格式 `"10","Rel-20 Study of 6GR"` / `"10.2","Waveform for 6GR air interface"`，2.9 KB |
| 纪要 | `Report/Draft_Minutes_report_RAN1#126_v010.docx`，968 KB，下载耗时约 2 s |
| 纪要内容 | 7803 段、83 个 heading、**320 Agreement / 29 Conclusion / 13 Working Assumption** |
| 文稿量 | RAN1#126 `Docs/` 有 1736 个 zip；目录列表 2 MB / 2.7 s |
| 当前进度 | RAN1 至 #127，TSG RAN plenary 至 #114；6G 术语为 **"6GR"** |
| 议程号 | 纪要标题是 Word **自动编号**，正文取不到议程号 → 必须靠 `agenda.csv` 标题文本对齐 |
| 纪要版本 | 存在 v010 → v100 演进，高版本出现时须整场重解析 |
| `claude -p` 固定开销 | 单次调用约 **16,337** cache-creation token；建 1 小时 ephemeral 缓存，连续调用降为 ~1,400 create + ~14,936 read（$0.066 → $0.0095） |
| 认证 | **`--bare` 不可用** —— 该模式只认 `ANTHROPIC_API_KEY`/apiKeyHelper，不读 OAuth，会绕开 Max 订阅认证 |

**用户环境约束**：只有 Claude Max 订阅，**无 Anthropic API 账户**。所有 LLM 调用必须走 `claude -p` CLI（消耗订阅额度），不走 API SDK。

## 3. 架构：分层增量管线

四层，层间只通过落盘的 JSON 通信，每层可独立重跑：

```
fetch    远端字节 → data/raw/        （唯一联网的层）
parse    data/raw/ → data/parsed/    （纯函数，无网络无 LLM）
extract  data/parsed/ → data/state/  （唯一调 LLM 的层）
render   data/state/ → out/          （纯渲染）
```

选择理由：本项目的真实成本不在首次实现，而在 3GPP 改目录命名／换纪要模板后修改解析器。分层落盘让解析逻辑能在本地缓存上离线秒级重跑，而单体管线每次改动都要重新联网并重新消耗 LLM 额度。

### 3.1 仓库布局

```
D:\Project\NGR_Spec\
├─ ngr/
│   ├─ fetch/  parse/  extract/  render/  cli.py
├─ config/
│   ├─ sources.yaml        # 抓哪些组、从哪次会议起、每组抓哪些文件
│   └─ features.yaml       # 人工维护的特性词典
├─ data/
│   ├─ raw/                # 原始字节镜像             —— 不进 git
│   ├─ parsed/             # 解析产物 JSON（可重建）   —— 不进 git
│   └─ state/              # 事实库                   —— 进 git
│       ├─ meetings.json  events.json  specs.json  tdocs.json
│       ├─ features_state.json      # 每特性的 stage / open_issues / 综述正文
│       ├─ llm_cache/<sha256>.json
│       ├─ usage_log.jsonl  run_history.json
├─ out/                    # 进 git
│   ├─ dashboard.md  ALERTS.md
│   ├─ features/<slug>.md
│   ├─ reports/YYYY-MM-DD-<WG>-<n>.md
│   └─ site/index.html
├─ logs/                   # 不进 git
├─ tests/fixtures/RAN1_126/
└─ docs/superpowers/specs/
```

### 3.2 核心数据模型

`state/events.json` 为主表：

```jsonc
{ "id": "RAN1-126-10.2-a017",
  "wg": "RAN1", "meeting": 126, "meeting_end": "2026-08-21",
  "agenda_item": "10.2",
  "agenda_title": "Waveform for 6GR air interface",
  "kind": "agreement",
  "text_en": "…原文逐字，含表格转 Markdown…",
  "source": { "file": "Draft_Minutes_report_RAN1#126_v010.docx",
              "minutes_version": "v010", "para": 4417, "url": "https://…" },
  "feature": "waveform",
  "summary_zh": "…", "tags": ["OFDM","PAPR"], "impact": "high",
  "llm_status": "ok",
  "first_seen": "2026-08-25", "content_hash": "sha256:…" }
```

设计取舍：

1. **`text_en` 逐字保留，永不让 LLM 改写。** LLM 只产出 `summary_zh` / `tags` / `impact`。协议 agreement 的价值在措辞本身；摘要是索引，不是事实来源。
2. **主键用「会议+议程项+序号」，不用文本哈希。** 纪要版本演进时同一条 agreement 措辞可能微调，文本哈希会误判为新条目。`content_hash` 单独存，用于触发"此条已变更"。
3. **`raw`/`parsed` 不进 git，`state`/`out` 进。** `git diff state/events.json` 即"这次新增了哪几条 agreement"。

### 3.3 特性词典 `config/features.yaml`

```yaml
features:
  - slug: waveform
    name_zh: 6GR 波形与帧结构
    match:
      agenda: ["RAN1:10.2", "RAN1:10.2.*"]   # 主锚点
      title_re: "(?i)waveform|numerolog"      # 兜底
      wi_code: ["FS_6GR_AI"]
  - slug: channel_coding
    name_zh: 6GR 信道编码与调制
    match:
      agenda: ["RAN1:10.3", "RAN1:10.3.*"]
      title_re: "(?i)channel coding|modulation"
unmapped_policy: report
```

**特性归类由规则决定，不由 LLM 决定。** 议程号匹配上即确定性赋值；归类漂移会毁掉跨会议纵向对齐。未映射的 6G 议程项进报告"待归类"清单，LLM 可给建议，但不自动落库。

## 4. fetch 层

单一职责：把远端字节原样搬到 `data/raw/`，不解析、不判断内容。

```python
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36")
CONCURRENCY = 2
DELAY = 0.5          # 秒
RETRY = [2, 8, 30]   # 退避；403/429 视为限流
TIMEOUT = (10, 300)  # 连接 / 读取
```

**发现**：从 WG 根目录列表正则提取会议目录（`TSGR1_(\d+)([a-z]*)`），与 `sources.yaml` 的 `since` 比对，新会议自动纳入。

**每次会议固定抓**：`Agenda/agenda.csv`、`Report/` 下最新版本的 Minutes docx、`Docs/` 目录列表、`LS/` 目录列表。合计每会几 MB。

**增量判定**：`data/raw/<wg>/<mtg>/_manifest.json` 记 `{url, etag, content_length, sha256, fetched_at}`。先 HEAD，ETag 或 Content-Length 变化才 GET。

**纪要版本**：文件名抽 `v(\d{3})`，出现更高版本则重抓并触发该会议全量重解析。

**按需深挖**：`ngr fetch-docs --wg RAN1 --meeting 127 --agenda 10.2` 才下载 TDoc zip，按议程项过滤，解压抽文本存 `raw/.../docs/`。日常定时任务绝不触发此路径。

**每组独立配置**（`config/sources.yaml`）：

```yaml
sources:
  RAN1:
    path: tsg_ran/WG1_RL1
    dir_re: 'TSGR1_(\d+)([a-z]*)'
    since: 120
    artifacts: [agenda_csv, minutes_docx, docs_listing, ls_listing]
    sixg_agenda_roots: ["10"]
  RAN2: { path: tsg_ran/WG2_RL2, dir_re: 'TSGR2_(\d+)([a-z]*)', since: 130, artifacts: [...] }
  RAN3: { path: tsg_ran/WG3_Iu,  dir_re: 'TSGR3_(\d+)([a-z]*)', since: 130, artifacts: [...] }
  RAN4: { path: tsg_ran/WG4_Radio, dir_re: 'TSGR4_(\d+)([a-z]*)', since: 116, artifacts: [...] }
  RANP: { path: tsg_ran/TSG_RAN, dir_re: 'TSGR_(\d+)([a-z]*)', since: 108, artifacts: [...] }
```

**未验证项**：仅 RAN1 经过实测。RAN2/3/4 路径与 plenary 结构须在实现第一步探明后填实（含 `WG3_Iu` / `WG4_Radio` 等目录名；plenary 的关键产物是批准的 WID/SID 与状态表，而非 agreement）。

## 5. parse 层

纯函数，输入 `data/raw/` 字节，输出 `data/parsed/` JSON。

三个解析器：

- `agenda_csv.py` → `{item, depth, title}`，`depth = item.count(".") + 1`
- `docs_listing.py` → `[{tdoc, filename, size, url}]`
- `minutes_docx.py` → 主力：`zipfile` 读 `word/document.xml`，逐 `<w:p>` 抽 `<w:pStyle>` + `<w:t>`

### 5.1 议程号对齐

纪要标题无议程号（Word 自动编号）。对齐算法：标题归一化（小写、去标点、压空白）→ 精确匹配 → 失败退到 `difflib` 相似度 ≥ 0.9 → 用 heading 层级与议程号深度互校（`Heading2` ↔ `10.2` 深度 2）。三者均通过才落库；不通过进 `unaligned` 清单并在报告中显式列出。**宁可少归类，不可错归类。**

### 5.2 Agreement 块提取

Agreement 是块不是行。从标记段（`Agreement` / `Conclusion` / `Working assumption` / `Observation` / `Proposal`）起，吃到下一个标记或下一个 heading 为止。`<w:tbl>` 转 Markdown 表格嵌入 `text_en` —— 波形、编码类议题的大量结论就在表里，丢了表等于丢了结论。

### 5.3 6G 过滤

从 `sources.yaml` 的 `sixg_agenda_roots`（RAN1 当前为 `"10"`，对应 "Rel-20 Study of 6GR"）整棵子树取事件，其余议程项丢弃。按会议可配，因议程号会随版本漂移。

### 5.4 沉默失败防线

每次解析强制断言，任一不满足即**报错退出、保留 raw、不写 state**：

- heading 数 > 0
- 6G 子树存在
- 事件数 > 0
- 未对齐议程项占比 < 20%

理由：3GPP 换纪要模板时解析器会安静返回 0 条，而定时任务照常"成功"，数月后才被发现。

## 6. extract 层（LLM）

**后端唯一为 `cli`**（另加 `none`）。不实现 API SDK 后端。

### 6.1 调用方式

```python
CMD = ["claude", "-p", "--output-format", "json",
       "--model", "sonnet",           # 批量摘要 sonnet；简报/综述 opus
       "--effort", "low",             # 批量 low；简报/综述 high
       "--restricted",                # 去掉 Bash/PowerShell/REPL
       "--disable-slash-commands"]    # 关闭 skills，避免干扰批处理
```

- **prompt 走 stdin，不走 argv** —— Windows 命令行上限约 32K，一批 40 条 agreement 远超。
- **禁用 `--bare`** —— 见 §2，会绕开 OAuth 订阅认证。

### 6.2 四项任务

| 任务 | 触发 | 输入 | 输出 | 模型/effort |
|---|---|---|---|---|
| ① 事件摘要 | 每条新增/变更 event | `text_en` + 议程标题 | `summary_zh`(2–3 句)、`tags`、`impact` | sonnet / low |
| ② 会议简报 | 每次会议解析完 | 该会议全部 event 的**摘要** | `reports/….md` 正文 | opus / high |
| ③ 特性综述 | 该特性有新事件 | 该特性全部历史 event | `features/<slug>.md` 顶部"当前进展" + `stage` + `open_issues` | opus / high |
| ④ 候选归类建议 | 存在未映射 6G 议程项 | 议程标题 | 建议 slug（**仅写入报告，不落库**） | sonnet / low |

**枚举值定死，不许自由发挥**（写进 prompt 并在解析时校验，不合法即视为 JSON 校验失败走重试）：

- `impact`：`high` | `medium` | `low` —— 对协议走向的影响程度。
- `stage`：`未启动` | `讨论中` | `收敛中` | `已定稿` —— 特性当前所处阶段，由任务 ③ 判定并写入 `state/features_state.json`。这是看板"阶段"列的唯一来源。
- `open_issues`：字符串数组，该特性尚未解决的争议点，对应看板"未决"列的计数。

`stage` 是全设计中**唯一由 LLM 判定的结构化字段**（归类仍归规则），因为它本质是对一段历史的判断，没有可靠的机器规则。它随每次综述重算，历史值可从 `git log` 回溯。

### 6.3 针对 16K 固定开销的三条优化

1. **一批 40 条事件**（非 15 条），靠大批量摊薄固定开销；批量上限由输出质量决定，不由输入长度决定。
2. **简报只吃摘要不吃原文** —— 250 条事件原文约 150K token，其摘要仅约 37K。
3. **extract 阶段必须连续跑完**，落在同一个 1 小时 ephemeral 缓存窗口内，16K 开销只付一次。

### 6.4 用量预算

回填（1000 条事件 / 8 次会议 / 15 个特性）：

| 环节 | 调用数 | 输入 | 输出 | list 等价 |
|---|---|---|---|---|
| 摘要（40 条/批，sonnet） | ~25 | ~1.0 M | ~150 K | ~$3 |
| 会议简报（opus，吃摘要） | 8 | ~430 K | ~24 K | ~$2 |
| 特性综述（opus） | ~15 | ~540 K | ~22 K | ~$2.3 |
| 合计 | ~48 | ~2.0 M | ~200 K | **≈ $7–8** |

日常增量：绝大多数日子 0 次调用；纪要上传后的几天约 10–15 次调用。

`total_cost_usd` 在订阅模式下是**按 list price 折算的用量代理值，非账单**。每次调用的 token 与该值记入 `state/usage_log.jsonl`。

### 6.5 四道防线

1. **缓存键 = `sha256(model + prompt_version + effort + text_en)`**，存 `state/llm_cache/`，进 git。改 prompt 自动失效重算；不改则永不重复消耗额度，换机器亦可复用。
2. **幻觉拦截**：`summary_zh` 中出现的 TDoc 编号、数字、公司名若不在 `text_en` 中出现，该条标红进"待人工核对"。
3. **LLM 失败不阻断管线**：JSON 解析失败重试一次（附错误信息要求修正），再失败则 `summary_zh` 留空、标 `llm_status: failed`，**事件本身照常入库**，下次运行自动重试。摘要可以缺，agreement 不能丢。
4. **`--no-llm` 模式**：不调 LLM 也产出完整看板（仅无中文摘要）。

## 7. render 层与发布

只读 `state/`，不联网、不调 LLM。四个产物：

1. **`out/dashboard.md`** —— 特性状态总表、本期新增摘要、待归类议程项清单、顶部告警横幅。总表各列定义：
   - **阶段** ← `features_state.json` 的 `stage`（§6.2 枚举值）
   - **累计 Agr.** ← 该特性全部历史 `kind == "agreement"` 事件数
   - **本期新增** ← **最近一次已解析会议**中该特性的新增事件数（口径是"最近一次会议"，不是"上次运行以来"—— 后者会因运行频率变化而抖动）
   - **最近活动** ← 该特性最后一次出现事件的会议号
   - **未决** ← `open_issues` 数组长度
2. **`out/features/<slug>.md`** —— 顶部为 LLM 生成的"当前进展"综述，下方按会议倒序列出全部事件，每条含中文摘要 + 英文原文 + 原文链接。**本工具最有价值的一页。**
3. **`out/reports/YYYY-MM-DD-<WG>-<n>.md`** —— 单次会议增量简报，按特性分组，末尾附未归类项与解析警告。
4. **`out/site/index.html`** —— 单文件自包含看板，JSON 内联，无构建步骤、无外部依赖、`file://` 可开。面板：特性状态表（按工作组／时间筛选）、特性 × 会议活动热力图、事件可展开看原文。图表形式与配色在实现时遵循 dataviz 规范确定。

**发布约束**：Python 脚本无法将网页发布为 Artifact —— 发布是 Claude Code 会话内的工具调用。因此：

- `ngr render`（脚本，定时跑）产出 `out/site/index.html` 并进 git —— **永远自动完成**。
- 发布为可分享链接 —— **永远需要用户在会话中显式要求**，由 Claude 读取该文件发布，后续更新发到同一 URL。

**git 策略**：`ngr run` 结束后自动 `git add state/ out/ && git commit`，提交信息为自动生成的变更摘要，例如：

```
RAN1#127: +23 agreements (waveform +9, coding +7, ISAC +5, 未归类 +2)
```

**不自动 push** —— 推到哪个远端、要不要推，由用户决定。

## 8. 调度与错误处理

### 8.1 命令面（`ngr` = `python -m ngr`）

| 命令 | 作用 |
|---|---|
| `ngr run` | fetch → parse → extract → render → commit |
| `ngr run --no-llm` | 跳过 extract，零额度消耗 |
| `ngr backfill --wg RAN1 --from 120 --to 127` | 回填历史，按会议逐个提交，可中断续跑 |
| `ngr fetch-docs --wg RAN1 --meeting 127 --agenda 10.2` | 按需深挖 |
| `ngr enrich` | 只补跑 extract |
| `ngr doctor` | 自检：claude CLI、认证、3GPP 可达性、配置合法性、git 状态 |

### 8.2 节奏

```
每日 07:00  ngr run
```

RAN1 每约两个月开一次会，全年约 12 个会议周期 —— 一年中有新内容的不足 20 天。绝大多数日子仅发若干 HEAD 请求后秒退，LLM 调用数为 0。单次 `ngr run` 内部连续执行，天然满足 §6.3 的缓存窗口约束。

**`max_calls_per_run` 的计数口径**（默认 60）：按**单次进程调用**计，不按会议计。`ngr run` 用满即停，剩余队列留给次日；`ngr backfill` 处理完一个会议就检查一次，超限则在会议边界干净退出（已完成会议已 commit），重跑自动续上 —— 因此回填 8 次会议约需 1–2 次 `backfill` 调用，而非一次跑完。

```powershell
schtasks /Create /TN "NGR_Spec" /SC DAILY /ST 07:00 /RL LIMITED `
  /TR "powershell -NoProfile -WindowStyle Hidden -Command `"cd D:\Project\NGR_Spec; .venv\Scripts\python.exe -m ngr run`""
```

实现阶段提供 `scripts/install-task.ps1` 一键注册。

### 8.3 错误分类

| 失败 | 处理 | 退出码 |
|---|---|---|
| 网络超时 / 403 | 退避重试 3 次；仍失败则跳过该源，其余源继续 | 0 |
| **解析断言失败** | 硬失败：保留 raw、不写 state、不 commit | 2 |
| LLM 限流 / 认证失效 | 已完成的落库，队列留存，干净退出 | 3 |
| `max_calls_per_run` 用尽 | 正常结束，dashboard 标"还有 N 条待摘要" | 0 |
| git 有未提交的手工改动 | 不自动 commit，报警退出（绝不覆盖手改的 `features.yaml`） | 4 |

### 8.4 失败可见性

静默失败是此类工具最典型的死法。三重可见性：

1. `out/ALERTS.md` —— 有告警即写入，无则为空文件。
2. **`dashboard.md` 顶部横幅** —— 每日必看的一页，问题在第一行。
3. `logs/ngr-YYYY-MM-DD.log` + `state/run_history.json`（时间、耗时、新增事件数、LLM 调用数、退出码）。

**心跳检查**：`run_history` 显示连续 7 天无成功运行时，dashboard 横幅报"调度可能已失效"。这样即使计划任务被 Windows 停掉，打开看板也能立刻发现。

### 8.5 幂等性

同一份 `data/raw` 跑两遍，`state/` 必须逐字节相同。这是回归测试的基础：改完解析器重跑，`git diff state/` 应只显示预期变化。

## 9. 测试策略

原则：**真实 fixture 离线跑，测试中绝不联网、绝不调 LLM。**

`tests/fixtures/RAN1_126/` 存入实测抓取的 `agenda.csv`(2.9 KB)、`Draft_Minutes_report_RAN1#126_v010.docx`(968 KB)、`docs_listing.html`(裁至前 50 条)。

| 层 | 方法 | 重点 |
|---|---|---|
| `fetch` | mock HTTP | UA、403 退避、HEAD 增量判定、manifest 读写、纪要版本比较 |
| **`parse`** | **真实 fixture + golden file** | **主战场，走 TDD** |
| `extract` | stub `claude` 子进程 | JSON 解析、畸形输出修复重试、失败标记、批次切分、调用上限、限流优雅退出 |
| `render` | snapshot | Markdown／HTML 输出快照 |
| 端到端 | fixture 会议全流程 `--no-llm` | 各层接口契合 |

parse 层断言直接写死实测数字：

```python
def test_ran1_126_minutes_structure():
    doc = parse_minutes(FIXTURE / "Draft_Minutes_report_RAN1#126_v010.docx")
    assert len(doc.paragraphs) == 7803
    assert len(doc.headings) == 83
    assert count(doc, kind="agreement") == 320
    assert count(doc, kind="conclusion") == 29
    assert count(doc, kind="working_assumption") == 13

def test_agenda_alignment():
    aligned = align(parse_agenda(FIXTURE / "agenda.csv"), doc.headings)
    assert aligned["10"].title == "Rel-20 Study of 6GR"
    assert aligned["10.2"].title == "Waveform for 6GR air interface"
    assert aligned.unmatched_ratio < 0.20
```

3GPP 换模板时这几行会第一个失败，而不是等半年后发现看板空了。

LLM 相关测试一律用桩，覆盖畸形 JSON、限流错误、超时 —— 测的是"我们如何应对 LLM 的不靠谱"。真实输出质量由人查看 `out/` 判断。

**不做**：覆盖率指标；Markdown 措辞测试；联网集成测试（每日 `ngr run` 的解析断言即最好的线上契约检查）。

## 10. 实现阶段的第一件事

**先探明 RAN2 / RAN3 / RAN4 与 TSG RAN plenary 的实际目录布局并填实 `sources.yaml`，再写代码。** §4 中这些路径为假设值，仅 RAN1 经实测确认。先写代码后撞墙的代价高于先探明。
