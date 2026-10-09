# 6GR RRC

**当前进展** · 阶段：—

_尚无综述_

## 6GR 演进

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.1 RRC Modelling and connection management

```text
The “inactive” state is fundamentally distinct from RRC idle state in the following aspects:
-	AS context storage
-	UE identification for RRC resume/setup in the applicable area
-	AS security requirement
-	data transfer requirement
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-o001`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.1 RRC Modelling and connection management

```text
Different procedures shall be performed for transition to RRC connected state from “inactive” state and RRC idle state. In addition, different procedures shall be performed for transition to “inactive” state and RRC idle state from RRC connected state.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-o002`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.1 RRC Modelling and connection management

```text
IoT cases with infrequent traffic and high delay tolerance are a clear match for inactive operation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-o003`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.1 RRC Modelling and connection management

```text
Some cases of agentic AI background traffic may lend themselves to inactive operation, but the future traffic patterns for such activity are not yet clear.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-o004`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.1 RRC Modelling and connection management

```text
Generative AI traffic facing a human user is unlikely to be a match for inactive operation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-o005`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.1 RRC Modelling and connection management

```text
Smartphone/eMBB/FWA foreground traffic is poorly suited for inactive operation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-o006`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.1 RRC Modelling and connection management

```text
Smartphone/eMBB/FWA background traffic could in some instances be suitable for inactive operation, but in many cases the traffic density and latency sensitivity may be expected to be incompatible with inactive.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-o007`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.1 RRC Modelling and connection management

```text
Wearables, trackers, and similar devices may see gains from inactive operation, often requiring short DRX but potentially having small data exchanges when active.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-o008`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.1 RRC Modelling and connection management

```text
The energy-consumption difference between SDT and state transition is concentrated in RRC signalling and link adaptation (both of which are present for state transition and absent for SDT).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-o009`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.1 RRC Modelling and connection management

```text
For "Inactive" state, the fast state transition to fulfill the CP latency requirement can be enabled via resume-like procedure based on the stored UE AS context at both UE and network.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-o010`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.1 RRC Modelling and connection management

```text
The restrictions of the SDT mechanism in NR include:
-	SDT can be utilized only if less than or equal to an amount of UL data awaits transmission, and the DL RSRP is above a configured threshold;
-	NW blindly scheduling of the subsequent DL/UL transmission with low transmission efficiency or low transmission reliability;
-	For RA-SDT, dedicated RACH resources are needed;
-	For CG-SDT, dedicated CG resources are needed, which can only be reserved by the last serving cell, and the TA should be valid (RSRP change should be within a configured threshold, and the TAT for SDT is running);
-	Data transmission continuity is not supported during cell reselection while SDT is ongoing.
Proposal 1a:	As a baseline, the fast transition to data transmission can be achieved through fast state transition from "Inactive" state to RRC connected via resume-like procedure.
Proposal 1b:	RAN2 to study the necessity of supporting data transmission in the "Inactive" state considering the following aspects of insensitive/ bursty traffic:
-	The typical data size of the bursty traffic;
-	Whether the bursty traffic is periodical or random arrival;
-	Whether the device with insensitive/ bursty traffic is stationary or mobile.
UE-based mobility
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-o011`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.1 RRC Modelling and connection management

```text
As the network has no idea of when and where the UE will resume the connection within the paging area, providing pre-configurations of candidate cells to UE in "Inactive" state would be highly challenging and would highly reduce the resource efficiency.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-o012`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.1 RRC Modelling and connection management

```text
In the LTE, on top of the baseline RRC_IDLE state, the sub-state of ‘IDLE with suspend’ has the following characteristics:
-	The CN-RAN connection for the UE is suspended, which can enable fast resume when needed.
-	UE AS context is stored at the network and the UE.
-	Unicast data/signaling can be transferred via EDT/PUR.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-o013`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.1 RRC Modelling and connection management

```text
In 6G, with a single CN-triggered paging mechanism and a single paging area, the difference between the Idle state and "Inactive" state may include:
-	Whether the CN-RAN connection for the UE remains as established or suspended (To be discussed by RAN3/SA2);
-	Whether UE AS context is stored at the network and the UE;
-	Whether unicast data/signaling can be transferred without state transition via SDT (If SDT is introduced).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-o014`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.1 RRC Modelling and connection management

```text
The RRC connection release is a strictly network-led procedure where the final decision for state transition has resided solely with the network.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-o015`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.1 RRC Modelling and connection management

```text
Although the DataInactivityTimer enables an autonomous transition to RRC_IDLE state, the subsequent NAS recovery triggers a return to RRC_CONNECTED state.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-o016`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.1 RRC Modelling and connection management

```text
Existing UAI mechanism in NR fails to guarantee timely state transitions in practice, as the network maintains full control over whether to allow reporting and determines whether to respond (for power saving) or when to respond (for MUSIM).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-o017`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.1 RRC Modelling and connection management

```text
The reliance on proprietary workarounds (e.g., local RRC connection release) highlights an opportunity for 6G to resolve current limitations by introducing a standardized UE-initiated RRC connection release procedure.
Based on the discussion in the previous section we propose the following:
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-o018`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.1 RRC Modelling and connection management

```text
RAN2 to clarify that paging is the signaling used to reach the UE for incoming DL data/signaling when the UE is in “inactive” state.
-	Nokia asks if paging refers to paging concept or RRC signaling.   Samsung thinks that the paging RRC message can be the same for idle or inactive.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-p001`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.1 RRC Modelling and connection management

```text
UE-based mobility in the “inactive” state should be the same as that in idle state, i.e. based on cell (re) selection framework (e.g., best cell principle, cell ranking, inter-freq/RAT prioritization, etc.), and can follow the progress of cell (re)selection made in mobility topic.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-p002`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.1 RRC Modelling and connection management

```text
RRC signaling shall be used as the only mechanism to initiate the state transition from “inactive” state to RRC connected state.
-	Fraunhaufer thinks that we should study other mechanisms like random access
Modeling of” inactive” state
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-p003`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.1 RRC Modelling and connection management

```text
Define separate RRC inactive state for 6G.
UE-based mobility in the “inactive” state should be the same as that in idle state, i.e. based on cell (re) selection framework (e.g., best cell principle, cell ranking, inter-freq/RAT prioritization, etc.), and can follow the progress of cell (re)selection made in mobility topic.
SDT support
R2-2603032	Functionality for inactive in 6G	ZTE Corporation, Sanechips, Nokia, LG Electronics, Sony, TIM, China Telecom, CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-p004`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.1 RRC Modelling and connection management

```text
Support small data transmission for both MT and MO cases in inactive state.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-p005`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.1 RRC Modelling and connection management

```text
For small data transmission in inactive state, Network is not required to reserve dedicated radio resource for the UE in the neighbour cells. Dedicated signalling for resource configuration is not required before the small data transmission for both MT and MO cases.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-p006`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.1 RRC Modelling and connection management

```text
Study the following aspects for small data transmission in inactive state:
-	Flexible time duration and burst size
-	Energy efficiency
-	UE controlled mobility during small data transmission
Noted
R2-2603258	Is SDT Useful? (and other aspects of inactive operation)	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-p007`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.1 RRC Modelling and connection management

```text
Consider inactive operation as primarily applicable to IoT traffic, with the possibility of applying it to wearables, trackers, and potentially some AI traffic patterns (depending on the future evolution of AI services).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-p008`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.1 RRC Modelling and connection management

```text
Specifying SDT is conditioned on showing energy-saving benefits as compared to transition to RRC_CONNECTED, for the case of infrequent small traffic bursts.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-p009`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.1 RRC Modelling and connection management

```text
Further study possible SDT procedures along with the energy costs of RRC signalling for state transitions, with the goal of determining if the costs justify the complexity of specifying SDT.
-	ZTE thinks that signaling overhead is also a strong consideration.  There can be frequent small data transmission so that  would be a valid use case (e.g. like sensor).
Energy cost and signaling overhead
Discussion
-	Huawei thinks that for IoT there is a use case but not for smart phones.   Xiaomi also has the same understand for smart phones, the UE can go in connected mode and be configured with long DRX.    If we are going to compare we should compare with UE going to connected with long DRX.
-	Oppo also doesn’t observe small data for MBB traffic.   So we should understand what is the use case.    ZTE explains that at least for IoT devices this is needed, and we are targeting a common solution so we should at least study.    Vivo agrees but we should also understand whether we are considering stationary IoT scenarios.
-	CMCC would like to to study but hopes that it is not only for IoT but should be common to various devices.     For some devices there heartbeat can be 1min, so we should understand periodicity and data size.
-	Qualcomm and Nokia agrees that this should be supported with IoT being the driving use cases but should aim for a common solution.
-	CATT also supports
-	Ericsson thinks we should avoid msg1 partitioning.
-	Apple would like to remind everyone that we need to take the max TB size into account to make useful for IP packets.
-	LG point out that we already studied SDT and concluded it was beneficial.    ZTE agrees and inactive without SDT is not very useful.    Also when you move to connected the network will release you when it wants.
-	Tmobile explains that SDT and inactive has been deployed in their network and there are latency benefits.
Agreements for inactive state
1	Paging message is used to reach the UE for incoming DL data/signaling when the UE is in “inactive” state.  Same paging model as in idle is assumed.  How the paging signaling looks like is FFS (depending on RAN2/SA2/RAN1, etc discussions).
2	UE-based mobility in the “inactive” state should be the same as that in idle state, i.e. based on cell (re) selection framework (e.g., best cell principle, cell ranking, inter-freq/RAT prioritization, etc.), and can follow the progress of cell (re)selection made in mobility topic.
3	RRC based mechanism is used as baseline to perform the state transition from “inactive” state to RRC connected state from the UE.
4	Identify limitations/drawbacks/possible modification of 5G SDT, and understand the need for different use cases and traffic characteristics, the maximum TBS size.  Use 5G SDT analysis as a starting point and continue to understand the benefits/gains/limitation for such cases in terms of at least energy efficiency and signaling overhead, including mobility and coverage considerations.
[POST134][20][6G CP] SDT (ZTE)
Intended outcome:
To identify the use cases and expected traffic pattern size and frequency
Understand the candidate solutions and clarify the space of what we are discussing next meeting
Discuss need
Deadline: long
Fast transition
R2-2602963	Discussion on RRC Modelling and Connection Management for 6G	LG Electronics Inc.	discussion
Observation 1 	Due to the payload size limitation of Msg3, it would be unfeasible for a single resume identity to accommodate the routing information for both the last serving aNB and the last AMF.
Observation 2	If the use of CG SDT resources can be extended to the purpose of RRC connection establishment, transmitting RRC resume request message regardless of SDT, it would enable a fast RRC state transition (i.e., RACH-less resume).
Observation 3	If the UE has valid TA and configured grant (CG) for a candidate cell, and their use is allowed in RRC_INACTIVE; the UE can perform RACH-less resume upon cell reselection to that candidate cell.
Observation 4	Early TA for candidate cells can be complemented by enabling UEs to acquire early TA through on demand SIB1 acquisition, allowing valid UL timing to be obtained without additional signalling overhead and improving the reliability and coverage of RACH less resume procedures.
Proposal 2	Study RRC resume using different resume identities depending on the UE context fetch method (i.e., with/without Xa) to solve the Msg3 size limitation issue.
Proposal 3	Study RACH-less resume for fast state transition with following approaches:
•	Consider CG based SDT as a baseline for RACH-less resume for UEs camp on the Anchor cell (=last PCell).
	TA maintenance via CG-SDT procedure in serving cell.
•	Reuse early TA and CG configured for cell switch (e.g., candidate cell for CLTM) as a baseline for RACH-less resume after cell re-selection to non-anchor cell.
	Early TA acquisition through on demand SIB1/SI acquisition.
Proposal 7	Study low latency and highly reliable connection setup procedures, together with fast data transmission/reception and immediate connection release or suspension, as a means to enhance network and UE energy saving efficiency in 6GR.
Noted
R2-2602951	Discussion on functionalities and modeling of the Inactive state	vivo, Huawei, HiSilicon, NTT DOCOMO	discussion	Rel-20
Fast transition to data transmission
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-p010`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.1 RRC Modelling and connection management

```text
For "Inactive" state, the UE-based mobility can be supported without the need for pre-configuration of candidate cells.
Consideration of the modeling
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-p011`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.1 RRC Modelling and connection management

```text
With the single CN-triggered paging in 6G, modelling "Inactive" state as a sub-state of IDLE state, i.e., ‘IDLE with suspend’, can be considered as a candidate.
Noted
UE triggered release – if time allows ([CB Friday]
R2-2603941	Discussion on UE-initiated RRC connection release procedure	Samsung, MediaTek Inc., Xiaomi, Apple, vivo	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-p012`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.1 RRC Modelling and connection management

```text
Study a standardized UE-initiated RRC connection release procedure for 6G.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-p013`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.1 RRC Modelling and connection management

```text
For the design of the UE-initiated RRC connection release, the following aspects should be further investigated:
•	Whether the initiation of the procedure is subject to explicit network configuration(s)
•	Feasibility of autonomous state transition upon successful message delivery or timer/timeline-based transition in the absence of network response
•	Identification of relevant use cases
-	Ericsson thinks that this should be under network control and we use the UAI.  Samsung thinks that it should definitely be discussed, there are two ways network can enable the procedure, but in some cases like MUSIM it would be better without network configuration.
-	CATT shares the same concerns in bad channel conditions it can release autonomously and there may be a misalignment between UE and network.
-	Nokia is fine to study but would like everyone to review the fast dormancy work in the past, we should understand the benefit and it should absolutely be in network control.
-	CMCC also shares the same concerns.
-	Huawei thinks it is fine to study but focus on the network control we should look at issues and functionalities, not details.
-	ZTE thinks that we are also discussing early reporting and this are overlapping.  Samsung explains that we should look at the relevant use cases, as it is more related to the UE needing to leave as soon as possible, but early reporting is more about no more date coming.
-	Qualcomm thinks that this is the pain point and MUSIM is a problem and the network control is the issue, UAI is not configured.   Oppo agrees that it happens already in the field.
-	ZTE thinks that the pain point is really occurring because we don’t have inactive state so in 6G if inactive state is usuable then the network will release the UE in inactive.
-	Huawei thinks that this is also related the UE Capability update.   Samsung explains that there is a difference as the in UE capability update the UE wants to stay in connected and updates capabilities in this case it wants to leave.
Study UE-initiated/request RRC connection release.  Understand the pain point and use cases that require such behavior.  Focus on functionality and possible impacts to UE and NW.
Not treated
R2-2602972	RRC modelling and connection management in 6GR	Xiaomi	discussion	Rel-20	FS_6G_Radio
R2-2603091	Discussion on RRC Modelling and connection management in 6G	Transsion Holdings	discussion	Rel-20
R2-2603243	Inactive state for 6G	Ericsson	discussion	Rel-20
R2-2603298	RRC Modelling and connection management	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2603386	Pain points of NR RRC connection re-establishment and how to resolve them in 6GR	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
R2-2603451	Enhancing RRC inactive	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
R2-2603552	Discussion on RRC modelling and connection management	Lenovo	discussion	Rel-20
R2-2603622	Some considerations on Inactive state	Sony	discussion	Rel-20	FS_6G_Radio
R2-2603658	Further discussion on INACTIVE	NEC	discussion	Rel-20	FS_6G_Radio
RRC State Model for 6GR	InterDigital, Inc.	discussion	Rel-20	FS_6G_Radio
R2-2603698	RRC state functionalities	Panasonic	discussion	Rel-20
R2-2603708	Discussion on 6G RRC state(s) and functionalities	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
R2-2603729	Views on 6G inactive state	Apple	discussion	Rel-20	FS_6G_Radio
R2-2603756	6G RRC state modelling issues	AT&T	discussion	FS_6G_Radio
R2-2603780	RRC Modelling for bursty traffic 	Kyocera	discussion
R2-2603830	Inactive state and additional functionalities for consideration for 6G	Nokia	discussion	Rel-20	FS_6G_Radio
R2-2603845	Discussion on 6G RRC connection management	KT Corp.	discussion
R2-2603852	RRC functionality and connection management in 6GR	Sharp	discussion
R2-2603859	Discussion on 6G RRC INACTIVE	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2603894	Discussion on RRC functionality and connection management	Spreadtrum, UNISOC	discussion	Rel-20
R2-2603962	Support for delay-sensitive and bursty traffic in RRC_CONNECTED	TCL	discussion	Rel-20
R2-2603985	Discussion on RRC state for 6GR	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2604023	Discussion on RRC Inactive in 6GR	Rakuten Symphony	discussion	Rel-20
R2-2604053	Discussion on 6G RRC states	Qualcomm Incorporated	discussion
R2-2604062	RRC modelling and connection management	1Finity	discussion	Rel-20
R2-2604140	RRC_INACTIVE State Naming	Turkcell, China Unicom, Sony	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.1-p014`

### [6G/Rel-20 RAN2#134] `agreement` 9.3.2.2 RRC Structure and (re)configuration

```text
1	RAN2 will not pursue a specification based solution for UE applying partial (re)configuration in case of failure in 6G.
2	RAN2 studies a simplified procedure for (re)configuration failure handling, with some operations skipped (e.g., cell search, security key derivation, etc.) to reduce UE service interruption, compared with NR re-establishment. FFS specific operations to be skipped.
3	RAN2 further discusses whether the simplified procedure is based on "RRC Re-establishment" procedure or other RRC procedures (e.g. configuration fallback).
For next meeting, companies can address the follow points
1) for simplified procedure what specific operations would be skipped, and what are the UE impacts/interruptions
2) Fallback, how is the UL access performed and configuration the UE applies, impacts to the NW
3) what is the network response and whether the network can fallback to RRC setup procedure
Only two co-sourced papers are expected next meetings and no individual contributions are allowed.
UE Interruption Avoidance
R2-2602973	(Re)configuration failure handling without service interruption in 6GR	Xiaomi, Qualcomm Incorporated, Apple, Samsung, InterDigital, Ofinno, Kyocera, Sharp	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.2-a001`

### [6G/Rel-20 RAN2#134] `agreement` 9.3.2.2 RRC Structure and (re)configuration

```text
Study the use of stored configurations.  Understand how the UE processes the configuration, how it gets the configurations and what are the gains for different use cases.   Study at least the use of stored configurations during 1) Transition from INACTIVE to CONNECTED; 2) Reconfiguration while the UE is in CONNECTED.
Study at least cases while the UE remains in the same cell.
The use of the stored configuration for a UE in IDLE is not considered for the moment.
Split RRC (to be discussed after June checkpoint on CU-DU split)
R2-2604144	Discussion on Radio Protocol Architecture – Control Plane	Rakuten Inc, Apple, 1-Finity (former Fujitsu), Xiaomi, Sony, Ofinno, Jio Platforms Limited	discussion	Rel-20
R2-2602952	Discussion on 6GR RRC Reconfiguration Failure	vivo	discussion	Rel-20
R2-2603092	Discussion on RRC structure and (re)configuration in 6G	Transsion Holdings	discussion	Rel-20
R2-2603299	RRC structure and partial configuration failure	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2603339	Discussion on RRC (re)configuration structure	LG Electronics France	discussion	Rel-20	FS_6G_Radio
R2-2603374	Discussion on Reconfiguration failure	Lenovo, LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
R2-2603520	Solutions for UE reporting what caused reconfiguration failure	Ericsson, AT&T	discussion	Rel-20	FS_6G_Radio
R2-2603607	Discussion on RRC Reconfiguration Failure	Fainity Innovation	discussion	Late
R2-2603665	RRC Reconfiguration for 6G	InterDigital, Inc.	discussion	Rel-20	FS_6G_Radio
R2-2603730	Views on 6G RRC structure and (re)configuration	Apple	discussion	Rel-20	FS_6G_Radio
R2-2603749	Reconfiguration Failure with Parallel RRC Procedures	Jio Platforms	discussion	Rel-20	FS_6G_Radio	Withdrawn
R2-2603782	Module-level failure reporting on RRC configuration	Fraunhofer IIS, Fraunhofer HHI	discussion	R2-2602300
R2-2603819	Reconfiguration Failure with Parallel RRC Procedures	Jio Platforms	discussion	Rel-20	FS_6G_Radio
R2-2603944	Discussion on RRC ASN.1 Restructuring and modular	Samsung	discussion	Rel-20
R2-2603964	Discussion on RRC structure and reconfiguration	Sharp	discussion	Rel-20	FS_6G_Radio
R2-2604016	Discussion on Radio Protocol Architecture – Control Plane	Rakuten Symphony	discussion	Rel-20 	Withdrawn
R2-2604029	Discussion on 6G RRC Modular Design and Configuration failure	Google Korea LLC	discussion	FS_6G_Radio
R2-2604063	RRC Design, RRC (re)configuration and Harmonized RRC procedures	1Finity	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.2-a002`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.2 RRC Structure and (re)configuration

```text
Only relying on reporting of failed configuration during RRC reestablishment procedure (legacy or simplified) to handle Reconfiguration failure cannot achieve the design target of service interruption avoidance from UE perspective.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.2-o001`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.2 RRC Structure and (re)configuration

```text
In commercial network deployments, the RRC configuration parameters signaled to UEs with similar capabilities and service types are frequently identical or nearly identical, resulting in the network repeatedly transmitting the same parameter sets during initial access, across different cells, and during frequent UE-dedicated reconfigurations.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.2-o002`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.2 RRC Structure and (re)configuration

```text
RRC signaling overhead and latency for initial configurations, state transitions, and frequent repetitive reconfigurations can be significantly reduced by utilizing a framework of reference, default, or stored configurations rather than explicitly signaling full parameter lists.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.2-o003`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.2 RRC Structure and (re)configuration

```text
Use of delta configuration alone to change between typical configurations associated with different profiles (e.g., eMBB, XR, RedCap) may not be signalling efficient.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.2-o004`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.2 RRC Structure and (re)configuration

```text
RAN2 to consider the following options for reporting the reconfiguration failure information:
-	UE reports which RRC module includes the erroneous configuration;
-	UE indicates non-compliant configuration parameters via pre-defined or implicit parameter indexes;
-	UE reports the bit-stream positions in the RRCReconfiguration message for the network to locate configuration errors;
-	UE sends an RRC container of RRCReconfiguration message which includes erroneous parameters and their values (if any).
Noted
R2-2603320	Further details on reconfiguration failure handling	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.2-p001`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.2 RRC Structure and (re)configuration

```text
RAN2 to discuss and down-select among the following options for UE reporting of partial reconfiguration failure: option 1) indicate a single flag that one or more parameters were not applied, option 2) report back the IDs of fields or groups of fields that the UE could not apply, option 3) echo the ‘delta’ of RRC configuration that the UE received vs applied, option 4) echo the whole RRC configuration that the UE applied.
Noted
R2-2603462	RRC reconfiguration failure handling	MediaTek Inc., Huawei, HiSilicon, Ericsson	discussion	Rel-20	FS_6G_Radio
Proposal 3 	The UE reports top-level fields or groups of fields (such as RRC modules/containers, if such will be defined) of the RRC reconfiguration in the "RRC reconfiguration failure report". A failure cause can also be included (e.g., decoding failure, unexpected field, missing field, invalid combination, details FFS).
Noted
Discussion
-	ZTE would like to know which specific IE caused the problem, the module isnot enough as we may have a very big module so it would be very hard to identify where the problem starts.   So the 3rd option of representing the position in the RRC reconfiguration message that caused the problem.
-	Nokia thinks we should not spend too much time on fixing this and has sympathy on what ZTE commented, so what is technically feasible for the UE to provide and how much can it can provide for the error case.
-	Vivo indicates that it is feasible to report the IEs and would be useful.
-	Huawei is concerned that it is not possible to identify one particular IE, so it may be difficult to provide too many details.    We should identify options and then study the feasibility.
-	Lenovo thinks that this should not force us to have to ASN.1 modifications and IDs just for this.
-	Jio thinks that our ultimate goal is to understand how we can fix this reconfiguration problem, so we should take the appropriate time.  Initial step can be the category of the problem and then we can discussion what information.
-	Qualcomm doesn’t think that the problems of decoding are actual problems.   Interdigital thinks that we should provide sufficient information to the network, rather than a high level problem type.  Start with high level like module.
-	Offinno thinks that modular is a good start but perhaps we don’t need a very detailed report.
-	Mediatek doesn’t thinks that option 3 and 4 are feasible.  Option 3 can’t be handle by current ASN.1  Option 4 is not clear how you echo back only the optional parameters.
-	High level granularity is sufficient
-	Apple thinks that IE level information is feasible.
-	Samsung thinks that cause value can be useful but there are some concerns on the number of values but good with Mediatek’s proposal as baseline.
-	Qualcomm points out that we should provide information to solve the reconfiguration aspects and not long term debugging, like for SCell if config cause the problem the network can solve it by not configuring.
-
Aim to have a finer granularity reporting of the configuration that caused the problem.   How and what is possible can be discussed after further clarity on how ASN.1/RRC structure will look like.
[AT134][004][6G CP] RRC reconfiguration (Xiaomi)
Intended outcome:  Offline on understand if there is a solution that reduces interruptions in the UE, including simplified recovery, fallback
Deadline:  Thursday
R2-2604392	Summary of [AT134][004][6G CP] RRC reconfiguration (Xiaomi)	Xiaomi (Rapporteur)	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.2-p002`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.2 RRC Structure and (re)configuration

```text
RAN2 studies a simplified procedure for (re)configuration failure handling, with some operations skipped (e.g., cell search, security key derivation, etc.) to reduce UE service interruption, compared with NR re-establishment. FFS specific operations to be skipped.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.2-p003`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.2 RRC Structure and (re)configuration

```text
RAN2 further discusses whether the simplified procedure is based on "RRC Re-establishment" procedure (i.e., RACH+CCCH for RRC Reestablishment Request) or other RRC procedures.
-	Nokia thinks we can study it but it is important to understand that we will not specify a different procedure.
-	Vivo thinks that companies are concerned with RRC re-establishment.   Apple also agrees and the re-establishment still doesn’t provide enough interruption opportunities.   Oppo thinks that UE vendors would like to do more which may come with some complexity to NW but we should further study.
Noted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.2-p004`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.2 RRC Structure and (re)configuration

```text
RAN2 confirms that the study on (re)configuration failure handling in 6GR should aim at avoiding service interruption at the UE as much as possible.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.2-p005`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.2 RRC Structure and (re)configuration

```text
RAN2 further studies how to avoid UE service interruption and enable the UE reporting of erroneous/inapplicable configurations in 6GR upon (re)configuration failure, taking the following candidate solutions for further study:
1.	Partial (re)configuration success
	Solution 1-A: UE applies the good/applicable configurations, ignores the erroneous/inapplicable configurations and reports this to the NW, if the reconfiguration failure happens to the "non-critical" configurations; otherwise, UE triggers RRC reestablishment.
	Solution 1-B: UE applies the good/applicable configurations and reports the erroneous/inapplicable configurations for which the UE applies default/fallback values configured by the NW, if reconfiguration failure happens to "non-critical" configurations; otherwise, UE triggers RRC re-establishment.
2.	(Re)configuration failure reporting with UE fallback operations
	Solution 2-A: UE continues using the current configurations (prior to reception of RRC Reconfiguration) to resume its communication and reports to the NW the erroneous/inapplicable configuration(s) (based on which NW may decide to keep the UE continuing with the current configuration or perform further reconfiguration).
	Solution 2-B: UE applies the NW-configured fallback/default configuration to resume its communications, and reports the erroneous/inapplicable configuration parameter(s) to the NW (where the fallback/default configuration may include minimum set of configurations that enable UE's basic data transfer).
R2-2603462	RRC reconfiguration failure handling	MediaTek Inc., Huawei, HiSilicon, Ericsson	discussion	Rel-20	FS_6G_Radio
Proposal 2 	In 6GR, RRC reconfiguration failure (non-mobility scenario) handling is based on a simplified RRC connection re-establishment procedure in which cell search, security key derivation, and bearer re-establishment are not performed, and during which the user data transfer is resumed without subsequent RRC reconfiguration procedure.
R2-2603878	RRC (re)configuration and Failure Reporting for 6G	CMCC, ZTE Corporation, CATT, Huawei	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.2-p006`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.2 RRC Structure and (re)configuration

```text
5G NR real network test statistics by CMCC indicate that the probability of re-establishment caused by reconfiguration failure is approximately less than 0.0004. Therefore, 6GR design should prioritize state machine consistency and robustness rather than introducing excessive complexity for UE autonomous partial application.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.2-p007`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.2 RRC Structure and (re)configuration

```text
RAN2 should consider not to support the mechanism of UE autonomous partial application of RRC configuration in 6GR, as it introduces unacceptable cross-layer state mismatches and immense specification complexities.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.2-p008`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.2 RRC Structure and (re)configuration

```text
RAN2 can confirms that RRC connection re-establishment remains the baseline procedure triggered in case the UE can only apply a part of the critical RRC reconfiguration.
R2-2603004	Discussion on (Re-)Configuration Failure	OPPO	discussion	Rel-20	FS_6G_Radio
Observation 3	The gain from partial configuration seems not justified by its complication / risk leading to configuration conflict.
Proposal 4	Upon (re)configuration failure, at least support full (instead of partial) configuration fallback, either 1) fallback to default/SIB1 configuration, or 2) fallback to prior configuration. R2 further discuss whether to additionally support ‘partial’ configuration after further progress of ASN.1 structure design (e.g., the modular design).
Stored Configurations
R2-2603794	On the use of Stored Configurations for 6G	InterDigital, Nokia, Jio Platforms Limited, Apple, Samsung, CMCC, Qualcomm, Ofinno, Sony, LG Electronics	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.2-p009`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.2 RRC Structure and (re)configuration

```text
RAN2 to study a method to allow the network to configure the UE by indicating an Identifier (ID) or Index that refers to a known set of baseline parameters, instead of the entire configuration.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.2-p010`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.2 RRC Structure and (re)configuration

```text
RAN2 to support delta signaling relative to an indicated reference or stored configuration, allowing the network to activate a specific set of baseline parameters while simultaneously signaling only the specific parameter modifications (deltas) to that baseline in the same message.
-	Ericsson thinks that if we don’t improve something in terms of UE behavior and how the messages are processed there isn’t much gain with just the signaling.   Nokia explains that we need to discuss how this work and then understand the gain for the same cell case.    Huawei thinks that pre-processing seems impossible to do, we should bring examples of procedure on how the UE processes that if we study this.
-	Jio thinks that for LTM it was only targeting mobility scenario and we are now thinking of UEs that have different services and those service require different configurations so it is inefficient.
-	Xiaomi thinks we can study but need to understand how the stored configuration is acquired by the UE from the beginning.
-	Qualcomm explains that we have two things, processing and application of configuration. Confirms that we can reduce processing time if you know the parameters, at least you can do a checking on parameters.   Apple agrees with Qualcomm.  Apple explains that today we have the default configuration to avoid signaling overhead and that is not sufficient.
-	CMCC thinks that we can study further some of this aspects like how to get the stored configuration etc.
-	ZTE is also open to study it, but think how the configuration is provided (e.g. SI or dedicated), whether we require the UE to acquire the SIB, etc.
-	CATT is also open to study and would like to understand the target use case.
-	Ericsson thinks that the goal should be on improving transitions from inactive to connected, but if you save signaling and the UE takes the same amount of time, then it is not that useful.  Nokia agrees that we should study the gain, is it just a signaling or a latency gain, but let’s not forget connected to connected.
Noted
R2-2604209	RRC Stored Configuration	InterDigital	discussion	Rel-20	FS_6G_Radio
Noted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.2-p011`

### [6G/Rel-20 RAN2#133bis] `agreement` 9.3.2.1 RRC Modelling and connection management

```text
1	For delay insensitive/ bursty traffic, RAN2 continues the study with focus on “Inactive” state.  FFS what it is called and exact modelling.
2	For delay sensitive and bursty traffic, RAN2 can continue studying further aspects related to UE power saving from mobility perspective in connected mode (e.g. benefits/security impact/feasibility of UE not notifying the network every cell switch with pre-configuration).
Not treated
Modeling
R2-2602614	Views on 6G Inactive State/Sub-State	Apple	discussion	Rel-20	FS_6G_Radio	R2-2602229
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.1-a001`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.2.1 RRC Modelling and connection management

```text
The proposed “inactive sub-state” in RRC CONNECTED state has two main designs:
The sub-state transition between inactive and normal is same as the transition between “DRX ON” and “DRX OFF” in the WUS based CDRX design.
The UE based mobility design utilizes the CLTM framework and considers additional power saving design (e.g. no measurement report).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.1-o001`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.2.1 RRC Modelling and connection management

```text
An inactive/idle state with stored context is unlikely to meet the needs of devices with bursty, delay-sensitive traffic.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.1-o002`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.2.1 RRC Modelling and connection management

```text
An RRC_CONNECTED substate is unlikely to meet the needs of devices with infrequent, delay-insensitive traffic such as low-end IoT.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.1-o003`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.2.1 RRC Modelling and connection management

```text
Some foreseeable use cases would be best served by regular transitions from a low-power substate (e.g., C-DRX-based) to continuous downlink monitoring.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.1-o004`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.1 RRC Modelling and connection management

```text
For small data exchange in inactive state, Network is not required to reserve dedicated radio resource for the UE in the neighbour cells. When UE is in inactive state, dedicated signalling for resource configuration is not required before the small data exchange for both MT and MO cases.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.1-p001`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.1 RRC Modelling and connection management

```text
The state transition from connected state to inactive state should be done via explicit network signalling (e.g. RRCRelease) that is security protected.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.1-p002`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.1 RRC Modelling and connection management

```text
Cell selection and reselection should be supported as UE based mobility for inactive state. No connected mode RLM/RRM is applicable for the inactive state and the UE power consumption in inactive state should be comparable to that of idle state.
Noted
R2-2601528	Discussion on Inactive/Sub-state for 6G	Ericsson, T-Mobile USA	discussion	Rel-20
Observation 1	UE based mobility is supported for the additional state, i.e., Inactive/Sub-state, to achieve UE power consumption on par with the RRC Idle state.
Observation 2	It is unclear how UE-dedicated WUS can work when the UE cell-level location is unknown and without requiring UE specific resources to be reserved in the target cells in advance.
Proposal 1	Mobility in Inactive/Sub-state should not require UE specific resources to be reserved in the target cell in advance (such as RACH preambles, C-RNTI, SR resources, etc).
-	Huawei asks what use case this is addresses.    ZTE thinks that for very small delay services the UE can stay in connected.    ZTE asks for sub-state is it both UL and DL.  Huawei confirms.
Noted
Discussion
-	Interdigital asks about the sub-state, as for inactive it is very clear where the power saving gains are coming from, so where is it coming from for the sub-state.   Oppo thinks that we can have some power saving gains from the UE not always reporting.
-	Samsung understood that we would try to discuss common functionality.
-	ZTE thinks that the power saving gain comes from C-DRX and WUS and not from sub-state.  Vivo thinks it is because the UE doesn’t need to notify the NW when it changes cells.
-	Apple thinks that power saving should be handled with conditional mobility and DRX/LP-WUS.
-	Qualcomm thinks that for delay sensitive what we are actually doing is looking at connected state enhancements and more from a power saving perspective. WE shouldn’t mix it with inactive discussion as they serve different purposes.
-	Mediatek thinks that for delay sensitive we didn’t agree that we need sub-state for connected but rather study on power saving.
-	Docomo would like to ensure that we are not duplicating the solution.
-	AT&T would like to discuss further the resource capacity issue in inactive state.    Samsung thinks that the pain point for inactive state was paging and that why we agreed to have a single paging mechanism.
-	Huawei thinks that we should add bursty for connected mode.   CATT thinks that we can consider bursty traffic in connected or inactive.   Ericsson also thinks that inactive can handle both bursty and insensitive, there shouldn’t be a limitation.
-	Nokia thinks that it can be handled in both cases
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.1-p003`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.1 RRC Modelling and connection management

```text
To support two target scenarios, RAN2 should study both the RRC INACTIVE state and “inactive sub-state” in RRC CONNECTED state.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.1-p004`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.1 RRC Modelling and connection management

```text
Support 6G RRC INACTIVE state, which is based on 5G RRC INACTIVE state design and replace RAN paging with 6G single paging design.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.1-p005`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.1 RRC Modelling and connection management

```text
Split the study of “inactive substate” into the following two directions in RRC CONNECTED state:
1) WUS based CDRX design
2) Conditional connected mobility.
R2-2601882	Options for power saving "inactive-like" operation	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.1-p006`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.1 RRC Modelling and connection management

```text
RAN2 plan to support a C-DRX-based substate of RRC_CONNECTED with UE-controlled mobility and no measurement reporting for the benefit of devices with bursty but delay-sensitive traffic.  Transitions between this substate and conventional RRC_CONNECTED (with continuous downlink monitoring and network-controlled mobility) should be as efficient as possible in terms of signalling overhead, transition time, and power consumption.  FFS if the mobility area is the same as the TA.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.1-p007`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.1 RRC Modelling and connection management

```text
Study connection suspend/resume mechanisms for a UE going to or coming from RRC_IDLE, using the LTE mechanisms as a starting point (including CN awareness and CN paging).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.1-p008`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.1 RRC Modelling and connection management

```text
RAN2 plan to address the C-DRX enhancements for bursty and delay-sensitive traffic first, with the initial assumptions (subject to being revisited) that the idle-mode enhancements for wakeup triggering will initially follow paging decisions and identifier definition will follow the model of the C-DRX solution.
R2-2601437	Discussion on RRC Modelling and Connection Management	LG Electronics Inc.	discussion
R2-2601439	Discussion on 6GR RRC Modelling and Connection Management	CATT	discussion	Rel-20
R2-2601449	Discussion on RRC Modelling of IDLE with suspend	vivo, Huawei, HiSilicon, NTT DOCOMO INC.	discussion	Rel-20
R2-2601490	RRC state modelling	Lenovo	discussion	FS_6G_Radio
R2-2601493	Pain points of NR RRC connection re-establishment and how to resolve them in 6GR	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
R2-2601505	Substate, RRC modeling and basic RRC procedures in 6GR	Xiaomi	discussion	Rel-20	FS_6G_Radio
R2-2601516	Discussion on 6G RRC state(s) and functionalities	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
R2-2601724	RRC state functionalities	Panasonic	discussion	Rel-20
R2-2601796	Discussion on 6G RRC states	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
R2-2601859	RRC Modelling and connection management	Ofinno	discussion
R2-2601882	Options for power saving "inactive-like" operation	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
R2-2602043	RRC modelling and connection management	Nokia	discussion	Rel-20	FS_6G_Radio
R2-2602052	Discussion on RRC Modelling and connection management in 6G	Transsion Holdings	discussion	Rel-20
R2-2602073	Discussion on RRC state for 6GR	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2602109	Discussion on functions of RRC state	Spreadtrum, UNISOC	discussion	Rel-20
R2-2602163	Discussion on Inactive state / sub-state	Sony	discussion	Rel-20	FS_6G_Radio
R2-2602195	RRC State Model for 6GR	InterDigital, Inc.	discussion	Rel-20	FS_6G_Radio
R2-2602229	Views on 6G Inactive State/Sub-State	Apple	discussion	Rel-20	FS_6G_Radio
=> Revised in R2-2602614
R2-2602614	Views on 6G Inactive State/Sub-State	Apple	discussion	Rel-20	FS_6G_Radio
R2-2602278	Further discussion on RRC functionality in Inactive	NEC	discussion	Rel-20	FS_6G_Radio
R2-2602326	Discussion on inactive state/sub-state	Toyota ITC	discussion	Rel-20
R2-2602354	Discussion on RRC Inactive vs Sub-state in 6GR	Rakuten Symphony	discussion	Rel-20
R2-2602375	RRC Modelling for 6GR	Kyocera	discussion
R2-2602393	Discussion on RRC states in 6G	NTT DOCOMO	discussion	Rel-20
R2-2602405	Discussion on small data transmission in the new 6G RRC state	KT Corp.	discussion
R2-2602420	Discussion on 6G RRC states	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2602453	Discussion on 6G RRC inactive state	Google Korea LLC	discussion	FS_6G_Radio
R2-2602490	RRC functionality and connection management in 6GR	SHARP Corporation	discussion	R2-2600557
R2-2602496	Discussion on RRC functionality and connection management	Samsung	discussion	Rel-20	FS_6G_Radio
R2-2602539	Discussion on 6G RRC states	Qualcomm Incorporated	discussion
R2-2602543	RRC modelling and connection management	1Finity	discussion	Rel-20
R2-2602587	Further discussion on functionalities for 6GR RRC states	TCL	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.1-p009`

### [6G/Rel-20 RAN2#133bis] `agreement` 9.3.2.2 RRC Structure and (re)configuration

```text
Agree on the following for 6G RRC structure:
1)	Define additional parameterized types that are consistently used in 6G RRC. FFS on the details of the parameterized types
2)	Utilize ID-based linking in 6G RRC configuration to allow cross-referencing parts of the configuration elsewhere. FFS how the IDs are defined
3)	Except for mandatory features, UE need not comprehend the entire ASN.1 configuration. FFS how this can be accomplished (e.g. containers, ASN.1 modules, …)
4)	We aim to make the proposals more detailed in terms of ASN.1. The discussion does not pre-empt other decisions in other sessions or WGs, these decisions are purely from RAN2 perspective, and we will adapt to their decisions as needed.
[AT133bis][004][6G] RRC structure and ASN.1 (Nokia, Ericsson)
Intended outcome:
For RRC structure:
Discuss offline companies views/interests for selecting a single approach (e.g. via combining all the approaches)
Discuss the mitigation mechanisms for the downsides of the chosen approach(es) in an offline discussion during RAN2#133bis. The goal of the offline discussion would be to at least find out if there are any issues requiring further discussion in the next meeting(s).
For RRC structure and ASN.1
Next steps and guidance for RRC structure (e.g. evaluation, details and examples, etc) and ASN.1 topic
Deadline:  Friday
R2-2602812	Report of [AT133bis][004][6G] RRC structure and ASN.1 (Nokia, Ericsson)	Nokia (Rapporteur), Ericsson (rapporteur)	report	Rel-20	FS_6G_Radio
Noted
After comeback:
-	Rapporteurs explains that instead of contributions we can continue the discussion in a more constructive manner.   We can have an email discussion until August to identify some questions and we can discuss in the may meeting offline and the report will only be discussed online in august.   We should not try to shoot down proposals but just understand how it works first.
-	Ericsson thinks that companies should consolidate their proposals so they are easier to understand as a full idea.
-	Qualcomm thinks that we shouldn’t invite new ideas and it should be based on already provided examples.
-	Nokia thinks that we should keep thinking.
-	Huawei thinks that we should provide the examples based on the real NR fields.
-	Nokia highlights that we should use the email reflector for some technical discussion rather than just providing inputs.  It will be clear when technical discussions are invited over the reflector.
Have a long email discussion until August.   Phase the email discussion such that first phase discussion questions/guidance can be discussed offline in RAN2#134 (No official meeting report expected in RAN2#134).    Second phase continues until RAN2#135.
NOTE: based on examples already provided in the previous email discussions and the agreements
[POST133bis][009][6G CP] RRC structure and ASN.1 (Nokia, Ericsson)
Intended outcome:  Report in August meeting providing more details on RRC structure.  Exact scope and definition of the phases up to rapporteurs
Deadline:  August email discussion deadline
R2-2602329	Report of [POST133][006][6G] ASN.1 discussion	Ericsson	discussion	Rel-20	FS_6G_Radio	Late
Delta Signalling
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.2-a001`

### [6G/Rel-20 RAN2#133bis] `agreement` 9.3.2.2 RRC Structure and (re)configuration

```text
All fields (except for fields that should always be configured(i.e. logically mandatory fields)) that support delta signalling (i.e., the possibility to maintain/keep their previous value) shall also offer means to release them (explicitly by signalling or implicitly upon absence).
Continue discussions on refining the proposed delta signalling solution directions (“partial full config”, “release by default + signal to keep”) and continue their evaluation in terms of robustness and signalling overhead. Investigate whether it is meaningful to combine them in some way. Take related aspects into account (e.g. “configuration constraints”).
3	Continue discussions on analysing and quantifying the listed (potential) benefits and drawbacks of OCTET STRINGs in terms of message size and processing time. Aim to derive rules in which cases (message size, number of extensions, …) OCTET STRINGs should be used or avoided.
4	Aim to introduce a parameterized type to generalize the handling of delta-signalling lists (instead of NR’s separate- and case-specific lists for AddMod- and Release). Discuss further details of such (e.g. whether and how to support release+add) taking agreements on delta signalling and configuration constraints into account.
5	RAN2 should aim to capture at least typical constraints (setup vs. modify) in the signalling structure.   FFS the details and how/when to apply it
6	RAN2 should introduce configuration constrains when it is necessary to rule out some configuration.
7	Consider the extensible ID (CHOICE of INTEGERs) as a tool in the toolbox that could serve as a safety net when it is difficult to predict the required size of IDs (and lists) that are difficult to extend by other means. RAN2 will decide on a case-by-cases basis, whether and where to use extensible IDs.
8	Study and discuss further in which scenarios parallel lists have benefits over per-element extensions and over critical extensions of the entire lists. Investigate also the signalling overhead of the different solutions for practical sizes of lists.
9	Continue study lists extensions.
Reconfiguration Failure
R2-2601506	Further discussion on (re)configuration failure handling in 6GR	Xiaomi, Samsung, Apple, InterDigital Inc., Sharp, Kyocera, Ofinno	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.2-a002`

### [6G/Rel-20 RAN2#133bis] `agreement` 9.3.2.2 RRC Structure and (re)configuration

```text
1	When a (re-)configuration failure occurs the UE reports the reason(s) for the (re-)configuration failure (e.g. what part of configuration caused the failure).  FFS on details of reporting.  FFS whether the UE can avoid re-establishment in such scenarios and/or if we can improve the re-establishment procedure.
Stored Configurations
R2-2601843	Stored RRC configurations for 6G	Nokia, CMCC, Jio Platforms, Apple, Samsung, Interdigital	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.2-a003`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.2.2 RRC Structure and (re)configuration

```text
NR’s delta signalling results in too many cases where the gNB must apply a full configuration since it cannot determine a delta-configuration that brings UE and gNB reliably to the same configuration state.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.2-o001`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.2.2 RRC Structure and (re)configuration

```text
A target gNB implementing an earlier ASN.1 version can skip non-comprehended extensions and NCEs at the end of the message. But it fails to decode the remainder of the message when the source gNB uses e.g. a newly defined CHOICE option that was declared as spare (NULL) in the target gNB’s ASN.1 version.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.2-o002`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.2.2 RRC Structure and (re)configuration

```text
If a UE discovers extensions of a later release than it implements, it may assume a network- or transmission error and should declare that it cannot comply with the configuration
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.2-o003`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.2.2 RRC Structure and (re)configuration

```text
Need codes in ASN.1 comments, field descriptions, condition tables and procedural text are fragile, and handling thereof cannot be automated reliably. This contributes to the problem that gNBs fall back to a full configuration too often.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.2-o004`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.2.2 RRC Structure and (re)configuration

```text
Fields that are kept by default (“Need M”) and that do not offer means for explicit release (SetupRelease), can cause substantial signalling overhead and to the observed problem of too many full configurations.
Noted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.2-o005`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.2 RRC Structure and (re)configuration

```text
Discuss the potential for selecting a single approach (e.g. via combining all the approaches) over reflector until the RAN2#133bis start.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.2-p001`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.2 RRC Structure and (re)configuration

```text
Continue to discuss the mitigation mechanisms for the downsides of the chosen approach(es) in an offline discussion during RAN2#133bis. The goal of the offline discussion would be to at least find out if there are any issues requiring further discussion in the next meeting(s).
Noted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.2-p002`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.2 RRC Structure and (re)configuration

```text
Study on (re)configuration failure handling in 6GR should aim at both enabling the UE to provide sufficient information to the NW on erroneous/inapplicable configurations and reducing service interruption between UE and the NW as much as possible.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.2-p003`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.2 RRC Structure and (re)configuration

```text
Support UE reporting of the erroneous/inapplicable configurations to the NW for (re)configuration failure (i.e. UE can only apply a part of RRC reconfiguration) in 6GR. FFS the specific configurations whose failure needs to be reported and the reporting granularity for such configurations.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.2-p004`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.2 RRC Structure and (re)configuration

```text
RAN2 further studies how to avoid UE service interruption and/or enable the UE reporting of erroneous/inapplicable configurations in 6GR upon (re)configuration failure, taking the following candidate solutions as the baseline:
1.	Enhanced RRC Re-establishment
	Solution 1-A: UE triggers RRC Re-establishment during which the erroneous/inapplicable configurations are reported to the NW;
2.	Partial (re)configuration success
	Solution 2-A: UE applies the good/appliable configurations and ignores the erroneous/inapplicable configurations which are reported to the NW, if the reconfiguration failure happens to the "non-critical" configurations; otherwise, UE triggers RRC reestablishment.
	Solution 2-B: UE applies the good/appliable configurations and reports the erroneous/inapplicable configurations for which the UE applies default/fallback values configured by the NW, if reconfiguration failure happens to "non-critical" configurations; otherwise, UE triggers RRC re-establishment.
3.	(Re)configuration failure information reporting w/o Re-establishment or partial (re)configuration
	Solution 3-A: UE continues using the current configurations to resume its communication and reports to the NW the erroneous/inapplicable configuration(s) (based on which NW may decide to keep the UE continuing with the current configuration or perform further reconfiguration).
	Solution 3-B: UE applies the NW-configured fallback/default configuration to resume its communications, and reports the erroneous/inapplicable configuration parameter(s) to the NW (where the fallback/default configuration may include minimum set of configurations that enable UE's basic data transfer).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.2-p005`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.2 RRC Structure and (re)configuration

```text
As a general principle, (re)configuration failure handling by the UE should be under NW control. FFS how the NW controls UE behaviour for (re)configuration handling, pending the specific solution to be adopted.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.2-p006`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.2 RRC Structure and (re)configuration

```text
RAN2 carries out the pros and cons analyses for the listed candidate solutions in Proposal 3, as the next step for 6GR (re)configuration failure study.
Noted
R2-2601990	Simplified RRC connection re-establishment for RRC reconfiguration failure	MediaTek Inc., Nokia, Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
Proposal 1 	Do not define partial application of the RRC configuration in RRC reconfiguration failure or categorization of the UE configuration parameters to critical and non-critical parameters in 6GR.
Proposal 2 	RAN2 to study improvement on RRC reconfiguration failure (non-mobility scenario) handling in 6GR based on a simplified RRC connection re-establishment procedure, in which the UE applies simple physical layer and MAC configurations for the purposes of re-establishment signalling, in which cell search, security key update, and bearer re-establishment are not performed, and during which the user data transfer is resumed without subsequent RRC reconfiguration procedure.
Proposal 3	After triggering the simplified RRC connection re-establishment procedure, the UE signals the network about it. This signalling identifies the UE in unambiguous and secure manner. The network responds with reconfiguration of the UE with more sophisticated physical layer and MAC configurations for the user data transfer to continue. Signalling during the procedure could also let the network know which part(s) of RRC reconfiguration caused the RRC reconfiguration failure.
Noted
Discussion
-	Qualcomm explains that the main problem was not being able to apply one minor configuration and now we are making things worst.   The intention is to not always do re-establishment.
-	Huawei thinks that improved re-establishment is improving service interruption as it is not the usual re-establishment.  The network would reconfigure the UE.   Xiaomi thinks that we can’t avoid the interruption as we need to do random access.
-	CMCC would like to understand the main issue and according to the real field results this happens very rarely 2% amongst the re-establishment failures that also occur 2% of the time.   We can just report something and that’s it.   Qualcomm thinks that the network doesn’t know why it happens, 27% of failure happen because of network configuration.  CATT agrees with CMCC.
-	Ericsson agrees that we can get more information from the UE but this doesn’t mean that a new configuration will be provided.   We should make sure that the network is aware of the issue as soon as possible.   We won’t be able to get rid of the re-establishment procedure and we shouldn’t allow a partial reconfiguration as this may cause a misalignment.   ZTE has the same concerns and solution 2 and 3 don’t work from network perspective.   There are some benefits from improving the procedure by for example not triggering the full re-establishment procedure on other cells, just trigger it on the current cell.   Xiaomi explains that the UE would report which part of the configuration it applied, for example SCell configuration, or configuration on CHO canadidate cells.   In this case the PCell connection can still work.
-	Oppo agrees with ZTE and Ericsson and there seems to be complexity in the partial configuration.  However, they are open to optimize the procedure and see what can be saved.
-	Samsung thinks that even if we don’t standardize the UE can still do partial configuration so we should enhance the procedure to support some reporting and study how to enhanced.
-	Nokia thinks that there are ways to improve the re-establishment procedure, by skipping cell reselection, UP resetting etc.
-	Lenovo thinks that at least we report it to the network.   Qualcomm thinks that telling the network I couldn’t is not useful, it needs to tell more to the NW.
-	Apple thinks that even today we have some workaround that doesn’t require the UE to re-establish and this is now forcing the UE to always do re-establish.    Anyways, we have UE reporting.
-	LG agrees that the UE needs to report the problem and the reason of the problem.
-	Vivo thinks that partial configuration is a good option and it is already an implementation workaround.
-	Interdigital thinks that there will some cases where re-establishment is needed and for the reporting we can either report right away or after re-establishment.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.2-p007`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.2 RRC Structure and (re)configuration

```text
Study how to efficiently store and reuse RRC configurations for frequent RRC state transitions or configuration changes at least in the same serving cell.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.2-p008`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.2 RRC Structure and (re)configuration

```text
Study use of stored RRC configurations that can be activated in an on-demand manner by the network for both transition to CONNECTED and during CONNECTED mode.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.2-p009`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.2 RRC Structure and (re)configuration

```text
RAN2 to study and adopt a Reference Configuration framework for 6G RRC, allowing the network to configure the UE by indicating an Identifier (ID) or Index that refers to a known set of baseline parameters (e.g., a reference configuration, stored configuration, or predefined profile).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.2-p010`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.2 RRC Structure and (re)configuration

```text
Study how to enable efficient signalling (e.g. via a modular RRC) to allow network to modify stored configurations at activation time for dynamically allocated resources (e.g. UE-specific resources such as C-RNTI and PUCCH resources).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.2-p011`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.2 RRC Structure and (re)configuration

```text
The stored configurations should support delta signalling, allowing the network to activate a baseline stored configuration with specific parameter modifications (deltas) in the same message.
-	Ericsson points out we had reference configuration in 5G but they didn’t work well.   If we make delta signaling that actually is efficient we don’t need to have stored configurations.  Maintaining the reference with mobility has some complexity.    Mediatek has the same understanding as Ericsson on reference configuration.   Proposal 5 is complex.
-	Nokia explains that the proposal is for at least the same serving cell that avoids the mobility related issues, and we should avoid the reference configuration issues we introduced in 5G.
-	Oppo asks what is the dependency on modular RRC.  Nokia thinks it would work well with modular but it is not dependent on it.
-	Huawei agrees with Ericsson and in 5G the usage of reference configuration was very loosely specified and if we want something with even more flexibility it is even more complex.   Also agrees with meditek that we are doing a delta on a stored config which is complex.  Nokia explains that we are doing that for inactive.  We get a delta on top of stored config.
-	Xiaomi ask based on what information would the network configure the UE for later use.    Nokia explains that it depends on what the network wants to enable for the UE.  For example voice call or data, or something that the NW can learn.
-	Qualcomm thinks the intent is good to improve things from 5G, like improving reference config from 5G.   So we should study how to improve.
-	Lenovo asks how is this different from RRC inactive.   Nokia explain that it is one of the use cases.   We can see how to enable this in connected and aim to have the same solution.
-	LG thinks this can be very useful for CA configuration case.
-	ZTE asks if it is only for common or only for dedicated config.  What is on-demand.  Nokia explain that ondemand means it is under network control.  Common config is a monster we should avoid.
-	Apple thinks that this is very valuable.
-	Ericsson thinks that we need to clarify UE behavior with this configuration, and what we are saving.
Noted
Not treated
R2-2601450	6GR RRC Structure and (re)configuration	vivo	discussion	Rel-20
R2-2601481	Discussion on 6G RRC ASN.1 Encoding	OPPO	discussion	Rel-20	FS_6G_Radio
R2-2601492	Way forward for RRC Reconfiguration failures	Lenovo	discussion	FS_6G_Radio
=> Revised in R2-2602592
R2-2602592	Way forward for RRC Reconfiguration failures	Lenovo	discussion	FS_6G_Radio	R2-2601492
R2-2601674	Considerations on partial RRC reconfiguration failure	CATT	discussion	Rel-20	FS_6G_Radio
R2-2601860	RRC Structure and (re)configuration.	Ofinno	discussion
R2-2601951	Aspects not covered by email discussions: Reconfiguration failure handling	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
R2-2602001	Considerations on RRC reconfiguration failure	ZTE Corporation, Sanechips	discussion	Rel-20	NR_cov_Ph3
R2-2602051	Discussion on RRC structure and (re)configuration in 6G	Transsion Holdings	discussion	Rel-20
R2-2602196	RRC Reconfiguration for 6GR	InterDigital, Inc.	discussion	Rel-20	FS_6G_Radio
R2-2602230	Views on 6G RRC structure and (re)configuration	Apple	discussion	Rel-20	FS_6G_Radio
R2-2602285	6G RRC structure and reconfiguration	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio	Late
R2-2602300	Module-level failure reporting on RRC configuration	Fraunhofer IIS, Fraunhofer HHI	discussion
R2-2602327	Enhancing 6G RRC Signaling Robustness through Exception Handling	Toyota ITC	discussion	Rel-20
R2-2602363	Discussion on Radio Protocol Architecture – Control Plane	Rakuten Symphony, 1Finity , Jio Platforms	discussion	Rel-20
R2-2602371	Reconfiguration failure handling in 6G	AT&T	discussion	FS_6G_Radio
R2-2602399	On making the network aware of partial RRC reconfiguration failure	Jio Platforms	discussion	Rel-20	FS_6G_Radio
R2-2602436	Discussion on 6GR RRC Structure and (re)configuration	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2602454	Discussion on RRC structure and reconfiguration	Sharp	discussion	Rel-20	FS_6G_Radio
R2-2602455	Discussion on 6G RRC Modular Design and Configuration	Google Korea LLC	discussion	FS_6G_Radio
R2-2602487	Discussion on RRC ASN.1 Restructuring and modular	Samsung, Verizon	discussion	Rel-20
R2-2602549	Discussion on RRC (re)configuration structure	LG Electronics France	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.2-p012`

### [6G/Rel-20 RAN2#133] `agreement` 10.3.2.1 RRC Modelling and connection management

```text
1	For data transfer, the study should consider both long-cycle, delay insensitive services (e.g. low end IoT) and bursty and delay-sensitive traffic, for both MO and MT cases.   Signaling overhead, power saving, latency requirement should be taken into account.
Functionality of inactive state/sub-state
R2-2600248	RRC Inactive state for 6G	Ericsson	discussion	Rel-20
=> Revised in R2-2601127
R2-2601127	RRC Inactive state for 6G	Ericsson, LG Uplus	discussion	Rel-20
Proposal 1	6G RRC Inactive supports the following functionality:
•	UE AS context stored in UE and network enabling fast transition to RRC connected state with reduced signalling
•	An identifier (such as I-RNTI or similar) used to identify and locate the stored UE context
•	Paging used to reach the UE at incoming DL data/signalling (FFS if its RAN or CN paging)
•	UE based mobility based on cell selection/re-selection as aligned as much possible with RRC Idle
•	System information acquisition and other procedures (e.g. PLMN selection) also aligned as much as possible with RRC Idle
Noted
R2-2600942	Discussion on 6G RRC states	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.1-a001`

### [6G/Rel-20 RAN2#133] `agreement` 10.3.2.1 RRC Modelling and connection management

```text
6G Inactive/sub-state supports the following functionality
1	UE AS context in both UE and RAN
2	Signaling used to reach the UE at incoming DL data/signalling (FFS details)
3	An identifier used to identify/verify (if needed) and locate the stored UE context
4	UE based mobility is supported.  The UE doesn’t need to notify the network every time it changes cells and it doesn’t need to report measurements.   Study further whether the enhancement with pre-configuration is needed and how it works.
Mobility
R2-2600120	Discussion on Inactive State/Sub-State in 6GR	Xiaomi, Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.1-a002`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.1 RRC Modelling and connection management

```text
For periodic traffic, network can handle it well using C-DRX.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.1-o001`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.1 RRC Modelling and connection management

```text
For bursty but non-delay-sensitive traffic, there is no serious problem to use C-DRX or transfer the UE to IDLE.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.1-o002`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.1 RRC Modelling and connection management

```text
For “bursty and delay-sensitive” traffic, sub-state or (enhanced) INACTIVE could be useful.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.1-o003`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.1 RRC Modelling and connection management

```text
What is the scenario with “bursty and delay-sensitive” traffic and how much demand fosr the scenario in future market is still unclear.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.1-o004`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.1 RRC Modelling and connection management

```text
RRC_INACTIVE can reduce the overhead for uplink-triggered small data. However, downlink is limited by the paging cycle(no less than 320ms) and the constraints on data size and duration in the SDT mechanism. Therefore, it is difficult to meet the needs of bursty services that require latency around hundred-millisecond level.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.1-o005`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.1 RRC Modelling and connection management

```text
The connected sub-state enables fast transitions via L1/L2 signaling, allowing network/UE to use traffic gaps for energy saving while still meeting QoS requirements around hundred-millisecond level.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.1-o006`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.1 RRC Modelling and connection management

```text
In 5G, the use of RNA, RNA update procedure and RAN-paging are all results of having to support mobility and UE-reachability in order to support this new RAN-managed RRC_INACTIVE state providing signalling optimizations and to minimize impacts to core network.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.1-o007`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.1 RRC Modelling and connection management

```text
In 5G, introduction of RRC_INACTIVE state avoided having to manage UE AS context in RRC_IDLE and avoided having a separate UE-controlled mobility solution in RRC_CONNECTED.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.1-o008`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.1 RRC Modelling and connection management

```text
For 5G RRC_INACTIVE, CN paging in addition to RAN paging is to increase the reliability of UE reachability.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.1-o009`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.1 RRC Modelling and connection management

```text
RNA concept, RNA update procedure, RNA-level UE tracking, RAN paging and UE context transfer while in RRC_INACTIVE are all closely related concepts to support RRC_INACTIVE state impacting RAN2, RAN3 and SA2 that requires a coordinated study.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.1-o010`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.1 RRC Modelling and connection management

```text
I-RNTI like identification is required for 6G RRC-INACTIVE UEs and the identifier definition has cross workgroup dependancy and initial analysis from RAN3 may be required.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.1-o011`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.1 RRC Modelling and connection management

```text
The details of UE based mobility is still open, i.e., whether it is supported based on cell (re)selection or other forms of mobility mechanisms.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.1-o012`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.1 RRC Modelling and connection management

```text
RAN2 to clarify the target scenario for sub-state or (enhanced) INACTIVE before discussing details of the solutions.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.1-p001`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.1 RRC Modelling and connection management

```text
RAN2 to confirm that the sub-state or (enhanced) INACTIVE is useful for bursty and delay-sensitive traffic, and to study what is the scenario with the traffic.
-	ZTE asks if this is applicable to both UL and DL.
Noted
R2-2600942	Discussion on 6G RRC states	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.1-p002`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.1 RRC Modelling and connection management

```text
RAN2 studies RRC states in two different scenarios:
For long-cycle, delay-insensitive services, focus on simplifying and enhancing the RRC_INACTIVE state combined with the SDT mechanism;
For high-frequency burst traffic with short packet intervals(e.g., hundred-millisecond level), study RRC_CONNECTED sub-state.
Noted
Discussion
-	LG explain the long history and hopes that we can develop a useful inactive state.
-	Huawei thinks that we should study the two use cases - long-cycle, delay-insensitive services and high-frequency burst traffic with short packet.  Mediatek agrees that for data transfer we target low end IoT and we cover higher frequency burst traffic with efficient data transfer.
-	Fraunhofer thinks that we should cover periodic traffic
-	ZTE thinks that another target should be signaling overhead.
-	Qualcomm thinks power saving is important and wonders what is the difference with WUS.
-	Futurewei asks if we are considering having two solutions for these types of traffic.   Chair reminds everyone that we need to focus on solutions that only introduce 1 state/sub-state
-	Vivo and CATT thinks that bursty and delay insensitive.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.1-p003`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.1 RRC Modelling and connection management

```text
The Energy Efficient Sub-state, applicable for scenarios with no data transmission in RRC_CONNECTED, which is characterized by:
•	A pre-configured cell-list and pre-configuration for the cells therein.
•	UE based mobility (e.g., cell reselection or conditional reselection similar to C-LTM).
•	Low state transition latency via L1/L2 signaling.
-	Interdigital asks how L1/L2 signaling provide low state transitioning or is it the pre-configuration/context that provides the low transitioning.   CMCC explains that this means that RRC message is not required.
-	Qualcomm asks if this is for both UL and DL.   CMCC explains that L1/L2 can trigger network to wake up.
-	ZTE asks whether this includes the security as you need security for state transition.
•	Low UP resumption latency.
•	UL/DL WUS for energy saving for both NW and UE.
-	CATT asks what is the meaning of no data transmission.  CMCC explains that in sub-state there is no need for data transmission.  Mediatek asks who determines there is no data transmission, like is there an inactivity timer.  CMCC explains that it is like C-DRX.
Noted
R2-2600543	RRC_INACTIVE state functionalities	Nokia	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.1-p004`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.1 RRC Modelling and connection management

```text
RAN2 to study the following areas in 6G: a) choice of UE identification in RRC_INACTIVE, b) interaction between paging architecture and UE mobility handling, c) RRC state transition upon inter-RAT cell reselection by RRC_INACTIVE UE, and, d) PLMN reselection by RRC_INACTIVE UE.
Noted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.1-p005`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.1 RRC Modelling and connection management

```text
Consider "NW-controlled UE based" mobility mechanism (e.g. CHO/C-LTM like cell switch) as a candidate solution in the study for 6GR Substate in CONNECTED mode, where the execution of cell switch is triggered by the UE based on candidate cell configurations by the NW and UE notifies its access to the new cell after cell switch.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.1-p006`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.1 RRC Modelling and connection management

```text
In the study on Sub-state in CONNECTED mode, the fast-transition from "Sub-state" (i.e. no on-going traffic) to data exchange can be performed as follows:
	UE wakes up and monitors its DL scheduling from the NW for the first DL data arrival; or
	UE requests NW scheduling and monitors UL scheduling from the NW for the first UL data arrival.
-	Vivo thinks that this seems to be more related to power saving in connected state.   Xiaomi thinks that if we have efficient power saving mode in connected we don’t need inactive.
-	Offino asks if we have Nw-controlled UE based mobility does this mean we need to have RAN requirements on the measurements etc.   Xiaomi thinks that we can reduce the frequency of reporting for the sub-state.
-	Ericsson asks if the UE informs the network.  Why do we need an sub-state this sounds like RRC connected.
-	Huawei thinks we have to solutions – CHO like and cell reselection like.
-	ZTE thinks that the fundamental difference is that for cell reselection the network doesn’t need to be made aware, for CHO is a handover.
-	Lenovo thinks that we are not enhancing anything that the UE has to inform the network everytime it changes.  Also RRC connected needs RRM.
-	Nokia thinks that whether it is sub-state or inactive the main power saving benefit is from the UE based mobility.   Qualcomm agrees and also the requirements from RAN4 are different and it is better for the power.
-	Vodafone thinks that the main difference is that there is some preparation for cells but when the UE does the mobility it is relaxed.
-	Oppo thinks that measurements should be something to investigate in this sub-state.   There are other solutions where the UE doesn’t have to report to the network everytime there is a change.
-	CATT also thinks that the UE based mobility is the baseline.  It is simple for INACTIVE, but for sub-state the camp thinks that we are already connected so we need some form of mobility.
-	Interdigital thought that until today inactive and sub-state were similar but it appears that for sub-state we need to send the network measurements.  So if the sub-state remains a valid option the solution should be that the UE doesn’t have to notify the network everytime.
-	Xiaomi thinks that we can leave whether the UE notifies the network as FFS.
-	ZTE also thinks that the other main power saving is whether the UE is doing RRM.  CHO is being discussed in mobility so we need to first have that discussion.
Noted
Not treated
R2-2600168	RRC functionality and connection management	ZTE Corporation, Sanechips	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.1-p007`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.1 RRC Modelling and connection management

```text
The state transition from the network-controlled mobility state to a UE controlled mobility state should be done via explicit network signalling (e.g. RRCRelease) that is security protected
UE ID
R2-2600068	Discussion on 6GR RRC Modelling and Connection Management	CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.1-p008`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.1 RRC Modelling and connection management

```text
In addition to the baseline of RRC connection procedure, RAN2 considers to introduce a unique UE identification (same length as C-RNTI) which identifies the UE across RAN node(s) within a configurable valid area, applicable in any UE state (idle/inactive/connected) to support fast transition.
SDT
R2-2600248	RRC Inactive state for 6G	Ericsson	discussion	Rel-20
=> Revised in R2-2601127
R2-2601127	RRC Inactive state for 6G	Ericsson, LG Uplus	discussion	Rel-20
Observation 6	For small data transmission in 6G, it would be better to discuss and agree on the requirements rather than using the NR functionality as baseline.
Proposal 6	Small data transmission in 6G is studied based on the principles below:
a.	The target use case should apply to all transmissions, not only IoT.
b.	Data transfers should have small overhead for radio resource efficient transmission.
c.	Early indication in Msg1 should be avoided, if possible.
d.	Network should be in control of conditions for small data transmission in 6G RRC Inactive.
R2-2600168	RRC functionality and connection management	ZTE Corporation, Sanechips	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.1-p009`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.1 RRC Modelling and connection management

```text
The RAN and UE should retain at least the following UE context to enable small data transmissions with UE controlled mobility:
a.	AS security context (including security keys and material to refresh the security upon mobility)
b.	A UE ID with which RAN can uniquely identify the UE within certain area
c.	Basic RB configuration to enable small data transmission over DRB and/or SRB
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.1-p010`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.1 RRC Modelling and connection management

```text
During UE-controlled mobility, when there is no data to exchange, the network does not need to be informed of individual cell changes within a configured area
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.1-p011`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.1 RRC Modelling and connection management

```text
Small data exchange for both MT and MO cases should be supported with UE controlled mobility when RAN has stored UE context
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.1-p012`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.1 RRC Modelling and connection management

```text
For data transmission during UE controlled mobility state, RAN2 study should include use cases such as text-based interactions with AI models that typically generate small and infrequent data packets
WUS/trigger
R2-2601106	Discussion on RRC State Modelling and Connection Management	Turkcell, KPN, TIM, Huawei, HiSilicon, OPPO, Xiaomi, Meta, NEC, Sharp, Ofinno, TCL	discussion	Rel-20
Proposal 2	For the sub-state in connected state, RAN paging message is not used for faster transition to data exchange. Instead, RAN2 to study whether the network can use L1 signaling to wake up the UE (e.g., UE-dedicated DL WUS). The study should also consider the WUS related conclusions and any other forms of wake-up mechanism (including C-DRX) in energy efficiency agenda from RAN1/RAN2.
R2-2600067	Discussion on RRC Modelling and Connection Management	LG Electronics Inc.	discussion
R2-2600079	Further discussion on 6GR RRC Modelling	vivo	discussion	Rel-20
R2-2600103	Discussion on 6GR RRC connection management	WILUS Inc.	discussion	FS_6G_Radio	Withdrawn
R2-2600111	Discussion on RRC states and functionalities	Xiaomi	discussion	Rel-20	FS_6G_Radio	Withdrawn
R2-2600130	Discussion on 6G RRC Connection Management	OPPO, Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio	Late
R2-2600356	Discussion on 6G RRC state(s) and functionalities	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
R2-2600399	RRC Inactive in 6G Radio	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
R2-2600454	Views on 6G INACTIVE State	Apple	discussion	Rel-20	FS_6G_Radio
R2-2600497	"Inactive" operation and UE-initiated RRC connection release	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
R2-2600503	Discussion on RRC state for 6GR	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2600543	RRC_INACTIVE state functionalities	Nokia	discussion	Rel-20	FS_6G_Radio
R2-2600557	RRC functionality and connection management in 6GR	SHARP	discussion
R2-2600667	Discussion on functions of RRC state	Spreadtrum, UNISOC	discussion	Rel-20
R2-2600677	Discussions on RRC functionalities related to inactive/sub-state	Fainity Innovation	discussion
R2-2600722	Discussion on functionalities of 6GR RRC states	TCL	discussion	Rel-20
R2-2600725	Discussion on RRC functionality in Inactive	NEC	discussion	Rel-20	FS_6G_Radio
R2-2600747	RRC states and connection management for 6G	Lenovo	discussion	Rel-20
R2-2600762	Discussion on Inactive state for IOT devices	Sony	discussion	Rel-20	FS_6G_Radio
R2-2600775	RRC State Model for 6GR	InterDigital, Inc.	discussion	Rel-20	FS_6G_Radio
R2-2600778	RRC state functionalities 	Panasonic	discussion
R2-2600815	Sub-state functionalities for 6GR 	Kyocera	discussion
R2-2600830	RRC modelling and connection management	Fujitsu	discussion	Rel-20
R2-2600834	Discussion on UE context handling for inactive mode/sub-state	AUMOVIO	discussion
R2-2600858	RRC Modelling and connection management	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2600926	Discussion on small data transmission in the new 6G RRC state	KT Corp.	discussion
R2-2600999	Discussion on RRC Inactive mode or sub-state requirements in 6GR	Rakuten Mobile, Inc	discussion	Rel-20
R2-2601002	Discussion on 6G RRC inactive state	Google Korea LLC	discussion	FS_6G_Radio
R2-2601007	Discussion on 6G RRC states	Qualcomm Incorporated	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.1-p013`

### [6G/Rel-20 RAN2#133] `agreement` 10.3.2.2 RRC Structure and (re)configuration

```text
Delta signaling
1.	Investigate how to make the rules for delta signalling more explicit inside the signalling structure and thereby less ambiguous and less error prone to implement including the case of inter-node mobility.
2	In the context of delta signalling, investigate especially how to improve the definition and extensibility of (AddMod/Release) lists.
3	Ensure that delta signalling allows the network to modify/replace parts of the configuration without resending also large unmodified parts of the configuration.
4	Ensure that the signalling structure can represent the UE’s entire current configuration (which the UE might have received in several “deltas”), e.g. for inter-node signalling in case of inter-node handover.
Conditional Presence
5	Investigate how to specify configuration constraints unambiguously and clearly distinguish from delta signalling.
Common and dedicated configuration
6	Avoid splitting the connected mode configuration into common- and dedicated branches unless necessary to express dependencies between the UEs dedicated configuration and information provided in MIB/SIB.
ID based linking
7	Investigate how to use ID-based linking of configuration components while avoiding unfavourable signalling overhead and lack of readability.
Parallel Lists
8	Seek for consistent means to specify and extend lists in and overhead-efficient and implementation-friendly manner.
What to do next
-	Ericsson as rapporteur thinks we can now move to the phase where we discuss and see examples for all the bullets.   Xiaomi thinks that already during the email discussion there are already tools proposed in the email discussion.
-	Oppo thinks that companies have different views about the solutions and it is not clear whether we can go to another phase of email discussion.
-	Huawei thinks that companies have provided principles but when reading them it is not clear what they mean so companies need to provide clear examples.   Nokia agrees and we need to get to practical details.   Worry is that we come to next meeting and companies may not understand what was the intention.
-	Vivo thinks that we should also prioritize amongst the issue.
-	Apple thinks that we should expand the scope to include the efficiency of initial and reconfiguration.  Qualcomm agrees that we should discuss the partial configuration and how to synchronize etc.
[POST133][006][6G] ASN.1 discussion  (Ericsson)
Intended outcome:
-	Present and discuss example ASN.1 snippets addressing the agreed study scope.
-	At least in the context of delta signalling: Compare solutions e.g. with respect to their ability to setup, change, maintain and release branches at different levels (including lists), maintaining synchronization between UE and NW after several reconfiguration, ....
-	Consider aspects such as “unambiguity”, “robustness”, “maintainability”, “extensibility”, “readability”, “ease of use” from specification- and implementation perspective.
-	Generate example encodings and assess the solutions’ impact on message size for initial- and delta-configurations.
discuss details of the scope of follow up email discussion and expectations for input from companies.
Deadline:  Long
R2-2601332	Report of [AT133][006][6G] ASN.1 discussion	Ericsson	discussion	Rel-20	FS_6G_Radio
-	Companies should write to the company for which they have a question in the email discussion
Noted
For next steps:
In the context of agreed study areas (“delta signalling”, “conditional presence”, “ID based linking”, “parallel lists”...)
-	Present and discuss example ASN.1 snippets addressing the agreed study scope.
-	At least in the context of delta signalling: Compare solutions e.g. with respect to their ability to setup, change, maintain and release branches at different levels (including lists), maintaining synchronization between UE and NW after several reconfiguration, ....
-	Consider aspects such as “unambiguity”, “robustness”, “maintainability”, “extensibility”, “readability”, “ease of use” from specification- and implementation perspective.
-	Generate example encodings and assess the solutions’ impact on message size for initial- and delta-configurations.
Modular Design
R2-2600260	Report of [POST132][017][6G] RRC structure – modular design (Nokia)	Nokia (rapporteur)	report	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.2-a001`

### [6G/Rel-20 RAN2#133] `agreement` 10.3.2.2 RRC Structure and (re)configuration

```text
1	Complexity of RRC specification due to the following root causes (based on the examples highlighted in R2-2600260):
a) complex and interdependent tree-like ASN.1 structure, making specification readability harder, and having costly extensions due to linkages between RRC configurations can make signalling size larger and make it difficult to add new features to the existing ASN.1 structure
b) frequent use of fullConfig e.g. due to difficulties in delta configuration (as discussed in the [POST132](017])
c) in current ASN.1, UE has to understand more of the ASN.1 signalling than the features it supports (e.g. because the feature parameters are usually split between multiple IEs)
2	 RAN2 to consider the following aspects as starting points for solving 5G RRC problems:
-	Avoid complicated structure (e.g. BWPs) by “flattening” and “modularizing” the structure. Study the potential proposals, including how they can be extended in future releases (e.g. whether critical extensions are needed and at which level).
-	Apply conclusions of the delta signalling discussion in [POST132][017][6G] to the RRC structural discussion (e.g. to allow better machine-readability and avoid use of fullConfig).
-	Study modular design with a “basic” module supported by all UEs and additional modules supported by specific devices.  The exact details of how this could work and whether it will be supported are FFS.
3	RAN2 to perform a feasibility study on modular RRC structure. The study should consist of 1) potential ASN.1 details of the proposed structure, 2) ASN.1 module structure of the proposals and 3) guidelines to be used for the modular RRC design.
Baseline of evaluation for feasibility study is Rel-19 RRC structure.
General NOTE: The other WGs will be notified once we have progressed the study and determined what is relevant to tell them.
[POST133][007][6G] RRC structure (Nokia)
Scope: Analyze proposals for modular RRC structure for 6G:
3)	Propose a modular RRC structure with ASN.1 examples of at least the following RRC messages and features (using Rel-19 RRC structure as the content baseline)
- RRC message structure for RRCReconfiguration
- IE structure for CellGroupConfig, CSI-MeasConfig, ServingCellConfig
- Feature configuration of Carrier aggregation and NTN
4)	Extensions of modular design in later releases
Intended outcome: Discussion report
Deadline:  Long (1st phase until March 16th, 2nd phase until March 31st)
Reconfiguration failure handling
R2-2600121	(Re)configuration failure handling in 6GR – Root causes and partial (re)configuration	Xiaomi, Samsung, Apple, InterDigital, Qualcomm Incorporated, Kyocera, Sharp 	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.2-a002`

### [6G/Rel-20 RAN2#133] `agreement` 10.3.2.2 RRC Structure and (re)configuration

```text
Study how to address the (re)configuration failures.  Study if and how the results of the failure on the UE can have less interruptions and/or study how the network can be made aware of the problem.
For next meeting, bring proposals on how it works, details and examples of the solutions.
Not treated
R2-2600080	6GR RRC Structure and (re)configuration	vivo	discussion	Rel-20
R2-2600112	Discussion on RRC (re)configuration and signalling design	Xiaomi	discussion	Rel-20	FS_6G_Radio	Withdrawn
R2-2600131	Discussion on 6G RRC ASN.1 Encoding	OPPO	discussion	Rel-20	FS_6G_Radio
R2-2600192	Considerations on RRC Structure and (re)configuration	CATT	discussion	Rel-20	FS_6G_Radio
R2-2600317	RRC (re)configuration structure design and principle	LG Electronics France	discussion	Rel-20	FS_6G_Radio
R2-2600318	Aspects not covered by email discussions on RRC (re)configuration	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
R2-2600337	Practical solutions for RRC reconfiguration failure	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
R2-2600373	Considerations on 6G Modular RRC design	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
R2-2600401	Discussion on RRC structure and reconfiguration	Sharp	discussion	Rel-20	FS_6G_Radio
R2-2600455	Views on 6G RRC structure and (re)configuration	Apple	discussion	Rel-20	FS_6G_Radio
R2-2600629	Discussion on RRC structure and (re)configuration in 6G	Transsion Holdings	discussion	Rel-20
R2-2600727	Discussion on Signaling Constraints and Partial Configurations	TOYOTA ITC	discussion	Rel-20	FS_6G_Radio
R2-2600743	Discussion on Control Plane for 6GR	AUMOVIO	discussion
R2-2600794	Way forward for RRC Reconfiguration failures	Lenovo	discussion	FS_6G_Radio
R2-2600831	Split RRC Design and (re)configuration	Fujitsu	discussion	Rel-20	Withdrawn
R2-2600859	RRC Structure and (re)configuration	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2600881	Views on RRC structure for modular design	ETRI	discussion
R2-2600904	Delta-Based RRC Configuration and Need Code Enhancements in 6G	Jio Platforms	discussion	Rel-20	FS_6G_Radio
R2-2600905	On Service-Profile-Based RRC Configuration in 6G	Jio Platforms	discussion	Rel-20	FS_6G_Radio
R2-2600918	RRC Reconfiguration Failure Handling and Root Cause Visibility in 6G	Jio Platforms	discussion	Rel-20	FS_6G_Radio	R2-2508780
R2-2600927	Discussion on RRC structure and reconfiguration	KT Corp.	discussion
R2-2600966	Modular design for 6GR Protocol	CMCC	discussion	Rel-20	FS_6G_Radio
=> Revised in R2-2601113
R2-2601113	Modular design for 6GR Protocol	CMCC	discussion	Rel-20	FS_6G_Radio	R2-2600966
R2-2600983	Discussion on Radio Protocol Architecture – Control Plane	Rakuten Mobile, Inc	discussion	Rel-20
R2-2600985	Discussion on RRC Restructuring and modular aspects for 6G	Samsung	discussion	Rel-20
R2-2600989	Consideration for RRC Structure and (re)configuration	Panasonic	discussion
R2-2601003	Discussion on 6G RRC Modular Design and Configuration	Google Korea LLC	discussion
R2-2601025	Split RRC Design and RRC (re)configuration	Fujitsu Limited, NTT DoCoMo	discussion
R2-2601101	6G ASN.1 structure	TCL	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.2-a003`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.2 RRC Structure and (re)configuration

```text
Discuss whether it is necessary that RRC CONNECTED UEs (re-)acquire parameters from system information. If so, seek for means to specify/configure unambiguously which parameter the UE shall (re-)acquire from system information and which ones it shall take from the dedicated configuration.
-	 Xiaomi thinks that if we can get the information with dedicate signaling we don’t need to re-acquire SI.  Mediatek thinks we can discuss this in the SI info agenda.
-	Qualcomm thinks that we should avoid this scenario all together in 6G.  Ericsson thinks that we have parameters that all UEs must apply.
-	Interdigital thinks we should at least avoid the ambiguity.
Noted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.2-p001`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.2 RRC Structure and (re)configuration

```text
RAN2 to study how to improve on 6G RRC structure based on three main 5G RRC problem categories:
1)	Deeply nested structure (including discussion on “maintainability of RRC”) – which causes the following:
a) Added complexity and interdependencies due to tree like structure
b) costly extensions and linkages between configurations
c) readability
d) difficult to add new features
2)	Complicated RRC configuration (including discussion on “use of fullConfig”, and “machine-readability aspects”)
NOTE: this problems are based on examples highlighted in R2-2600260.
and
3)	Limiting implementation to specific device types (including discussion on “implementation and testing issues”).
-	Mediatek thinks that the deeply nest structure is not the problem but it causes the problems, like it makes it less readable.    Huawei doesn’t think that those problems are related to deeply nested structure.  It is difficult to understand the problem when companies don’t explain with real examples.  Mediatek agrees we should rather identify the problems and the understand what is the cause of this problems.
-	ZTE thinks that we can’t consider all these bullets, but we should rather prioritize the first 2.   Huawei and Xiaomi think that bullet 3 is not linked to device types and it is important to consider.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.2-p002`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.2 RRC Structure and (re)configuration

```text
RAN2 to perform a feasibility study on modular RRC structure. The study should consist of 1) potential ASN.1 details of the proposed structure, 2) ASN.1 module structure of the proposals and 3) guidelines to be used for the modular RRC design. Once the study has progressed, communication to other WGs (e.g. RAN1) on how they should take the structure into account.
-	Xiaomi thinks that we need to understand how to do the evaluation and what is the baseline.   Nokia thinks that we should take R15 and based our study on that.
-	Ericsson would like to understand what modules companies have in mind.  Huawei explain that it is to define something that only a subset of UEs understand.
Noted
R2-2601310	Report of offline discussion [AT133][007][6G] RRC structure (Nokia)	Nokia (rapporteur)	report	Rel-20	FS_6G_Radio
Noted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.2-p003`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.2 RRC Structure and (re)configuration

```text
RAN2 confirms the following reasons and root causes that result in (re)configuration failure (i.e. UE can only apply a part of RRC reconfiguration), and takes them into account for further study on (re)configuration failure handling in 6GR:
Root Cause 1 - NW signals in RRC Reconfiguration msg configuration parameter(s) that cannot be correctly applied by the UE, including:
-	Reconfiguration errors due to configuration restriction/ambiguity including cases e.g.:
•	Case 1: Mis-configuration on parameters with coupling/inter-dependency;
•	Case 2: Parameter(s) not set following the conditions/restrictions on their presence/absence;
-	Non-UE-specific configurations in dedicated signalling not supported by the UE;
-	Oppo thinks that case1 is more of a IODT problem and case 2 is linked to the ASN.1 problem we already discussed.    Xiaomi thinks that we can’t assume that the network will provide 100% correct configuration.  So in ASN.1 we intend to avoid it as much as possible.
-	Qualcomm explains that you don’t do IODT for every parameter and even if you have done IODT the problem still exists as there are different interpretation.  We are talking about practical cases where the network still gives you the wrong configuration even if you support it.  Apple agrees.
-	Jio thinks that we will always have this problem as long as humans implement this.
-	Ericsson doesn’t see this happening often in their network.  When they find it in their networks it is fixed.   Also this can’t be testable.   ZTE has the same view as Ericsson.  Root cause 2 can be discussed in UE capability change.    ZTE thinks that in the field we observe that it is not only an network error but also UE error.   Different UEs fail for the same configuration.   The network will fix the problem so we shouldn’t have a complex specification solution to fix this.
-	Huawei thinks that the UEs don’t do a re-establishment, they just ignore the configuration and that’s why other network vendors said they don’t see it happening.   We don’t need a super optimized mechanism but it could be valuable to have a way to trigger a procedure in case of error that is a little lighter than re-establishment.   This way the UE is not punished and the network knows what happened.
-	Samsung has a similar understand as Huawei, and have the same problem.  It is critical for the UE.
-	Nokia thinks we need to understand how do we know that the UE and network have the same understanding of the configuration.  Worried that partial failure will cause more problem.  It would be good to understand actual examples.
-	Huawei thinks that the intention is that the result of the failure doesn’t have such severe consequences and that somehow the network is made aware.
-	ZTE thinks that we can have a light solution.  In 5G RLF cause set to “other” is very severe, so we can still trigger re-establishment and provide information to the network on which part of the configuration failed.   Xiaomi thinks that this neglects service interruption on the UE side, so we should consider both sides.  Qualcomm agrees that the solution should help both.  Apple thinks that there are two directions, one where the UE helps and one where the interruptions on UE are less.  Both are helpful.
-	Ericsson thinks companies should understand the frequency of the problem.
Root Cause 2 - Inapplicability of the current configurations provided by NW due to change of UE capability/operating status, including:
-	Temporary UE capability restriction due to MUSIM operation;
-	Temporary UE capability reduction due to Overheating detection/power saving operation;
-	Inapplicability of NW provided functionalities for AI/ML operations;
-	Dynamic UE AS capability change with UE form-factor variation.
-	Oppo thought that the intention of UE capability change is to align it with UE capability.   Xiaomi explains that there will be cases like AI/ML or other cases that may not be solved by UE capability reporting.
-	Qualcomm thinks that this is for cases where UE dynamic update doesn’t solve it.   Interdigital thinks that even in 5G we do have UAI and we still have the problem.  Apple thinks that we may still have race conditions even with UE capability change.
-	Lenovo thinks that we will never eliminate this problem, so it doesn’t matter what the problem is, but we should do better than 5G.
-	CMCC thinks that the target should be performance and identifying the root cause will be difficult.  Re-establishment will guarantee the performance.
-	Qualcomm would like to not wait 10 years to solve the problems.  In 5G they were eventually solved but the initial release suffered.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.2-p004`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.2 RRC Structure and (re)configuration

```text
RAN2 takes the following candidate solutions as the baseline for the further study on (re)configuration failure handling in 6GR:
-	Sol.0 - RRC reestablishment is triggered if the UE is unable to comply with (part) of the (re)configuration parameter(s);
-	Sol.1 - UE applies only the good/valid configuration parameters, and ignores the invalid/inapplicable configurations parameters;
-	Sol.2 - Synchronization of applied/problematic configurations between UE and NW via UE reporting;
-	Sol.3 - UE adaptation/fallback to valid/applicable configurations under NW control;
NOTE: The solutions proposed above may not be mutually exclusive and may work jointly.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.2-p005`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.2 RRC Structure and (re)configuration

```text
RAN2 further discusses whether/how to rely on the above candidate solutions to address the (re)configuration failure due to "critical" and/or "non-critical" configurations, where:
-	"Critical" configuration corresponds to the configuration parameter that impacts whether the UE can keep the connection with the NW and perform current communications normally;
-	"Non-critical" configuration corresponds to the configuration parameters otherwise.
[3 min]
Noted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.2-p006`

### [6G/Rel-20 RAN2#132] `agreement` 10.3.2 Control plane

```text
1	Inactive mode or sub-state: In addition to what was agreed last meeting, it can also support fast transition to data exchange and network controlled transitions into state/sub-state.
2	For fast transition to data exchange, we can consider small data transmission in the new state/sub-state and/or transition to RRC connected.
3	Revisit the modelling of state or sub-state after some further progress is made on functionalities and understanding how things would work in these states.
4	Study single paging mechanism and understand the pain points and impacts of each paging mechanism.
(Not treated ) Procedures
R2-2509018	RRC connection management and structure	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
Observation 1 5G RRC does not include practical procedure for the UE to leave RRC_CONNECTED, which would be especially benefial for UE power saving purposes. Without such procedure, local RRC connection release by the UE causes a temporary desync of the UE RRC state between the network and the UE.
Proposal 1	RAN2 to study the following core list of connection management procedures of 6G RRC:
•	RRC connection establishment;
•	RRC connection reconfiguration;
•	RRC connection re-establishment for RLF/error recovery;
•	RRC connection release (including UE initiated RRC connection release).
Proposal 2 RAN2 to study UE initiated RRC connection release procedure for 6G RRC. The procedure may be initiated for power saving purposes by the UE, but may also be applied for other scenarios where avoidance of a temporary desync of the UE RRC state between the network and the UE provides benefit.
Proposal 3 6G RRC comprises a single sublayer (no upper/lower split).
[2min]
R2-2508945	Discussion on RRC modelling and connection management in 6G	Fujitsu	discussion	Rel-20
Proposal#1:
•	NR RRC functions are considered as baseline for 6GR RRC.
•	List of baseline 6GR RRC functions to be considered during study item is FFS.
Observation#1: From procedure point of view RRC Reestablishment and RRC Resume are achieving the same functionality, whereas the trigger at UE is different.
Observation#2: Resume procedure has a dependency on the definition of RRC_INACTIVE state.
Proposal#2:
•	NR RRC procedures are considered as baseline for 6GR except the Reestablishment and Resume procedure.
•	If RRC_INACTIVE state is defined, then it is worthwhile studying the unification of Reestablishment and Resume state.
Observation#3: Split RRC design allows CU-CP and DU to manage reconfigurations towards UE independently, therefore reducing control plane latency, minimizing coordination between CU-CP and DU, reducing the processing load at CU-CP and relaxing the requirements on the F1 interface.
[2min]
R2-2508405	Consideration on RRC functionality and RRC states	ZTE Corporation, Sanechips	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-a001`

### [6G/Rel-20 RAN2#132] `observation` 10.3.2 Control plane

```text
The evolution path from 2G to 5G over the year had shown that a three-state RRC state model provides a good trade-off between complexity and the ability to meet diverse services and use case requirements.
-	Oppo asks what is the use case.   Nokia explains that there are application like IoT and smartphone apps of small data burst.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-o001`

### [6G/Rel-20 RAN2#132] `observation` 10.3.2 Control plane

```text
Any unique state that has both power savings like RRC_IDLE and data activity like RRC_CONNECTED is bound to have some overlap in functionalities with other states.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-o002`

### [6G/Rel-20 RAN2#132] `observation` 10.3.2 Control plane

```text
In 6G there is still a need for RRC_INACTIVE state due to control plane latency requirement for low latency transition to RRC_CONNECTED state while still meeting the energy efficiency goals for 6G.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-o003`

### [6G/Rel-20 RAN2#132] `observation` 10.3.2 Control plane

```text
For the three-state RRC model in 5G, there are limitations on significant signaling overhead due to frequent state transition, multi-level paging in RRC_INACTIVE and limited commercial adoption for RRC_INACTIVE.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-o004`

### [6G/Rel-20 RAN2#132] `observation` 10.3.2 Control plane

```text
6G RAN will face diverse use cases requiring state management that minimizes signaling and
power consumption while allowing some flexibility per device type.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-o005`

### [6G/Rel-20 RAN2#132] `observation` 10.3.2 Control plane

```text
RRC_INACTIVE has not been widely enabled in 5G networks due to the following reasons: 1) Network planning complexity for RAN Notification Area (RNA); 2) Limited power saving gain compared to RRC_IDLE; 3) Lack of use cases requiring low state transition delay.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-o006`

### [6G/Rel-20 RAN2#132] `observation` 10.3.2 Control plane

```text
Further narrowing the RNA range leads to higher network overhead and deployment complexity.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-o007`

### [6G/Rel-20 RAN2#132] `observation` 10.3.2 Control plane

```text
For fast transition, the lower-layer transition procedure can be considered, to enable the fast switching to DL data transmission status.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-o008`

### [6G/Rel-20 RAN2#132] `observation` 10.3.2 Control plane

```text
In NR, different location area management and paging monitoring procedures for Idle and Inactive require duplicate standards and implementation efforts in both the UE and the network.
Proposal 3	Paging in Inactive mode should be same as IDLE state, i.e.
-	Only CN-initiated paging is applicable
-	Same paging DRX parameters and same paging ID
-	Same paging area management
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-o009`

### [6G/Rel-20 RAN2#132] `observation` 10.3.2 Control plane

```text
In NR, UE context storage and retrieval relies on Xn interface deployment, which is main roadblock to wide deployment of Inactive state.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-o010`

### [6G/Rel-20 RAN2#132] `observation` 10.3.2 Control plane

```text
Along with the introduction of service-based RAN arthitecture, it is feasible to deploy a new storage function to store UE context.
Proposal 4	In 6G Inactive state, the UE AS context is stored in both UE and a network node. RAN2 should study in coordination with RAN3/SA2 which network node stores UE AS context:
-	Store UE AS context in RAN node
-	Store UE AS context in CN as a container
-	Store UE AS context in a new logical storage node
[2min]
Noted
R2-2508783	UE context and location area management in non-connected RRC state	Panasonic	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-o011`

### [6G/Rel-20 RAN2#132] `observation` 10.3.2 Control plane

```text
In 5G deployment, the RRCReconfiguration procedure triggered by RAN-DU is rare.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-o012`

### [6G/Rel-20 RAN2#132] `observation` 10.3.2 Control plane

```text
Supporting RRC split (e.g. allow DU to directly send CellGroupConfig to the UE) may require more coordination between RAN-CU and RAN-DU.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-o013`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2 Control plane

```text
Adopt a three-state RRC state model for 6G based on 5G RRC_IDLE, RRC_INACTIVE and RRC_CONNECTED functionalities and study further for improvements to the functionalities of the three-state RRC state model.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-p001`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2 Control plane

```text
Study if the RRC_INACTIVE state can be made to support unique value-added functionality or if existing inactive functionalities can be enhanced to make it simpler.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-p002`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2 Control plane

```text
RAN2 should study RRC state behaviour, including paging mechanisms, identifier usage, location update procedures and the associated end-to-end latencies, ways to improve RAN Notification Area planning and deployment and UE context management.
-	Xiaomi asks if this RAN notification are would be needed for the sub-state in connected mode case.
[2min]
Noted
R2-2508965	Discussion on RRC Modelling for 6GR	TCL	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-p003`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2 Control plane

```text
to retain only two top-level RRC states – RRC_CONNECTED and RRC_IDLE – while introducing sub-states (modes) to handle different activity levels and power-performance trade-offs, and allow per-UE tailoring of the RRC sub-state machine to keep the UE lean.
[2min]
Noted
R2-2508767	RRC State Model for 6GR	InterDigital, Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-p004`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2 Control plane

```text
Consider model agnostic functionality for idle, inactive, connected as well as state transition mechanisms, with the assumption that any discussed functionality can work using either 2 state or 3 state model and that “inactive” refers to the intermediate state in both models.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-p005`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2 Control plane

```text
Revisit the state model and decide whether inactive as a connected sub-state, or as a separate RRC state, best expresses the functionality once it is known
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-p006`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2 Control plane

```text
Define latency target for fast transition from inactive to connected, e.g. 10ms.
[2min]
Noted
Discussion
-	Fraunhofer asks how the mobility in the sub-state would work.   Huawei explains that it can be UE initated mobility.   Lenovo asks if the measurement framework is reused.    Huawei explains that there is no need for measurement reports.
-	Interdigital asks what is the difference between that and inactive.   Huawei thinks that the key difference is that we don’t need RAN paging but can use WUS.   Samsung thinks that we can use WUS.
-	ZTE thinks that the state is just a label, so we can agree that we will have a UE initiated mobility and network controlled mobility.  And we can do state transitions with lower layer but in 5G we didn’t do this because of SA3 security.
-	CMCC would like to have consensus on what issue we are addressing, 1) small data transmission and 2) simplify procedures including 2 level paging.   For substate we are trying to address the power efficiency in connected mode.
-	Mediatek thinks that we should have a condition for UE controlled mobility, low latency to data exchange, power saving, small data transmission.
-	Ericsson thinks that if we start addressing the problems within sub-state we will end up with something similar to RRC inactive at the end.
-	Apple also doesn’t see much difference for sub-state and RRC inactive.   We can start by focusing.
-	Sony thinks we should consider on UE context.
-	Vivo thinks that we should consider state transition, CP latency and we can use the same concept.
-	qualcomm thinks we can start with Mediatek’s list and the proponents of sub-state should provide details on how things would work in the substate.
-	Xiaomi thinks that for sub-state we may not have CP latency as it will be just scheduling.
-	Rakuten thinks we should add signaling overhead.  Huawei thinks that’s covered by low latency.   Also we shouldn’t limit to small data, it should be for big and small.
-	Ericsson reminds everyone that we should address the problems that occurred with INACTIVE and make sure we don’t repeat them and this can be implemented.   ZTE would like to ensure that we don’t have multiple solution for this.
(Not treated) Mechanisms for Fast Transition and Energy Efficiency
R2-2508944	Discussion on RRC state and connection management for 6G	LG Electronics Inc.	discussion
Observation 1 UE context stored in the gNB side for inactive UEs can reduce initial access delay i.e. UE state transition latency and gNB-CN initial setup latency and support fast data transfer with low latency, even without RACH if CG-SDT configuration is available.
Observation 2 Support of RRC_INACTIVE helps gNB/UE to reduce the amount of resource required to transfer data and gNB/UE energy consumption, compared to RRC_CONNECTED.
Observation 3 Support of RRC_INACTIVE helps gNB/UE to reduce initial setup delay required before actual data transfer and gNB/UE energy consumption, compared to RRC_IDLE.
Proposal 1 Study enhanced RRC_INACTIVE to provide clear operational benefits over RRC_IDLE and RRC_CONNECTED, with a focus on enabling low-latency RRC resume, optimizing paging and enhancing network control over UE mobility.
Proposal 3	Introduce efficient small data transmission from 6G Day-1.
-	Introduce SDT specific BWP and carrier.
-	Support longer SDT duration: longer than 4s, e.g. up to 1 hour.
-	Reduce PDCCH monitoring in SDT procedure.
-	Introduce shared CG-SDT resource.
Observation 4 During the CG-based SDT, if non-SDT data occurs, 5G NR already supports UE state transition from RRC_INACTIVE to RRC_CONNECTED without requiring a RACH procedure.
Observation 5 If a UE has valid TA and CG for a candidate cell and their use is permitted in RRC_INACTIVE, the UE reselected to the candidate cell can perform a RACH-less resume while camped on it.
Proposal 4 Study RACH-less resume for fast transition as follows:
Consider CG based SDT as a baseline for RACH-less resume for UEs camp on the Anchor cell (=last PCell).
Reuse early TA and CG configured for cell switch (e.g., candidate cell for CLTM) as a baseline for RACH-less resume after cell re-selection to non-anchor cell.
[3min]
R2-2508845	Discussion on 6G RRC states	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-p007`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2 Control plane

```text
For the RRC_INACTIVE state evolution, the following two directions are considered:
•	Context fetch optimization: further study SDT by a more lightweight context fetch mechanism.
•	Enlarge the RNA range (e.g., merging it with the TA): it needs to be studied whether context fetch via the 6G-AMF through the NG interface introduces additional complexity and CP latency.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-p008`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2 Control plane

```text
We propose an Energy Efficient Sub-state, applicable for scenarios with no data transmission in RRC_CONNECTED, which is characterized by:
•	A pre-configured cell-list and pre-configuration for the cells therein.
•	UE based mobility (e.g., cell reselection or conditional reselection similar to C-LTM).
•	UL/DL WUS for energy saving for both NW and UE.
•	Low state transition latency.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-p009`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2 Control plane

```text
It is proposed to study the support for RACH-less functionality, CG configuration and early CSI acquisition for both PCell and SCell during the transition from Energy Efficient Sub-state to RRC_CONNECTED state.
[3mins]
R2-2508562	RRC state: requirements and functions discussion	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-p010`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2 Control plane

```text
RAN2 study the UE based mobility:
When UE is in “DRX-off”/“no-data” period, UE can perform cell switch based on its RRM measurement results, rather than being triggered by network HO command;
Upon this cell switch within a small area (e.g., several cells), UE may not notify the network.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-p011`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2 Control plane

```text
For fast transition, RAN2 to study the DL wake-up via UE dedicated layer-1 signalling, e.g., DL WUS, to replace RAN paging, which can save the latency of paging message scheduling and reception.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-p012`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2 Control plane

```text
For fast transition, RAN2 to study the aspects to reduce the preparation latency for data transmission:
	UL access latency reduction, e.g., CFRA, 2-step RA, configured grant, RACH-less;
	Measurement related latency reduction, e.g., early measurement/CSI acquisition;
	Configuration related latency reduction, e.g., pre-configured UE context/configuration.
[3 min]
R2-2508348	Suspend/Resume as an alternative to RRC Inactive	VODAFONE Group Plc	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-p013`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2 Control plane

```text
RAN 2 should investigate the suspend/resume procedure as a potential method to reduce the transition delay from IDLE to CONNECTED mode and to simplify the 6GR UE and to simplify the overall 6G system.
[2min]
Paging / Context Harmonization
R2-2508941	Discussion on 6G RRC states	Qualcomm Incorporated	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-p014`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2 Control plane

```text
RAN2 study one single location tracking management for non-connected mode (e.g. both IDLE and INACTIVE).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-p015`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2 Control plane

```text
RAN2 study managing the UE RAN context at CN for non-connected mode, including
-	Uploading UE RAN context to CN when transitioning from connected to non-connected mode
-	Delivering UE RAN context to base station for paging
[2min]
Noted
R2-2508114	Discussion on 6G RRC Connection Management	OPPO	discussion	Rel-20	FS_6G_Radio
Proposal 3 For 6G INACTIVE mode, R2 relies on R3 to study for solution candidates that reduce/remove Xn reliance to reduce deployment complexity, and if R3 decided to do so, based on the identified use case (in terms of inter-packet time and latency requirement), R2 evaluate the applicability of solution candidates in terms of CP latency.
Proposal 4 For 6G INACTIVE mode, R2 decide whether to study for solution candidates that enable fast UP resumption upon data arrival, based on the identified use case (in terms of inter-packet time and latency requirement), including 1) pro-active UE context preparation and configuration, 2) Extended RACH-less access, and 3) Early CSI acquisition/reporting.
[2min]
Noted
Discussion
-	Interdigital agrees that we should have a single mechanism but which one can be better, CN or RAN.   And we need more discussions on which state the paging is really needed.
-	Lenovo agrees on the paging.  For context, the issue in 5G was that the area of benefit was very limited because of Xn.
-	Huawei thinks we have two problem, paging simplification and Xn availability.    For paging simplification, we can decide to either have CN paging or now paging and rely on WUS.   CATT thinks we need to solve the problems in Qualcomm problem and we need to study with other working groups on context storage and retrieval without Xn.
-	Samsung would prefer to have a simple solution for paging, and for context storage we need to check with CN whether it is ok or not.
-	Sharp agrees that RAN paging is one of the pain points, so we can remove it and have only CN paging.
-	CMCC supports having single paging mechanism.   Xn is available between neighbors but not for neighbor of neighbors.
-	ZTE also supports Xn-less paging operation but this has no impact on RAN2.   We should indicate this to RAN3.   We need to study whether the UE would have two paging cycles even if we have a single CN paging mechanism.   Apple thinks one paging cycle and one type of paging.
-	Ericsson is ok to study the CN paging but we should store the context in the RAN for latency purposes.
-	Study single paging mechanisms and understand if CN paging can be used in these connected mode and what are the impacts to RAN2.  Then we can ask the other WGs.  Mediatek agrees and thinks we need to be careful.   Lenovo thinks that this is an interesting point as this means that the CN has to page the UE in connected.  Ofinno agrees with Lenovo.  If we leave the context in CN doesn’t that increase the transition time.
-	Vodafone thinks that CN paging can simplify this and RAN paging has complicated things.   Docomo would like to support Xn based paging.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-p016`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2 Control plane

```text
The following 5G RRC procedures are considered as a baseline for connection management in 6GR.
-	RRC connection establishment (for transition from RRC_IDLE to RRC_CONNECTED);
-	RRC connection resume (for transition from RRC_INACTIVE to RRC_CONNECTED);
-	RRC connection reconfiguration;
-	RRC connection re-establishment;
-	RRC connection release (for transition from RRC_CONNECTED to RRC_IDLE or RRC_INACTIVE);
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-p017`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2 Control plane

```text
RAN2 to postpone the discussion on RRC layer split until RAN3 or RAN makes decision on the support of CU-DU split and the design decisions until then should be based on a single RRC layer.
[2min]
Not treated:
R2-2508050	6GR RRC Modelling and connection management	vivo	discussion	Rel-20
R2-2508059	Discussion on RRC States in 6G Radio	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
R2-2508067	Discussion on 6GR RRC Modelling and Connection Management	CATT	discussion	Rel-20	FS_6G_Radio
R2-2508079	Discussion on RRC states and functionalities	Xiaomi	discussion	Rel-20	FS_6G_Radio
R2-2508191	RRC states and functions for 6G radio	Samsung	discussion	Rel-20	FS_6G_Radio
R2-2508226	Discussion on RRC modeling and connection management in 6G	Transsion Holdings	discussion	Rel-20
R2-2508238	RRC modelling and connection control in 6GR	Sharp	discussion
R2-2508311	RRC Inactive state in 6G	Ericsson	discussion	Rel-20
R2-2508449	Views on 6G RRC State	Apple	discussion	Rel-20	FS_6G_Radio
R2-2508500	Discussion on RRC Modelling and connection management in 6GR	China Telecom	discussion	Rel-20	FS_6G_Radio
R2-2508545	Discussion on Inactive state for IOT devices	Sony	discussion	Rel-20	FS_6G_Radio
R2-2508630	RRC Modelling and connection management	Ofinno	discussion	Rel-20
R2-2508656	RRC states and connection management for 6G	Lenovo	discussion	Rel-20
R2-2508671	Discussion on RRC functionality and states	NEC	discussion	Rel-20	FS_6G_Radio
R2-2508762	Discussion on RRC State modelling in 6GR	Rakuten Mobile, Inc	discussion	Rel-20
R2-2508767	RRC State Model for 6GR	InterDigital, Inc.	discussion	Rel-20	FS_6G_Radio
R2-2508770	RRC state modelling for 6GR 	Kyocera	discussion
R2-2508780	RRC Reconfiguration Failure Handling and Root Cause Visibility in 6G	Jio Platforms	discussion	Rel-20	FS_6G_Radio
R2-2508866	Discussion on 6GR RRC Design	AUMOVIO	discussion
R2-2508893	Considerations for RRC state in 6GR	ETRI	discussion
R2-2508935	Discussion on RRC modelling and connection management	Spreadtrum, UNISOC	discussion	Rel-20
R2-2508998	Discussion on RRC modelling and spectrum aggregation for 6GR	ITL	discussion	Rel-20
R2-2508969	Discussion on inactive state	Google Korea LLC	discussion	FS_6G_Radio
R2-2508973	Discussion on RRC states in 6G	NTT DOCOMO, INC.	discussion	Rel-20
R2-2508975	Considerations on RRC Modelling and connection management for 6GR	KDDI Corporation (TTC)	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2-p018`

### [6G/Rel-20 RAN2#132] `agreement` 10.3.2.2 RRC Structure and (re)configuration.

```text
Delta configuration is still useful in 6G to reduce signalling overhead.
At least the following issues have been identified
Issue identified: The need code introducing additional restraints (e.g., Need S) and conditions (e.g. conditional presence) are the main causes of implementation complexity and compatibility issues in delta configuration
Issue identified - The ambiguity "Functionally mandatory UE configuration parameters can be absent in over-the-air RRC messages for initial configuration of a feature/functionality" is very common in 5G RRC signalling.
Issue identified - The ambiguity "UE configuration parameters which shouldn't be modified after initial configuration of a feature/functionality can be sent in subsequent over-the-air RRC messages with new values" is relatively common in 5G RRC signalling.
Goal is to address the issues
[POST132][018][6G] ASN.1 structure (Ericsson)
Intended outcome: Identify possible ways to address the issues agreed in the meeting and capture any additional observation.
Deadline:  long
(Not treated) Other Signalling Reduction Enhancements
R2-2508349	RRC structure and configuration in 6GR	Nokia	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.2-a001`

### [6G/Rel-20 RAN2#132] `agreement` 10.3.2.2 RRC Structure and (re)configuration.

```text
Issue identified: UE can only apply a part of RRC reconfiguration.  NOTE this is not related to IODT issue.
Study how to solve the issue
R2-2508098	Considerations on RRC Structure and (re)configuration	CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.2-a002`

### [6G/Rel-20 RAN2#132] `observation` 10.3.2.2 RRC Structure and (re)configuration.

```text
Storing RRC configurations even across state transitions and reusing them would reduce signalling overhead and thus saves power. This can allow faster state transitions, better power saving with more predictable latency benefitting both UE and network performance.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.2-o001`

### [6G/Rel-20 RAN2#132] `observation` 10.3.2.2 RRC Structure and (re)configuration.

```text
Signalling technique(s) (e.g., delta configuration) which avoid explicitly configuring all the UEs RRC parameters with each reconfiguration message should be part of 6GR RRC design.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.2-o002`

### [6G/Rel-20 RAN2#132] `observation` 10.3.2.2 RRC Structure and (re)configuration.

```text
Delta configuration applied to the UE’s current configuration may be inefficient when performing subsequent reconfigurations in succession and when performing significant changes in the UE configuration resulting from a change in service(s) or hardware profile.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.2-o003`

### [6G/Rel-20 RAN2#132] `observation` 10.3.2.2 RRC Structure and (re)configuration.

```text
Delta signalling applied to the UE’s current configuration may be error-prone and some network implementations may choose to prioritize full configuration instead.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.2-o004`

### [6G/Rel-20 RAN2#132] `observation` 10.3.2.2 RRC Structure and (re)configuration.

```text
Upon detecting the RRC reconfiguration failure, triggering the RRC connection reestablishment upon brings the significant negative impact.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.2-o005`

### [6G/Rel-20 RAN2#132] `observation` 10.3.2.2 RRC Structure and (re)configuration.

```text
Not all configuration errors will affect the current transmission.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.2-o006`

### [6G/Rel-20 RAN2#132] `observation` 10.3.2.2 RRC Structure and (re)configuration.

```text
Network cannot fully guarantee the correctness of configuration.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.2-o007`

### [6G/Rel-20 RAN2#132] `observation` 10.3.2.2 RRC Structure and (re)configuration.

```text
In NAS procedure and CHO candidate configuration procedure, if there is any error, UE does not need to break current connection and initiate RRC reestablishment procedure.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.2-o008`

### [6G/Rel-20 RAN2#132] `observation` 10.3.2.2 RRC Structure and (re)configuration.

```text
In 5G, if a UE cannot apply some (part) of the NW-provided configuration, while a majority of the configuration is good, generally the whole configuration is useless. When problematic configurations are encountered, or when reconfiguration failure occurs, currently the UE initiates connection re-establishment procedure.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.2-o009`

### [6G/Rel-20 RAN2#132] `observation` 10.3.2.2 RRC Structure and (re)configuration.

```text
We have observed a tangible portion of reconfigurations are such that the UE cannot apply the whole configuration, and such problems are more prevalent when the technology is just being deployed and not mature enough, especially in new markets where configurations take time to stabilize and the UE must implement targeted workarounds to enable such markets.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.2-o010`

### [6G/Rel-20 RAN2#132] `observation` 10.3.2.2 RRC Structure and (re)configuration.

```text
Neither dynamic capability updates nor UAI can effectively solve such issues, which results in unnecessary reestablishment procedures, service interruptions, and increased RLF statistics.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.2-o011`

### [6G/Rel-20 RAN2#132] `observation` 10.3.2.2 RRC Structure and (re)configuration.

```text
It is very important to have proper synchronization of the (re)configuration between the UE and the NW.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.2-o012`

### [6G/Rel-20 RAN2#132] `observation` 10.3.2.2 RRC Structure and (re)configuration.

```text
The overall probability of UE re-establishment in the field is approximately 2% to 3%, and re-establishment caused by the UE's failure to comply with partial reconfiguration messages account for only a small portion of the total re-establishment.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.2-o013`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.2 RRC Structure and (re)configuration.

```text
It is proposed to define functional modules in RRC configuration, organizing the protocol not in "layers" but in "functional modules",  such as "Mobility Management-Module" ,"Access Control-Module" ,“L2 Data Handling Module” , “Physical radio resource configuration-Module” and so on.
[2min]
Noted
R2-2508098	Considerations on RRC Structure and (re)configuration	CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.2-p001`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.2 RRC Structure and (re)configuration.

```text
To partition the ASN.1 content of RRC protocol as following:
-	Basic RRC modules: One general module + several common modules which have less/weak cross-coupling with other common modules, e.g. mobility, measurement;
-	Feature modules: Separate modules for specific features, e.g. NTN.
[2min]
Noted
Discussion
-	Xiaomi asks if the modules include both the mandatory and optional parameters.   CMCC is open to discuss if we can group further mandatory/optional configurations.
-	Huawei asks how we define the function.  CMCC explains for example, mobility, CA etc.
-	Oppo asks if this is a conceptual module or is it an ASN.1 module.  CMCC thinks it can be both.
-	Ericsson asks what we are trying to achieve, we should understand this first.   CMCC thinks it is to simplify the design.
-	Qualcomm asks how can this reduce the lower capability devices.
-	CATT thinks that ASN.1 can be partitioned between mandatory, optional, or general configuration.   We can also address Qualcomm concerns by grouping with features.
-	Interdigital thinks we should spend less time on how to modularize, and focus on what we want to achieve.   MEdiatek agrees to focus on what to achieve and we should be careful, for example if we modularize for NTN and then mobility for NTN has to be modified, then all mobility modules have to be updated.
-	Apple thinks the key part is how to address the common part.
-	ZTE thinks that we should go into the potential problems right away.
-	Nokia agrees too, people have different view what it means, and once we understand what we want to solve then discuss how each issue solves the problems.    We should got into level of details and show actual examples.
Study what we want to achieve, what are the main problems to address based on lessons learned from 5G
[POST132][017][6G] RRC structure – modular design (Nokia)
Intended outcome: Highlight the issues/problems we want to address/solve, and discuss how some of suggested proposals/definitions of modules solve the problems.  Examples must be provided.   This includes ASN.1 modularization
Discuss details of questions for email discussion on an offline during the meeting
Deadline:  Two phase: 1) identify issues and 2) suggested solutions/definitions of modules/examples
Long
R2-2508051	6GR RRC Structure and (re)configuration	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.2-p002`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.2 RRC Structure and (re)configuration.

```text
study the possible rules for module division, including:
	Rule1: feature dimension, i.e., one/several basic/common/mandatory modules + several additional optional modules. The additional optional modules may be vertical-specific/use-case-specific/device-type specific and can be discussed case by case.
	Rule2: dimension of pair of communication objects.
	Rule3: dimension of different WG. Further consider work group/protocol layer division, e.g., physical configuration as a separate module. FFS for PDCP/RLC/MAC. Discuss the possibility that physical configuration module is maintained by RAN1.
[2min]
Noted
R2-2508115	Discussion on 6G RRC ASN.1 Encoding	OPPO	discussion	Rel-20	FS_6G_Radio
Proposal 5	For 6G ASN.1 modularization, R2 study to which level the modularization is to be done, e.g., IE structure level, RRC message level, ASN.1 module level or specification level.
[2min]Noted
R2-2508080	Discussion on RRC (re)configuration and signalling design	Xiaomi	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.2-p003`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.2 RRC Structure and (re)configuration.

```text
Following principles are considered during 6G RRC modulization study:
	Principle 1: RRC configuration parameters needed for basic CP/UP communication functionalities need to be covered by the common module(s).
	Principle 2: RRC configuration parameters are not for basic CP/UP communication functionalities, e.g., optional features, can be put in the feature-/functionality-specific module(s).
	Principle 3: If the RRC parameters of a feature/functionality are not coupled and can work independently with those of another feature/functionality, they should be put in different feature-/functionality-specific modules.
[2min]
Delta Configuration – Improvements
R2-2508618	Discussion on RRC signaling design	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
Observation 5-1:	Delta configuration is still useful in 6G to reduce signalling overhead.
Observation 5-2:	The need code introducing additional restraints (e.g., Need S) and conditions are the main causes of implementation complexity and compatibility issues in delta configuration.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.2-p004`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.2 RRC Structure and (re)configuration.

```text
RAN2 to study the improvement of delta configuration to reduce ambiguities and implementation complexity — for example, decoupling the handling of optional signaling (e.g., Need codes) from the configuration guideline information (e.g., explanations for relevant configuration conditions).
[2min]
-	Ericsson agrees that the way we define it is not machine readable and it makes it impossible for the network.
-	Lenovo asks if we see this only for DL.   Huawei explains it is only DL and it is easier to have one common solution.   Ericsson agrees we should have one scheme but of course analyze for which config we apply delta signaling.
Noted
.
R2-2508112	RRC signalling and ASN.1 aspects	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
Observation 4	The ambiguity "Functionally mandatory UE configuration parameters can be absent in over-the-air RRC messages for initial configuration of a feature/functionality" is very common in 5G RRC signalling. Typically, an occurrence of this kind of ambiguity is a negative side-effect of the delta signalling mechanism.
-	ZTE thinks this issue is eventually solved in IODT so do we really want to address this with ASN.1.
Observation 5	The ambiguity "UE configuration parameters which shouldn't be modified after initial configuration of a feature/functionality can be sent in subsequent over-the-air RRC messages with new values" is relatively common in 5G RRC signalling. It is independent of the delta signalling mechanism, as UE reconfiguration for features/functionalities will anyway be required.
Proposal 3	6G RRC signalling for UE configuration is defined in a way that the ambiguity "Functionally mandatory UE configuration parameters can be absent in over-the-air RRC messages for initial configuration of a feature/functionality" is avoided.
Proposal 4	6G RRC signalling for UE reconfiguration is defined in a way that the ambiguity "UE configuration parameters which shouldn't be modified after initial configuration of a feature/functionality can be sent in subsequent over-the-air RRC messages with new values" is avoided.
Proposal 5	RAN2 to study the following ASN.1 method to make the delta signalling implementable and to avoid ambiguities in 6G RRC signalling for UE (re)configuration:
	Separate ASN.1 IEs are defined for initial configuration of a feature/functionality and subsequent reconfiguration of the feature/functionality;
	In the ASN.1 IE for initial configuration of the feature/functionality, functionally mandatory UE configuration parameters are carried by mandatory ASN.1 fields;
	In the ASN.1 IE for subsequent reconfiguration of the feature/functionality, ASN.1 fields do not exist for UE configuration parameters which shouldn't be modified after initial configuration of the feature/functionality.
[3min]
-	Xiaomi thinks that this increases the UE complexity.   Mediatek agrees it is true that with this the definitions will be a bit more complex, but that is acceptable as the ASN.1 will be more machine readable.
-	MEdiatek explains that we should push the definition more in the ASN.1
-	Ericsson agrees with the problem but not sure if we should define two IEs but we can look at further ways of solving.
-	Huawei doesn’t thinks this is related to delta signaling.   Ericsson doesn’t thinks it is related directly related but it’s more about constrains about what combination of parameters are allowed.
-	Oppo thinks that this is related to other issues related to ASN.1 encoding this problem will be minimized.
-	Jio agrees with the existence of the problem and there are a lot of errors that occur.
-	Xioami thinks that deep nesting is also an issue.   Huawei thinks this is more in the RRC structure discussion.
-	Apple would like network vendors to make some commitment of not changing some of the common configuration, and not have too much flexibility.    Ericsson thinks flexibility is desired but we have learned from the past and we should do better.   Nokia believes that network doesn’t do unnecessary reconfigure, but we should design something better.  RAN1 should give us more information on the paratemers, can it change, how often does it change or not.
-	Nokia thinks that we should give some practical guidance to RAN1.   Huawei agrees and in our spec we can give some clarification on whether parameters can be changed.   Samsung thinks that this would add additional work for each release.
-	CATT explains that the failure of RRC config is less than 2% and this type of issue comes from IODT.   Qualcomm asks if this is 2% of all RRC config
Noted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.2-p005`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.2 RRC Structure and (re)configuration.

```text
The 6G RRC configuration and signalling design should allow reusable stored configurations based on configuration modules.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.2-p006`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.2 RRC Structure and (re)configuration.

```text
Consider multiple stored configurations optimized for different use cases which can be activated in an on-demand manner by the network in designing 6G RRC.
[3min]
R2-2508386	RRC Structure and Reconfiguration for 6GR	InterDigital France R&D, SAS	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.2-p007`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.2 RRC Structure and (re)configuration.

```text
Support delta signalling relative to one of multiple reference configurations known by the UE and network.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.2-p008`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.2 RRC Structure and (re)configuration.

```text
Support reconfiguration by indicating (e.g., via a MAC CE or RRC message) one of several stored configurations or reference configurations.
[2min]
Reconfiguration Errors
R2-2508450	Views on RRC Structure and Configuration	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.2-p009`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.2 RRC Structure and (re)configuration.

```text
In RRC reconfiguration procedure, if UE is unable to comply with (part of) the configuration which does not affect the current transmission, UE is allowed to apply the good (part of) configuration and not initiating the connection re-establishment procedure.
[3min]
Noted
R2-2508758	Views on 6G RRC structure and (re)configuration	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.2-p010`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.2 RRC Structure and (re)configuration.

```text
6G design will allow the UE to keep/apply the good (part of) configuration in order to minimize the number of re-establishment procedures.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.2-p011`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.2 RRC Structure and (re)configuration.

```text
Study how to keep synchronization of (re)configurations between the UE and the NW while allowing the UE to keep/apply partial (re)configuration.
[3min]
Noted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.2-p012`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.2 RRC Structure and (re)configuration.

```text
RAN2 first studies the failure probability caused by the UE's inability to comply with the configuration, and then determining whether a partial success/failure mechanism is required.
[2min]
(Not treated) Other ASN.1 Improvements
R2-2508614	RRC ASN.1 structure for 6G	Ericsson	discussion	Rel-20	FS_6G_Radio
Observation 4	Continued non-critical extensions of large IEs tend to make it ambiguous which combination of parameters and values is valid.
Observation 6	NR’s delta signalling isn’t feasible for inter-node reconfigurations since the target node would need to support releasing features which it does not support itself.
Observation 9	In NR the dependencies between the common (IDLE) and dedicated (CONNECTED) mode configuration are partially ambiguous and tend to hinder UE specific configurations.
Proposal 2	6G’s ASN.1 configuration structure should accommodate for critical extensions of lower-level configuration IEs. Whether to extend critically or non-critically shall be decided on a case-by-case basis.
Proposal 4	By default, the connected mode configuration should be independent of the UE’s IDLE mode configuration obtained via MIB/SIB1. The network may configure the UE explicitly to acquire selected parameters from system information and to re-acquire it if system information changes.
[3min]
R2-2508649	Robust RRC Signaling Using Constraint ASN.1 Subtypes	TOYOTA ITC	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.2-p013`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.2 RRC Structure and (re)configuration.

```text
Introduce constraint subtypes in 6G signaling.
[3min]
R2-2508450	Views on RRC Structure and Configuration	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.2-p014`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.2 RRC Structure and (re)configuration.

```text
To reduce the difficulty of UE processing and network configuration provision, consider optimizing the RRC configuration structure to reflect the attributes and relationships of configuration parameters from two aspects:
•	Group the configurations with the same attributes together.
•	Place the parameters that need to be associated in the same structure or describe the relationship in the same way/location.
[3min]
Not treated
R2-2508139	Considerations on RRC (re)configuration structure	LG Electronics France	discussion	Rel-20	FS_6G_Radio
R2-2508175	Discussion on the modular design of RRC for 6GR	TCL	discussion
R2-2508227	Discussion on RRC structure and (re)configuration in 6G	Transsion Holdings	discussion	Rel-20
R2-2508406	Consideration on modular RRC and RRC signalling improvements	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
R2-2508414	RRC Signaling Framework with more close integration with the slices	Panasonic	discussion	Rel-20
R2-2508510	Discussion on RRC structure and reconfiguration	KT Corp.	discussion
R2-2508609	Reducing RRC signalling overhead	Fraunhofer IIS, Fraunhofer HHI	discussion
R2-2508623	Considerations on modular ASN.1 and RRC design for 6GR	Lenovo	discussion	Rel-20	FS_6G_Radio
R2-2508781	Discussion on Radio Protocol Architecture – Control Plane	Rakuten Mobile, Inc	discussion	Rel-20
R2-2508220	RRC structure and configuration	Sharp	discussion	Rel-20	FS_6G_Radio
R2-2508852	Discussion on RRC Structure and Configuration in 6G	ETRI	discussion	Rel-20	FS_6G_Radio
R2-2508874	RRC Restructuring and modular aspects for 6G	Samsung	discussion	Rel-20
R2-2508946	Discussion on RRC Structure and (re)configuration in 6G	Fujitsu	discussion	Rel-20
R2-2508972	Discussion on RRC Structure and (re)configuration	Google Inc.	discussion	Rel-20	FS_6G_Radio
R2-2509014	RRC configuration for flexible and adaptive UE behaviour	Qualcomm Incorporated, MediaTek Inc.	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.2-p015`

