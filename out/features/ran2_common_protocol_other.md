# 6GR 共用协议其他议题

**当前进展** · 阶段：讨论中

RAN2 正在研究 UE 在网络监督或有限网络控制范围内，依据环境、应用和无线条件动态调整 RRC 参数及协议行为，以改善性能，并探讨相关 KPI、场景和报告需求。与此同时，RAN2 已启动承载 mobility 相关数据的系统信息安全保护研究，目标是防范伪基站等攻击。对于系统信息安全机制及威胁范围，讨论倾向结合 SA3 的威胁分析后再考虑具体方案。相关研究仍需兼顾 PWS 可达性及系统信息开销等影响。

**未决问题**

- 哪些系统信息需要安全保护，以及应采用何种保护机制，待 SA3 讨论和威胁分析。
- 如何满足 TS 22.268 的 PWS 要求并避免因 UE 缺少安全密钥或经由其他运营商基站不可达而降低 PWS 可达性。
- 系统信息安全保护对 SIB 开销的影响，以及需要保护与无需保护的系统信息如何区分。
- UE 智能调整网络参数的适用场景、网络监督方式、性能指标及报告需求尚待研究。
- 网络控制下 UE 可调整参数或配置的范围，以及具体特性的收益和系统性能影响尚待后续分析。

## 跨会议演进脉络（6G）

材料仅包含 RAN2-132（2025-11-17 至 2025-11-21），不能判断跨会议变化。本次会议推进了“flexible” protocols 与 system information（SI）安全保护的研究方向，具体机制及技术方案仍待研究。

### 关键进展

- 研究在 Control Plane 和 User Plane 层级启用“flexible” protocols，允许 UE 利用内部算法，在网络监督及网络控制的有限范围内调整 RRC configured parameters 或配置，例如 RLC timer 和 LCH priority；该研究不依赖 AI/ML model management framework。（依据：RAN2-132）
- 启动承载 mobility-related data 的 SI 安全保护研究，以防御 false base stations 攻击；研究需考虑 TS 22.268 的 PWS messages 要求并保持 PWS reachability，具体安全保护方式由 SA3 讨论决定。（依据：RAN2-132）

### 待决问题

- UE 智能调整参数的具体机制、适用场景、收益及对 system performance 的影响尚待研究，后续可按具体 feature 提交提案。（依据：RAN2-132）
- 网络监测 UE 性能所需的 KPIs、其他 metrics，以及是否需要 reporting 和 reporting 级别尚未确定。（依据：RAN2-132）
- SI 安全威胁及新增潜在风险仍需确认，具体技术方案有待 SA3 threat analysis 的后续进展。（依据：RAN2-132）
- PWS 安全保护仍需解决跨运营商 base stations 的可达性问题，以及 UE 缺少对应 security key、无法解码所导致的可达性下降风险。（依据：RAN2-132）
- SI 安全机制引入的 SIB Overhead，以及哪些 SI 需要或不需要保护，仍需评估。（依据：RAN2-132）

### 会议时间线

_目前只有一场会议的 6G 综述，尚无法判断跨会议变化。_

- **RAN2#132**（2025-11-17 至 2025-11-21）：RAN2#132 围绕“flexible” protocols 和 system information（SI）安全保护推进了研究方向。前者研究在网络监督和有限控制范围内允许 UE 利用内部算法调整配置参数，并评估性能监测需求，不依赖 AI/ML model management framework；后者聚焦 mobility-related SI 的保护，同时要求考虑 PWS requirements 且不降低 PWS reachability。具体 SI 安全保护方式由 SA3 讨论决定，讨论支持等待 SA3 threat analysis 后再考虑技术方案。

## 6GR 演进

### [6G/Rel-20 RAN2#132] `observation` 10.3.3.3 Others

现有部署几乎总是对所有 UE 使用相同的一组参数值，很少根据 UE 的动态条件和能力进行区分；这可能导致 UE 和系统性能次优，并使用户体验在不确定的期间内较差。

```text
Existing deployments almost always use the same set of parameter values for all UEs with little differentiation for the dynamic conditions and capabilities of the UEs, which can result in sub-optimal performance for both the UE and the system and poor user experience for indefinite period of time.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.3-o001`

### [6G/Rel-20 RAN2#132] `observation` 10.3.3.3 Others

UE 可根据环境、应用和无线条件动态调整参数值，以改善用户体验。

```text
The UE can adapt the parameter values dynamically based on environmental, application, and radio conditions to improve the user experience.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.3-o002`

### [6G/Rel-20 RAN2#132] `observation` 10.3.3.3 Others

引入对 system information 的安全保护，以防止篡改和 false base station attacks。

```text
Introduction of security protection for system information prevents tampering and false base station attacks.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.3-o003`

### [6G/Rel-20 RAN2#132] `observation` 10.3.3.3 Others

对与邻区测量相关的 system information 进行安全保护，有助于使 IDLE mode mobility 保持在 NW 控制之下。

```text
Security protection of system information related to neighboring cell measurements is beneficial to keep IDLE mode mobilities under NW’s control.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.3-o004`

### [6G/Rel-20 RAN2#132] `observation` 10.3.3.3 Others

对指示 PWS 的 system information 进行安全保护仍有待解决的挑战，包括 TS 22.268 中的 PWS requirements，以及经由其他运营商 base stations 无法触达 PWS 的问题。

```text
Security protection of system information indicating PWS involves several challenges that need to be resolved: PWS requirements in TS 22.268 and unreachability of PWS via other operators’ base stations.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.3-o005`

### [6G/Rel-20 RAN2#132] `observation` 10.3.3.3 Others

若 UE 未获得用于传送 PWS 的 system information 对应的 security key，就无法解码该信息，可能导致 PWS reachability 降低。

```text
Regarding the system information used to deliver PWS, if the UE does not obtain the corresponding security key, it will be unable to decode the system information, which may lead to reduced reachability of PWS.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.3-o006`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.3 Others

RAN2 研究如何在 Control Plane 和 User Plane 层级启用“flexible” protocols，使 UE 可使用内部算法提升性能，同时不依赖 AI/ML model management framework。

```text
RAN2 study how to enable “flexible” protocols at Control and User Plane levels which allow the UE to use internal algorithms for better performance but do not rely on the AI/ML model management framework.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.3-p001`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.3 Others

RAN2 研究一种机制，使 UE 能在网络监督下调整 RRC configured parameters 的值。

```text
RAN2 study a mechanism which can allow the UE to adapt values of RRC configured parameters under network supervision.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.3-p002`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.3 Others

为在 UE 使用“smart”算法调整参数值时支持 NW 监测 UE 性能，RAN2 研究 KPIs 和其他 metrics。研究还包括适用场景，以及是否需要此类 reporting 及其级别。

```text
To enable NW monitoring of the UE performance when the UE uses “smart” algorithms to adapt parameter values, RAN2 study KPIs and other metrics along with the applicable use cases and necessity and level of such reporting.
Noted
R2-2508566	Discussion of User Plane Functionalities	Lenovo	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.3-p003`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.3 Others

RAN2 应研究使 UE 能在网络控制的有限范围内智能调整 NW 参数或配置（例如 RLC timer、LCH priority）的方案。讨论指出，后续阶段可针对具体 feature 提交提案，并分析其收益和对 system performance 的影响。

```text
RAN2 should study solutions which enable UE to adapt NW parameter/configurations, e.g. RLC timer or LCH priority, intelligently within some limited ranges which are under network control.
Noted
Discussion
-	Xiaomi is open to study this, but asks is the adaptation based on some criteria.   For proposal 3 question is whether we need to have separate performance monitoring mechanism.   Qualcomm would prefer to have it up to UE implementation but open to study some reporting.   It would be good have common mechanism.
-	Oppo understands the pains from UE side but the network needs to care about system performance, so what kind of KPIs can ensure both.   Qualcomm explains it depends on the case, for example PDCP discarding, can be number of PDU discarded and it is important for the network to have the big picture and have ability to de-activate.
-	 Turkcell thinks that network control is very important so we need to understand the details.
-	Docomo thinks that it is important for the network to have the information, control and select the parameters.
-	Lenovo thinks that there are different levels of control depending on the parameters.   We introduced in Rel-18/19 XR something similar, for example we configure two different LCP and based on some criteria the UE selects one of them.
-	Ericsson thinks it is important the NW knows the value the UE is using as it would introduce ambiguity.   We need to ensure that the behaviour is consistent amongst the UEs.  Nokia agrees with Ericsson.  Some examples are interesting but it is difficult to generalize from limited use cases and try everything.   ZTE agrees but thinks this is more AI/ML and key is how we evaluate the gain.
-	CATT thinks system performance is very important and is not sure how we can deal with the collision of UEs.
-	Interdigital thinks that are some specific functions to look at and agrees that it doesn’t work for everything.   For example discard value is common for the whole bearer but we have many services and we use one value.  This can be based on a range and it would not have impact to system performance.
-	Huawei agrees with other NW vendors and thinks we first need to understand if it is beneficial.  We can evaluate with other AI models and compare with NW side models.
-	CMCC thinks that the NW should be in control we can use UAI.   Qualcomm thinks that would be extremely inefficient the UE always requesting.
-	Mediatek is in favor of this as the UE has a lot of information and the design is so rigid so it forces the network to select a single value. The network can set the guardrails and it should hopefully alleviate the concern.
-	Vivo thinks that it is a good direction.
-	Apple thinks NWs should relax and see where it can be used. It is not new.
-	ZTE thinks that we need to have an understanding on how the UEs are implementing this, unless we get ue vendor ID and sw ID.
-	BT, DT, TIM, Verizon, Tmob, Vodafone, thinks that we wouldn’t understand where the problem is coming from and this is not necessary.
-	LG thinks that there are three cases in 5G where we allow selection of a parameter for a sub-set of values.
Companies can bring proposals in later phase of the study for a specific feature and analyze the benefits, system performance impact etc.
System information security
R2-2508421	On system information security	NTT DOCOMO INC.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.3-p004`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.3 Others

RAN2 启动研究，为承载 mobility-related data 的 system information 引入安全保护，以防御 false base stations 发起的攻击。

```text
RAN2 starts a study to introduce security protection for system information that conveys mobility-related data, to defend against attacks from false base stations.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.3-p005`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.3 Others

系统信息应引入何种安全保护由 SA3 讨论并决定。

```text
It is up to SA3 to discuss and decide what kind of security protection is introduced for system information.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.3-p006`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.3 Others

RAN2 研究系统信息安全保护，并考虑 TS 22.268 中对 PWS messages 的要求，同时不降低 PWS 的可达性。

```text
RAN2 studies security protection of system information considering requirements for PWS messages in TS 22.268 and without reducing reachability of PWS.
[3min]
Noted
R2-2508950	Security Requirements in 6GR	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.3-p007`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.3 Others

除 SA3 检出的 DoS 和 Rogue service attacks 外，RAN2 认为潜在威胁还可能包括涉及 ETWS 和 CMAS 的公共安全威胁，以及针对 MBMS、NTN 和其他服务相关 SIBs 的攻击。

```text
In addition to DoS and Rogue service attacks detected by SA3, potential threats from RAN2 prespective may include:
1) Public safety threats involving ETWS and CMAS;
2) Service attacks targeting MBMS, NTN, and other service-related SIBs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.3-p008`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.3 Others

SI 安全机制可能带来的 RAN2 影响包括 SIB Overhead，以及区分哪些 SI 需要或不需要保护。

```text
Possible RAN2 effects posed by the SI security mechanism:
1) SIB Overhead;
2) SI that is protected and does not need to be protected.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.3-p009`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.3 Others

关于 6G system information security，RAN2 提出应确认系统信息是否确实面临安全威胁及是否存在新的潜在风险，并可等待 SA3 的 threat analysis 后再考虑具体技术方案。RAN2 可向 SA3 提供包括 P1、P2 在内的意见；讨论意见支持等待 SA3 后续进展。

```text
A key question to SA3 regarding system information security is whether the system information in 6G network is genuinely faces security threats or what are new potential risks. RAN2 can wait the output of SA3's threat analysis before considering specific technical solutions. However, RAN2 can provide inputs including P1 and P2 about RAN2’s key question, extra consideration of threats and conserns to SA3.
[2min]
Noted
Discussion
-	Qualcomm thinks SA3 is discussing this. Oppo thinks that they are studying it but they are not aware of the RAN concerns.
-	Lenovo, Huawei and Xiaomi thinks that we have discussed this a lot in 5G area and we should wait for SA3.
Wait for further SA3 progress
R2-2508055	Further Discussion on 6G security	vivo	discussion	Rel-20
R2-2508100	Considerations on 6G AS security	CATT	discussion	Rel-20	FS_6G_Radio
R2-2508108	Discussion on the RAN2-related 6G security aspects	OPPO	discussion	Rel-20	FS_6G_Radio
R2-2508144	Discussion on AS security in 6G	Transsion Holdings	discussion
R2-2508294	Additional Security Aspects for 6G	NEC	discussion	Rel-20	FS_6G_Radio
R2-2508347	Security assumptions for system information	MediaTek Inc.	discussion	Rel-20	Revised
R2-2508424	Discussion for AS security in 6GR	Sharp	discussion	Rel-20	FS_6G_Radio	Withdrawn
R2-2508525	Other common user and control plane issues	Ericsson	discussion	Rel-20	FS_6G_Radio
R2-2508572	Considerations for Security and SON/MDT in 6GR 	Samsung	discussion
R2-2508620	Discussion on system information protection	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio	Withdrawn
R2-2508635	Security for system information	Ofinno	discussion	Rel-20
R2-2508681	AS security for 6GR	InterDigital, Inc.	discussion	Rel-20
R2-2508697	Further improvements to AS security in 6G	Nokia	discussion	FS_6G_Radio
R2-2508948	Discussion on Access Stratum Security	Fujitsu	discussion	Rel-20
R2-2508987	Discussion on AS Security for 6G	China Telecom	discussion	Rel-20	FS_6G_Radio
R2-2509003	Views on AS security aspects	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
R2-2509047	Security assumptions for system information	MediaTek Inc.	discussion	Rel-20	R2-2508347
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.3-p010`

