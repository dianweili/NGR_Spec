# 6GR 寻呼

**当前进展** · 阶段：—

_尚无综述_

## 6GR 演进

### [6G/Rel-20 RAN2#134] `agreement` 9.3.2.4 Paging

```text
1	UE monitors a single paging occasion per UE paging cycle
2	For 6G PF/PO design, aim to use one single PF/PO distribution formula to support both clustered PF/PO and uniform PF/PO for all paging cycles.
3	For next meeting, capture requirements for paging formula and shortcoming/limitations we want to address for 6G.  The detailed formula design is left to WI phase.
Other Paging Requirements (Clustered PF/PO)
R2-2603015	Paging in 6G	Samsung	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.4-a001`

### [6G/Rel-20 RAN2#134] `agreement` 9.3.2.4 Paging

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

```text
The paging occasions within a paging cluster must be more densely packed, resulting in a paging cluster containing a greater number of POs compared to NR Rel-19.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.4-o001`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.4 Paging

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

```text
RAN2 aim to ensure the signaling overhead of PO configurations should not be increased significantly with the increased POs within one PF.
-	Nokia and Apple thinks it should be considered but it quite stage 3.
Noted
R2-2603562	Paging considerations for 6G	Lenovo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.4-p002`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.4 Paging

```text
RAN2 to support the configuration of one or multiple paging clusters within a single DRX cycle, each containing 1 or more Paging Possibility.
Noted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.4-p003`

### [6G/Rel-20 RAN2#133bis] `agreement` 9.3.2.4 Paging

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

```text
Restriction#1 of Rel-19 paging adaptation: it can’t support paging cycle>32 radio frames (i.e. 64/128/256 radio frames) because value range of N is only extended to 1/32 due to the following concerns:
1)	The actual paging cycle may be restricted by UE dedicated paging cycle configured by NAS.
2)	N<1/32 requires to introduce larger Ns>8 to compensate the decrease of PF number. However, larger Ns value will lead to significant increase of SIB1 size as the PMO offset linearly increases according to Ns.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.4-o001`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.2.4 Paging

```text
In NR, PDCCH and PDSCH for paging are transmitted ‘N*X’ times, where N is the number of transmitted SSBs in the cell and X is the number of repetitions per SSB. This leads to significant overhead and increased network energy consumption.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.4-o002`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.4 Paging

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

```text
For UE context transfer, RAN2 support both of the following solutions:
-Xn solution：In the scenarios with an Xn interface between a new serving RAN node and the last serving RAN node, the new serving RAN node can fetch UE context from the last serving RAN node;
-NG solution：In the scenarios without an Xn interface between a new serving RAN node and the last serving RAN node, UE context is forwarded by the core network through the NG interface. And RAN2 send LS to ask SA2 about feasibility.
Noted
R2-2601508	Single paging design in 6GR	Xiaomi	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.4-p002`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.4 Paging

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

```text
Ask SA2 and RAN3 to work on the following aspects to support single paging mechanism in 6G:
Define single paging area for UE in idle and inactive state
Define UE context fetch with or without Xn interface within this paging area
Define UE ID to identify the UE context storage within this paging area
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.4-p004`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.4 Paging

```text
For MT traffic, RAN2 prefer to have DL data and signaling buffered in CN and trigger paging for inactive state and would like to ask SA2 and RAN3 to work on the procedures to support this.
Noted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.4-p005`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.4 Paging

```text
RAN2 to clarify the understanding of the single paging area for both idle and inactive state:
A TA like list in 6G used for idle state is also applied to inactive state for single CN triggered paging mechanism.
R2-2601693	Discussion on paging	NEC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.4-p006`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.4 Paging

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

```text
Lesson Learned from 5G: The dual-paging mechanism in 5G creates unnecessary complexity and relies on Xn connectivity that is not always available, hindering the deployment of RRC_INACTIVE.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-o001`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.4 Paging

```text
To meet 6G latency requirements for fast state transitions, it is preferable to store the UE context in the RAN for rapid retrieval.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-o002`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.4 Paging

```text
Mechanisms are needed to allow the transfer of RAN context between gNBs via the Core Network (or other indirect paths) when direct Xn connectivity is unavailable.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-o003`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.4 Paging

```text
Current specs support NG-RAN node to notify the AMF of the UE RRC state when the UE enters or leaves RRC_INACTIVE state.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-o004`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.4 Paging

```text
In current specs, UPF can trigger CN paging procedures upon receiving downlink data for UE in CM-IDLE state.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-o005`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.4 Paging

```text
There are two Options to realize the single paging mechanisms for RRC_INACTIVE UE:
-Option 1：Upon a UE entering the RRC_INACTIVE, RAN node informs the core network the RRC state change.
-Option 2: Upon DL data from UPF or DL signaling from AMF arrival, RAN node indicates the core network to trigger CN paging for RRC_INACTIVE UE.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-o006`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.4 Paging

```text
In NR paging design, UE can distinguish IDLE paging and INACTIVE paging based on the different paging UE-IDs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-o007`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.4 Paging

```text
6G paging study from UE complexity reduction perspective should consider including more paging cause than 5G in the paging message.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-o008`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.4 Paging

```text
5G paging adaptation solution has limited NES gain due to backward compatibility and it can’t flexibly enable PF bundling.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-o009`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.4 Paging

```text
6G paging study from the network energy efficiency perspective should consider the non-uniform PO distribution direction in flexible way as day-1 design.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-o010`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.4 Paging

```text
In NR, for paging DRX cycles of up to 32 radio frames, it is possible to configure all PFs/POs at the beginning of paging DRX cycle. For longer paging DRX cycles of T > 32 such as 64, 128, 256 radio frames, all PFs/POs cannot be configured at the beginning of DRX cycle T.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-o011`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.4 Paging

```text
NR design is rigid as it always prioritizes paging delay and does not give network a choice to decide between paging delay and network energy savings.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-o012`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.4 Paging

```text
The network can achieve energy savings by controlling the timing of the paging occasions of UEs relative to the expected paging frequency.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-o013`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.4 Paging

```text
RAN2 preference is for CN-triggered paging as the unified paging mechanism for both IDLE state and INACTIVE state (or equivalent substate) UEs in 6G.
-	Lenovo asks if this has the problem that the CN has to page across a large area even in connected.  Interdigital thinks that we should study how to page in a small area
-	Samsung asks if this is for inactive only.
-	Vivo asks if this applied for the connected sub-state.    Huawei thinks this should be only for inactive.
-	Mediatek asks if we are going to ask CN to page the UE in connected.  Interdigital thinks that even for inactive the UE is in CN connected and we’d have to ask them if they can do it.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-p001`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.4 Paging

```text
RAN2 to send an LS to SA2 indicating the preference for CN-initiated paging for UEs in the 6G Inactive state (or equivalent substate)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-p002`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.4 Paging

```text
RAN2 should assume context retrieval mechanisms that prioritize fast retrieval from the RAN when Xn is available, while assuming context transfer via the CN/RAN3 mechanisms when Xn is unavailable.
-	Lenovo thinks we can minimize the looping with CN direct involved.  Interdigital thinks that we need to ask SA2 what is possible.
-	Xiaomi asks whether we would end up supporting more than one RAN context transfer.  Interdigital thinks that the CN context fetching is like a fallback.
-	Frauohaufer explains that some analysis show that 95% of the time the UE is in the same cell, so do we need to care about the other cases.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-p003`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.4 Paging

```text
RAN2 to coordinate with RAN3 and SA2 to determine the feasibility of transferring RAN context via CN nodes (NG interface) to support mobility in sparse Xn deployments
Noted
R2-2600957	Discussion on Paging open issues for 6GR	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-p004`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.4 Paging

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

```text
In the single paging design for both IDLE paging and INACTIVE paging, UE needs to be able to distinguish between the two types of paging through the paging record, either through different paging UE-IDs or the new state indication.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-p006`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.4 Paging

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

```text
6G paging should support the non-uniform PO distribution design from day-1.
Noted
R2-2600058	Paging in 6G	Samsung	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-p008`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.4 Paging

```text
Paging design in 6G should give network choice to decide between paging delay and network energy savings.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-p009`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.4 Paging

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

```text
6G should enable both legacy approach (non-clustered paging allocation) and clustered paging allocation to allocate paging frame to support different scenarios in 6G.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-p011`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.4 Paging

```text
It should be possible to configure paging periodicities to be multiples of SSB periodicities in order to align with SSB transmissions and also offsets to calculations should be allowed to not require paging occasions being exactly in the same slots as SSBs
R2-2600714	Paging in 6G	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-p012`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.4 Paging

```text
Support Cell DTX for paging, with PF and PO located in Cell DTX on duration.
Paging occasions Configuration for Network Energy
R2-2600440	Paging for 6GR	InterDigital France R&D, SAS	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.4-p013`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.4 Paging

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

