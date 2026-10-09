# 6GR 提前报告

**当前进展** · 阶段：—

_尚无综述_

## 6GR 演进

### [6G/Rel-20 RAN2#134] `agreement` 9.3.3.4 Early reporting

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

```text
all the three cases are supported for predictive reporting: to report 1) timing information only, 2) predicted data size within a certain window, or 3) information of how much data is expected to arrive at which time point.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p001`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

```text
for predictive timing information, TTNB from Rel-19 XR defined for DL, defined as the interval between the transmission of the last PDU in the current data burst and the first PDU of the next data burst, could be reused for UL for 6G.
Reporting mechanism
R2-2603145	Discussion on early reporting	Samsung	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p002`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

```text
2: Uplink early scheduling information is reported by MAC CE.
R2-2603427	Predictive BSR	Nokia	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p003`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

```text
MAC CE is used to convey the burst arrival prediction and/or burst size prediction.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p004`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

```text
Appropriate triggers shall be defined and configured for predictive SR/BSR to avoid additional overhead and only limit it to the scenarios that can benefit from it.
R2-2603714	Views on 6G early reporting	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p005`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

```text
RAN2 aim to integrate the short-term early reporting into the unified scheduling information feedback framework with BSR and DSR.
CP use cases for long term traffic prediction [30 mins]
R2-2603638	Discussion on traffic prediction for CP	Huawei, HiSilicon, Ericsson, CATT, LG Electronics Inc., 1Finity, Nokia	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p006`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

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

```text
For the long-term traffic prediction, two use cases can be considered for RAN2 discussion:
- To predict the service flow level information for which the service flow has NOT been established between UE and NW Predictable traffic flow;
- To predict the service flow level information for which the service flow has been established between UE and NW
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p008`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

```text
For the long-term traffic prediction on the service flow that has not been established, there is no any RAN 2 activity can be foreseen since:
- Early initiation of service flow establishment between UE and CN: it is not in RAN2 scope which can be discussed in SA2/CT1.
- Early initiation of the RRC setup/resume: it can be UE implementation and there is no any RAN2 spec impact.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p009`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

```text
For the long-term traffic prediction on the service flow that has been established, the CP enhancement including:
- The early service flow modification related procedure: it is not in RAN2 scope which shall be discussed in SA2/CT1.
- Early state transition to the RRC Idle: a UE can be configured to send an UL control signaling containing the predicted information to help the aNB determine the early RRC release for the UE, FFS the UL control signaling
Noted
R2-2603114	Discussion on early report	OPPO	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p010`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

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

```text
Reporting based on traffic prediction (AI or non-AI) requires some form of performance monitoring to ensure prediction accuracy, for all use cases.
Noted
R2-2603145	Discussion on early reporting	Samsung	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p012`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

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

```text
If AI-based traffic prediction is supported, RAN2 to study the LCM procedures including UE-side data collection for model training, applicability reporting, and performance monitoring.
R2-2603351	Discussion on traffic prediction for UP and CP	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p014`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

```text
Study a lightweight LCM-related function (e.g., UE capability reporting and performance monitoring) and fallback/mitigation mechanisms for prediction failure for CP-related use cases, considering the higher trust requirement and larger impact of wrong prediction.
Information used for performance monitoring (if time allows)
R2-2604006	Discussion on early reporting	ASUSTeK	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p015`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

```text
Study UE reported confidence, NW side performance monitoring, and fallback mechanisms for early reporting confidence.
R2-2603311	6G Traffic prediction and Early reporting	Ofinno	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p016`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

```text
Performance monitoring of early reporting accuracy can be handled by NW implementation, e.g., based on comparing received predictions against actual subsequent data arrivals and grant utilisation. No additional standardised per-report confidence signalling or AI LCM overhead is needed for the initial study.
Signaling and content of long term traffic prediction (if time allows)
Signalling for long-term traffic prediction (if time allows)
R2-2602958	Consideration on Early Reporting for UP and CP	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p017`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

```text
Early reporting of traffic prediction information can be included within RRC state transition message, e.g., in Msg5 of RACH procedure along with EMR (Early Measurement Report), for optimization for state transitions and CA configuration.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p018`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

```text
Reporting of predicated UL/DL traffic information in RRC_CONNECTED mode, e.g., via UAI, can be supported for management of CA, RRC state transitions and mobility.
Contents of long term traffic prediction (if time allows)
R2-2603245	Discussion on Traffic Prediction and Early Report	MediaTek Inc.	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p019`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

```text
Support the prediction of the time until the arrival of the next data burst, and optionally the expected data volume, to optimize SCell addition/removal and dynamic SCell activation/deactivation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p020`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

```text
Support the prediction and report of traffic cessation (i.e., end of a traffic burst or time interval until the next burst) by the UE to facilitate early RRC connection release.
R2-2603405	Discussions on Early Reporting	Qualcomm Incorporated	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.4-p021`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.4 Early reporting

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

```text
1	How traffic prediction is done is up to UE implementation.   FFS how aNB trusts (e.g. UE reporting is reliable/accurate), whether there is need for performance monitoring, LCM, etc.  These needs to be discussed based on the use case basis.
2	6GR supports early scheduling information for reporting of UL data not yet available in L2
3	Uplink early scheduling information can include at least timing information and data volume estimates. FFS whether both timing and volume information are always reported together, how it is reported, controlled and conditions when to report, what the timing information represents, and how to efficiently support at least delay-critical/senstive data.  FFS level of granularity of reporting
R2-2601692 Discussion on Early Reporting in 6G LG Electronics. discussion Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-a001`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.3.4 Early reporting

```text
The early short-term and long-term traffic prediction/reporting can be based on
Prediction of the uplink and/or downlink traffic at the UE (i.e., an AI/ML-enabled feature), or
Information from different protocol layers at the device (e.g., application, transport, etc).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-o001`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.3.4 Early reporting

```text
UE is able to utilize the AI model (e.g.LSTM) or non-AI method(e.g. ARIMA) to predict the UL/DL traffic pattern for a predictable traffic flow of which the periodical data transmission and occasionally extra data transmission per period is composed.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-o002`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.3.4 Early reporting

```text
6G is expected to support highly variable uplink traffic, including delay-critical data bursts. Service awareness of traffic characteristics enables the scheduler to timely allocate resources and meet QoS requirements.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-o003`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.3.4 Early reporting

```text
Early reporting of anticipated data arrival allows for proactive resource allocation and reduced latency.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-o004`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.3.4 Early reporting

```text
Early triggering of RRC state transitions to RRC_CONNECTED based on predicted UL traffic, or early reporting of traffic prediction information in RRC_CONNECTED mode, is beneficial for optimizing RRC state transition procedures.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-o005`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.3.4 Early reporting

```text
Unlike radio-centric AI such as the AI-enabled PHY features, early traffic prediction relies on upper-layer service awareness, supports non-AI methods, and carries minimal failure risk. Thus, imposing the comprehensive AI/ML LCM framework as specified for AI-PHY in 5G Rel-18/19 introduces unjustified complexity.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-o006`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.4 Early reporting

```text
The early reporting mechanism should aim for a generic reporting framework common to AI/non-AI based traffic prediction methods.
Noted
R2-2601877 Discussions on Early Reporting Qualcomm Incorporated discussion Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-p001`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.4 Early reporting

```text
From the standard point of view, early short-term and long-term traffic prediction/reporting are considered non-AI/ML features, i.e., the network assumes that the UE does not use an underlying AI/ML model to provide these services.
Noted
R2-2601814	Discussion on traffic prediction and early reporting	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-p002`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.4 Early reporting

```text
How to predict the traffic in short- and long-term can be left to UE implementation and there is no need to discuss this aspect in RAN2.
Noted
R2-2602190 Views On Early Report According to Traffic Prediction ZTE Corporation, Sanechips discussion Rel-20 FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-p003`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.4 Early reporting

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

```text
6GR supports early scheduling information for reporting of UL data not yet available for transmission in L2 at the time of reporting.
-	Samsung asks what is UL data not yet available for transmission.  Interidigtal explains that it is something not in the L2 buffer.  Samsung thinks we can updated UL data not yet arrived in L2.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-p005`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.4 Early reporting

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

```text
In early reporting, following can be included: - the expected/predicted data volume within the certain time period - the expected/predicted arrival time.
Noted
R2-2602095 Discussion on early reporting based on traffic prediction Spreadtrum, UNISOC discussion Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-p007`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.4 Early reporting

```text
RAN2 to study the granularity of short term traffic prediction and reporting, e.g., per LCG/LCH/flow, or per UE.
Short term - triggering
R2-2601692 Discussion on Early Reporting in 6G LG Electronics. discussion Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-p008`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.4 Early reporting

```text
Study early reporting triggered by data burst arrival, upper layer indication, AI-assisted traffic prediction.
R2-2601750 Considerations on Early Reporting Lenovo discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-p009`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.4 Early reporting

```text
RAN2 should study how to support the coexistence between early reporting and the existing BSR.
Long term - RRC State Transition
R2-2601457 consideration on early traffic reporting for both UP and CP vivo discussion Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-p010`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.4 Early reporting

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

```text
Early reporting can include predicted traffic load. The network may use it in carrier aggregation management, e.g. SCell activation/deactivation.
R2-2601562 Discussion on traffic reporting and prediction OPPO discussion Rel-20 FS_6G_Radio
Proposal 2 For CA (de)activation based on early reporting, rely on network implementation to control CA operation based on proactive buffer status report, i.e., no additional spec impact.
Performance Monitoring, Confidence & LCM
R2-2601925	Discussion on Traffic Prediction and Early Report	MediaTek Inc.	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-p013`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.4 Early reporting

```text
The comprehensive over-the-air AI/ML LCM framework is not required for traffic prediction. RAN2 should focus on applicable LCM components, such as UE capability reporting and performance monitoring, where necessary.
R2-2601514 Discussion on early reporting Xiaomi discussion Rel-20 FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.4-p014`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.4 Early reporting

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

