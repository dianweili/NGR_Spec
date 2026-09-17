# 6G (Rel-20) RAN 协议进展跟踪工具 — 设计文档

- 日期：2026-09-17
- 状态：设计已确认，待转实现计划
- 项目根：`D:\Project\NGR_Spec`

## 1. 目标与范围

自动定期跟踪 3GPP 6G (Rel-20 起) RAN 侧协议进展，产出两类互补的东西：

1. **特性状态看板** —— 以特性为主键的持续演进状态，回答"这个特性定到哪一步了、是怎么一步步定成这样的"。
2. **会议增量简报** —— 每次会议后的"发生了什么"，回答"这次比上次多了什么"。

**范围**：TSG RAN plenary + RAN1 / RAN2 / RAN3 / RAN4 中：

1. **6GR 议程**（RAN1 当前为第 10 章 "Rel-20 Study of 6GR"）的全部内容；
2. **各特性自行声明的 5G-A 血统段** —— 部分 6G 特性是 5G-A 中未做充分的议题的延续（ISAC、AI/ML 空口、MIMO、NTN、省电/WUS 等），对这些特性要从 5G-A 源头开始跟踪，而不是从 6G 立项开始。

⚠️ **"Rel-20" 不等于 "6G"。** RAN1 #126 议程实测显示第 9 章 `Release 20 NR`（AI/ML 空口增强、MIMO Phase 6、Ambient IoT Ph2、GNSS resilient NTN）与第 10 章 `Rel-20 Study of 6GR` **并列存在** —— 前者是 Rel-20 里的 5G-A 演进，不是 6GR。因此范围不能用 release 号界定，只能用**议程锚点 + 特性血统**界定。

**不在范围**：与 6G 无血统关系的 5G-A 议题、SA/CT 各组、RAN5。

**哪些特性算"延续"由人判断**，写在 `config/features.yaml` 的 `lineage` 中，工具不替用户猜。

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
| **议程锚点的时间边界** | `agenda.csv` 实测 **#124/#125/#126 存在，#120 不存在**（其 `Agenda/` 目录下只有 TDoc zip）；#122 返回 403，无法区分缺文件与限流。**5G-A 历史段没有机读议程锚点** |
| **Rel-20 ≠ 6G** | RAN1 #126 议程第 9 章 `Release 20 NR`（5G-A 演进）与第 10 章 `Rel-20 Study of 6GR` 并列 |
| **403 语义歧义** | WAF 限流与文件缺失**都返回 403**。fetch 层不得用 GET 状态码判断文件是否存在，必须先读目录列表再取 |
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
parse    data/raw/ → data/parsed/    （纯函数，全量解析，不筛选）
map      data/parsed/ → data/state/  （纯规则，按血统筛选，无 LLM）
extract  data/state/ 就地增补        （唯一调 LLM 的层，只处理 depth=full）
render   data/state/ → out/          （纯渲染）
```

选择理由：本项目的真实成本不在首次实现，而在 3GPP 改目录命名／换纪要模板后修改解析器。分层落盘让解析逻辑能在本地缓存上离线秒级重跑，而单体管线每次改动都要重新联网并重新消耗 LLM 额度。

### 3.1 仓库布局

```
D:\Project\NGR_Spec\
├─ ngr/
│   ├─ fetch/  parse/  map/  extract/  render/  cli.py
├─ config/
│   ├─ sources.yaml        # 抓哪些组、每组抓哪些文件、回溯硬下限
│   └─ features.yaml       # 人工维护的特性词典（含跨时代血统）
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
├─ tests/fixtures/RAN1_126/   # 6GR 时代（有 agenda.csv）
├─ tests/fixtures/RAN1_120/   # 5G-A 时代（无 agenda.csv，靠 title_re）
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
  "era": "6G", "release": "Rel-20", "depth": "full",   // 由命中的血统段决定
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

### 3.3 特性词典 `config/features.yaml`（血统模型）

特性不是单一议程锚点，而是一串**跨时代的血统段（lineage segment）**。每段声明：所属时代、release、议程锚点、会议区间、处理深度。

```yaml
features:
  # —— 纯 6G 出身，无 5G-A 血统 ——
  - slug: waveform
    name_zh: 6GR 波形与帧结构
    lineage:
      - era: 6G
        release: Rel-20
        anchor: { agenda: ["RAN1:10.2", "RAN1:10.2.*"], title_re: "(?i)waveform|numerolog" }
        meetings: { RAN1: [124, null] }        # null = 至今
        depth: full

  # —— 有 5G-A 血统，从源头跟起 ——
  - slug: isac
    name_zh: ISAC 通感一体
    lineage:
      - era: 5G-A
        release: Rel-19
        anchor: { title_re: "(?i)(channel model.{0,30}(sensing|ISAC))|ISAC|integrated sensing" }
        meetings: { RAN1: [116, 126] }         # 无 agenda.csv，只能靠标题正则
        depth: origin
      - era: 6G
        release: Rel-20
        anchor: { agenda: ["RAN1:10.8", "RAN1:10.8.*"], title_re: "(?i)ISAC|sensing" }
        meetings: { RAN1: [124, null] }
        depth: full

  - slug: ai_air_interface
    name_zh: AI/ML 空口 → 6GR AI-native
    lineage:
      - { era: 5G-A, release: Rel-18, anchor: { title_re: "(?i)AI/ML for NR air interface" },
          meetings: { RAN1: [112, 120] }, depth: origin }
      - { era: 5G-A, release: Rel-19, anchor: { agenda: ["RAN1:9.1", "RAN1:9.1.*"],
          title_re: "(?i)(AI|artificial intelligence).{0,40}air interface" },
          meetings: { RAN1: [116, null] }, depth: origin }
      - { era: 6G, release: Rel-20, anchor: { agenda: ["RAN1:10.*"], title_re: "(?i)AI.native|AI/ML" },
          meetings: { RAN1: [124, null] }, depth: full }

unmapped_policy: report
default_depth: origin      # lineage 段未写 depth 时的默认值
```

**血统段重叠是允许且正常的** —— 同一次会议可能同时有 Rel-19 的 9.1 和 Rel-20 的 10.x 两段命中。事件按各自命中的段记录 `era`/`release`/`depth`，不去重、不合并。

**处理深度 `depth` 三档：**

| 值 | 含义 |
|---|---|
| `full` | 全量入库 + 逐条中文摘要 / tags / impact。**6GR 段一律 `full`** |
| `origin` | 全量入库 + 保留英文原文与原文链接，**不逐条摘要**；由特性综述统一概括该段脉络。**5G-A 血统段默认值** |
| `milestone` | 仅入库 WI/SI 立项、`Conclusion`、`Working assumption` 等转折点，普通 agreement 不入库 |

**特性归类由规则决定，不由 LLM 决定。** 议程号或标题正则匹配上即确定性赋值；归类漂移会毁掉跨会议纵向对齐。未映射的 6GR 议程项进报告"待归类"清单，LLM 可给建议，但不自动落库。

**5G-A 段的锚定精度低一档，靠人工校准补偿。** 老会议无 `agenda.csv`，只能用 `title_re` 匹配纪要 heading 文本。缓解手段：Rel-18/19 已冻结，**历史是静态的，校准一次永久有效**。因此 `ngr backfill` 结束后必须打印**血统命中对照表**（每段命中了哪些 heading、各多少条事件），供人工核对；调完正则后重跑映射的成本为零（§5.3）。

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

**发现**：从 WG 根目录列表正则提取会议目录（`TSGR1_(\d+)([a-z]*)`），新会议自动纳入。

**抓取区间 = 血统段的并集，不是单一起点。** 每个工作组要抓的会议范围由 `features.yaml` 中所有 lineage 段该组的 `meetings` 区间取并集得出。`sources.yaml` 只保留 `hard_floor` 作为**硬下限**，防止血统配置写错导致回溯到 2018 年；取值为各组的 Rel-18 起始会议（实现第一步核实，见 §10）。

**每次会议固定抓**：`Agenda/agenda.csv`（**存在才抓** —— 见下）、`Report/` 下最新版本的 Minutes docx、`Docs/` 目录列表、`LS/` 目录列表。合计每会几 MB。

**403 歧义的处理（§2）**：WAF 限流与文件缺失都返回 403，因此**不得用 GET 状态码判断文件是否存在**。流程固定为：先取目录列表 → 在列表中确认目标文件名存在 → 再 GET。目录列表本身若返回 403，一律按**限流**处理（退避重试），绝不当作"这个会议没有数据"而静默跳过 —— 后者会导致血统段出现无声的空洞。

**增量判定**：`data/raw/<wg>/<mtg>/_manifest.json` 记 `{url, etag, content_length, sha256, fetched_at}`。先 HEAD，ETag 或 Content-Length 变化才 GET。

**已冻结会议免检**：Rel-18/19 的历史会议纪要不会再变。manifest 中标记 `frozen: true` 的会议在日常 `ngr run` 中完全跳过（连 HEAD 都不发）。这让 5G-A 血统的加入**不增加任何日常运行开销** —— 回填一次之后，每天照常只检查最近几次会议。冻结判定：会议号 < 当前最新会议号 - 2 且已成功解析过。

**纪要版本**：文件名抽 `v(\d{3})`，出现更高版本则重抓并触发该会议全量重解析。

**按需深挖**：`ngr fetch-docs --wg RAN1 --meeting 127 --agenda 10.2` 才下载 TDoc zip，按议程项过滤，解压抽文本存 `raw/.../docs/`。日常定时任务绝不触发此路径。

**每组独立配置**（`config/sources.yaml`）：

```yaml
sources:
  RAN1:
    path: tsg_ran/WG1_RL1
    dir_re: 'TSGR1_(\d+)([a-z]*)'
    hard_floor: 112        # 硬下限：血统段再怎么写也不回溯到此之前
    artifacts: [agenda_csv, minutes_docx, docs_listing, ls_listing]
    agenda_csv_since: 124  # 此会议号起才有 agenda.csv；之前退到 title_re 锚定（§2，待实测确认）
  RAN2: { path: tsg_ran/WG2_RL2, dir_re: 'TSGR2_(\d+)([a-z]*)', hard_floor: 121, artifacts: [...] }
  RAN3: { path: tsg_ran/WG3_Iu,  dir_re: 'TSGR3_(\d+)([a-z]*)', hard_floor: 118, artifacts: [...] }
  RAN4: { path: tsg_ran/WG4_Radio, dir_re: 'TSGR4_(\d+)([a-z]*)', hard_floor: 106, artifacts: [...] }
  RANP: { path: tsg_ran/TSG_RAN, dir_re: 'TSGR_(\d+)([a-z]*)', hard_floor: 99, artifacts: [...] }
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

### 5.3 解析存全量，筛选在映射层

**parse 不做特性筛选。** `data/parsed/<wg>/<mtg>/events.json` 存该次会议**全部**事件（RAN1#126 约 362 条：320 Agreement + 29 Conclusion + 13 WA），带议程项与 heading 路径，不进 git。

随后独立的 **map 步骤**（`ngr/extract/mapping.py`，纯规则、无 LLM）按 `features.yaml` 的血统段筛选，命中的才写入 `state/events.json`（进 git）。

这样拆分的收益是实质性的：**往 `features.yaml` 里加一个新特性、或调一条 5G-A 的 `title_re`，只需重跑 map，不必重新抓取、不必重新解析、不消耗任何 LLM 额度。** 5G-A 血统段的正则必然要反复调（§3.3），这条设计就是为它服务的。

代价是 `data/parsed/` 体积变大（每会议约几 MB JSON），但它本就不进 git 且可从 `raw/` 重建。

### 5.4 沉默失败防线

每次解析强制断言，任一不满足即**报错退出、保留 raw、不写 state**：

- heading 数 > 0
- 事件数 > 0
- 未对齐议程项占比 < 20%（仅对有 `agenda.csv` 的会议生效；老会议无议程锚点，跳过此项）

map 步骤另有一条断言：**某个血统段在其声明的会议区间内命中数为 0 时告警**（不硬失败）。这能抓住"5G-A 正则写错了"和"6G 议程号漂移了"两类问题 —— 前者在回填时暴露，后者在日常运行时暴露。

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
| ① 事件摘要 | 每条新增/变更且 **`depth == "full"`** 的 event | `text_en` + 议程标题 | `summary_zh`(2–3 句)、`tags`、`impact` | sonnet / low |
| ② 会议简报 | 每次会议解析完 | 该会议全部 event 的**摘要** | `reports/….md` 正文 | opus / high |
| ③ 特性综述 | 该特性有新事件 | 该特性全部历史 event（见下） | `features/<slug>.md` 顶部"当前进展" + `stage` + `open_issues` + **`legacy_summary`** | opus / high |
| ④ 候选归类建议 | 存在未映射 6GR 议程项 | 议程标题 | 建议 slug（**仅写入报告，不落库**） | sonnet / low |

**`depth` 如何改变各任务的输入：**

- **任务 ①** 只处理 `depth == "full"` 的事件。`origin` 段事件入库但跳过摘要（`llm_status: "skipped_by_depth"`），`milestone` 段事件在 map 阶段就已按类型过滤。
- **任务 ③** 是 `origin` 段价值的唯一出口：输入为该特性 `full` 段的逐条摘要 + `origin` 段的**英文原文**（按会议分组）。额外产出 `legacy_summary` 字段 —— 专门回答"5G-A 阶段做到哪一步、哪些没做充分、为什么延续到 6G"。这是本次范围扩展要的东西。
- `origin` 段原文体量可观（一个特性十几次会议可能上千条），超出单次调用舒适区时按**会议分批预归纳**：先每 3–4 次会议归纳一段，再合并成 `legacy_summary`。仅在首次回填时发生一次，之后 `legacy_summary` 缓存复用，除非该血统段有新事件（对已冻结的 Rel-18/19 而言永远不会）。

**枚举值定死，不许自由发挥**（写进 prompt 并在解析时校验，不合法即视为 JSON 校验失败走重试）：

- `impact`：`high` | `medium` | `low` —— 对协议走向的影响程度。
- `stage`：`未启动` | `讨论中` | `收敛中` | `已定稿` —— 特性当前所处阶段，由任务 ③ 判定并写入 `state/features_state.json`。这是看板"阶段"列的唯一来源。
- `open_issues`：字符串数组，该特性尚未解决的争议点，对应看板"未决"列的计数。

`stage` 是全设计中**唯一由 LLM 判定的结构化字段**（归类仍归规则），因为它本质是对一段历史的判断，没有可靠的机器规则。它随每次综述重算，历史值可从 `git log` 回溯。

### 6.3 针对 16K 固定开销的三条优化

1. **一批 40 条事件**（非 15 条），靠大批量摊薄固定开销；批量上限由输出质量决定，不由输入长度决定。
2. **简报只吃摘要不吃原文** —— 250 条事件原文约 150K token，其摘要仅约 37K。相应地，**会议简报只对含 `full` 段事件的会议生成** —— 纯 5G-A 历史会议不出简报（其事件无逐条摘要，且历史脉络由 `legacy_summary` 承载）。
3. **extract 阶段必须连续跑完**，落在同一个 1 小时 ephemeral 缓存窗口内，16K 开销只付一次。

### 6.4 用量预算

回填分两部分。**6GR 段**（约 1000 条 `full` 事件 / 8 次会议 / 15 个特性）：

| 环节 | 调用数 | 输入 | 输出 | list 等价 |
|---|---|---|---|---|
| 摘要（40 条/批，sonnet） | ~25 | ~1.0 M | ~150 K | ~$3 |
| 会议简报（opus，吃摘要） | 8 | ~430 K | ~24 K | ~$2 |
| 特性综述（opus） | ~15 | ~540 K | ~22 K | ~$2.3 |
| 小计 | ~48 | ~2.0 M | ~200 K | **≈ $7–8** |

**5G-A 血统段**（约 2000–3000 条 `origin` 事件，约 6 个有血统的特性，跨约 15 次会议）：

| 环节 | 调用数 | 输入 | 输出 | list 等价 |
|---|---|---|---|---|
| 逐条摘要 | **0** | — | — | **$0**（`depth: origin` 跳过） |
| `legacy_summary` 分批预归纳（opus） | ~18 | ~1.5 M | ~40 K | ~$3 |
| `legacy_summary` 合并（opus） | ~6 | ~150 K | ~12 K | ~$1 |
| 小计 | ~24 | ~1.65 M | ~52 K | **≈ $4** |

**回填总计 ≈ $11–12 等价用量，约 72 次 `claude -p` 调用。** 按 `max_calls_per_run=60` 计，需分 2 次 `ngr backfill` 完成。

选择 `origin` 而非 `full` 处理 5G-A 的收益：逐条摘要 2000–3000 条约需 ~$18–25，此处省掉。代价是历史段无法按中文检索 —— 但英文原文与链接完整保留，且 `legacy_summary` 已回答"源头脉络"这个真实需求。

日常增量：绝大多数日子 0 次调用；纪要上传后的几天约 10–15 次调用。**5G-A 血统段不增加任何日常开销** —— 相关会议已冻结（§4），既不重抓也不重算。

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
   - **血统** ← 该特性是否含 5G-A 段，标 `5G-A→6G` 或 `6G 原生`
   - **累计 Agr.** ← 该特性全部历史 `kind == "agreement"` 事件数（6G 段 / 5G-A 段分列，如 `47 / 210`）
   - **本期新增** ← **最近一次已解析会议**中该特性的新增事件数（口径是"最近一次会议"，不是"上次运行以来"—— 后者会因运行频率变化而抖动）
   - **最近活动** ← 该特性最后一次出现事件的会议号
   - **未决** ← `open_issues` 数组长度
2. **`out/features/<slug>.md`** —— **本工具最有价值的一页**，结构自上而下：
   1. **当前进展**（LLM，`stage` + 综述）
   2. **5G-A 源头**（LLM `legacy_summary`）—— 该特性在 5G-A 阶段做到哪一步、哪些没做充分、为何延续到 6G。**仅有 5G-A 血统段的特性才有此节。**
   3. **6GR 演进**（`era: 6G` 事件按会议倒序，每条：中文摘要 + 英文原文 + 链接）
   4. **5G-A 历史事件**（`era: 5G-A` 事件按会议倒序，折叠默认收起，每条：英文原文 + 链接，无中文摘要）

   每条事件行首标注来源段，例如 `[6G/Rel-20 RAN1#127]`、`[5G-A/Rel-19 RAN1#120]`，让血统一眼可辨。
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
| `ngr run` | fetch → parse → map → extract → render → commit |
| `ngr run --no-llm` | 跳过 extract，零额度消耗 |
| `ngr backfill --wg RAN1 --from 112 --to 127` | 回填历史，按会议逐个提交，可中断续跑 |
| **`ngr remap`** | **只重跑 map + render**，不联网不调 LLM。改完 `features.yaml` 的血统正则后用它，秒级出结果、零额度 |
| **`ngr lineage-report`** | 打印血统命中对照表：每段命中哪些 heading、各多少条事件、哪些段命中为 0。5G-A 正则校准的主要工具 |
| `ngr fetch-docs --wg RAN1 --meeting 127 --agenda 10.2` | 按需深挖 |
| `ngr enrich` | 只补跑 extract |
| `ngr doctor` | 自检：claude CLI、认证、3GPP 可达性、配置合法性、git 状态 |

`remap` + `lineage-report` 这一对是 5G-A 血统段能落地的前提：调正则 → `remap` → `lineage-report` 看命中 → 再调，整个循环不联网、不花额度、秒级完成。

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

两套 fixture，分别覆盖两个时代：

- `tests/fixtures/RAN1_126/` —— 实测抓取的 `agenda.csv`(2.9 KB)、`Draft_Minutes_report_RAN1#126_v010.docx`(968 KB)、`docs_listing.html`(裁至前 50 条)。覆盖**有议程锚点**的 6GR 路径。
- `tests/fixtures/RAN1_120/` —— 一次 5G-A 时代会议的纪要 docx + `Agenda/` 目录列表（**实测该目录下只有 TDoc zip，无 `agenda.csv`**）。覆盖**无议程锚点、只能靠 `title_re` 锚定**的 5G-A 路径。

第二套 fixture 是本次范围扩展新增的，不可省 —— 5G-A 段走的是完全不同的锚定分支，用 #126 的 fixture 测不到。

| 层 | 方法 | 重点 |
|---|---|---|
| `fetch` | mock HTTP | UA、403 退避、**403 不得被当作"文件不存在"**、目录列表先行、HEAD 增量判定、manifest 读写、纪要版本比较、frozen 跳过 |
| **`parse`** | **真实 fixture + golden file** | **主战场，走 TDD** |
| **`map`** | 真实 fixture + 构造的 `features.yaml` | 血统段区间匹配、多段重叠同时命中、`depth` 赋值、命中为 0 时告警、无 `agenda.csv` 时退到 `title_re` |
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

**先探明以下事实并填实配置，再写代码。** 这些在 spec 中均为假设值，先写代码后撞墙的代价高于先探明：

1. **RAN2 / RAN3 / RAN4 与 TSG RAN plenary 的目录布局** —— §4 中路径（`WG3_Iu`、`WG4_Radio` 等）为推测，仅 RAN1 经实测确认。plenary 的关键产物是批准的 WID/SID 与状态表，而非 agreement，产物清单需单独确定。
2. **`agenda.csv` 的确切起始会议** —— 实测 #124 有、#120 无、#122 返回 403 无法判定。需在放慢请求速率后重测，确定 `title_re` 兜底分支从哪次会议开始生效。
3. **5G-A 血统段的真实议程位置** —— §3.3 中 AI/ML、ISAC 等的 Rel-18/19 议程号与标题为推测。需抓取 #112–#122 的纪要 heading 清单，据此写出首版 `title_re`，再用 `ngr lineage-report` 校准。

第 3 项依赖第 2 项，且必须在编写 map 层测试之前完成 —— 否则测试断言无从写起。
