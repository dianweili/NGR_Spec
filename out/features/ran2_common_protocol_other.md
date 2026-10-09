# 6GR 共用协议其他议题

**当前进展** · 阶段：—

_尚无综述_

## 6GR 演进

### [6G/Rel-20 RAN2#132] `observation` 10.3.3.3 Others

```text
Existing deployments almost always use the same set of parameter values for all UEs with little differentiation for the dynamic conditions and capabilities of the UEs, which can result in sub-optimal performance for both the UE and the system and poor user experience for indefinite period of time.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.3-o001`

### [6G/Rel-20 RAN2#132] `observation` 10.3.3.3 Others

```text
The UE can adapt the parameter values dynamically based on environmental, application, and radio conditions to improve the user experience.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.3-o002`

### [6G/Rel-20 RAN2#132] `observation` 10.3.3.3 Others

```text
Introduction of security protection for system information prevents tampering and false base station attacks.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.3-o003`

### [6G/Rel-20 RAN2#132] `observation` 10.3.3.3 Others

```text
Security protection of system information related to neighboring cell measurements is beneficial to keep IDLE mode mobilities under NW’s control.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.3-o004`

### [6G/Rel-20 RAN2#132] `observation` 10.3.3.3 Others

```text
Security protection of system information indicating PWS involves several challenges that need to be resolved: PWS requirements in TS 22.268 and unreachability of PWS via other operators’ base stations.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.3-o005`

### [6G/Rel-20 RAN2#132] `observation` 10.3.3.3 Others

```text
Regarding the system information used to deliver PWS, if the UE does not obtain the corresponding security key, it will be unable to decode the system information, which may lead to reduced reachability of PWS.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.3-o006`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.3 Others

```text
RAN2 study how to enable “flexible” protocols at Control and User Plane levels which allow the UE to use internal algorithms for better performance but do not rely on the AI/ML model management framework.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.3-p001`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.3 Others

```text
RAN2 study a mechanism which can allow the UE to adapt values of RRC configured parameters under network supervision.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.3-p002`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.3 Others

```text
To enable NW monitoring of the UE performance when the UE uses “smart” algorithms to adapt parameter values, RAN2 study KPIs and other metrics along with the applicable use cases and necessity and level of such reporting.
Noted
R2-2508566	Discussion of User Plane Functionalities	Lenovo	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.3-p003`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.3 Others

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

```text
RAN2 starts a study to introduce security protection for system information that conveys mobility-related data, to defend against attacks from false base stations.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.3-p005`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.3 Others

```text
It is up to SA3 to discuss and decide what kind of security protection is introduced for system information.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.3-p006`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.3 Others

```text
RAN2 studies security protection of system information considering requirements for PWS messages in TS 22.268 and without reducing reachability of PWS.
[3min]
Noted
R2-2508950	Security Requirements in 6GR	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.3-p007`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.3 Others

```text
In addition to DoS and Rogue service attacks detected by SA3, potential threats from RAN2 prespective may include:
1) Public safety threats involving ETWS and CMAS;
2) Service attacks targeting MBMS, NTN, and other service-related SIBs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.3-p008`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.3 Others

```text
Possible RAN2 effects posed by the SI security mechanism:
1) SIB Overhead;
2) SI that is protected and does not need to be protected.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.3-p009`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.3 Others

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

