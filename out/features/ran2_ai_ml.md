# 6GR AI/ML 协议支持

**当前进展** · 阶段：—

_尚无综述_

## 6GR 演进

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.2 AI/ML

```text
For UE-sided model, the network needs to be aware that it is a model (without being aware of model content or detailed meta info) to avoid the impacts on other traffic, e.g. whether and when to transfer/delivery the model to the UE can be controlled by the network.
Noted
R2-2603447	Discussion on LCM framework for AL/ML	China Unicom	discussion	Late
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.2-p001`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.2 AI/ML

```text
For one sided UE models:
- When stored outside 3GPP, model transfer may remain transparent to 3GPP.
- When stored inside 3GPP, the network shall have partial visibility (awareness of model vs. non model) and controllability of transfer.
Noted
R2-2603281	Discussion on AI/ML LCM and model transfer	Futurewei Technologies	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.2-p002`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.2 AI/ML

```text
RAN2 to adopt the transparent/OTT approach as the baseline for UE-side model transfer in 6G. FFS other UP-based approaches.
Noted
MNO control of model transfer
R2-2604073	Discussion on model transfer	NTT DOCOMO, Nokia, Ericsson, CMCC, Verizon, Turkcell, T-Mobile USA	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.2-p003`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.2 AI/ML

```text
About model transfer from UE server to the UE in 6G, RAN2 to study whether RAN2-impacted mechanism of network controllability is needed and what is the function of the network controllability if needed. As the starting point, the function of the network controllability is following.
- Network can allow/prohibit the procedure of model transfer.
- Network can stop/suspend/resume the procedure of model transfer.
Noted
R2-2603713	Views on 6G AI/ML general framework and model transfer	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.2-p004`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.2 AI/ML

```text
UE-sided model transfer is transparent to NW and NW controllability is not needed.
Noted
Discussion
-	ATT agrees that the network should know, as it can avoid charging the subscriber, and handle congestion cases, we don’t need to understand what’s in the model but just to understand so we can control.
-	Oppo thinks that for two sided model there is motivation as there needs to be some coordination, but for one sided model wonders where the control/awareness would be.
-	Docomo thinks that to avoid congestion is one motivation so lower level controllability.    CMCC thinks that at least we can configure it with a different QoS so if there is congestion we can handle it properly.
-	ATT thinks that we can ask can you do it later.
-	Ericsson agrees that it would be good to have some awareness.
-	Apple thinks that we should focus on one sided model and for that cases it is from OTT to UE, so why this model would cause network congestion and this is the same as the software update.     ATT doesn’t thinks that model transfers are the same as software as the user has the choice to say I want to do it now or not, but for model transfer the user has no say and they don’t know that anything is going on.  Docomo also thinks that this is completely different and there is responsibility from MNO.   CMCC explains that it is not the model transfer that causes the congestion, the network is congested and just need to know to give it a lower priority.   Samsung thinks that there is some means already to know that there is a software update and control and that is transparent to the RAN.
-	Xiaomi thinks that there is nothing we need to do, as we can just map this service and charging is out of scope of RAN2.   Samsung agrees.
-	Vivo agrees with the operators.
-	Lenovo sees the concerns from the operators and understand that the issue belong to SA.  Something similar like background data transfer can be considered there is coordination between AF and CN to negotiate when it can transfer.  We can discuss what are the requirements for model transfer.  Mediatek thinks we should be careful as the background data is very long delay and for model transfer may not be the same delay.  But we should agree to an intention and SA can study.
-	Qualcomm thinks this is SA discussion and we can’t set requirements.
-	ZTE would like to have test before transfer.
-	LG thinks that what matter is the size and frequency.
-	Futurewei doesn’t think we need to do anything special as anyways different model transfer may have different priority.   CMCC thinks that model transfer is not high priority.
-	Huawei understand that there is a willingness to not impact user traffic.
-	Nokia would like to understand how often they happen, is it the same as OS updates, like every 3 months.   Interdigital thinks that the UE check applicability and if it doesn’t have the model it has download and this is evaluated after mobility and for a lot of UE this can be quite a lot.  Mediatek agrees we need to understand how big this problem is and in real products we may go with more generalized solution so perhaps the problem will not be so severe.
-	Tmobile would like to stop models.   Qualcomm doesn’t think it is possible to stop if you have no visibility on the model.
-	Samsung and Qualcomm thinks that this is a problem if the model transfer size is big and/or frequent.
Agreements on model transfer
MNO should be aware model transfer is happening over 3GPP for the purpose to differentiate between user traffic and model transfer traffic  (e.g. to minimize impact to user traffic, adjust priority).   No visibility of the model is required and there is no intention for MNO to disable the UE from doing model transfer.    Understanding from RAN2 is that how to achieve this is not in scope of RAN2 and can be perhaps be achieved by CN mechanisms (e.g. QoS, PDU session management, etc).
Notify LS to SA2, cc: RAN, SA.  Action: take this into account
[AT134][016][6G AI] model transfer LS (Docomo)
Intended outcome: Agree to LS
Deadline:  Friday
R2-2604397	[Draft] LS on Model transfer	NTT DOCOMO	LS out	Rel-20	FS_6G_Radio	To:SA2 cc:RAN, SA
The LS is approved in R2-2604407
AIML general principles (if time allows)
R2-2603637	Discussion on AIML framework and model transfer	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.2-p005`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.2 AI/ML

```text
For NW-sided models, reuse an approach from 5G-A that no LCM functions other than network-side data collection (e.g. for training) are specified (i.e. they are left to network implementation).
R2-2603279	LCM and model transfer in 6GR	Samsung	discussion	Rel-20	FS_6G_Radio	R2-2601648
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.2-p006`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.2 AI/ML

```text
RAN2 to consider the common procedures (i.e., UE capabilities, applicability determination, inference, performance monitoring, data collection) defined in Rel-19 AI/ML PHY as baseline for unified LCM framework. However, detailed signaling messages and parameters are studied separately for each 6G AI/ML use case.
R2-2603069	Discussion on LCM and model transfer	OPPO	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.2-p007`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.2 AI/ML

```text
Functionality-based LCM should be the baseline in 6G.
AIML LCM (if time allows)
R2-2602967	Discussion on LCM and model transfer	Xiaomi	discussion	Rel-20	FS_6G_Radio	R2-2601512
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.2-p008`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.2 AI/ML

```text
RAN2 to study LCM decision by NW initiated and UE as following,
- Option 1: Decision by the network
- Option 1-1: Network-initiated
- Option 1-2: UE-initiated and requested to the network
- Option 2: Decision by the UE
- Option 2-1: Event-triggered as configured by network, UE’s decision is reported to the network
- Option 2-2: UE-autonomous, UE’s decision is reported to the network
R2-2603255	On AI/ML enablers and model transfer	Nokia	discussion	Rel-20	FS_6GSpecs
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.2-p009`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.2 AI/ML

```text
Study the feasibility of fallback mechanisms for low-latency (fast, one signalling step), bidirectional switching between an AI/ML-enabled configuration and a non-AI/ML-enabled configuration.
R2-2603069	Discussion on LCM and model transfer	OPPO	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.2-p010`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.2 AI/ML

```text
For performance monitoring, the following directions can be further studied:
- For NW-sided model, study UE assisted performance monitoring.
- For UE-sided model, study:
- For the case that performance monitoring is performed at the NW side:
- Scenario 1: Calculated performance metrics is generated by UE and terminated at NW side, management decision is made by NW side.
- Scenario 2: Data needed for performance metric calculation is generated by UE and terminated at gNB, management decision is made by NW side.
- For the case that performance monitoring is performed at the UE side
- Scenario 3: UE performs performance monitoring. Suggested management decision is sent from UE to NW side and management decision is made by NW side.
- Scenario 4: UE performs performance monitoring. Management decision is made by UE side and Management decision is sent from UE to NW side for alignment.
- Scenario 5: UE performs performance monitoring. Management decision is made by UE side autonomously without notification to NW side for alignment.
R2-2603592	Views on 6GR LCM and Model Transfer	ZTE Corporation, Beijing Digital Nebula, Sanechips	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.2-p011`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.2 AI/ML

```text
The 6GR applicability reporting shall meet the following requirement:1) Avoid the NW blindly configuring a formal inference configuration without any prior applicability information. 2)Support the update report to the NW for the applicability change of one inference configuration;
Not Treated
R2-2602956	LCM aspects for AIML and model transfer requirements	vivo	discussion	Rel-20
R2-2603045	LCM for 6G AIML use cases	NEC	discussion	Rel-20	FS_6G_Radio
R2-2603152	Discussion on 6G LCM Framework 	LG Electronics Finland	discussion	Rel-20	FS_6G_Radio
R2-2603178	Discussion on LCM of AIML use cases and model transfer	1Finity	discussion	Rel-20	FS_6G_Radio
R2-2603211	Discussion on AIML LCM and model transfer	CATT	discussion	Rel-20	FS_6G_Radio
R2-2603309	AI/ML LCM in 6G	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2603404	Discussions on AIML Use Case and Procedures 	Qualcomm Incorporated	discussion
R2-2603422	AIML LCM and model transfer for 6GR	InterDigital, Inc.	discussion	Rel-20	FS_6G_Radio
R2-2603561	Consideration on 6G AIML LCM and model transfer	Lenovo	discussion	Rel-20
R2-2603613	Discussion on Model transfer and AI/ML LCM in 6G	Tejas Networks Limited	discussion	Rel-20	FS_6G_Radio
R2-2603625	Views on 6GR general LCM aspects for AIML use cases	Sony	discussion	Rel-20	FS_6G_Radio
R2-2603713	Views on 6G AI/ML general framework and model transfer	Apple	discussion	Rel-20	FS_6G_Radio
R2-2603784	LCM of UE-sided models in 6G	Fraunhofer IIS, Fraunhofer HHI	discussion	R2-2602303
R2-2603802	Realistic LCM	MediaTek Beijing Inc.	discussion	Rel-20
R2-2603832	Discussion on LCM and model transfer in 6G	Ericsson, Verizon	discussion	Rel-20	FS_6G_Radio
R2-2603833	Discussion on AI/ML LCM and Model Transfer	Sharp	discussion
R2-2603892	Discussion on model transfer and AIML framework	Spreadtrum, UNISOC	discussion	Rel-20
R2-2603939	Analysis of Model Transfer and AI/ML	Kyocera	discussion
R2-2604004	Discussion on 6G AIML LCM	ASUSTeK	discussion	Rel-20
R2-2604014	Discussion on general LCM for AI/ML use cases and model transfer	Transsion Holdings	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.2-p012`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.2 AI/ML use cases

```text
In 6G, the model transfer should follow requirements:
•	Awareness: MNO can be aware of the existence of model.
•	Controllability: MNO can control the model transfer/delivery procedure (initiate, suspend, resume, stop etc.).
R2-2602216	Views on 6G AI/ML general framework and model transfer	Apple	discussion	Rel-20	FS_6G_Radio	Late
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.2-p001`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.2 AI/ML use cases

```text
UE-sided model transfer is transparent to NW and NW controllability is not needed.
R2-2602438	Discussion on general LCM and model transfer	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.2-p002`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.2 AI/ML use cases

```text
When the UE-sided model is trained by OTT server and stored outside 3GPP network, there is no requirements on controllability or visibility for model transfer/delivery. The model can be transferred to the UE directly from OTT-server (transparent to 3GPP).
Not treated
AIML LCM (if time allows)
NW-based vs. UE based management of AIML functionality
R2-2601813	Discussion on AIML framework and model transfer	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.2-p003`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.2 AI/ML use cases

```text
Network should have a control on whether the UE applies any AIML based functionality which may impact network QoS requirements, user experience or overall system performance.
R2-2602104	Discussion on general AIML framework and model transfer	Spreadtrum, UNISOC	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.2-p004`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.2 AI/ML use cases

```text
6G AI/ML LCM framework should support both UE-based and NW-based management for UE-sided model.
Fallback/switching between AIML and non-AIML functionality
R2-2602192	Views on 6GR LCM and Model Transfer	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.2-p005`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.2 AI/ML use cases

```text
The network shall be able to control the switch between AI/ML functionality and non-AI/ML functionality via: 1)Method 1: The network indicates/configures the UE to switch between AI/ML functionality and non-AI/ML functionality; 2)Method 2: The network controls whether the UE can autonomously switch between AI/ML functionality and non-AI/ML functionality, and the current status ( AI/ML functionality or non-AI functionality) shall be informed to the NW.
Functionality vs. Model based LCM
R2-2601512	Discussion on LCM and model transfer	Xiaomi	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.2-p006`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.2 AI/ML use cases

```text
RAN2 supports functionality-based LCM as baseline. FFS whether to support model-based LCM.
R2-2601938	Discussion on 6G AIML LCM	ASUSTeK	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.2-p007`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.2 AI/ML use cases

```text
Study model-based LCM in 6G.
Not treated
R2-2601455	LCM aspects for AIML and model transfer requirements	vivo	discussion	Rel-20
R2-2601475	Discussion on general LCM for AI/ML use cases and model transfer	Transsion Holdings	discussion	Rel-20
R2-2601594	LCM for 6G AIML use cases	NEC	discussion	Rel-20	FS_6G_Radio
R2-2601648	LCM and model transfer in 6GR	Samsung	discussion	Rel-20	FS_6G_Radio
R2-2601677	Discussion on AIML LCM and model transfer	CATT	discussion	Rel-20	FS_6G_Radio
R2-2601691	Discussion on 6G LCM Framework 	LG Electronics Finland	discussion	Rel-20	FS_6G_Radio
R2-2601755	Discussion on LCM and model transfer	OPPO	discussion	Rel-20
R2-2601771	Discussion on LCM of AI/ML use cases and model transfer	1Finity	discussion	Rel-20	FS_6G_Radio
R2-2601865	AI/ML LCM in 6G	Ofinno	discussion
R2-2601876	Discussions on AIML Use Case and Procedures 	Qualcomm Incorporated	discussion	Rel-20
R2-2601997	AIML LCM and model transfer for 6GR	InterDigital	discussion	Rel-20	FS_6G_Radio
R2-2602132	Consideration on 6G AIML LCM and model transfer	Lenovo	discussion	Rel-20
R2-2602142	Discussion on general AI/ML framework	TCL	discussion
R2-2602166	Views on 6GR general LCM aspects for AIML use cases	Sony	discussion	Rel-20	FS_6G_Radio
R2-2602297	AI/ML enablers and model transfer	Nokia, T-Mobile USA	discussion	Rel-20	FS_6G_Radio
R2-2602303	LCM of UE-sided models in 6G	Fraunhofer IIS, Fraunhofer HHI	discussion
R2-2602336	Discussion on LCM and model transfer in 6G	Ericsson, Verizon	discussion
R2-2602498	Analysis of Model Transfer	Kyocera	discussion
R2-2602584	Realistic LCM	MediaTek USA	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.2-p008`

### [6G/Rel-20 RAN2#133] `agreement` 10.3.3.2 AI/ML use cases

```text
-	Study UL traffic prediction. UL traffic prediction can be non-AI or AI based. Study what can be predicted and the benefits. Study what network needs to have some level of confidence in the prediction. Continue the discussion in UP.
R2-2600807	AI ML use cases	Ericsson	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-a001`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

```text
The following use cases concluded feasible in 5G-A study are considered also feasible and beneficial in 6G. No need to repeat simulation. RAN2 can directly study the potential solutions.
-	temporal domain cell level prediction (including case A and case B)
-	frequency(co-located) domain cell level RRM prediction
-	Event prediction
-	L3 beam level prediction
-	Qualcomm thinks that we didn’t do enough simulation for L3 beam level.  The scope was very narrow.   Nokia agrees and we didn’t evaluate all the sub-cases.
-	Apple thinks that we only did nw side for L3 beam level prediction and not UE side.
-	Oppo thinks that if we do L1 beam level prediction in Ran1 it is similar so we shouldn’t repeat.
-	Vivo doesn’t thinks we need to do simulation again.
-	Huawei thinks that we did conclude it was feasible and the reason why didn’t specify it was because of RAN4 impact so we don’t need to do anything additional.
-	Samsung thinks that for measurement event prediction we mainly evaluated temporal domain.
-	Interdigital thinks we should prioritize the mobility use cases. Oppo agrees. Xiaomi thinks that we need to wait for AI mobility.
Noted
R2-2600887	On AI/ML use cases and enablers	Nokia	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p001`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

```text
When studying AI Mobility use-cases, endorse at least the following principles for the 6G Rel. 20 SI:
1)	Aim to minimize overlap with ongoing Rel. 20 5G WI on AI Mobility.
2)	There should be clear assumptions on the 6G Mobility procedure for which the AI enhancements are being studied.
3)	There should be clear assumptions on data collection and model transfer/delivery framework.
4)	6G evaluation assumptions studied in Rel-20 should be considered in the 6G AI/ML mobility evaluations.
Noted
R2-2600066	Views on AI/ML use cases	OPPO	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p002`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

```text
RAN2 is proposed to first concentrate on evaluating the motivation and potential performance gains of introducing AI/ML for the new use cases. The aspects of model complexity and memory footprint are preliminarily assessed as non-critical barriers and can be addressed in detailed specification phases.
-	Samsung thinks that for energy saving model complexity should be considered as critical since the energy saving gains may be less than the energy consumption of the model inference. Xiaomi wonders how we can evaluate that.   Samsung agrees and that is the missing point.
-	MEdiatek agrees for the cases we have studied but for new use cases complexity needs to be considered. It should be welcomed if companies can do it but not mandatory.
Noted
Not treated
AIML use cases
L1/L3 measurement and event prediction
R2-2600840	Discussions on RAN2 6G AI/ML Use Cases	Qualcomm Incorporated	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p003`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

```text
RAN2 should build on RAN1 agreed use cases for inter-cell and inter-frequency L1/L3 beam measurement prediction for AI/ML-based mobility. While RAN1’s output is L1 beam measurement prediction, RAN2 can work on cell-level measurement, L3 beam measurement prediction, and L1/L3 event predictions.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p004`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

```text
Please refer to Table 2 for justification, and others for additional sub-use cases listed in Table 1.
R2-2600378	Discussion on 6G AI Mobility Use Cases 	MediaTek Inc.	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p005`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

```text
RAN2 study RRM measurement prediction for non-co-located scenarios in 6G, including but not limited to:
• Non-co-located inter-frequency inter-cell prediction.
• Non-co-located inter-frequency intra-cell prediction with different beam patterns..
R2-2600887	On AI/ML use cases and enablers	Nokia	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p006`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

```text
Consider the following AI mobility use cases in the 6G SI: RRM Measurement prediction; Measurement event prediction; Spatial domain RRM measurement prediction; and L3 beam prediction.
R2-2600105	Discussion on AI/ML use cases and LCM	Xiaomi	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p007`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

```text
For RRM prediction use cases other than temporal domain and frequency domain (co-located) L3 cell/beam level prediction,
-	RAN2 is responsible for
	Mobility performance gain evaluation,
	LCM enhancement
	Data collection
	Spec impact of AI mobility enhancement
-	RAN4 is responsible for,
	Prediction accuracy evaluation
	Requirements
	Testability and interoperability
-	RAN2 postpone the RRM prediction use cases study until RAN4 concluds prediction accuracy evaluation
R2-2600418	Discussion on AIML use cases and AIML framework	Huawei, HiSilicon	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p008`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

```text
Consider RRM measurement prediction and mobility event prediction as use cases to be studied as soon as the L1, L3 measurement and mobility framework design for 6G becomes clearer.
LTM/CHO
R2-2600562	Considerations On New AIML Use Cases in RAN2	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p009`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

```text
For 6G AI/ML assisted mobility, extend AI/ML into LTM scenario, i.e. support AI/ML based LTM as 6G AIML use case in RAN2.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p010`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

```text
For AI/ML-assisted LTM, with the goal of measurement efforts reduction and handover performance improvement, RAN2 to support: 1)AI/ML based L1 measurement prediction with UE side model and NW side model; 2) AI/ML based L1 measurement event prediction with UE side model, and it can be up to NW implementation to perform L1 event prediction with NW side model.
Note: Simulations are need for AI/ML based L1 measurement prediction and L1 measurement event prediction. When performing simulation, the study progress of 6G mobility framework shall be considered.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p011`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

```text
For AI/ML-assisted LTM, to support: 1)AI/ML based early downlink sync prediction: to predict activated /deactivated TCI state; 2)AI/ML based early uplink sync prediction: to predict TA value; 3)AI/ML based target cell prediction: to predict target cell.
-	Ericsson thinks we don’t know yet what will happen with 6G mobility so we should discuss that first.
-	Apple agrees to study LTM, for L1 prediction we can use RAN1 evaluation for 5G.  6G will likely have LTM so we can assume it is there.
-	Xiaomi thinks that TCI state and TA prediction would have to be done by RAN1 and also L1 beam prediction can be done in RAN1.
-	LG thinks that TA prediction was done in RAN3.
-	Lenovo supports to study in 6G, the only thing that RAN1 needs to study is the L1 event prediction.
-	Qualcomm asks what does it imply.   Apple thinks that the only thing RAN2 needs to worry is the L1 event prediction and TA is already done in RAN2.
-	CATT doesn’t think we need anymore inputs from RAN1.   For UE sided model TA prediction would be something new to evaluate.
-	Nokia reminds that the study in RAN1 was intra-cell.  Also thinks we don’t know exactly what 6G mobility.  Huawei doesn’t agree for RAN1 as it not using one cell measurement to predict another cell.
-	Huawei agrees we should consider it and the only new thing is TA prediction.    Early CSI prediction could be useful but it is more in RAN1 scope.
-	docomo thinks that we need to study inter-cell prediction.  ZTE thinks that we need to study inter-cell prediction, and it is also a RAN1 use case, but RAN2 can do the simulation for both inter-cell and L1 event prediction.
-	Samsung asks if TA prediction is for RACH-less LTM or for CG SDT.    Vivo thinks that the baseline is for RACH-less.
-	Fujitsu thinks that if we have done L1 measurement predictions why do we need to do L1 event prediction.
-	Mediatek thinks that we may not even need AI to do TA prediction and if the network is not synchronized this is not very useful.   We should think of complexity if the network can do it then we don’t need to do it in UE.   Ericsson agrees with Mediatek and it is very difficult for the UE to do it.
-	Mediatek thinks that we would need to do system level evaluation and that is RAN2 domain.
-	Xiaomi asks if RAN3 can do the TA prediction why do we have to do it in the UE.
-	Ericsson thinks that the workload should be taken into account.
TA prediction FFS
Noted
R2-2600953	Discussion on potential AIML use cases in 6G	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p012`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

```text
RAN2 is proposed to study AI/ML based pre-configured mobility prediction, e.g. CHO/CLTM prediction in 6G. The Table 4 can be considered as starting point.
Not treated
Agreements on AI/ML use cases
1	The following use cases concluded feasible in 5G-A study are considered also feasible from RAN2 point of view and beneficial in 6G. No need to repeat simulation. RAN2 can directly study the potential solutions.
-	temporal domain cell level prediction (including case A and case B)
-	frequency(co-located) domain cell level RRM prediction
-	Measurement Event prediction (A1-A6)
-	L3 beam level prediction (limited only to what was studied in RAN2) NOTE: can revisit if we decised to support L3 beam level if something additional needs to be evaluated studied.
2	Starting point – RAN2 will support at least the cases supported in Rel-20 AI Mobility from 5G.  The mechanisms will be adapted to fit the 6G framework for mobility.
3	RRM measurement prediction and mobility event prediction as use cases to be studied as soon as the L1, L3 measurement and mobility framework design for 6G becomes clearer.
4	Evaluations should focus on the motivation and potential performance gains of introducing AI/ML for the new use cases.  Complexity evaluation may depend on use cases and ability to be evaluated.
5	Desire to study AI assisted Lower layer Mobility.    To study AI assisted lower layer mobility, at least the following evaluation needs to be done temporal and frequency domain L1 measurements and L1 event prediction.   RAN2 can do these two evaluations (if needed).  Discuss in plenary how to coordinate the work.  Whether we will have Lower layer mobility depends on 6G mobility framework discussion.
Traffic prediction
R2-2600461	Views on 6G AI/ML use cases	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p013`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

```text
Study UL traffic prediction for L2 scheduling enhancement as one RAN2-led 6G AI/ML use case.
Use case description:
Use predicted UL traffic information to enhance the L2 scheduling (UE-side model), which at least includes
•	BSR with predicted traffic information to reduce scheduling latency
•	Avoidance of LCH starvation according to predicated traffic
FFS other L2 feature
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p014`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

```text
For UL traffic prediction for L2 scheduling enhancement, RAN2 study the following aspects:
•	Evaluation of prediction accuracy with aligned traffic model to identify applicable traffic types and performance. FFS whether 3GPP specified traffic model or field dataset with different traffic types.
•	Granularity of traffic prediction, e.g. per QoS flow or per LCH or others.
•	Other L2 features besides BSR and LCP, with consideration of latest progress of 6G UP.
•	Potential specification impacts.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p015`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

```text
RAN2 discuss the following aspects to determine how to study DL traffic prediction for UE/NW energy efficiency (e.g. enhance UE CDRX and Cell DTX/DRX) as one 6G AI/ML use case:
•	Whether predicted is performed in UE or NW.
•	Whether / How to evaluate performance
•	Cross-WG impacts, e.g. NW/UE power consumption model
Noted
Discussion on UL traffic prediction
-	Ericsson thinks that should study UL and DL traffic but we should study what we should do.
-	ZTE agrees that BSR prediction is beneficial but it appears that the focus in only UE sided.   Apple explains that it is only for UL traffic it should be UE sided.
-	Oppo thinks that we don’t need to do system level simulation, so we should consider an intermediate KPI.  Apple agrees as it is very difficult otherwise.
-	Interdigital is not sure this is an AI discussion as for example we don’t need performance monitoring or other LCM framework.   There are benefits but it is not an AI/ML use cases, the UE can by implementation use AI to predict BSR.   Apple wants to use LCM for this procedure as the network doesn’t trust the UE.   Qualcomm thinks we would just need to think which part of the LCM procedure should be considered or not.
-	LG also thinks that this is not only applicable to AI/ML.  There are proposals in the UP section on prediction of BSR and should be discussed together with scheduling enhancements.   Huawei agrees with LG and it would be good to keep them in one place.   Prediction on historical traffic to predict BSR is one way but it is not the only way.    Also agree with interdigital that we won’t have LCM framework.   Nokia also agrees that this is more a UP topic rather than AI/ML and it is unclear what are the specification impact.
-	Xiaomi sees some difference in UP solution and AI, as the UE for UP enhancements can be done by the UE always and the network may need to check so we may need applicability reporting.   LG reminds that we shouldn’t have different solutions.
-	ZTE is concerned that with UP prediction solutions we may never have performance monitoring.  Vivo agrees and another point is that we should have applicability reporting.
-	Nokia asks that we are not sure why we have to run a simulation evaluation, we need to have some level of trust between the UE and network.
-	Oppo thinks we need to perform simulation to show that it has benefits.  CATT thinks that UP session should only consider non-AI and here we should understand whether the UE can do prediction accurately enough.
-	Qualcomm thinks that there are different ways to predict UL some AI and some non-AI based and the solutions can be common for both.   Ericsson thinks that some performance monitoring is needed.    Interdigital thinks that the network can tell the ground truth based on what data is actually transmitted so we don’t necessarily need special performance monitoring.  Nokia agrees, if the UE over predicts the BSR the network will see it.
-	ATT thinks that this a buffer prediction but perhaps we can use this information in other cases.  This is not necessarily just a UE sided model and network can maybe come up with good models.
-	Lenovo thinks that we don’t need to care where we get the information of predicting, either application or AI.   We don’t need to have all LCM, and reminds everyone that BSR itself is not perfect so we may need something to give the network some confidence.  Interdigital think there can be some performance monitoring but doesn’t have to be the full blown LCM.  Mediatek agrees.
-	CMCC agrees that we need performance monitoring.
On DL traffic prediction
-	Qualcomm, Vivo and Xiaomi think we can do DL prediction in the UE. Huawei, LG and Nokia thinks we should prioritize UL and keep in mind the workload. LG further clarifies that there is DRX enhancements so it should be discussed with those UP enhancements.
-	ZTE thinks that the UE needs to offload the network load.
-	Mediatek thinks that the amount of things being brought are quite a lot.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p016`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

```text
Study support for traffic predictions in 6G. The following use cases are included:
•	Setting up/releasing/activating/deactivating carrier aggregation.
•	State transitions, e.g. transfer from RRC_IDLE/RRC_INACTIVE to RRC_CONNECTED or vice versa or to/from battery saving mode.
•	Mobility decision for load balancing purposes.
Noted
R2-2601342	Report of AIML use case discussion	InterDigital (Rapporteur)	report	Rel-20		FS_6G_Radio
Noted
-	Xiaomi thinks that UP can apply to both UL and DL.  Nokia has serious concerns about DL.
Table in R2-2601349 is used a baseline for further offline discussion.
| Agreements from offline (the table discussed in post meeting email discussion will reflect the latest agreements from online): There is a desire in RAN2 to study L3 measurement prediction for non-co-located scenarios in 6G, including e.g.: • Non-co-located inter-frequency inter-cell prediction. • inter-frequency co-sited prediction with different beam patterns/sectors. However RAN2 understands this is currently being worked on by RAN4 (e.g., they are doing the simulation). RAN2 scope (if needed) can wait for RAN plenary decision. This can be captured as a note in the table and coordinated at plenary. RAN2 Consider the following AI mobility use cases in the 6G SI: intra/inter cell L1 beam spatial domain prediction; and L3 beam spatial/temporal/frequency prediction. Coordination is needed with RAN1/RAN4 (e.g., regarding simulations, lead WG). This can be captured as a note in the table and coordinated at plenary. RAN2 understands that conditional mobility can be a possible use case/motivation for AIML measurement event prediction. This will be captured in the table under the “motivation” section for L3/L1 event prediction. The table will include a note that whether we will have conditional depends on 6G mobility framework discussion. RAN2 includes RLF prediction/recovery in the AIML use case table. The need for simulations is FFS and can be discussed in plenary. This will be listed as second priority Study the AI/ML based TA prediction in 6G. Issues on synchronization, complexity, and use of UE-side vs. NW-side model will be included in the notes. Coordination may be needed with RAN1 (e.g., regarding simulations). This will be listed as second priority Study traffic predictions for CP in 6G. The following use cases are included: • Setting up/releasing/activating/deactivating carrier aggregation. • State transitions, e.g. transfer from RRC_IDLE/RRC_INACTIVE to RRC_CONNECTED or vice versa or to/from battery saving mode. • Mobility decision for load balancing purposes. Traffic prediction for this case can be non-AI or AI based and can apply to both UL and DL. Can continue the discussion in CP. |
| --- |
R2-2601349	AIML use case draft table	Chairlady	discussion	Rel-20	FS_6G_Radio
The table will be used as a baseline for RAN2 email discussion.
The priorities in the table are considered agreed and will not be discussed in the email discussion
[POST133][010][6G AI] Use cases (InterDigital)
Intended outcome: review updated table to be brought to RAN plenary.  Review should focus on content of the table and not the agreed priorities
Deadline:  short
=> Noted in R2-2601385
Failure prediction (RLF/HOF/BFD)
R2-2600756	Consideration on 6G AIML use cases	Lenovo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p017`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

```text
RAN2 resumes the study on RLF prediction based on the progress in 5GA Rel19 AI for mobility study. The input can be at least measured/predicted L1 SINR of the PCell.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p018`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

```text
RAN2 resumes the study on MOF prediction based on the progress in 5GA Rel19 AI for mobility study, focusing on the “too early handover” and “handover to wrong cell” sub-scenarios wherein RLF occurs shortly after successful handover. The input can be at least measured/predicted L1 SINR of the candidate target cells.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p019`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

```text
RAN2 studies the use case of BFD prediction by considering at least the measured/predicted L1 SINR of the associated cells as input information.
R2-2600195	AIML use cases in 6G	CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p020`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

```text
It is recommended to perform the 6G AI/ML use case studies as below:
-	For 5G legacy use cases, reuse the evaluation results of Rel-19 RRM measurement prediction and measurement event prediction until the 6G RRM mechanisms are defined. RLF prediction study is excluded for now;
TA prediction
R2-2600085	Discussion on 6GR AIML use cases and framework	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p021`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

```text
Study the AI/ML based TA prediction in 6G. The predicted TA values can be leveraged to minimize the reliance on RACH-based synchronization across all RRC states (e.g., RACH-less handover, STAG TA establishment, CG-SDT).
LCM framework (if time allows)
R2-2600663	Discussion on general AIML framework	Spreadtrum, UNISOC	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p022`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

```text
6G AI/ML LCM framework should support both one-sided and two-sided model.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p023`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

```text
6G AI/ML LCM framework should support both functionality-based LCM and model ID-based LCM.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p024`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

```text
6G AI/ML LCM framework should support both UE-based and NW-based management for UE-sided model.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p025`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

```text
A unified cross-WGs AI/ML framework can be considered. Coordinate with RAN3 and SA if necessary.
R2-2600418	Discussion on AIML use cases and AIML framework	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p026`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

```text
Network should have a control on whether the UE applies any AIML based functionality which may impact network QoS requirements, user experience or overall system performance.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p027`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

```text
For all AIML use cases, the network needs to be able to evaluate AIML functionality performance and disable under-performing AIML functionalities as soon as possible.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p028`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

```text
For NW-sided models, reuse an approach from 5G-A that no LCM functions other than network-side data collection (e.g. for training) are specified (i.e. they are left to network implementation).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p029`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

```text
RAN2 should study impacts of online training on the AIML procedures such as data collection and functionality management.
Not treated
R2-2600116	Discussion on 6GR energy efficiency	Xiaomi	discussion	Rel-20	FS_6G_Radio	Withdrawn
R2-2600269	AIML use case and AIML framework for 6G	NEC	discussion	Rel-20	FS_6G_Radio
R2-2600281	Discussion on RLF prediction in 6GR	Samsung, NTT DOCOMO	discussion
R2-2600286	Discussion on uses cases for 6GR AIML	Transsion Holdings	discussion
R2-2600329	Discussion on AI/ML use cases	LG Electronics	discussion	Rel-20	FS_6G_Radio
R2-2600354	Discussion on RAN2 led AI/ML use cases	Fujitsu	discussion	Rel-20	FS_6G_Radio
R2-2600618	Discussions on AI/ML framework and use cases	NTT DOCOMO, INC.	discussion
R2-2600696	AI-Based Optimization of RRC Configuration Parameters Using UE-Side Models	KDDI Corporation (TTC)	discussion
R2-2600764	Discussions on new AIML use case: Intelligent Data Collection based on Data Utility	Sony	discussion	Rel-20	FS_6G_Radio
R2-2600812	Considerations on AI/ML use cases for connected mode mobility in 6GR	AUMOVIO	discussion
R2-2600814	AI/ML Use cases	SHARP Corporation	discussion
R2-2600864	AI/ML use cases in 6G	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2600892	Discussion on AI/ML use cases	AT&T	discussion	FS_6G_Radio
R2-2601019	L2/L3 AIML use cases for 6GR	InterDigital	discussion	Rel-20	FS_6G_Radio
R2-2601028	Discussion on AI/ML Use Cases	Futurewei Technologies	discussion	Rel-20
R2-2601052	Consideration on the New Use Case for AI/ML	China Unicom	discussion
=> Revised in R2-2601083
R2-2601083	Consideration on the New Use Case for AI/ML	China Unicom, BUPT	discussion	R2-2601052
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p030`

