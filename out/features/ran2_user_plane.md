# 6GR 用户面架构

**当前进展** · 阶段：收敛中

RAN2 已确认 6GR 用户面需支持一组核心传输、排序、安全、压缩、丢弃、复用及重传功能，并提出 Day‑1 支持要求；部分方向已有明确结论，例如 PDCP 与 RLC 重传保持分离、UDC 是 Day‑1 必要特性。协议栈架构、单一序列号及其与 CU-DU split、Dual Connectivity 等部署场景的适配仍在研究。针对高层与低层 HOL blocking、重排序、丢弃、HARQ 辅助快速 ARQ 及早期转发的机制和适用范围尚未完全确定，部分事项还依赖 RAN1。随机接入、QoS 映射、AI 流量支持和压缩框架也仍有待进一步研究或跨工作组协调。

**未决问题**

- 单一 SN、PDCP/RLC 分层或合并，以及不同部署架构下的控制 PDU、SN gap 和状态报告处理。
- QoE 感知的重排序与丢弃，以及同一 DRB 内多种 QoS flow 的 HOL blocking 缓解方案。
- HARQ 辅助快速 ARQ、HARQ 状态反馈、MAC control PDU 处理及成功解码 CB/CBG 交付，部分依赖 RAN1 设计。
- 统一且高效的 RACH 框架、资源自适应、early indication 和更大 Msg3/MsgA 的支持方式。
- AI 流量特征与模型、TokenCom 特性及相应 QoS/L2 机制，需结合 SA4 等工作组反馈推进。
- UDC、ROHC、EHC、SCHC 等机制如何构成并集成到 6G 压缩框架。

## 6GR 演进

### [6G/Rel-20 RAN2#134] `agreement` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

分别设置 PDCP 和 RLC 时，PDCP 至少承担安全、按序交付、头压缩、重复检测和重传，RLC 至少承担分段与重组、重复检测和 ARQ；合并层至少承担前述 PDCP 功能，分段与重组方式仍待研究。RAN2 旨在针对 RAN plenary 确定的所有支持场景和架构采用共同协议栈，部署选项不应影响协议栈；Single SN 的开销、处理、分离承载 DC、控制 PDU 分段及 CU-DU split 相关事项仍有待研究或决定。

```text
1	For a separate PDCP and RLC layer architecture, at least the following 5G PDCP and RLC SN-based functionality are considered:
PDCP performs security, in-order delivery, header compression, duplicate detection, retransmission.
RLC performs (re)segmentation, reassembly, duplicate detection and ARQ.
2	For a merged layer architecture, the PDCP-RLC merged layer performs at least: security, in-order delivery, header compression, duplicate detection, retransmission
FFS how to handle (re)-segmentation and reassembly.  One option is it can handled by MAC, but that increases complexity in terms of window management and SN numbering for MAC.
FFS on NW side whether ARQ can run on the network interface (e.g. Xa) that is subject to congestion.
3	RAN2 aims to address all supported scenarios/architectures, as determined by RAN plenary with a common protocol stack (for PDCP/RLC), i.e., deployment options should not impact protocol stack
4	As observations to the study, the impact of Single SN on overhead and processing is as follows:
Header reduction by up to ~2 bytes in the combined L2 header (for the first segment of the PDU).
Depending on layering and header design, packet processing may also be simplified if we have a merged window operation.
For separate PDCP and RLC, some increased inter-layer interaction is expected.
FFS Segmentation details, e.g., how segmentation entity tracks PDCP SN and how single SN is carried across the two headers.
5    RAN2 to note that single SN requires additional complexity to support 6G-6G split bearer DC (if agreed by plenary).
Note: DC split bearer as defined in 5G, i.e., PDCP anchor and 1 RLC leg per Cell group.
For separate layer with single SN
6	Segmentation and ARQ are supported for PDCP Control PDU (at least for separate layer and if needed). RAN2 to discuss how an SN can be assigned to PDCP control PDU for that purpose and the possible HOL blocking risk
7	New RLC window initialization procedure is needed to align with the continuing PDCP SN with RLC re-establishment
8	Pending RAN3/plenary decisions on HLS, From RAN2 point of view, it is noted that:
Single SN with separate layers is possible with CU-DU split (assuming no split bearer)
At least the following functions should reside in the DU: segmentation, (re)segmentation, reassembly
F1 impacts depending on SN field placement and interactions required between CU and DU can be further studied by RAN3.
9	RAN2 to study how RLC SN gaps are handled, e.g., due to PDCP discard, for separate window case.
Header compression
R2-2603206	Uplink Data Compression in 6G Day-1	CATT, China Mobile, Ericsson, Huawei, HiSilicon, Turkcell	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-a001`

### [6G/Rel-20 RAN2#134] `agreement` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

记录 5G PDCP 重排序机制在 DL 峰值吞吐时导致接收端内存需求高、延迟，并缺乏适应 QoE 的能力这一不足。研究简单的重排序机制以解决该问题。

```text
1	Capture the following shortcoming: 5G PDCP reordering mechanism causes high Rx memory requirements at DL peak throughput, latency and lacks ability to adapt to QoE.
2	Study simple reordering mechanisms to address this shortcoming.
[AT134][006][6G UP] L2 retransmission (Mediatek)
Intended outcome: Discuss:
-  L2 retransmission
-  window management for single SN and separate layer.
Deadline:  Thursday
R2-2604393	Report of [AT134][006][6G UP] L2 retransmission	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-a002`

### [6G/Rel-20 RAN2#134] `agreement` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

与 NR 相同，重传有两种触发：RLC retransmission 用于处理 Uu 数据丢失，PDCP reestablishment/recovery；SDU 和 SDU-segment 都需要支持重传。共同的 L2 retransmission function 仅在采用 single SN 时可行，具体方案及 CU-DU split 下的窗口操作、不同终止点时的共同状态报告仍待讨论。

```text
1	As in NR, there are two triggers for retransmission:
•	RLC retransmission to deal with data losses over the Uu
•	PDCP reestablishment, recovery
2	As in NR, retransmissions of both SDUs and SDU-segments are necessary.
3	A common L2 retransmission function is only possible with a single SN.  FFS details
For the next meeting, companies are encouraged to provide input on the following aspects:
•	Address the identified set of benefits and drawbacks of each approach to handle the two retransmission triggers
•	Single window operation when considering a CU-DU split (depending the RAN plenary decision on CU-DU split)
•	Common status reporting in case of different termination points for the two retransmission triggers
Common L2 Retransmissions & Status Reporting
R2-2603009	Discussion on upper user plane	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
Observation 1-1:	If unified retransmission is supported in the PDCP layer, there is higher latency due to PDCP operations and F1-U delay under CU-DU split; there is also resource waste because retransmission for segments could not be supported.
Observation 1-2:	If unified retransmission is supported in the RLC layer, after handover, the SDUs have to be handled with the target node's security functions before retransmission, which involves PDCP necessarily.
Observation 2-1: In NR, PDCP status report is used for addressing the issue of un-timely RLC status report for selective retransmission in AM DRB during handover.
Observation 2-2: With single SN, after handover, the receiving RLC entity can send the RLC status report based on the PDCP receiving status, and it can be used for PDCP selective retransmission if it can be sent in-time after handover.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-a003`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

原文认为 UDC 是具成本效益且成熟的特性，符合 6G 核心需求，包括 IMS service（含 TN/NTN）支持、UE 节能和上行覆盖增强。UDC 是 6G Day‑1 部署的必要特性。

```text
UDC is a cost-effective and mature feature that aligns with 6G’s core requirements: IMS service support including TN/NTN, UE power saving, and uplink coverage enhancement. UDC constitutes a necessary feature for 6G Day‑1 deployment.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-o001`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

NR 的 PDCP reordering framework 可能导致接收端 PDU 的重排序延迟不确定，延迟范围可在一个至两个 reordering timer 周期之间变化。

```text
NR’s PDCP reordering framework can lead to non-deterministic reordering delays for PDUs in the receiver, which can vary between one and two reordering timer periods.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-o002`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

5G PDCP reordering 机制在 DL 峰值吞吐量下会导致较高的 Rx 内存需求，且无法适应 QoE。

```text
5G PDCP reordering mechanism causes high Rx memory requirements at DL peak throughput and lacks ability to adapt to QoE.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-o003`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

原文指出，切换期间若将 L2 retransmission 集成到 RLC，需要 DU 与 CU-UP 之间复杂且紧密的交互，并预计会出现许多问题；若全部集成到 PDCP，则可能没有问题。

```text
During handover, if L2 retransmission is integrated into RLC, complex and tight interactions between DU and CU-UP should be required and many issues are expected, but there may be no issue if all L2 retransmission are integrated into the PDCP.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-o004`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

原文认为，带有 HARQ failure indication 的 Fast ARQ 不能证明将 L2 retransmission 集成到 RLC 是合理的。

```text
Fast ARQ with a HARQ failure indication cannot justify L2 retransmission integrated into RLC.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-o005`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

PDCP retransmissions 与 RLC ARQ 的触发条件和目的不同。

```text
PDCP retransmissions and RLC ARQ have different triggers and purposes.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-o006`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

若 6GR 中 PDCP layer 与 RLC layer 合并为单一层，则自然支持一份 status report。

```text
If the PDCP layer and the RLC layer are merged into a single layer in 6GR, one status report would be naturally supported.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-o007`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

若 6GR 中 PDCP layer 与 RLC layer 保持分离，可进一步研究是否以及如何统一两份 status reports。

```text
If the PDCP layer and the RLC layer remain separate layers in 6GR, whether and how to unify the two status reports can be further studied.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-o008`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

原文指出，NR 基于 timer 或 feedback 的 data discarding 可能不足以满足 6G 多样化服务需求，并提出考虑 per-QoS flow discarding、基于 QoE 的 discarding、queue/congestion-based discarding，以及由 RAN 控制、UE 修改或选择配置参数的适配机制。另列出既有拥塞管理机制及观点：R19 UL rate control 可及时直接地支持应用层调节速率；L4S 和 SA2 congestion information exposure 存在应用对拥塞指示理解不同的问题。

```text
The data discarding functionality in NR, based on either timer or feedback, can be insufficient for 6G’s diverse service requirements, as it lacks per-QoS-flow granularity handling, adaptability to application-layer conditions (e.g., DASH buffering), support for AL-FEC redundancy removal, and responsiveness to dynamic buffer and queue states.
Proposal 3a: For the data discarding functionality in 6G, RAN2 could consider the following:
1)	Data/SDU discarding is performed at per-QoS flow granularity when QoS flows are N:1 mapped to DRB.
2)	Support discarding based on QoE, e.g., discarding can be relaxed when QoE downgrades.
3)	Queue/congestion-based discarding: immediate data discarding when congestion occurs or the AS layer queue becomes too long.
Proposal 3b: For the data discarding configuration in 6G, a RAN-assisted discarding configuration adaption mechanism can be supported, where UE can modify/select discarding configuration/parameter(s) under RAN control.
R2-2603009	Discussion on upper user plane	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
Observation 3-1:	Congestion management mechanism in legacy includes bit rate recommendation in R15, L4S in R18, congestion information/available bitrate exposure in R19 and UL rate control in R19.
Observation 3-2:	R19 UL rate control is timely and direct to allow the application layer quickly adjust the data rate according to NW conditions from AS point of view.
Observation 3-3:	L4S is untimely and inaccurate compared with rate control/exposure solutions. Different applications may have different understandings on the indicated rate marked by RAN/UPF. While from deployment point of view, L4S is easier than the other solutions.
Observation 3-4:	The SA2’s solution of congestion information exposure suffers from the same issue as L4S that different applications may have different understandings on congestion level.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-o009`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

原文指出，当前 UE 和 NW 已支持 L3 Congestion management 的 ECN marking。

```text
L3 Congestion management ECN marking is supported in UEs and NWs today.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-o010`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

原文指出，Congestion management 是 per-flow 操作；由于中间路由器与流的源/目的端之间没有其他控制信令，它在 IP layer 的 header 中实现，并指出 RAN 的情况不同。

```text
Congestion management is a per-flow operation. It is implemented at the header in IP layer since there is no other control signaling available between intermediate routers and source/destination of the flow. This is not the case for RAN.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-o011`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

原文指出，legacy AM 和 UM 面向差异明显的服务，且在 window operation、PDU header format 等方面完全不同。目前尚未识别出统一 RLC transmission mode 的明确收益和动机。

```text
Legacy AM and UM are designed for services with noticeable differences and with complete differences in aspects like window operation and PDU header format. No clear benefits and motivation of a unified RLC transmission mode have been identified yet.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-o012`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

提出将 UDC 作为 6G compression framework 的一部分进行研究，并研究其在 6G protocol stack 中的支持方式，要求涵盖 IMS services（包括 TN/NTN）、改善 UE power saving 和增强 uplink coverage。原文还指出 SCHC 可作为 6G PDCP layer 中 ROHC 的补充，适用于 ROHC 不适合的特定 IoT traffic patterns。

```text
Study UDC for 6G as part of a compression framework and how it can be supported in the 6G protocol stack considering the following requirements:
Support for IMS services including TN/NTN.
Improvement of UE power saving.
Enhancement of uplink coverage.
R2-2603741	Static Context Header Compression (SCHC) for IoT traffic in 6G	Orange, Ericsson, Nokia, T-Mobile USA, Turkcell, Deutsche Telekom, Huawei	discussion	Rel-20	FS_6G_Radio	R2-2602288
Observation 2	For typical IoT traffic patterns, header compression can substantially improve device energy consumption, latency, reliability and spectrum efficiency
Observation 4	SCHC with its characteristics is a strong candidate for integration into the 6G PDCP layer as a complement to ROHC.
Observation 5	SCHC’s ability to address different message types and protocols that are sent using specific traffic patterns for which ROHC is ill-suited, using a single static context, and to compress multiple protocol layers at once (e.g. IP/UDP/CoAP), makes it well suited to the mid-tier IoT
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-p001`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

RAN2 将 SCHC 作为 PDCP compression mechanism 候选，并研究在 6G Study 中支持 SCHC 对 RAN2 的影响；相关提案认为 SCHC、ROHC、UDC 和 EHC 互为补充，建议纳入 6G SI 研究。讨论记录了对 UDC 处理开销、加密数据支持、SCHC 与 ROHC 关系等问题的意见，并记载下次会议聚焦 UDC、ROHC 相对 5G 的不足。

```text
RAN2 to consider SCHC as a candidate for a PDCP compression mechanism and study RAN2 impact of supporting SCHC in the 6G Study
Noted
R2-2603744	Header Compression Functionality in 6G	Orange, Ericsson, Nokia, T-Mobile USA, Turkcell, Deutsche Telekom, Huawei	discussion	Rel-20	FS_6G_Radio	R2-2602289
Observation 1	In NR, multiple compression mechanisms co-exist, i.e., ROHC, UDC, EHC, yet not all use case scenarios are covered, in particular mMTC uses, which are expected in 6G.
Proposal 1	Regarding the PDCP compression framework, RAN2 considers the SCHC, ROHC, UDC and EHC mechanisms as complementary and proposes to include them in 6G SI.
Study SCHC, ROHC, UDC and EHC???
-	ZTE asks whether SCHC should be done in SA2 like we did for NTN.
-	Mediatek thinks that we should be careful with UDC as it is processing intensive.  Qualcomm agrees and UDC doesn’t work for encrypted data.  SIP compression too should be looked at.
-	LG thinks that ROHC, UDC and EHC are already there, so we should focus on SCHC.
-	Qualcomm thinks that SCHC competes with ROHC so ROHC may give use what we need.
Noted
For next meeting, focus should on short comings from 5G for UDC, ROHC
Reordering
R2-2603754	Reordering behaviour at the receiver	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-p002`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

RAN2 研究如何消除同一 PDU 多个 reordering timer 实例造成的过度 reordering delay。记录的讨论涉及 TCP、RTP、当前配置下是否存在问题，以及识别可乱序交付数据包的方式。

```text
RAN2 to study how to eliminate excessive reordering delays caused by multiple instances of the reordering timer running for the same PDU.
-	Qualcomm thinks that the end to end would depend on the flavor of TCP.   Mediatek is thinking more about RTP traffic.
-	LG hasn’t seen any problem with current configuration so why do we have a problem with the maximum 2 Treordering
-	ZTE asks who is identifying the packets that you can deliver out of order.
Noted
Moved from 9.3.1.2
R2-2603474	Discussion on Dynamic QoS and HOL	CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-p003`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

RAN2 考虑增强 reordering，包括结合 in-order delivery 与 out-of-order delivery，以及增强 PDCP reordering procedure。

```text
RAN2 to consider the following enhancements for reordering:
Combining in-order delivery and out-of-order delivery;
Enhancing PDCP reordering procedure.
Noted
R2-2602938	Discussion on functionalities for upper user plane	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-p004`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

RAN2 将研究增强 6G 中的 PDCP reordering，以适配 application QoE、降低高 DL throughput 下的内存使用，并支持同一 DRB 中具有不同 reordering requirements 的多个 flows（如可行）。讨论涉及 HOL、FARQ、DL 扩展、乱序交付及高接收内存问题，尚未给出解决方案。

```text
RAN2 to study how to enhance PDCP reordering in 6G to achieve the following goals, if possible:
Adapt to application QoE needs
Reduce memory usage at high DL throughput
Support multiple flows in a DRB with different reordering requirements
Noted
Discussion
-	Samsung thinks that we are in a good path to solve the problem with HOL, FARQ, etc.  Qualcomm thinks FARQ is for UL and we want to extend for DL.
-	Apple thinks that there are many protocols that can handle out-of-order delivery.
-	Huawei is not sure what can be done for the high Rx memory as it is implementation.  So what is the solution.  Qualcomm thinks that sometimes we can just forward the window.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-p005`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

决定不支持 unified L2 retransmission。PDCP 与 RLC retransmissions 保持分离。

```text
Do not support unified L2 retransmission: Keep PDCP and RLC retransmissions separate.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-p006`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

AM DRB 仅支持用于 PDCP 和 RLC retransmission 的 RLC status report。

```text
Support only RLC status report for PDCP and RLC retransmission for AM DRB.
R2-2603345	Discussion on functionality for Upper User Plane and related functional requirements	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-p007`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

提出将所有 L2 retransmission mechanisms 集成到 PDCP，以实现 common L2 retransmission functionality。

```text
All L2 retransmission mechanisms are integrated into PDCP for common L2 retransmission functionality.
R2-2603550	Discussion on common L2 retransmissions	Philips International B.V.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-p008`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

6GR 中，PDCP retransmissions 与 RLC ARQ 是分离的 procedures。

```text
PDCP retransmissions and RLC ARQ are separate procedures in 6GR.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-p009`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

6GR 支持 unified L2 status report。

```text
A unified L2 status report is supported in 6GR.
Congestion Management & Packet Discarding
R2-2603854	Consideration on 6GR UP Functioanlities	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-p010`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

建议将 R19 引入的 UL rate control mechanism 作为 AS 侧 congestion control 的基线，并研究 6G DL rate control。还建议询问 SA2 是否支持 6G 中的 L4S。

```text
Support UL rate control mechanism introduced in R19 as the baseline for congestion control mechanism from AS point of view and study DL rate control in 6G. Ask SA2 whether L4S could be supported in 6G.
R2-2602938	Discussion on functionalities for upper user plane	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-p011`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

RAN2 聚焦于不引入 per-packet overhead 的 congestion management 方案，并可进一步研究用于指示 flow congestion 的 control signaling 及其性能收益。另有提案研究 6G RLC 的 AM 和 UM common framework，可在配置时基于 FARQ 或 polled RLC status reporting 触发 retransmissions。

```text
For congestion management, RAN2 focuses on solutions that do not introduce per-packet overhead. Control signaling to indicate flow congestion can be further studied to assess performance benefits.
Data transfer modes
R2-2603232	6G upper user plane functionalities	Ericsson	discussion	Rel-20	FS_6G_Radio
Proposal 5	Study common framework in 6G RLC for AM and UM operation, where retransmissions may be triggered based on FARQ or polled RLC status reporting, if configured.
R2-2602946	Considerations on User Plane functionalities	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-p012`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

Legacy AM 和 UM 可作为 6G data transfer modes 的基线。可按具体情况研究对 AM 或 UM 的进一步增强。

```text
Legacy AM and UM can be as baseline of 6G data transfer modes. Further enhancements to AM or UM can be studied case by case.
R2-2603586	Upper UP functionalities and requirements	Nokia	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-p013`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

RAN2 研究一种 single non-transparent RLC mode，以支持不同的 retransmission 和 feedback behaviour。

```text
RAN2 studies one single non-transparent RLC mode that can support different retransmission and feedback behaviour
R2-2602998	Discussion on UP functionality and requirement	NEC Corporation	discussion	Rel-20	FS_6G_Radio
R2-2603020	Atomic transfer mode for RLC	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
R2-2603025	Discussion on packet discard functionality	Google	discussion	Rel-21	FS_6G_Radio
R2-2603035	Discussion on upper user plane functionalities	Xiaomi	discussion	Rel-20
R2-2603049	Functionality for upper user plane	ZTE Corporation, Sanechips	discussion
R2-2603109	Functionalities and architecture impacts of the merged PDCP and RLC	OPPO	discussion	Rel-20	FS_6G_Radio
R2-2603158	Upper User Plane Functionalities	Sharp	discussion	Rel-20	FS_6G_Radio
R2-2603261	Views on 6G User Plane: L2 Functionalities	Apple	discussion	Rel-20	FS_6G_Radio
R2-2603303	6G User Plane functionalities	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2603416	Upper L2 functionality	InterDigital, Inc.	discussion	Rel-20	FS_6G_Radio
R2-2603473	Discussion on UP Functionalities	CATT	discussion	Rel-20	FS_6G_Radio
R2-2603602	Further discussion of User Plane functionalities	Lenovo	discussion	Rel-20	FS_6G_Radio
R2-2603618	Discussion on congestion control aspects and UP functionality	Sony	discussion	Rel-20	FS_6G_Radio
R2-2603643	Functionality and architecture of UP for 6G	Panasonic	discussion	Rel-20
R2-2603683	6G UP function design	China Telecom	discussion	Rel-20
R2-2603787	Further discussion on segmentation and related requirements	Futurewei	discussion	Rel-20	FS_6G_Radio
R2-2603885	Discussion on UP functionalities in 6G	Spreadtrum, UNISOC	discussion	Rel-20
R2-2603911	Considerations on a merged layer 	Samsung 	discussion	FS_6G_Radio
R2-2603912	Discussion on mechanisms for congestion management	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
R2-2604013	Discussion on 6G User Plane Functionality	Transsion Holdings	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-p014`

### [6G/Rel-20 RAN2#134] `agreement` 9.3.1.4 Other UP functionality

研究中无需专门处理 RLC/PDCP control PDUs 的 HOL blocking；应从 RX 和 TX 两个角度研究其他 HOL blocking 问题。若为 upper layer data 设计解决方案，可将其应用于 PDCP/RLC control PDUs，并需考虑 QoS framework，由 RAN2 评估是否还需其他措施。

```text
No need to address HOL blocking for RLC/PDCP control PDUs specifically in study.
Study other HOL blocking issues from both RX and TX perspective.   Understanding is if we design a solution for upper layer data, we may apply it to PDCP/RLC control PDUs.   QoS framework would need to be taken into account and RAN2 can evaluate if anything additional is needed
R2-2602987	Discussion on fast ARQ	NEC	discussion	Rel-21	FS_6G_Radio
R2-2603022	Addressing Lower-layer HOL blocking issue	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
R2-2603113	Discussion on faster HARQ assisted ARQ and head-of-line blocking	OPPO	discussion	Rel-20	FS_6G_Radio
R2-2603116	Other UP functionality in 6G	Samsung	discussion	Rel-20	FS_6G_Radio
R2-2603156	Discussion on Fast ARQ and HOL Blocking	Sharp	discussion	Rel-20	FS_6G_Radio
R2-2603162	Discussion on HOL blocking 	Pengcheng Laboratory	discussion
R2-2603176	Discussion on L2 retransmission enhancements and HOL blocking issue	1Finity	discussion	Rel-20	FS_6G_Radio
R2-2603265	Views on 6G User Plane: Fast ARQ and HoL Blocking	Apple	discussion	Rel-20	FS_6G_Radio
R2-2603307	6G Faster ARQ and HOL blocking	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2603381	Discussion on Faster HARQ assisted ARQ for 6GR	TCL	discussion	Rel-20	FS_6G_Radio
Fast ARQ and HOL blocking	InterDigital, Inc.	discussion	Rel-20	FS_6G_Radio
R2-2603448	Discussion on FARQ and HOL blocking 	ETRI	discussion	Rel-20
R2-2603456	6G fast ARQ and HOL blocking avoidance	Ericsson	discussion
R2-2603600	Discussion on HARQ/ARQ protocol operation and HOL blocking	Lenovo	discussion	Rel-20	FS_6G_Radio
R2-2603621	Lower layer HOL blocking and Fast ARQ data recovery	Sony	discussion	Rel-20	FS_6G_Radio
R2-2603706	Discussion on FARQ and HoL issues for 6G	Panasonic	discussion	Rel-20
R2-2603790	Further discussion on other user plane functions	Futurewei	discussion	Rel-20	FS_6G_Radio
R2-2603847	Disscussion on faster ARQ retransmission and HOL blocking	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
R2-2603887	Discussion on L2 (re-)transmission and HOL in 6G	Spreadtrum, UNISOC	discussion	Rel-20
R2-2603947	Discussion on fast ARQ for 6G	DENSO CORPORATION	discussion	Rel-20
R2-2603978	Discussion on Other UP functionality	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2604079	HoL blocking, retransmission and other cross-layer aspects	CEWiT	discussion	Rel-20	FS_6G_Radio
R2-2604159	Views on UP others	NTT DOCOMO INC..	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-a001`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.4 Other UP functionality

在 5G NR 机制中，单个 CB 或 CBG 不被视为可靠；未经 TB CRC verification 成功，不能独立交付给 MAC layer。

```text
In the 5G NR mechanism, a single CB or CBG is not considered reliable and cannot be delivered to the MAC layer independently without successful TB CRC verification.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-o001`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.4 Other UP functionality

允许通过 CB-level CRC verification 的 CB/CBG 交付给 MAC，可部分解决 PHY layer HOL blocking；位于错误 CB/CBG 之前的 CB/CBG 将不再被阻塞。

```text
The PHY layer HOL blocking issue could be partially solved by enabling delivery of CBs/CBGs passing CB-level CRC verification to MAC, i.e., CBs/CBGs before an error CB/CBG will not be blocked.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-o002`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.4 Other UP functionality

从 RAN2 角度，要完全解决 PHY layer HOL blocking，MAC 需要识别每个交付的 CB/CBG 中 MAC subPDUs 的边界。

```text
From RAN2’s perspective, a solution to completely solve the PHY layer HOL blocking issue requires MAC to recognize the boundary of MAC subPDUs within each delivered CB/CBG.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-o003`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.4 Other UP functionality

TB-level CRC verification 是否可以移除或忽略，以及 CBG 是否会在 6G 中保留，需要与 RAN1 确认。

```text
Whether TB-level CRC verification can be removed/ignored and whether CBG will be retained in 6G should be checked with RAN1.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-o004`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.4 Other UP functionality

当前 5G NR 准备和转发 MAC subPDUs 的方式不支持提前转发 control 或 data subPDUs。在相关 CB 已正确解码的 HARQ 重传场景中，这会导致显著时延。

```text
The current 5G NR approach for preparing and forwarding MAC subPDUs does not allow for early forwarding of control or data subPDUs. This results in significant latency in HARQ retransmission scenarios, when the relevant CB has already been decoded correctly.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-o005`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.4 Other UP functionality

提前转发 MAC CEs 和/或其他 control messages 与 PDCP HOL blocking issue 无关。

```text
Early forwarding of MAC CEs and/or other control messages is not related to the PDCP HOL blocking issue.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-o006`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.4 Other UP functionality

ARQ 仅对 AM mode PDUs 有益，因此 FARQ 应仅应用于 AM mode PDUs。

```text
ARQ is only beneficial for AM mode PDUs. So, FARQ should be applied only for AM mode PDUs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-o007`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.4 Other UP functionality

FARQ 可能使 TB 中包含的部分 MAC CEs 受益，但并非所有 MAC CEs 都需要此机制。部分 MAC CE 内容在重传前可能需要重构。

```text
FARQ may benefit some of the MAC CEs which are included in the TB, however, not all MAC CEs need this and some MAC CE content may need to be reconstructed before retransmission.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-o008`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.4 Other UP functionality

Type 3（RLC Tx 侧 PDCP data PDU 阻塞 PDCP control PDU 的 Intra-DRB HOL blocking）在 5G 中并非问题，因为 UE 实现始终可以优先发送 PDCP control PDU。6G 中是否存在该问题，可根据 single SN 讨论进一步确认。

```text
Type 3 (Intra-DRB HOL blocking of PDCP control PDU by PDCP data PDU at RLC Tx side) has not been an issue in 5G, as UE implementation can always prioritize transmission of PDCP control PDU. Whether it is an issue in 6G can be further confirmed based on single SN discussions.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-o009`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.4 Other UP functionality

大多数 Type 4（RLC Tx 侧 PDCP data PDU 阻塞 PDCP control PDU 的 Inter-DRB HOL blocking）可通过适当的 NW configuration 处理。需要 RAN2 关注的特殊情况是 MAC LCP procedure 中 Bj<0，导致 PDCP/RLC control information 无法发送。

```text
Most Type 4 (Inter-DRB HOL blocking of PDCP control PDU by PDCP data PDU at RLC Tx side) can be handled by proper NW configuration. The special case that needs RAN2 attention is when Bj<0 in the MAC LCP procedure, gating PDCP/RLC control information from being transmitted.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-o010`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.4 Other UP functionality

Type 4 HOL blocking issue 可能无需解决，因为高优先级 LCH 的 L2 control/data PDU 应始终优先于低优先级 LCH 的 L2 data/control PDU。

```text
Type 4 HOL blocking issue may not need to be resolved as L2 control/data PDU of high priority LCH should always have higher priority than L2 data/control PDU of low priority LCH.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-o011`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.4 Other UP functionality

已记录向 RAN1 发送 LS，询问是否有必要且可行：无论 TB CRC verification 结果如何，将成功解码的 CB 或 CBG 交付给 MAC layer。

```text
Send LS to RAN1 to inquire about the necessity and feasibility of delivering successfully decoded CBs or CBGs to the MAC layer regardless of the result of TB CRC verification.
Noted
R2-2602950	Considerations on faster ARQ retransmission and HOL blocking issues	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-p001`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.4 Other UP functionality

已记录向 RAN1 发送 LS 以澄清 lower layer HOL blocking issue，并询问能否将通过 CB-level CRC verification 的已成功解码 CB/CBG 交付给 MAC layer。

```text
Send an LS to RAN1 to clarify the lower layer HOL blocking issue. Ask RAN1 if it is possible to deliver the successfully decoded CB/CBG (passing CB-level CRC verification) to MAC layer.
Noted
R2-2603463	Other UP functionalities	Nokia	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-p002`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.4 Other UP functionality

需研究提前转发对 MAC CEs、Other control messages 和 User Data 等不同 payload types 的收益。还需研究此类转发应对所有 TB 始终启用（“always on”），还是仅在认为有益时对部分 TB 启用（“opportunistic”）。

```text
Study the benefits of early forwarding for various payload types: MAC CEs, Other control messages, User Data; and if such forwarding shall be “always on” (for all TBs) or “opportunistic” (for some TBs when deemed beneficial)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-p003`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.4 Other UP functionality

讨论了基于 MAC PDU preparation 的 early forwarding，要求不影响 TB-to-CB splitting 或其他 RAN1 定义的 PHY mechanisms；其收益、适用场景、可解析且可信的数据单位及方案仍需研究。还记录了 UL HARQ process status 对 RLC UM 的潜在益处，包括避免不必要的资源浪费，以及尽早发送 MAC CE 和 RLC control PDU。

```text
Study earlyforwarding solutions based on MAC PDU preparation that do not impact TBtoCB splitting or other RAN1defined PHY mechanisms.
Noted
Discussion
-	Qualcomm thinks that we still don’t know how the TB looks like whether we have CB and CBG.  Whether decoded CB, CBG can already be sent, it’s network implementation.
-	Lenovo thinks that RAN1 is better equipped to have such discussions.  Qualcomm thinks that is is a MAC issue and it is transparent to RAN1.  Lenovo thinks that there are two ways to do this, one in MAC and modifying the LCP etc, or in RAN1.
-	Fraunhoufer thinks that there are two new things, very large TB size,
-	Huawei thinks that RAN1 would need to tell us the CB size.
-	Docomo thinks we should discuss benefit before solution.
-	Ericsson thinks that we should first understand the problem
-	Apple thinks that we can ask RAN1 to see the benefit of early data delivery for large TB
-	Mediatek thinks that we should just ask what is the unit of data that can be parsed and trusted.
-	Qualcomm thinks that we can decouple our solution with PHY design, like a mini TB can be constructed.
-	Huawei thinks that we can just ask whether it is possible to deliver a CB that has passed CRC check before the TB CRC check has passed.   Samsung agrees that this is a main question.
-	Nokia thinks that we need to analyze the scenario, for all TBs or some TBs.
-	LG reminds that the CB is not the only solution, we can other upper layer solution if we map a specific LCH to a separate MAC PDU.   Also the TB structure is not decided.
Contributions on HOL blocking should take into account RAN1 progress, understand the benefits, understand all solutions on HOL blocking in L2, etc.
FARQ re-transmission content
R2-2603013	Discussion on HARQ status indication and HOL blockage	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
Observation 1-1:	UL HARQ process status also provides benefits in RLC UM scenario, for example, if UE can discard the other RLC SDU segments of the RLC SDU in the corresponding MAC PDU based on UL HARQ process status of NACK, unnecessary resource waste can be avoided.
Observation 2-1:	If UE can directly re-trigger MAC CE and RLC control PDU in the corresponding MAC PDU based on UL HARQ process status of NACK, MAC CE and RLC control PDU can be sent as soon as possible, which is beneficial to communication.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-p004`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.4 Other UP functionality

提出 HARQ status indication 可应用于 RLC UM。

```text
HARQ status indication could be applied for RLC UM.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-p005`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.4 Other UP functionality

提出收到 UL HARQ process status 的 NACK 时，若对应 MAC PDU 包含 MAC CE 和 RLC control PDU，则 MAC entity 重新触发 MAC CE，RLC entity 重新触发 RLC control PDU。

```text
When UL HARQ process status of NACK is received, MAC entity re-triggers MAC CE and RLC entity re-triggers RLC control PDU if included in the corresponding MAC PDU.
R2-2603052	Fast ARQ and other 6G UP enhancements	ZTE Corporation, Sanechips	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-p006`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.4 Other UP functionality

提出 fast ARQ 仅适用于 MAC PDU 中 AM mode 的 MAC SDUs；TB 中 MAC CEs 的处理仍待研究，并留给 stage 3。

```text
For the MAC SDUs in a MAC PDU, fast ARQ is applicable only to AM mode SDUs – handling of MAC CEs in the TB is FFS (left to stage 3).
R2-2603753	Transmitter behaviour on fast ARQ trigger	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-p007`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.4 Other UP functionality

提出收到 FARQ NACK indication 后，来自配置了其他约束（例如 delay budgets）的 AM-like bearers 的 uplink HARQ buffer 数据，只有在满足这些约束时才考虑重传。

```text
Upon FARQ NACK indication, data in the uplink HARQ buffer from AM-like bearers configured with other constraints (e.g. delay budgets) are only considered for retransmission if those constraints are met.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-p008`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.4 Other UP functionality

提出 FARQ 重传候选数据不适用特定优先级规则，LCP 定义的规则除外。

```text
Data considered for FARQ retransmission is not subject to any specific prioritisation except those defined for LCP.
[15 min]
Higher layer HOL
R2-2602942	Discussion on other UP functionalities	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-p009`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.4 Other UP functionality

RAN2 观察到，Type 3 Intra-DRB HOL Blocking 可完全由 UE implementation 处理，且 5G 中没有该类型在现场造成问题的实例。RAN2 将研究 Type 4 Inter-DRB HOL Blocking：当 LCP 长时间导致 Bj<0 时，PDCP 和 RLC control PDUs 的阻塞可能造成该 DRB 停滞和吞吐量下降。

```text
For Tx HOL Blocking between control and data PDUs, RAN2 observes the following:
-	Type 3 Intra-DRB HOL Blocking can be fully handled by UE implementation. In 5G, there are no instances of type 3 HOL Blocking causing any issues in the field.
-	For Type 4 Inter-DRB HOL Blocking, RAN2 to study the blocking of PDCP and RLC control PDUs when the LCP causes Bj<0 for a long time, causing stalling and throughput reduction for this DRB.
Noted
R2-2603040	Discussion on FARQ and HOL blocking issue	Xiaomi	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-p010`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.4 Other UP functionality

提出降低对 higher layer 的 Type 4 HOL blocking 问题研究优先级。

```text
RAN2 to deprioritize the study of type 4 HOL blocking issue at higher layer.
Noted
R2-2603858	Consideration on 6GR HoL Blocking and Fast ARQ	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-p011`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.4 Other UP functionality

提出 RAN2 研究将控制相关信令（包括 TCP/UDP feedback 和 PDCP/RLC control PDUs）映射到专用 radio bearer 和 LCH，以缓解 HOL blocking。讨论中对 UE implementation 是否能处理相关问题、是否应遵循 LCP，以及是否需要允许加速控制数据包存在不同意见。

```text
It is proposed that RAN2 studies mapping control-related signaling, including TCP/UDP feedback and PDCP/RLC control PDUs to a dedicated radio bearer and LCH to mitigate HOL blocking issue.
Noted
-	Nokia is not sure UE implementation can handle Type 3.
-	Apple agrees and the Bj issue maybe it won’t be an issue at the end.
-	ZTE would not like to have a separate solution for every type of data, we should have a solution that can accelerate the packets and how the L2 can identify.
-	Ericsson thinks that we should keep both options open if we have means to easily perform this.
-	Nokia thinks that if you let the UE implementation on what is prioritized the problem may be solved.
-	Mediatek thikns that we should have a system solution for HOL Tx to Rx.   ZTE agrees, a simple solution is a little bit in PDCP that indicates you can accelerate and both lower layers and RX know.
-	LG thinks that we need to follow LCP so we can’t leave it to implementation.
-	Samsung thinks that some control PDUs require in order delivery.   LG doesn’t think that we can leave PDCP Control PDUs to UE implementation.  ZTE thinks that when the PDCP and RLC are in the same place then UE can do it anyways.   Qualcomm and Mediatek explain it is possible and we should just ensure that we don’t over specify.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-p012`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

观察到 separate layer design 可能存在 robustness 问题：fake PDCP PDUs 可故意更新 RLC variables，阻止 authentic packets 后续处理。

```text
A potential robustness issue for separate layer design is observed that fake PDCP PDUs may update RLC variables deliberately and block authentic packets to be processed later.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o001`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

通过合并 PDCP 和 RLC，re-ordering、window maintenance、status report 和 SDU discard 等重复功能可设计得更高效。

```text
The duplicated functions, such as re-ordering, window maintenance, status report and SDU discard, can be designed in a more efficient manner by merging PDCP and RLC.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o002`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

在 merged layer 中，security function 可识别 fake PDUs，并阻止其故意更新 ARQ state 和 SN status variables。这样 authentic packets 后续到达时仍可处理。

```text
In merged layer, fake PDUs could be idenfitied by security function and will not update ARQ state and SN status variables deliberately. Authentic packets can still be processed when received later.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o003`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

RAN2 应研究以下场景中的 single sequence numbers：无 CU-DU split 且无 Dual Connectivity；有 CU-DU split 且无 Dual Connectivity；有 CU-DU split 且可能有 Dual Connectivity，例如 RANP 讨论的 FR1/FR2 non-collocated deployments。

```text
RAN2 should study the issue of single sequence numbers for the following scenarios:
Scenario 1: Assuming no CU-DU split (or equivalent) and no Dual Connectivity.
Scenario 2: Assuming CU-DU split (or equivalent) and no Dual Connectivity.
Scenario 3: Assuming CU-DU split (or equivalent) and possible Dual Connectivity, e.g., for FR1/FR2 non-collocated deployments discussed by RANP.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o004`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

在 RLC header 中重复 common SN 是冗余的，并会增加开销和 header processing complexity。

```text
Repeating the common SN in the RLC header is redundant and increases both overhead and header processing complexity.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o005`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

现场数据表明，携带 NACK 的 RLC Status PDU 中，RLC Status PDU 截断问题较为常见。

```text
Field data shows that the issue of truncation of RLC Status PDU is common for NACK-carrying RLC status PDUs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o006`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

截至 Rel-18，DRB 的 RLC 运行于两种模式：RLC UM 在 RLC 层将时延最小化但不提供可靠性保证；RLC AM 提供 100% 可靠性，但 RLC 时延无界（PDCP discard timer 除外）。

```text
Up to Rel-18, RLC for DRBs operated in two modes: 1) RLC UM: Minimized latency with no reliability guarantees at RLC level. 2) RLC AM: Operates at a 100% reliability with unbounded RLC latency (except for PDCP discard timer).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o007`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

RLC segmentation 会在发送端和接收端造成处理瓶颈：发送端无法进行 pre-processing，接收端则会在 reassembly 时受阻。

```text
RLC segmentation creates a bottleneck of processing both at transmitter and receiver. The transmitter cannot apply pre-processing. The receiver gets blocked at reassembly.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o008`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

在高数据速率下，RLC segmentation 不增加收益，因为 TB 已可一次承载数百个 IP packets。

```text
RLC segmentation does not add any benefit at high data rates as TBs can already carry hundreds of IP packets in one piece.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o009`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

RLC segmentation 仅适用于低数据速率链路。

```text
RLC segmentation is only needed for low data rate links
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o010`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

将多个 QoS flows/traffic flows 映射到单个 DRB，可能因 PDCP reordering 导致 HOL blocking。

```text
Mapping multiple QoS flows/ traffic flows to a single DRB may cause HOL blocking due to PDCP reordering.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o011`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

静态 PDCP reordering 机制不适用于具有动态 QoS 的服务特性。

```text
The static PDCP reordering mechanism is not suitable for service characteristics with dynamic QoS.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o012`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

5G PDCP reordering 机制在 DL 峰值吞吐量下会导致较高的 Rx 内存需求，且无法适应 QoE。

```text
5G PDCP reordering mechanism causes high Rx memory requirements at DL peak throughput and lacks ability to adapt to QoE.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o013`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

5G 静态 PDCP discard timer 机制存在两项问题：逐包定时器可能丢弃 application bursts，且不考虑 QoE 是否改善；单一静态 timer 无法适应路径时延变化，控制 application delay 的能力较粗略。

```text
5G static PDCP discard timer mechanism leads to the following issues:
-	Per-packet discard timer leads to discarding of application bursts without considering if this leads to improvement of degradation of QoE.
-	Single Static timer that does not adapt to path latency variations provide a very coarse tool for controlling application delay.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o014`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

应论证支持 AQM discarding mechanism 的 AS layer enhancements 相较于现有 SDU discard mechanism 的必要性。关于潜在 ECN enhancements 的讨论取决于 RAN3 对 CU-DU split 的讨论。

```text
AS layer enhancements to support AQM discarding mechanism should be justified over existing SDU discard mechanism. Discussion on potential ECN enhancements depends on RAN3 discussion on CU-DU split.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o015`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

NR 中 ROHC、UDC 和 EHC 是分别引入的多种压缩机制，但它们具有共性。

```text
In NR, multiple compression mechanisms (ROHC, UDC, EHC) were introduced independently, but those are all compression mechanisms which have commonalities.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o016`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

原文指出 UDC 是成熟且具成本效益的功能，符合包括 IMS service support、TN/NTN convergence、UE power saving 和 uplink coverage enhancement 在内的 6G 核心需求。原文认为 UDC 是 6G Day‑1 deployment 的必要功能。

```text
UDC is a cost-effective and mature feature that aligns with 6G’s core requirements, including IMS service support, TN/NTN convergence, UE power saving, and uplink coverage enhancement. UDC constitutes a necessary feature for 6G Day‑1 deployment.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o017`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

RAN2 将基于合并 PDCP 和 RLC 层进一步研究 single sequence numbering functionality；否则保留具有独立 SN 的两个子层。该项被 noted。

```text
RAN2 to further investigate a single sequence numbering functionality on the basis of merging the PDCP and RLC layers into one layer. Otherwise, two sub-layers with two separate SNs will be retained.
Noted
R2-2601463	Discussion on functionalities for upper user plane	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p001`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

对于依赖 SN 的功能，(Re)segmentation/reassembly 和 ARQ 应由 RLC 执行，以满足实时低时延要求。

```text
For SN-dependent functionalities, (Re)segmentation/reassembly and ARQ should be performed by RLC due to their real-time low-latency requirements.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p002`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

RAN2 将以 Table 1 为起点，按部署场景研究 unified Sequence number 的三种方案：PDCP 与 RLC 使用独立 SN、两层间统一 SN 但保留独立层，或合并为单层。原文列出合并层对 dual connectivity、CU-DU split、handover 和 data duplication 的影响或疑虑。

```text
RAN2 to take Table 1 as a starting point for the unified Sequence number study considering the following three options based on the deployment scenario:
Option 1: PDCP and RLC operate with separate sequence numbers, like 5G.
Option 2: Unified Sequence numbers between PDCP and RLC, but separate layers.
Option 3: Merge PDCP and RLC into a single layer.
Noted
R2-2601622	Discussion for upper user plane functionalities	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
Observation 1-1:	Merged PDCP and RLC layer would impose multiple functionality difficulties for various dual connectivity options.
Observation 1-2: Merging PDCP and RLC would complicate the CU-DU split functionality under RAN3 discussion.
Observation 1-3: Merging PDCP and RLC into one layer will impact the handover procedure.
Observation 1-4: It is unclear how to support data duplication when PDCP and RLC are merged.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p003`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

原文提出暂缓 single SN 的合并 PDCP/RLC 层研究，待 migration options 和 CU-DU split 取得进展，目前假设 PDCP 与 RLC 分层。后续继续研究 single SN 在不同架构场景下的影响、复杂度、利弊及相关功能位置。

```text
Postpone the study on merged PDCP/RLC layer for single SN after progress made for migration options and CU-DU split. For now, assume separate RLC and PDCP layer for single SN.
Noted
Discussion
-	Xiaomi thinks that we need to consider mobility and there is an advantage in the single layer.   Separate layers also have SN gap issues.
-	Samsung asks if merged layer can handle both real time and non-real time, also how will the ARQ/HARQ interaction.  LG things both and we can handle the interaction functions separately.
-	LG doesn’t think we should postpone, we can discuss the different options and vivo’s options make sense.
-	Nokia thinks that merging PDCP/RLC and single SN functionality is not linked and we can take Huawei’s proposal as baseline.
-	Panasonic thinks Qualcom’s approach of listing the options and understanding the pros and cons is a good approach.
-	1finitiy thinks that we can postpone until June.
-	Ericsson and Ofino thinks that we should study all these aspects.
-	ZTE thinks that if CU-DU split or DC is supported two layers will be needed.   Regardless of CU-DU split we may need separate layers as we may need separate header information for other functionality like segmentation, so regardless of the split a separate layer is better.
-	Mediatek thinks that the layers are not important for now, it is more about functionality and what’s important is architecture where they need to reside in this architecture.
-	Docomo thinks that it really depends on agreements from plenary, but we can agree what ZTE mentioned.
-	CMCC would like to avoid duplication of functionality on two layers and have a lean 6G protocol.
-	Verizon thinks that we should consider all the scenarios for the study of SN
-	LG thinks that for DC the issue is only if there is a split bearer.
-	Qualcomm agrees that we should study the scenarios, and not consider split before 5G.
-	Apple thinks that redundant functionality removal is not linked with layers.
-	Huawei thinks that companies need to provide feasibility of merged layer in different architecture options and if it works.
Continue study how the single SN functionality would work under different architecture scenarios (e.g. no CU-DU split, CU-DU split, split bearer DC), to understand the impacts, complexity, pros/cons, and where relevant functionalities resides etc.
[POST133bis][005][6G UP] Single SN (Qualcomm)
Intended outcome:
Analysis of impacts, complexity, pros/cons of how single SN functionality works under different architecture options, with some discussions/assumptions of where relevant functionalities would reside.
Deadline:  Tdoc submission deadline
Not treated
Single SN – Control PDU handling (If time allows)
R2-2601622	Discussion for upper user plane functionalities	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
Observation 5-1:	RAN2 should consider how to handle the PDCP control PDUs under the single SN mechanism.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p004`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

原文提出由 RAN2 处理 single SN 下的 PDCP control PDU 问题，列出三种方案：分配 PDCP SN 并触发 SN gap report、为控制 PDU 分配独立 PDCP SN，或通过 SRB 传输。

```text
RAN2 to handle the issue of PDCP control PDU under the single SN by the following:
Option 1: Assign PDCP SNs for PDCP control PDUs and trigger SN gap report to indicate discard of PDCP control PDUs;
Option 2: Assign separate PDCP SN to PDCP control PDUs;
Option 3: Transmit the control PDUs on SRB.
R2-2601723	Considerations on single SN framework	Samsung	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p005`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

原文请 RAN2 讨论最高层 Control PDU 的 SN 分配方案：按 NR 分配 SN、不分配 SN，或仅为部分 Control PDU 分配 SN。该项标注为 Not treated。

```text
For the single SN study, RAN2 is kindly asked to discuss the following options:
Regarding a Control PDU of the highest layer,
Option 1. SN is allocated to the Control PDU as in NR.
Option 2. SN is NOT allocated to the Control PDU.
Option 3. While SN is allocated to some Control PDUs, it is not allocated to others.
Not treated
Single SN – Header/Segmentation handling (If time allows)
R2-2601577	Discussion on Upper User Plane Functionality	Sharp	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p006`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

PDCP entity 分配 SN，且 PDCP header 包含 SN。

```text
PDCP entity assigns SN, and PDCP header includes SN.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p007`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

RLC 使用 PDCP header 中包含的 PDCP SN 执行 (re-)segmentation 和 ARQ。

```text
RLC performs (re-)segmentation and ARQ by using the PDCP SN included in the PDCP header.
R2-2601991	Single SN and other upper L2 functionality	InterDigital	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p008`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

无论采用何种层建模，利用 SN 的功能应共用 header structure 和 SN allocation mechanism。

```text
Regardless of the layer modelling, the header structure and the SN allocation mechanism should be common to functions exploiting the SN.
L2 re-transmissions
R2-2601829	Views on 6G User Plane: L2 Functionalities	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p009`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

无论是否合并 PDCP 与 RLC，跨层的 L2 retransmission 功能可整合为单一功能，以支持 L2 ARQ 和 RRC procedures。该提议被记录（Noted）。

```text
Regardless of whether PDCP and RLC should be merged into one single layer, L2 retransmission functionality across different layers (for L2 ARQ and RRC procedures) can be integrated into a single functionality.
Noted
R2-2602041	Further Discussion of upper User Plane Functionalities	Lenovo	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p010`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

研究 L2 common retransmission mechanism，覆盖 RLC ARQ 和 PDCP retransmissions，并评估 UL、DL（包括 RLC/PDCP status report）的适用性、收益与影响，同时考虑架构选项。讨论提及 mobility、fast ARQ 及不同重传用途等考量。

```text
RAN2 to study potential L2 protocol simplification by considering a common retransmission mechanism at L2 covering RLC ARQ and PDCP retransmissions.
Noted
-	Oppo thinks that we have to have separate re-transmission as we have non-real time retransmission for HO and RLC for ARQ.   LG and Lenovo think that even if they have different purposes we can still study the re-transmission.  Lenovo thinks that we have the fast ARQ which makes thinks simpler compared to 5G.
-	Qualcomm is confused as where do we keep the retransmissions that are for different options.   Apple thinks we can discuss, but they prefer to keep it in PDCP.   Huawei thinks it can only be in one layer, PDCP.
-	Huawei has similar concerns as Oppo but has some interest in optimizing the RLC and PDCP status reports.  Samsung agrees and would like to understand the benefit.
-	Mediatek thinks that this discussion shows that this should be part of the study.
-	ZTE thinks that we need to discuss this separate for UL and DL, as one thing we should not do is run ARQ on backhaul link, it has to remain close to radio so it can’t be merged.   The status report can be merged however.
-	Nokia thinks that the key to look at is the mobility, as for 5G we never wanted to exchange state variables, so we created a very simple PDCP retransmission.
-	Ericsson also thinks that we can study but the PDCP retransmission functionality will still be needed.
-	Mediatek and Interdigital think we should also taking into account that we have fast ARQ.
Study possibility of common L2 retransmission function for UL and DL (including RLC/PDCP status report), including benefits, impacts, taking into account architecture options.
Data transfer modes
R2-2601894	Upper UP functionalities	Nokia	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p011`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

考虑为 6G 采用一种 non-transparent RLC mode，以 common framework 配置 retransmissions 和 acknowledgements，适用于 RLC AM 与 UM。该提议被记录（Noted）。

```text
RAN2 consider one non-transparent RLC mode for 6G, where retransmissions and acknowledgements are configurable with a common framework for RLC AM and UM.
Noted
R2-2601463	Discussion on functionalities for upper user plane	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p012`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

研究 RLC AM (ARQ) 如何根据不同 QoS requirements 在不同 reliability 和 latency targets 下运行，例如向 Rx 引入 Tx-discard/move window signaling。另有提议研究 6G RLC 中 AM 和 UM operation 的 common framework。

```text
RAN2 to study how RLC AM (ARQ) can operate at different reliability and latency targets depending on diverse QoS requirements, e.g., by introducing Tx-discard/move window signaling to Rx.
Noted
R2-2602178	6G UP Functionality	Ericsson	discussion	Rel-20	FS_6G_Radio
Proposal 3	Study common framework in 6G RLC for AM and UM operation.
Noted
Discussion
-	Lenovo asks if we’d have a common header.  Nokia thinks we can consider different options.
-	Huawei asks what would be the functionality change.  Nokia explains it is can be dynamic changes.
-	Samsung asks if we’d have different window management mechanisms and how it work for different modes.   Nokia thinks that the window operation can be different.
-	Mediatek also thinks it’s good to study.
-	Qualcomm thinks we should keep it separate as it is very simple, there is no feedback channel, and it is for voice.  We can study AM and see if we can make it dynamic.   ZTE agrees as we need one mode of operation where the header operation is very small.   And for AM we should discuss enhancements separately.
-	Interdigital asks if this mode would replace AM and UM.  Nokia explains it is a single mode in addition to transparent mode.
-	Apple doesn’t see a need for this.
-	LG thinks that one key for this is mix type traffic and QoS adaptation and we can chose based on the priority of packets the transmission mode.
-	Sharp thinks that even if we unify so many procedures will be different, header, window etc, so we might as well keep it separate.
R2-2602557	Atomic transfer mode for RLC	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p013`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

提议研究 atomic RLC mode：禁用 RLC segmentation，且 IP packets 仅以完整单元交付。该提议标记为 Not treated。

```text
RAN2 to study an atomic RLC mode, where RLC segmentation is disabled and IP packets are only delivered in one piece.
Not treated
Reordering
R2-2601906	Discussion on 6G UP Functions	CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p014`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

提议考虑两项 reordering 增强：结合 in-order delivery 与 out-of-order delivery，并根据 service requirements 动态调整 PDCP reordering procedure。

```text
RAN2 to consider the following enhancements for reordering:
Combining in-order delivery and out-of-order delivery;
Adjusting PDCP reordering procedure based on service requirements dynamically.
R2-2601463	Discussion on functionalities for upper user plane	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p015`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

研究增强 6G PDCP reordering，在可行时适配 application QoE、降低高 DL throughput 下的 memory usage，并支持单个 DRB 中具有不同 reordering requirements 的多个 flows。

```text
RAN2 to study how to enhance PDCP reordering in 6G to achieve the following goals, if possible:
Adapt to application QoE needs
Reduce memory usage at high DL throughput
Support multiple flows in a DRB with different reordering requirements
R2-2602041	Further Discussion of upper User Plane Functionalities	Lenovo	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p016`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

提议考虑在 radio protocol 中支持 L4S、优先传送 L4S feedback，并研究在 L2 protocol layers 中区分 L4S 与 non-L4S traffic 及对 L2 buffer 支持 AQM。另提议研究 congestion management，包括在 L2 header 中支持 SN gap indication 和 congestion notification；相关研究标记为 Not treated。

```text
RAN2 to study PDCP discard mechanism and reordering procedure in 6G considering that packets of a radio bearer have different latency/reliability requirements.
Queue management/discarding
R2-2602039	Discussion on support for L4S in 6G radio protocol	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
Proposal 1	Consider support of L4S in radio protocol.
Proposal 2	Prioritize L4S feedback transmission (TCP ACK prioritization).
Proposal 3	Study how to separate L4S traffic from non-L4S traffic in L2 protocol layers.
Proposal 4	Consider support of active queue management (AQM) for L2 buffer.
-	ATT asks what kind of AQM considering.
Noted
R2-2602178	6G UP Functionality	Ericsson	discussion	Rel-20	FS_6G_Radio
Observation 6	Indications to manage queueing latency in RAN to transport layer are essential to reduce overall end-to-end latency and are subject to delays considering 5G’s need for pre-processing.
Proposal 4	To achieve lower end-to-end latencies for general services (e.g. eMBB), study support for faster queue management as an integral component of 6G RAN, i.e. support SN gap indication & congestion notification in L2 header.
Noted
Study mechanisms for congestion management
Not treated
R2-2601463	Discussion on functionalities for upper user plane	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p017`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

研究增强 6G PDCP/RLC discarding mechanisms，在确定丢弃内容时适配 application QoE 和 path latency variations，并支持单个 DRB 中具有不同 discard requirements 的多个 flows。

```text
RAN2 to study how to enhance PDCP/RLC discarding mechanisms in 6G to achieve the following goals, if possible
-	Adapt to application QoE and path latency variations in determining what to discard.
-	Support multiple flows in a DRB with different discard requirements.
R2-2601498	Discussion on upper user plane functionalities	Xiaomi	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p018`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

6G UP 支持基于定时器的 SDU discard。

```text
6G UP supports the timer based SDU discard.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p019`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

提出研究 discard function 是否以及如何适配 UE 侧时延，范围不限于 AS delay。该议题未处理；相关材料指出 SCHC 适用于 ROHC 不适用的 IoT 流量类型，并可作为 6G PDCP 层中 ROHC 的补充候选。

```text
Study whether and how discard function can adapt to UE side delay not limiting to AS delay.
Not treated
Header/data compression
R2-2602288	Static Context Header Compression (SCHC) for IoT traffic in 6G	Orange, Ericsson, Nokia, T-Mobile USA, Turkcell, Deutsche Telekom	discussion	Rel-20	FS_6G_Radio	R2-2600680
Observation 1	Efficient header compression is a key enabler to address IoT challenges
Observation 2	For typical IoT traffic patterns, header compression can substantially improve device energy consumption, latency, reliability and spectrum efficiency
Observation 3	Considering ROHC design and the IoT traffic characteristics, the net benefit of ROHC for IoT seems limited
Observation 4	SCHC with its characteristics is a strong candidate for integration into the 6G PDCP layer as a complement to ROHC.
Observation 5	SCHC’s ability to address different message types and protocols that are sent using specific traffic patterns for which ROHC is ill-suited, using a single static context, and to compress multiple protocol layers at once (e.g. IP/UDP/CoAP), makes it well suited to the mid-tier IoT
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p020`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

提出 RAN2 在 6G Study 中将 SCHC 作为 PDCP compression mechanism 候选，并研究支持 SCHC 的 RAN2 影响。相关提案认为 SCHC、ROHC、UDC 和 EHC 可作为互补的压缩机制纳入 6G SI。

```text
RAN2 to consider SCHC as a candidate for a PDCP compression mechanism and study RAN2 impact of supporting SCHC in the 6G Study
R2-2602289	Header Compression Functionality in 6G	Orange, Ericsson, Nokia, T-Mobile USA, Turkcell, Deutsche Telekom	discussion	Rel-20	FS_6G_Radio
Observation 1	In NR, multiple compression mechanisms co-exist, i.e., ROHC, UDC, EHC, yet not all use case scenarios are covered, in particular mMTC uses, which are expected in 6G.
Proposal 1	Regarding PDCP compression framework, RAN2 considers SCHC, ROHC, UDC, and EHC mechanisms as complementary and is considering including them in 6G SI.
R2-2601577	Discussion on Upper User Plane Functionality	Sharp	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p021`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

提出 RAN2 研究包含 ROHC、UDC 和 EHC 的统一压缩框架。

```text
RAN2 to study a unified compression framework including ROHC, UDC, and EHC.
R2-2601906	Discussion on 6G UP Functions	CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p022`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

提出 6G 从 day 1 支持 UDC，以满足 IMS services 支持、促进 TN/NTN convergence、改善 UE power saving 和增强 uplink coverage 的要求。

```text
6G should support UDC from day1 to satisfy the following requirement:
Support for IMS services;
Facilitation of TN/NTN convergence;
Improvement of UE power saving;
Enhancement of uplink coverage.
R2-2601539	Discussion on required functions and requirements for UP	NEC Corporation	discussion	Rel-20	FS_6G_Radio
R2-2601556	Discussion on single SN solutions	OPPO	discussion	Rel-20	FS_6G_Radio
R2-2601767	Functional requirements on 6GR User plane	1Finity	discussion	Rel-20	FS_6G_Radio
R2-2601818	6G UP Functionality	ZTE Corporation, Sanechips	discussion
R2-2601854	6G User plane functionalities	Ofinno	discussion
R2-2601892	Functionality and architecture of UP for 6G	Panasonic	discussion	Rel-20
R2-2601964	Discussion on 6G functionality and requirements for upper user plane	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
R2-2601980	The details of User Plane for 6GR	China Telecom	discussion	Rel-20	FS_6G_Radio
R2-2602068	Discussion on Functionality for Upper User Plane	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2602091	Discussion on UP functionalities in 6G	Spreadtrum, UNISOC	discussion	Rel-20
R2-2602157	Discussion on 6GR user plane protocol aspects	Sony	discussion	Rel-20	FS_6G_Radio
R2-2602265	Discussion on UP functionalities	NTT DOCOMO	discussion	Rel-20	FS_6G_Radio
R2-2602305	On the distribution of L2 functionality and congestion-adaptation	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
R2-2602411	Considerations on upper layer functionalitiey for 6GR UP	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2602499	Discussion on Single SN considerations	ETRI	discussion	Rel-20
R2-2602509	Discussions on segmentation and related functional requirements	Futurewei	discussion	Rel-20	FS_6G_Radio
R2-2602578	Discussion on functionality for upper user plane	DENSO CORPORATION	discussion	Rel-20
R2-2602581	Discussion on Upper UP Functionality for 6GR	TCL	discussion	Rel-20	FS_6G_Radio
R2-2602594	Discussion on Functionality for User Plane 	Rakuten Mobile, Inc	discussion
R2-2602606	Discussion on 6G User Plane aspects	Rakuten Symphony	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p023`

### [6G/Rel-20 RAN2#133bis] `agreement` 9.3.1.4 Other UP functionality

已批准发给 RAN1 的 FARQ LS，指出对 FARQ 而言，DL HARQ feedback 和 UL HARQ status 的 DCI 若具备 high reliability 将有益；可靠 HARQ feedback 的设计由 RAN1 决定。DL FARQ 可在了解 RAN1 最终设计及 feedback reliability 后再讨论是否需要增强。

```text
From RAN2 point of view, an ACK indication in the DCI is beneficial for a given HARQ process success.  RAN1 can be kindly asked to consider this benefit when designing the NACK.
The assumption is that there is no network requirement on when it is sent.
Upon reception of ACK, the correspond HARQ buffer can be cleared.  FFS on if and what enhancements can be considered once we see the RAN1 design and have an understanding on the reliability of the feedback.
For DL FARQ, can revisit the discussion for need of any enhancement after RAN1 final design.
Inform RAN1 about agreements from RAN2#133 and 133bis for both UL and DL FARQ.   Provide RAN1 a few lines about the fact that some concerns were raised about DCI overhead and some companies though it comes for free with the NACK design, however it is up to RAN1 how to design it.   Also indicate that from RAN2 point of view it would be beneficial to have a high reliability.
[AT133bis][008][6G UP] FARQ LS  (Mediatek)
Intended outcome: Agree to RAN1 LS
Deadline:  Friday
R2-2602806	LS on fast ARQ	RAN2	LS out	Rel-20	FS_6G_Radio	To:RAN1
Update: For FARQ for downlink data, RAN2 expects that networks can consider the HARQ feedback from the UE to trigger fast ARQ retransmissions.
Move to end of LS and update: From RAN2 point of view, HARQ feedback for DL and DCI for UL HARQ status with high reliability is beneficial for FARQ.   RAN2 expects that the design for reliable HARQ feedback is up to RAN1.
Add to action: (e.g. reliability and NACK to ACK error rate).
LS is approved in R2-2602813 with the changes above
Not treated
FARQ re-transmission content
R2-2601625	Discussion on fast ARQ and HOL blockage issue	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
Observation 3-1:	If UE can directly re-trigger MAC CE and RLC control PDU in the corresponding MAC PDU based on UL HARQ process status of NACK, MAC CE and RLC control PDU can be sent as soon as possible, which is beneficial to communication.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-a001`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

材料指出，按 NR design，即使超过 90% 的数据已成功传输，数据仍需在 RLC buffer 中保留一个 RLC RTT period（>30ms）。

```text
With NR’s design, data is required to remain in the RLC buffer for the RLC RTT period (>30ms), despite successful transmission of >90% of this data.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o001`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

HARQ process 成功时，若在 DCI 中提供 ACK，可增强对误解读的鲁棒性，并可用于清除 L2 buffer。

```text
If the ACK is provided in the DCI upon HARQ process success, it would be robust to misinterpretation and can be relied upon to clear the L2 buffer.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o002`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

HARQ process 成功时在 DCI 中提供 ACK，可使 L2 buffer 需求减少 60–80%。

```text
With an ACK provided in the DCI upon HARQ process success, there is a 60-80% reduction in L2 buffer needs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o003`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

基于 ACK signalling 的内存需求减少可 effectively had for free。

```text
The memory requirement reduction based on ACK signalling can be effectively had for free.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o004`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

通过 DCI 显式提供 HARQ ACK，可使 UE 避免冗余重传，并确保 MAC CEs 可靠交付。

```text
Explicit HARQ ACK via DCI enables the UE to prevent redundant retransmissions and ensures the reliable delivery of MAC CEs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o005`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

若 UE 指示的 ACK 设计为可抵御误解读，aNB 可据此清除其 L2 buffers，使 aNB 的 L2 buffer 需求减少 60–80%。

```text
If the ACK indicated by the UE is designed to be robust to misinterpretation, it can be used by the aNB to clear its L2 buffers leading to 60-80% reduction in aNB’s L2 buffer needs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o006`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

DL 中，网络可随时终止现有 HARQ process，并立即转为类似 ARQ 的重传；UL 中不可行。

```text
For DL, the network is free to terminate an existing HARQ process and move to an immediate ARQ like retransmission at any point in time. For UL, this is not feasible.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o007`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

HARQ-assisted DL ARQ 有望显著降低 latency，同时不增加 RLC retransmission rate。

```text
HARQ-assisted DL ARQ has the potential of significantly reducing latency without increasing RLC retransmission rate.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o008`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

NACK-To-ACK/DTX-to-ACK error detection mechanism 的动机是 DL RLC latency，属于 RAN2 范围；具体机制可由 RAN1 研究。

```text
The motivation for NACK-To-ACK/DTX-to-ACK error detection mechanism is DL RLC latency which is in RAN2 scope. The exact mechanism can be studied by RAN1.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o009`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

DL 中 N2A/DTX2A error detection and reporting 的挑战之一，是尽量减少由非 PUCCH errors 引起的 HARQ terminations 所导致的冗余报告。

```text
One challenge with N2A/DTX2A error detection and reporting in DL is minimizing redundant reporting based on HARQ terminations not caused by PUCCH errors.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o010`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

DL 中，PUCCH errors 和 missed DCIs 会导致 residual HARQ errors，进而需要 NW 进行 RLC retransmission。

```text
In DL, PUCCH errors and missed DCIs lead to residual HARQ errors, requiring an RLC retransmission at NW.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o011`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

高层 HOL blocking 主要有四类：Type 1 为 PDCP Rx window 内 Inter SDF intra DRB；Type 2 为 RLC Tx side 的 Intra/Inter-SDF intra-DRB。Type 3 为 RLC Tx side 的 PDCP data PDU 阻塞 PDCP control PDU；Type 4 为 Tx side control PDU 与 data PDU 之间的 Inter DRB 阻塞。

```text
There are mainly four types of HOL blocking issue at higher layer:
Type 1 (Inter SDF intra DRB HOL blocking at PDCP Rx window);
Type 2 (Intra/Inter-SDF intra-DRB HOL blocking at RLC Tx side);
Type 3 (Intra-DRB HOL blocking of PDCP control PDU by PDCP data PDU at RLC Tx side);
Type 4 (Inter DRB HOL blocking between control PDU and data PDU at Tx side).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o012`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

仿真结果显示，Type 1/2 HOL blocking 可能使网页下载延迟增加 80%。

```text
Simulation results show that Type 1/2 HOL blocking issue may result in 80% more delay for web page downloading.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o013`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

5G radio bearer setup/release procedure 无法以可扩展、动态、高效且灵活的方式适应应用产生的动态、大量短 TCP/QUIC 连接。

```text
5G radio bearer setup/release procedure cannot adapt to the application's dynamic and massive short TCP/QUIC connections in a scalable, dynamic, efficient and flexible manner.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o014`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

PDCP transmitter 的 HOL blocking 可由 UE/NW 实现充分处理。部分 QoS-related HOL blocking 可能发生在 RLC 的 Tx 与 ReTx buffers 之间。

```text
HOL Blocking at PDCP transmitter can be adequately handled by UE/NW implementation. Some QoS-related HOL blocking can happen at RLC between Tx and ReTx buffers.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o015`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

PDCP Rx 中，若某个 SDU 丢失，即使其他 SDU 属于不同 QoS flow，或无需等到该丢失 SDU 后再交付，也可能被滞留在 Rx buffer 中，从而发生 Head-of-line blocking。

```text
Head-of-line blocking in PDCP Rx happens when a missing SDU causes other SDUs to be held in the Rx buffer even if they belong to a different QoS flow or otherwise do not need to be delivered after the missing SDU.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o016`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

对于 Rx HOL blocking，从协议或硬件角度看，单个 DRB 使用多个 Sequence Number spaces（用于 reordering）相比多个 DRB 各使用单个 Sequence Number space 没有优势。

```text
For Rx HOL blocking issue, there is no advantage is supporting a single DRB with multiple Sequence Number spaces (for reordering) over multiple DRBs with a single Sequence Number space from a protocol or hardware standpoint.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o017`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

考虑到 6G 中 TB size 可能较大，交付已成功解码的 TB 部分可带来性能收益。

```text
With the potential large TB sizes in 6G, delivering successfully decoded portions of TB would offer performance benefits.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o018`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

在 5G NR mechanism 中，单个 CB 或 CBG 不被视为可靠；未成功验证 TB CRC 时，不能将其独立交付给 MAC layer。

```text
In the 5G NR mechanism, a single CB or CBG is not considered reliable and cannot be delivered to the MAC layer independently without successful TB CRC verification.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o019`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

启用将通过 CB-level CRC verification 的 CB/CBG 交付给 MAC，可部分解决 PHY layer HOL blocking：错误 CB/CBG 之前的 CB/CBG 将不再被阻塞。

```text
The PHY layer HOL blocking issue could be partially solved by enabling delivery of CBs/CBGs passing CB-level CRC verification to MAC, i.e., CBs/CBGs before an error CB/CBG will not be blocked.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o020`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

从 RAN2 角度看，要完全解决 PHY layer HOL blocking，MAC 需要识别每个已交付 CB/CBG 中 MAC subPDUs 的边界。

```text
From RAN2’s perspective, a solution to completely solve the PHY layer HOL blocking issue requires MAC to recognize the boundary of MAC subPDUs within each delivered CB/CBG.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o021`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

是否可以移除 TB-level CRC verification，以及 6G 是否保留 CBG，需要与 RAN1 确认。

```text
Whether TB-level CRC verification can be removed and whether CBG will be retained in 6G should be checked with RAN1.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o022`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

当前 5G NR 的 MAC subPDU 准备与转发方式不支持提前转发 control 或 data subPDU。HARQ 重传中，相关 CB 已正确解码时仍会造成显著时延。

```text
The current 5G NR approach for preparing and forwarding MAC subPDUs does not allow for early forwarding of control or data subPDUs. This results in significant latency in HARQ retransmission scenarios, when the relevant CB has already been decoded correctly.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o023`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

Early forwarding of MAC CEs 和/或其他 control messages 与 PDCP HOL blocking issue 无关。

```text
Early forwarding of MAC CEs and/or other control messages is not related to the PDCP HOL blocking issue.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o024`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

RAN2 倾向于在 DCI 中为指定 HARQ process success 提供显式指示，以清除 UL L2 buffers。该指示如何传送由 RAN1 决定。

```text
From RAN2 point of view, for clearing L2 buffers in UL, an explicit indication in DCI is preferred for a given HARQ process success. It is up to RAN1 how this is signalled.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p001`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

UE 收到 HARQ process success indication 后，可清除 uplink L2 buffer 中对应的数据，且不预期继续 HARQ retransmissions。Mediatek 和 ZTE 说明，原意是在 NDI toggled 时发送 ACK，而非每次 transmission 都发送。

```text
Upon reception of HARQ process success indication, the UE can clear corresponding data from the uplink L2 buffer.  The UE is not expected to continue HARQ retransmissions after this indication is received.
-	Mediatek and ZTE explain that the intention was that the ACK would be sent when the NDI is toggled rather than for every transmission.
Noted
R2-2601661	Other UP functionality in 6G	Samsung, Verizon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p002`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

RAN2 决定不继续推进 positive HARQ feedback assisted RLC enhancement，理由是其在 legacy RLC 之上的预期增益不显著或有限。讨论中提及 NACK 与 ACK 可利用同一 bit，以及 HARQ buffer 清理、RLC 恢复和可靠性等考虑。

```text
RAN2 to not pursue positive HARQ feedback assisted RLC enhancement, due to the expected gain is insignificant/marginal on top of legacy RLC.
Noted
Discussion
-	Mediatek highlights that both PDCCH and PDSCH have the same false positive probability.  Samsung thinks that DCI resource is scarce and variable and these benefits are marginal.   MEdiatek explains that we will need a bit for the NACK and the same bit can be used.  This is important for memory which is also a scarce resource lately.
-	ZTE thinks that we should ensure that there is no network requirement on when it sends it.   And the question is can we combine this with NDI.   With the NDI we would send a NACK and this same bit can also be used for the ACK.
-	Huawei agrees with ZTE, the network doesn’t always need to send.  There is a possibility of CRC passing but DCI is not decoded, but that is fine.
-	Apple agrees with Mediatek and explains that it is useful because the we can use the ACK a lot of the L2 timers which will release some resources and power saving gains.
-	LG has concerns on lossless operation. MEdiatek thinks that performance of DCI is very good and if it is good enough for URLLC it is good for eMBB.
-	Qualcomm also supports and indicates that it comes for free.  For reliability it is fairly safe to flush the HARQ buffer even if there are some errors as the RLC can recover.  For the RLC buffer that depends on how it is sent.
-	Vivo sees the benefits but we have to be careful with how we move the window and timer control.
-	Xiaomi thinks that we can implicitly assume it is there as the NACK will be in the DCI.
-	Interdigital doesn’t see an overhead issue as the bit is always there, so it is for free.   It can also maybe be used for MAC CE confirmation.
-	Ericsson thinks that it is up to RAN1 how they will design the NACK.  Also the blind decoding may be different.  What happens when you don’t receive the ACK as one the network may not want to send or there is reliability issue.  Mediatek agrees and RAN2 is just providing recommendation.  Blind decoding is not a big issue.   And there is no problem if we miss a DCI as you just continue keeping the data in your buffer.
-	ZTE wants to confirm that this will not impact max HARQ number of processes, it is just beneficial.   Companies confirm.
R2-2601575	Fast ARQ Retransmission and HOL Blocking Issue	Sharp	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p003`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

Explicit HARQ ACK 被认为有用，可用于快速更新 transmitting window。UL HARQ process status of ACK 无需针对每个 TB 发送，可在 transmission 成功且网络希望在同一 HARQ process 上以 toggled NDI 调度下一个 TB 时 piggyback。

```text
Explicit HARQ ACK is useful.
Noted
R2-2601625	Discussion on fast ARQ and HOL blockage issue	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
Observation 1-1:	UL HARQ process status of ACK is useful for fast update of the transmitting window.
Observation 1-2:	UL HARQ process status of ACK does not need to be sent for every TB and could be piggybacked when the transmission is successful and network wants to schedule the next TB on the same HARQ process with toggled NDI.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p004`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

UL HARQ process status of ACK 也可得到支持。

```text
UL HARQ process status of ACK could also be supported.
DL FARQ
R2-2602599	On HARQ triggered L2 retransmissions	MediaTek Inc., T-Mobile USA	discussion	Rel-20	FS_6G_Radio	R2-2602304
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p005`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

针对 downlink data 的 uplink HARQ feedback，其设计目标是与 uplink data transmission 一样能够抵御 misinterpretation。

```text
Uplink HARQ feedback for downlink data is designed to be as robust to misinterpretation as uplink data transmission.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p006`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

RAN2 将向 RAN1 发送 LS，提供启用 uplink 和 downlink FARQ 的设计要求。

```text
RAN2 to send an LS to RAN1 to provide them with our design requirements to enable uplink and downlink FARQ.
Noted
R2-2601715	Other UP functionality	Nokia	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p007`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

对于 DL fast ARQ，RAN2 将讨论如何实现对 NACK-to-ACK error 的快速检测。

```text
For DL fast ARQ, RAN2 discuss how to enable fast detection of NACK-to-ACK error.
Noted
R2-2601779	Fast ARQ and other 6G UP enhancements	ZTE Corporation, Sanechips	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p008`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

对于 DL，FARQ 已可行，其实现由 gNB 决定；HARQ feedback 中 NACK to ACK errors 的改进可留给 RAN1 研究。

```text
For DL, FARQ is already feasible and is up to gNB implementation and improvements for NACK to ACK errors for HARQ feedback can be left to RAN1 study
Noted
R2-2601467	Discussion on other UP functionalities	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p009`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

RAN2 将基于 N2A/DTX2A error detection 讨论相关问题，具体取决于 RAN1 的确认和进一步指导。讨论内容包括 UE 检测到错误后的行为（如提前终止 t-reassembly、发送 New MAC CE report）以及如何减少冗余 UE reporting。

```text
RAN2 to discuss the following issues based on N2A/DTX2A error detection (depending on confirmation and further guidance from RAN1)
-	UE behaviour upon N2A/DTX2A error detection, e.g., early termination of t-reassembly, New MAC CE report, etc.
-	How redundant UE reporting can be minimized.
Noted
R2-2602042	Discussion on fast ARQ support and HOL blocking	Lenovo	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p010`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

RAN2 将就基于 UE assistance information 支持 DL fast ARQ retransmissions 达成一致，例如指示中止后续 HARQ Retx(s) 并触发 RLC re(tx)。

```text
RAN2 to agree on supporting fast ARQ retransmissions for DL based on UE assistance information, e.g. indication to abort further HARQ Retx(s) and trigger RLC re(tx).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p011`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

RAN2 将研究提高 PDSCH transmissions 的 HARQ feedback reliability、减少 HARQ residual errors 的机制，并研究 UE 能否检测特定 HARQ feedback error cases 且向 NW 指示潜在错误。讨论中对 UE feedback 可能带来的额外开销及其帮助 aNB 了解 HARQ internal status 的作用有不同看法。

```text
RAN2 to study mechanisms to improve the HARQ feedback reliability for PDSCH transmissions to reduce HARQ residual errors. It should be studied whether UE can detect certain HARQ feedback error cases and indicate a potential HARQ feedback error to NW.
Noted
Discussion
-	Apple thinks that even L1 reliability is perfect we may need to discuss some of the L2 aspects, but it can be stage 3 anyways.
-	ZTE thinks that feedback from UE may just introduce excessive overhead as the NW has various reasons it has moved on to new transmission.  Huawei agrees and remembers in the last meeting we already agreed that this is dependent on ACK to NACK error.
-	Lenovo explains that the aNB doesn’t know the HARQ internal status and this indication would help the aNB similar to UL.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p012`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

当收到 UL HARQ process status 为 NACK 时，MAC entity 会重新触发对应 MAC PDU 中的 MAC CE，RLC entity 会重新触发其中的 RLC control PDU。

```text
When UL HARQ process status of NACK is received, MAC entity re-triggers MAC CE in the corresponding MAC PDU and RLC entity retriggers RLC control PDU in the corresponding MAC PDU.
R2-2601661	Other UP functionality in 6G	Samsung, Verizon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p013`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

对于未成功终止的 uplink HARQ process 对应的 MAC PDU，RAN2 将进一步讨论其重传处理，包括其中的 MAC CE(s) 和 control PDU(s)（如 status report）。

```text
For the MAC PDU of unsuccessfully terminated uplink HARQ process, RAN2 to further discuss the retransmission, in terms of:
the MAC CE(s) included in the MAC PDU
the control PDU(s) such as status report included in the MAC PDU
R2-2601833	Views on 6G User Plane: Fast ARQ and HoL Blocking	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p014`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

当某个 HARQ process 收到 NACK 时，发送端应仅对对应 TB 中复用的 AM radio bearer(s) 的 SDUs 触发 L2 retransmission。

```text
When NACK is received for a HARQ process, the transmitter should only trigger L2 retransmission for SDUs from AM radio bearer(s) that are multiplexed in the corresponding TB.
Higher layer HOL blocking
R2-2601503	Discussion on HOL blocking issue	Xiaomi, MediaTek Inc., CMCC, Sony	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p015`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

RAN2 优先研究 higher layer 的 type 1 和 type 2 HOL blocking 问题。

```text
RAN2 prioritizes the study of type 1 and 2 HOL blocking issue at higher layer.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p016`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

研究 type 1/2 HOL blocking 时应考虑应用流量特征：大量并发、动态且短生命周期的 TCP/QUIC connections（例如超过 100），以及指向多样服务器（包括第三方服务器）的多样 IP addresses。

```text
The study of type 1/2 HOL blocking issue should take into account the following characteristics of applications' traffic:
A large amount of concurrent, dynamic and short-lived TCP/QUIC connections, e.g. more than 100;
Very diverse IP addresses targeting diverse servers, even third-party servers.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p017`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

解决 type 1/2 HOL blocking 的方案应考虑 scalability、latency、signalling overhead 和 flexibility。

```text
The solution to type 1/2 HOL blocking issue should take into account the scalability, latency, signalling overhead and flexibility.
Noted
R2-2601769	Discussion on L2 retransmission enhancements and HOL blocking issue	1Finity	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p018`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

为缓解 higher layer HOL blocking，支持在 PDCP 层感知 QoS flow。研究选项包括在 PDCP Data PDU header 中通过 in-band signaling 携带 QFI，或由一个 PDCP entity 拆分到多个 RLC bearers 承载不同 QoS flows 或 QoS flow groups。

```text
To address the higher layer HOL blocking issue, QoS flow awareness in PDCP layer is supported by the following options:
Option 1: Use in-band signaling, i.e., QFI is included in the header of PDCP Data PDU.
Option 2: One PDCP entity can split into multiple RLC bearers to carry different QoS flows or QoS flow groups.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p019`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

RAN2 将研究接收端避免 HOL blocking 的两种方案：接收 PDCP entity 为不同 QoS flows 或 QoS flow groups 维护不同队列，或为 DRB 中的 QoS flows 配置不同的 in-order delivery requirements。

```text
RAN2 to study the following approaches for avoiding HOL blocking at receiver:
Option 1: Receiving PDCP entity maintains different queues for different QoS flows or QoS flow groups.
Option 2: QoS flows in a DRB can be configured with different in-order delivery requirements.
Noted
R2-2601467	Discussion on other UP functionalities	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p020`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

HOL blocking 解决方案不应在 DRB 内引入多个 PDCP sequence number spaces。

```text
HOL blocking solutions should not introduce multiple PDCP sequence number spaces within the DRB.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p021`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

研究接收端对部分 PDCP SDUs 进行选择性处理并乱序转发至上层；如何识别这些 SDUs 及转发标准仍待讨论。研究将不考虑 DRB 内多个 PDCP sequence number spaces，并将接收端选择性处理与 QoS 和 differentiated treatment 一并讨论，同时研究 Type 3 和 Type 4 HOL blocking。

```text
To alleviate PDCP Rx HOL blocking, RAN2 to study if UE can forward some PDCP SDUs selectively out-of-order to upper layers. FFS on how those PDCP SDUs are identified and the criteria to forward them.
Noted
Type 1 (Inter SDF intra DRB HOL blocking at PDCP Rx window);
Type 2 (Intra/Inter-SDF intra-DRB HOL blocking at RLC Tx side);
Type 3 (Intra-DRB HOL blocking of PDCP control PDU by PDCP data PDU at RLC Tx side);
Type 4 (Inter DRB HOL blocking between control PDU and data PDU at Tx side).
Discussion
-	Mediatek sees value in splitting out SN space to not block some of the application.    The assumption of configuring them in different bearers never happened, as it is expensive for networks to configure multiple bearers but separate SN is easier.   Qualcomm thinks that is complex for the UE as we need to maintain separate buffers.  Huawei has the same understanding as Qualcomm.
-	ZTE thinks that the only reason a flow is mapped to same bearer is because they have the same PDB anyways.   So if there is a good reason to map it to a different bearer we do it.  If they have a same PDB there is no the HOL blocking.  Support some packet differentiation like TCP ACK.   LG, Nokia, Lenovo, Vivo and Apple also agrees and supports QC proposal.   Maintaining different SN/windows/buffer is complex.
-	Fraunhofer points out that different mapping hasn’t happened, so we can at least start with P6.
-	Nokia thinks type1 and 2 depend on what higher layer information and we shouldn’t rule out yet type 3 and 4.
-	Docomo thinks that we should have some differentiation within a DRB, but if separate SN is complex we can at least consider P6 from QC
-	Samsung also agrees with QC and it should be on a per packet basis.
-	Mediatek and Xiaomi rae sad because the SN solution is excluded.
-	Apple would like to have one solution to address the multiple issues identified across HOL blocking and QoS
Agreements on HOL
Study will not consider multiple PDCP sequence number spaces within the DRB.
For HOL blocking at the receiver, study selective treatment of some PDCP SDUs (e.g. packets like TCP ACK or services).  This should be discussed together with QoS and differentiated treatment discussion.
Study Type 3 (Intra-DRB HOL blocking of PDCP control PDU by PDCP data PDU at RLC Tx side) and Type 4 (Inter DRB HOL blocking between control PDU and data PDU at Tx side).
Not treated
Lower layer HOL blocking (early CB content delivery)
R2-2601910	Faster HARQ Assisted ARQ and HOL Blocking	CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p022`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

向 RAN1 发送 LS，询问无论 TB CRC verification 结果如何，是否有必要且可行将成功解码的 CBs 或 CBGs 交付给 MAC layer。

```text
Send LS to RAN1 to inquire about the necessity and feasibility of delivering successfully decoded CBs or CBGs to the MAC layer regardless of the result of TB CRC verification.
R2-2601448	Considerations on faster ARQ retransmission and HOL blocking issues	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p023`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

向 RAN1 发送 LS，澄清 lower layer HOL blocking，并询问能否将通过 CB-level CRC verification 的已成功解码 CB/CBG 交付给 MAC layer。原文指出，按 CB multiplexing data 可能造成大量 segmentation 和 header overhead；CB 解码下若不提高 HARQ feedback granularity，fast ARQ 可能导致已解码数据被不必要地重传。

```text
Send an LS to RAN1 to clarify the lower layer HOL blocking issue. Ask RAN1 if it is possible to deliver the successfully decoded CB/CBG (passing CB-level CRC verification) to MAC layer.
R2-2601995	Fast ARQ and HoL blocking	InterDigital	discussion	Rel-20	FS_6G_Radio
Observation 3.2-5: Multiplexing data on a per CB basis would potentially result to extensive segmentation and header overhead of upper layer data and is, hence, not feasible approach.
Observation 3.2-6: With CB based data decoding, the fast ARQ procedure could not be supported without unnecessary re-transmissions of already decoded data in case the HARQ feedback granularity is not increased.
Observation 3.2-7: The encoding of upper layer data should be on basis of a finite number of CB groups of a large TB for which the HARQ feedback could be individually provided.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p024`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

从 RAN2 角度，如果能立即使发送端获知接收情况，则将完全/成功接收的 PDUs 从未完全接收的 TB 中交付给上层可能有益。

```text
From RAN2 perspective, being able to deliver completely/successfully received PDUs to upper layers from a not completely received TB can be beneficial if the transmitter can be immediately made aware of this.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p025`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

为避免不必要的重传，需要向发送端指示：从未完全接收的 TB 中，某组 CBs 已成功解码。

```text
Successful decoding of a group of CBs from a not completely received TB needs to be indicated to the transmitter to avoid unnecessary re-transmissions.
R2-2602407	Disscussion on faster ARQ retransmission and HOL blocking	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p026`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

对于 HOL blocking 的 lower layer 解决方案，RAN2 应等待 RAN1 完成 CB/CBG level design 后再继续讨论。

```text
For lower layer solution for HOL blocking issue, RAN2 should wait and postpone further discussion until RAN1 completes the CB/CBG level design.
R2-2601715	Other UP functionality	Nokia	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p027`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

研究对不同 payload types 进行 early forwarding 的收益，包括 MAC CEs、Other control messages 和 User Data。

```text
Study the benefits of early forwarding for various payload types: MAC CEs, Other control messages, User Data
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p028`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

研究基于 MAC PDU preparation 的 early forwarding 方案，且不影响 TBtoCB splitting 或其他 RAN1 定义的 PHY 机制。

```text
Study earlyforwarding solutions based on MAC PDU preparation that do not impact TBtoCB splitting or other RAN1defined PHY mechanisms.
UCI
R2-2602347	UL HARQ- and CSI feedback in 6G	Ericsson, MediaTek Inc., Charter Communications Inc., Turkcell, Jio Platforms, Kyocera, T-Mobile USA Inc., Ofinno, III, Anterix, CEWiT, Telstra, Deutsche Telekom, ASUSTek, AUMOVIO, Thales, ESA, LG Uplus, KDDI Corporation, NTHU, Bell Mobility	discussion	Rel-20
Observation 1	NR’s HARQ feedback for carrier aggregation requires tight coordination among involved schedulers which is very challenging in practical implementation.
Observation 2	Multiplexing HARQ feedback and CSI reports into PUCCH or PUSCH is complex and error-prone due to multiplexing rules and timeline restrictions.
Observation 3	The complexity of HARQ-FB and CSI reports and the way they are transmitted in NR became one of the biggest pain points for network and UE implementation.
Observation 4	MAC offers a generic framework of multiplexing control information and user data.
Observation 5	Explicit IDs for HARQ processes and CSI reports would make the reports self-contained which is a prerequisite for avoiding timeline- and multiplexing restrictions, inter-carrier dependencies and race conditions that were observed with NR’s L1 UCI.
Observation 6	The PUSCH’s in-built CRC and HARQ would avoid ACK(NACK errors in UL HARQ feedback and thereby reduce end-to-end latency spikes compared to NR’s RLC retransmissions.
Observation 7	The PUSCH’s in-built CRC and HARQ would make CSI feedback robust.
Proposal 1	Evaluate how different transmission schemes for UL HARQ- and CSI feedback affect the end-to-end performance for various applications. Evaluate for various bandwidths including the narrowest bandwidths of 6G, and evaluate various deployment scenarios including NTN. Choose a transmission scheme that offers the best performance/complexity trade-off and that avoids NR’s complicated timeline- and multiplexing restrictions.
-	Samsung wonders why we have a parallel discussion in RAN1 and RAN2.  RAN1 is discussing how to improve this so we can’t benchmark with 5G design.   Comparing MAC and PDSCH would need to be analysed and compared in same place in RAN1.
-	Vivo, Xiaomi also has the same understanding as Samsung.   RAN1 should discuss reliability for UL and DL so RAN1 should discuss this issue first.
-	Mediatek is surprised that we let RAN1 study the UCI on MAC.
-	Apple explains that it has happened many times, RAN1 decides something and asks us to design MAC CEs and we do it.
-	Ericsson asks if RAN1 is studying end-to-end performance.
-	Qualcomm can study whether it is better to send something on PUCCH or PUSCH and then they can tell us.   Let’s follow the usual procedure.
-	Oppo thinks that we can discuss in RAN2 what can be enhanced.
-	ZTE, LG, Nokia, and Huawei also thinks RAN1 has to finish the evaluation.
-	Futurewei explains that reliability is not the only consideration, latency is also a consideration and in some cases it is too slow in MAC CE.
Wait for RAN1 guidance if they need RAN2 to evaluate something once they have done some initial evaluations.
Noted
Not treated
R2-2601473	Discussion on fast ARQ	NEC	discussion	Rel-21	FS_6G_Radio
R2-2601561	Discussion on faster HARQ assisted ARQ and head-of-line blocking	OPPO	discussion	Rel-20	FS_6G_Radio
R2-2601782	Addressing HOL blocking issue	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
R2-2601797	Discussion on fast ARQ	CANON Research Centre France	discussion	Rel-20	FS_6G_Radio
R2-2601858	6G Faster ARQ and HOL blocking	Ofinno	discussion
R2-2601891	Discussion on FARQ and HoL issues for 6G	Panasonic	discussion	Rel-20
R2-2602011	Discussion on faster HARQ assisted ARQ in 6G	KT Corp.	discussion	Rel-20	FS_6G_Radio
R2-2602026	6G fast ARQ and HOL blocking avoidance	Ericsson	discussion
R2-2602072	Discussion on Other UP functionality	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2602093	Discussion on L2 (re-)transmission and HOL in 6G	Spreadtrum, UNISOC	discussion	Rel-20
R2-2602161	Discussion on HOL aspects	Sony	discussion	Rel-20	FS_6G_Radio
R2-2602162	HARQ and fast ARQ data recovery in 6G	Sony	discussion	Rel-20	FS_6G_Radio
R2-2602304	On HARQ triggered L2 retransmissions	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
=> Revised in R2-2602599
R2-2602376	Discussion on HARQ assisted ARQ 	ETRI	discussion	Rel-20
R2-2602415	Considerations on fast ARQ and HoL for 6GR UP	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2602448	Discussion on lower layer mechanism for HOL blocking	WILUS Inc.	discussion	Rel-20	FS_6G_Radio
R2-2602564	Cross-layer aspects on latency, reliability and resource usage	CEWiT	discussion	Rel-20	FS_6G_Radio
R2-2602582	Discussion on Faster HARQ Assisted ARQ for 6GR	TCL	discussion	Rel-20	FS_6G_Radio
R2-2602595	Discussion on FARQ and HOL reduction for 6G UP	Rakuten Mobile, Inc	discussion
R2-2602609	discussion on other UP functionality	NTT DOCOMO INC..	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p029`

### [6G/Rel-20 RAN2#133] `agreement` 10.3.1 User plane

对于 single SN，研究假设为 standalone，待 RAN 全会决定 CU/DU split 和 DC 后再确定适合的方案；使用 SN 的最高层分配 SN，可用于 security、in-order delivery、segmentation/re-segmentation、ARQ 等功能。尚待研究该机制在单层（如 PDCP/RLC combined）和分层结构中的工作方式，并应考虑 PDCP control PDUs 处理及 SN gap 问题。

```text
For single SN
-	Study assumes standalone and depending on RAN plenary decision on CU/DU split and DC we will determine what solution best fits those decisions.
-	Highest layer utilizing the SN assigns SN, which can be used for at least the following functionalities: security, in-order delivery, segmentation/re-segmentation, ARQ, etc.
-	FFS how the functionality works in the single layer (e.g. PDCP/RLC combined) and separate layer.   Study should highlight benefits/gains/problems
R2-2600149	Discussion on functionalities for user plane	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
Observation 2-1:	RAN2 should consider how to handle the PDCP control PDUs under the single SN mechanism.
Observation 2-2: SN gap issues should be resolved under the single SN mechanism.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-a001`

### [6G/Rel-20 RAN2#133] `agreement` 10.3.1 User plane

应研究 HOL blocking，覆盖高层（如 QoS 相关）和低层（如 MAC、CB）机制，以及 RX 和 TX 两侧。公司可提供评估并说明假设。

```text
Study HOL blocking issues.   Study should address both higher layer (e.g. QoS related) and lower layer (e.g. MAC, CB) mechanism and both RX/TX.   Companies can bring evaluations and explain assumptions, etc.
Functionality of SDAP layer
R2-2601033	Discussion on SDAP	NTT DOCOMO INC.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-a002`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

PDCP 和 RLC 各自保留 SN，因为它们在不同协议层承担不同功能。

```text
Both PDCP and RLC have their own SNs because they serve different functional purposes at different protocol layers.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o001`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

NR RACH procedures 的复杂性来自不同 RACH type 分别定义流程造成的冗余、RACH partitioning 带来的资源选择复杂性，以及 RACH fallback 的复杂检查。

```text
NR RACH procedures are complicated due to 1/ redundancy caused by separate procedures defined for different RACH type; 2/ resource selection complexity introduced by RACH partitioning; 3/ complicated checks for RACH fallback.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o002`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

2step RACH 对低时延连接建立和小数据传输具有明显优势。

```text
2step RACH offers clear benefits for lowlatency connection setup and smalldata transmission.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o003`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

应在 RACH partitioning 框架基础上考虑缓解 RA overload 的机制。

```text
Mitigation mechanisms for RA overload should be considered on top of the RACH partitioning framework.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o004`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

RACH resource adaptation 不必限于 additional RACH resources，也可应用于 6G 中配置的任意 RACH resources。

```text
RACH resource adaptation does not need to be limited to additional RACH resources and can be applied to any RACH resources configured in 6G.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o005`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

提出研究支持更大的 Msg3/MsgA size 的可能性，以实现更快且更适当的 initial setup。

```text
It would be beneficial to study the possibility of supporting a larger Msg3/MsgA size to enable faster and more appropriate initial setup in 6G.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o006`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

在 NR 中，通过 RACH partitioning 提前指示 feature combinations 会导致 RACH resources 使用效率很低，并使 signaling 过于复杂。

```text
In NR, early indication of feature combinations by RACH partitioning leads to very inefficient use of RACH resources and overly complex signaling.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o007`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

在 NR 中，RACH resources 难以适应接入负载的短期变化，常导致高争用和接入失败。

```text
In NR, RACH resources do not adapt well to short-term variations in access load, often resulting in high level of contention and access failures.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o008`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

AS layer 的 HOL blocking 可能源于多种 traffic 映射到同一 DRB 并由同一 queue 处理，或不同 DRB 的 traffic 被复用到同一 TB。后者会使映射到解码失败 CB 的 traffic 阻塞映射到成功解码 CB 的 traffic 交付。

```text
HOL blocking issue at AS layer may be caused by the following reasons:
-	Multiple traffics are mapped to the same DRB and they are handled by the same queue;
-	Traffics from different DRBs are multiplexed in the same TB, the traffics mapped to the failed decoded CBs will block the delivery of traffics mapped to the successfully decoded CBs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o009`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

将 service flows 映射到不同 DRB 的现有方案无法解决同一 DRB 内一个 service flow 对其他 service flows 的 HOL blocking。该方案缺乏 scalability 和 flexibility，并导致 high latency 与 high signalling overhead。

```text
The HOL blocking issue of one service flow to other service flows in the same DRB cannot be resolved by existing solution of mapping service flows to different DRBs, as it is not scalable, flexible, and results in high latency and high signalling overhead.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o010`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

在 NR 中，单个 code block (CB) 失败可能延迟其他 CB 中 PDU 的交付；由于 6G 的 TB 更大，该问题可能更严重。

```text
In NR, failure of a single code block (CB) can delay the delivery of PDUs in other CBs. This problem can be more critical in 6G with its much larger TBs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o011`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

在 TB 起始处包含有关 MAC CEs 或 MAC subPDUs 的 metadata，可帮助接收端加快 TB 处理。

```text
Including metadata about MAC CEs or MAC subPDUs at a start of a TB can help the receiver speed up processing of the TB.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o012`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

NR 的 SDAP layer 需要投入 operational effort，以确保 handover 期间正确转发数据；发生 QoS flow remapping 时，也无法保证 in-order delivery。

```text
The SDAP layer in NR requires operational effort to ensure proper data forwarding during handover and does not guarantee in-order delivery when QoS flow remapping occurs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o013`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

NR 中的 SDAP Rmap 和 RQoS mechanism 会增加 user plane processing overhead 与 latency。

```text
The SDAP Rmap and RQoS mechanism in NR increases the user plane processing overhead and latency.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o014`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

QFI marking 是一项简单功能，可合并到其他 protocol layer 中。

```text
QFI marking is a simple function and can be merged into other protocol layer.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o015`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

认为 Reflective QoS 在 6GR 中效率不高。

```text
Reflective QoS is not efficient in 6GR.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o016`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

RAN2 将研究如何增强 6G 的 PDCP/RLC discarding mechanisms（如可行），以处理 per-packet discard timer 可能丢弃 application bursts、且不考虑 QoE 是否改善的问题。还指出不随 path latency variations 调整的 single static timer 对控制 application delay 过于粗略。

```text
RAN2 to study how to enhance PDCP/RLC discarding mechanisms in 6G to achieve the following goals, if possible
-	Per-packet discard timer leads to discarding of application bursts without considering if this leads to improvement of degradation of QoE;
-	Single Static timer that does not adapt to path latency variations provide a very coarse tool for controlling application delay.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o017`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

提出 6G User Plane 设计需考虑卫星载荷的 SWaP 约束，并针对全量或部分 6G RAN 功能在星上的 regenerative payload 优化协议开销。还提出为 NTN extended RTT 定义 user plane timers，并支持按 service type 动态启停 user plane retransmission mechanisms。

```text
Designing the satellite link for very low error rates minimizes the need for retransmission mechanisms at user plane level that can be turned off, reducing complexity and resource use without impacting end-to-end reliability.
Proposal 1	The 6G User Plane shall be designed to take into consideration the satellite’s constraints SWaP (Size, Weight and Power) on board:
	Regenerative payload with full 6G RAN on board: Optimize the memory and computational footprints of the user plane protocols
	Regenerative payload with partial 6G RAN functions on board (6G RAN architecture split): Optimize the number of interactions between the user plane protocols
Proposal 2	The user plane timers of the 6G radio access shall be defined to accommodate extended RTT for NTN scenarios
Proposal 3	The 6G access radio protocol shall support all specific features defined for 5G NR-NTN including the dynamic activation and deactivation of retransmission mechanisms at user plane level, depending on the service type.
[3 min]
R2-2600491	The functions of User Plane for 6GR	China Telecom	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o018`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

RAN2 将研究 single layer 2 SN 的细节，包括由哪个协议分配 SN、哪个协议头携带 SN；control PDUs 的处理尚未确定。

```text
RAN2 to study details of the single layer 2 SN, e.g. which protocol assigns the SN and which protocol header carries the SN in the header. Handling of control PDUs is FFS.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p001`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

RAN2 将研究通过 L2 common retransmission mechanism 覆盖 RLC ARQ 和 PDCP retransmissions，来简化 L2 protocol 的可能性。

```text
RAN2 to study potential L2 protocol simplification by considering a common retransmission mechanism at L2 covering RLC ARQ and PDCP retransmissions.
[2 min]
Noted
R2-2600591	Considerations on a single SN	Samsung	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p002`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

对于 single SN study，采用 PDCP sequence number 作为 single SN。

```text
For a single SN study, the PDCP sequence number is utilized as the single SN.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p003`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

对于 single SN study，若存在 RLC layer，则其将引用 PDCP header 中的 SN field，并将其作为 RLC layer 的 SN。

```text
For a single SN study, if the RLC layer is present, it will refer to the SN field in the PDCP header and treat it as the SN in the RLC layer.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p004`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

就 single SN study，提出讨论两种方案：保留分别的 RLC header 和 PDCP header，或在 RLC 与 PDCP layers 使用 common header。原文记录了对层间拆分、同步、开销和复杂度的不同意见，未给出方案结论。

```text
For a single SN study, RAN2 is kindly asked to discuss the following options:
Option 1. To have a RLC header and a PDCP header, separately as in NR.
Option 2. To have a common header in RLC and PDCP layers.
[2 min]
Noted
Discussion
-	Qualcomm asks if PDCP and RLC are collocated and if the schedulers are collocated for CA case.   Ericsson explains that this would definitely depend on higher layer split.
-	Mediatek thinks that we should have a discussion on single Scell and can we assume that a SN is available and does the system work.   Once we know the split we can discuss does it work or not.   Qualcomm thinks that whether it works or not will depend on the overall system.   Mediatek explains that we have to make an initial assumption.   Qualcomm thinks that when we send the status report which entity/carrier/layer is aware of the information right away.
-	ZTE thinks that this discussion shows that we are not ready for the layering discussion, but we think it should work even if there is CU/DU.   LG thinks that there would be an F1 impact as the SN would need to be provided to the DU from the CU.    Mediatek explains that SN is in the F1 interface already.
-	Verizon asks what is the benefits.   Lenovo explains that in the last meeting we discussed the benefit is overhead and processing.   Samsung thinks that if we have CU/DU split the benefit may go away as now we have to synchronize the numbers via F1
-	CMCC thinks that we should combine.
-	LG thinks that we are now creating complexity and it is better to duplicate the SN.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p005`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

RAN2 将进一步讨论两个问题：如何处理 PDCP control PDU，以及如何处理 single SN mechanism 的 SN gap。

```text
RAN2 to further discuss the following two issues: 1) How to handle PDCP control PDU and 2) How to address SN gap for the single SN mechanism
[2 min]
Not treated
Random Access procedure
R2-2600622	UP functionalities and requirements	Nokia	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p006`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

提出设计统一的 Random Access procedure，以尽量减少对 RA partitioning 的需求，并与 RAN1 一起研究 RA PUSCH payload size 可能引发的问题。

```text
Design a unified Random Access procedure which minimizes the need of RA partitioning, and study, together with RAN1, possible issues with RA PUSCH payload size.
[2 min]
Noted
R2-2600207	Discussion on the 6G user plane features	OPPO	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p007`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

RAN2 将研究 6G 统一且简化的 RACH 框架，涵盖统一的 2-step RACH 与 4-step RACH、统一 RAR format、简化 RACH partition 和简化 fallback procedure。

```text
For 6G, RAN2 to support a unified and simplified RACH framework considering:
	Unified 2-step RACH and 4-step RACH.
	Unified RAR format.
	Simplified RACH partition.
	Simplified fallback procedure.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p008`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

RAN2 认为 RACH partitioning 仅应在确有必要时使用，并同意研究随机接入流程，明确哪些特性绝对需要 msg1 indication、哪些可等到 msg3；LS 已获批准并发送至 RAN1。

```text
For 6G, RAN2 study to support dynamic load distribution for RACH, e.g., flexible carrier switching during RACH.
[2 min]
Noted
Discussions
-	Xiaomi asks if there is a RAN2 issue.  Nokia explains that there may be no impact.   ZTE thinks that one impact is that we don’t support segmentation so we have design the RA PUSCH payload size to be long enough.   One option could be to design the CP to support segmentation.
-	Nokia thinks that if we can minimize the amount of CCCH sizes based on features etc it would be simpler.
-	Huawei thinks that the requirement comes from RAN1.   For partitioning the need was for early identification of the preamble, so how do we solve this?  Nokia explains that for example for SDT we don’t need identify in msg1 and can do it in msg3.  And we can unify the solutions for both msg1 and msg3 based RA.
-	Mediatek agrees with the RACH partitioning issue so we should consider how we can avoid the need for partitioning with a correct design.    Sharp agrees with Mediatek.   Qualcomm agrees we should avoid the partitioning but we should work with RAN1.    Please avoid partitioning as much as possible and check if RAN1 can create a msg1 which allows some information to be provided.
-	Ericsson agrees and we would need to understand what needs the msg1 indication and what can wait for msg3.
-	Interdigital agrees with Ericsson and we should study whether we can simplify the partitioning and the combination
-	Ericsson thinks that together with the agreement we should also indicate why it increases complexity and that even if we increase preamble space we will still have these problem.
Agreements on RA
-	One problem identified from 5G is the excessive RA partitioning.  Study random access procedures and understand what feature absolutely needs msg1 indication and what can wait for msg3.
-	Send LS to RAN1 indicating our pain points
[AT133][011][6G UP] LS to RAN1 on RA (Qualcomm)
Intended outcome: agree to LS
Deadline:  Friday
R2-2601351	[DRAFT] LS on early indication via RACH partitioning	Qualcomm	LS out	Rel-20	To:RAN1	FS_6G_Radio
-	Nokia and others think that we should say used only.  Qualcomm was concerned that then it implies we are removing the option of avoiding it all together.  Other companies explains that even if we say should only be used when truly necessary, it includes the option of avoiding if possible.
Update: From RAN2’s perspective, RACH partitioning should be used only when it is truly necessary and remove “if at all”
The LS is approved in R2-2601354 with change above
Not treated
R2-2600434	Discussion on 6G UP functionality and requirements	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p009`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

RAN2 将研究 RACH procedure，至少考虑 6G Day1 的多种用途与事件、2-step 和 4-step RACH、RA overload 缓解、PRACH 与 MsgA PUSCH resources 调整，以及更大的 Msg3/MsgA size。

```text
Study RACH procedure considering at least following aspects:
	Multiple purposes and events requiring the RACH procedure from 6G Day1
	Support of both 2-step RACH and 4-step RACH
	Mitigation of RA overload situations
	Adaptation of PRACH and MsgA PUSCH resources
	Larger Msg3/MsgA size
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p010`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

RAN2 将研究如何在 random access procedure 期间，为不同 device types/features 支持可扩展的 early indication mechanisms。

```text
Study how to support scalable early indication mechanisms for diverse device types/features during random access procedure.
[2 min]
R2-2600139	Discussion on 6G user plane functionalities	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p011`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

RAN2 将研究提升 RACH resources 使用效率的设计，例如除非确有必要否则避免 RACH partitions，以及动态或按需分配 RACH resources。

```text
Study RACH designs that enable more efficient use of resources, e.g. explore methods to avoid RACH partitions unless truly necessary, dynamic or on-demand allocation of RACH resources, etc.
[2 min]
Head-of-line blocking and CB/CBG based data handling
R2-2600101	Discussion on HOL blocking issue	Xiaomi, MediaTek Inc., Huawei, HiSilicon, CMCC, Sony	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p012`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

RAN2 同意研究同一 DRB 内一个 service flow 对其他 service flows 造成的 HOL blocking 解决方案，并考虑 scalability、latency、signalling overhead 和 flexibility。

```text
RAN2 agrees to study solutions to the HOL blocking from one service flow to other service flows in the same DRB, taking into account the scalability, latency, signalling overhead and flexibility.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p013`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

RAN2 同意研究解决 failed decoded CBs 阻塞 successfully decoded CBs 的方案。

```text
RAN2 agrees to study solutions to the HOL blocking from failed decoded CBs to successfully decoded CBs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p014`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

针对同一 DRB 内 service flows 之间的 HOL blocking，RAN2 考虑研究降低每个 queue 的成本与 signalling overhead、允许 UE/BS 动态建立或释放 queue，以及动态调整 queue properties（如 priority、bit rate）的方向。

```text
For the HOL block from one service flow to other service flows in the same DRB, to allow scalable, low latency, low signalling overhead and flexible solution, RAN2 considers to study the following directions:
- Scalability: reduce the cost/processing per queue;
- Latency: allow UE/BS dynamical queue setup/release;
- Signalling overhead: reduce the signalling overhead per queue;
- Flexibility: allow dynamical adjustment of queue properties (e.g. priority, bit rate).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p015`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

针对 failed decoded CBs 阻塞 successfully decoded CBs 的问题，RAN2 考虑研究允许已成功解码的 CBs/CBGs 交付至 upper layer 的方案。

```text
For the HOL blocking from failed decoded CBs to successfully decoded CBs, RAN2 considers to study solution to allow delivery of successfully decoded CBs/CBGs to upper layer.
[3 min]
Noted
R2-2600139	Discussion on 6G user plane functionalities	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p016`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

RAN2 将研究可加快接收端处理的新 MAC PDU formats，例如按 CB/CBG 或其组复用数据而非按 TB 复用，并在 TB 起始处携带 MAC CEs 或 MAC subPDUs 的 metadata。讨论提及需关注 overhead、processing、data rate、HARQ 及 RAN1 依赖等影响。

```text
Study new MAC PDU formats that can enable faster processing at receiver, e.g. multiplexing data per CB/CBG or groups of CB/CBGs instead of per TB, including metadata about MAC CEs or MAC subPDUs at start of a TB.
[2 min]
Noted
Discussion
-	LG thinks that HOL will still occur if there are multiple MAC SDUs in on CB.   So is the assumption that one SDU is mapped too on CB.
-	CATT thinks that CB was never deployed so we are enhancing something on top of that.
-	Interdigital asks Xiaomi at which level we differentiate the service flows to go on CB.  Xiaomi explains that HOL can occur between flows and within a slow.   Interdigital also ask what would be the overhead if we have to fit into CB.  Qualcomm thinks that the CB size will the same but TB will be higher and higher so it can HOL.
-	ZTE is happy to study as this problem can occur.   CB is small and ZTE reminds everyone that we still have to pass a full PDCP PDU so security can pass.     Xiaomi thinks that their evaluation showed a reduction in 60% in delay.
-	Huawei and Nokia think that we should study both UL and DL.   Nokia thinks that we can consider CB level but aligning all MAC SDU with CBs might be a little too much.
-	Mediatek thinks that this is an important issue to address as today we see this issue with everything mapped to single DRB, and if one packet is missed everything gets stuck.   However, if we look at the MAC solution space we should be careful with overhead, processing and data rate impacts.
-	LG thinks that a better QoS flow scheduling, for example per QoS flow handling,  can solve some of the problems already.  For lower layer agree with the problems and there is dependencies on RAN1.
-	Apple thinks that HOL is a problem and feel that this topic should be addressed in QoS as some of the solution will already solve some of these problems.   For lower layer there seems to be higher L1 impact and also there may be some impact to HARQ operation and we would further introduce restriction on what is put in the CB.
-	Lenovo thinks that CB based would have impact to RAN1.   What we can do is look at LCP and how multiplexing takes into account QoS information into account.    The interesting thing is how is the transmitter aware and understand how to map things.
-	CMCC thinks this also improves latency and we should focus our study in RAN2 first.
-	Samsung thinks that the lower layer mechanism may cause other issue for example triggering PDCP to detect a gap while the CB retransmission is taking time to complete successfully.
-	Interdigital thinks that we can start by acknowledging that we have this HOL in higher layer and the CB based solutions are linked to RAN1.
-	LG thinks we should address both intra and inter QoS flow issues.  Ericsson would like to process some of the MAC CEs early, so we should separate the end to end blocking and early processing of MAC CE.
-	ZTE reminds everyone that we need to think about HW friendliness so going towards LTE like would remove that HW benefits we did in NR.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p017`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

RAN2 将与其他工作组协调，研究是否将 SDAP 子层合并到 PDCP 子层，使 PDCP 支持 QoS Flow 与 DRB 之间的映射。该项研究已记为 Noted。

```text
RAN2 studies whether SDAP sublayer can be merged to PDCP sublayer, i.e., PDCP can support mapping between QoS Flow and DRB, coordinating with other WGs.
[2 min]
Noted
R2-2600658	Discussion on 6G user plane functionality	Spreadtrum, UNISOC	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p018`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

RAN2 将研究移除 RQoS、Rmap 机制和 SDAP，将 QFI 标记移至其他协议层（例如 PDCP），以及在 stage2 规范中规定 QoS flow 到 DRB 的映射。该项研究已记为 Noted。

```text
RAN2 to study:  1) Removing RQoS and Rmap mechanism and SDAP; 2) Moving QFI marking to other protocol layers, e.g., PDCP; 3) QoS flow to DRB mapping is specified in stage2 spec.
[2 min]
Noted
R2-2600348	Functional requirements on 6GR User plane	Fujitsu	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p019`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

以在 SDAP 层保留 QoS flow 到 DRB 的映射功能作为基线；若 RAN2 同意 6GR 不支持 reflective QoS，则向 SA2 发送 LS 供其了解。还将研究满足 QoS framework requirements 所需的功能，并讨论由哪个协议层及如何规定这些功能。

```text
Keep the QoS flow to DRB mapping function in the SDAP layer as baseline. If RAN2 agrees that reflective QoS is not supported in 6GR, send an LS to SA2 for information.
[2 min]
Noted
Functionality
Reflective QoS
-	Huawei thinks that IP may change frequently so this feature can help with that issue.
-	ZTE explains that in 5G it doesn’t change often, but in 6G one of the things is the fast QoS switching, so removing it doesn’t fully make sense.  So we should remove the pain point with adding bit in every header, but we should find a way to address the fast changing QoS.
-	Nokia thinks that the QoS flow marking was a solution to handle QoS flow relocation from one DRB to another so we should discuss that.
-	Qualcomm thinks that we should aim for solutions that don’t have per packet processing, we can consider RRC and this was never used.  ZTE agrees on the per packet processing but not to move it to RRC.  Huawei agrees.
Study the functionalities required to meet the QoS framework requirements and come back to how and which protocol layer this is specified
Not treated
Queue management/discarding
R2-2600974	Discussion on support for L4S in 6G radio protocol	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
Proposal 1	Consider support of L4S in radio protocol.
Proposal 2	Prioritize L4S feedback transmission (TCP ACK prioritization).
Proposal 3	Study how to separate L4S traffic from non-L4S traffic in L2 protocol layers.
Proposal 4	Consider support of active queue management (AQM) for L2 buffer.
[3 min]
R2-2600410	UP functionalities in 6G L2	Ericsson	discussion	Rel-20	FS_6G_Radio
Observation 4	Indications to manage queueing latency in RAN to transport layer are essential to reduce overall end-to-end latency and are subject to delays considering 5G’s need for pre-processing.
Proposal 5	To achieve lower end-to-end latencies for general services (e.g. eMBB), study support for faster queue management as an integral component of 6G RAN, i.e. support SN gap indication & congestion notification in L2 header.
[2 min]
R2-2600139	Discussion on 6G user plane functionalities	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p020`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

RAN2 将研究如何增强 6G 中的 PDCP/RLC discarding mechanisms，以尽可能适应应用 QoE 需求和路径时延变化来决定丢弃内容，并支持同一 DRB 中具有不同丢弃要求的多个 flows。

```text
RAN2 to study how to enhance PDCP/RLC discarding mechanisms in 6G to achieve the following goals, if possible
-	Adapt to application QoE needs and path latency variations in determining what to discard;
-	Support multiple flows in a DRB with different discard requirements.
[3 min]
TN/NTN harmonization (If time allows)
R2-2600176	User Plane for 6G NTN	THALES, TNO, ESA, Novamint, Iridium	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p021`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

RAN2 将考虑 TN/NTN 集成对用户面设计的影响，包括 HARQ process number、下行禁用 HARQ 与上行 HARQ mode A/B，以及与 RTT 相关的 L2 timers（如 reassembly 和 reordering timers）。

```text
RAN2 consider the following TN/NTN integration in UP design:
	HARQ process number
	HARQ disabled in DL and HARQ mode A/B in UL
	L2 timers related RTT, such as reassembly and reordering timers.
[2 min]
R2-2600075	Considerations on User Plane Functionalities for 6GR	vivo	discussion	Rel-20
R2-2600097	Consideration on 6G UP L2 functionalities	Xiaomi	discussion	Rel-20
R2-2600165	6G UP functionality	ZTE Corporation, Sanechips	discussion
R2-2600181	Discussions on 6G User Plane	Sharp	discussion	Rel-20	FS_6G_Radio
R2-2600215	HARQ design for unicast communication in NTN	Tejas Network Limited	discussion	Rel-20
R2-2600237	Discussion on required functions and requirements for UP	NEC Corporation	discussion	Rel-20	FS_6G_Radio
R2-2600243	6GR UP Functions and Improvements	CATT	discussion	Rel-20	FS_6G_Radio
R2-2600265	Discussion on UP Functionality for 6G RAN	TCL	discussion	Rel-20	FS_6G_Radio
R2-2600447	Views on 6G User Plane: Functionalities and Processing	Apple	discussion	Rel-20	FS_6G_Radio
R2-2600516	Discussion on Functionality for User Plane	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2600517	Discussion on Random Access procedure	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2600590	Concatenation function for downlink	Samsung	discussion	FS_6G_Radio
R2-2600623	Discussion on RA design in 6GR	ETRI	discussion	Rel-20
R2-2600680	Static Context Header Compression (SCHC) for IoT traffic in 6G 	Orange, Ericsson	discussion	Rel-20	FS_6G_Radio
R2-2600735	6GR L2 functions	InterDigital	discussion	Rel-20	FS_6G_Radio
R2-2600760	Discussion on 6GR user plane protocol aspects	Sony	discussion	Rel-20	FS_6G_Radio
R2-2600845	On single SN based operation	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
R2-2600854	6G User Plane functionalities	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2600895	Further discussions on user plane functionalities	Futurewei	discussion	Rel-20	FS_6G_Radio
R2-2600959	Considerations on functionalities for 6GR UP	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2600992	Discussion on Radio Protocol Architecture – User Plane	Rakuten Mobile, Inc	discussion	Rel-20	Withdrawn
R2-2600993	Discussion on Radio Protocol Architecture – User Plane	Rakuten Mobile, Inc	discussion
R2-2601001	Discussion on Initial access procedure	Google Korea LLC	discussion	FS_6G_Radio
R2-2601041	Considerations for User Plane functionality and design in 6GR	CEWiT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p022`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

Real-time mobile AI traffic 的流量特征与 XR applications 的流量模型相似：具有周期性，但 burst size 高度可变，并有严格的时延要求。

```text
Real-time mobile AI traffic has similar traffic characteristics as the traffic models developed for XR applications:
-	Periodic but has highly variable burst size;
-	Has strict delay requirement.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o001`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

Non-real-time mobile AI traffic 与 legacy eMBB traffic 特征相似，同时具有非周期、突发、UL 负载较高等特点，并使用 HTTP 和 TCP/QUIC、短时连接更多。其 delay budget 灵活，但 latency 对用户体验至关重要。

```text
Non-real-time mobile AI traffic shares similar characteristics with legacy eMBB traffic, but also possess the following distinct features:
-	Aperiodic, bursty, with higher UL load;
-	Use HTTP and TCP/QUIC;
-	Has more short-lived connections than other mobile apps;
-	Has a flexible delay budget, but latency is critical to user experience.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o002`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

R20 mobile AI service 和研究结果可复用于 6G 的场景均考虑上行流量；下行 AI 流量可在 6G 讨论中进一步分析。

```text
Uplink traffic is considered for both R20 mobile AI service and the results of the study could be reused for 6G. The downlink AI traffic could be further analyzed in the 6G discussion.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o003`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

Non-real-time uplink mobile AI traffic 依赖 TCP 或 QUIC/UDP 等可靠传输。

```text
The non-real-time uplink mobile AI traffic relies on reliable transport such as TCP or QUIC/UDP.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o004`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

与传统上行流量传输（如 FTP upload）不同，mobile AI services 主要是交互式服务，时延会直接影响用户体验。

```text
Unlike traditional uplink traffic transmission (e.g., FTP upload), mobile AI services are predominantly interactive, meaning that the latency directly affects user experience.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o005`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

Interactive AI、Agentic AI 和沉浸式流量（包括 conversational XR 实时通信）会产生上行突发、对时延敏感且速率变化的流量模式。从系统效率角度看，其 latency、data arrival time 和 inter-burst time interval 等特性带来挑战。

```text
Interactive AI, Agentic AI and immersive traffic including real-time communication for conversational XR introduce challenging traffic patterns (uplink bursty, delay-sensitive, and of varying bitrate, latency, data arrival time and inter-burst time interval) from a system efficiency perspective.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o006`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

Interactive AI 服务流量主要以上行为主且对时延敏感。其数据会话包含周期性和/或不规则的 UL data bursts，payload size 和 inter-burst interval 可变。

```text
Traffic associated with interactive AI-based services is predominantly uplink-heavy and latency-sensitive, with data sessions characterized by periodic and/or irregular UL data bursts exhibiting variable payload sizes and inter-burst intervals.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o007`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

带有 AI assistance 的 interactive real-time services 会产生 delay-critical uplink data bursts。bounded latency 和 high reliability 是其关键性能要求。

```text
Interactive real-time services with AI assistance generate delay-critical uplink data bursts, for which bounded latency and high reliability are key performance requirements.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o008`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

应优先高效支持具有 low、deterministic latency 的 delay-critical UL bursts。

```text
Efficient support for delay-critical UL bursts with low, determistic latency should be a priority.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o009`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

AI traffic 的传输特性包括突发和非周期流量模式、多模态数据类型、增强可靠性，以及严格的端到端时延和往返时延要求。

```text
Transmission characteristics of AI traffic include burst and non-periodic traffic patterns, multi-modality for diverse data types, enhanced reliability, and strict end-to-end latency and round-trip time requirements.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o010`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

Mobile AI traffic 具有很强的异构性和多模态特征。它无法用单一或静态流量模型描述。

```text
Mobile AI traffic exhibits strong heterogeneity and multi-modalities and cannot be characterized by a single or static traffic model.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o011`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

面向 Rel-18 和 Rel-19 XR traffic 的现有 RAN mechanisms 和 QoS handling，可能无法高效支持以上行为主且多模态的 AI traffic。

```text
Existing RAN mechanisms and QoS handling for Rel-18 and Rel-19 XR traffic may not efficiently support uplink-heavy and multi-modal AI traffic.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o012`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

AI 应用和 transport protocols 的快速演进会导致 AI traffic patterns 难以预测且频繁变化。

```text
The rapid evolution of AI applications and transport protocols leads to unpredictable and frequently changing AI traffic patterns.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o013`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

Agentic AI traffic 需要持续连接，并要求时延和可靠性可预测。这会限制 UE 节能的机会。

```text
Agentic AI traffic requires sustained connectivity with predictable latency and reliability, which limits UE opportunities to save power.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o014`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

Mobile AI services 越来越多地运行于与同一用户关联的异构多设备之间，而非局限于单个 UE。

```text
Mobile AI services increasingly operate across heterogeneous multi-devices associated with the same user, rather than being confined to a single UE.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o015`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

现有系统假设和业务模型主要以 UE 为中心，未能充分体现 multi-device AI services 的特征与需求。

```text
Existing system assumptions and traffic models are largely UE-centric and do not fully capture the characteristics and requirements of multi-device AI services.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o016`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

6G mobile AI 聚焦 AI-native communication mechanisms，包括通过 tokenizer localized deployment 实现 token communication、以 tokens 作为最小传输单元并直接连接下游 AI 应用处理 AI traffic。另一类是基于 AI codec 的 AI source compression traffic service，例如 TR 22.870 中的 Grace。

```text
6G mobile AI focuses on the  AI-native communication mechanisms,  including token communication by tokenizer localized deployment, using tokens as the minimum transmission unit and directly connecting to downstream AI application processing AI traffic. Another type is the AI source compression traffic service based on AI codec, e.g. Grace in TR 22.870.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o017`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

作为 5G-A R20 AI traffic 的 Chatbot 通常使用非常短的数据包，包括 data packets 和 ACK packets。

```text
Chatbot, as a 5G-A R20 AI traffic, typically use very short data packet sizes, including both data packets and ACK packets.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o018`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

TR 22.870 中的 GenAI services 具有 QoS-dynamic 和 delay-sensitive 特性。数据突发可能周期性或非周期性到达，具有高数据速率和变化的数据量。

```text
GenAI services as provided in the TR 22.870 are QoS-dynamic and delay-sensitive. The data burst may arrive periodically or a-periodically with high data rate and varying volumes.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o019`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

评估结果显示，tokenized AI codec traffic 具有 error-tolerance：并非所有 tokens 都需要正确传输。不同 tokens 的 transmission reliability requirement（例如 token error rate）也不同。

```text
The evaluation results given in this contribution and [3][4] show the following features for the (tokenized) AI codec traffic:
	Error-tolerance: Not all tokens need to be transmitted correctly.
	Importance: Different tokens have different transmission reliability requirement (e.g. token error rate)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o020`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

RAN#110 同意，RAN 域内关于 AI traffic characteristics 的工作应集中在一处，由 RAN2 主导，以避免碎片化和重复，并听取 SA4 对 AI traffic characteristics 的反馈。

```text
RAN#110 agreed that RAN is to “ensure that any work on AI traffic characteristics in the RAN domain takes place in one place only (led by RAN2) to avoid fragmentation and duplication with feedback from SA4 on AI traffic characteristics”.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o021`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

Tokenized AI communication 引入独特复杂性。若缺少 SA4 的基础 media framework，可能导致碎片化设计，无法恰当考虑 source files 的分解方式。

```text
Tokenized AI communication introduces unique complexities. Proceeding without the foundational media framework from SA4 could lead to a fragmented design that fails to properly account for how these source files are decomposed.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o022`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

目前尚不清楚 tokenized AI traffic 与 non-tokenized AI traffic 是否具有不同的业务特征。

```text
It is not clear whether tokenized AI traffic and non-tokenized AI traffic have different traffic characteristics.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o023`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

Mobile AI traffic 涵盖 conversational interactions、agentic/task-execution workflows 等多种服务类型；conversational services 可通过 text、image 和 video 等多种模态实现。目前最普遍的是 text-based conversational LLM（chatbot-style）traffic。

```text
Mobile AI traffic spans multiple service types including conversational interactions, agentic/task-execution workflows, etc. Within conversational services, interactions may be realized across multiple modalities, namely, text, image, and video. Among these, text-based conversational LLM (chatbot-style) traffic is currently the most prevalent.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o024`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

在保持复杂度处于合理低水平的同时，构建能忠实体现 conversational、multi-turn GenAI traffic 的业务模型并非易事。

```text
It is a non-trivial task to develop a traffic model that faithfully captures conversational, multi-turn GenAI traffic while keeping the complexity at a reasonably low level.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o025`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

Conversational GenAI traffic model 应与现有 3GPP traffic models 一致，并采用既有统计方法表示 packet inter-arrival times 和 packet/burst sizes 等关键特征。

```text
A traffic model for conversational GenAI traffic should be consistent with existing 3GPP traffic models, leveraging established statistical methods to represent key characteristics such as packet inter-arrival times and packet/burst sizes.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o026`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

为支持忠实且实用的实现，模型宜为单向，同时考虑相反方向；模型应可配置为分别生成 UL 或 DL flows 的 traffic。

```text
To facilitate a faithful and practical implementation, it is desirable for the model to be unidirectional while keeping the opposite direction in consideration, i.e., configurable to generate traffic separately for UL or DL flows.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o027`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

现有 3GPP traffic models（如 FTP models 和 XR model）无法体现 conversational GenAI traffic 的突发、多轮交互模式。

```text
Existing 3GPP traffic models, e.g. FTP models and XR model do not capture the bursty, multi-turn interaction pattern of conversational GenAI traffic.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o028`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

RAN2 确认 mobile AI traffic 可大致分为两类：实时流量（如 conversational audio、augmented reality）和非实时流量（UE 与 server 间交换 text、image、audio/video clips 等对象）。

```text
RAN2 confirm that mobile AI traffic can be broadly categorized into two types:
-	Real-time, e.g. conversational audio, augmented reality, etc;
-	Non-real-time, e.g. exchange of objects such as text, image, audio/video clips, etc between UE and server.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p001`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

RAN2 采用为 XR 开发的 traffic models，作为 real-time mobile AI traffic 的基线。

```text
RAN2 adopt the traffic models developed for XR as the baseline for real-time mobile AI traffic.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p002`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

Non-real-time mobile AI traffic 可建模为使用 HTTP 和 TCP/QUIC 的 eMBB flow，具有更高 UL load、更多短连接和较小但灵活的 delay budget。

```text
Non-real-time mobile AI traffic can be modeled as eMBB flow using HTTP and TCP/QUIC, with higher UL load, more short-lived connections, and small but flexible delay budget.
-	Vivo asks how to determine the real time vs. non-real time and we understand that most traffic is non-real time.   Qualcomm thinks that conversational is real-time.
-	Nokia thinks that there are applications that use both and the real challenge is what the application will do and haven’t been able to categorize and we aren’t sure how to identify what the UL will do.  Qualcomm acknowledges that within the same application the traffic does change from time to time but there are proprietary mechanisms to determine the type of traffic.
-	ATT thinks that in reality the real-time traffic is not real real time they are still best effort traffic.   The traditional eMBB modelling is not sufficient.   Qualcomm explains that translation service has to have a strict delay requirement otherwise it is not very useful.     Theoretically eMBB models can be a good starting point.
-	XR type of traffic would it have congestion control and rate adaptation.   Qualcomm thinks that it depends from use case to use case.
-	Lenovo asks what are the impact of short lived connections in RAN2.   Qualcomm explains that by short it means shorter that the usual connection and one of the areas for us to look at is how to meet the latency of this applications.
Noted
[3 min]
R2-2600147	Discussion on mobile AI traffic for R20	Huawei, HiSilicon, Meta, NTT Docomo, China Unicom, China Telecom, China Mobile, CATT, Futurewei, LG Electronics, OPPO, vivo, Xiaomi	discussion	Rel-20	NR_XR_Ph4-Core
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p003`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

确认 R20 mobile AI 讨论（也可能适用于 6G AI 讨论）的流量特征：聚焦非实时服务的 uplink traffic；application layer packet 可分成多个 packet 并分批到达 AS buffer；mobile AI service 是具有 latency requirements 的交互式服务。

```text
Confirm the following traffic characteristics for R20 mobile AI discussion, which could also be applicable for 6G AI traffic discussion:
(a)	Focus on the uplink traffic for the non-real-time mobile AI service
(b)	Application layer packet for mobile AI could be fragmented to multiple packets and arrive in the AS buffer in multiple batches
(c)	Mobile AI service is interactive service with latency requirements
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p004`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

研究基于上述流量特征的 latency reduction enhancements。讨论指出服务的时延与抖动需求各异，且可讨论 end-to-end latency。

```text
Study the enhancements for latency reduction based on the traffic characteristics above.
-	Nokia is concerned that if we focus on non-real time we will exclude the rest of the market.    Huawei explains that for real time the service cares about latency and jitter but for non-real time it has to be reliable but not as much about latency.   If we do any enhancements we should focus on single modality.   We can’t exclude because even a real time service is doing some non-real time and the RAN should be able to deal with highly dynamic traffic.
-	Apple also agrees that latency is the most important but what we are observing it is not about the air interface but rather the inference in the cloud.   We should understand the type of latency budget and does it really matter from user experience point of view if we reduce air latency by 50%.   Huawei explains that if the segment is very large then the packet has to be segmented and the air interface latency is a big component.  We can also define and discuss the end-to-end latency.
[3 min]
Noted
R2-2600734	Mobile AI transmission characteristics	InterDigital	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p005`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

L2 支持具有不同数据量和 inter-burst interval 的 delay-bound data bursts，并以资源高效方式处理，例如避免过度配置 radio resources。

```text
L2 supports delay-bound data bursts of varying volumes and inter-burst interval in a resource efficient manner (e.g., without over-provisioning of radio resources).
-	Nokia thinks this is a good approach as it doesn’t focus on specific services.
-	Xiaomi asks what is the difference between PDU set in XR and what is the impact and expect the UE to do, provide assistance information.   Interdigital explains that the system can be designed that the burst information is provided so the network is aware of the bursts.
-	Qualcomm asks 1) at which layer is the burst defined and the delay bound and 2) how do you define delay bound budget on objects given how the codecs work.    Interdigital thinks that it is related to service awareness and how we can identify the bursts inside and that can be done via implementation or API (not necessarily by standards means).   For the delay budget we need to understand how the information can be made available.
-	Oppo asks what you have in mind for delay bound.   Interdigital thinks that the delay bound is referring mainly to the UL burst as DL is more to network in the end.
-	Lenovo explains that for XR Rel-19 we provided some bursts information from the network to the gNB.  Are we envisioning something similar.  Itnerdigital explains that it could be one way.
[2 min]
Noted
R2-2600074	Discussion on mobile AI transmission characteristics	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p006`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

提出将 UL data burst size 作为 Rel-20 mobile AI 和 6GR study 的新 traffic characteristic，例如由 UE 向 RAN node 报告。

```text
UL data burst size could be considered as a new traffic characteristic, e.g. reporting from UE to RAN node, for Mobile AI in Rel-20 and 6GR study.
-	Oppo asks why is the burst so important.  Vivo thinks it is related to user experience.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p007`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

记录了 Mobile AI 传输特征供 6GR 研究进一步考虑，包括首个 DL 响应包及每个 AI task session 的 UL 上传和 DL 响应需要低时延，以及 UL/DL 可变的 packet loss tolerance。原文还记录了首包延迟可能来自 application layer，以及 AS 如何识别首包的问题。

```text
The following traffic characteristics for Mobile AI can be further considered for 6GR study:
-	low latency transmission for first response packet, at least for DL
-	low latency transmission for each AI task session for both UL task uploading and DL response
-	varied packet loss tolerance for both DL and UL
-	TCL has the same observation that the first packet is delayed because of application layer and we may have to wait for 10s for application layer so what is the point of optimizing the AS.
-	Xiaomi asks how the AS know that this is a first packet do we need to do deep packet inspection.   Vivo thinks we can discuss more.
Noted
[2 min]
R2-2600389	Discussion on Mobile AI transmission characteristics	Samsung	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p008`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

RAN2 同意研究 Mobile AI 流量的 UL heavy、突发且对时延敏感（同一应用内时延要求可变）、round trip delay 重要，以及同一应用内流量特征高度可变等特征，并分别考虑 UL 和 DL。RAN2 将研究 UL 和 scheduler 支持这些特征/要求所需的机制，向 SA4 通报假设并等待其 tokenized traffic 讨论进展后再进一步提问。

```text
RAN2 is asked to study mechanisms to accommodate burst and non-periodic traffic patterns, multi-modality, enhanced reliability, strict end-to-end latency and round-trip time for AI traffic beyond existing 5G functionalities for XR.
Noted
[2 min]
Discussion
-	Ericsson thinks that at least we should highlight what is different from eMBB.
-	Huawei thinks that we need to look at the aspects that will impact our L2 design and classifying real time vs. non real time.
-	Mediatek thinks it is a difficult task to predict the future but we see some characteristics, like it is UL heavy, bursty and delay bound is difficult to achieve.
-	ZTE thinks that we need to consider UL and DL separately and the way it was proposed in interdigital proposal makes sense and the problem is that they are variable inter-arrival points and we need to understand how the RAN will know.  ZTE asks if the application layers map to different layer protocol and maybe we can identify them.   The real difference is the fast switching.
-	LG also thinks that we should focus on the difference between XR, what’s important is to support the mix of the two services, burstiness is one characteristic and varying delaying bound in the same application and error tolerance mixture.  CMCC agrees
-	ATT has observed that there is a large type of traffic that is best effort.   Some application may be UL heavy and some not.   We cannot say that this looks exactly like XR.
-	Ericsson thinks that we should consider thinks like congestion control and we would go down in rate which wasn’t the case in XR.
-	Apple thinks that round trip delay is important and one thing that is different that time to generate the content is highly variable depending on the task.
-	Vivo thinks we need to study which part for XR will be reused as starting point.   Vivo thikns that companies have different understanding of real time vs. non-real time.
-	Futurewei thinks that the delay is not as bad as XR and the main challenge is UL and aperiodicity and the switching.  The short lived connection is not part of the characteristics.
-	Nokia thinks we have 3 aspects 1) SA4 should tell us what the traffic looks like 2) we need to understand what mechanism we need to deal with AI traffic 3) how we apply this mechanisms and whether we need to go below the QoS flow and the current mechanisms we can’t distinguish.
-	Qualcomm thinks that the round trip delay is not only dependent on RAN2 as it depends on many things.
-	Lenovo thinks that the key question is the UE aware of these characteristics and SA2 may also need to be involved.
-	Ericsson as part of the study would like to understand the benefits from the scheduler perspective.
-	Xiaomi indicates that a single application can have multiple connections, up to 100 connection.   Qualcomm thinks that there is nothing new compared to today.   ZTE thinks that there is no impact and we just see multiple QoS flow.
-	Meta is not sure about the rate adaptation as this is not unique to mobile AI.   Ericsson thinks that variability results from code rate changes.  Mediatek thinks that rate adaptation is important.
-	Nokia thinks UL is more important to start in RAN2 as DL is more a network aspects.  ZTE thinks that this information  needs to be provided to gNB from CN.
-	Huawei thinks SA2 is responsible for QoS requirements (variable characteristics, delay etc) and SA4 is more responsible for codecs (traces that show packet size, delay budget, packet success rate and packet arrival interval).
-	Interdigital thinks that we can wait for SA2 until we have QoS discussion and understand what we want.  Nokia agrees and for SA4 they are in charge of the traffic characterics.
For traffic modelling, RAN2 is responsible for traffic characteristics and will provide the characteristics to RAN1
Agreements on mobile AI
To study AI mobile traffic RAN2 will consider the following
-	UL heavy
-	data bursts and delay bound/sensitive (varying delay requirement within same application)
-	round trip delay is important
-	highly variable traffic characteristics within same applications (e.g. bursts, volume, delay, inter-arrival time, reliability, connection duration, etc).
RAN2 will study what is needed for the UL and scheduler to support such type of characteristics/requirements.   Consider UL and DL separately.
Notify SA4 of our assumptions and ask for feedback if needed
Wait for SA4 to progress tokenized traffic discussion before we ask further questions.
For 5GA R20 discussion, take the agreements above as a baseline.  Focus should be on UL, avoid SA2 impacts and discuss further which requirements should be considered.
[AT133][009][6G UP] LS to SA4 on mobile AI (Nokia)
Intended outcome: agree to LS
Deadline:  Friday
R2-2601340	[DRAFT] LS on Mobile AI Traffic Characteristics	Nokia	LS out	Rel-20	FS_6G_Radio	To:SA4
The LS is approved in R2-2601355
Not treated
R2-2600480	Key Characteristics and Requirements of Mobile AI	Meta, Qualcomm Incorporated, NTT DOCOMO, INC., NVIDIA, Verizon, KDDI	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p009`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

5G-Advanced Rel-20 XR 的重点应是增强 uplink mobile AI traffic，尤其是支持 RAN 中的 AI-traffic awareness。

```text
The 5G-Advanced Rel-20 XR should focus on enhancements for uplink mobile AI traffic, in particular by enabling AI-traffic awareness in RAN.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p010`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

6G QoS 应支持灵活且自适应的 QoS 处理，以高效容纳新的和演进中的 AI traffic 及 protocol behaviors。

```text
The 6G QoS should support flexible and adaptive QoS handling to efficiently accommodate new and evolving AI traffic and protocol behaviors.
[3 min]
Not treated
Tokenized traffic
R2-2600965	Discussion on AI traffic for R20 6G and 5G-A	CMCC, OPPO, Huawei, HiSilicon, Fujitsu	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p011`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

可就上述 ob2 至 ob5 与 SA4（并可能包括 SA1）进行确认。

```text
We can confirm with SA4 (and possibly SA1) about the above ob2 to ob5.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p012`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

RAN2 应研究 TokenCom traffic 的潜在特征，包括 error tolerance、differential importance 和 context relevance。研究可涉及 RAN2 对这些特征的感知及技术优化，例如 Packet/PDU Set/PDU level Importance Indication 或将 error tolerant 映射到 QoS。

```text
RAN2 should study the potential characteristics of TokenCom traffic such as error tolerance, differential importance, and context relevance, which may involve technical optimization of RAN2 by awareness of these characteristics (e.g., Packet/PDU Set/PDU level Importance Indication or error tolerant mapping to QoS).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p013`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

若 RAN2 对 token communication 的 error tolerance、differential importance 和 context relevance 等潜在特征形成结论，可询问 SA4 这些特征是否与其 TR 26.847 研究一致，并沟通 RAN2 的考虑及影响。

```text
If RAN2 can establish conclusions regarding token communication's potential features such as error tolerance, differential importance, and context relevance, we may inquire with SA4 whether these align with their research in TR 26.847, along with RAN2's considerations and implications.
[3 min]
R2-2600446	Views on 6G User Plane: Mobile AI Traffic Characteristics	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p014`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

在 SA4 提供更多与 AI traffic models 相关的反馈之前，RAN2 可以降低 tokenized traffic 研究的优先级。

```text
RAN2 can de-prioritize the study on tokenized traffic, until SA4 provides more feedback related to AI traffic models.
[2 min]
R2-2600206	AI traffic characteristics and coordination between RAN2 and SA4	OPPO, China Telecom, China Unicom, CSCN, CMCC, Huawei, HiSilicon, HONOR, Ofinno, NEC, Transsion Holdings	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p015`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

拟向 SA4 发 LS，说明 RAN2 牵头 RAN domain 的 AI traffic characteristics 研究，并将考虑 SA4 对 AI/ML traffic data 特征及 AI data representation format 的研究。LS 还将说明 NR_XR_Ph4 与 FS_6G_Radio 中 UL/DL 研究一并讨论的状态，并询问 SA4 的研究范围、时间线及 AI service 与 AI data representation format 的关系。

```text
Send an LS (draft LS in the Annex C) to SA4 to inform the followings:
•	The study on the AI traffic characteristics in the RAN domain is led by RAN2.
•	RAN2 will take into account the SA4 study on the characterisation of AI/ML traffic data and AI data representation format, as indicated in the SA4 LS R2-2600042 (S4-252135).
•	Explain the current RAN2 study status that the study of AI traffic characteristics in NR_XR_Ph4 and FS_6G_Radio will be discussed together for both UL and DL.
•	Ask SA4 on the scope and timeline of the study of the AI traffic characteristics, e.g. packet size, packet arrival rate, packet error rate and packet delay budget of AI/ML traffic data and AI data representation format, and the relation between AI service (e.g. AI codec for audio/video/image) and AI data representation format (e.g. token).
[3 min]
R2-2600183	Mobile AI Transmission Characteristics for 6GR and 5G-Adv XR	Sharp	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p016`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

RAN2 将等待 SA4 推进或回复其 6G media aspects 研究后，再开始讨论 tokenized traffic。

```text
RAN2 waits for SA4 progress/reply to conclude its study on media aspects for 6G before starting RAN2 discussions on tokenized traffic.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p017`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

RAN2 询问 SA4：tokenized mobile AI traffic 的 traffic pattern 是否不同于 non-token-based mobile AI traffic。

```text
RAN2 asks SA4 whether a tokenized mobile AI traffic has a different traffic pattern from non-token-based mobile AI traffic.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p018`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

RAN2 询问 SA4：tokenized mobile AI traffic 是否具有不同于 non-token-based mobile AI traffic 的 latency 和 reliability requirements。讨论后决定等待 SA4 推进 tokenized traffic 讨论，再提出进一步问题。

```text
RAN2 asks SA4 whether a tokenized mobile AI traffic has different latency and reliability requirements from non-token-based mobile AI traffic.
[2 min]
Discussion
-	Oppo asks whether SA4 will analyse traffic characteristics of tokenized traffic for error tolerance.
-	Huawei – for non-AI codec whether the legacy traffic model can be applicable and for AI codec whether it has error tolerance and relative packet importance.  Mediatek would be ok but we would need to highlight that from RAN2 perspective we’d like to have this information to drop packets at lower layers.
-	Nokia thinks they are looking into it already so no need to micro manage their work.
-	ZTE thinks that we don’t have the experience for token.  Maybe we can just state that we are not analysing tokens and if there is anything different for tokens let us know.
-	Ericsson thinks that we should have a generic design and not have specific things for tokenized.  Our expectations is that the traffic characteristics we agreed apply to everything.
-	Interdigital agrees with Nokia  and we shouldn’t ask anything for now as it may delay response for other things.   Qualcomm, LG and Xiaomi also agree, SA4 can tell us if they have something.
Wait for SA4 to progress tokenized traffic discussion before we ask further questions.
Not treated
Traffic model
R2-2600890	A Model for Mobile AI Traffic in 6G Networks	AT&T	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p019`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

将 text-based conversational GenAI traffic model 作为 6G AI/ML mobile traffic evaluations 的起点。

```text
Consider text-based conversational GenAI traffic model as a starting point for 6G AI/ML mobile traffic evaluations
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p020`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

定义 conversational GenAI mobile AI traffic model，采用单向 UL/DL 形式，分别规定 UL 和 DL traffic profiles，并由共享的 session/turn process 管理。

```text
Define a conversational GenAI model for mobile AI traffic in a unidirectional UL/DL form, where UL and DL traffic profiles are specified separately but governed by a shared session/turn process
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p021`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

conversational GenAI model 由 mean turns/session、mean think time、prompt 和 response size distributions、first-byte delay distribution，以及 streaming chunk/cadence parameters 参数化。

```text
The conversational GenAI model is parameterized with the following parameters: mean turns/session, mean think time, prompt size distribution, response size distribution, first-byte delay distribution, and streaming chunk/cadence parameters.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p022`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

conversational GenAI model 的 baseline evaluations 使用 geometric、exponential、shifted lognormal/lognormal with truncation 等默认统计分布族，参数保持可配置。

```text
Default statistical distribution families, e.g., geometric, exponential, shifted lognormal/lognormal with truncation, are used for baseline evaluations of conversational GenAI model, with parameters left configurable.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p023`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

模型可选地增加 multimodal extension，并沿用相同的 session/turn framework。音频和视频建模为分块字节流，包括 audio frames 和 video segments。

```text
Optionally, a multimodal extension can be added to the model. The multimodal extension reuses the same session/turn framework, with audio/video modeled as chunked byte streams (audio frames, video segments).
[4 min]
R2-2600102	Consideration on Mobile AI Traffic characteristics	Xiaomi	discussion	Rel-20
R2-2600148	Overview of mobile AI transmission characteristics	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
R2-2600153	Discussion on Mobile AI Transmission Characteristics and Required Coordination with SA2 and SA4	Pengcheng Laboratory	discussion
R2-2600164	Mobile AI traffic characteristics	ZTE Corporation, Sanechips	discussion
R2-2600183	Mobile AI Transmission Characteristics for 6GR and 5G-Adv XR	Sharp	discussion	Rel-20	FS_6G_Radio
R2-2600242	Mobile AI Traffic Characteristics	CATT	discussion	Rel-20	FS_6G_Radio
R2-2600315	Mobile AI Transmissions	Nokia	discussion	Rel-20	FS_6G_Radio
R2-2600347	Discussion on Mobile AI transmission characteristics	Fujitsu	discussion	Rel-20	FS_6G_Radio
R2-2600389	Discussion on Mobile AI transmission characteristics	Samsung	discussion	Rel-20
R2-2600409	Initial Considerations to Support User Plane Function in the AI-native RAN Architecture	Hanbat National University	discussion
R2-2600480	Key Characteristics and Requirements of Mobile AI	Meta, Qualcomm Incorporated, NTT DOCOMO, INC., NVIDIA, Verizon, KDDI	discussion
R2-2600515	Discussion on mobile AI transmission characteristics	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2600552	Discussion on Mobile AI Transmission Characteristics	NEC	discussion	Rel-20	FS_6G_Radio
R2-2600673	Discussion on the tokenize traffic characterestics	Spreadtrum, UNISOC	discussion	Rel-20
R2-2600676	Mobile AI transmission characteristics	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20
R2-2600685	Discussion on Mobile AI transmission characteristics	China Telecom	discussion
R2-2600745	Discussion on mobile AI transmission characteristics	Lenovo	discussion	Rel-20
R2-2600757	Mobile AI Transmission Characteristics	Panasonic	discussion	Rel-20
=> Revised in R2-2601302
R2-2601302	Mobile AI Transmission Characteristics	Panasonic	discussion	Rel-20
R2-2600853	6G AI Traffic Characteristics	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2600885	Discussion on mobile AI traffic characteristics	Ericsson	discussion	Rel-20	FS_6G_Radio
R2-2600890	A Model for Mobile AI Traffic in 6G Networks	AT&T	discussion	FS_6G_Radio
R2-2600925	Mobile AI traffic characteristics	NVIDIA	discussion	Rel-20	Late
R2-2600978	Discussion on AI traffic characteristics	NTT DOCOMO, INC.	discussion
R2-2601005	Discussion on Mobile AI Transmission Characteristics	TCL	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p024`

### [6G/Rel-20 RAN2#133] `agreement` 10.3.1.4 Others

对于 UL 中触发更快 ARQ procedure，RAN2 倾向于通过 DCI 显式指示特定 HARQ process failure；收到指示后，UE 触发 ARQ retransmission，且预期不再继续该 HARQ process 的 retransmissions。ACK 是否有用及其他 RAN2 相关方面仍待讨论，内容标记为 Not treated。

```text
From RAN2 point of view, for triggering the faster ARQ procedure in UL, an explicit indication in DCI is preferred for a given HARQ process failure.   It is up to RAN1 how this is signalled.
Upon reception of indication of HARQ process failure, the UE triggers ARQ retransmission.  The UE is not expected to continue the HARQ retransmissions after this indication is received.
FFS whether ACK can be useful from RAN2 perspective and any other RAN2 related aspects
Not treated
Content of ARQ retransmission
R2-2600057	Fast ARQ Retransmissions in 6G	Samsung	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-a001`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.4 Others

在 DL 中，PUCCH errors 和 missed DCIs 会导致 DL RLC errors，UE 需通过 RLC Status report 纠正，并触发 gNB 的 RLC retransmission。

```text
In DL, PUCCH errors and missed DCIs contribute to DL RLC errors requiring UE to correct using an RLC Status report, triggering an RLC retransmission at gNB.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-o001`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.4 Others

HARQ-assisted DL ARQ 有望显著降低 latency，同时不增加 RLC retransmission rate。

```text
HARQ-assisted DL ARQ has the potential of significantly reducing latency without increasing RLC retransmission rate.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-o002`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.4 Others

RRC 配置后，Type 1 CG 不能动态修改、停用或重新激活，除非进行 RRC reconfiguration。

```text
Once RRC-configured,Type 1 CG cannot be dynamically modified, deactivated or re-activated without RRC reconfiguration
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-o003`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.4 Others

Type 2 CG 不能在 RRC configuration 后自动激活，需要显式的 DCI-based activation。

```text
Type 2 CG cannot be automatically activated upon RRC configuration and relies on the explicit DCI-based activation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-o004`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.4 Others

由于 SR 延迟和 CG Confirmation MAC CE，Type 2 CG adjustments 对动态突发流量的时间效率不足。

```text
Due to the SR delay and the CG Confirmation MAC CE, Type 2 CG adjustments are not sufficiently time-effective for dynamic, bursty traffic.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-o005`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

为在 UL 触发更快的 ARQ procedure，当 HARQ process 的 NDI toggled 时，gNB 在 UL grant 的 DCI 中加入一位 indication。该提案被记为 Noted。

```text
For triggering the faster ARQ procedure in UL, the gNB includes a one-bit indication in the DCI for UL grant when NDI is toggled for the HARQ process.
[2 mins]
Noted
R2-2600246	Discussion on L2 Retransmission and CG	CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p001`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

RAN2 提议向 RAN1 发 LS，询问 UE 获取 UL HARQ process HARQ status 的较优方案：根据 retransmission grant 推断 DL HARQ feedback result，或引入显式 DL HARQ feedback。该提案被记为 Noted。

```text
RAN2 sends LS to RAN1 to check which options is better for UE to acquire the HARQ status for UL HARQ process:
	Option 1: UE deduces the DL HARQ feedback result for UL HARQ process based on the retransmission grant.
	Option 2: Introduce explicit DL HARQ feedback for UL HARQ process.
[2 mins]
Noted
R2-2600450	Views on 6G User Plane: HARQ-ARQ Coordination, LCP and CG	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p002`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

提议向 RAN1 发 LS，说明 UL 需要显式 HARQ process status feedback；讨论中对采用 DCI 或 MAC CE、是否在 RAN2 先研究以及 indication 的时机存在不同意见。

```text
RAN2 should send a LS to RAN1, to notify the need of explicit HARQ process status feedback for UL.
[1 mins]
Noted
Discussion
-	Sony indicates that this 1 bit is expensive as this doesn’t happen very often.  We can try it with MAC CE as it is even triggered and doesn’t always have to be included.  ZTE thinks that it would generate even more signaling as there are headers etc.
-	Interdigital ask why it is linked to NDI toggled as it would be beneficial to know before as sometimes the next new grant/transmission may be delayed.   ZTE explains that we didn’t see a need to signal earlier.    Nokia also doesn’t think we need to link to NDI, it should be good to just indicate the final state.
-	Huawei think we should DCI but we shouldn’t do the final design for RAN1, just tell them our requirements, to know the status.
-	Vivo thinks we shouldn’t send an LS to RAN1, but we should do the study in RAN2 first.
-	Futurewei thinks we should decide RAN1 or MAC.
-	NEC thinks that we would need to understand what information needs to be provided and be careful with how many bits are needed.
-	Samsung, Ericsson and Docomo prefer DCI and the indication when the HARQ process is completed.
-	Docomo asks ZTE what happens when there is no data.   ZTE explains that the network knows that the HARQ has failed so it will provide a new grant so the UE can retransmit the lost packets using that grant.
-	Offino thinks both should studied.
-	Lenovo thinks that there should be no time issue if the indication is with the UL grant NDI toggle.
-
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p003`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

UE 收到 UL HARQ process unsuccessful termination 信息后，触发该 HARQ process 对应 MAC PDU 中所含 RLC SDU 或 RLC SDU segment 的 RLC retransmission。

```text
Upon receiving information about the unsuccessful termination of an UL HARQ process, UE triggers RLC retransmission of RLC SDU(s)/RLC SDU segment(s) included in the MAC PDU associated with the HARQ process.
[3 mins]
R2-2600167	MAC layer enhancements for 6G	ZTE Corporation, Sanechips	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p004`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

Fast ARQ 仅适用于需要 ARQ 的 MAC SDUs（即 AM mode SDUs），且应支持对这些 MAC SDUs 进行 (Re-)Segmentation。另提出研究适用于混合类型 packet flow 的 per-packet transmission mode，包括按 packet 决定是否重传，以及单个 DRB 同时支持 lossless 和 lossy transmission。

```text
Fast ARQ mechanism is applicable only to MAC SDUs that are subject to ARQ (i.e. AM mode SDUs) and (Re-)Segmentation should be possible for these MAC SDUs (similar to SDUs subject to normal ARQ)
[2 mins]
R2-2600975	Discussion on L2 ARQ retransmission and MAC CE re-trigger	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
Proposal 4	Study per-packet transmission mode suitable for mixed type packet flow, e.g.,
a. Whether to perform retransmission is determined per packet basis
b. Single DRB supports both lossless and lossy transmission
[2 mins]
R2-2600368	Other aspects of UP design	Nokia	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p005`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

用于跟踪 RLC retransmission 的 LCHs 或 PDUs 的方案应考虑内存需求影响。另有提案指出，UE 收到指示特定 HARQ process 的 UL ARQ retransmission request 的 L1 DCI 后，可在适用时由 UE 实现确定正确的 ARQ entities 并触发重传。

```text
The solutions for tracking LCHs or PDUs for RLC retransmission should consider the impact to memory requirement.
[2 mins]
R2-2600431	Faster ARQ and HARQ	Ericsson	discussion	Rel-20
Proposal 3	Upon receiving the L1 DCI indicating an UL ARQ retransmission request for a given HARQ process, the UE up to its implementation, if applicable, and finds the correct ARQ entities for triggering retransmission.
[2 mins]
Downlink Fast ARQ
R2-2600078	Considerations on faster ARQ retransmission and CG scheduling	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p006`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

RAN2 同意在发送端基于 HARQ process status 进行更快的 DL ARQ retransmissions。

```text
RAN2 agree to have faster DL ARQ retransmissions at the transmitter side based on HARQ process status.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p007`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

对于 DL data transmission，当 UE 检测到潜在 HARQ feedback error 时，UE 向 RAN node 提供 HARQ process status 有益；例如，UE 在 PUCCH 发送 HARQ NACK 后，针对同一 HARQ process 收到 HARQ new transmission scheduling。该提案被记为 Noted。

```text
For DL data transmission, HARQ process status from UE to RAN node is beneficial when potential HARQ feedback error is detected by UE, i.e., in case of HARQ new transmission scheduling is received on certain HARQ process after HARQ NACK was sent in PUCCH.
[2 mins]
Noted
R2-2600428	Discussion on HARQ/ARQ protocol design 	Lenovo	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p008`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

提议 RAN2 同意支持基于 HARQ feedback information（ACK/NACK）和 UE assistance information，在 DL 发送端快速触发 ARQ retransmissions 的机制；UE assistance information 可包括指示中止后续 HARQ Retx(s) 并触发 RLC re(tx)。该提案被记为 Noted。

```text
RAN2 to agree on supporting mechanisms for fast triggered ARQ retransmissions at the transmitter side for DL based on HARQ feedback information (ACK/NACK) and UE assistance information, e.g. indication to abort further HARQ Retx(s) and trigger RLC re(tx).
[2 mins]
Noted
R2-2600142	Discussion on HARQ, ARQ and RLC	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p009`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

RAN2 将发送 LS，请求 RAN1 研究 UE 如何以低时延检测 HARQ Nack-to-Ack error 和 DTX-to-Ack error。

```text
On Downlink, RAN2 to send an LS requesting RAN1 to investigate how the UE can best detect the following events with low latency:
-	HARQ Nack-to-Ack error
-	DTX-to-Ack error, i.e., due to missing DL DCI, UE does not transmit HARQ feedback while network detects DTX as ACK.
[3 mins]
Noted
R2-2600246	Discussion on L2 Retransmission and CG	CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p010`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

DL HARQ process 可基于 UL HARQ feedback 执行更快的 ARQ retransmission。具体细节留给 network implementation。

```text
For DL HARQ process, faster ARQ retransmission can be performed based on UL HARQ feedback. The details can be left to network implementation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p011`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

已认定 DL fast ARQ 的相关问题是 HARQ Nack-to-Ack error，HARQ 可靠性很重要，但属于 RAN1 design decision。支持 DL fast ARQ；RAN2 可研究如何降低 ARQ latency、提高 reliability，例如在 RLC level。

```text
For the fast ARQ retransmission based on HARQ, no optimization is needed to handle the HARQ ACK/NACK error or DTX.
[2 mins]
Noted
Discussion
-	Ericsson and Panasonic thinks thinks that CATTs proposal makes sense as the network can use the feedback to determine by implementation.  Panasonic also doesn’t understand how the UE determines the error.
-	Apple believes the latency applies to both UL and DL and there is an ack to nack error which will make the gNB to interpret the results incorrectly so it is worth looking in RAN2 first.
-	Nokia thinks its good to study further and the key is if the UE can detect the error.
-	ZTE two cases, packet successfully decoded and when it wants to move on because it has exceeded the PDB, there is no way for the UE to know why the gNB moved on.   The NW can triggered the HARQ retransmission whenever it wants, so there is not RAN2 reasons for this.   LG agrees as the UE doesn’t know why the network dropped the packet.  Huawei agrees too and the robustness of HARQ robustness is RAN1 issue.
-	Xiaomi doesn’t know the gNB can detect the error.  The error can happen even in the first occasion.
-	Mediatek thinks there is benefit for both UL and DL but for DL the network implementation can handle it.   What’s important is that the HARQ feedback is reliable.
-	Ericsson understands agreement doesn’t preclude any discussions in RAN2 on UCI on MAC.   Companies understanding is that RAN1 will make the decision but if RAN2 is required to discuss anything related to feedback on L2 it may still do so.
Agreements on DL fast ARQ
1	The identified issue is HARQ Nack-to-Ack error.    Common understanding reliability of HARQ is important for fast ARQ from RAN2 point of view.  However, this is a RAN1 design decision.
2	Fast ARQ for DL is supported (e.g. nw can triggered ARQ retransmission when it wants).    RAN2 can study if and how to reduce ARQ latency and improve reliability in RAN2 (e.g. at RLC level).
Configured Grants
CG Types
R2-2600152	Discussion on fast ARQ and configured grant	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p012`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

研究 configured grant 时，将 NR CG Type 1 和 Type 2 都作为起点。

```text
For configured grant, consider both NR CG Type 1 and Type 2 as the starting point.
[2 mins]
Noted
R2-2600368	Other aspects of UP design	Nokia	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p013`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

研究统一的 CG framework，以支持 pre-configuration、activation/deactivation 和 modification。

```text
Study a unified CG framework that allows pre-configuration, activation/deactivation and modification.
[2 mins]
Noted
R2-2600078	Considerations on faster ARQ retransmission and CG scheduling	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p014`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

RAN2 至少将 Type 1 和 Type 2 CG 作为 6GR Day-1 支持 periodic traffic 的起点；basic CG schemes 的增强需有 RAN1 参与。后续会议应聚焦现有 CG 的问题及满足 6G requirements 所需的功能。

```text
RAN2 assumes both Type 1 and Type 2 CG can be considered as starting points in 6GR Day-1 at least to support the periodic traffic. RAN1 should be involved in any enhancement of the basic CG schemes.
[2 mins]
Noted
Discussion
-	CATT thinks that it is hard to design a uniform framework without first understanding scenarios.
-	Interdigital thinks we should agree on the functionalities for CG and then address the details later.  Sonny agrees.
-	Samsung agrees that we should study CG1 and CG2 types and what enhancements are needed.  We should discuss the functionalities required first.
-	Oppo asks if the intention whether we would add new DCI formats.  Nokia thinks that is a RAN1 and we had a DCI format modification for type 2 so we can just use the same for both.
-	LG thinks that the only difference is the modification so it is time to consider a unified framework.
-	Vivo asks if CG type 1 also needs to have an activation.   Nokia thinks that we should at least support the 5G functionality and see if we can do better.
-	Mediatek thinks that type 1 and 2 are already kind of unified.
-	Qualcomm thinks that we should have multi config and multi pusch as well.
-	Apple thinks that the priority should be what is wrong with CG and what we need for 6G.
For next meetings companies should focus on the issues with the current CG and the functionality required to meet the 6G requirements.
Not treated
CG Enhancements
R2-2600152	Discussion on fast ARQ and configured grant	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
Observation 4-1:Legacy CG resource  allocation is  not  suitable  to  support  the  realistic  UL traffic envisioned for 6GR without compromising on resource and energy efficiency.
Observation 4-2:Providing  CG scheduling  related  parameters  to  NW from UE side  based  on  its knowledge of the UL traffic is beneficial adapt to unpredictable traffic while avoiding over provisioning or under provisioning of CG resources.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p015`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

应研究 adaptive configured grant resource allocation mechanism，根据 RAN1 已同意的新 mixed traffic model，使预分配资源更适应 UL service requirement。

```text
Adaptive configured grant resource allocation mechanism should be studied to better adapt the pre-allocated resources to UL service requirement based on the new mixed traffic model agreed in RAN1.
[2 mins]
R2-2600450	Views on 6G User Plane: HARQ-ARQ Coordination, LCP and CG	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p016`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

6GR 的 configured grant 可考虑以 Rel-16 version of CG 为基线，每个 serving cell 可配置多个 CG configurations。

```text
For configured grant in 6GR, Rel-16 version of CG may be considered as the baseline, where multiple CG configurations can be configured per serving cell.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p017`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

RAN2 可研究如何提高 CG 效率，例如让 CG 以 “on-demand” basis 运行。

```text
RAN2 can study to see if CG can be made more efficient, e.g. the CG may operate in an “on-demand” basis.
[2 mins]
R2-2600962	Considerations on fast ARQ and CG for 6GR UP	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p018`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

RAN2 应研究 Type-2 CG fast adjustment，以应对 SR 和 CG confirmation MAC CE 所导致的影响。

```text
RAN2 should study the Type-2 CG fast adjustment to address the mitigate caused by SR and CG confirmation MAC CE.
[2 mins]
R2-2600656	6G HARQ/ARQ and CG	NEC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p019`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

RAN2 以 type2 CG 为起点，考虑进一步增强，以更好适应不同 packet size 和 packet periodicity。

```text
RAN2 takes type2 CG as start point and consider further enhancement for better adaption over varying packet size and packet periodicity
[2 mins]
R2-2600182	Retransmission and Periodic Data Support in 6GR	Sharp	discussion	Rel-20	FS_6G_Radio
R2-2600210	Consideration on fast ARQ and head-of-line issue	OPPO	discussion	Rel-20	FS_6G_Radio
R2-2600266	Discussion on Re-transmissions for 6G RAN	TCL	discussion	Rel-20	FS_6G_Radio
R2-2600312	Discussion on Faster ARQ for 6G	KT Corp.	discussion	Rel-20	FS_6G_Radio
R2-2600351	Discussion on L2 retransmission enhancements in 6G	Fujitsu	discussion	Rel-20	FS_6G_Radio
R2-2600520	Discussion on faster ARQ retransmissions and CG mechanism	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2600621	Discussion on HARQ and ARQ	NTT DOCOMO INC..	discussion
R2-2600625	Discussion on fast ARQ retransmission	ETRI	discussion	Rel-20
R2-2600659	Discussion on (re-)transmission in 6G	Spreadtrum, UNISOC	discussion	Rel-20
R2-2600738	HARQ, ARQ, and scheduling grants	InterDigital	discussion	Rel-20	FS_6G_Radio
R2-2600769	Pre-Configured UL Resources for 6G	Sony	discussion	Rel-20	FS_6G_Radio
R2-2600770	HARQ and ARQ for fast data recovery in 6G	Sony	discussion	Rel-20	FS_6G_Radio
R2-2600772	Discussion on retransmission enhancements for 6G	Panasonic	discussion	Rel-20
R2-2600844	On HARQ triggered L2 retransmissions	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
R2-2600850	UL HARQ- and CSI feedback in 6G	Ericsson, MediaTek Inc., Verizon, Charter Communications Inc., Turkcell	discussion	Rel-20	FS_6G_Radio
R2-2600857	6G ARQ/HARQ and CG/SPS	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2601044	Retransmission enhancements for 6GR	CEWiT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p020`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.1 Functionality for User Plane and related functional requirements

大多数 NR UP functions 被认为是连接 L2 以上 upper layers 与 physical layer 所必需的。

```text
Most of NR UP functions are considered essential to connect between upper layers above L2 and physical layer.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o001`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.1 Functionality for User Plane and related functional requirements

NR UP protocol stack 存在多组重复功能。

```text
NR UP protocol stack has multiple sets of duplicated functions.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o002`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.1 Functionality for User Plane and related functional requirements

考虑到 6GR 将支持的 service types，radio bearer 和 logical channel 仍可能有助于满足 latency、error recovery 等特定要求。

```text
Considering the service types will be supported by 6GR, radio bearer and logical channel could still be helpful to fulfil the specific requirements like latency, error recovery, etc.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o003`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.1 Functionality for User Plane and related functional requirements

NR 中引入了多种 compression mechanisms，包括 ROHC、UDC 和 EHC；这些机制虽独立引入，但具有共同点。

```text
In NR, multiple compression mechanisms, i.e., ROHC, UDC, EHC. ROHC were introduced independently, but those are all compression mechanisms which have commonalities.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o004`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.1 Functionality for User Plane and related functional requirements

在 5G 中，每个 PDCP SDU 生成的 MAC-I 会带来额外 signalling overhead，并占用 UE processing capability，从而影响 UE transmission bit rate。

```text
In 5G, the MAC-I generated for each PDCP SDU causes extra signalling overheads and UE processing capability (i.e. impacting the UE’s transmission bit rate).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o005`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.1 Functionality for User Plane and related functional requirements

Data concatenation 可能导致大小可变、bit positions 不固定的 headers，不利于硬件处理。

```text
Data concatenation can lead to variable-sized headers with varying bit positions that are not hardware-processing friendly.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o006`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.1 Functionality for User Plane and related functional requirements

Data concatenation 可能增加 segment handling 和 reassembly delays。

```text
Data concatenation can lead to increased segment handling and reassembly delays
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o007`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.1 Functionality for User Plane and related functional requirements

同一 SN 用于 ARQ 与 (re-)segmentation 功能，以及 security 与 re-ordering 功能，有利于降低 L2 overhead 并提升效率。

```text
Same SN used for both ARQ & (re-)segmentation functions and security & re-ordering functions is beneficial for L2 overhead reduction and efficiency improvement.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o008`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.1 Functionality for User Plane and related functional requirements

在 NR 中，单个 code block (CB) 失败可能延迟其他 CB 中 PDU 的交付；在 TB 大得多的 6G 中，这一问题可能更严重。

```text
In NR, failure of a single code block (CB) can delay the delivery of PDUs in other CBs. This problem can be more serious in 6G with its much larger TBs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o009`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.1 Functionality for User Plane and related functional requirements

在 TB 中包含关于 MAC CEs 或 MAC subPDUs 的 metadata，可以帮助接收端加快 TB 处理。

```text
Including metadata about MAC CEs or MAC subPDUs in a TB can help the receiver speed up processing of the TB.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o010`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.1 Functionality for User Plane and related functional requirements

6G 中的 MAC CEs 可以采用更结构化的设计，以实现高效处理并满足预期更严格的 6G timing requirements。

```text
MAC CEs in 6G can be designed in a more structured way to enable efficient processing and meet the stricter timing requirements expected in 6G.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o011`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.1 Functionality for User Plane and related functional requirements

NR UP headers 的长度可变，尤其是在 MAC 和 RLC 中，这不利于硬件实现。

```text
NR UP headers are variable size especially in MAC and RLC which is not hardware-friendly.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o012`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.1 Functionality for User Plane and related functional requirements

导致 header length 动态变化的因素包括 RLC 中 segmentation 的有无，以及 MAC 中的 LCID 和 L field。

```text
The factors that cause the header length to change dynamically are as follows: the presence or absence of segmentation in RLC, and the LCID and L field in MAC.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o013`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.1 Functionality for User Plane and related functional requirements

统一 header length 的一种简单方式是始终采用较长的 header；但应避免这样做，因为这会增大 Message 3 等消息的尺寸，而这些消息是 coverage bottlenecks。

```text
A simple way to unify header lengths is to always adopt the longer header; however, this should be avoided as it would increase the size of messages such as Message 3, which are coverage bottlenecks.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o014`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.1 Functionality for User Plane and related functional requirements

在 NR 中，通过 RACH partitioning 提前指示 feature combinations 会导致 RACH resources 的利用非常低效。

```text
In NR, early indication of feature combinations through RACH partitioning leads to very inefficient use of RACH resources.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o015`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.1 Functionality for User Plane and related functional requirements

在 NR 中，RACH resources 难以适应接入负载的短期变化，常导致高争用和接入失败。

```text
In NR, RACH resources do not adapt well to short-term variations in access load, often resulting in high level of contention and access failures.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o016`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

6GR 应在 UP protocol stack 的高层支持 QoS flows（或由 SA2 设计的 sub flows）到 UL 和 DL radio bearer 的映射，以及 security protection、data PDU 的 sequence numbering、ROHC Header and Data compression、延迟 PDU 的 timer-based discard 和 duplicate detection and discard。原文还指出 Header compression 应根据 plenary 暂缓，data compression 是 UDC 且尚未商业化；ZTE 认为 data compression 也可适用于 DL，且不意味着需要对所有内容启用。

```text
6GR shall support the following functionality in a higher layer(s) in UP protocol stack:
-	Mapping between QoS flows (or sub flows if/as designed by SA2) to a radio bearer in UL and DL
-	Security protection, Sequence numbering of data PDUs, ROHC Header and Data compression, and timer-based discard for delayed PDUs
-	Header compression should be parked based on plenary and data compression is UDC and it is not commercialized.    Maybe there are some compression for those.  ZTE thinks that data compression can also be applicable to DL.  Also it doesn’t mean we need to enable this for everything.
-	Duplicate detection and discard
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p001`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

6GR 应在 UP 协议栈的低层支持按物理层 grant 大小分段、逻辑信道优先级处理与复用、调度请求，以及带或不带软合并的传输和重传（HARQ、ARQ）。

```text
6GR shall support the following functionality in a lower layer(s) in UP protocol stack:
-	Segmentation of packets based on physical layer grant size
-	Logical channel prioritization and multiplexing, Scheduling requests (SR/BSR like functionality)
-	Transmission and retransmission with and without soft combining (HARQ and ARQ)
[2 min]
Noted
R2-2508217	6GR User Plane Functionality	Sharp	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p002`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

列出了被视为 6GR UP 必需基本功能的 NR UP 功能，包括数据传输、序列编号、重复检测与丢弃、PDU 丢弃、重传、分段与重组、MAC 复用与解复用、优先级处理、压缩、安全协议及有序和无序交付。

```text
The following NR UP functions are considered as required essential 6GR UP functions:
- Data transfer
- Sequence numbering
- Duplicate discarding/duplicate detection
- PDU discard
- Retransmission (HARQ, ARQ)
- Segmentation/reassembly
- MAC multiplexing and de-multiplexing
- Priority handling (between UE, between LCHs/RBs, between resources, etc)
- Compression (ROHC, UDC, EHC)
- Security protocol (both integrity protection and ciphering)
- In-order delivery (including reordering) and out-of-order delivery
[2 min]
Noted
R2-2508233	6GR UP Functions	CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p003`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

提出 6G Day1 至少应支持所列 UP 功能，具体支持方式可进一步研究。清单涵盖 QoS flow 与 DRB 映射、SN 维护、压缩、安全、丢弃、重复处理、交付顺序处理、重分段、L2 ARQ、复用、调度信息报告、HARQ 和 LCP。

```text
At least the following UP functions should be supported in 6G Day1 and how to support these functions can be further studied:
-	Mapping/remapping between QoS flow(s) and a DRB,
-	SN maintenance,
-	Header compression and decompression (ROHC and EHC),
-	UDC,
-	AS security ((de)ciphering and integrity protection/integrity verification),
-	SDU discard,
-	L2 PDU duplication,
-	Reordering and in-order delivery,
-	Out-of-order delivery,
-	Duplication discarding/detection,
-	(Re)segmentation,
-	L2 ARQ retransmission,
-	(De)multiplexing,
-	Scheduling information report,
-	HARQ,
-	LCP.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p004`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

提出 QoS（重）映射、SN 维护、重复丢弃、（重）分段和（解）复用等功能应在 UP 中支持且不可禁用；并列出 UP 至少支持的数据传输、安全、序列编号、头压缩、SDU 丢弃、重复检测与丢弃、有序和无序交付、重排序、分段与重组、逻辑信道优先级处理与复用、调度信息报告及传输和重传。

```text
The functions should be supported in UP and cannot be disabled including: QoS (re)mapping, SN maintenance, duplication discarding, (re)segmentation, and (de)multiplexing.
[2 min]
Noted
UP will at least support the following functionalities
Data transfer
Mapping of QoS flow(s) (or what SA2 may come up with) to a radio bearer in UL and DL
Security protection (in coordination with SA3), Sequence numbering, Header compression (e.g. ROHC, etc based on plenary discussion),
SDU discard
Duplicate detection at the receiver side and discard
In-order and out-of-order delivery.  Reordering.
(re)Segmentation of packets and re-assembly
Logical channel prioritization and multiplexing/demultiplexing
Scheduling information reporting
Transmission and retransmission (e.g. HARQ and ARQ like)
NOTE: Details of these functionalities will be further discussed later and the list is not exclusive
NOTE: functions related to RAN1 aspects will be added and considered later on.
Concatenation:
R2-2508105	Discussion on the 6G user plane features	OPPO	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p005`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

提出可将多个 PDCP SDU 拼接为单个 PDCP PDU。讨论涉及目标服务、硬件适配、grant 预测、MAC-I 开销，以及拼接后再分段可能带来的时延和内存缓冲需求。

```text
Multiple PDCP SDUs can be concatenated to a single PDCP PDU.
[2 min]
-	Xiaomi asks what specific service you are targeting and wonders if this is hardware friendly and the UE has to predict the grant.   Oppo is referring to many small packets so we have to consider the overhead of MAC-I.  The UE doesn’t need to predict anything and the number of packets to be concatenated can be pre-configured.  Qualcomm ask then does it mean that it will be concatenated and then segmented.   MEdiatek thinks that this is a big problem, latency performance, memory buffer requirements etc.
Noted
R2-2508124	On essential functionality for 6G data transfer	MediaTek UK	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p006`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

提出 6G 用户面协议栈的数据处理单位仍保持为逐包粒度，与 NR 相同。

```text
As in NR, the unit of data handling in the 6G user plane stack remains at a per-packet granularity.
[2 min]
Noted
R2-2508310	UP functionalities and requirements	Nokia, Nokia Shanghai Bell	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p007`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

建议在高数据率、短到达间隔或时延要求宽松等有明确收益的场景研究 6GR packet concatenation，同时尽量减少对低层运行的约束并保留 QoS 和优先级隔离。还提出研究发送侧逐包预处理；讨论记录了拼接的处理开销、时延、硬件加速器利用及安全相关考量，并决定待 UP 协议和安全理解进一步完善后再讨论拼接。

```text
For scenarios with clear gains (e.g. high-rate, short inter-arrival, or relaxed latency traffics) investigate packet concatenation in 6GR that minimises operational constraints on lower layers and preserve QoS/prioritisation separation.
[2 min]
Noted
R2-2508472	User Plane Function Assessment in 6GR	Ericsson	discussion	Rel-20	FS_6G_Radio
Observation 3	Pre-processing capability on transmitter side is essential to achieve the 6G target of minimizing processing and memory transfers.
Observation 4	Grouping of packets for joint pre-processing leads to delays and cannot efficiently utilize hardware accelerators optimized for typical MTU sizes.
Proposal 5	When studying protocol functionality in 6G, also consider implementations based on per-packet pre-processing on transmitter side.
[2 min]
Noted
Discussion
-	Lenovo thinks that it makes sense only in some scenarios, for example when you have huge chunks of packets at the same time and you need to predict what the grant is and it doesn’t come for free.   Nokia also thinks good to study but there are things to take into account
-	Docomo is open to discuss but agree with Mediatek and Ericsson.  Ciphering and integrity protection takes a lot of processing resourcing.
-	Apple thinks that concatenation is very useful especially when there are all these small packets that come to UE buffers we need to process them each individually and this is a lot of overhead and processing.
-	CMCC and Vivo supports the concatenation
-	Qualcomm has the same view as Mediatek, and points out that this is dependent on integrity protection if done the same way as 5G and this might change.
-	Samsung thinks that there is a way to have fix header with concatenation and the main benefit is to minimize the number of L2 headers.  Samsung thinks that we are only using a portion of the hardware accelerator.
-	Huawei thinks that this only useful for small packets and the gain is mainly for processing.  There is very little concatenation gain.
-	Xiaomi agrees with the other chipset vendors and if we concatenate we are increasing complexity.  Also we need to predict the traffic.
-	LG thinks that there isn’t much gain.  Ciphering is the same and the only benefit is the MAC-I field as it is included only 1.  To concatenate we have to add other headers so there is no gain.   Then the issue is that we have to segment.
-	Ofinno thinks that we need to consider resource efficiency.
-	ZTE supports to study this especially for FWA which has been very successful, as we will have tons of small packets.   LG thinks that this is only a MAC-I issue, so we can discuss selective removal of MAC-I.  ZTE thinks that this is not nice.  Nokia also thinks that this is important for FWA and this reduces the number of time you have to call the function.   Qualcomm doesn’t think we can take data from multiple UEs in the same security context.   ZTE explains that there is a single Uu for the client that is multiplexing multiple UEs.
Come back to concatenation after some further progress on UP protocol and understanding of security
Sequence numbering:
R2-2508047	Considerations on User Plane functionalities for 6GR	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p008`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

提出 RAN2 研究 joint sequence numbering，以提升 6G L2 transmission efficiency。讨论认为该方案可能与 PDCP 和 RLC 是否合并有关，可进一步研究。

```text
RAN2 to investigate joint sequence numbering in order to improve L2 transmission efficiency in 6G.
[2 min]
-	Xiaomi asks if this depends on PDCP and RLC being combined.  Vivo thinks that it would be easier but we can study.
Noted
R2-2508381	Views on 6G User Plane: Functionalities and Processing	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p009`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

提出研究跨 PDCP 和 RLC 层统一 packet 的 SN，并研究适用于 standalone operation 的单一 sequence numbering 功能设计。讨论提及该方案与层间关系及相关功能有关，意见包括可行性、硬件适配性和研究时机。

```text
RAN2 should study if sequence number (SN) for a packet could be unified across in PDCP and RLC layers.
[2 min]
Noted
Discussions
-	LG explains that in LTE we discussed this and we didn’t agree as we had a PDCP control PDU and then we introduced DC and a PDCP was connected to multiple RLC.  If DC is not supported then we go back to LTE discussion.   If we merge then all the problem will be gone.
-	Huawei doesn’t agree it is the same in LTE as we had concatenation in RLC.   In 6G we have 1 to 1 correspondence so it is possible.
-	Xiaomi thinks that this is hardware friendly and we should support it.
-	Lenovo agrees we should study it.
-	Samsung thinks it is too early to study as many functions are related.
Study how to design UP with a single sequence numbering functionality for standalone operation
PDU/header structures (NOT TREATED):
R2-2508032	Discussion on 6G user plane functionalities	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p010`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

提出研究新的 MAC PDU 格式，例如独立 CB，以及包含 TB 中 MAC CE 或 MAC subPDU 元数据的格式，以支持接收端更快处理。

```text
Study new MAC PDU formats (e.g. independent CBs, including metadata about MAC CEs or MAC subPDUs in a TB) that can enable faster processing at receiver.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p011`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

MAC CEs 应设计为灵活且多用途的信令机制，同时保持易于处理和组装。

```text
MAC CEs in 6G should be designed to be a flexible and versatile signalling mechanism for various purposes, while remaining easy to process and assemble.
[2 min]
R2-2508217	6GR User Plane Functionality	Sharp	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p012`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

为支持硬件友好处理，6GR UP protocol 追求为每个 upper layer SDU 使用固定大小的 header。

```text
For hardware-friendly processing, 6GR UP protocol pursues fixed size header for each upper layer SDU.
[2 min]
R2-2508796	On user plane functionalities for 6G	NTT DOCOMO INC.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p013`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

RAN2 研究尽量减少 header length 的动态变化，重点关注 RLC 中的 segmentation 以及 MAC 中的 LCID 和 L field，同时避免统一为更长的 header。

```text
RAN2 studies to minimize dynamic changes of header length focusing on segmentation in RLC, and the LCID and L field in MAC while avoiding unifying to a longer header.
[2 min]
Not treated
(if time allows)
RA procedure:
R2-2508310	UP functionalities and requirements	Nokia, Nokia Shanghai Bell	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p014`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

提出设计统一的 Random Access procedure，以尽量减少对 RA partitioning 的需求，并与 RAN1 一同研究 RA PUSCH payload size 可能存在的问题。

```text
Design a unified Random Access procedure which minimizes the need of RA partitioning, and study, together with RAN1, possible issues with RA PUSCH payload size.
[2 min]
R2-2508032	Discussion on 6G user plane functionalities	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p015`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

提出研究更高效利用资源的 RACH designs，例如除非确有必要，否则避免 RACH partitions，并动态或按需分配 RACH resources。意见指出，preamble partitioning 应仅用于严格需要的功能，例如 coverage enhancements。

```text
Study RACH designs that enable more efficient use of resources, e.g. avoid RACH partitions unless truly necessary, dynamic or on-demand allocation of RACH resources, etc.
[2 min]
R2-2508641	L2 requirements and functions	InterDigital	discussion	Rel-20	FS_6G_Radio
Observation 2.3.5.1-1: NR RA procedure became complex due to additions of new features in later releases of NR while there was a need to retain backwards compatibility with the legacy UEs.
Observation 2.3.5.1-2: Preamble partitioning should not be generally used as an easy tool for all types of early indication but allocated only for functions strictly requiring it, like coverage enhancements.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p016`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

6GR RA procedure 从一开始就支持 2-step 和 4-step RA procedures，以及 coverage enhancement。

```text
6GR RA procedure supports both 2-step and 4-step RA procedures as well as coverage enhancement from the beginning.
Reflective QoS:
R2-2508823	Discussions on 6G UP Functionalities and Requirements	Futurewei	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p017`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

提出 6GR 不考虑 Reflective QoS。

```text
Reflective QoS is not to be considered for 6GR.
R2-2508310	UP functionalities and requirements	Nokia, Nokia Shanghai Bell	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p018`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

6G 保留使用 End-Marker 将 QoS flow 重新映射到 RB 的机制；Reflective QoS 在 6G 中是否仍有必要将进一步讨论。

```text
(Re)mapping of QoS flow to RB with the use of End-Marker is retained in 6G while the necessity of Reflective QoS remains in 6G is further discussed.
[2 min]
R2-2508320	6G User plane functionality and requirements	ZTE Corporation, Sanechips	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p019`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

提出 RAN2 研究以 UP control signalling（例如 PDCP control PDU）替代 5G Reflective QoS mechanism 的新 QoS flow 到 DRB remapping mechanism。另有提案提出考虑 L4S、优先传输 L4S feedback、研究在 L2 protocol layers 中区分 L4S 与非 L4S traffic，以及考虑对 L2 buffer 支持 AQM。

```text
RAN2 should study mechanisms to replace the reflective QoS mechanism of 5G with a new QoS flow to DRB remapping mechanism using UP control signalling (e.g. PDCP control PDU)
[2 min]
Queue management:
R2-2508878	Discussion on support for L4S in 6G radio protocol	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
Proposal 1	Consider support of L4S in radio protocol.
Proposal 2	Prioritize L4S feedback transmission (TCP ACK prioritization).
Proposal 3	Study how to separate L4S traffic from non-L4S traffic in L2 protocol layers.
Proposal 4	Consider support of active queue management (AQM) for L2 buffer.
[3 min]
Not treated
R2-2508074	Discussion on functionalities in user plan	Transsion Holdings	discussion
R2-2508092	Consideration on 6G UP L2 functionalities	Xiaomi	discussion	Rel-20
FS_6G_Radio
R2-2508136	Discussion on 6GR UP functions and related requirements	Huawei, HiSilicon	discussion	Rel-20
R2-2508236	Optimization and Enhancements to F1 and NR UP Protocols for 6G	Tejas Network Limited	discussion
R2-2508268	Functional requirements on 6GR User plane	Fujitsu	discussion	Rel-20	FS_6G_Radio
R2-2508357	Study Considerations for 6GR User Plane	Charter Communications, Inc	discussion	Withdrawn
R2-2508432	Considerations on required functionalities and design objectives for 6G protocol stack	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
R2-2508495	Discussion on User Plane Functions for 6GR	China Telecom	discussion	Rel-20	FS_6G_Radio
R2-2508542	Discussion on 6GR user plane protocol aspects	Sony	discussion	Rel-20	FS_6G_Radio
R2-2508566	Discussion of User Plane Functionalities	Lenovo	discussion	Rel-20	FS_6G_Radio
R2-2508594	Discussion on Functionality for User Plane	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2508627	6G User plane functionalities	Ofinno	discussion	Rel-20
R2-2508661	Optimizing 6GR for small UL packets	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
R2-2508669	Discussion on required functions and requirements for UP	NEC	discussion	Rel-20	FS_6G_Radio
R2-2508785	Discussion on Radio Protocol Architecture – User Plane	Rakuten Mobile, Inc	discussion	Rel-20
R2-2508822	User plane functions for 6G	Samsung	discussion	FS_6G_Radio
R2-2508846	Considerations on functionalities for 6GR UP	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2508890	Discussion on UP Functionality for 6G RAN	TCL	discussion	Rel-20	FS_6G_Radio
R2-2508927	Discussion on 6G user plane protocol	Spreadtrum, UNISOC	discussion	Rel-20
R2-2508976	Discussion on SDAP 	KDDI Corporation (TTC)	discussion	Rel-19
R2-2509026	Considerations for User Plane functionality and design in 6GR	CEWiT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p020`

