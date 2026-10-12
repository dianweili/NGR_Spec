# 6GR 提前报告

**当前进展** · 阶段：收敛中

RAN2 已确认 6GR 可针对尚未进入 L2、暂不可用于传输的上行数据提供提前调度信息，内容可包括预测到达时间和数据量。短期提前报告正朝采用 MAC CE、并纳入含 BSR 和 DSR 的统一调度信息反馈框架收敛，同时需配置触发条件以控制开销。长期预测信息的研究已聚焦于连接建立与重配置、数据不活跃释放，以及 CA 和 RRC 状态管理等用途；部分控制面流程被认为不属于 RAN2 范围或由 UE 实现决定。报告框架应兼容 AI 与非 AI 预测，但监测、LCM 和预测失败处理仍在讨论。

**未决问题**

- 预测到达时间与数据量是否同时报告、其含义和报告粒度，以及按 UE、LCG、LCH 或 flow 区分的方式。
- 提前报告的触发条件、优先级及其与现有 BSR 的共存方式。
- 长期预测信息的具体内容、提供时机，以及预测已建立 service flow 时所用 UL control signaling 的支持方式。
- 预测准确性的监测需求与实现方式，以及是否需要 UE capability、confidence、轻量级 LCM 或失败回退机制。
- 基于预测提前触发 RRC 状态转换的适用范围，以及由网络还是 UE 决定状态转换。

## 6GR 演进

### [6G/Rel-20 RAN2#134] `agreement` 9.3.3.4 Early reporting

研究有助于 aNB 的 long-term traffic prediction information 内容及其用于 UE 重配置、因 data inactivity 释放 UE，以及 idle/inactive 到 connected 的场景；并研究信息提供时机与有用信息。短期和长期 traffic reporting 均应允许 network 启用或禁用，性能监测需求及 CP 相关讨论仍待后续推进，并提及使用 LCM framework。

```text
1	Study the contents of long-term traffic prediction information which would be useful for the aNB and procedures for at least the following two use cases
-	Reconfiguration of the UE already in RRC CONNECTED state, e.g. carrier addition/removal SCells, handover etc.
-     Releasing the UE from RRC_CONNECTED state due to data inactivity
2	For idle/inactive to connected, need to understand when the information is provided and what information is provided/useful.
3	For both short and long term traffic reporting, the network should be able to enable/disable the reporting.   FFS what level of performance monitoring is required (if any) for the various use cases.   For UP can already discuss what additional information (if needed) the network needs to do some form of performance monitoring.   For CP, comeback to this topic after further details on information reported have progressed.
Use of LCM framework
R2-2603179	Discussion on early reporting	1Finity	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-a001`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

predictive reporting 支持三种情况：仅报告 timing information、报告特定时间窗口内的 predicted data size，或报告预期数据到达的时间点及数据量。

```text
all the three cases are supported for predictive reporting: to report 1) timing information only, 2) predicted data size within a certain window, or 3) information of how much data is expected to arrive at which time point.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p001`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

对于 predictive timing information，可将 Rel-19 XR 为 DL 定义的 TTNB（当前 data burst 最后一个 PDU 传输与下一 data burst 第一个 PDU 之间的间隔）复用于 6G UL。

```text
for predictive timing information, TTNB from Rel-19 XR defined for DL, defined as the interval between the transmission of the last PDU in the current data burst and the first PDU of the next data burst, could be reused for UL for 6G.
Reporting mechanism
R2-2603145	Discussion on early reporting	Samsung	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p002`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

Uplink early scheduling information 通过 MAC CE 报告。

```text
2: Uplink early scheduling information is reported by MAC CE.
R2-2603427	Predictive BSR	Nokia	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p003`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

采用 MAC CE 传递 burst arrival prediction 和/或 burst size prediction。

```text
MAC CE is used to convey the burst arrival prediction and/or burst size prediction.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p004`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

应为 predictive SR/BSR 定义并配置适当的触发条件，以避免额外开销，并将其限制在能够受益的场景中。

```text
Appropriate triggers shall be defined and configured for predictive SR/BSR to avoid additional overhead and only limit it to the scenarios that can benefit from it.
R2-2603714	Views on 6G early reporting	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p005`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

RAN2 旨在将 short-term early reporting 纳入包含 BSR 和 DSR 的 unified scheduling information feedback framework。另列出 CP use cases for long term traffic prediction 供讨论。

```text
RAN2 aim to integrate the short-term early reporting into the unified scheduling information feedback framework with BSR and DSR.
CP use cases for long term traffic prediction [30 mins]
R2-2603638	Discussion on traffic prediction for CP	Huawei, HiSilicon, Ericsson, CATT, LG Electronics Inc., 1Finity, Nokia	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p006`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

RAN2 应研究对 aNB 有用的 long-term traffic prediction information 内容，适用于 UE 转入 RRC_CONNECTED 时或之后的初始 RRC (re)configuration、已处于 RRC_CONNECTED 的 UE reconfiguration，以及因 data inactivity 释放 UE。

```text
RAN2 should study the contents of long-term traffic prediction information which would be useful for the aNB for:
- Initial RRC (re)configuration of the UE during/after transition to RRC_CONNECTED state
- Reconfiguration of the UE already in RRC CONNECTED state, e.g. carrier addition/removal, handover etc.
- Releasing the UE from RRC_CONNECTED state due to data inactivity
Noted
R2-2603590	Further Views On Early Report and Traffic prediction	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p007`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

long-term traffic prediction 可考虑两种 RAN2 讨论用例：预测 UE 与 NW 尚未建立 service flow 的信息，以及预测已建立 service flow 的信息。

```text
For the long-term traffic prediction, two use cases can be considered for RAN2 discussion:
- To predict the service flow level information for which the service flow has NOT been established between UE and NW Predictable traffic flow;
- To predict the service flow level information for which the service flow has been established between UE and NW
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p008`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

对于尚未建立的 service flow，原文认为没有可预见的 RAN2 活动：提前发起 UE 与 CN 间的 service flow establishment 不属于 RAN2 范围；提前发起 RRC setup/resume 可由 UE 实现且不影响 RAN2 规范。

```text
For the long-term traffic prediction on the service flow that has not been established, there is no any RAN 2 activity can be foreseen since:
- Early initiation of service flow establishment between UE and CN: it is not in RAN2 scope which can be discussed in SA2/CT1.
- Early initiation of the RRC setup/resume: it can be UE implementation and there is no any RAN2 spec impact.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p009`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

对于已建立的 service flow，CP enhancement 中的 early service flow modification procedure 不属于 RAN2 范围。UE 可配置为发送包含预测信息的 UL control signaling，以帮助 aNB 决定提前释放 RRC；UL control signaling 仍待研究。

```text
For the long-term traffic prediction on the service flow that has been established, the CP enhancement including:
- The early service flow modification related procedure: it is not in RAN2 scope which shall be discussed in SA2/CT1.
- Early state transition to the RRC Idle: a UE can be configured to send an UL control signaling containing the predicted information to help the aNB determine the early RRC release for the UE, FFS the UL control signaling
Noted
R2-2603114	Discussion on early report	OPPO	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p010`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

RRC_IDLE 到 RRC_CONNECTED 的状态转换决定依赖 UE implementation，且与 NR 一样没有规范影响。讨论涉及 long-term prediction 用例和报告内容、在连接建立早期支持 CA setup 的潜在用途，以及报告时机、security、UE capability 和预测准确性等问题。

```text
For decision on state transition from RRC_IDLE to RRC_CONNECTED: Rely on UE implementation with no specification impact as in NR.
Noted
Discussion
-	Xiaomi asks if the first two use case are the same.  Huawei thinks that they can be the same but we would have different ways to report it.
-	ZTE what is the difference with UE.  Huawei explain that the information will be courser than UP as for UP this is used for scheduling.   Vivo thinks that in msg5 the UE can report the data and arrival time
-	Mediatek asks if the information reported would be the same across the usecases.   Huawei hope it was the same but we have to study.   Lenovo doesn’t think the format and what you report can be the same as you have no bearers setup.
-	CMCC thinks that we should study case 3 and case 2 but first one not sure what are the benefits compared to BSR.
-	Qualcomm asks if releasing the UE from connected also means maintaining.  Confirmed.
From idle to connected
-	Ericsson thinks that this is the main use case to enable early CA setup.    It can be some information. Nokia agrees and we shouldn’t use the NAS aspects in this discussion, the network just would like to know I have a lot of data, it doesn’t need too granular, so the network would know what  it may want to do.
-	Qualcomm doesn’t think the service level information is needed to decide whether we want to setup CA or not.   ZTE thinks that for CA the short term reporting can help, the network has enough time from the early reporting to set up the CA.
-	Interdigital thinks that the only benefit of this would be in msg3 and if it is subsequent message the benefits of it are not clear given all the other pains/complications.   The UE can send it in connected mode anyways.   Huawei thinks that the NW doesn’t the know the capabilities yet so it would anyways do the reconfiguration after receiving UE capabilities, at that point the reconfiguration should be the right one for CA.
-	Mediatek thinks msg3 should not be excluded and maybe RAN1 will do some magic.
-	Xiaomi asks how the UE is aware how much volume would trigger the CA and wonders how the UE would know what the is volume in idle mode.
-	Tmobile thinks that we are missing is service awareness and letting the aNB know what QoS/Service calls so it would know what it has to do.   Mediatek wonders if we can provide application information (like background, streaming, interactive etc) if we don’t have the QoS information yet.
-	Samsung asks about security, as the it is only activated after RRC connection, so we need to understand if it is ok to provide this information before.   Apple agrees that measurements can only be reported only after security is established.   Vivo points out that for RRC inactive the security is not a problem.
-	Apple thinks that the UE can trigger the service request before the data is in AS buffer.    The network can only use CA after the CSI resources are configured, so there is no benefit for the fast setup.
-	Oppo thinks that also UE capability is needed before it can setup anything.
-	ZTE thinks that we can consider doing something in inactive as the nw has UE context, security etc, but idle doesn’t make too much sense.
-	ZTE asks how accurate this information is.   Qualcomm explains that the UE can know 100% if it is based on application awareness.
Performance monitoring [30 mins]
Need for performance monitoring
R2-2603576	Discussion on Early Reporting	Lenovo	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p011`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

基于 traffic prediction（AI 或 non-AI）的 reporting 在所有用例中都需要某种形式的 performance monitoring，以确保预测准确性。

```text
Reporting based on traffic prediction (AI or non-AI) requires some form of performance monitoring to ensure prediction accuracy, for all use cases.
Noted
R2-2603145	Discussion on early reporting	Samsung	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p012`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

提出无需为 UE 的 short/long-term traffic prediction 引入 standardized performance monitoring solution。讨论中对 UP 是否需要监测意见不一；部分观点认为 CP 的影响较大，可进一步讨论轻量监测及由网络启停的方式。

```text
1: There is no need to introduce a standardized performance monitoring solution for UE's short/long-term traffic prediction.
Noted
Discussion
-	CATT thinks that only for short term we need performance monitoring.
-	Mediatek thinks that this needs to be done case by case, for CP we would need it as it impact system, but for UP it is not too critical if the UE doesn’t predict too well.  We can discuss later.
-	Vivo thinks that there need to be some form of network to have confidence in the results, and for which use this is needed can be further discussed.
-	Oppo doesn’t see the need for UP, as the aNB knows the information and can determine.   If it is not accurate it can just disable it.    For CP, we should discuss it later after we have more information.
-	Qualcomm doesn’t see a need for performance as the network has full ability to check against.
-	Ericsson thinks that some form of light performance monitoring is needed.   The network should be able to turn off if the UE is not properly predicting.   Lenovo has in mind a lightweight and the network should be able to turn it on or off.  ZTE agrees on UP.
-	Interdigital agrees that for UP the issue is not very big, as the grant will just be a bit overprovisioned, but in CP the consequences would be larger and agree with ericsson it can be light weight.   What new information is needed to evaluate the performance.  LG agrees.
-	CMCC thinks for both it is important.
-	Tmobile asks if we should consider some feedback from network to tell the UE whether it is doing well or not so the UE can improve the accuracy.
-	Qualcomm thinks that we have been told by plenary to have a simplified specifications and we should have the minimum specification.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p013`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

若支持 AI-based traffic prediction，RAN2 研究包括 UE-side data collection for model training、applicability reporting 和 performance monitoring 在内的 LCM procedures。

```text
If AI-based traffic prediction is supported, RAN2 to study the LCM procedures including UE-side data collection for model training, applicability reporting, and performance monitoring.
R2-2603351	Discussion on traffic prediction for UP and CP	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p014`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

针对 CP-related use cases，研究轻量级 LCM-related function（如 UE capability reporting 和 performance monitoring），以及 prediction failure 的 fallback/mitigation mechanisms。研究考虑较高的 trust requirement 和错误预测的较大影响；performance monitoring 使用的信息视时间情况而定。

```text
Study a lightweight LCM-related function (e.g., UE capability reporting and performance monitoring) and fallback/mitigation mechanisms for prediction failure for CP-related use cases, considering the higher trust requirement and larger impact of wrong prediction.
Information used for performance monitoring (if time allows)
R2-2604006	Discussion on early reporting	ASUSTeK	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p015`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

研究 UE reported confidence、NW side performance monitoring，以及 early reporting confidence 的 fallback mechanisms。

```text
Study UE reported confidence, NW side performance monitoring, and fallback mechanisms for early reporting confidence.
R2-2603311	6G Traffic prediction and Early reporting	Ofinno	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p016`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

Early reporting accuracy 的 performance monitoring 可由 NW implementation 处理，例如将收到的 predictions 与后续实际 data arrivals 和 grant utilisation 比较。初始研究不需要额外的 standardized per-report confidence signalling 或 AI LCM overhead。

```text
Performance monitoring of early reporting accuracy can be handled by NW implementation, e.g., based on comparing received predictions against actual subsequent data arrivals and grant utilisation. No additional standardised per-report confidence signalling or AI LCM overhead is needed for the initial study.
Signaling and content of long term traffic prediction (if time allows)
Signalling for long-term traffic prediction (if time allows)
R2-2602958	Consideration on Early Reporting for UP and CP	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p017`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

Early reporting 的 traffic prediction information 可纳入 RRC state transition message，例如在 RACH procedure 的 Msg5 中与 EMR（Early Measurement Report）一起发送，用于优化 state transitions 和 CA configuration。

```text
Early reporting of traffic prediction information can be included within RRC state transition message, e.g., in Msg5 of RACH procedure along with EMR (Early Measurement Report), for optimization for state transitions and CA configuration.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p018`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

支持在 RRC_CONNECTED mode 下报告预测的 UL/DL traffic information，例如通过 UAI，用于 CA、RRC state transitions 和 mobility 管理。

```text
Reporting of predicated UL/DL traffic information in RRC_CONNECTED mode, e.g., via UAI, can be supported for management of CA, RRC state transitions and mobility.
Contents of long term traffic prediction (if time allows)
R2-2603245	Discussion on Traffic Prediction and Early Report	MediaTek Inc.	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p019`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

支持预测下一次 data burst 到达前的时间，并可选报告预期 data volume，以优化 SCell addition/removal 和 dynamic SCell activation/deactivation。

```text
Support the prediction of the time until the arrival of the next data burst, and optionally the expected data volume, to optimize SCell addition/removal and dynamic SCell activation/deactivation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p020`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

支持 UE 预测并报告 traffic cessation，即 traffic burst 结束或到下一次 burst 的时间间隔，以便提前释放 RRC connection。

```text
Support the prediction and report of traffic cessation (i.e., end of a traffic burst or time interval until the next burst) by the UE to facilitate early RRC connection release.
R2-2603405	Discussions on Early Reporting	Qualcomm Incorporated	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p021`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

长期 UL traffic prediction/reporting 可包括每个 FR 的最小和最大 bandwidth preference、分 UL/DL 的 FR bandwidth preference、最小和最大 CC、最小和最大 MIMO layers，或估计的 UL/DL traffic。UL/DL traffic 的 QFI、LC、LCG 或 UE 粒度仍为 FFS。

```text
For long-term UL traffic prediction/reporting, i.e., early reporting/prediction can be
- Minimum and maximum bandwidth preference per FR,
- Minimum and maximum bandwidth preference over an FR separately for UL and DL,
- Minimum and Maximum CC,
- Minimum and Maximum MIMO layers, or
- Estimated UL and DL traffic, FFS granularity per QFI / LC / LCG / UE
R2-2602958	Consideration on Early Reporting for UP and CP	vivo	discussion	Rel-20
R2-2602969	Discussion on Early reporting	Xiaomi	discussion	Rel-20	FS_6G_Radio
R2-2603046	Discussion on Early Traffic Report	NEC	discussion	Rel-20	FS_6G_Radio
R2-2603153	6GR Early Reporting	Sharp	discussion	Rel-20	FS_6G_Radio
R2-2603212	Discussion on 6G early reporting	CATT	discussion	Rel-20	FS_6G_Radio
R2-2603245	Discussion on Traffic Prediction and Early Report	MediaTek Inc.	discussion
R2-2603311	6G Traffic prediction and Early reporting	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2603405	Discussions on Early Reporting	Qualcomm Incorporated	discussion	Rel-20
R2-2603424	Early traffic reporting	InterDigital, Inc.	discussion	Rel-20	FS_6G_Radio
R2-2603576	Discussion on Early Reporting	Lenovo	discussion
R2-2603590	Further Views On Early Report and Traffic prediction	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
R2-2603632	Discussion on early reporting of UL traffic information and buffer status	Sony	discussion	Rel-20	FS_6G_Radio
R2-2603638	Discussion on traffic prediction for CP	Huawei, HiSilicon, Ericsson, CATT, LG Electronics Inc., 1Finity, Nokia	discussion	Rel-20	FS_6G_Radio
R2-2603644	Discussion on early reporting of scheduling information	Panasonic	discussion	Rel-20
R2-2603714	Views on 6G early reporting	Apple	discussion	Rel-20	FS_6G_Radio
R2-2603742	UE traffic predictions	Ericsson	discussion	Rel-20	FS_6G_Radio
R2-2603768	Discussion on Early Reporting	AUMOVIO	discussion
R2-2603781	Prediction and reporting of UE traffic	Fraunhofer IIS, Fraunhofer HHI	discussion	R2-2602307
R2-2603842	Discussion on early reporting	KT Corp.	discussion
R2-2603865	Considerations on Early reporting	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2603904	Discussion on early reporting of scheduling information	Spreadtrum, UNISOC	discussion	Rel-20
R2-2603960	Discussion on early reporting	TCL	discussion	Rel-20
R2-2603989	Discussion on early data reporting	Google	discussion	Rel-21
R2-2604006	Discussion on early reporting	ASUSTeK	discussion	Rel-20
R2-2604155	Views on early reporting	NTT DOCOMO INC..	discussion
R2-2604163	Discussion on early reporting	ETRI	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p022`

### [6G/Rel-20 RAN2#133bis] `agreement` 9.3.3.4 Early reporting

原文支持6GR为L2中尚不可用的上行数据提供early scheduling information。上行early scheduling information至少可包含timing information和data volume estimates；是否总是同时报告、报告方式与条件、时序含义及粒度等仍待讨论。

```text
1	How traffic prediction is done is up to UE implementation.   FFS how aNB trusts (e.g. UE reporting is reliable/accurate), whether there is need for performance monitoring, LCM, etc.  These needs to be discussed based on the use case basis.
2	6GR supports early scheduling information for reporting of UL data not yet available in L2
3	Uplink early scheduling information can include at least timing information and data volume estimates. FFS whether both timing and volume information are always reported together, how it is reported, controlled and conditions when to report, what the timing information represents, and how to efficiently support at least delay-critical/senstive data.  FFS level of granularity of reporting
R2-2601692 Discussion on Early Reporting in 6G LG Electronics. discussion Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-a001`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.3.4 Early reporting

early short-term和long-term traffic prediction/reporting可基于UE对上行和/或下行流量的预测（AI/ML-enabled feature），或基于设备不同协议层的信息，例如application、transport层。

```text
The early short-term and long-term traffic prediction/reporting can be based on
Prediction of the uplink and/or downlink traffic at the UE (i.e., an AI/ML-enabled feature), or
Information from different protocol layers at the device (e.g., application, transport, etc).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-o001`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.3.4 Early reporting

UE能够使用AI模型（例如LSTM）或非AI方法（例如ARIMA），预测可预测流量流的UL/DL traffic pattern；该流量流由周期性数据传输及每周期偶发的额外数据传输构成。

```text
UE is able to utilize the AI model (e.g.LSTM) or non-AI method(e.g. ARIMA) to predict the UL/DL traffic pattern for a predictable traffic flow of which the periodical data transmission and occasionally extra data transmission per period is composed.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-o002`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.3.4 Early reporting

6G 预计支持高度可变的上行流量，包括时延关键数据突发。对流量特征的服务感知可使调度器及时分配资源并满足 QoS 要求。

```text
6G is expected to support highly variable uplink traffic, including delay-critical data bursts. Service awareness of traffic characteristics enables the scheduler to timely allocate resources and meet QoS requirements.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-o003`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.3.4 Early reporting

提前报告预期的数据到达可实现主动资源分配并降低时延。

```text
Early reporting of anticipated data arrival allows for proactive resource allocation and reduced latency.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-o004`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.3.4 Early reporting

基于预测的 UL traffic 提前触发 RRC 状态转换至 RRC_CONNECTED，或在 RRC_CONNECTED 模式下提前报告流量预测信息，有利于优化 RRC 状态转换流程。

```text
Early triggering of RRC state transitions to RRC_CONNECTED based on predicted UL traffic, or early reporting of traffic prediction information in RRC_CONNECTED mode, is beneficial for optimizing RRC state transition procedures.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-o005`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.3.4 Early reporting

Early traffic prediction 依赖上层服务感知，支持非 AI 方法且失败风险较低；它不同于 AI-enabled PHY 等 radio-centric AI。对其施加 5G Rel-18/19 AI-PHY 规定的全面 AI/ML LCM framework 会引入不合理的复杂性。

```text
Unlike radio-centric AI such as the AI-enabled PHY features, early traffic prediction relies on upper-layer service awareness, supports non-AI methods, and carries minimal failure risk. Thus, imposing the comprehensive AI/ML LCM framework as specified for AI-PHY in 5G Rel-18/19 introduces unjustified complexity.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-o006`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.4 Early reporting

Early reporting mechanism 应采用通用报告框架，适用于基于 AI 和非 AI 的流量预测方法。

```text
The early reporting mechanism should aim for a generic reporting framework common to AI/non-AI based traffic prediction methods.
Noted
R2-2601877 Discussions on Early Reporting Qualcomm Incorporated discussion Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-p001`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.4 Early reporting

从标准角度，early short-term 和 long-term traffic prediction/reporting 被视为 non-AI/ML features。网络假定 UE 不使用底层 AI/ML model 提供这些服务。

```text
From the standard point of view, early short-term and long-term traffic prediction/reporting are considered non-AI/ML features, i.e., the network assumes that the UE does not use an underlying AI/ML model to provide these services.
Noted
R2-2601814	Discussion on traffic prediction and early reporting	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-p002`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.4 Early reporting

短期和长期流量预测方式可留给 UE 实现决定，RAN2 无需讨论该方面。

```text
How to predict the traffic in short- and long-term can be left to UE implementation and there is no need to discuss this aspect in RAN2.
Noted
R2-2602190 Views On Early Report According to Traffic Prediction ZTE Corporation, Sanechips discussion Rel-20 FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-p003`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.4 Early reporting

关于可预测流量，原文提出网络应知晓 UE 使用的预测方法是 AI-based 还是 non-AI-based；讨论意见对此存在分歧，涉及性能监测、预测置信度及准确性等问题。

```text
For the use case of predictable traffic flow, it shall be aware of by NW that which traffic prediction method is applied by UE (i.e. AI based or non-AI based).
Noted
Discussion
-	ZTE thinks that this is related to performance monitoring and the network would need to be aware for which kind of solution or CPU computation.   LG agrees with ZTE but for some cases for AI we will need some LCM.
-	Apple thinks that how the UE performs the prediction is up to UE implementation, and from network perspective we’d need to understand if there is some level of confidence.
-	Mediatek agrees with Qualcomm and we just need to understand whether performance monitoring is required for use cases and for test cases we don’t need to differentiate.
-	Ericsson thinks that we need to understand whether it is deterministic (e.g. coming from application level information) or AI based which is not so deterministic.  Apple doesn’t agree that non-AI is better.
-	Nokia doesn’t want to know whether it is AI based or not, as long as the prediction is accurate.
-	Tmobile thinks monitoring is crucial and it may be good to understand that it is AI traffic.
-	Qualcomm thinks that similar to BSR the network can always check whether the information is accurate or not.    ZTE is concerned that the network has to always schedule a grant to verify if the prediction is correct or not.
Short term – reporting information
R2-2601808 Early traffic reporting InterDigital, Apple, Huawei, ZTE Corporation, vivo discussion Rel-20 FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-p004`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.4 Early reporting

6GR 支持针对尚未在报告时进入 L2、因而尚不可用于传输的 UL data 提供 early scheduling information。讨论中将其解释为尚未进入 L2 buffer 的数据，并提出可称为尚未到达 L2 的 UL data。

```text
6GR supports early scheduling information for reporting of UL data not yet available for transmission in L2 at the time of reporting.
-	Samsung asks what is UL data not yet available for transmission.  Interidigtal explains that it is something not in the L2 buffer.  Samsung thinks we can updated UL data not yet arrived in L2.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-p005`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.4 Early reporting

Uplink early scheduling information 可包含 timing information 和 data volume estimates。是否总是同时报告两者、报告方式、timing information 的含义以及如何高效支持 delay-critical bursts 仍待讨论；讨论还涉及报告粒度及不同流的优先级。

```text
Uplink early scheduling information can include timing information and data volume estimates. FFS whether both timing and volume information are always reported together, how it is reported, what the timing information represents, and how to efficiently support delay-critical bursts.
-	Samsung asks why burst and not data.   Interdigital explains that burst is data at the end.   Samsung is concerned that this implies PDU set.
-	Oppo asks if it means data are at the application layer or not yet.  Both cases are possible.
-	Oppo asks what is the granularity.
-	Xiaomi asks what is specific to delay critical data.   Interdigital explains that not all data will trigger the reporting this so we can study further.
-	Tmobile thinks there should be more granularity in the reporting, for example the priority of the different flows that may need to be treated differently.
-	Qualcomm also thinks that it shouldn’t be only for critical-delay data.  Interdigital explain it is not restciting but rather that we have to think more a bout delay critical.
Noted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-p006`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.4 Early reporting

Early reporting 可包含特定时间段内的预期/预测数据量和预期/预测到达时间。

```text
In early reporting, following can be included: - the expected/predicted data volume within the certain time period - the expected/predicted arrival time.
Noted
R2-2602095 Discussion on early reporting based on traffic prediction Spreadtrum, UNISOC discussion Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-p007`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.4 Early reporting

RAN2 将研究短期 traffic prediction and reporting 的粒度，例如按 LCG/LCH/flow 或按 UE。

```text
RAN2 to study the granularity of short term traffic prediction and reporting, e.g., per LCG/LCH/flow, or per UE.
Short term - triggering
R2-2601692 Discussion on Early Reporting in 6G LG Electronics. discussion Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-p008`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.4 Early reporting

研究由 data burst arrival、upper layer indication 和 AI-assisted traffic prediction 触发的 early reporting。

```text
Study early reporting triggered by data burst arrival, upper layer indication, AI-assisted traffic prediction.
R2-2601750 Considerations on Early Reporting Lenovo discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-p009`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.4 Early reporting

RAN2 应研究如何支持 early reporting 与现有 BSR 共存。

```text
RAN2 should study how to support the coexistence between early reporting and the existing BSR.
Long term - RRC State Transition
R2-2601457 consideration on early traffic reporting for both UP and CP vivo discussion Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-p010`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.4 Early reporting

6GR 支持基于 UE 或 UE AS layer 尚不可用的 UL data transmission request（例如基于 AI model prediction 或与 applications 交互）提前触发 RRC state transition 至 RRC_CONNECTED。会议意见涉及该用例是否限于 UL、UE 影响、baseline mechanism 与 long term prediction，以及其重要性。

```text
6GR supports early triggering of RRC state transition to RRC_CONNECTED based on an UL data transmission request not yet available in UE or UE AS layer, e.g., based on AI model prediction or interaction with applications.
-	Ericsson asks why it is limited to UL.
-	CATT asks what is the UE impact.
-	Apple thinks that we don’t even know the baseline mechanism for state transition and we should first understand what is long term prediction.   Vivo thinks we have idle so we can consider that as baseline.
-	Lenovo doesn’t see this use case as an important one
Noted
R2-2601712	Discussion on early reporting	Samsung, Verizon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-p011`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.4 Early reporting

提出两种 proactive RRC state transition 选项：UE 向网络报告 predicted traffic inactivity information，由网络决定转至 IDLE/INACTIVE；或 UE 根据 traffic prediction 决定并发送 RRC release request。另有提案建议网络决策依赖 proactive buffer status report，且不支持 UE 决策流程；该议题标记为 Not treated。

```text
7: For proactive RRC state transition, the UE can provide assistance information for NW’s decision. RAN2 can discuss the following two options.
- Option 1 (Predicted traffic inactivity information): The UE reports the predicted traffic inactivity information (e.g., inactivity period start time, duration, …) to the NW and the NW determines the need for RRC state transition (from CONNECTED to IDLE/INACTIVE).
- Option 2 (RRC release request) : The UE determines whether it can go RRC_IDLE/INACTIVE state based on traffic prediction, and sends an RRC release request to NW, similar to what is supported in 5G NR.
Noted
R2-2601562 Discussion on traffic reporting and prediction OPPO discussion Rel-20 FS_6G_Radio
Observation 3 Based on the LTE and NR framework, network decisions related to CA and RRC state transitions from RRC_CONNECTED to RRC_IDLE/RRC_INACTIVE are fully controlled by network implementation. While the RRC state transition from RRC_IDLE/RRC_INACTIVE to RRC_CONNECTED is up to UE.
Proposal 3 For RRC state transition based on early reporting, 1) For Network decision-based procedure (e.g., keeping the UE in RRC_CONNECTED or releasing the UE to RRC_IDLE or RRC_INACTIVE (if any)), rely on network implementation based on proactive buffer status report, no additional impact is needed; 2) For UE decision-based procedure (e.g., selection between keeping the UE in RRC_INACTIVE (if any) or entering RRC_CONNECTED), not support the scenario.
Noted
Discussion
-	Xiaomi,LG, thinks that from idle to inactive/idle we don’t need to do anything, it’s up to UE.   From Connected to idle/inactive there is power saving gain.   We should discuss what should be reported to the network.
-	Qualcomm thinks that we have this preference indication already in 5G and there is no need to report statistics, we can follow what we have in 5G.   CMCC also asks what new mechanisms we need to support.   Vivo thinks UAI it’s only on what you have now.  Samsung thinks one bit is not enough to make the decision, so additional information like inactivity period.
-	LG thinks we can further discuss more about connected to idle based on trust and accuracy.
-	Nokia thinks that we should discuss what the UE tells to the network and what does the network do with it.   We have done quite a bit of this in 5G and need to understand what needs to be enhanced.
-	Huawei also thinks it is important on when the UE tells the network.   What’s important is what the UE report once it is connected.
-	ZTE thinks that for idle and connected the network doesn’t need any indication.   From connected to idle, we can study information to provide the prediction but it doesn’t need to tell the network what to do.  It is up to the NW what to do.
-	Ericsson explains that when UE comes to connected we need to understand whether to setup CA, so if we know a bit earlier then we can set up CA already before the traffic has already started or gone.
-	Fraunhaufer would like to understand time frame.
-	Docomo has some concerns on Idle to connected, as network doesn’t want to increase unnecessary setup.
-	ZTE thinks that for idle to connected we need to consider that we have to first send service request and to compile the service request you need send a NAS request.  Huawei explains that the UE would start it when a service starts.  Ericsson thinks that we can make it applicable to inactive.
Not treated
Long term - CA management
R2-2601667 Discussion on 6GR Early Reporting Sharp discussion Rel-20 FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-p012`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.4 Early reporting

Early reporting 可包含 predicted traffic load，网络可将其用于 carrier aggregation management，例如 SCell activation/deactivation。提案建议依靠网络实现基于 proactive buffer status report 控制 CA 操作，不产生额外规范影响。

```text
Early reporting can include predicted traffic load. The network may use it in carrier aggregation management, e.g. SCell activation/deactivation.
R2-2601562 Discussion on traffic reporting and prediction OPPO discussion Rel-20 FS_6G_Radio
Proposal 2 For CA (de)activation based on early reporting, rely on network implementation to control CA operation based on proactive buffer status report, i.e., no additional spec impact.
Performance Monitoring, Confidence & LCM
R2-2601925	Discussion on Traffic Prediction and Early Report	MediaTek Inc.	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-p013`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.4 Early reporting

Traffic prediction 不需要 comprehensive over-the-air AI/ML LCM framework；RAN2 应聚焦适用的 LCM 组件，例如必要时的 UE capability reporting 和 performance monitoring。

```text
The comprehensive over-the-air AI/ML LCM framework is not required for traffic prediction. RAN2 should focus on applicable LCM components, such as UE capability reporting and performance monitoring, where necessary.
R2-2601514 Discussion on early reporting Xiaomi discussion Rel-20 FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-p014`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.4 Early reporting

建议依靠网络实现监测 prediction performance，并由网络控制是否允许 early reporting；无需引入 confidence 或 performance monitoring enhancement。

```text
Rely on NW implementation to monitor the prediction performance. Early reporting is under NW control, i.e. allow/disallow. No need to introduce confidence or performance monitoring enhancement.
R2-2601595	Discussion on Early Traffic Report	NEC	discussion	Rel-20	FS_6G_Radio
R2-2601678	Simulation results of AI based traffic prediction and early reporting	CATT	discussion	Rel-20	FS_6G_Radio
R2-2601740	Optimizing the UL scheduling delay by early data reporting	Google	discussion	Rel-20	FS_6G_Radio
R2-2601772	Discussion on early reporting	1Finity	discussion	Rel-20	FS_6G_Radio
R2-2601867	6G Traffic prediction and early reporting	Ofinno	discussion
R2-2601889	Early Reporting	Nokia	discussion	Rel-20	FS_6G_Radio
R2-2601940	Discussion on early reporting	ASUSTeK	discussion	Rel-20
R2-2602173	Discussion on early reporting of scheduling information	Panasonic	discussion	Rel-20
R2-2602218	Views on 6G early reporting	Apple	discussion	Rel-20	FS_6G_Radio
R2-2602307	Prediction and reporting of UE traffic	Fraunhofer IIS, Fraunhofer HHI	discussion
R2-2602358	Enhancement of CP and UP functionalities using UE traffic prediction	Ericsson	discussion	Rel-20	FS_6G_Radio
R2-2602404	Discussion on early reporting	KT Corp.	discussion
R2-2602426	Considerations on Early reporting	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2602608	Required framework for early reporting	NTT DOCOMO INC..	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-p015`

