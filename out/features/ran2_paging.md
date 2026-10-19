# 6GR 寻呼

**当前进展** · 阶段：收敛中

RAN2 已形成方向性共识：6G 倾向以 CN 触发寻呼统一支持 Idle 与 Inactive UE，共用单一寻呼区域和寻呼 ID，并将 AS context 保存在最后服务的 RAN 节点。UE 在有直接 Xn/Xa 时可从原 RAN 节点获取 context；无直接连接时经 CN 存储或转发的可行性及实现仍交由 SA2、RAN3 研究。寻呼无线设计目标包括以单一 PF/PO 分布公式支持 clustered 与 uniform 分布、从第一天起支持非均匀 PO，并允许网络在时延与能耗间权衡。会议已记录多项设计目标与提案，但公式细节及部分配置和信令问题尚待后续阶段处理。

**未决问题**

- 无 Xn/Xa 时通过 CN 存储或转发 RAN context 的可行性、流程及安全验证方式。
- single paging area、context fetch 与 UE ID 的具体协议和实现，待 SA2、RAN3 协调。
- PF/PO 单一分布公式的需求、局限及具体设计，留待后续会议和 WI 阶段确定。
- 支持所有 DRX 周期的 bundling、更多或更密集的 PO/cluster 配置时，信令开销、最低周期与配置延迟如何处理。
- 基于 UE paging capabilities 分配 PO 的机制及其与现有基于 UE-ID 的基线关系。

## 跨会议演进脉络（6G）

2026年2月至5月，6GR 寻呼从统一 IDLE/INACTIVE 的 CN-triggered paging 方向，推进到明确 single paging area、single paging ID 的偏好及 last aNB 存储 AS context 的安排；无线侧逐步明确每个 UE paging cycle 监测一个 PO、以统一公式支持 clustered 和 uniform PF/PO，并增加 cluster 内 PO 密度与数量。跨组 context retrieval 和 CN procedures 仍待研究，具体 paging formula 留待 WI phase，尚无完整机制定案的证据。

### 关键进展

- 2月倾向于为 IDLE/INACTIVE 采用 single CN-triggered paging，并假设使用 single paging ID；4月进一步明确 CN-triggered mechanisms、single paging area（no RNA）及 single paging ID 的偏好，其中 idle 使用的 TA-like list 同样适用于 inactive，且 paging LS 已获批准。（依据：RAN2-133、RAN2-133bis）
- Context 存储从2月假设至少保存在 last RAN node，推进到4月同意 UE AS context 存储在 last aNB；新 aNB 有直接 Xa interface 时，可经 Xa 获取 context。（依据：RAN2-133、RAN2-133bis）
- 2月提出按 paging load 调整 UE 监测 PO 数量的研究方向；4月明确 UE 每个 paging cycle 监测一个 PO，5月以每个 UE paging cycle 监测一个 PO 再次明确。（依据：RAN2-133、RAN2-133bis、RAN2-134）
- PF/PO 设计从2月支持 non-uniform PO distribution、distributed/bundled PF/PO 的方向，推进到4月以一个 distribution formula 支持所有 paging cycles 下的 clustered 和 uniform PF/PO；5月进一步明确 cluster 内 POs 应更密集，且数量多于 NR Rel-19。（依据：RAN2-133、RAN2-133bis、RAN2-134）
- 2月提出 paging periodicities 可配置为 SSB periodicities 的倍数，并通过 offsets 调整 PO；支持 paging 的 Cell DTX 要求 PF/PO 位于 on duration 内，同时假设 single DL wake-up scheme，尽量统一 PEI 与 LP-WUS 的 upper layer procedure 和参数。后续材料未报告这些方向的进一步变化。（依据：RAN2-133）

### 待决问题

- 统一 CN-triggered paging 和共用 paging area 的跨组可行性仍缺乏确认结果；4月明确偏好并批准 LS，不足以证明2月提出的 paging area 大小、是否适用于 connected 子状态等问题已解决。（依据：RAN2-133、RAN2-133bis）
- 无 Xa interface 时，由 CN 存储 AS context 或经 CN 转移 context 的影响与实现仍需 SA2、RAN3 决定，并考虑安全信息及验证；context fetch 和用于识别 context storage 的 UE ID 也仍待研究。（依据：RAN2-133bis）
- Inactive UE 的 CN paging 触发及恢复 procedures 尚未确定；4月进一步列明 CN 缓冲 MT DL data/signaling、触发 paging 和通过 RRC resume 响应等内容仍需 SA2、RAN3 研究。（依据：RAN2-133、RAN2-133bis）
- 4月和5月均将 paging formula 的 requirements 及 shortcoming/limitations 整理留至下次会议，详细公式设计留待 WI phase；5月的全部 DRX cycle lengths 下 PF/PO bundling、更小 N、多个 clusters/Paging Possibility 等提案仅获 Noted，signaling overhead、最低周期及配置延迟仍待处理。（依据：RAN2-133bis、RAN2-134）
- 支持 idle/inactive UE paging、通知 system information change 与 ETWS/CMAS，以及 paging capacity（含 paging records）至少达到5G水平，在5月材料中仍为提出的要求；基于 UE paging-related capabilities 分配 PO 也尚无明确结论。（依据：RAN2-134）

### 会议时间线

- **RAN2#133**（2026-02-09 至 2026-02-13）：本会议推进了以 CN-triggered paging 统一 IDLE 和 INACTIVE 寻呼的设计方向，并倾向于共用 paging area，但其可行性仍需向 SA2 确认。为支持 fast resume，RAN2 假设 RAN context 至少可保存在 last RAN node，跨节点 context transfer 仍需与 SA2、RAN3 协调。寻呼无线侧设计明确面向灵活 PO 分布和网络节能，使网络能够在 paging delay 与 network energy savings 之间进行选择。
- **RAN2#133bis**（2026-04-13 至 2026-04-17）：本会议明确了 6G 寻呼对 CN-triggered mechanisms、single paging area（no RNA）及 single paging ID 的偏好，并同意 AS context 存储在 last aNB，批准了 paging LS。这为 idle/inactive 统一寻呼及恢复时的 context retrieval 确立了方向，但无 Xa 时通过 CN 获取或转发 context 的影响与实现仍需 SA2、RAN3 研究。PF/PO 方面明确 UE 每个 paging cycle 监测一个 paging occasion，并以单一 distribution formula 支持所有 paging cycles 下的 clustered 和 uniform PF/PO 为设计目标，具体公式留待 WI 阶段。
- **RAN2#134**（2026-05-18 至 2026-05-22）：本会议明确了 6G 寻呼中 UE 每个 UE paging cycle 监测一个 paging occasion，并以统一的 PF/PO distribution formula 支持 clustered 和 uniform PF/PO 为设计目标。会议明确 paging cluster 内需更密集地排列 POs，且每个 cluster 的 PO 数量应多于 NR Rel-19，为后续寻呼时机分布设计确定方向。具体 paging formula 的 requirements 和局限将于下次会议整理，详细公式设计留待 WI phase；部分配置与信令开销提案仅获 Noted。

## 6GR 演进

### [6G/Rel-20 RAN2#134] `agreement` 9.3.2.4 Paging

UE 在每个 UE paging cycle 监测一个 paging occasion。6G PF/PO design 目标是使用一个 PF/PO distribution formula，同时支持 clustered 和 uniform PF/PO；下一次会议将整理 paging formula 的 requirements 及需解决的 shortcoming/limitations，详细公式设计留待 WI phase。

```text
1	UE monitors a single paging occasion per UE paging cycle
2	For 6G PF/PO design, aim to use one single PF/PO distribution formula to support both clustered PF/PO and uniform PF/PO for all paging cycles.
3	For next meeting, capture requirements for paging formula and shortcoming/limitations we want to address for 6G.  The detailed formula design is left to WI phase.
Other Paging Requirements (Clustered PF/PO)
R2-2603015	Paging in 6G	Samsung	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.4-a001`

### [6G/Rel-20 RAN2#134] `agreement` 9.3.2.4 Paging

原文提出 paging cluster 可包含一个或多个 PF/PO，并支持 cluster 内 PO 间隔、每个 paging frame 配置多个 paging occasions，以及每个 UE paging DRX cycle 配置一个或多个 paging clusters。6G paging 应支持 idle 和 inactive UE 的 paging、向至少处于 RRC Idle/Inactive 的 UE 通知 system information change 与 ETWS/CMAS，并使 paging capacity（包括 paging records）至少达到 5G 水平；同时提出研究基于 UE paging-related capabilities 分配 paging occasions。

```text
A cluster can have one or multiple PF/PO
Support having gaps between Paging PF/PO within a cluster  (i.e., clustered paging)
Support configuration of multiple paging occasions associated with a paging frame
Support configuration of PO/PF close to common signals e.g. with SSB transmission
We aim to distribute UEs among Paging PO/PF
A RRC paging message should be able to address multiple UEs (e.g. like paging records in 5G).
Should be possible to have one or multiple paging clusters per UE paging DRX cycle.
From RAN2 point of view, paging mechanism in 6G allows network to:
Reach UEs in idle state and inactive state, through Paging messages.
Notify UEs at least in RRC Idle/Inactive states of system information change and ETWS/CMAS indications.  FFS whether SI change and ETWS/CMAS in RRC connected.
From RAN2 point of view, the paging capacity (including paging records) in 6G should be at least the same level as 5G.
Paging Message and Capacity Requirements
R2-2603033	Paging in 6G	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
Noted
UE Distribution to POs
R2-2604055	Discussion on 6G Paging	Qualcomm Incorporated	discussion
Proposal 3	UE determines the paging frames/occasions using the negotiated DRX cycle and UE ID and configured radio parameters (e.g. paging frame number in a paging cycle, paging occasion number in a paging frame).
R2-2604164	6G Paging Requirements	Ericsson	discussion
Observation 6	Uniform, UE identity-based PO assignment in NR does not account for UE paging capability differences, which limits paging efficiency when different UEs are paged together.
Proposal 6	Study mechanisms to support paging occasion assignment for UEs based on UE paging-related capabilities.
[15 min]
R2-2603085	Discussion on paging design	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
R2-2603088	Discussion on paging	NEC	discussion	Rel-20	FS_6G_Radio
R2-2603182	Discussion on 6G Paging	OPPO	discussion	Rel-20	FS_6G_Radio
R2-2603184	6G Paging Requirements	Ericsson	discussion	Withdrawn
R2-2603301	Paging in 6G	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2603328	Discussion on 6GR paging	China Telecom	discussion	Rel-20	FS_6G_Radio
R2-2603574	Paging for 6G	LG Electronics Inc.	discussion	Rel-20
R2-2603598	Discussion on paging for 6GR	TCL	discussion
R2-2603629	Discussion on paging aspects related to LP-WUS and single paging mechanism	Sony	discussion	Rel-20
R2-2603667	Paging for 6GR	InterDigital, Inc.	discussion	Rel-20	FS_6G_Radio
R2-2603732	Views on 6G paging	Apple	discussion	Rel-20	FS_6G_Radio
R2-2603844	Discussion on Paging in 6GR	Sharp	discussion	Rel-20	FS_6G_Radio
R2-2603848	Discussion on 6G paging	ETRI	discussion	Rel-20
R2-2603881	Views on 6G Paging	NTT DOCOMO	discussion
R2-2603902	Discussion on paging of 6GR	Spreadtrum, UNISOC	discussion	Rel-20
R2-2603908	Discussion on paging requirements for 6GR 	Kyocera 	discussion	Rel-20
R2-2603954	Discussion on Paging for 6GR	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2603980	Discussion on paging for 6GR	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2604048	Paging Subgrouping in 6G	Google Korea LLC	discussion
R2-2604070	Paging Handling	Nokia	discussion	Rel-20	FS_6G_Radio
R2-2604096	Discussion on 6G paging for energy efficiency	CSCN	discussion	Rel-20	FS_6G_Radio
R2-2604134	Discussion on PF/PO design	Transsion Holdings	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.4-a002`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.4 Paging

Paging cluster 内的 paging occasions 需要更密集排列。相比 NR Rel-19，每个 paging cluster 应包含更多 POs。

```text
The paging occasions within a paging cluster must be more densely packed, resulting in a paging cluster containing a greater number of POs compared to NR Rel-19.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.4-o001`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.4 Paging

提出 6G 的 PF/PO bundling 应支持所有 paging DRX cycle lengths，而不局限于特定周期，并允许更小的 N（如 T/64、T/128、T/256）。会议记录了对 signaling overhead、最低周期以及配置延迟的不同意见，结论为 Noted。

```text
In 6G, paging design should not limit clustering of PF/POs only for specific paging DRX cycle length (e.g. shortest paging DRX cycle length). Bundling of PF/POs should be supported for all paging DRX cycle lengths. Allow smaller values of N such T/64, T/128, T/256 and so on.
-	Vivo is not sure as this would increase the signaling overhead.   Samsung thinks that we can study how to reduce the singaling overhead and anyways this is network configuration so they can decide how to configure.   Huawei thinks that overhead issue is a secondary issue and there are ways to solve it.   Interidigtal thinks that we should design it in a better way and are not restricted to 5G design, so this shouldn’t be a problem.
-	Qualcomm is concerned that we don’t know what is the lowest cycle.   Huawei thinks it would be 32.
-	 Ericsson thinks that we should keep the N restricted to larger delays.
-	Ericsson is concerned that we end up with configuration that CN assumes for example 320ms but the RAN is only 640ms.
Noted
R2-2603209	Discussion on 6G Paging	CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.4-p001`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.4 Paging

RAN2 的目标是确保在单个 PF 内增加 POs 时，PO configurations 的 signaling overhead 不会显著增加。Nokia 和 Apple 认为该问题应予考虑，但指出其处于 stage 3；结论为 Noted。

```text
RAN2 aim to ensure the signaling overhead of PO configurations should not be increased significantly with the increased POs within one PF.
-	Nokia and Apple thinks it should be considered but it quite stage 3.
Noted
R2-2603562	Paging considerations for 6G	Lenovo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.4-p002`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.4 Paging

提出支持在单个 DRX cycle 内配置一个或多个 paging clusters。每个 cluster 包含一个或多个 Paging Possibility；结论为 Noted。

```text
RAN2 to support the configuration of one or multiple paging clusters within a single DRX cycle, each containing 1 or more Paging Possibility.
Noted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.4-p003`

### [6G/Rel-20 RAN2#133bis] `agreement` 9.3.2.4 Paging

RAN2 同意 AS context 存储在 last aNB，并同意 CN-triggered mechanisms、single paging area（即 no RNA）和 single paging ID 的偏好，以及向 RAN3 提供 resume ID 相关协议。对于 UE 在新 aNB 恢复时的 context retrieval，已识别经 Xa 直接获取，以及无 Xa 时由 CN 存储或转发两类情形；相关影响和实现由 SA2、RAN3 决定，paging LS 已获批准。

```text
Indicate to SA2/RAN3 that RAN2 agreed:
-	The AS context is stored in the last aNB.
-	Agreement on CN-triggered mechanisms
-	agreement on preference on single paging area (i.e. no RNA) and one single paging ID
-	provide RAN3 with agreement on resume ID
RAN2 has identified the following options for context retrieval –
-	There are two cases for when cotext retrieval is needed
1	UE resumes in a new aNB that has a direct Xa interface.  The context can be fetched directly from last aNB via Xa
2	UE resumes in a new aNB that doesn’t have an Xa interface.    RAN2 would like to ask SA2 how the context can be transferred to aNB.  Two options were identied: CN also stores the AS context or transferred via CN.
The impact and how this is done is up to SA2 and RAN3
Provide background on why single paging is beneficial
Provide background that we agreed that the RAN context will be stored in last aNB and why (e.g. low latency)
Provide background on what is stored as part of AS context (including security) and need for verification.   SA2 should take into account these possible issues in the case where the CN would store AS context when making a decision.
Ask SA2
-	About feasibility of single paging area and explain the benefit of this single paging
DL data
-	For MT data, RAN2 discussed DL traffic buffered in CN, but it is up to SA2 how to handle DL traffic in the above scenarios that RAN2 has identified.
[POST133bis][007][6G CP] Paging LS to SA2 (ZTE)
Intended outcome: agree to LS to SA2
Deadline:  short post
=> Approved in R2-2602817.
R2-2602817	LS on single paging mechanism for idle and inactive in 6G	RAN2	LS out	Rel-20	FS_6G_Radio	To: SA2, RAN3
=> Approve
R2-2601574	Discussion on 6G Paging	OPPO	discussion	FS_6G_Radio
Observation 1	In LTE/NR, the handling of DL data arrival and paging depends on the RRC state of the UE: 1)For RRC_IDLE (with suspend), DL data arrival is detected by CN and paging is triggered by the CN. 2)For RRC_INACTIVE, DL data arrival is detected by RAN, and paging is triggered by the RAN.
Proposal 1	For a single paging mechanism in 6G, RAN2 asks for feedback from SA2/RAN3 on the feasibility/preference on how “single paging” is implemented, including 1) which network entity to detect the DL data arrival, e.g., last serving RAN or CN, 2) which entity to trigger paging, e.g., last serving RAN or CN.
Proposal 2	RAN2 asks SA2 and RAN3 to study DL data delivery mechanisms to the UE under different data-buffering entity options, i.e., how to perform the data forwarding when UE moves out of last serving RAN node.
UE Identifier and paging area
R2-2602348	Discussion on unified paging in 6GR	Rakuten Symphony	discussion	Rel-20
Observation 1		A single Paging area for both INACTIVE and IDLE will compromise the performance of INACTIVE UEs.
Observation 2		In 5G, gNB ID is 24 bits out of a full I-RNTI’s 40 bits. This causes mismatch with the global gNB ID (32 bits) and is therefore susceptible to collisions in identifying a UE’s old serving gNB unambiguously.
Proposal 1		CN-based unified paging operates at two different granularities of Paging area, INACTIVE UEs at RNA level and IDLE UEs at TA level.
Proposal 2		I-RNTI and S-TMSI are used as UE identifiers in CN-based unified paging for RRC Inactive and IDLE in 6G respectively.
Noted
Not treated
R2-2601675	Consideration on single CN-triggered Paging	CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.4-a001`

### [6G/Rel-20 RAN2#133bis] `agreement` 9.3.2.4 Paging

UE 在每个 paging cycle 监测一个 paging occasion。6G PF/PO 设计目标是使用一个 distribution formula，同时支持所有 paging cycles 下的 clustered PF/PO 和 uniform PF/PO；下次会议记录 paging formula 的需求及待解决的局限，具体公式设计留待 WI 阶段。

```text
1	UE monitors a single paging occasion per UE paging cycle
2	For 6G PF/PO design, aim to use one single PF/PO distribution formula to support both clustered PF/PO and uniform PF/PO for all paging cycles.
3	For next meeting, capture requirements for paging formula and shortcoming/limitations we want to address for 6G.  The detailed formula design is left to WI phase.
Not treated
UE Distribution to POs
R2-2602476	Views on 6G Paging	NTT DOCOMO	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.4-a002`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.2.4 Paging

Rel-19 paging adaptation 的 Restriction#1 是无法支持大于 32 radio frames 的 paging cycle，因为 N 的取值范围仅扩展到 1/32。原文指出，较小的 N 需要更大的 Ns 补偿 PF 数量减少，而较大的 Ns 会因 PMO offset 随 Ns 线性增加而显著增大 SIB1 size。

```text
Restriction#1 of Rel-19 paging adaptation: it can’t support paging cycle>32 radio frames (i.e. 64/128/256 radio frames) because value range of N is only extended to 1/32 due to the following concerns:
1)	The actual paging cycle may be restricted by UE dedicated paging cycle configured by NAS.
2)	N<1/32 requires to introduce larger Ns>8 to compensate the decrease of PF number. However, larger Ns value will lead to significant increase of SIB1 size as the PMO offset linearly increases according to Ns.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.4-o001`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.2.4 Paging

NR 中，paging 的 PDCCH 和 PDSCH 按 N*X 次发送，其中 N 是小区中发送的 SSB 数量，X 是每个 SSB 的重复次数。原文指出，这会造成显著开销并增加网络能耗。

```text
In NR, PDCCH and PDSCH for paging are transmitted ‘N*X’ times, where N is the number of transmitted SSBs in the cell and X is the number of repetitions per SSB. This leads to significant overhead and increased network energy consumption.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.4-o002`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.4 Paging

RAN2 提出对 Inactive state 的 UE paging response procedure 采用如下步骤，并请 SA2/RAN3 进一步研究：DL data 缓存在 CN（如 UPF），CN 向 paging area 内的 RAN nodes 发送 paging request，UE 通过 RRC resume 响应。若部署 Xn，UE AS context 可从 last RAN node 直接获取；否则可从 CN 获取或经 CN 转发。

```text
RAN2 assumes the following steps can be applied to UE paging response procedure in Inactive state and ask SA2/RAN3 for further study.
- The downlink data is buffered in CN (e.g. UPF)
- CN sends paging request to the RAN nodes within the paging area. Details are left to SA2 and RAN3.
- UE performs RRC resume procedure to respond paging
- UE AS context can be fetched from the last RAN node directly if Xn interface is deployed. Details are left to SA2 and RAN3.
- UE AS context can be fetched from CN (if stored in CN) or via CN (CN as a relay) if Xn interface is not deployed. Details are left to SA2 and RAN3.
Noted
R2-2602433	Discussion on Paging for 6GR	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.4-p001`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.4 Paging

对于 UE context transfer，RAN2 支持两种方案：new serving RAN node 与 last serving RAN node 之间有 Xn 时，由前者从后者获取 UE context；没有 Xn 时，UE context 经 NG interface 由 core network 转发。RAN2 将向 SA2 发送 LS 询问后一方案的可行性。

```text
For UE context transfer, RAN2 support both of the following solutions:
-Xn solution：In the scenarios with an Xn interface between a new serving RAN node and the last serving RAN node, the new serving RAN node can fetch UE context from the last serving RAN node;
-NG solution：In the scenarios without an Xn interface between a new serving RAN node and the last serving RAN node, UE context is forwarded by the core network through the NG interface. And RAN2 send LS to ask SA2 about feasibility.
Noted
R2-2601508	Single paging design in 6GR	Xiaomi	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.4-p002`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.4 Paging

RAN2 同意 UE AS context 存储在 last serving aNB；若新 aNB 有直接 Xa interface，则可经 Xa 获取。若无 Xa interface，RAN2 提出请 SA2 研究通过 CN 获取 context 的两种选项：由 CN 存储 AS context，或经 CN 转移；影响及实现方式由 SA2 和 RAN3 决定，并需考虑安全信息及验证。

```text
Check with SA2/RAN3 on the feasibility of below options for UE AS context retrieval and ask for their feedback:
[Option 0]: UE AS context is stored in last serving aNB and is retrieved via Xa.
[Option 1]: UE AS context is stored in the RAN and is retrieved via CN.
[Option 2]: UE AS context is stored in the CN and is retrieved via CN.
Noted
Discussion
-	ZTE thinks that the only thing we didn’t agree is if the CN is also stored in the CN.
-	Samsung thinks that we can just tell SA2 that we have two options and the other WGs can decide.
-	ZTE thinks that there may be a problem with CN AS storage as security context is part of stored information.   Apple thinks that the problem with security is not just storage it also has to verify, which would require a new SA3 mechanism.
Indicate to SA2/RAN3 that RAN2 agreed:
-	The AS context is stored in the last aNB.
RAN2 has identified the following options for context retrieval –
-	There are two cases for when cotext retrieval is needed
1	UE resumes in a new aNB that has a direct Xa interface.  The context can be fetched directly from last aNB via Xa
2	UE resumes in a new aNB that doesn’t have an Xa interface.    RAN2 would like to ask SA2 how the context can be transferred to aNB.  Two options were identied: CN also stores the AS context or transferred via CN.
The impact and how this is done is up to SA2 and RAN3
Provide background that we agreed that the RAN context will be stored in last aNB and why (e.g. low latency)
Provide background on what is stored as part of AS context (including security) and need for verification.   SA2 should take into account these possible issues in the case where the CN would store AS context when making a decision.
---
R2-2601538	Paging in 6G	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.4-p003`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.4 Paging

请 SA2 和 RAN3 研究支持 6G single paging mechanism 的事项：为 UE 在 idle 和 inactive state 定义 single paging area，在该区域内定义有无 Xn interface 时的 UE context fetch，并定义用于识别该区域内 context storage 的 UE ID。

```text
Ask SA2 and RAN3 to work on the following aspects to support single paging mechanism in 6G:
Define single paging area for UE in idle and inactive state
Define UE context fetch with or without Xn interface within this paging area
Define UE ID to identify the UE context storage within this paging area
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.4-p004`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.4 Paging

对于 MT traffic，RAN2 倾向于在 CN 缓冲 DL data 和 signaling，并为 inactive state 触发 paging。RAN2 请 SA2 和 RAN3 研究支持该方案的 procedures。

```text
For MT traffic, RAN2 prefer to have DL data and signaling buffered in CN and trigger paging for inactive state and would like to ask SA2 and RAN3 to work on the procedures to support this.
Noted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.4-p005`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.4 Paging

RAN2 澄清 single paging area 的理解：6G idle state 使用的 TA-like list 也适用于 inactive state。该方案用于 single CN-triggered paging mechanism。

```text
RAN2 to clarify the understanding of the single paging area for both idle and inactive state:
A TA like list in 6G used for idle state is also applied to inactive state for single CN triggered paging mechanism.
R2-2601693	Discussion on paging	NEC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.4-p006`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.4 Paging

single paging framework 提议在 paging message 中使用由 6GC 分配的 S-TMSI-like UE temporary identity 寻址目标 UE，并在 RRC_INACTIVE UE 的 RRCResumeRequest-like message 中包含由 last serving aNB 分配的 RNTI-like identity。RRC_IDLE 和 RRC_INACTIVE UE 共用 NAS level registration area 与 periodical registration update timer；若 6G 支持 legacy paging，PF/PO calculation 仅使用 cell default DRX cycle 和 UE specific DRX cycle，I-RNTI 与 NCC 配置给 RRC_INACTIVE UE。

```text
For single paging framework, the following points are proposed:
S-TMSI like UE temporary identity allocated by 6GC is used in paging message to address the target UE.
RNTI like identity allocated by the last serving aNB will be included in RRCResumeRequest like message for RRC_INACTIVE UE. The profile of I-RNTI in 6G is FFS.
NAS level registration area, NAS level periodical registration update timer (e.g., T3512 like timer) are common for both RRC_IDLE and RRC_INACTIVE UE.
only cell default DRX cycle and UE specific DRX cycle are used for PF/PO calculation if legacy paging is supported in 6G.
I-RNTI and NCC are configured for RRC_INACTIVE UE.
Paging formula principles
R2-2601583	Efficient 6G Paging	Ericsson	discussion
Proposal 1	Study clustering of POs based on NR Rel-19 paging mechanism.
Noted
R2-2602232	Views on 6G Paging	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.4-p007`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.4 Paging

6G PF/PO design 的目标是使用一个 single PF/PO distribution formula，原生支持所有 paging cycles 的 clustered PF/PO 和 uniform PF/PO。讨论中提出 re-using current paging formula 作为 baseline，并探讨 paging requirements、每 cell 一组参数及 signalling overhead。

```text
For 6G PF/PO design, aim to use one single PF/PO distribution formula to natively support both clustered PF/PO and uniform PF/PO for all paging cycles.
Noted
Discussions
-	Samsung thinks that if network wants to prioritize NAS gain we can remove the restrictions and for the PMO offset it is anyways options so we can remove signaling overhead.  So re-using the current paging formula is the baseline.   Apple thinks that PMO offset is a RAN1 issue so we can keep it in mind in the future.
-	Nokia agrees with apple as it is a little earlier and we should discuss what are the requirements for paging, UE only needs to monitor only one paging frame and enable the clustering and have multiple paging frames in one clusters, and uniform paging cycles.
-	Qualcomm asks if we should strive to have one set of parameters per cell for the UE.  Nokia and Apple agrees.
-	Huawei thinks that we should investigate and optimize signalling overhead.
-	Nokia thinks that we have to have some requirements.   Samsung thinks we should discuss the limitations of NR.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.4-p008`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.4 Paging

现有基于 UE-ID 的 PF/PO determination 应作为 6G baseline 保留。另有提案研究基于 UE paging-related capabilities 的 paging occasion assignment 机制，以处理不同 UE paging capability 带来的效率问题。

```text
	The existing UE-ID-based PF/PO determination should be kept as the baseline for 6G.
R2-2601583	Efficient 6G Paging	Ericsson	discussion
Observation 2	Uniform, UE identity-based PO assignment in NR does not account for UE paging capability differences, which limits paging efficiency when different UEs are paged together.
Proposal 3	Study mechanisms to support paging occasion assignment for UEs based on UE paging-related capabilities.
Other Energy Efficiency Mechanisms
R2-2601517	Paging in 6G	Samsung	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.4-p009`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.4 Paging

被 WUS 唤醒的 UE 发送 indication（例如在 random access occasion 上发送 single shot PRACH），指示其处于特定 SSB 的覆盖范围。网络据所指示的 SSB，在 PO 上发送用于 paging 的 PDCCH/PDSCH。

```text
UE(s) waked up by the WUS, transmits indication (e.g. single shot PRACH in random access occasion) to indicate that UE is in coverage of a specific SSB. Network transmits PDCCH/PDSCH for paging in PO using the indicated SSB(s).
R2-2601452	Discussion on paging	vivo	discussion	Rel-20
R2-2601611	Discussion on paging design	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
R2-2601670	Paging Handling	Nokia	discussion	Rel-20	FS_6G_Radio
R2-2601720	Discussion on single paging mechanism	Panasonic	discussion	Rel-20
R2-2601732	Discussion on 6GR Paging, DL WUS and paging optimizations	Nordic Semiconductor ASA	discussion	Rel-20
R2-2601862	Paging in 6G	Ofinno	discussion
R2-2601944	Discussion on paging for 6GR	TCL	discussion
R2-2601962	Paging for 6G	LG Electronics Inc.	discussion	Rel-20
R2-2601971	Consideration on 6GR paging	China Telecom	discussion	Rel-20	FS_6G_Radio
R2-2601999	Discussion on paging	Sharp	discussion	Rel-20
R2-2602013	Paging in 6G	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
R2-2602098	Discussion on paging of 6GR	Spreadtrum, UNISOC	discussion	Rel-20
R2-2602125	Paging considerations for 6G	Lenovo	discussion	Rel-20
R2-2602390	Discussion on 6GR paging	ETRI	discussion	Rel-20
R2-2602444	Consideration of paging framework for 6GR 	Kyocera 	discussion	Rel-20
R2-2602546	Views on Paging in 6G	1Finity	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.4-p010`

### [6G/Rel-20 RAN2#133] `agreement` 10.3.2.4 Paging

RAN2 倾向于为 idle 和 inactive state 采用基于 CN triggered paging mechanism 的单一 paging mechanism，并倾向于共用一个 paging area，但需向 SA2 确认可行性。为支持 fast resume，RAN2 假设 RAN Context 至少可存储在 last RAN node；对于 UE 不在 last known cell 时的 context transfer（有或无 Xn），需进一步询问 SA2，并与 SA2、RAN3 后续讨论。

```text
For paging RAN2 is exploring the possibilities and feasibility and has concluded on these preferences:
1	From RAN2 perspective the preference is to have a single paging mechanism from UE and NW perspective for idle and inactive state, based on CN triggered paging mechanism.
2	RAN2 has a preference to have a single paging area for both idle and inactive state, but need to ask SA2 about feasibility.
For UE context fetch
3	To enable fast resume, RAN2 assumes at least the RAN Context stored may be stored the last RAN node. Where else can be stored would depend on SA2/RAN3.
4	RAN2 discussed RAN context transfer, for the case where the UE is not in the last known cell.  There are two scenarios with Xn or without Xn.  Need to ask SA2 if they can study how to deal with context transfer.
5	Ask SA2 and RAN3 next meeting after some further progress on Inactive state and explains that we need fast transitions etc
Content
R2-2600457	Views on 6G Paging	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-a001`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.4 Paging

5G 的 dual-paging mechanism 增加了不必要的复杂度，并依赖并非始终可用的 Xn connectivity，从而阻碍 RRC_INACTIVE 的部署。

```text
Lesson Learned from 5G: The dual-paging mechanism in 5G creates unnecessary complexity and relies on Xn connectivity that is not always available, hindering the deployment of RRC_INACTIVE.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-o001`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.4 Paging

为满足 6G 快速状态转换的时延要求，preferable to store the UE context in the RAN，以便快速检索。

```text
To meet 6G latency requirements for fast state transitions, it is preferable to store the UE context in the RAN for rapid retrieval.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-o002`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.4 Paging

需要机制在直接 Xn connectivity 不可用时，通过 Core Network（或其他间接路径）在 gNB 间传输 RAN context。

```text
Mechanisms are needed to allow the transfer of RAN context between gNBs via the Core Network (or other indirect paths) when direct Xn connectivity is unavailable.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-o003`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.4 Paging

当前规范支持 NG-RAN node 在 UE 进入或离开 RRC_INACTIVE state 时向 AMF 通知 UE 的 RRC state。

```text
Current specs support NG-RAN node to notify the AMF of the UE RRC state when the UE enters or leaves RRC_INACTIVE state.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-o004`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.4 Paging

当前规范中，UPF 在收到发往 CM-IDLE state UE 的下行数据后，可以触发 CN paging procedures。

```text
In current specs, UPF can trigger CN paging procedures upon receiving downlink data for UE in CM-IDLE state.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-o005`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.4 Paging

实现 RRC_INACTIVE UE 单一 paging mechanism 有两种选项：Option 1 是 UE 进入 RRC_INACTIVE 时由 RAN node 通知 core network 状态变化；Option 2 是收到 UPF 下行数据或 AMF 下行信令时，由 RAN node 指示 core network 为该 UE 触发 CN paging。

```text
There are two Options to realize the single paging mechanisms for RRC_INACTIVE UE:
-Option 1：Upon a UE entering the RRC_INACTIVE, RAN node informs the core network the RRC state change.
-Option 2: Upon DL data from UPF or DL signaling from AMF arrival, RAN node indicates the core network to trigger CN paging for RRC_INACTIVE UE.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-o006`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.4 Paging

在 NR paging design 中，UE 可根据不同的 paging UE-IDs 区分 IDLE paging 和 INACTIVE paging。

```text
In NR paging design, UE can distinguish IDLE paging and INACTIVE paging based on the different paging UE-IDs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-o007`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.4 Paging

从降低 UE complexity 的角度进行 6G paging study 时，应考虑在 paging message 中纳入比 5G 更多的 paging cause。

```text
6G paging study from UE complexity reduction perspective should consider including more paging cause than 5G in the paging message.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-o008`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.4 Paging

5G paging adaptation solution 因 backward compatibility 而 NES gain 有限，且无法灵活启用 PF bundling。

```text
5G paging adaptation solution has limited NES gain due to backward compatibility and it can’t flexibly enable PF bundling.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-o009`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.4 Paging

从网络能效角度开展 6G paging 研究，应将非均匀 PO 分布方向以灵活方式纳入 day-1 设计考虑。

```text
6G paging study from the network energy efficiency perspective should consider the non-uniform PO distribution direction in flexible way as day-1 design.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-o010`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.4 Paging

在 NR 中，paging DRX 周期不超过 32 个 radio frames 时，可以在周期开始时配置所有 PFs/POs。对于 T > 32（如 64、128、256 个 radio frames）的较长周期，无法在 DRX 周期开始时配置所有 PFs/POs。

```text
In NR, for paging DRX cycles of up to 32 radio frames, it is possible to configure all PFs/POs at the beginning of paging DRX cycle. For longer paging DRX cycles of T > 32 such as 64, 128, 256 radio frames, all PFs/POs cannot be configured at the beginning of DRX cycle T.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-o011`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.4 Paging

原文指出，NR 设计较为僵化，始终优先考虑 paging delay，未给网络在 paging delay 与 network energy savings 之间作出选择的余地。

```text
NR design is rigid as it always prioritizes paging delay and does not give network a choice to decide between paging delay and network energy savings.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-o012`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.4 Paging

网络可通过控制 UE paging occasions 的时机，使其与预期 paging frequency 相匹配，从而实现能耗节省。

```text
The network can achieve energy savings by controlling the timing of the paging occasions of UEs relative to the expected paging frequency.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-o013`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.4 Paging

RAN2 倾向于将 CN-triggered paging 作为 6G 中 IDLE 和 INACTIVE（或等效子状态）UE 的统一 paging 机制。讨论中提出了 paging 区域大小以及该机制是否适用于 connected 子状态等问题。

```text
RAN2 preference is for CN-triggered paging as the unified paging mechanism for both IDLE state and INACTIVE state (or equivalent substate) UEs in 6G.
-	Lenovo asks if this has the problem that the CN has to page across a large area even in connected.  Interdigital thinks that we should study how to page in a small area
-	Samsung asks if this is for inactive only.
-	Vivo asks if this applied for the connected sub-state.    Huawei thinks this should be only for inactive.
-	Mediatek asks if we are going to ask CN to page the UE in connected.  Interdigital thinks that even for inactive the UE is in CN connected and we’d have to ask them if they can do it.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-p001`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.4 Paging

RAN2 将向 SA2 发送 LS，说明其倾向于对 6G Inactive 状态（或等效子状态）的 UE 采用 CN-initiated paging。

```text
RAN2 to send an LS to SA2 indicating the preference for CN-initiated paging for UEs in the 6G Inactive state (or equivalent substate)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-p002`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.4 Paging

RAN2 应假设：Xn 可用时优先从 RAN 快速检索 context；Xn 不可用时，则通过 CN/RAN3 机制传输 context。讨论中将 CN context fetching 视为 fallback。

```text
RAN2 should assume context retrieval mechanisms that prioritize fast retrieval from the RAN when Xn is available, while assuming context transfer via the CN/RAN3 mechanisms when Xn is unavailable.
-	Lenovo thinks we can minimize the looping with CN direct involved.  Interdigital thinks that we need to ask SA2 what is possible.
-	Xiaomi asks whether we would end up supporting more than one RAN context transfer.  Interdigital thinks that the CN context fetching is like a fallback.
-	Frauohaufer explains that some analysis show that 95% of the time the UE is in the same cell, so do we need to care about the other cases.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-p003`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.4 Paging

RAN2 将与 RAN3 和 SA2 协调，确定通过 CN 节点（NG interface）传输 RAN context、以支持 Xn 部署稀疏场景下 mobility 的可行性。该事项为 Noted。

```text
RAN2 to coordinate with RAN3 and SA2 to determine the feasibility of transferring RAN context via CN nodes (NG interface) to support mobility in sparse Xn deployments
Noted
R2-2600957	Discussion on Paging open issues for 6GR	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-p004`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.4 Paging

UE 进入 RRC_INACTIVE 时，RAN node 通知 core network 状态变化；该事项为 Noted。讨论涉及通知对 latency 的影响、paging area、context 保留位置及相关机制等问题。

```text
Upon a UE entering the RRC_INACTIVE, RAN node informs the core network the RRC state change.
Noted
Discussion on paging
-	Nokia asks if the CN impact and latency are impacted.    Interdigital thinks that it does impact latency in those cases.  Qualcomm explains that even in NR we started by the CN not knowing that the UE is in inactive, but at the end we had to notify CN about UE moving to inactive.  Also they are designing the new system and they can have a fast mechanism.  Nokia thinks that we should have more details on how we envision it from RAN2.   Nokia is concerned that we may to report everytime it changes state.
-	Ericsson thinks that the modelling of the CN state is a SA2
-	Ofinno asks how it works for SDT and thinks we need to involve RAN3 as well.
-	Lenovo ask what is the paging area, is it a RAN area.   CMCC doesn’t thinks there will be a RAN area just a tracking area like in Idle.
-	CMCC thinks that because the UE access the same cells most of the time we should keep the context in the last serving cell.   Honor agrees with CMCC and we may need to have two areas for this paging.
-	Ericsson thinks that the CN can store the DL data and because the paging is monitored every second the delay is not so problematic.
-	Qualcomm thinks that we should just provide the requirements to SA2, with Xn or without Xn and the SA2 can analyse.
-	Vivo thinks that the UE ID needs to be extended to include gNB ID and CN ID so RAN1 should also be involved. CMCC explains that the CN knows where gNB is as it is connected. ZTE thinks that we need an ID to identify where the context is stored and we can discuss whether we want to make it complete and the whole ID included.
-	Huawei assumes the paging are will be the same and perhaps to fit both idle and inactive we would have to design a area that’s a bit smaller than normal tracking area, but that’s not a problem.
-	Mediatek is not sure about how to distinguish from redesigning INACTIVE.  ZTE explains that the network strategy is already send paging first in serving cell first and then the rest. Mediatek ask then what is the benefit for inactive. ZTE explain that there is benefit as the UE is likely in the last serving cell. Huawei thinks there may be some CN impact if the UE is not in the last serving cell and we would need to study what it is.
-	Fraunhoufer thinks that we should notify the network when we leave the serving cell.
-	Nokia thinks we should try to have a set of questions.
-	LG thinks that there is not strong reason to have a separate area than idle tracking area since only 5% of the time the UE has left the cell.
-	Apple ask whether the NG interface is kept for the UE when the UE is inactive. Fujitsu thinks that this is an SA2 study.
-	Mediatek would like to avoid having separate monitoring mechanisms.
-	Nokia asks if the assumption that we mainly focus on UEs and Idle in lower bands.
-	Mediatek thinks we need to be very specific in what we ask SA2 and provide the end to end view.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-p005`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.4 Paging

在同时支持 IDLE paging 和 INACTIVE paging 的单一 paging 设计中，UE 需要通过 paging record 区分两类 paging。可采用不同的 paging UE-IDs 或新的 state indication。

```text
In the single paging design for both IDLE paging and INACTIVE paging, UE needs to be able to distinguish between the two types of paging through the paging record, either through different paging UE-IDs or the new state indication.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-p006`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.4 Paging

对于 single CN triggered paging，RAN2 假设可使用 single paging ID，目前没有动机在 paging message 中区分状态。对于 resume，UE ID 尚待讨论，可能不同于 paging ID；此外，Rel-19 NR paging mechanism（支持 clustered POs）被视为研究基线。

```text
6G paging should support the paging cause included in paging message.
-	Huawei thinks it is not that simple as there are cases where the UE doesn’t need to look into the paging message. Apple thinks that from the UE side it needs to know the reason for this paging
-	CMCC asks why do we need to differentiate if the UE is in idle or inactive.  Apple explains that the procedures are different for idle and inactive. CMCC explains that the UE knows it is in inactive. ZTE thinks that we need a different ID in INACTIVE as we need it to fext the context and identify gNB. Lenovo agrees with CMCC.
-	LG thinks that this is related to UE and NW state mistmatch and if this mistmatch can still happen the UE should be able to differentiate. Huawei agrees it may still occur so we either need to have a different ID or an indication. Ericsson thinks that mistmatch is not a problem as we always have a fallback mechanism.
-	Qualcomm thinks that we need to differentiate between paging and resume.  For paging we can use same ID but for resume we would need different IDs, like I-RNTI.
-	ofinno indicate that we may have WUS or paging message and we’d need to consider both.
-	Vivo thinks that NR should be baseline.
-	ZTE also thinks that the UE may lose the context and a mistmatch but if the CN is doing the paging we can use the same paging.
Noted
Paging Occasion Distribution for Network Energy
R2-2601111	Discussion on paging for 6G	Ericsson	discussion
Proposal 1	The Rel-19 paging mechanism in NR, which enables clustered POs is considered as baseline for the study.
-	Lenovo asks whether they see any paging capacity issues.  Ericsson hasn’t seen any and this includes IoT.
Noted
R2-2600457	Views on 6G Paging	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-p007`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.4 Paging

6G paging 从第一天起应支持 non-uniform PO distribution design。

```text
6G paging should support the non-uniform PO distribution design from day-1.
Noted
R2-2600058	Paging in 6G	Samsung	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-p008`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.4 Paging

6G paging design 应允许网络在 paging delay 与 network energy savings 之间进行选择。

```text
Paging design in 6G should give network choice to decide between paging delay and network energy savings.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-p009`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.4 Paging

6G paging design 支持在 paging DRX cycle 中采用 distributed 或 bundled PF/PO，且 bundling 应适用于所有 paging DRX cycle 长度。

```text
Paging design in 6G should enable both distributed and bundled PF/POs in paging DRX cycle. The bundling should be supported for all paging DRX cycle lengths.
Noted
Discussion
-	Huawei supports the clustered design and there was some concerns in Rel-19 because of legacy so it can be used as starting point but we should look at making it better.
-	Vivo thinks we should have a unified design for PF/PO and the CN paging cycle should be respected.
Not treated
R2-2601124	Paging in 6G	Nokia	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-p010`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.4 Paging

6G 应支持 legacy approach（non-clustered paging allocation）和 clustered paging allocation，以适配不同场景中的 paging frame 分配。

```text
6G should enable both legacy approach (non-clustered paging allocation) and clustered paging allocation to allocate paging frame to support different scenarios in 6G.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-p011`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.4 Paging

应可将 paging periodicities 配置为 SSB periodicities 的倍数，以便与 SSB transmissions 对齐；也应允许在计算中配置 offsets，使 paging occasions 不必恰好位于 SSB 的相同 slots。

```text
It should be possible to configure paging periodicities to be multiples of SSB periodicities in order to align with SSB transmissions and also offsets to calculations should be allowed to not require paging occasions being exactly in the same slots as SSBs
R2-2600714	Paging in 6G	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-p012`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.4 Paging

支持 paging 的 Cell DTX，且 PF 和 PO 位于 Cell DTX on duration 内。

```text
Support Cell DTX for paging, with PF and PO located in Cell DTX on duration.
Paging occasions Configuration for Network Energy
R2-2600440	Paging for 6GR	InterDigital France R&D, SAS	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-p013`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.4 Paging

Paging occasion configuration 应能适配不同的网络和 UE 活跃程度；提议研究由 paging load 调整、供 UE 监测的可变数量 paging occasions。RAN2 假设采用 single DL wake-up scheme；对于 UE 节能，PEI 和 LP-WUS 的 upper layer procedure 与参数应尽量统一。

```text
Paging occasion configuration is designed to be adaptable to different levels of network activity (e.g., resulting from a different number of served UEs) and UE activity (e.g., potential/active services at the UE).
Noted
R2-2600546	Paging for 6G	LG Electronics Inc.	discussion	Rel-20
Observation 1	For paging transmission in NR, the network must remain active during a fixed number of paging occasions regardless of the actual paging load, due to the static mapping between UE ID–based paging groups and paging occasions.
Proposal 1	Study the dynamic allocation of paging occasions to be monitored by UEs, enabling operation with a variable number of paging occasions that adapt to the paging load.
Noted
Discussion
-	Apple thinks that we discussed this in Rel-18 but the conclusion was that the system load doesn’t change dynamically
-	Xiaomi is concerned as it increase UE complexity
UE Power Savings
R2-2600186	Discussion on 6G Paging	OPPO	discussion	Rel-20	FS_6G_Radio
Observation 6	In NR, both PEI and LP‑WUS are supported using similar procedures and mechanisms for the same purpose, i.e., reducing false paging alarms. A UE may support either feature or both.
Proposal 5	For UE energy efficiency of 6G Paging, RAN2 assume a single DL wake-up scheme is to be adopted, and focus on the corresponding procedure design, e.g., Subgrouping. The detailed signal design is up to RAN1.
Noted
R2-2601009	Discussion on 6G Paging	Qualcomm Incorporated	discussion
Observation 3	In NR, separate procedures and parameters for PEI and LP-WUS make the specification complex in both AS and NAS layer, also bring additional implementation complexity to the UE and the network.
Proposal 2	RAN2 should strive to achieve a common upper layer procedure and common set of parameters if both PEI and LP-WUS paging monitoring are supported.
Noted
Agreements on paging
For single CN triggered paging, RAN2 assumes a single paging ID can be used and so far there has been no motivation to differentiate the state in the paging message.
For resume, FFS on UE ID, it may be different than the paging ID.
Paging design supports both clustered PF/PO design and distributed evenly PF/PO design.
RAN2 assume a single DL wake-up scheme is to be adopted.  Wait for some RAN1 progress.
Not treated
R2-2600082	Consideration on 6GR Paging	vivo	discussion	Rel-20
R2-2600123	Discussion on paging in 6GR	Xiaomi	discussion	Rel-20	FS_6G_Radio
R2-2600161	Discussion on paging in 6G	Ericsson	discussion	Withdrawn
R2-2600193	Discussion on Paging Mechanism	CATT	discussion	Rel-20	FS_6G_Radio
R2-2600235	Discussion on paging design	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
R2-2600506	Discussion on paging for 6GR	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2600558	Discussion on paging	NEC	discussion	Rel-20	FS_6G_Radio
R2-2600564	Discussion on paging for 6GR	TCL	discussion
R2-2600580	Discussion on 6G paging	ASUSTeK	discussion	Rel-20
R2-2600670	Discussion on paging of 6GR	Spreadtrum, UNISOC	discussion	Rel-20
R2-2600692	Views on 6G Paging	NTT DOCOMO, INC.	discussion
R2-2600694	Paging in 6G	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
R2-2600714	Paging in 6G	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
R2-2600774	Discussion on single paging mechanism	Panasonic	discussion
R2-2600791	Paging considerations for 6G	Lenovo	discussion	FS_6G_Radio
R2-2600810	Paging and Initial access on different bands	Vodafone Telekomünikasyon A.S.	discussion	Rel-20
R2-2600833	Views on Paging in 6G	Fujitsu	discussion	Rel-20
R2-2600861	Paging mechanism in 6G	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2600919	Discussion on 6GR paging	ETRI	discussion	Rel-20
R2-2600929	Consideration of paging framework for 6GR 	Kyocera 	discussion	Rel-20
R2-2601111	Discussion on paging for 6G	Ericsson	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-p014`

