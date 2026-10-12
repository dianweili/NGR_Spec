# 6GR AI/ML 协议支持

**当前进展** · 阶段：收敛中

RAN2 已将多类 AI/ML 用例纳入 6G 研究，包括 RRM 与波束预测、LTM、UL/DL traffic prediction、RLF/MOF/BFD 及 TA prediction，并对部分 5G-A 已验证用例同意无需重复仿真。研究方向逐渐明确：AI/ML 机制需适配 6G mobility framework，网络需能评估功能表现并及时停用表现不佳的功能，functionality-based LCM 已作为基线。UE-side model transfer 的共识是网络应能识别经 3GPP 传输的模型流量，但无需获知模型内容；transparent/OTT approach 是基线，具体控制机制仍在研究。整体仍处于方案收敛阶段，多个用例的评估方法、规范影响和 LCM 细节尚未确定。

**未决问题**

- 是否支持 model-based LCM，以及 LCM 决策由网络发起、UE 发起还是由 UE 自主作出。
- UE-side model transfer 的 network controllability 机制及其功能，以及基于 UP 的其他传输方案。
- UL traffic prediction 的评估流量模型、预测粒度，以及 BSR/LCP 之外的 L2 用途仍待确定；DL prediction 的执行位置、性能评估和功耗模型也待研究。
- RRM measurement prediction 和 mobility event prediction 的研究需等待 6G measurement 与 mobility framework 更明确；部分用例还涉及预测精度、仿真范围和评估责任划分。
- AI/ML-assisted LTM 的 TA prediction 结论仍为 FFS；其他预测用例的仿真与规范影响也待研究。
- 低时延双向 fallback、performance monitoring 方案及 applicability reporting 的具体机制仍需研究。

## 6GR 演进

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.2 AI/ML

对于 UE-sided model，network 需要知道传输对象是 model，但无需知道其内容或详细 meta info，以避免对其他 traffic 造成影响。Network 可以控制是否以及何时向 UE transfer/delivery 该 model。

```text
For UE-sided model, the network needs to be aware that it is a model (without being aware of model content or detailed meta info) to avoid the impacts on other traffic, e.g. whether and when to transfer/delivery the model to the UE can be controlled by the network.
Noted
R2-2603447	Discussion on LCM framework for AL/ML	China Unicom	discussion	Late
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.2-p001`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.2 AI/ML

对于 one sided UE models，模型存储在 3GPP 之外时，model transfer 可对 3GPP 保持透明；存储在 3GPP 内时，网络应具备部分可见性（知晓 model 与 non model）以及 transfer controllability。

```text
For one sided UE models:
- When stored outside 3GPP, model transfer may remain transparent to 3GPP.
- When stored inside 3GPP, the network shall have partial visibility (awareness of model vs. non model) and controllability of transfer.
Noted
R2-2603281	Discussion on AI/ML LCM and model transfer	Futurewei Technologies	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.2-p002`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.2 AI/ML

RAN2 将 transparent/OTT approach 作为 6G UE-side model transfer 的基线；其他基于 UP 的方案仍待研究。

```text
RAN2 to adopt the transparent/OTT approach as the baseline for UE-side model transfer in 6G. FFS other UP-based approaches.
Noted
MNO control of model transfer
R2-2604073	Discussion on model transfer	NTT DOCOMO, Nokia, Ericsson, CMCC, Verizon, Turkcell, T-Mobile USA	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.2-p003`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.2 AI/ML

RAN2 将研究 UE server 到 UE 的 model transfer 是否需要受 RAN2 影响的 network controllability mechanism，以及其功能。初步提出网络可允许或禁止 transfer procedure，并可停止、暂停或恢复该 procedure。

```text
About model transfer from UE server to the UE in 6G, RAN2 to study whether RAN2-impacted mechanism of network controllability is needed and what is the function of the network controllability if needed. As the starting point, the function of the network controllability is following.
- Network can allow/prohibit the procedure of model transfer.
- Network can stop/suspend/resume the procedure of model transfer.
Noted
R2-2603713	Views on 6G AI/ML general framework and model transfer	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.2-p004`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.2 AI/ML

就 UE-sided model transfer，RAN2 记录的共识是 MNO 应能知晓经 3GPP 进行的 model transfer，以便区分 user traffic 与 model transfer traffic，并可调整优先级；无需了解模型内容，也无意由 MNO 禁止 UE 进行 transfer。如何实现不在 RAN2 范围内，可能由 CN mechanisms（如 QoS、PDU session management）实现，并已批准向 SA2 发送 LS。

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

对于 NW-sided models，沿用 5G-A 的做法：除 network-side data collection（例如用于 training）外，不规定其他 LCM functions，相关功能留给 network implementation。

```text
For NW-sided models, reuse an approach from 5G-A that no LCM functions other than network-side data collection (e.g. for training) are specified (i.e. they are left to network implementation).
R2-2603279	LCM and model transfer in 6GR	Samsung	discussion	Rel-20	FS_6G_Radio	R2-2601648
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.2-p006`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.2 AI/ML

RAN2 将考虑把 Rel-19 AI/ML PHY 定义的 common procedures（UE capabilities、applicability determination、inference、performance monitoring、data collection）作为 unified LCM framework 的基线。各 6G AI/ML use case 的详细 signaling messages 和 parameters 分别研究。

```text
RAN2 to consider the common procedures (i.e., UE capabilities, applicability determination, inference, performance monitoring, data collection) defined in Rel-19 AI/ML PHY as baseline for unified LCM framework. However, detailed signaling messages and parameters are studied separately for each 6G AI/ML use case.
R2-2603069	Discussion on LCM and model transfer	OPPO	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.2-p007`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.2 AI/ML

Functionality-based LCM 应作为 6G 的基线。

```text
Functionality-based LCM should be the baseline in 6G.
AIML LCM (if time allows)
R2-2602967	Discussion on LCM and model transfer	Xiaomi	discussion	Rel-20	FS_6G_Radio	R2-2601512
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.2-p008`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.2 AI/ML

RAN2 将研究由 network 或 UE 发起的 LCM decision 方案。备选方式包括 network 决策（network-initiated 或 UE-initiated 并请求 network），以及 UE 决策（由 network 配置事件触发或 UE-autonomous，且 UE decision 会报告给 network）。

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

研究低时延（fast, one signalling step）的 fallback mechanisms 可行性，以支持 AI/ML-enabled configuration 与 non-AI/ML-enabled configuration 之间的双向切换。

```text
Study the feasibility of fallback mechanisms for low-latency (fast, one signalling step), bidirectional switching between an AI/ML-enabled configuration and a non-AI/ML-enabled configuration.
R2-2603069	Discussion on LCM and model transfer	OPPO	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.2-p010`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.2 AI/ML

performance monitoring 的后续研究方向包括：NW-sided model 的 UE assisted performance monitoring，以及 UE-sided model 的五种场景，涵盖 NW 或 UE 执行监测、management decision 由 NW 或 UE 作出，以及 decision 是否发送至 NW 或用于 alignment。

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

6GR applicability reporting 应避免 NW 在没有先验适用性信息时盲目配置 formal inference configuration，并支持向 NW 报告单个 inference configuration 的适用性变化。

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

提出 6G model transfer 应满足 awareness 和 controllability 要求：MNO 可知晓 model 的存在，并可控制 model transfer/delivery procedure，包括 initiate、suspend、resume 和 stop。

```text
In 6G, the model transfer should follow requirements:
•	Awareness: MNO can be aware of the existence of model.
•	Controllability: MNO can control the model transfer/delivery procedure (initiate, suspend, resume, stop etc.).
R2-2602216	Views on 6G AI/ML general framework and model transfer	Apple	discussion	Rel-20	FS_6G_Radio	Late
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.2-p001`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.2 AI/ML use cases

提出 UE-sided model transfer 对 NW 透明，因此不需要 NW controllability。

```text
UE-sided model transfer is transparent to NW and NW controllability is not needed.
R2-2602438	Discussion on general LCM and model transfer	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.2-p002`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.2 AI/ML use cases

对于由 OTT server 训练并存储在 3GPP network 外的 UE-sided model，提出 model transfer/delivery 无需 controllability 或 visibility；model 可由 OTT-server 直接传至 UE，且对 3GPP 透明。该提议标记为 Not treated。

```text
When the UE-sided model is trained by OTT server and stored outside 3GPP network, there is no requirements on controllability or visibility for model transfer/delivery. The model can be transferred to the UE directly from OTT-server (transparent to 3GPP).
Not treated
AIML LCM (if time allows)
NW-based vs. UE based management of AIML functionality
R2-2601813	Discussion on AIML framework and model transfer	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.2-p003`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.2 AI/ML use cases

提出 network 应能控制 UE 是否应用可能影响 network QoS requirements、user experience 或 overall system performance 的 AIML based functionality。

```text
Network should have a control on whether the UE applies any AIML based functionality which may impact network QoS requirements, user experience or overall system performance.
R2-2602104	Discussion on general AIML framework and model transfer	Spreadtrum, UNISOC	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.2-p004`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.2 AI/ML use cases

提出 6G AI/ML LCM framework 应支持对 UE-sided model 采用 UE-based 和 NW-based 两种管理方式。

```text
6G AI/ML LCM framework should support both UE-based and NW-based management for UE-sided model.
Fallback/switching between AIML and non-AIML functionality
R2-2602192	Views on 6GR LCM and Model Transfer	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.2-p005`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.2 AI/ML use cases

提出 network 应能控制 UE 在 AI/ML 与 non-AI/ML functionality 间的切换：可指示或配置 UE 切换，也可控制 UE 是否能自主切换，并要求将当前状态通知 NW。

```text
The network shall be able to control the switch between AI/ML functionality and non-AI/ML functionality via: 1)Method 1: The network indicates/configures the UE to switch between AI/ML functionality and non-AI/ML functionality; 2)Method 2: The network controls whether the UE can autonomously switch between AI/ML functionality and non-AI/ML functionality, and the current status ( AI/ML functionality or non-AI functionality) shall be informed to the NW.
Functionality vs. Model based LCM
R2-2601512	Discussion on LCM and model transfer	Xiaomi	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.2-p006`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.2 AI/ML use cases

RAN2 支持 functionality-based LCM 作为 baseline；是否支持 model-based LCM 仍待进一步研究（FFS）。

```text
RAN2 supports functionality-based LCM as baseline. FFS whether to support model-based LCM.
R2-2601938	Discussion on 6G AIML LCM	ASUSTeK	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.2-p007`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.2 AI/ML use cases

提出在 6G 中研究 model-based LCM。该提议标记为 Not treated。

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

研究 UL traffic prediction，可采用 non-AI 或 AI-based 方法；研究可预测的内容及其收益，并研究网络需要对预测具备何种程度的 confidence。相关讨论在 UP 继续。

```text
-	Study UL traffic prediction. UL traffic prediction can be non-AI or AI based. Study what can be predicted and the benefits. Study what network needs to have some level of confidence in the prediction. Continue the discussion in UP.
R2-2600807	AI ML use cases	Ericsson	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-a001`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

认定 5G-A 研究中结论为可行的 temporal domain cell level prediction、frequency (co-located) domain cell level RRM prediction、event prediction 和 L3 beam level prediction，在 6G 中也被认为可行且有益，因此无需重复仿真，可直接研究潜在方案。对 L3 beam level prediction 的仿真范围和覆盖子场景是否充分，以及是否仅评估 network side 等意见存在讨论。

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

研究 AI Mobility use-cases 时，Rel. 20 SI 至少应遵循四项原则：尽量减少与 ongoing Rel. 20 5G WI on AI Mobility 的重叠；明确所研究 AI enhancements 对应的 6G Mobility procedure 假设；明确 data collection 和 model transfer/delivery framework 假设；并在 6G AI/ML mobility evaluation 中考虑 Rel-20 的 6G evaluation assumptions。

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

建议 RAN2 优先评估新 use cases 引入 AI/ML 的动机和潜在性能增益，并初步认为 model complexity 和 memory footprint 并非关键障碍，可在详细规范阶段处理。讨论中提出，对于 energy saving，应考虑模型推理能耗可能抵消节能收益；对新 use cases，复杂度评估可由公司开展但不强制。

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

RAN2 应基于 RAN1 已同意的 inter-cell 和 inter-frequency L1/L3 beam measurement prediction use cases 开展 AI/ML-based mobility 研究。RAN2 可研究 cell-level measurement、L3 beam measurement prediction 及 L1/L3 event predictions。

```text
RAN2 should build on RAN1 agreed use cases for inter-cell and inter-frequency L1/L3 beam measurement prediction for AI/ML-based mobility. While RAN1’s output is L1 beam measurement prediction, RAN2 can work on cell-level measurement, L3 beam measurement prediction, and L1/L3 event predictions.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p004`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

该条目请参阅 Table 2 获取 justification，并参阅其他表格内容了解 Table 1 所列的 additional sub-use cases。

```text
Please refer to Table 2 for justification, and others for additional sub-use cases listed in Table 1.
R2-2600378	Discussion on 6G AI Mobility Use Cases 	MediaTek Inc.	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p005`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

建议 6G 研究 non-co-located 场景下的 RRM measurement prediction，包括 non-co-located inter-frequency inter-cell prediction，以及采用不同 beam patterns 的 non-co-located inter-frequency intra-cell prediction。

```text
RAN2 study RRM measurement prediction for non-co-located scenarios in 6G, including but not limited to:
• Non-co-located inter-frequency inter-cell prediction.
• Non-co-located inter-frequency intra-cell prediction with different beam patterns..
R2-2600887	On AI/ML use cases and enablers	Nokia	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p006`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

建议在 6G SI 中考虑以下 AI mobility use cases：RRM Measurement prediction、Measurement event prediction、Spatial domain RRM measurement prediction 和 L3 beam prediction。

```text
Consider the following AI mobility use cases in the 6G SI: RRM Measurement prediction; Measurement event prediction; Spatial domain RRM measurement prediction; and L3 beam prediction.
R2-2600105	Discussion on AI/ML use cases and LCM	Xiaomi	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p007`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

对于时域和频域（同址）L3 小区/波束级预测以外的 RRM prediction use cases，RAN2 负责 mobility performance gain evaluation、LCM enhancement、data collection 和 AI mobility enhancement 的规范影响；RAN4 负责 prediction accuracy evaluation、requirements、testability 和 interoperability。RAN2 将 RRM prediction use cases 研究推迟至 RAN4 完成 prediction accuracy evaluation 后。

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

将 RRM measurement prediction 和 mobility event prediction 作为待研究用例，研究时机为 6G 的 L1、L3 measurement 和 mobility framework design 更明确之后。

```text
Consider RRM measurement prediction and mobility event prediction as use cases to be studied as soon as the L1, L3 measurement and mobility framework design for 6G becomes clearer.
LTM/CHO
R2-2600562	Considerations On New AIML Use Cases in RAN2	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p009`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

将 AI/ML 扩展到 LTM 场景，支持 AI/ML based LTM 作为 6G AIML use case 纳入 RAN2 研究。

```text
For 6G AI/ML assisted mobility, extend AI/ML into LTM scenario, i.e. support AI/ML based LTM as 6G AIML use case in RAN2.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p010`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

对于 AI/ML-assisted LTM，为减少 measurement efforts 并提升 handover performance，RAN2 支持基于 UE-side model 和 NW-side model 的 AI/ML based L1 measurement prediction，以及基于 UE-side model 的 AI/ML based L1 measurement event prediction；NW-side model 的 L1 event prediction 可由网络实现决定。相关预测需要进行 simulations，且应考虑 6G mobility framework 的研究进展。

```text
For AI/ML-assisted LTM, with the goal of measurement efforts reduction and handover performance improvement, RAN2 to support: 1)AI/ML based L1 measurement prediction with UE side model and NW side model; 2) AI/ML based L1 measurement event prediction with UE side model, and it can be up to NW implementation to perform L1 event prediction with NW side model.
Note: Simulations are need for AI/ML based L1 measurement prediction and L1 measurement event prediction. When performing simulation, the study progress of 6G mobility framework shall be considered.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p011`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

提出 AI/ML-assisted LTM 支持 early downlink sync prediction（预测 activated/deactivated TCI state）、early uplink sync prediction（预测 TA value）和 target cell prediction。关于 TA prediction 的结论为 FFS。

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

RAN2 认为 5G-A study 中已确认可行且有益的时域小区级、频域（同址）小区级 RRM、Measurement Event（A1-A6）及限定范围内的 L3 beam level prediction 用例，在 6G 也可行，无需重复 simulation，可直接研究潜在方案。RAN2 至少以 Rel-20 AI Mobility 支持的用例为起点，并将机制适配 6G mobility framework；RRM measurement prediction 和 mobility event prediction 待 6G 测量与 mobility framework 更明确后研究。

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

将 UL traffic prediction 用于 L2 scheduling enhancement 列为 RAN2 主导的 6G AI/ML use case，采用 UE-side model。预测的 UL traffic information 至少用于携带预测流量信息的 BSR 以降低 scheduling latency，以及避免 LCH starvation；其他 L2 feature 为 FFS。

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

针对用于 L2 scheduling enhancement 的 UL traffic prediction，RAN2 研究基于一致 traffic model 的 prediction accuracy evaluation，以识别适用流量类型和性能；采用 3GPP 指定 traffic model 还是不同流量类型的 field dataset 仍为 FFS。研究内容还包括预测粒度、除 BSR 和 LCP 外的其他 L2 features（考虑 6G UP 最新进展）以及潜在规范影响。

```text
For UL traffic prediction for L2 scheduling enhancement, RAN2 study the following aspects:
•	Evaluation of prediction accuracy with aligned traffic model to identify applicable traffic types and performance. FFS whether 3GPP specified traffic model or field dataset with different traffic types.
•	Granularity of traffic prediction, e.g. per QoS flow or per LCH or others.
•	Other L2 features besides BSR and LCP, with consideration of latest progress of 6G UP.
•	Potential specification impacts.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p015`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

RAN2 将讨论如何研究用于 UE/NW energy efficiency（例如增强 UE CDRX 和 Cell DTX/DRX）的 DL traffic prediction，包括预测在 UE 还是 NW 执行、是否及如何评估性能，以及 NW/UE power consumption model 等跨工作组影响。

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

RAN2 将研究 6G traffic prediction，CP 用例包括 carrier aggregation 的设置、释放、激活和去激活，RRC 状态或 battery saving mode 间的转换，以及用于负载均衡的 mobility decision；该类预测可基于 AI 或非 AI，并适用于 UL 和 DL。离线讨论还提出将非同址 L3 measurement prediction、L1/L3 beam prediction、conditional mobility 相关 measurement event prediction、RLF prediction/recovery 和 AI/ML based TA prediction 纳入用例表，其中部分事项待协调或仍需讨论。

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

RAN2 根据 5GA Rel19 AI for mobility study 的进展恢复 RLF prediction 研究。输入至少可包括 PCell 的 measured/predicted L1 SINR。

```text
RAN2 resumes the study on RLF prediction based on the progress in 5GA Rel19 AI for mobility study. The input can be at least measured/predicted L1 SINR of the PCell.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p018`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

RAN2 根据 5GA Rel19 AI for mobility study 的进展恢复 MOF prediction 研究，聚焦成功切换后不久发生 RLF 的 “too early handover” 和 “handover to wrong cell” 子场景。输入至少可包括候选目标小区的 measured/predicted L1 SINR。

```text
RAN2 resumes the study on MOF prediction based on the progress in 5GA Rel19 AI for mobility study, focusing on the “too early handover” and “handover to wrong cell” sub-scenarios wherein RLF occurs shortly after successful handover. The input can be at least measured/predicted L1 SINR of the candidate target cells.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p019`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

RAN2 研究 BFD prediction 用例，并考虑将相关小区的 measured/predicted L1 SINR 至少作为输入信息。

```text
RAN2 studies the use case of BFD prediction by considering at least the measured/predicted L1 SINR of the associated cells as input information.
R2-2600195	AIML use cases in 6G	CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p020`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

建议在 6G RRM mechanisms 定义前，复用 Rel-19 RRM measurement prediction 和 measurement event prediction 的评估结果开展 5G legacy use cases 研究。当前暂不纳入 RLF prediction study。

```text
It is recommended to perform the 6G AI/ML use case studies as below:
-	For 5G legacy use cases, reuse the evaluation results of Rel-19 RRM measurement prediction and measurement event prediction until the 6G RRM mechanisms are defined. RLF prediction study is excluded for now;
TA prediction
R2-2600085	Discussion on 6GR AIML use cases and framework	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p021`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

研究 6G 中基于 AI/ML 的 TA prediction。预测的 TA values 可用于降低所有 RRC states 对基于 RACH 的同步的依赖，例如 RACH-less handover、STAG TA establishment 和 CG-SDT。

```text
Study the AI/ML based TA prediction in 6G. The predicted TA values can be leveraged to minimize the reliance on RACH-based synchronization across all RRC states (e.g., RACH-less handover, STAG TA establishment, CG-SDT).
LCM framework (if time allows)
R2-2600663	Discussion on general AIML framework	Spreadtrum, UNISOC	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p022`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

6G AI/ML LCM framework 应支持 one-sided 和 two-sided model。

```text
6G AI/ML LCM framework should support both one-sided and two-sided model.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p023`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

6G AI/ML LCM framework 应支持 functionality-based LCM 和 model ID-based LCM。

```text
6G AI/ML LCM framework should support both functionality-based LCM and model ID-based LCM.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p024`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

对于 UE-sided model，6G AI/ML LCM framework 应支持 UE-based 和 NW-based management。

```text
6G AI/ML LCM framework should support both UE-based and NW-based management for UE-sided model.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p025`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

可考虑统一的跨 WGs AI/ML framework；如有必要，与 RAN3 和 SA 协调。

```text
A unified cross-WGs AI/ML framework can be considered. Coordinate with RAN3 and SA if necessary.
R2-2600418	Discussion on AIML use cases and AIML framework	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p026`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

Network 应能控制 UE 是否应用可能影响 network QoS requirements、user experience 或 overall system performance 的 AIML based functionality。

```text
Network should have a control on whether the UE applies any AIML based functionality which may impact network QoS requirements, user experience or overall system performance.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p027`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

所有 AIML use cases 中，网络需要能够评估 AIML functionality 的性能，并尽快停用表现不佳的 AIML functionalities。

```text
For all AIML use cases, the network needs to be able to evaluate AIML functionality performance and disable under-performing AIML functionalities as soon as possible.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p028`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

对于 NW-sided models，沿用 5G-A 的做法：除 network-side data collection（例如用于 training）外，不规定其他 LCM functions，由网络实现决定。

```text
For NW-sided models, reuse an approach from 5G-A that no LCM functions other than network-side data collection (e.g. for training) are specified (i.e. they are left to network implementation).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.2-p029`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.2 AI/ML use cases

RAN2 应研究 online training 对 AIML procedures（如 data collection 和 functionality management）的影响。

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

