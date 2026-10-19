# 6GR 控制面其他议题

**当前进展** · 阶段：讨论中

RAN2 已确认 6G 多载波部署中聚合 always-on common signalling、支持 cross-CC initial access，并以 5G CA 为 CONNECTED 态频谱聚合基线；非连接态 UE 无需在多个载波监听寻呼。研究重点正收敛到 FR1-FR2 同步非共址部署，回传时延上限为 10 ms，并需评估调度架构、协议影响和性能可行性。RAN2 也在梳理 cell、primary/secondary serving cell 的概念与功能，并研究灵活聚合所需的测量、快速切换和故障恢复能力。多项关键选择仍待跨工作组讨论或可行性评估，整体尚处于讨论阶段。

**未决问题**

- Cross-CC initial access 是否使用与驻留相同的载波仍为 FFS，后续研究依赖 RAN1 进展。
- cell 与物理载波的映射、RRC_CONNECTED 中 cell 的用途，以及 primary/secondary serving cell 的定义和术语仍待确定。
- 非共址聚合的集中式或分布式调度、HARQ 与 PDCP/RLC 影响、节点间接口需求，以及最高 10 ms 回传带来的用户面时延是否可接受，仍需评估。
- NR-DC framework 能否支持目标非共址部署，以及所需规范影响和对现有 5G DC 设计的简化范围尚未确定。
- 统一 carrier-level aggregation 方案纳入哪些增强仍待研究；cross-carrier HARQ 属于 RAN1 讨论范围。
- SCell 支持更多功能及 PCell failure recovery、RLF 韧性工具和相关测量方法仍处于研究或提案讨论中。

## 跨会议演进脉络（6G）

2026年2月至4月，6GR 多载波研究从公共信令聚合、cross-CC initial access 和以 5G CA 为基线的统一载波资源聚合方向，推进到 RRC_CONNECTED 多 serving cells 的 L2/L3 功能、连接转换时快速重定向，以及非共址聚合的研究边界。研究范围更具体，但 cell 定义、协议架构和增强功能仍未定案；后续材料未表明此前 cross-CC initial access 待决项已解决。

### 关键进展

- 2月确认 always-on common signalling aggregation mechanism 的节能收益：由 reference carrier frequency 广播 SSB/SIB1，并提供其他载波的同步参考及初始接入相关配置；同时同意非连接态 UE 无需在多个载波监测 paging。（依据：RAN2-133）
- 接入研究从2月支持覆盖驻留 coverage layer、跨载波初始接入及在 capacity layer 保持连接的 cross-CC initial access 三阶段研究，推进到4月明确支持 UE 从 IDLE/INACTIVE 转换时更快重定向至合适的 carrier(s)/cell(s)，并在 RRC_CONNECTED 建立 aggregation；后者不代表跨载波初始接入方案已确定。（依据：RAN2-133、RAN2-133bis）
- CONNECTED mode 聚合从2月提出以 5G CA 为基线的统一 carrier level resource aggregation，推进到4月明确 6G 支持 carrier aggregation、UE 可配置不同载波上的多个 serving cells，且 primary cell 至少承担 system information reception、RLM 等功能；RAN2 聚焦 L2/L3 功能。（依据：RAN2-133、RAN2-133bis）
- 4月明确非共址聚合的研究起点为 FR1-FR2 synchronous deployments，latency 上限为 10 ms，并要求覆盖 single/dual scheduler、调度器可协调或不可协调的情况，以及 PUCCH 假设、性能和可行性。（依据：RAN2-133bis）

### 待决问题

- 初始接入采用驻留载波还是不同载波仍为 FFS，需等待 RAN1 进展；cross-CC initial access 三阶段的 UE 和网络具体操作仍待研究，4月材料未提供这些问题已解决的证据。（依据：RAN2-133、RAN2-133bis）
- cell、primary/secondary serving cells 的定义及其与 physical carrier(s) 的映射仍需澄清；哪些功能必须关联特定 serving cell、主辅 serving cells 功能差异及 5G CA framework 改进点仍待研究，6G 术语待 RRC 结构确定。（依据：RAN2-133bis）
- 2月提出的 SCell 功能扩展、经 SCell 的 PCell failure recovery 及相关测量方案尚未确定；4月仍需研究 flexible aggregation 的 RRM measurement architecture、fast cell change、RLF handling，以及额外韧性触发条件和 UE 动作。（依据：RAN2-133、RAN2-133bis）
- 非理想回传对调度、HARQ、PDCP/RLC 和额外 UP 时延的影响，以及节点间接口需交换的信息仍待评估；以 NR-DC framework 支持非共址聚合的可行性及 CP/UP 简化方案也未确定。（依据：RAN2-133bis）
- 具体 CA 增强功能尚未确定：2月的 UL/DL decoupling、PCell/SCell 快速角色变更，以及4月的单一 MAC entity、multiple TAGs、无需 RRC 参与的载波动态激活/去激活、CA-based duplication、LCH/carrier 灵活映射和 early measurement reporting，仍处于提案或研究阶段。（依据：RAN2-133、RAN2-133bis）

### 会议时间线

- **RAN2#133**（2026-02-09 至 2026-02-13）：RAN2#133 推进了 6GR 多载波部署下公共信令聚合、cross-CC initial access 和 CONNECTED mode 载波资源聚合的研究方向。会议确认 always-on common signalling aggregation mechanism 的收益，并明确非连接态 UE 无需在多个载波监测 paging，但初始接入是否跨载波仍待研究。CONNECTED mode 以 5G CA 为统一 carrier level resource aggregation 方案的基线，同时将 SCell 功能扩展和经 SCell 的 PCell failure recovery 纳入研究。
- **RAN2#133bis**（2026-04-13 至 2026-04-17）：本会议将非共址频谱聚合的研究起点聚焦于 FR1-FR2 synchronous non-collocated deployments，latency 上限为 10 ms，并明确需评估调度器配置、回传时延对 UP protocol 的影响及可行性。围绕 6GR 多载波操作，讨论推进了 serving cells 的 L2/L3 功能、carrier aggregation 和连接转换时快速重定向的方向。cell 定义、载波映射及协议架构仍待澄清，具体 MAC、移动性与韧性增强方案尚处于提案或研究阶段。

## 6GR 演进

### [6G/Rel-20 RAN2#133bis] `agreement` 9.3.2.5 Others

RAN2 将研究起点聚焦于 FR1-FR2 synchronous non-collocated deployments，latency 上限为 10ms。研究应考虑 single 或 dual scheduler、调度器可协调或不可协调的情况，以及 PUCCH 假设、回传时延对 UP protocol 的影响、性能和可行性。

```text
RAN2 to focus the study as a starting point FR1-FR2 synchronous non-collocated deployments with up to 10ms latency.
Study can consider how this works in case of single or dual scheduler assumption.  The study should consider the cases where schedule can coordinate and case where scheduler can’t coordinate.
Study should consider assumptions on PUCCH, impacts to UP protocol due to latency over backhaul, performance, feasibility etc.
R2-2601476	Discussion on 6G spectrum aggregation	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.5-a001`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.2.5 Others

原文将 cell 描述为一种 logical concept，用于让 network 管理 physical end points、其资源，并按所需 service quality 配置硬件。需要澄清 6G 中 cell 的定义，以明确 primary 和 secondary serving cells 概念，同时纳入 RAN1/RAN2 和 RAN4 中的 UE requirements。

```text
The cell is a logical concept that allows network to manage physical end points (for security, data and signalling exchanges), its resources and dimension the required hardware to the desired service quality. The definition for a cell in 6G is required to be clarified so that the primary and secondary serving cells concepts are clear while capturing UE requirements in RAN1/RAN2 and RAN4.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.5-o001`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.5 Others

在 RRC_CONNECTED 多载波操作中，6GR UE 可配置不同载波上的多个“serving cells”，RAN2 聚焦其 L2/L3 功能。采用“per cell per carrier”还是“single cell multiple carrier”建模，待 RAN1/4 进一步讨论。

```text
For multi-carrier operation in RRC_CONNECTED, an RRC_CONNECTED UE in 6GR can be configured with multiple "serving cells" on different carriers. RAN2 discussion should focus on L2/L3 functionalities of the "serving cell". For the "serving cell", RAN2 waits for further RAN1/4 progress on whether to adopt "per cell per carrier" modelling as in 4G/5G or "single cell multiple carrier" modelling (similar to "Gothia cell" in RAN1).
-	Oppo asks that if we have multi carrier cell why do we need the concept of SCell.  Xiaomi explains that in any case there will be interband case where we can’t have MCSC.   Apple likes Xiaomi, so we can just focus on cell and cell aggregation.
-	Mediatek and ZTE thinks we should keep simple complexity and power saving.
Noted
PCell/SCell Role
R2-2601806	Discussion on multi-carrier and other control plane issues	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.5-p001`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.5 Others

6G 支持 carrier aggregation，primary cell 至少用于 system information reception、RLM 等。RAN2 将研究需关联到特定 serving cell 的功能及 primary/secondary serving cells 功能不同的原因，并识别 5G carrier aggregation framework 的待改进之处；6G 术语待 RRC 结构确定后再定。

```text
Carrier aggregation is supported in 6G. The primary cell is supported in CA at least for system information reception, RLM, etc.
Noted
R2-2602273	Inputs on spectrum aggregation for non-collocated FR1-FR2 deployments	Ericsson	discussion	Rel-20	FS_6G_Radio
Proposal 7	When discussing 6G functionality in connected mode, avoid using NR terminology like PCell and SCell, which assumes functionality grouping as in NR. 6G terminology can be fixed once the RRC structure is agreed.
Noted
Discussions
-	Ericsson explains that the reason for not using PCell and SCell is mainly from a ASN.1 structure.   Nokia understands but not sure we can avoid doing the same things.  Ericsson thinks that some operations may apply to both PCell and Scell so it would be better to make something general.
-	Xiaomi thinks that we need to add security.  Huawei thinks that this are the essential that have to be there, security and mobility can be discussed.
-	CMCC thinks that we need to address the signaling overhead, like for example changing SCell and PCell, and avoiding re-establishment.
Agreements for multi-carrier operations in connected mode
1	For multi-carrier operation in RRC_CONNECTED, an RRC_CONNECTED UE in 6GR can be configured with multiple "serving cells".   RAN2 discussion will focus on L2/L3 functionalities of the "serving cell". For the "serving cell", RAN2 waits for further RAN1/4 progress on whether to adopt "per cell per carrier" modelling as in 4G/5G or "single cell multiple carrier" modelling (similar to "Gothia cell" in RAN1).  FFS whether “serving cell” includes only one or multiple carriers based on RAN1 discussions.
2	Study which functionalities need to be associated to a particular serving cell (i.e. primary/secondary cells) and explain why the functionalities are different between primary/secondary serving cells.
3	Identify and capture the shortcomings of 5G we want to address for 6G carrier aggregation framework.
Not treated
Spectrum Aggregation Functionality
R2-2601476	Discussion on 6G spectrum aggregation	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.5-p002`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.5 Others

提出支持单一 MAC entity 的 spectrum aggregation，并包含 multiple TAGs、无需 RRC 参与的 component carrier 动态激活/去激活、基于 CA 的 duplication 与 LCH 和 carrier 的灵活映射，以及 early measurement reporting。

```text
Spectrum aggregation with a single MAC entity should be supported with following features:
	Multiple TAGs   (aim to support the aggregation of carriers with non-collocated TRPs)
	Dynamic activation/deactivation of component carriers without RRC involved
	CA based duplication and flexible mapping between LCH and carrier
	Early measurement reporting
R2-2601985	Discussion on spectrum aggregation in 6GR	China Telecom	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.5-p003`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.5 Others

多载波连接模式下，可考虑增强 fast cell change 和 RLF handling 相关流程。另有提案建议 6G 在 RLF detection 和 RRC re-establishment 之外提供韧性工具，包括额外触发条件及新的 UE 动作。

```text
Regarding multicarrier operation in connected mode, further enhancements on the procedures related to fast cell change and RLF handling could be considered in 6GR.
R2-2602087	How to improve resilience aspects in 6G	NTT DOCOMO, Ericsson, FirstNet, Reliance Jio, Sync Techno Inc., Airbus, UIC	discussion	Rel-20
Proposal 1	6G supports additional tools (i.e., besides RLF detection and RRC re-establishment) for providing resiliency, such as:
a.	Additional triggers, e.g., loss of keep-alive signaling over UP or keep-alive signaling over CP.
b.	New UE actions, e.g., starting a handover procedure, activating a carrier.
R2-2602199	Spectrum Aggregation for 6GR	InterDigital, Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.5-p004`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.5 Others

6G 支持 UE 从 IDLE/INACTIVE 转换时，更快重定向到合适的 carrier(s)/cell(s)，并在 RRC_CONNECTED 中建立 aggregation。

```text
6G supports faster redirection to the appropriate carrier(s)/cell(s) and setup of aggregation in RRC_CONNECTED when moving from IDLE/INACTIVE.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.5-p005`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.5 Others

RAN2 研究支持 flexible aggregation 所需的 RRM measurement architecture。

```text
RAN2 studies the RRM measurement architecture required to support flexible aggregation.
Not treated
Cell Definition (if time allows)
R2-2601806	Discussion on multi-carrier and other control plane issues	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.5-p006`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.5 Others

Cell 被定义为管理 physical carrier resources 的逻辑术语。cell 与 physical carrier(s) 的映射取决于 RAN1 讨论，例如 Gothia cells。

```text
Cell is defined as a logical term to manage physical carrier resources. The mapping between cell and physical carrier(s) depends on the RAN1 discussion, e.g. on Gothia cells.
R2-2601845	Discussion on spectrum aggregation in 6G	Nokia	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.5-p007`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.5 Others

提议 RAN2 将 cell 定义为可由 RRC signalling 关联的 downlink 和/或 uplink resources 组合。cell signalling 还应明确区分 schedulable PRBs 和 RF bandwidth。

```text
RAN2 to define a cell as a combination of downlink and/or uplink resources that may be linked together by RRC signalling. The cell signalling shall also unambiguously distinguish the schedulable PRBs and the RF bandwidth.
R2-2601476	Discussion on 6G spectrum aggregation	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.5-p008`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.5 Others

预计 RAN2 在 system information、IDLE mobility、connected mobility 及 RRM 中使用“cell”术语。cell 是否仍用于 connected mode 下 UE 的 radio resource configuration 尚待确定。

```text
The terminology “cell” is expected to be used in the following aspects in RAN2: System information (e.g. NCGI), Mobility in IDLE (i.e. cell (re-)selection) and in Connected(e.g. target aNB/cell identification during Handover), RRM(L3/L2 Measurement, RLM, BFM). It is FFS whether the cell is still be used for radio resource configuration of UE in connected mode.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.5-p009`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.5 Others

Cell 可包含 downlink、uplink 或两者资源，对应由单一 aNB 控制的一个或多个 TRPs，并关联一个 CD-SSB 和一个 PCI。每个 cell 可为 TDD 或 FDD；“Gothia cell”讨论留待 RAN1。

```text
The cell has following characteristic:
	A Cell contains downlink or uplink or combination of downlink or uplink resources.
	A cell corresponds to 1 or many TRPs controlled by a single aNB.
	Each cell is associated to one CD-SSB and one PCI.
	One cell can be either TDD cell or FDD cell.
NOTE: The discussion about “Gothia cell” is left to RAN1.
Study of non-collocated, non-ideal backhaul
Scenarios and Requirements
R2-2602048	6G-6G spectrum aggregation for non-collocated FR1-FR2 scenario 	Verizon, Qualcomm Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.5-p010`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.5 Others

RAN2 将考虑 6G FR1-FR2 非共址频谱聚合的要求，包括支持单向 10 ms 或更高的站间时延、吞吐量和覆盖优于 5G FR1-FR2 部署，以及便于从 5G NR-DC 部署迁移。还要求支持非共址节点间跨厂商频谱聚合的标准化接口，并兼容已部署的 RAN 架构。

```text
RAN2 shall consider the following requirements for 6G FR1-FR2 non-collocated spectrum aggregation scenario:
Latency tolerance: Support inter-site latency of up to 10 ms one way or more.
Better performance: Ensure better performance than 5G FR1-FR2 deployments in terms of throughput and coverage.
-	Apple asks if Verizon can support non-split bearer for DC.    Verizon has thought about this but the actual functionality of splitting traffic can’t be avoided but perhaps we can think how it can be done.
-	ZTE thinks that the moment we need real spectrum aggregation we have to accept the delays that come with the non-collocated deployments.
Ease of migration: Support easy cost-effective migration of 5G NR-DC based deployments. Consider a new solution only if really justified by significant performance gains.
-	Mediatek asks what does this mean in practice.   Verizon explains that we have already NR-DC deployments and we should ease the migration by doing something similar in 6G as a baseline, a version of DC.
Deployment flexibility: Support standardized interface for inter-vendor spectrum aggregation between non-collocated nodes and shall support backward compatibility to deployed RAN architecture.
-	Ericsson thinks that we need to use carrier aggregation as a baseline and see if that can meet the requirement.   Verizon thinks that is not an ease of migration as we have to start from scratch.  And we are compromising to using 10ms delay
-	Nokia thinks that we should design a solution that works for FR1 and FR2.   And last two bullets are RAN3.   Verizon explains that for inter-vendor support it is important as we may have different vendors for FR1 and FR2
-	CMCC thinks that RAN2 should understand the requirements and from CMCC perspective DC is too complicated.   Verizon disaagrees that DC is more complicated as we are aggregating at higher layers which is simpler than aggregating at lower layers and having to coordinate at those layers.
-	Qualcomm thinks that from UE side it would be nice if it can work with CA as it is simpler, but it’s important that we address the operators requirements and understands how and if it works under different assumptions, multiple or single schedulers.  We discussed in 5G and looked at different protocol layers.
-	Huawei explains that we need to understand how it works in the network side for non-ideal backhaul with the delay, as today we already use CA for non-collocated cases with ideal backhaul, as we have the coordination.   For inter-vendor Huawei doesn’t see the need.  Verizon explains that today we have inter-vendor scenarios.
-	Xiaomi thinks that we first need to study what information is needed for coordination and interface can be up to RAN3.   Also need to analyze based on carrier aggregation what changes need to be and what are the performance degradation we see.
-	Docomo thinks that 10ms is very different to satisfy and coordinate with RAN1 which solution satisfier the requirement.
-	Vivo thinks that we should analyze the different architecture.
-	Oppo thinks that we should start with simple solutions as we don’t want high complexity.
Noted
R2-2601842	Views on Non-collocated deployments in 6G	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.5-p011`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.5 Others

为简化规范和实现，考虑异步操作及 FR1-FR1 非共址部署前，应先证明其实用部署或用例。RAN2 将聚焦 FR1-FR2 和 FR1-FR3 同步部署；针对约 10 ms 回传时延的 FR1-FR2 非共址场景，RAN2 研究应聚焦 UL/DL 解耦。

```text
To simplify the specification and implementation efforts, practical deployment/use-cases for asynchronous operation and FR1-FR1 non-collocated deployment operations should be justified before being considered. RAN2 to focus on FR1-FR2 and FR1-FR3 synchronous deployments.
Noted
R2-2602274	Aspects on 6G spectrum aggregation	Ericsson	discussion	Rel-20	FS_6G_Radio
Proposal 2	For the RAN plenary task to study 6G-6G spectrum aggregation for non-collocated deployment scenarios for FR1-FR2 combination with ~10ms backhaul latency, the RAN2 study should focus on UL/DL decoupling.
Noted
Assumptions and further study points
R2-2601441	Cell Model Spectrum Aggregation and Non-collocated CA	CATT	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.5-p012`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.5 Others

针对回传时延最高 10 ms 的非共址 inter-aNB CA，需讨论网络侧采用集中式还是分布式 MAC scheduler、调度与 HARQ 的影响、PDCP/RLC 的影响，以及是否需要规定节点间接口交换的信息。讨论还提出研究单一和分布式 scheduler 的利弊，并考虑 UL/DL decoupling。

```text
For non-collocated inter-aNB CA assuming backhaul latency up to 10ms, at least the following issues should be discussed:
-	Centralized MAC scheduler or distributed MAC scheduler in NW side;
-	CMCC asks if this is for UE side.   CATT explains that from UE side it can be one MAC.  Xiaomi thinks it depends if it is CA or DC.
-	The impacts on scheduling and HARQ, e.g., scheduling/HARQ timing and HARQ processes number;
-	The impacts on the PDCP/RLC, e.g., SN range and reordering/reassembly timer length；
-	The necessity of specifying the information exchanged in the interface between two non-collocated aNBs.
-	Vivo doesn’t think we need to go this level of details for the information.
-	Ericsson thinks that we should also consider UL/DL decoupling and the best we can do is explain the solution and the assumption and take into account the required.   Also there are some things we never specified.
-	ZTE agrees with Ericsson but we need to discuss to understand what needs to be exchanged.   If we go for DC and we have split bearer DC this will hinder all the work we have been doing for UP design.
-	Nokia doesn’t thinks we will specify what scheduler we will use but we have to discuss how it works.
-	Verizon thinks that we need to make an assumption that it is a distributed scheduler.  Apple agrees and the most important one to select first is scheduler.    Should the UE report the feedback to one node or different nodes.   ZTE thinks that the UE shouldn’t care where the scheduler is.  Apple explains that we need to know where we send the feedback like HARQ, otherwise it becomes like NTN.
-	Interdigital thinks that we should identify the options and study pros and cons of single and distributed scheduler and we shouldn’t call it CA/DC.
-	Samsung doesn’t see why we have to start with CA and we had this discussion in LTE and we had to introduce two schedulers.
-	CMCC thinks we need to differentiate inter and intra-vendor scenario.
-	Mediatek thinks that the UP impact is very important like for example the HARQ processes should be independent as otherwise it will have a lot of impact
-	Oppo asks if we want to support the scenario that we have DL coverage in FR2 but not in UL.  Verizon thinks it is an important scenario.
-	Qualcomm thinks we need to ensure that performance is met and the system works.
-	Turkecell doesn’t thinks inter-vendor is a use case.
-	Ericsson thinks that one criteria should be likelihood of the deployment as it is important to not optimize on something that won’t be used.   We should avoid have yet another solution so hope is that the operator helps us what requirements they have.
-	Sumsung would be happy to make an assumption that we have separate scheduler and this doesn’t mean two MAC entities.
Noted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.5-p013`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.5 Others

RAN2 受请评估：非理想回传（最高 10 ms）造成的额外 UP 时延，对于带非理想回传的频谱聚合是否可接受。

```text
RAN2 is kindly asked to check whether the additional UP latency caused by non-ideal backhaul (up to 10 ms) is acceptable for spectrum aggregation with non-ideal backhaul.
Noted
R2-2601453	Discussion on 6G-6G spectrum aggregation for non-collocated deployment scenarios	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.5-p014`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.5 Others

RAN2 需就使用 NR-DC framework 支持回传时延最高 10 ms 的 6G FR1-FR2 非共址频谱聚合进行评估，涵盖 intra-aNB/inter-aNB 及 intra-vendor/inter-vendor 部署的可行性。原文提出现有 NR-DC 复杂，需结合 6GR 设计讨论规范影响及对 5G DC 设计的简化，例如 CP 和 UP 的 PDCP anchor 均仅位于 FR1 站点、无 SRB3、单一 RLM。

```text
RAN2 to agree the following evaluation for using NR-DC framework to support 6G FR1-FR2 non-collocated spectrum aggregation with up to 10ms backhaul latency:
-	Feasible to support intra-aNB/inter-aNB, intra-vendor/inter-vendor deployments;
-	Existing NR-DC is very complex, thus lots of specification impacts should be discussed based on 6GR design and simplifications on the 5G DC design are also needed (e.g., PDCP anchor only located in FR1 site for both CP and UP, no SRB3, single RLM etc).
Noted
Not treated
R2-2601530	Spectrum aggregation for non-collocated FR1 and FR2	Boost Mobile Network	discussion
R2-2601579	Discussion on 6G Spectrum aggregation and access control	OPPO	discussion	FS_6G_Radio
R2-2601770	Discussion on multi-carrier operationand and non-collocated scenarios	1Finity	discussion	Rel-20	FS_6G_Radio
R2-2601848	Paging and initial access procedures on different bands	Vodafone, Fraunhofer IIS	discussion	Rel-20
R2-2601863	Multi-Carrier Operation	Ofinno	discussion
R2-2602023	Discussion on signalling format for control plane	Panasonic	discussion	Rel-20
R2-2602030	6G Multicarrier operation in connected mode	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
R2-2602075	Discussion on Access Control	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2602133	Discussion on spectrum aggregation for Connected state	Lenovo	discussion	Rel-20
R2-2602152	Discussion on non-collocated Spectrum Aggregation	Rakuten Mobile, Inc	discussion
R2-2602212	DL WUS operation on different bands	Vodafone GmbH	discussion	Rel-20
R2-2602279	Spectrum aggregation in Connected and cell modelling	NEC	discussion	Rel-20	FS_6G_Radio
R2-2602296	Multi-Carrier and Non-Collocated Scenario	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
R2-2602370	Considerations on multicarrier operation deployments in 6G	AT&T	discussion	FS_6G_Radio
R2-2602418	Discussion on cell modeling, spectrum aggregation and access control	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2602443	Consideration of C-plane other aspects for 6GR 	Kyocera 	discussion	Rel-20
R2-2602486	Discussion on 6G-6G Spectrum Aggregation	Samsung, Verizon	discussion	FS_6G_Radio
R2-2602507	Discussion on 6G spectrum aggregation	NTT DOCOMO INC..	discussion
R2-2602522	Spectrum Aggregation for 6GR	MediaTek Inc.	discussion
R2-2602566	Discussion on dual connectivity for 6GR	CEWiT	discussion	Rel-20	FS_6G_Radio
R2-2602588	Discussion on multicarrier in connected mode for 6GR	TCL	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.5-p015`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.5 Others

UE 在一个 carrier 上驻留并在同一 carrier 上发起 RA，不存在 capacity issue。

```text
There is no capacity issue for UE camping on one carrier and initiating RA on the same carrier.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.5-o001`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.5 Others

在 multiple CC deployment 中，从网络和 UE 角度看，期望 IDLE/INACTIVE 状态的 UE 驻留在 coverage layer，并在 capacity layer 上进行 UE dedicated data transmission。

```text
In the multiple CC deployment, from both NW and UE perspective, it is desirable for UE in IDLE/INACTIVE state to camp on the coverage layer and to perform the UE dedicated data transmission on the capacity layer.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.5-o002`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.5 Others

原文指出，若 IDLE/INACTIVE UE 均驻留在 coverage layer，并在进入 CONNECTED 后切换到 capacity layer 进行专用传输，会造成 coverage layer 初始接入拥塞，以及切换延迟长、信令开销高。

```text
According to NR design, if all UEs in IDLE/INACTIVE state camp on coverage layer and then switches to capacity layer for UE dedicated transmission after entering the CONNECTED state, it will cause the following two issues: 1) initial access congestion on coverage layer, and 2) long delay and high signaling overhead to switch UE to capacity layer.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.5-o003`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.5 Others

在 MRSS 和 CA 部署中，若 PCell 位于 coverage layer，UE 连接和数据传输主要在 SCell 上。原文提出应考虑将 NR 中部分 PCell 功能卸载到 SCell，例如用于 SR 的 RACH。

```text
In MRSS and CA deployment, if PCell is on coverage layer, the UE connection and data transmission is mainly on SCell and some PCell function in NR should be considered offloading to SCell, e.g. RACH for SR purpose.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.5-o004`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.5 Others

在 MRSS 和 CA 部署中，若 PCell 位于 capacity layer，由于覆盖问题，恢复场景会比 NR 更频繁。原文提出应考虑通过 coverage layer（SCell）进行 PCell recovery。

```text
In MRSS and CA deployment, if PCell is on capacity layer, due to coverage issues, recovery scenarios are more frequent than NR, and the PCell recovery over coverage layer (SCell) should be considered.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.5-o005`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.5 Others

原文提出，对于 IDLE/INACTIVE UE，没有必要驻留在一个载波的同时在另一个载波执行 RA。

```text
For IDLE/INACTIVE UE, it is unnecessary for UE camping on one carrier while performing RA on another carrier.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.5-p001`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.5 Others

原文提出 IDLE/INACTIVE UE 不需要支持 multi-carrier operation。所列 5G NR 经验指出，多载波部署中各 serving cell 均需发送自身的 SSB/SIB1，可能导致 always-on common signalling 的能耗和系统开销、UE 额外功耗及碎片频谱聚合支持不足。

```text
IDLE/INACTIVE UE does not need to support multi-carrier operation.
Noted
R2-2600124	Discussion on Multi-carrier operations and other CP aspects	Xiaomi	discussion	Rel-20	FS_6G_Radio
Observation 1 [Lessons learnt from 5G]: In 5G NR, each serving cell for IDLE/INACTIVE mode has to signal "always-on" common signalling (i.e. SSB/SIB1) of its own. Such a design, in multi-carrier deployment:
	leads to inefficient "always-on" common signalling transmission from NW energy consumption and system overhead perspective;
	results in unnecessary additional power consumption for UE's camping/access to the intended carriers (e.g. capacity layer carriers, feature/UE type specific carriers, etc.);
	cannot effectively support the aggregation of fragmented spectrums.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.5-p002`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.5 Others

RAN2 确认 6GR multi-carrier deployment 中 always-on common signalling aggregation mechanism 的收益，例如网络能耗和 UE 功耗节省。该机制由 reference carrier frequency 广播 SSB/SIB1，并为其他载波提供同步参考和初始接入相关配置，例如 PRACH config、CSS。

```text
For multi-carrier deployment in 6GR, RAN2 confirms the benefit (e.g. NW energy/UE power saving, etc.) of the "always-on" common signalling aggregation mechanism that the "always-on" signalling (SSB/SIB1) is broadcast only by a reference carrier frequency which provides the synchronization reference and the initial access related configuration (e.g. PRACH config, CSS, etc.) for all the other carriers.
Noted
R2-2600458	Views on 6G spectrum aggregation	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.5-p003`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.5 Others

RAN2 6G study 应支持 cross-CC initial access procedure，并研究 UE 和网络在三个阶段的操作：初始接入前驻留 coverage layer、执行 cross-CC initial access，以及进入 CONNECTED 后在 capacity layer 保持连接。非连接态方面已同意 UE 无需在多个载波监测 paging；初始接入是否使用与驻留载波相同或不同的载波仍为 FFS，后续研究等待 RAN1 进展。

```text
RAN2 6G study should support the cross-CC initial access procedure, and study the UE and network operation in three phases:
-	Phase 1: Camp on coverage layer before UE initial access procedure
-	Phase 2: During cross-CC initial access procedure
-	Phase 3: Keep connection on capacity layer after UE initial access procedure and entering CONNECTED state.
Noted
Discussion
-	CMCC supports Xioami’s proposals and we need a solution to utilize the fragmented spectrum.
-	Mediatek points out that RAN1 is also discussing so we should understand the work split.
-	ZTE thinks that the proper spectrum utilization is important and RAN2 can focus on access procedures and RAN1 on common signal design.
-	Fraunhofer Do we support the case where we have less paging areas than initial access
-	Nokia thinks we need to understand if there is a use case for this.   In NB-IoT it was introduced for massive amount of devices, but in 6G we are not sure we have this scenario.   Qualcomm agrees with Nokia and anyways from RAN2 perspective it is feasible.   RAN1 and RAN4 should confirm the feasibility and benefit and then we can look at it.
-	Huawei thinks that RAN2 can discuss whether an anchor carrier can configure other carriers from signaling point of view.  This is also related to NW energy saving.
-	Vivo thinks that we don’t need to talk about feasibility as it is similar to SUL.
-	CATT thinks at least for paging the UE should only monitor on one carrier only.  For RA requirement does the UE need to monitor and/or measure the other carrier.   ZTE thinks that you don’t need to do any additional measurements as you anyways are doing neighbour cell measurements.   Xiaomi explains that NB-IoT we only measure the anchor carrier so we can theoretically do the same.   Qualcomm points out that we need to consider synchronization as well.  When measuring neighbor cells you are not doing synchronization.    Qualcomm thinks that in NB-IoT the carriers are very close.  RAN4 has to first confirm if we can measure somewhere and be able to synchronize to the other carrier.   Mediatek thinks we need to postpone the measurements discussions.   Apple thinks this is dependend on RAN1/RAN4
-	Docomo thinks that for energy saving it can be beneficial.
-	Huawei thinks that we need to consider two cases, on the UE measures only on anchor similar to SUL.  Qualcomm indicates that SUL was not successful in the field because of this synchronization.
-	Ericsson agrees with Qualcomm and if the UE has to perform measurements and synchronization it would delay RA procedure.
-	Vodafone is very keen to have initial access on one carrier.   RAN1 is discussing some concepts similar to SUL.  Giving RAN1 some guidance would be beneficial.   We should also consider WUS.
-	Interdigital confirms that RAN1 agreed to study multicarrier in both idle and connected.   We can start to progress some aspects of the access.
-	Xiaomi thinks that for IoT connectivity we may need to consider.   Lenovo thinks that even for IoT it shouldn’t be required to monitor paging on more than one carrier.
-	Vodafone thinks that at least that we can identify the system benefit and motivation.
-	CMCC thinks that we should study making some assumptions (e.g. synchronization and re-use of measurements on anchor carrier) and then it is up to the other WGs how and if this is feasible.
-	Ericsson thinks that this study would only be valid if this is feasible so we should know if this is a common scenario or only very special case.
-	Fraunhofer thinks that one scenario is when it is not latency critical and you can synchronized.
-	CATT thinks that we should first focus on the coverage layer and then understand what is the exact use case for the offload/capacity layer.  Vodafone explains that the UE stays in the camped in the coverage layer and it can’t be offloaded.   Ericsson thinks that we don’t have the problem.  CMCC thinks that use cases are very clear in the proponents contributions.   One example is very narrow spectrum and the only way to use this spectrum is HO and HO increases signaling overhead.
-	Qualcomm would also like to see some statistics and they weren’t sure about RA capacity and paging.
-	Xiaomi is saying the benefit is delay and power saving perspective and there was two operators that strongly request this.   Huawei thinks that if all carrier broadcast the system information that increases power saving.   ZTE thinks that it is about carrier deployment rather than capacity, it is efficient spectrum utilization and energy savings.
-	Vivo thinks that we should consider IoT and ensure that eMBB performance is not impacted.
Agreements on non-connected mode
1	UE is not required to monitor paging on more than one carrier (i.e. camped carrier)
2	FFS on initial access on same or different carrier than the camped carrier, when the UE needs to access the network.    RAN2 will wait at least until RAN2#134 for some further RAN1 progress on non-connected mode and further RAN2 progress on initial access to continue the study.
For RAN2#134, proponents can bring joint paper that clearly highlights the problems and motivation for the study.   Focus of contributions should be on RAN2 related aspects and possible assumptions we need to make.
Spectrum aggregation in CONNECTED [15 min]
R2-2600199	Discussion on multi carrier operation in 6G	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.5-p004`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.5 Others

对于 CONNECTED mode 的 spectrum aggregation，RAN2 目标是形成统一的 carrier level resource aggregation 方案，并以 5G CA 为基线。可继承的 5G CA 增强包括 Early measurement report、Dormancy SCell、Fast SCell activation、Fast SCell beam recovery 和 CA with Tx switching。

```text
For spectrum aggregation in connected mode, RAN2 aim to have a unified solution for the carrier level resource aggregation, and 5G CA should be considered as baseline. Enhancements developed in 5G CA can be inherited, including Early measurement report, Dormancy SCell, Fast SCell activation, Fast SCell beam recovery, CA with Tx switching.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.5-p005`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.5 Others

原文提出在 6G 进一步研究 CA 增强：UL/DL decoupling、PCell 与 SCell 间快速角色变更（也旨在改善 inter-frequency handover），以及 cross-carrier HARQ operation。讨论指出，统一方案不意味着必须纳入所有功能，且 cross-carrier HARQ 属于 RAN1 讨论范围。

```text
The following enhancements for CA should be further studied in 6G
	UL/DL decoupling (e.g. UL only SCell and DL only SCell）
	Fast role change between PCell&SCell (aim to improve the inter-frequency handover as well)
	Cross-carrier HARQ operation
-	Ericsson is fine with proposals but unified doesn’t mean that we take all those functionalities, we can also remove some.
-	Apple thinks that we should focus on L2 features
-	QC Some aspects like UL/DL requires more discussions and CC HARQ is RAN1, we can focus on the latency of switching
Noted
R2-2600458	Views on 6G spectrum aggregation	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.5-p006`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.5 Others

RAN2 6G CA study 应考虑在 SCell 支持更多功能（例如 RLM、RA-SR），以及通过 SCell 进行 PCell failure recovery。讨论中有观点认为，监测 SCell 并报告可避免完整重建；相关提案及测量方法列为讨论内容。

```text
RAN2 study on 6G CA should consider the following two directions:
-	Support more functions on SCell (e.g. RLM, RA-SR).
-	PCell failure recovery over SCell .
-	Oppo asks if this is assuming that we have PCell/Scell concept.   ZTE asks what is the intention and whether it performs monitoring for both or just has a configuration.
-	Xiaomi thinks that RLM is a RAN1 procedure.   Apple thinks that RLF is defined in RAN2.  Ericsson agrees with apple as it would allow the UE to monitor the SCell and report without needing full re-establishment.
Noted
Not treated
R2-2600804	Aspects on 6G spectrum aggregation and multi-carrier operations	Ericsson	discussion	Rel-20	FS_6G_Radio
Proposal 1	RAN2 together with RAN4 to study reusing measurements across RRC states for identifying candidate carriers (i.e. including reusing measurements from last time the UE was in RRC_CONNECTED).
Proposal 2	RAN2 together with RAN4 to study using intra frequency measurements like cell reselection measurements to aid network to identify relevant candidate carriers.
R2-2601081	Discussion on 6GR spectrum utilization and aggregation	Turkcell, NTT Docomo, Deutsche Telekom	discussion	Rel-20
Observation 1	Fragmentation of the 6G frequency band can result in inefficient spectrum use and reduced energy efficiency.
Observation 2	Fragmentation of the 6G frequency band can lead to CA, which does not scale well for 6G sustainability goals.
Observation 3	5G CA signaling overhead and latency conflict with 6G flexibility targets.
Observation 4	Inefficient random access and paging in 5G CA-based multi-carrier systems
Observation 5	Carrier aggregation measurement is critical when there is a need for configuring the UE.
Proposal 1	Multi-carrier operation energy savings and reduced management complexity can be effectively realized from a perspective by enhancing the existing CA framework.
Proposal 2	RAN2 should analyze transitions between carriers to support effective random access and paging.
Proposal 3	RAN2 to explore using a unified measurement framework that enables measurements to support CA configuration as needed.
Discussion on CA framework
Discussion on PCell/SCells
-	Samsung is concerned with UE complexity.
-	Qualcomm is supportive of doing recovery on another cell/carrier.
-	Huawei thinks that we should have functionality spread across groups or carriers.
-	Ericsson thinks that we need keep the discussion generic.
-	Lenovo thinks that we can’t throw away the concept of PCell and Scells, as PCell is associated to a number of functionalities that have been carefully chosen, so we should think hard that nothing is broken.
-	Nokia thinks that we should focus on functionality of what each of these cells/carriers need.
-	LG thinks that the concept of special cell is necessary.  RLM monitoring was not introduced in the past because of complexity.
-	Oppo is concerned that we will limit the SCMC concept.
-	LG reminds everyone that even for R10 CA, even if RAN1 was discussing carrier, RAN2 only sees a cell and not carrier.   For 6G the cell can have one carrier or multiple carrier and from RAN2 point of view we only see a cell.
Not treated
R2-2600083	Discussion on multi-carrier operation	vivo	discussion	Rel-20
R2-2600187	Discussion on 6G Spectrum and Access control	OPPO	discussion	Rel-20	FS_6G_Radio
R2-2600352	Discussion on multi-carrier operation	Fujitsu	discussion	Rel-20	FS_6G_Radio
R2-2600443	Multicarrier for 6GR	InterDigital France R&D, SAS	discussion	Rel-20
R2-2600493	Discussion on spectrum aggregation in 6GR	China Telecom	discussion	Rel-20	FS_6G_Radio
R2-2600504	Discussion on access control	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2600555	Multicarrier Operation for 6GR	Samsung	discussion	FS_6G_Radio
R2-2600608	Multi carrier operation for initial access	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
R2-2600682	Discussion on cell management and system access	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
R2-2600693	Views on 6G multi carrier operation in idle 	NTT DOCOMO, INC.	discussion
R2-2600697	6G multi-carrier operation	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
R2-2600720	Discussion on spectrum aggregation and multi-carrier operation in idle-mode	Nokia	discussion	Rel-20	FS_6G_Radio
R2-2600723	Discussion on multicarrier for 6GR	TCL	discussion	Rel-20
R2-2600726	Multi-carrier operation in Idle and spectrum aggregation	NEC	discussion	Rel-20	FS_6G_Radio
R2-2600748	Discussion on spectrum aggregation for Idle and Connected state	Lenovo	discussion	Rel-20
R2-2600768	RACH offloading in multicarrier	Sony	discussion	Rel-20	FS_6G_Radio
R2-2600786	Discussion on 6G Multi-Carrier	Qualcomm Incorporated	discussion	FS_6G_Radio
R2-2600787	Considerations for control plane design	Panasonic	discussion	Rel-20
R2-2600862	Multi Carrier Operation	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2600930	Consideration of other aspects for 6GR control plane 	Kyocera 	discussion	Rel-20
R2-2600939	Discussion on spectrum aggregation and access control	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2601058	Discussion on multi-carrier operation for 6G	ITL	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.5-p007`

