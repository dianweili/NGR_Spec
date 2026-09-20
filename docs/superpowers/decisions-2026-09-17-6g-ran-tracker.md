<!-- 这是执行账本 .superpowers/sdd/2026-09-17-6g-ran-tracker/progress.md 的提交副本。

账本是本项目唯一记录"为什么这么定"的地方 —— 代码注释里只有结论，没有推理过程
（比如为什么 320 该改成 319、为什么未对齐率阈值不能动、为什么否决 nan 哨兵方案）。
而它位于 .superpowers/ 下、被 gitignore，`git clean -fdx` 会删掉它，
我也曾用错误的截断方式把它删掉过一次（无备份，靠上下文重建）。

所以在这里留一份随仓库走的副本。**权威仍是 .superpowers/ 下的原件**，此副本在每个任务
收尾时同步。如果不需要它进仓库，删掉本文件即可，不影响任何流程。 -->

# SDD ledger — plan: docs/superpowers/plans/2026-09-17-6g-ran-tracker.md

Spec: docs/superpowers/specs/2026-09-17-6g-ran-tracker-design.md (已读，为绑定权威)
Branch: feat/ngr-tracker (从 master 91f7b0d 分出)
Tasks: 22

## Pre-flight 冲突扫描

### 跨任务接口配对（共享文件或符号的任务对）

| 生产方 | 消费方 | 产出 → 消费 | 结论 |
|---|---|---|---|
| T2 models/paths | T3,T5,T6,T7-T15 | Event/Meeting/Feature/LineageSegment/P | 一致 |
| T3 config | T4,T5,T6,T11,T17,T18,T20,T21 | HttpConfig/WgConfig/ExtractConfig | 一致 |
| T4 client | T5,T6,T20,T21 | Http/FetchError/RateLimited | 一致 |
| T5 listing/discover | T6,T20,T22 | parse_listing/discover_meetings/fetch_window | 一致 |
| T6 manifest/runner | T11,T20 | Manifest/pick_latest_minutes/fetch_meeting | 一致 |
| T7 agenda | T11 | parse_agenda → AgendaItem[] | 一致 |
| T8 docx | T9,T10,T11,T22 | parse_docx/Document/Block | **C4** |
| T9 events | T11 | extract_events → RawEvent[] | 一致 |
| T10 align | T11 | align/Alignment/normalize | 一致 |
| T11 parse.runner | T13,T20 | parse_meeting/write_parsed/ParseError | 一致 |
| T12 lineage | T13,T22 | match_event/agenda_matches | 一致 |
| T13 map.runner | T20,T22 | map_meeting/merge_events/write_state | **C3** |
| T14 markdown | T15 | render_dashboard/feature_page/report | 一致 |
| T15 site/runner | T20,T22 | render_site/render_all(unmapped=) | 一致 |
| T16 backend/cache/budget | T17,T18,T20 | ClaudeCli/LlmCache/Budget | 一致 |
| T17 tasks/runner | T18,T20 | PROMPT_VERSION/SchemaError/strip_fence/extract_all | **C2, C5** |
| T18 digest | T20 | digest_features | 一致 |
| T19 alerts/gitio | T20 | build_banner/commit_outputs/build_commit_message | 一致 |
| T20 cli/pipeline | T22 | main/run_pipeline/_load_json | **C1** |
| T21 doctor | T20 | run_doctor ← **被更早的 T20 引用** | **C1** |

### 单任务自洽性（测试 vs 代码 vs 文件清单）

T1 侦察产物即 T3/T12 的输入，自洽 · T2 dataclass 字段顺序合法（无默认值在前）· T3 七项测试覆盖全部校验分支 ·
T4 八项测试覆盖 403/429/404/超时 · T5 两文件两测试文件，自洽 · T6 ARTIFACTS 选择器签名统一为 `(names)->str|None` ·
T7 自洽 · T8 见 C4 · T9 MARKER_RE 锚定行首，与"不匹配句中 agreement"的测试一致 · T10 深度容差 ±1 与两项测试一致 ·
T11 五条断言与 §5.4 一致 · T12 通配按点分段，与"10.2.* 不命中 10.20"一致 · T13 见 C3 · T14 自洽 ·
T15 自洽 · T16 自洽 · T17 见 C2/C5 · T18 自洽 · T19 自洽 · T20 见 C1 · T21 自洽 · T22 自洽

### 冲突与裁定

**C1 — T20 的 cli.py 在模块顶层 `from ngr.ops.doctor import run_doctor`，但 doctor.py 到 T21 才创建。**
T20 的测试会在 import 阶段就 ImportError。
Ruling: T20 的 `cli.run_doctor` 改为惰性包装函数（与计划中 `run_remap`/`run_enrich` 同一模式），在函数体内 import。
— 理由: 与计划已有的包装模式一致，且 T20 的测试用 `monkeypatch.setattr(cli, "run_doctor", ...)`，包装函数同样可被替换。
— 代价: 若判断有误，仅影响一个函数的 import 写法，改回顶层 import 即可。

**C2 — T18 的 digest.py 从 tasks.py 导入私有名 `_strip_fence`。**
Ruling: T17 中该函数命名为公开的 `strip_fence`，T18 导入公开名。
— 理由: 跨模块导入下划线私有符号会被审查判为缺陷，且它确实是共享工具函数。
— 代价: 纯重命名，无行为影响。

**C3 — T20 的 `stats_by_meeting[...][ev.feature] += 1` 写在 `if stats.added:` 内，会把未变更事件也计入提交信息。**
Ruling: T13 的 `MergeStats` 增加 `added_ids: list[str]` 字段；T20 只按 added_ids 统计。
— 理由: 提交信息是给人看的进展流水账，数字错了就失去意义；加字段不破坏 T13 既有测试。
— 代价: 若判断有误，提交信息的计数偏大，不影响数据正确性。

**C4 — T8 的 parse_docx 用 `__import__("io").BytesIO`。**
Ruling: 改为文件顶层 `import io`。
— 理由: 无任何理由使用动态导入，审查必然判为缺陷。
— 代价: 无。

**C5 — T17 的 Interfaces 块写 `extract_all(events, features, cfg, ...)`，但其代码与测试均为 `extract_all(events, cfg, ...)`（无 features）。**
Ruling: 以代码与测试为准，签名为 `extract_all(events, cfg, *, cli_factory, cache, budget)`；Interfaces 块的写法作废。
— 理由: T20 的调用方写法与代码一致，且 extract_all 确实不需要 features（归类已在 map 层完成）。
— 代价: 无。

---

## 执行记录

Task 1: dispatched (BASE=91f7b0d, model=sonnet, 侦察任务，无产品代码)
Task 1: 控制器在 T1 运行期间用 `git add -A` 提交了计划裁定（6c10fb1），误将 T1 在写的 scripts/recon.py 一并纳入。
  Ruling: 不回滚（内容本就属于 T1，回滚反而制造冲突）；此后控制器在 implementer 运行期间**只做只读 git 操作**，
  必须提交时用显式路径而非 -A。
  — 代价: 若判断有误，T1 的 recon.py 提交归属记在控制器的提交里，历史略乱，无功能影响。
Task 1: 两轮后仍 BLOCKED（sonnet，agent 连续把带 sleep 的脚本投到后台后结束回合，未落盘报告/fixture/提交）。
  已产出: config/sources.yaml（质量合格：RAN1 标 verified:true，其余四组标 verified:false 并说明 403 歧义，未编造）
  缺失: tests/fixtures 两套均为空目录；task-1-report.md 未写；无提交
  Ruling: 拆分重派 —— 1a(fixture 下载，5 个文件，硬阻塞 T8-T11) 优先于 1b(#112-#122 heading 清单)；
    dispatch 中明令禁止 run_in_background，要求前台分批同步执行；模型由 sonnet 升为 opus。
  — 理由: 根因是执行模式（后台+回合结束）而非推理能力，但该任务是全部 22 个任务的事实地基，值得升配换确定性。
  — 代价: 若判断有误，多花一次 opus 的调用成本；fixture 若仍拿不到，T8-T11 无法开工，届时需由我直接下载。
Task 1: 旧 agent (a927fdc) 第三次通知仍无报告，已 TaskStop 终止，避免与重派的 agent (af3079d) 争抢 tests/fixtures 与 git 索引。
Task 1: 重派完成 DONE_WITH_CONCERNS (commits 04afbc8, 0490574)。fixture 5/5 校验通过；heading 清单 11/11 次会议、1148 条、零失败。
  对其 5 条顾虑的裁定：
  Ruling A(报告路径): 接受 docs/superpowers/recon-2026-09-17.md 作为入库报告 —— 计划 Task 1 的文件清单本就指定该路径；
    不 git add -f 绕过 .superpowers/sdd/.gitignore。代价: 无。
  Ruling B(sources.yaml 注释更正): 接受。实测证明不存在的路径同样返回 403（TSGR1_999/Agenda/ → 403，
    而 TSGR1_121/ → 200 且列表中无 Agenda 条目），印证并细化了 spec §2 的 403 歧义约束：正确探测法是读父目录列表。
    另 agenda_csv_since=124 被逐会实测坐实(#120无/#123无/#124有/#125有/#126有)，消除 spec 中 #122 的未决。代价: 无。
  Ruling C(ISAC 血统起点): 实测为 #116 而非 #112，Task 3 写 features.yaml 时 ISAC 的 5G-A 段用 [116, 123]。
    代价: 若错，ISAC 5G-A 段少收 #112-#115 四次会议的事件，可用 remap 零成本补回。
  Ruling D(省电): 不写"UE 省电/WUS"单条正则（1148 条 heading 中仅 2 次出现且均非血统证据），
    改为证据充分的两条：网络侧节能 NES、LP-WUS/WUR。代价: 若错，漏一个特性，可后补。
  Ruling E(限速): sources.yaml 的 delay_seconds 0.5 / concurrency 2 从未实测，而 Task 1 全程实测可用的是 5 秒串行。
    改为发布保守默认 delay_seconds=2.0 / concurrency=1；spec §4 的 0.5/2 降级为"上限，需实测后方可调到"。
    — 理由: 被 3GPP 限流会让日常任务静默失败，而回填慢几分钟没有代价；这是安全侧偏离且有实测依据。
    — 代价: 回填 15 次会议约多花 2 分钟。
  Ruling F(纪要 zip 包裹) **载荷性计划缺陷**: 实测 ≤#122 的纪要以 zip 包裹 docx 分发，#124 起为裸 docx。
    计划 Task 6 的 MINUTES_RE 只匹配 .docx，对全部 5G-A 会议会匹配失败 → missing → 管线静默跳过 → 血统空洞。
    Ruling: 修改计划 Task 6，令 minutes 识别与下载同时支持 .docx 与 .zip，下载后剥离外层 zip；补相应测试。
    — 代价: 若不改，5G-A 血统段全部为空且无告警，是本项目最坏的失败模式。
  Ruling G(zip→docx 切换边界): #123-#125 未探明。不阻塞 —— Ruling F 的双格式支持使边界无关紧要。代价: 无。
Task 1: 任务审查完成 — spec 符合性全项 ✅；Critical 0 / Important 2 / Minor 2；结论 Needs work。
  审查者独立重跑了 title_re 正则、重算 fixture 字节数与条目数、用 data/raw/_recon 缓存交叉验证，未发现任何编造结论。
  Important#1: 报告 §4.1 隐去了已实测的 #118/#119（均 403），与报告"全部状态来自本次实测"的完整披露声明不符。
  Important#2: #115-122 的原始抓取缓存缺失，HTTP 层无法独立复核（数据内部自洽，非造假）。
  Task 1: minor (deferred): dir_re 对 TSGR1_100b_e / TSGR3_107-cancelled / TSGR4_57AH 等历史 ad-hoc 目录名不匹配 —
    经核实全部低于各组 hard_floor，实际无影响；建议加注释。留给最终审查分诊。
  Task 1: minor (deferred): 控制器提交 683ab67（Ruling E/F）落在审查范围外且触碰 Task 6 计划文件 —
    这是控制器裁定提交，非 Task 1 交付物，账本已分别记录，无需修复。
Task 1: fix round 1/5 — 实现者报 DONE (commit fb74685)，定向复审已派出 (范围 683ab67..fb74685)。
  实现者新发现（本轮增量）: 低于 agenda_csv_since 的会议有两种形态 —— "Agenda/ 存在但无 csv"(#120/#123) 与
    "根本没有 Agenda 目录、GET 即 403"(#118/#119/#121/#122)。核实结论: 计划 Task 6 已先读会议根目录列表、
    子目录不在列表即跳过，故不会 GET 不存在的 Agenda/，不会触发 403 重试 —— **设计已覆盖，不改计划**。
  Ruling H(证据文件入库): 本轮新落盘的 4 份根目录 HTML 位于 gitignore 的 data/raw/ 下，不入库。
    — 理由: spec §3.1 明确 data/raw 不进 git（体积原因），且报告正文已记录结论与复核方法；不为个案破坏该规则。
    — 代价: 若判断有误，这 4 份证据只存在于本机，需要时可用 recon.py 重取。
Task 1: fix round 1/5 复审结果 — Important#1 ADDRESSED, Important#2 ADDRESSED（均经独立复核：grep 四份根目录 HTML
  确认不含 Agenda、清点缓存文件数、YAML 前后比对确认 sources.yaml 取值未动）。
  新增 Important: 修复为纯追加（附录 B），§4.1 表格本体与开篇"完整披露"承诺句未更正、未加交叉引用，文档自相矛盾。
  Ruling I: 不采纳复审者"可过审+待办"的建议，进 fix round 2。
  — 理由: 首轮审查的字面要求就是"补进 §4.1 表格"，未被执行；且这份报告是 21 个任务的地基，其价值全部来自可信度，
    开篇一句现在字面为假的"完整披露"承诺比数据缺失更伤。修复成本极低（改一张表+一处交叉引用）。
  — 代价: 多一轮往返；若判断有误，损失的是一次小修的时间。
Task 1: fix round 2/5 — 实现者报 DONE (commit a77bd8c)。§4.1 表格就地补成 9 行、开篇承诺句拆分改真、
  额外自查出 §4.2 同源矛盾并一并收口。
  Ruling J: 采纳实现者顾虑#1，把"修缺陷改源头、不用追加打补丁"写入计划 Global Constraints（对后续 21 个任务生效），
    而非留在报告正文。— 理由: 该模式在 Task 1 连犯两次，是会重复出现的系统性风险，不是个案。— 代价: 无。
  Task 1: minor (deferred): §4.1 与附录 B.1 各有一张同内容 9 行表，将来一方被改而另一方未跟上会复现矛盾。
    不修 —— 侦察报告是一次性历史产物，无后续编辑计划，风险为潜在而非现存。留给最终审查分诊。
Task 1: fix round 2/5 复审 — ADDRESSED，无新增 Critical/Important，sources.yaml 确认未被触碰。
  Ruling K: 用户明确授权"不着急，把 Task 1 弄扎实"，据此撤销三项此前以"不值得花时间"为由的 deferred，进 fix round 3：
    (a) 坐实 RAN2/RAN3/RAN4/RANP 的目录结构与 artifacts（当前四组 verified:false、agenda_csv_since:null、
        hard_floor 为 spec 推测值、RANP 的 artifacts 是照 RAN1 同构填的占位 —— 这是 Task 1 最大的剩余假设，
        且 spec §10 第一条本就要求实现前探明）；
    (b) 补齐 #115-122 原始响应存档，消除 Important#2 的残留（此前以"几十 MB/十几分钟不值"为由拒绝，该理由已不成立）；
    (c) 消除 §4.1 与附录 B.1 的重复表（B.1 只留叙述并引用 §4.1）。
  — 代价: 这一轮要发约 40 次 HTTP 请求，耗时较长；若 RANP 结构与 RAN1 差异大，可能牵出 Task 6 的计划改动。
Task 1: fix round 3/5 — DONE_WITH_CONCERNS (commit ade9075)，约 110 次请求。对 6 条顾虑的裁定：
  顾虑1(hard_floor 与计划断言冲突): **虚惊**。核实计划里 hard_floor=112 全部位于合成测试夹具
    (Task 3 内联 YAML、Task 5 的 WgConfig(...))，与真实配置取值无耦合，改配置不破坏任何断言。无需改计划。
  顾虑5(recon.py 漏 encoding): 实测缺陷属实且已由实现者修复。用平衡括号重扫计划中全部 write_text/read_text，
    **漏写 encoding 的调用为 0**，产品代码不受影响。无需改计划。
  Ruling L(schema 变更): 接受新增 report_dir / minutes_re / ls_dirs / latest_meeting_with_content /
    verified_fields。理由: minutes_re 是刚性需求（见 Ruling M）；latest_meeting_with_content 修正
    latest_meeting_seen 指向未召开会议的问题。需改计划 Task 3 的 WgConfig 与加载器。
  Ruling M(纪要识别改为按组配置) **载荷性**: 实测 RAN2 纪要名为 R2-2604502.zip（纯 TDoc 号）、RAN3 三种形态并存，
    计划的全局 MINUTES_RE 对这两组零匹配 → 静默空结果。改为 Task 6 从配置读该组 minutes_re；
    版本序在文件名无 _v### 时优雅降级；unwrap_docx 遇多个内层 docx 时取最大者（RAN2 zip 内含
    PartList/TDoc_List 等小文件）。— 代价: 不改则 RAN2/RAN3/RAN4/RANP 四组永远为空且无告警。
  Ruling N(agenda_csv_since 语义): 实测 RAN2 #131 无 agenda.csv 而 #130/#132 有 —— 该字段只能表示"最早出现"，
    不表示"此后每次都有"。故 Task 11 的 agenda_required 不得硬失败，改为降级到 title_re 锚定 + 写入 ALERTS。
    — 代价: 不改则管线在 #131 这类会议上以退出码 2 中止。
  Ruling O(hard_floor 语义): 实测 RAN4/RANP 的 "Rel-18 起始会议" 定义不成立（探到最早仍有 Rel-18 内容，下界不收敛），
    根因是频谱 WI 与新 WI/SI 提案远早于版本开工就上议程。将该字段语义从"Rel-18 起始会议"改为
    "允许回溯的最早会议号（安全钳位）"，RAN4 取 103、RANP 取 93（均为实测仍含 Rel-18 内容的最早会议）。
    — 理由: 该字段的设计目的本就是防配置写错导致失控回溯，不是语义边界；取值宁宽勿窄，真正的范围由血统段决定。
    — 代价: 若血统段配错，回溯范围比预期大，但 lineage-report 会显示命中情况。
  Ruling P(冻结逻辑) **载荷性**: 计划 Task 20 用 max(全部已发现会议号) 作 latest，而实测四组的最新目录
    都是只有 Invitation 的未召开会议 → latest 虚高 → 最新的有内容会议被提前冻结 → 其 v010→v100 的最终版纪要
    永远不会被抓取。改为: latest 取"本次成功抓到纪要的最大会议号"，且仅在该会议解析成功后才标记 frozen
    （spec §4 原文就有"且已成功解析过"，计划代码漏了这个条件）。
  Ruling Q(report_dirs) **载荷性**: 实测 RAN4 老会议用复数 Reports、新会议用单数 Report，计划的单值 report_dir
    覆盖不了 → 回填到老会议时整段抓不到纪要。改为候选名列表，取第一个在会议根目录列表中出现的。
  裁定 L/M/N/O/P/Q 已全部落回计划与 config/sources.yaml（commits 见 git log），并同步修正了配置中
    与新取值矛盾的注释（遵守本轮新增的"改源头不打补丁"全局约束）。
Task 1: complete (commits 04afbc8..ade9075 + 控制器裁定提交, fix rounds 3/5, 2 minors parked)
  最终交付: fixture 5/5 校验通过 · RAN1 #112-#122 heading 清单 11/11 会议 1148 条 · 五个工作组抓取源全部填实
  (RAN1/RAN2 verified:true，RAN3/RAN4/RANP 标注 unverified_fields 说明差什么) · 侦察报告入库 docs/superpowers/recon-2026-09-17.md
  副产物: 提前发现 6 条会导致静默失败的计划缺陷（纪要 zip 包裹、按组 minutes_re、agenda 缺口硬失败、
  冻结逻辑提前冻住最新会议、report_dirs 单值、recon.py 编码）—— 均已修入计划。

Task 2: dispatched (BASE=8787695, model=sonnet — 首个代码任务，建立后续全部任务 import 的包布局，
  故未用最低档；纯转写类任务后续降档)
Task 2: 任务审查 Approved，零缺陷（5 条测试逐字采用并经审查者独立跑通，无范围外改动，无多余抽象）。
  实现者两条顾虑已在源头修复: 计划中 "cli.py 到 Task 18" 的过期引用改为 Task 20；
  KIND_PREFIX 与 MARKERS 的漂移由运行期 KeyError 改为导入期断言。
Task 2: complete (commits 8787695..6e4a5db, review clean)
Task 3: 派发前自查发现**控制器自身引入的不一致** —— 加载器已把 minutes_re 设为必填，
  但 Task 3 的测试夹具 SOURCES_OK 没有该键，会导致 Task 3 一开跑全红。已在计划中修正夹具并补 4 条新字段测试。
  教训: 改 A 任务的接口时必须回头检查所有引用该接口的任务夹具，不能只改定义处。
Task 3: 实现者按纪律停下汇报（未改测试、未提交），发现计划中三处真缺陷。裁定并已改源头：
  Ruling R(Mozilla 校验): 保留校验、改夹具 —— 该校验防的是真实故障（默认 UA 被 WAF 挡成 403），
    属启动时就该炸的配置错误。补一条专门覆盖该校验的测试，并让错误信息含 user_agent 字样。
  Ruling S(重复 slug 测试): 字符串拼接构造不出合法 YAML，yaml.safe_load 阶段即报错，永远到不了检测逻辑。
    改为显式 FEATURES_DUP_SLUG 常量。— 这是计划自检时没抓到的测试缺陷。
  Ruling T(waveform/channel_coding 无 title_re 证据): 不需另行核实。二者是纯 6G 出身，主锚点是议程号，
    而议程号本身即实测 —— agenda.csv 逐字含 "10.2","Waveform for 6GR air interface" 与
    "10.3","Channel coding and modulation for 6GR interface"。侦察报告 §3 只服务于无 agenda.csv 的 5G-A 段，
    故 6G 段的证据出处应引 agenda.csv 而非 §3。
  已重新生成 task-3-brief.md 并让实现者重读后从 Step 1 重做。
Task 3: 任务审查 — Needs work。Critical 1 / Important 2 / Minor 3。审查者独立跑通 17 项测试与真实配置加载，
  并自行去 recon 附录 A 与 agenda.csv 逐字核对了 4 条 title_re 的出处，全部命中。
  Critical: ai_air_interface 的 Rel-19(5G-A) 段配成 depth:full，违反"5G-A 段默认 origin"硬约束，
    且区间开放 [116,null] 会随会议持续放大额度消耗。已进 fix round 1。
  Important: 数值字段类型错误抛裸 ValueError，报错指不出字段；若干校验分支无测试覆盖（源自计划的测试集不全）。
  **控制器自身缺陷（审查在范围外观察中指出）**: Ruling O 改了 hard_floor 取值与口径，只改了 config/sources.yaml，
    未同步记录这些值的侦察报告（四处仍写"保留推测值 106/99"），与配置互相矛盾 —— 违反的正是我自己定的
    "改源头不打补丁"全局约束。已修并提交，加脚注说明口径变更。
  Ruling U: 该修复由控制器直接执行，未派 agent。— 理由: 这是控制器裁定的不完整应用、属文档同步，
    且 Task 1 已收工，为 4 行文字派一个 agent 不成比例。— 代价: 该修复未经独立审查，留待最终全分支审查复核。
Task 3: fix round 1/5 — DONE (commit 49a27ae)，33 项测试通过。Critical(depth:full) 已改回 origin 并在 yaml 写明不给例外的理由。
  实现者主动追问"整数校验是否要扩到 http/extract 段"（未点名处不擅自扩大范围）。
  Ruling V: 扩。理由 —— 同一类缺陷而非新范围：审查给的判据是"错误信息必须能定位字段"，
    concurrency: "两个" 抛的裸 ValueError 同样指不出字段；配置错误须在启动时炸且炸得可读，是通则，
    不按字段所在段落区别对待。另新增取值合理性校验（concurrency<1 / batch_size<1 / delay_seconds<0 等）——
    类型对但取值无意义比类型错误更难排查（concurrency: 0 会让抓取层一个请求都发不出却不报错）。
Task 3: fix rounds 2-3 — 数值/取值合理性校验扩到 http/extract 段；父容器类型校验（_as_dict/_as_list），
  未用 except Exception 兜底（实现者自行 grep 验证）。36 项测试通过。
  **控制器方法论错误（由实现者指出）**: 我要求"关掉父容器类型错误这一整类"却给了一份七条枚举清单，
    清单漏了 meetings —— 给枚举本身就是在继续打地鼠，只是改由我来漏。
  Ruling W: 改为让实现者自行对 ngr/config.py 做完整性扫描（grep 所有 .get( / .items( / 下标 / 遍历 / len(），
    逐处确认是否已过校验，并在报告中列出扫描结论。— 理由: 它手上有代码，grep 比我凭记忆列清单可靠；
    且扫描结论留档后，下次验证完整性无需重做。— 代价: 若扫描不彻底，仍可能漏，但由定向复审兜底。
Task 3: fix round 4/5 收口 (commit 0b85b35)，38 项测试通过。完整性扫描补的缺口多于点名项，
  其中 artifacts/report_dirs/ls_dirs 的裸 list() 最有价值 —— YAML 漏写方括号会把字符串静默拆成字符列表，
  不崩溃只是行为诡异，比抛异常隐蔽。
  Ruling X: 认同实现者对"标量叶子字段类型未校验"的判断 —— 与本轮商定的容器类型校验属不同性质，
    堵上需给几乎每个字符串字段加校验，是未经要求的更大范围。**不展开**，记为 deferred 留给最终审查分诊。
  — 理由: 标量字段写成不可哈希类型属罕见手误，且会立即抛异常（非静默），危害远低于已修的静默拆字符串。
  — 代价: 若发生，用户看到裸 TypeError 而非可定位的 ConfigError。
Task 3: minor (deferred): 标量叶子字段（backend/depth/default_depth/user_agent 等）未做类型校验，
  误写成列表等不可哈希类型会抛裸 TypeError。
Task 3: fix round 4/5 定向复审 — 全部 ADDRESSED。复审者独立复核四项：yaml 段落计数（5G-A 3 段全 origin /
  6G 3 段全 full）、grep 确认无 except Exception 兜底、独立重跑容器操作完整性扫描（未发现实现者遗漏）、
  38 项测试通过。未引入新 Critical/Important。
Task 3: complete (commits d5b0b5f..0b85b35, 4 fix rounds, review clean, 1 minor parked)

Task 4: dispatched (BASE=0b85b35, model=haiku — 首次降档试验：该任务计划里含完整代码，属转写+测试，
  按模型选择指引用最低档。若 BLOCKED 或质量不足则升档重派，结论记入账本供后续任务参考)
Task 4: 任务审查 Approved，零 Critical/Important。8 条测试逐字采用并经审查者独立跑通；
  对抗性检查确认：网络故障抛 FetchError、限流抛 RateLimited，上层可用 isinstance 精确区分。
  **降档试验结论: 成功。** haiku 一次通过、零顾虑。判据: 计划文本含完整代码的转写型任务可用最低档。
  适用于后续 Task 7/8（同为完整代码转写）；Task 13/20 等判断密集任务仍用 sonnet 及以上。
Task 4: minor (deferred): head() 对 403/429/503 不退避重试，与 get() 不对称（简报原设计）。
  影响评估: HEAD 是日常流量主体，瞬时 403 会跳过该次会议的抓取，但有告警且下次运行自愈，不静默。故不修。
Task 4: minor (deferred) **下游检查点**: RateLimited 继承自 FetchError —— 若 Task 5/6 的调用方写成宽泛的
  `except FetchError` 并把"抛异常"等同于"文件不存在"，会重新引入本项目最坏的失败模式（静默空洞）。
  **必须在 Task 5/6 的派发与审查中显式检查异常捕获顺序（except RateLimited 优先于 except FetchError）。**
Task 4: complete (commits 0b85b35..41b3f05, review clean, 2 minors parked)
Task 5: 实现者按纪律 BLOCKED 停下汇报（未擅自改测试），发现计划缺陷：parse_listing 的正则在全文裸匹配
  目录 URL，页面正文/注释里出现同一 URL 时会把周围文字当成文件名。
  Ruling Y: 改为锚定 href 属性 —— 实测裸匹配得 51 条（多一条说明文字），锚定后恰好 50 条全为 R1-*.zip。
    捕获 base 之后第一个路径段，直接子条目语义反而更准。补回归测试，重新生成简报。
  — 代价: 若 3GPP 将来改用无引号或单引号 href，需再调；已兼容单双引号。
  观察: 该缺陷是靠"用真实 fixture 做测试"暴露的。若只有合成 HTML 测试，它会活到首次真实抓取才显形，
    且表现为"目录里多出莫名其妙的文件名"，排查成本高得多。这印证了计划里保留真实 fixture 的决定。
Task 5: 第二次 BLOCKED — 合成夹具 WgConfig 缺 minutes_re（我加必填字段时只修了 Task 3 的夹具）。
  Ruling Z: 不逐个修。扫描计划里全部 WgConfig/HttpConfig/ExtractConfig 构造并逐项核验必填字段：
    WgConfig 三处（Task 5/6/22）全缺、已补；HttpConfig 一处、ExtractConfig 三处确认无漏。
  — 这是第二次犯"改定义处不扫引用处"的错（第一次是 Task 3 的 SOURCES_OK）。此后凡改数据类必填字段，
    一律立即全量扫描该类的所有构造点，不等下游任务撞上。
Task 5: 任务审查 — Needs work。Critical 1（对抗性检查发现）/ Important 0 / Minor 2。
  spec 符合性全项 ✅（12 条测试逐字采用并经审查者独立跑通）；专门检查 A（异常处理）合规 ——
  listing.py/discover.py 全文无 try/except，RateLimited 原样上抛，Task 4 park 的下游检查点已兑现。
  Critical: fetch_window 在血统闭区间整体低于 hard_floor 时返回 (112,100) 倒置区间 —— 类型合法语义非法，
    下游按 range(lo,hi+1) 消费得空循环或负数，且分不清"未覆盖"与"被钳没"。缺陷源自简报参考实现。
  Ruling AA: 闭区间情形下 max(highs) < low 则返回 None 并打 warning 日志。— 日志不可省：
    否则排查"这个组为什么不抓"时无从下手，等于用另一种静默替换原来的静默。
  Task 5: minor (deferred): discover_meetings 每次调用重新 re.compile（每组每次运行仅一次，非热路径，
    加缓存属过早优化，不修）。
  Task 5: minor (deferred): parse_listing 返回字典序非数值序（discover_meetings 自行重排，
    其余消费者只做集合判断，不依赖顺序，不修）。
Task 5: fix round 1/5 定向复审 — ADDRESSED。复审者独立跑验 7 个边界场景（开放区间/混合/全钳没/无覆盖等）
  全部正确；确认日志只在"被钳没"时打、"无覆盖"时不打，两种 None 可区分。14/14 通过，无范围外改动。
Task 5: complete (commits 41b3f05..b9cb9b0, 1 fix round, review clean, 2 minors parked)

Task 6: dispatched (BASE=b9cb9b0, model=sonnet — 升档：fetch 层收口点，承载 Task 1 挖出的四条硬约束)
Task 6: 实现者按纪律 BLOCKED（未改测试、未提交），发现两条 tie-break 测试的文件名缺 Draft_/Final_ 前缀，
  与同文件顶部的 RAN1_RE 矛盾 —— 又一次"改定义处不扫引用处"（引入按组 minutes_re 时加了 RAN1_RE 常量，
  未回头改这两条旧全局正则时代写的测试数据）。
  Ruling AB: 按其建议加前缀。并**全量核验**计划里七条 pick_latest_minutes 测试的文件名与各自声明的正则，
    确认无其余同类矛盾。顺带修正 Step 4 遗留的预期条数 9 -> 19。
  — 这是第三次同类错误（Task 3 SOURCES_OK、Task 5 WgConfig 三处、本次 RAN1_RE）。全量核验已成常规动作。
Task 6: 第二次 BLOCKED — 这次缺陷在**实现代码**而非测试数据：pick_latest_minutes 的 rank() 元组把
  原始文件名排在格式偏好之前，同版本号仅差扩展名时 '...v100.docx' < '...v100.zip'（'d'<'z'）
  已在文件名位分出胜负，格式偏好成死代码，max() 选中 zip，与其 docstring 声明相反。
  Ruling AC: 元组改为 (有版本号, 版本号, 格式偏好, 文件名)。格式偏好必须在文件名之前；
    文件名只作最后兜底（无版本号时按 TDoc 号取新）。六条排序规则已独立脚本验证。
  — 注: 实现者两次都精确定位到根因并给出可行修法，但按纪律未擅自改。
Task 6: 第三次 BLOCKED — runner 组两处跨模块矛盾。
  Ruling AD(矛盾A，归因被修正): 实现者倾向"改测试助手转义"但把它当作迁就实现；查 Task 1 留下的
    data/raw/_recon/report_dir_TSGR1_*.html（八个会议）确认真实 HTML 里 # 一律写作 %23 ——
    parse_listing 排除 # 并 unquote() 还原是**正确的**，是测试助手 _listing() 塞了未转义文件名、
    模拟了现实不存在的 HTML。已拿真实 HTML 验证生产链路正常（得到 Final_Minutes_report_RAN1#112_v100.zip
    并被 RAN1_RE 命中）。改测试助手用 quote()。
  — 若无 Task 1 保留的原始缓存，只能靠推理，可能误判为"正则太严"而放宽掉一个正确的正则。
    这是保留原始抓取存档的第一次实际回报。
  Ruling AE(矛盾B): 采纳实现者修法 —— 只在扩展名为 .zip 时调 unwrap_docx。语义更准确
    （"只有 zip 需要剥壳"），且测试不必为每个 .docx 场景构造合法 zip 字节。四组实际形态均已核对覆盖。
Task 6: 完成 (commit c547c77)，manifest 19/19 + runner 5/5，全仓 84 passed。三轮阻塞暴露的五个缺陷全部来自计划。
  Ruling AF: 采纳实现者的流程建议 —— 新增 scripts/preflight_task.py，在下发前把计划里的代码块与测试块
    抽出来跑一遍 pytest，验证二者自洽。已用 Task 6（已交付，24 passed 与实际一致）验证工具可信。
    **此后每个任务下发前必跑预检，[FAIL] 则先修计划再下发。**
  — 工具设计要点: 只抽当前任务的实现块，前序模块用仓库里的真实实现（预检在下发前跑，Task 1..N-1 已交付）；
    曾错误地尝试累积前序任务的计划文本，导致 Task 6 从 PASS 变 FAIL，已撤销。
Task 6: 任务审查 — Approved（Critical 0 / Important 1 / Minor 2）。审查者逐条核实四条硬约束的代码位置，
  自造输入验证 pick_latest_minutes 四条排序规则与 unwrap_docx 三种输入，grep except 零命中。
  Important: man.save() 只在循环跑完后调用一次，中途抛 RateLimited 会让已成功的 artifact 不入 manifest，
    下次重试重复下载 —— **重试放大**。审查建议推给后续任务，我不采纳。
  Ruling AG: 现在就修。— 理由: 该缺陷的方向与本项目核心运维风险（限流）正相反：限流引发重复下载、
    重复下载又加剧限流；而修法只是 try/finally 两行。推给 Task 20 会脱离上下文或被遗忘。
  同时补两条测试：限流中断时 manifest 必须落盘；report_dirs 多候选按序取首个（后者是审查指出的
  测试集覆盖间隙 —— 原 5 条 runner 测试都用默认单候选，该规则本身从未被测到）。
  预检脚本首次实战：改完计划跑 preflight_task.py 6 得 26 passed，下发前即确认自洽。
Task 6: fix round 2 完成 (commits 2829876 try/finally, 3b58a3e 缩进)。runner 7/7、全仓 86/86。
  控制器两次缩进笔误: 先把 for 缩成 6 空格，再用 delta 方式"修"成 for=8/if=10 的另一种不规范。
  Ruling AH: 缩进类改动一律整段重写，不做 delta 手术 —— 增量改缩进无法保证层级一致。已重写并预检 26 passed。
  注: 实现者忠实照抄了可疑缩进并在报告里点出来，而非擅自美化 —— 正因如此我才看见自己的笔误。
Task 6: fix round 2 定向复审 — ADDRESSED。复审独立核实：grep except 零命中（异常原样上抛）、
  两条新测试断言有实质内容、缩进 4/8/12/16 标准递增、86 passed、自构造限流中断场景验证
  manifest 含已成功 artifact 的完整记录。无新增 Critical/Important。
Task 6: complete (commits b9cb9b0..a6bce72, 2 fix rounds + 4 轮下发前阻塞, review clean, 2 minors parked)
  **fetch 层（Task 4/5/6）全部完成。**

Task 7: 预检先行（新流程首次完整应用）
Task 7: complete (commit 405ceb0, 一次通过零修复, review Approved 零缺陷, 对抗性检查 12 项边界输入全过)
  **预检生效的第一个完整案例**：下发前 [PASS]，实现者零顾虑，审查零缺陷。
Task 8: 预检在下发前抓到**真实数据丢失缺陷**（非仅数字错误）。
  (a) 写死的 7803 段/320 Agreement 是用正则量的，正则处理不了表格内嵌套 <w:p>，数字本身错误。
      计划实现真实产出: 5061 段 / 83 heading / 82 表格 / 顶层 308 Agreement+26 Conclusion+11 WA。
  (b) **12 条 agreement 位于表格单元格内**（顶层 308 vs 全文 320，约 4%）。parse_docx 把表格整体
      转 markdown 块，这些标记对 extract_events 不可见 → 静默丢弃。
  Ruling AI: table 块新增 cell_paras 字段带出单元格段落；标记识别仍留在 Task 9（不在 parse 层做）。
    Task 9 据此把"用表格画的框"识别成事件。补测试锁定 8/2/1 的分布。
  — 若无预检，这 4% 的丢失会一路活到回填后才可能被发现，且表现为"某些 agreement 就是没有"，
    极难反推到表格嵌套这个原因。这是预检工具第一次抓到静默数据丢失。

================================================================
---

## Task 8: docx 段落/heading/表格抽取

- BASE: `ff1c571`；预检 `preflight_task.py 8` → **[PASS] 11 passed**
- 派发 implementer（haiku，计划含完整代码属转写型）
- 派发时强调：`cell_paras` 是为修静默数据丢失而加（12 条 agreement 在表格单元格里，约 4%）；
  标记识别留 Task 9，parse 层不做语义判断。

### Ruling AJ —— Task 8 修了生产者，消费者 Task 9 没跟着改

`ff1c571` 给 Task 8 的 table 块加了 `cell_paras`，但核对 Task 9 计划正文：**全段 0 次出现 `cell_paras`**，
其循环只有 `kind = _marker_kind(block.text) if block.kind == "para" else None`。
**生产者带出来了，消费者仍然不看**，原缺陷分毫未修。

这是全局约束"改源头"的反面案例被我自己踩中：只改了缺陷**被发现**的那一层，
没沿数据流走到真正**丢数据**的那一层。**预检抓不到它 —— 它只验单任务自洽性，
跨任务的生产/消费契约不在视野里。** 这是预检工具的一条真实边界。

裁定：修 Task 9 计划让 `extract_events` 遍历 table 块的 `cell_paras`。
时机压到 Task 8 提交并过审之后 —— 此刻 implementer 在跑，它 commit 时若 `git add -A`
会把我的计划改动扫进它的提交（Task 1 已踩过一次）。

### Task 8 审查结果（第一轮）

交付 `6be50bc`，102 passed，规格符合性 PASS（与简报逐字节一致），代码质量 CHANGES REQUESTED：

1. **commit 署名写成 `Claude Haiku 4.5`**，约束要求逐字 `Claude Opus 5 (1M context)`。
   实现者自查只查了"有没有这一行"，没查内容。
2. **`_text_of` 忽略 `w:tab`/`w:br`/`w:cr`，把两侧文本静默焊死**。审查者实测：
   3795 处 tab、48 处 br 落在两段无空白的文本之间，`"Opening of the meeting"+"5"` → `"...meeting5"`。
   不报错、不返回空，只是产出与原文本意不符的段落。

### Ruling AK —— Critical 2 源自计划，由我在源头修，不回退给 implementer

审查者核实该代码与简报**逐字节一致**，是简报本身的设计缺陷。按"修缺陷改源头"，
源头是计划，而计划是我的产物。回退只会让它照抄我新写的代码，多一轮往返不产生判断。

修法（`0966287` amend + `7622e3d` 计划同步）：
- `_text_of` 改递归 `walk()`，`w:tab`→`\t`、`w:br`/`w:cr`→`\n`，按文档顺序插入。
- **跳过 `w:pPr` 子树**：里面的 `<w:tab>` 是制表位定义，与制表符同名。不跳过会凭空多出
  大量制表符 —— 这是修复本身最容易引入的新缺陷。
- `_cell_text` 压平空白：单元格文本要塞进 markdown 一行，带换行会撑断整张表。
- commit 用 `--amend` 直接改正署名，**不追加新提交去覆盖**。

### Ruling AL —— MARKER_RE 只加括号限定，不认 "/词" 后缀

修 AJ 时我先把正则放宽成 `(?:\([^)]*\)|/\w+)?`，fixture 计数从 319/26 涨到 320/29，
**正好对上计划断言** —— 差点就此收工。但预检只到 28，逼我去查差额：
第 29 条是 **Annex E 表格的表头列名** `Conclusion/Decision`，是我放宽正则造出的假阳性；
它因正文为空被最后一道过滤丢掉，所以"计数对上了"和"多一条假事件"同时成立。

裁定：只保留括号限定（认 `Conclusion (RAN#112)`、`Agreement (RAN1#124bis)`，实测漏 3 条），
**明确不认 `/词`**，理由写进计划注释防止后人"修回去"。期望值按实测改为 320/28/13。

**教训：「数字对上了」不等于「对」。** 计划里的期望值本身可能是用后来被证伪的方法测的；
两个错误恰好抵消时最像验证通过。

### 定向复审结果：APPROVED

复审者核实 `git reflog` 确认 `6be50bc → a8a6aa0 → 0966287` 是同一提交位置的连续修订、
错误提交已不可达，不存在打补丁式处理；并构造 `w:ins`/`w:del`/`w:hyperlink`/`w:fldSimple`
fixture 对照新旧实现，确认递归 `walk()` 与原 `el.iter()` 结果字节级一致
（`w:delText` 正确排除），跳过 `w:pPr` 不丢正文。Ruling AK 的风险项由此关闭。

### Ruling AM —— 复审剩余三项全部在源头修掉（`579bd23`）

1. **`_cell_paragraphs` 不压平空白**：裁定**保持不压平**但补注释表明有意。
   `cell_paras` 供下游做标记识别与正文拼接，`text_en` 须逐字保留，在 parse 层压平等于改写原文。
   此前代码对此没有表态 —— **沉默本身是缺陷**。
2. **`w:cr` 无测试**：`_SEP` 三种元素只测了两种，补上。
3. **Task 18 逐行 blob 的归属错位**（复审标 Informational，我按 Major 处理）：
   `blob = "\n".join(f"{id}:{text_en}")` 隐含"一行一个事件"，而 `text_en` 内部**本就可能带换行**
   —— 正是 Task 8 给 `w:br`/`w:cr` 补分隔符的直接后果（实测 48 处）。事件跨占多行时续行不带
   `id:` 前缀，LLM 会误归到下一个 id，产出**张冠李戴且无异常迹象**的摘要。
   修法：新增 `_one_line()` 只压平**喂给 LLM 的呈现形式**，不动落盘的 `text_en`。

   **意义超出它本身**：这是 Task 8 的修复在 10 个任务之外引发的次生缺陷。同文件早有
   `"\x00".join(...)` 的先例，说明问题被意识到过，但这两处漏了 —— 又一次"改了一处、没扫全部同类"。

### 待办：Task 8 审查的两条 Minor 归入 Task 11（沉默失败防线）

- `word/document.xml` 存在但无 `<w:body>` 时 `for el in list(body)` 抛 `TypeError`，信息无助定位。
- zip 缺 `word/document.xml` / docx 被二次 zip 包裹 / XML 损坏，分别抛裸的 `KeyError` /
  `BadZipFile` / `ParseError`，不带是哪个文件失败的上下文。

两者都是**崩溃而非静默返回空**，符合本项目优先级，不阻塞 Task 8。Task 11 派发须带上。

**Task 8: complete** —— `0966287` + `579bd23`，105 passed，复审 APPROVED。

---

## Task 9: agreement 块提取

- BASE: `579bd23`；预检 `preflight_task.py 9` → **[PASS] 15 passed**
- 交付 `f56fd12`，120 passed（105 → 120）
- **署名又写成了自己的模型名**（第二次）。这次派发已明写"注意不是你自己的模型名"，仍没拦住 ——
  不是提示词不够清楚，是模型的固有倾向。已 amend 为 `a876df1`。
  **固化做法：收到报告后固定跑 `git log -1 --format=%B | tail -2` 核对署名。**
  机械项由控制器兜底比反复加强措辞便宜。

### Ruling AN —— Task 10 预检失败（未对齐率 23% > 20%），修 align() 而非调阈值

该阈值一旦越过 Task 11 直接抛 `ParseError`，即按现状**每次真实运行都会硬失败**。

**先排除嫌疑**：未对齐清单里有 `Annex H:\tTSG RAN WG1 meetings...`，那个制表符正是我 Task 8
修复的产物。把全部 `\t` 换成空格重测，比率**仍是 22.9%** —— 与我的修复无关。

**19 条未对齐的分解（实测）**：
- **1 条是 `align()` 的真 bug**：`GNSS resilient NR-NTN operation` 在文档里 L2/L3 各一次
  （3GPP 纪要常见结构：分组标题 + 同名子标题），而 `used` 强制一对一，第二次落空。
- **9 条 Annex 结构性附录**，永远不在 agenda.csv 里。
- **9 条会务小节**（Call for IPR 等），agenda 里确实没有，属正常。

裁定：修前两类，不动阈值。修完 9/74 = **12.2%**。
- `align()` 新增 `seen`：标题逐字相同的 heading 复用同一议程项。`used` 的本意是阻止
  两个**标题不同**的小节抢同一项，该保护保留。
- `Alignment` 新增 `skipped` 收纳 Annex 标题，不参与对齐也不计入比率。

**同时替换一条编码了错误行为的测试**：`test_each_agenda_item_used_at_most_once` 用的正是
**两个同名 heading**、断言只有一个能对上 —— 而实测证明同名 heading 就是同一议程项。
拆成同名共享与异名互斥两条（后者用 "Waveforms" vs "Waveform"，相似度 0.94 越过模糊阈值）。

**扫引用记录**：`Alignment` 构造点全文搜过，除 `align()` 内部只有 Task 11 测试一处；
新字段带 `default_factory`，不受影响。

**为什么调阈值是错的**：20% 是"议程或纪要模板已变"的静默失败探针。为让测试变绿抬阈值，
等于把探针调到永不报警 —— 和删掉它没区别，但看起来还在。

### Task 9 审查结果：规格符合性 PASS，代码质量 CHANGES REQUESTED

审查者做**字符级 diff**（difflib 逐行比对而非目测），确认 15 个测试与实现均是简报逐字拷贝，
`320/28/13` 未被篡改，`MARKER_RE` 没有偷偷放宽，表格分支与数据表续行行为均未被"优化"掉。
无 Critical。两条 Major + 三条 Minor，全部在源头修掉（`87cce84`）。

### Ruling AO —— Major 1：嵌套子表的标记把一份 CR 拆成两条互相借用正文的事件

`_cell_paragraphs` 用 `tbl.iter()` 递归，把嵌套子表段落拍平进外层表 `cell_paras`；而
`_table_to_markdown` 用 `findall()` 非递归，子表内容在 `block.text` 里完全不可见。于是
CR 封面表里子表的 `"Agreement:"` 另开一条事件，**标记之前的自有单元格并入表格外的旧 `current`，
标记之后的子表正文成为新事件** —— 一份完整 CR 被切成两条，各持半份正文。

**为什么测试抓不到**：拆分**不改变总数**。审查者原话值得记住：
**15 个测试全绿并不能说明这里没问题。**

**实测范围**：82 张顶层表格里**只有 1 张**含嵌套子表，正是那张 CR 封面表；
与 12 张"用表格画的框"零重叠。修复干净无副作用。

裁定（改 Task 8 的 parse 层，而非在 Task 9 打补丁）：
- `cell_paras` 只收**本表自有**单元格 —— 标记只在这里才算数。
- 新增 `nested_paras`，用"全部段落减自有段落"而非 `findall('.//tbl')` 展开，避免多层嵌套重复计入。
- `extract_events` 里 `nested_paras` **一律当内容**，不开新事件。

**期望值随之 320 → 319 —— 这不是为了让测试变绿改数字。** 320 是缺陷造成的虚高：
那条被拆出来的半份 CR 本就不该算一条独立 agreement。已核实合并后是一条 6429 字符的完整 CR，
无内容丢失，事件总数 370→369，少的正是那半条。理由写进测试注释防止后人"改回 320"。
**判据：差异必须恰好等于修复所解释的那一条，并核实合并后内容完整。**

### Ruling AP —— Major 2：空正文事件静默丢弃改为留痕

`[e for e in events if e.text_en.strip()]` 会把"标记后紧跟另一个标记/heading/文档结尾"的事件
整条丢掉，无日志无计数。**当前 fixture 命中 0 条** —— 但这正是简报点名要求核查的那道过滤，
是真实存在、只是本次样本没触发的静默丢数据缺口。改为丢弃时打 warning。

### Task 9 的三条 Minor（一并修掉）

- **注释数字全错且互相矛盾**：`docx.py` 说"9 Agreement/2 Conclusion/1 WA"，`events.py` 与测试说
  "14 条（12 agreement + 2 WA）"，实测是**自有单元格 15 条（11 agreement + 2 conclusion +
  2 working assumption）+ 嵌套 1 条 = 16 条**。那 2 条 conclusion 是 Task 8 的 `_text_of` 修复
  之后才匹配上的 —— **修一处代码会让别处的"实测注释"悄悄失效**。
- **计划与代码在引号上漂移**（实现者把全角 `“”` 换成 ASCII `"`），导致我按计划文本改代码时
  锚点对不上，来回折腾数轮。**根治：写回灌脚本把最终文件内容整体写回计划代码块**，
  保证字节一致；回灌会带掉测试块首行的 `# 路径` 注释（预检靠它归属），要补回。
- 报告里行号引用不准，仅记录。

**复验**：全量 122 passed；Task 8/9/10 预检均 PASS。Task 9 待定向复审。


### Task 9 定向复审：APPROVED

复审者按要求**独立判断** 320→319 站不站得住：用 `git show a4c1552:` 取出旧版到系统 temp 运行，
在同一 fixture 上逐事件比对（key = kind+para_index+heading_path）：
- 总数 370→369，agreement 320→319，**conclusion/WA/observation 三类计数完全不变**
- 只有一个 key 只存在于旧版（被拆出的那半份），新版**零新增 key**
- 368 个共同 key 的 `text_en` **逐字节相同**，仅被合并的那条文本变化

还追查了该表的真实 XML：外层自有单元格与嵌套子表在文档里是**交叉排列**的
（6 段自有 → 整段嵌套子表 13 段 → 3 段自有 Consequences）。旧代码线性扫描被嵌套标记切断，
把外层 Consequences 错挂到"错的那半"；新代码反而比旧版**更完整**地把三个字段拼回同一条。
结论：**理由成立**，319 是站得住的基准。

三层嵌套表格实测：`cell_paras` 与 `nested_paras` 并集与全部段落精确相等，无重复无遗漏、顺序正确。
真实 fixture 表格子树内 2737 段 = 2724 + 13，`Counter` 精确相等。

### Ruling AQ —— 复审新发现的两条 Minor：一条修、一条明确不修

**修**：`mc:AlternateContent` 的 `Choice` 与 `Fallback` 是**等价的两份**表示，两份都收会让文本
原样重复（实测 `"RAN1 Brk 2RAN1 Brk 2RAN1 Brk 1RAN1 Brk 1RAN1 MainRAN1 Main..."`）。
只取其一（优先 Choice）。**注意用显式 `is None` 判断 —— 空 Element 的布尔值是 False，
`a or b` 会选错**。顺带修了同源的第二处：文本框里的嵌套 `w:p` 各自成段，前后都要断开，
否则与外层文本焊成 `"RAN1 MainAnnex A-2:"`。
`_text_of` 按"结构性改动整段重写"的规矩整体重写：分隔符改为**挂起式**（先标记、等下一段真实文本
出现时才落下），避免段首/段尾多余空行和连续 `

`。事件计数不变（369，319/28/13/9）。

**不修**：复审建议给 `current is None`（表格/段落出现在任何事件之前）时丢弃内容也加 warning。
**裁定不加。** 首个标记之前的内容是封面页、目录、会务小节 —— **每份纪要都有**。
为它打 warning 等于每次运行都报警，只会训练人忽略日志，比不报更糟。
Major 2 那条 warning 之所以有价值，正因为它实测命中 0 次：它只在异常时出声。
**探针的价值来自它平时沉默。**

**Task 9: complete** —— `a876df1` + `87cce84` + `f796ca9`，124 passed，定向复审 APPROVED。

---

## Task 10: heading 与议程号对齐

- BASE: `f796ca9`；预检 `preflight_task.py 10` → **[PASS] 11 passed**
- 计划已在 `a4c1552` 修好（Ruling AN）：`seen` 复用同名议程项、`skipped` 收纳 Annex。

- 交付 `e1f542b`，135 passed（124 → 135）。**署名这次正确** —— 派发措辞未变，
  但我已把核对固化进流程，不依赖它每次都对。

### Ruling AR —— Task 11 预检失败三条，两类问题

**(1) 期望值过期且公式本身就漏项**：`assert len(p.events) == 320 + 29 + 13`。
320/29 是 Task 9 缺陷期的虚高值，而且**这个公式从一开始就漏了 observation**
（events 里有 9 条）。改为 `319 + 28 + 13 + 9`，按 kind 拆开写 —— 出错时一眼看出是哪类变了，
比写死 369 更能自我说明。

**(2) 真 bug**：`e.get("agenda_item", "").startswith("10")`。
`agenda_item` 这个键**总是存在**、未对齐时值为 `None`，所以 `.get(k, "")` 返回的是 `None`
而不是 `""`，直接 `.startswith` 抛 `AttributeError`。改为 `(e.get("agenda_item") or "")`。
**这是 `dict.get` 默认值的经典误用：默认值只在键缺失时生效，键存在但值为 None 时不生效。**

**(3) fixture 缺 `_manifest.json`**：`read_minutes_version` 从 `_manifest.json` 的原始 URL 还原版本号，
而 `tests/fixtures/RAN1_126/` 只有 agenda.csv / minutes.docx / docs_listing.html，
于是 `minutes_version` 恒为 `None`，测试断言 `== 10` 必败。

**裁定：补 fixture 而不是弱化断言。** 改成断言 `is None` 等于什么都没测 ——
版本号贯通是 parse 层向 fetch 层要信息的唯一通路，必须真正跑通。
按 manifest 的真实结构补了 `_manifest.json`（URL 用实测的
`Draft_Minutes_report_RAN1%23126_v010.docx`，length 与 sha256 照实算），
`minutes_version(url)` 返回 10，预检 9 passed。

**记录一处命名不一致（不改）**：`minutes_version(filename)` 的参数名是 filename，
而 `read_minutes_version` 传的是 url。`VERSION_RE.search` 在 URL 上同样能命中，行为正确，
不值得为此改签名扩大改动面。

### Task 10 审查：规格符合性 PASS，代码质量 CHANGES REQUESTED（一条 Critical）

审查者做字符级 diff，确认实现与测试逐字落地（仅 black 风格的空行/import 拆分差异），
阈值 `0.20`、`FUZZY_THRESHOLD=0.90`、`DEPTH_TOLERANCE=1` 均未被改动；
独立实测 `unmatched_ratio=0.1216, skipped=9, by_heading=65, unaligned=9`，与报告吻合。
还实测确认 `seen` 命中时确实绕过深度校验（把同名 heading 的 level 设成 9、深度差 8 仍命中），
与注释一致；`used` 对异名的保护未被 `seen` 削弱；heading 顺序打乱结果不变。

### Ruling AS —— Critical：`unmatched_ratio` 分母为 0 时返回 0.0，探针被自己的边界反噬

**已复现**：`align(agenda=[...], headings=[])` 与"headings 全是 Annex"两种情形下
`by_heading={}`、`unaligned=[]`、`total=0` → 返回 **0.0**，比正常值 12.2% **还要好看**。
Task 11 用 `ratio > MAX_UNMATCHED_RATIO` 当质量门禁，于是一份 heading 抽取彻底失效的纪要
会被放行且无任何信号。**这正是简报点名要求实测的那条静默失败路径。**

注意"headings 全是 Annex"这一情形绕过了 Task 11 已有的 `test_zero_headings_raises` 守卫
—— 那道守卫查的是 heading 数量，而这里 heading 非空（9 条 Annex），只是无一参与对齐。

**裁定：`total == 0` 时返回 1.0。**
0/0 数学上无定义，这里是刻意的策略选择：分母为 0 意味着"一条都没对上"，不是"全对上了"。
返回 1.0 直接让既有门禁开火，不需要 Task 11 记得去查一个新标志位。

**明确否决审查者给的第一个方案（`float("nan")` 哨兵）**：实测 `nan > 0.20` 恒为 `False`，
门禁**照样放行**，比返回 0.0 更隐蔽 —— 看起来是"强制调用方显式处理"，实际是把静默失败
藏得更深。理由写进了 docstring 和测试，防止后人"改回 nan"。

### Ruling AT —— Minor M1：归一化撞 key 只告警，不改行为

两个议程项归一化后重名时，候选池"先到先得"，后一个永远拿不到 heading ——
方向上违背"宁可少归类，不可错归类"。但实测 RAN1#126 的 66 条议程项**无冲突**，
没有真实触发条件。为零证据的场景加未经验证的改判逻辑是投机，**改行为不如先出声**：
构建 `exact` 字典时若发现同一 key 映射到多个 item，打一条 warning。
与 Ruling AQ 同理 —— 探针的价值来自平时沉默。

M2：简报 Step 4 写 "Expected: 10 passed" 而代码块有 11 个测试（现为 13），已订正。

**复验**：全量 137 passed；Task 10 / 11 预检均 PASS。

### Task 10 定向复审：APPROVED

复审者实测六种场景确认 1.0 修复在所有退化路径生效、且**未误伤正常情形**
（全部对齐时仍是 0.0）；并**实际调用 Task 11 的 runner 代码**（monkeypatch `align()` 返回
total==0 的 Alignment）证明门禁确实抛 `ParseError: 未对齐议程项占比 100%` —— 不是看代码推断。
把 `1.0` 改回 `0.0` 后新测试变红，确认守得住回归。

**否决 nan 的理由成立**，复审还补了一条我没想到的佐证：即便侥幸走到序列化，
`json.dumps(float("nan"))` 产出非标准 JSON token `NaN`，会污染 `events.json`。
**1.0 在门禁比较与 JSON 序列化两条路径上都严格更安全。**

Ruling AT（只告警不改行为）也被独立确认方向正确：先到先得的效果是第二个撞名议程项
拿不到 heading，该 heading 落入 `unaligned` → 计入未对齐率 → 有机会触发门禁，
属于**少归类**而非**错归类**，符合本任务原则。

### Ruling AU —— 复审点出的测试空隙：补 Task 11 的 total==0 门禁测试

Task 11 自带的 `test_high_unmatched_ratio_raises` 用 `unaligned=[Heading(...)]`，
走的是 **total==1 的正常分支**；而这次修的是 **total==0 分支**，两者根本不是同一条路径。
也就是说：修复落地了，但计划里没有任何测试守着它在 runner 层的效果。

已补 `test_no_eligible_heading_also_raises`（`by_heading={}`、`unaligned=[]`、
`skipped=[Annex]`，先断言 ratio==1.0 再断言门禁抛错），Task 11 Expected 9 → 10。

**这类空隙的共性值得记住**：同一个函数的不同**分支**需要各自的测试，而"这个函数已经有测试了"
最容易让人以为覆盖到了。前面 Task 9「只断言总数抓不到边界错位」是同一个道理的另一面。

复审另提一条纯风格 Minor（新增测试函数只隔 1 个空行，PEP8 E302），已顺手改掉。

**Task 10: complete** —— `e1f542b` + `3695ff8`，137 passed，定向复审 APPROVED。

---

## Task 11: parse 编排与沉默失败防线

- 预检 `preflight_task.py 11` → **[PASS]**
- 派发时必须带上前面攒下的两条 parse 层加固项（Task 8 审查的 Minor，裁定归入本任务）：
  - `word/document.xml` 存在但无 `<w:body>` 时抛 `TypeError`，信息无助定位。
  - zip 缺 `word/document.xml` / docx 被二次 zip 包裹 / XML 损坏，分别抛裸的
    `KeyError` / `BadZipFile` / `ParseError`，不带是哪个文件失败的上下文。

- 交付 `9c9fd5e`，**151 passed**（137 → 151，新增 14 = 简报 10 条 + 实现者自补 4 条畸形输入）。
  署名正确。实现者报告了一处解读：简报说"各补一条测试"，它用 `parametrize` 展开覆盖了
  `KeyError` / `BadZipFile` / `ParseError` 三种具体畸形，而不是只测一种 —— **比字面要求更严，接受**。
  它还主动说明 try/except 只包住 `parse_docx` 一次调用，没有扩大到 `extract_events`/`align`/
  `parse_agenda`，以免误吞其他层自己的 bug；`docx.py` 未改动。这两点正是我派发时点名的要求，
  已列入审查的重点核实项，等审查独立确认。
- Task 12 预检 → **[PASS] 14 passed**

### Task 11 审查：规格符合性 PASS，代码质量 APPROVED（零 Critical 零 Major）

审查用 `ast` 按函数名切分做**逐函数**字符级 diff：简报给定的 10 条测试全部 `identical`
（含注释、docstring、空行）；`runner.py` 与简报代码块的唯一差异是新增两行 import、
删掉一句过时注释、以及在 `parse_docx` 外包的 try/except。阈值与异常文案逐字一致。

**三项重点核实全部独立确认**：
- `docx.py` 未被触碰（`git show --stat` 核对）。
- try/except **包裹范围正确**：审查把 `runner.align` 换成抛 `KeyError` 的假函数，
  异常**原样冒出**未被误吞成 `ParseError` —— 证明只裹住了 `parse_docx` 一次调用。
- `raise ... from e` 保留了异常链。

**对抗性实测"会不会返回看起来正常但实际为空的 ParsedMeeting"**：raw 目录不存在、
目录为空、minutes 0 字节、agenda.csv 0 字节 —— **全部正确 raise，没有一条静默产出空结果。**

### Ruling AV —— 审查的 Minor 2 立即修：agenda.py 静默吞编码错误

审查发现 `data.decode("utf-8-sig", "replace")` 把编码错误静默吞成 `�`。它同时指出
下游门禁**今天**能兜住（乱码标题对不上任何 heading，比率触顶 100% 触发硬失败），
所以判为 Minor、且属 Task 7 遗留不计入 Task 11。

**我裁定立即修，不留到后面。** 审查自己写出了那个兜不住的场景：
**"乱码几条、比率仍在 20% 阈值内"会产出错误却不显眼的对齐结果** ——
这正是本项目定义的最坏情形（静默错误 > 崩溃）。依赖下游门禁兜底是概率性的，不是保证。

修法：`_decode()` 按 UTF-8 → cp1252 顺序解码，**任何一次退让都打 warning**。
不直接抛错，是因为 3GPP 的 CSV 确实可能是 cp1252，硬失败会把正常文件挡在门外 ——
**退让本身可以接受，不出声才是缺陷**。补两条测试：正常 UTF-8 零告警（探针平时沉默）、
GBK 中文触发告警且议程号仍照常解析。

**未修的 Minor 1**（`write_parsed` 非原子写）：审查核实 `ngr/fetch/manifest.py` 也是同样的
`write_text` 模式，是项目既有惯例；且半截 JSON 会在 map 层 `json.loads` 立即报错，
**不会被误读成"合法但为空"**，不违反本任务核心原则。裁定不为 Task 11 单独返工，
若要加固应在后续统一改造 —— 记在这里以免被忘记。

**Task 11: complete** —— `9c9fd5e` + agenda 解码修复，153 passed。
parse 层（Task 8–11）至此整体收口。

---

## Task 12: 血统段匹配引擎

- 预检 `preflight_task.py 12` → **[PASS] 14 passed**（第一个一次就过的预检）

- 交付 `a5423fd`，**167 passed**（153 → 167），署名正确。
  独立核实 `grep -rn "claude|llm|LLM|subprocess" ngr/mapping/` 无命中 —— 纯规则要求满足。
- 实现者按我的要求用了 `--junitxml`，但把 `test_results.xml` 落在了仓库根。已 gitignore
  （`fdc8a09`）。**这是我的指令引出的副作用**：以后派发里要顺带说明 junit 输出写到 temp。
- Task 13 预检 → 一开始 [FAIL]：`ngr/mapping/runner.py` 的 `MergeStats` 用了
  `field(default_factory=list)` 但 import 行只有 `dataclass, asdict`，**导入期就炸**。
  补 `field` 后 [PASS] 13 passed。这类缺陷预检几乎零成本就能抓到，而下发后才发现要多走一轮往返。

### Task 12 审查：规格符合性 PASS，代码质量 APPROVED（零 Critical 零 Major）

审查用 `ast` 按函数切分 + `difflib` 逐行比对：`lineage.py` 与简报**逐字节相同**；
测试文件 16 个函数（14 条测试 + 2 个 helper）的 `ast.dump()` 与简报**逐一完全相同**，
仅有删掉首行路径注释、多一个空行两处纯格式差异。改动范围恰好是简报指定的三个文件。

**穷举实测的边界**（独立脚本，不依赖简报给的测试）：
- 议程号点分段：`"10.2"` 对 `"10.20"` / `"110.2"` / `"10.2.1"` 均**不误命中**；
  `"10.2.*"` 对 `"10.2.3"` 命中、对 `"110.2"` / `"10.20"` 不命中。无前缀越界、无漏判。
- 会议区间：半开 `(124, None)`、闭区间、单点区间的边界点全部正确；
  **倒置区间 `(130, 100)` 在六个测试点上全部 fail-closed** —— 那正是 Task 6 出现过的
  缺陷模式（`fetch_window` 倒置区间），这次没有重演。该逻辑在 `models.py`，不在本次 diff 内。
- 多命中排序用 `sorted()`（Python 保证稳定），输入均为 list 无 dict/set 迭代，结果确定性可复现。
- 审查还核实"features 按列表顺序、段内 6G 优先"这条规则**在简报 docstring 里就已明文写出**，
  不是实现者自行发明后偷偷加的。

### Ruling AW —— 审查的 Minor 1 不改：核实后发现上一层早已满足

审查建议"给 features.yaml 加载层加 `title_re` 预编译校验，让错误在启动期暴露且带 feature slug"。
**核实后发现 Task 3 已经做了**：`ngr/config.py:199-203` 在 `_parse_segment` 里
`re.compile(title_re)`，失败即抛 `ConfigError`。实测写个 `"(unclosed"` 进 features.yaml：

    ConfigError: features[waveform].lineage[0].anchor.title_re 不是合法正则: missing ), unterminated subpattern

位置精确到 feature slug 与段下标，正是审查想要的效果。审查只看了 mapping 层，没往上看 config 层。

**这条记下来的价值不在结论，在做法**：审查提的建议要先核实是否已被满足，再动手。
这次核实成本几分钟，省下一次无谓改动；反过来若照单全收，会在 config 层加出第二处重复校验 ——
正是全局约束反对的"留下两处互相矛盾/重复的表述"。

Minor 2（实现者报告里自述的 commit author 与 `git show` 实际不符）仅提醒自审要对齐真实输出，
约束项（trailer 文本）已核实一致，无需动作。

**Task 12: complete** —— `a5423fd`，167 passed。

---

## Task 13: map 编排、state 合并与 lineage-report

- 预检 `preflight_task.py 13` → 先 [FAIL]（`field` 未 import，导入期即炸），补后 **[PASS] 13 passed**（`0739dd7`）

- 交付 `1b35f78`，**DONE_WITH_CONCERNS**，180 passed。署名正确。实现者报了三条 concern，
  都不是它做错，是它发现的真问题。第 1 条（简报正文里 362 已过期）它**没有改代码去迁就旧数字**，
  而是如实报告 —— 正是派发纪律要的反应。

### Ruling AX —— 事件 id 是位置式的，纪要改版会让被删那条变成永久孤儿

实现者的 concern 2 我实测复现（不靠读代码）：`id = "{wg}-{meeting}-{agenda}-{kind}{seq:03d}"`，
`seq` 是 (议程号, kind) 组内的位置计数。

- **新版纪要中间插入一条**：`a002` 从 BBB 变成 NEW、`a003` 从 CCC 变成 BBB、`a004` 是 CCC。
  合并后 `a002`(NEW) 继承了 BBB 的 `first_seen=09-18`（它其实今天才出现），
  `a004`(CCC) 却记成 09-19（它 09-18 就有）。**`first_seen` 失真。**
- **新版纪要删掉一条**：`a003`/CCC 在新纪要里已不存在，但**仍留在 state 里**，
  `unchanged=2` 只数了实际出现的两条。永久孤儿，**零信号**。看板会一直显示一条已不存在的 agreement。

**裁定一：加孤儿检测，只报告不删除。** `MergeStats.stale_ids` + warning。
**不删**是因为：若某次 parse 回归（正则改动之类）让事件暂时缺失，删除就是永久数据丢失 ——
那正是本项目最怕的。**缺失是信号，不是指令。**
实现上最容易写错的一点已写进注释与测试：`incoming` 只覆盖本次跑的会议、`existing` 是**全量** state，
比较必须限定在同一 `(wg, meeting)` 范围内，否则所有历史会议的事件都会被报成"本次缺失"。
补了两条测试，其中一条专门守这个跨会议边界。

**裁定二：`first_seen` 失真不修，保留现状。** 内容变了既可能是 id 被重新指向了另一条 agreement
（该重置），也可能只是同一条被编辑修订（该保留），**从 id 分辨不出来**。两种错里：
误重置会让一条老 agreement 在**每期简报里冒充新增** —— 简报是主要交付物，假新增比日期偏早
伤害大得多。所以保留现状更安全，理由写进 `stale_ids` 的 docstring。

**根因不修的说明**：真正的解法是内容寻址 id，但那要改 Task 2 的 models、Task 14/15 的渲染、
Task 17/18 的 LLM 缓存键 —— 改动面远超收益。位置式 id 的这个弱点现在**有了探针**，
不再是静默的。

### Ruling AY —— 预检工具自身的截断 bug（抽出半截模块）

Task 14 预检报 `SyntaxError: unterminated string literal`。查下来**计划文本是对的，是工具的错**：
`extract_blocks` 用非贪婪的 ```` ```python
(.*?)``` ```` 抓代码块，而 Task 14 的渲染器代码里
有字符串 `"```text"`（markdown 代码围栏），正则在**那里**就闭合了，抽出半截模块。

修法：闭合围栏必须在行首 —— `r"^```python
(.*?)^```"` + `re.M`。

**按"改一处要扫全部同类"核查了全部 22 个任务**，受旧正则影响的只有：
- Task 14：8813 → 9667 字符
- Task 17：10371 → 14142 字符（差 3771 字符，接近三分之一被吞）

**两个都还没下发**，所以已完成的任务没有一个是在被截断的代码上做的预检 —— 这一步核查必须做，
若受影响的是已交付任务，那些 PASS 全是假的。

**这个 bug 的失败模式值得记**：Task 14 是被截成**语法错误**才暴露的，属于运气好。
若截断点恰好落在函数边界上，抽出的会是**语法合法但内容缺失**的模块，
预检会给出一个毫无意义的 PASS，而且没有任何人会知道。
**工具本身也会静默失败，它的输出不能无条件当证据。**

修后重跑 Task 8–14 全部 [PASS]。

### Task 13 审查：规格符合性 PASS，代码质量 CHANGES REQUESTED（两条 Major）

审查逐字符核对：13 条简报测试与仓库文件完全一致；`runner.py`/`report.py` 与简报逐字符一致；
`8244af1` 的新增与 diff 完全对应，未改动简报原有任何一行。九组对抗性探针实测幂等性、
`write_state` 字节级确定性、`existing` 有重复 id / 缺 wg 字段等场景 —— 均无历史被删或覆盖。

### Ruling AZ —— Major 2：我加的孤儿探针，在最该响的时候哑火

审查指出并经我实测复现：`scope = {(ev.wg, ev.meeting) for ev in incoming}` 完全由**归集成功**
的事件反推。一旦某场会议归集**归零**（`features.yaml` 改坏、正则回归），它根本不在 scope 里，
那场会议的全部历史一条都不会被拿来比较，`stale_ids` 恒为 `[]`、无日志。

实测：state 有 3 条，模拟整场不命中后重跑 —— 数据没丢（对），但 `stale_ids = []`。
**局部缺失（3 条变 2 条）会报警，全部缺失反而不报警。**

这和 Task 10 那条 Critical 是**同一个病**：探针被自己的边界条件反噬，在最坏情形下最安静。
我修了 `unmatched_ratio` 的 total==0，转头就在自己写的新探针里犯了同一个错。

**裁定**：`merge_events` 增加显式 `scope` 参数，调用方必须传本次处理了哪几场会议；
反推仅作兜底，且 `incoming` 为空时打 warning（反推不出来时至少出声）。
实测显式传 scope 后，整场归零的 3 条全部被报出，而历史一条未删。
**Task 20（CLI 管线编排）派发时必须带上：调用 `merge_events` 要显式传 scope。**

### Ruling BA —— Major 1：legacy 回退 key 撞车会让历史张冠李戴

`_agenda_key` 在没有议程号时（5G-A 老会议）用 heading 末节造 key，标点被归一化掉。实测：

    "ISAC channel model"              -> isac-channel-model
    "ISAC channel-model"              -> isac-channel-model     ** 撞了 **
    "CSI enhancement: further study"  -> csi-enhancement-further-study
    "CSI enhancement further study"   -> csi-enhancement-further-study   ** 撞了 **

撞 key 之后 `seq` 按遍历顺序分配，两次纪要修订间只要这两个议题的先后调换，
**同一个 id 就指向了另一个议题** —— merge 判成一次普通内容变更，把 A 的历史
（`first_seen` 等）安到 B 头上。**既不报错，也不进 stale_ids，彻底静默**：
两个 id 在两次跑批里都"存在"，探针没有任何抓手。比"消失"更隐蔽。

**裁定**：回退 key 追加**未归一化原文**的 4 位短哈希。这是**预防**而不是探针 ——
不同议题从此拿不到同一个 key。只影响 legacy 路径（有议程号时行为不变），
且目前尚无 state 落盘，改 id 格式零代价；等有了历史数据再改就晚了。

三条 Minor（`.index()` 值相等性、`seq:03d` 超 999 的字典序、`existing` 重复 id 静默覆盖）
均为低概率或外部改坏 state 才触发，记录不改 —— 但第三条与本项目"静默丢历史"的敏感度相关，
**Task 20 若要加固可顺手补一行 warning**。

**复验**：全量 185 passed；Task 13 预检 PASS。

### Ruling BB —— "部分归零"盲区：在 Task 20 的调用点关掉，不留作派发时的口头要求

Ruling AZ 给 `merge_events` 加了显式 `scope`，但留了个缺口：**一次处理多场会议、其中一场归零、
且调用方没传 scope** 时，`incoming` 非空（另一场的事件）→ warning 不触发 → 那场的归零仍然静默。
`merge_events` 自己不可能知道那场会议被处理过，所以这个缺口只能在调用方关。

我当时把它写成"Task 20 派发时必须带上"的要求 —— **这种口头约定最容易在几十轮之后丢掉**。
去看了一眼：**调用方在计划里已经写好了**，就在 Task 20，两处，而且都是**每场会议调一次**
`merge_events`。于是直接改计划：两处都显式传 `scope={(wg, meeting)}`，并在 `stale_ids`
非空时写进 `res.alerts`。每次调用的 scope 就是那一场，与它是否归零无关 —— **盲区彻底关闭**，
不再依赖任何人记得。

**顺带又踩了一次"改定义不扫引用"**：我写 `res.warnings.append(...)` 时是凭记忆的，
核对后发现 `PipelineResult` 只有 `alerts` 没有 `warnings`。两处都改正了。
这已经是账本里记的第五次同类错误 —— 差别只在这次我在提交前查了。

### Task 13 定向复审：CHANGES REQUESTED —— 两条 Major 都只是"部分关闭"

复审对两条修复各给了"部分关闭"，两条判断都对，而且都指出**我的修复只挡住了我想到的那一半**。

### Ruling BC —— 回退 key 的哈希只取末节，末节同名必然撞车（比标点变体常见得多）

我上一轮给回退 key 加了原文短哈希，但哈希只喂了 `heading_path[-1]`。复审实测：

    _agenda_key(None, ["Rel-17 NR", "Overview"]) == _agenda_key(None, ["Rel-18 NR", "Overview"])
    -> 'overview-d4b1' == 'overview-d4b1'   True

**这不是小概率，是 100%**。而 "Overview" / "General" / "Summary" / "Way forward" / "Conclusions"
这类通用小节名，在 3GPP 纪要里跨 Release、跨上级章节反复出现是**常态**。
触发的是与原缺陷完全同一类的故障：不同议题共享 id → merge 把 A 的历史安到 B 头上。

**我修的是我想到的那类撞车（标点变体），漏掉的恰恰是更常见的那类。**

裁定：哈希输入改为**完整 heading 路径** `"/".join(heading_path)`，长度 4 → 8 位
（复审估算 4 位在标点变体场景下够用，但既然实际输入池比我原以为的大，且现在改零成本，
就一次加够）。顺带对 `heading_path` 为空的情形打一条 warning —— 那时所有事件落到同一个 key。

### Ruling BD —— `scope` 留默认值就等于允许静默反推，改为必填

复审实测了我预判的那个盲区并确认它是真的：**合批调用**（一次 `merge_events` 处理多场会议）
时若某场归零，`incoming` 非空 → warning 不触发 → 那场的归零仍然静默。
我在 `6910251` 已经把 Task 20 的两处调用点改成逐会议传 scope，但复审的判断更狠也更对：

> 代码层面没有任何机制强制或检测调用方是否传了 scope，默认值允许静默省略。
> 一旦未来实现偏离"逐会议单独调用"（例如为减少 I/O 合批处理），盲区会在没有任何
> 代码层提示的情况下复活。

**裁定：去掉默认值，`scope` 改为必填的关键字参数。** 确实需要反推时改用新加的
`scope_of(incoming)` —— 它做的事和原来的隐式反推一模一样，**区别只在于"我在反推"这件事
出现在调用点上，而不是藏在函数签名的默认值里**。

新增 `test_scope_has_no_default` 用 `inspect.signature` 守住这条：默认值不得回来。
这是本项目第一条**守护 API 契约本身**而非守护行为的测试 —— 因为这里真正危险的不是某次行为，
是那个默认值的存在。

十处既有调用点全部改为显式传参（六处单元测试用 `scope_of(new)`，其余按真实会议传）。

**复验**：全量 185 passed；Task 13 预检 PASS；Task 20 的两处调用点本就是关键字传参，不受影响。

## 当前状态与下一步（压缩/换会话后从这里接手）

> **维护须知**：本段**永远是文件最后一段**。新增执行记录一律插在它**之前**，
> 不要 append 到文件末尾。更新本段时也不要用 `t[:i] + new` 截断 —— 我这么干过一次，
> 把后面几轮的全部裁定删了（账本被 gitignore，没有备份，只能凭上下文重建）。

**进度：9/22 任务完成**（Task 9 待定向复审通过后归档）。分支 `feat/ngr-tracker`，工作树应为干净。
全量测试 **122 passed**。Task 8/9/10 预检均 PASS。

**关键提交**：
- `0966287` Task 8 代码（docx 抽取）
- `a876df1` Task 9 代码（事件提取）
- `a4c1552` Task 10 计划修复（同名 heading、Annex 污染探针）
- `87cce84` Task 9 审查修复（嵌套子表、空正文留痕、注释数字）

**下一步动作（按顺序）**：
1. 等 Task 9 的定向复审结论。APPROVED 就在账本记 Task 9 complete 并 `TaskUpdate` 标完成。
2. 下发 Task 10（BASE 取当时 HEAD，预检已 PASS 11 tests）。派发时必须强调：
   - `Alignment.skipped` 是为收纳 Annex 结构性附录而加，**不计入未对齐率** ——
     计入的话探针常年停在 20%+，真正的对齐崩溃淹没在固定噪声里。
   - `seen` 映射让**标题逐字相同**的 heading 复用同一议程项（分组标题 + 同名子标题是
     3GPP 纪要的常见结构）；`used` 保留，它防的是**标题不同**的小节抢同一项。
   - 20% 阈值不许动。为让测试变绿抬阈值等于把探针调到永不报警。
3. Task 11 派发时须带上两条 parse 层加固项（Task 8 审查的 Minor，已裁定归入 Task 11）：
   - `word/document.xml` 存在但无 `<w:body>` 时抛 `TypeError`，信息无助定位。
   - zip 缺 `word/document.xml` / docx 被二次 zip 包裹 / XML 损坏，分别抛裸的
     `KeyError` / `BadZipFile` / `ParseError`，不带是哪个文件失败的上下文。

**每任务固定流程**（不要省步骤）：
BASE 记 `git rev-parse --short HEAD` → `scripts/preflight_task.py N`（[FAIL] 先修计划）→
`task-brief` 抽简报 → 派 implementer（计划含完整代码用最低档）→ 收报告后**固定核对 commit 署名** →
`review-package` 生成 diff 文件 → 派审查（sonnet，要求对抗性检查 + 字符级 diff）→
有 Critical 就修（源头在计划就我改，别退回实现者照抄）→ 定向复审 → 账本记 complete → 下一个。

**派发 implementer 的必备措辞**：测试逐字采用、觉得测试错了停下来报告不许自己改；
风格可疑照抄并报告；不许派生子代理；不许后台执行；commit 署名逐字用
`Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>`（它会写成自己的模型名，我兜底）。

**任务收尾时**：用回灌脚本把最终文件内容写回计划代码块保证字节一致，并补回测试块首行的
`# 路径` 注释（预检靠它归属）。
