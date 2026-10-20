# 6G (Rel-20) RAN 进展看板

> 生成于 2026-10-20 · 最新会议 RAN2#134

| 特性 | 阶段 | 血统 | 累计 Agr. (6G/5G-A) | 本期新增 | 最近活动 | 未决 |
|---|---|---|---|---|---|---|
| [ISAC 通感一体](features/isac.md) | 收敛中 | 5G-A→6G | 37 / 213 | **+25** | RAN2#134 | 5 |
| [AI/ML 空口](features/ai_air_interface.md) | 未启动 | 5G-A→6G | 0 / 525 | **+0** | RAN1#126 | 0 |
| [6GR 波形与帧结构](features/waveform.md) | 收敛中 | 6G 原生 | 28 / 0 | **+0** | RAN1#126 | 5 |
| [6GR 信道编码与调制](features/channel_coding.md) | 收敛中 | 6G 原生 | 34 / 0 | **+0** | RAN1#126 | 6 |
| [6GR 空口评估假设](features/evaluation_assumptions.md) | 收敛中 | 6G 原生 | 11 / 0 | **+0** | RAN1#124 | 5 |
| [6GR 能效](features/energy_efficiency.md) | 收敛中 | 6G 原生 | 43 / 0 | **+25** | RAN2#134 | 6 |
| [6GR 多天线系统](features/multi_antenna.md) | 收敛中 | 6G 原生 | 315 / 0 | **+0** | RAN1#126 | 6 |
| [6GR 唤醒信号与运行机制](features/wus.md) | 收敛中 | 6G 原生 | 33 / 0 | **+0** | RAN1#126 | 5 |
| [6GR 非地面网络](features/ntn.md) | 收敛中 | 6G 原生 | 24 / 0 | **+14** | RAN2#134 | 6 |
| [6GR RRC](features/rrc.md) | 收敛中 | 6G 原生 | 14 / 0 | **+49** | RAN2#134 | 6 |
| [6GR UE 能力框架](features/ran2_ue_capability.md) | 收敛中 | 6G 原生 | 4 / 0 | **+36** | RAN2#134 | 5 |
| [6GR 通用设计与新业务](features/ran2_general_design.md) | 收敛中 | 6G 原生 | 2 / 0 | **+13** | RAN2#134 | 6 |
| [6GR 用户面架构](features/ran2_user_plane.md) | 收敛中 | 6G 原生 | 8 / 0 | **+53** | RAN2#134 | 6 |
| [6GR QoS/QoE 与服务感知](features/ran2_qos_qoe.md) | 收敛中 | 6G 原生 | 4 / 0 | **+51** | RAN2#134 | 6 |
| [6GR MAC 与调度](features/ran2_mac_scheduling.md) | 收敛中 | 6G 原生 | 9 / 0 | **+50** | RAN2#134 | 5 |
| [6GR 初始接入与系统信息](features/ran2_system_access.md) | 讨论中 | 6G 原生 | 4 / 0 | **+10** | RAN2#134 | 6 |
| [6GR 寻呼](features/ran2_paging.md) | 收敛中 | 6G 原生 | 5 / 0 | **+6** | RAN2#134 | 5 |
| [6GR 控制面其他议题](features/ran2_control_plane_other.md) | 讨论中 | 6G 原生 | 1 / 0 | **+0** | RAN2#133bis | 6 |
| [6GR 频谱聚合](features/ran2_spectrum_aggregation.md) | 收敛中 | 6G 原生 | 1 / 0 | **+42** | RAN2#134 | 6 |
| [6GR 数据与模型传输](features/ran2_data_model_transfer.md) | 收敛中 | 6G 原生 | 6 / 0 | **+23** | RAN2#134 | 6 |
| [6GR AI/ML 协议支持](features/ran2_ai_ml.md) | 收敛中 | 6G 原生 | 1 / 0 | **+12** | RAN2#134 | 6 |
| [6GR 共用协议其他议题](features/ran2_common_protocol_other.md) | 讨论中 | 6G 原生 | 0 / 0 | **+0** | RAN2#132 | 5 |
| [6GR 提前报告](features/ran2_early_reporting.md) | 收敛中 | 6G 原生 | 2 / 0 | **+23** | RAN2#134 | 5 |
| [6GR 移动性](features/ran2_mobility.md) | 收敛中 | 6G 原生 | 7 / 0 | **+29** | RAN2#134 | 6 |

## 本期新增（最近一次会议 #134）

- **ISAC 通感一体**：新增 25 条
  - 从 RAN2 角度，研究所有 modes 下由 UEs 和 TRPs 作为 TX 和/或 RX sensing entities（SEs）运行，并进一步研究由 SF/aNB 执行的 radio aspects/configuration/report 和 control aspects。还需研究 SE selection 的 criteria、参与节点及所需信息、aNB 与 SF 的协调，以及 moving target mobility 下的 sensing entity selection/re-selection 和 UE sensing entity 移动时的 service continuity；RRC states 视时间允许情况研究。
  - 已记录支持 UEs 和 TRPs 作为 Tx 和/或 Rx SEs 运行。
  - 按 sensing mode，UE 可作为 sensing signal transmitter 和/或 sensing signal receiver；sensing procedures 的研究分为 UE as sensing signal transmitter 与 UE as sensing signal receiver。
- **6GR 能效**：新增 25 条
  - 指出静态 CDRX timer operations 会在四种情形导致不必要的 PDCCH monitoring：无数据活动、无后续传输、重传无效，以及不能支持单连接内多种业务或动态时延要求。
  - 为适应 DL 和 UL traffic 的动态变化，可考虑采用 NW-initiated 或 UE-initiated solution 来实现 6G CDRX timer adaptation。
  - 提出为 connected mode 设计 single discontinuous monitoring framework：UE 在收到 DL WUS 或到达 periodic CDRX occasion 时，启动配置时长的 PDCCH monitoring。若 UE 在该时长内被 PDCCH 调度，则保持唤醒一段时间，并开始监测可能的 retransmission scheduling。
- **6GR 非地面网络**：新增 14 条
  - 针对 GNSS-free，研究非 UE-location-based mobility（包括 HO、cell selection/reselection 和 measurements）；对于 GNSS-degraded operation，等待 RAN1 进展。NTN 预计会有类似 5G 的 L2 timer 影响，待 RAN1 进一步进展后讨论，并涉及 multi-orbit operation。
  - 对于 GNSS-free，优先采用 non UE-location-based solutions，因为这符合 6G 的 TN/NTN harmonization 目标。
  - 在 NR-NTN 中，RACH 和 C-DRX 的关键 MAC timers 高度依赖基于 GNSS 的 RTT calculations。
- **6GR RRC**：新增 49 条
  - 指出 “inactive” state 与 RRC idle state 在以下方面有根本区别：AS context storage、适用区域内 RRC resume/setup 的 UE identification、AS security requirement，以及 data transfer requirement。
  - 从“inactive”状态和 RRC idle state 转至 RRC connected state，应执行不同流程；从 RRC connected state 转至“inactive”状态和 RRC idle state，也应执行不同流程。
  - 低频流量且高时延容忍度的 IoT cases 明确适合 inactive operation。
- **6GR UE 能力框架**：新增 36 条
  - UE capability change message 在 RRC connected mode 发送给 network，并预期在 mobility 时转发给 target aNB；UE 进入 Idle/Inactive 后如何处理以及是否存储最新信息仍待讨论。下次会议前鼓励各公司线下形成对流程的整体看法，且只预期 co-sourced contributions。
  - 网络实现或 operational policies 可能不处理其未考虑的 use cases 的 capability change requests，也可能不处理 capability change 影响不显著的请求。
  - 收到 UE capability change indication 后，network 可影响 UE 对 problematic situation 的响应；若未收到 indication，network 只能面对 UE 自主恢复行为带来的影响。
- **6GR 通用设计与新业务**：新增 13 条
  - 256-bit AEAD algorithm 有三种 operating modes：Confidentiality（仅 ciphering）、Integrity 和 Combined。
  - combined mode AEAD 使用同一把 cryptographic key 进行 integrity protection 和 ciphering，并可将两者合并为一次操作。编码端先执行 ciphering，再执行 integrity protection（Encryption-then-MAC）。
  - 基于 5G NR 的 RRC configurations，BWP、CORESET 和 SearchSpace 的可能配置规模巨大。原文指出，在不了解专用 RRC configuration 的情况下，对 MAC CE 发起攻击会有较大挑战。
- **6GR 用户面架构**：新增 53 条
  - 分别设置 PDCP 和 RLC 时，PDCP 至少承担安全、按序交付、头压缩、重复检测和重传，RLC 至少承担分段与重组、重复检测和 ARQ；合并层至少承担前述 PDCP 功能，分段与重组方式仍待研究。RAN2 旨在针对 RAN plenary 确定的所有支持场景和架构采用共同协议栈，部署选项不应影响协议栈；Single SN 的开销、处理、分离承载 DC、控制 PDU 分段及 CU-DU split 相关事项仍有待研究或决定。
  - 记录 5G PDCP 重排序机制在 DL 峰值吞吐时导致接收端内存需求高、延迟，并缺乏适应 QoE 的能力这一不足。研究简单的重排序机制以解决该问题。
  - 与 NR 相同，重传有两种触发：RLC retransmission 用于处理 Uu 数据丢失，PDCP reestablishment/recovery；SDU 和 SDU-segment 都需要支持重传。共同的 L2 retransmission function 仅在采用 single SN 时可行，具体方案及 CU-DU split 下的窗口操作、不同终止点时的共同状态报告仍待讨论。
- **6GR QoS/QoE 与服务感知**：新增 51 条
  - RAN2 研究在 QoS profile 不变或变化时，基于预配置范围/值动态调整 L2 参数；QoS profile 变化时需要与 SA2 协调。待讨论的事项包括适用于动态调整的功能、UE 切换条件与行为，以及 DRB 内的粒度和启用建模方式。
  - 可向 scheduler 报告的数据突发信息包括 AS buffer 中已有数据、尚未进入 AS buffer 的当前数据，以及尚未生成的预期数据的突发大小。突发时间信息可包含首个数据包预计可供传输的时间；如何向网络发送这些信息仍待研究。
  - 对于 Scenarios 2 和 3，QoS adaptation 需要在 user plane 按 per-PDU 或 per-burst 时间尺度发生。基于 control plane 的 reconfiguration 至少慢一个数量级。
- **6GR MAC 与调度**：新增 50 条
  - 由于 XR 和 IC 等实时流量出现增多，legacy LCP procedure 可能不足以支持 6G 中更多样的流量。
  - 6G 的新用例和流量特征要求更具适应性的 LCP。
  - 现有 LCP framework 可通过为每个 QoS flow 配置专用 DRB/LCH 实现 QoS adaptation，但受 DRB/LCH 数量有限、配置开销以及半静态 priority、PBR 和 BSD 限制，缺乏可扩展性和动态性。
- **6GR 初始接入与系统信息**：新增 10 条
  - 研究按每条 SI message 配置 SI-window width，并在方案研究中考虑 UE impacts、避免频繁 SI updates。还将研究显式或隐式的 window start positions，及其与每条 SI window width 和 UE calculations 的配合。
  - 原文指出，flexible SI scheduling 带来的 UEPS 收益有限，因为现有 scheduling mechanism 运作良好，且 UE 只需在相对较长的周期内接收一次 SIBs。
  - 6GR SI framework 应考虑为每条 SI message 配置 SI-window start position 和 SI-window width。原文指出，NR 可结合 implicit 和 explicit SI window determination，以减少 SI 配置开销并提升部分 SI messages 的配置灵活性。
- **6GR 寻呼**：新增 6 条
  - UE 在每个 UE paging cycle 监测一个 paging occasion。6G PF/PO design 目标是使用一个 PF/PO distribution formula，同时支持 clustered 和 uniform PF/PO；下一次会议将整理 paging formula 的 requirements 及需解决的 shortcoming/limitations，详细公式设计留待 WI phase。
  - 原文提出 paging cluster 可包含一个或多个 PF/PO，并支持 cluster 内 PO 间隔、每个 paging frame 配置多个 paging occasions，以及每个 UE paging DRX cycle 配置一个或多个 paging clusters。6G paging 应支持 idle 和 inactive UE 的 paging、向至少处于 RRC Idle/Inactive 的 UE 通知 system information change 与 ETWS/CMAS，并使 paging capacity（包括 paging records）至少达到 5G 水平；同时提出研究基于 UE paging-related capabilities 分配 paging occasions。
  - Paging cluster 内的 paging occasions 需要更密集排列。相比 NR Rel-19，每个 paging cluster 应包含更多 POs。
- **6GR 频谱聚合**：新增 42 条
  - RAN2 需研究 FR1+FR2 非共址场景中最高 10ms backhaul delay 对 CA 和 DC 的协议、接口、性能以及 UP/CP 的影响，并评估可满足的需求和简化 DC 的可行性。工作分为阶段一影响分析和阶段二协议层评估及方案比较，期限为 Long。
  - 在 5G CA 中，UL CC 数量不得超过 DL CC 数量的限制，使系统难以适应不同的 UL/DL 流量负载，尤其是 UL 流量较重时。
  - 在 5G CA 的某些情况下，例如将 serving SCell 切换为 PCell，执行 HO 会造成不必要的中断和 signaling overhead。
- **6GR 数据与模型传输**：新增 23 条
  - UE-side data collection 中，RAN 不解码或解释数据内容，但应了解传输数据的类型以支持 controllability 和 forwarding；standardized data 的 decodability 将在 CN 或 OAM，具体位置待定。拟于 August meeting 发送 LS，RAN awareness 的实现方案仍待研究。
  - RAN2 将明确 visibility 与 decodability 是不同概念：decodability 指解码并解释数据内容的能力，visibility 指判断收到的数据应如何处理的能力。
  - 条目提出 termination point 应具备 full visibility，以决定路由、处理或本地终止数据，并以此为基线研究至少适用于 AI/ML 的 standardized data collection framework。要求还涉及数据安全与隐私、MNO 对传输过程的控制、可扩展性，以及降低对 UE 和用户流量的影响；术语说明 full visibility 包含 decodability 和 controllability，并将在 MNO。
- **6GR AI/ML 协议支持**：新增 12 条
  - 对于 UE-sided model，network 需要知道传输对象是 model，但无需知道其内容或详细 meta info，以避免对其他 traffic 造成影响。Network 可以控制是否以及何时向 UE transfer/delivery 该 model。
  - 对于 one sided UE models，模型存储在 3GPP 之外时，model transfer 可对 3GPP 保持透明；存储在 3GPP 内时，网络应具备部分可见性（知晓 model 与 non model）以及 transfer controllability。
  - RAN2 将 transparent/OTT approach 作为 6G UE-side model transfer 的基线；其他基于 UP 的方案仍待研究。
- **6GR 提前报告**：新增 23 条
  - 研究有助于 aNB 的 long-term traffic prediction information 内容及其用于 UE 重配置、因 data inactivity 释放 UE，以及 idle/inactive 到 connected 的场景；并研究信息提供时机与有用信息。短期和长期 traffic reporting 均应允许 network 启用或禁用，性能监测需求及 CP 相关讨论仍待后续推进，并提及使用 LCM framework。
  - predictive reporting 支持三种情况：仅报告 timing information、报告特定时间窗口内的 predicted data size，或报告预期数据到达的时间点及数据量。
  - 对于 predictive timing information，可将 Rel-19 XR 为 DL 定义的 TTNB（当前 data burst 最后一个 PDU 传输与下一 data burst 第一个 PDU 之间的间隔）复用于 6G UL。
- **6GR 移动性**：新增 29 条
  - 除 CFRA baseline 外，RAN2 研究 UE 使用预配置 preamble 的 CBRA-based early UL synchronization 的可行性；支持 NW-triggered early UL synchronization，并进一步研究 UE-triggered 的潜在收益和可行性。NW-triggered baseline procedure 包括 source cell 向 UE 发命令、UE 向 target cell 发 RACH preamble、target cell 计算并传送 TA 给 source cell、source cell 将 TA 交付 UE，之后 UE 使用有效 TA 执行 RACH-less mobility；还考虑 network-triggered mobility 中 target cell initial access resources 在 cell switch command 前提供或随命令提供的两种情形。
  - UE 处理时间（Tprocessing，RAN4 定义）主要取决于 UE 收到 HO command 后需要执行的实际操作。它与 HO 期间变更的 IE/参数数量或 HO command 的大小没有直接相关性。
  - RAN2 认可，在某些痛点场景中，legacy handover mechanisms 可能有较高概率发生非预期事件。例如，快速 RSRP 下降时 measurement event 未能正确触发。
