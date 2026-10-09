# 6GR MAC 与调度

**当前进展** · 阶段：—

_尚无综述_

## 6GR 演进

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.3.1 Scheduling

```text
The legacy LCP procedure may not be sufficient in supporting more diverse traffic in 6G, due to increased presence of real time traffic such as XR and IC.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-o001`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.3.1 Scheduling

```text
New use cases and traffic characteristics in 6G call for more adaptive LCP.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-o002`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.3.1 Scheduling

```text
Existing LCP framework can achieve QoS adaptation by configuring dedicated DRB/LCH per QoS flow. However, it is not scalable and dynamic due to the limited number of DRBs/LCHs, configuration overhead, and semi-static priority, PBR and BSD.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-o003`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.3.1 Scheduling

```text
LCP procedure in 5G NR is performed among all the selected logical channels in the MAC entity, causing inflexibility to schedule the uplink grant for each traffic streams in XR service and mobile AI.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-o004`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.3.1 Scheduling

```text
In NR, refined buffer status granularity was intended for XR traffics. Therefore, quantization errors would still occur for large data volumes.
SR enhancements
R2-2603343	Scheduling Aspects for 6GR	Sharp	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-o005`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.3.1 Scheduling

```text
SR resources need to be used more efficiently in 6G, to provide low latency UL access to as many UEs as possible in a cell.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-o006`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.3.1 Scheduling

```text
The UE must wait for the expiration of the periodicBSRTimer to be triggered to send another BSR for the remaining UL data that could not be transmitted using the UL grant corresponding to the maximum reportable size of a Short BSR.　This leads to additional delay.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-o007`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

```text
Study new LCP designs that can support diverse traffic with distinct performance objectives (e.g. maximize throughput vs guarantee delay) in one unified procedure.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p001`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

```text
Study adaptive LCP designs that can better support 6G use cases, e.g. dynamic parameter adaptation, increased UE flexibility in channel selection and prioritization.
Noted
R2-2602948	Discussion on 6GR scheduling	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p002`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

```text
RAN2 to further study LCP enhancements considering various traffic characteristics, e.g., delay, importance, inter-QoS flow/packet dependency for 6GR.
Noted
Discussion
-	Qualcomm thinks that the NR design is not sufficient especially for real time.
-	Mediatek thinks that we should agree on what we want to identify.
-	Huawei thinks that the only scenario for LCP is dynamic QoS, what other requirements are there to justify the shortcomings.   Qualcomm thinks that the static priority is fine for MBB but not for the diverse type of data, and the dynamic priority in R19 was just a patch work so we can reconsider LCP in a more integrated.
-	Nokia would like to understand more what we are missing for LCP other than the already agreed dynamic priority.   Interdigital agrees with Qualcomm and we should make sure that LCP is designed well from the beginning.
Finer granularity LCP
R2-2604156	Views on UL scheduling	NTT DOCOMO INC..	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p003`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

```text
Study the framework for allocating UL resources to UL data that allow dynamic control at a finer granularity than the LCH level to enable QoS adaptation and to mitigate inter DRB HoL blocking.
-	Lenovo asks what is meant by finer granularity
Noted
R2-2603353	Consideration on Scheduling and uplink scheduling information in 6G	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p004`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

```text
Study UL grant enhancement with finer granularity, e.g., per-LCG UL grant, per-LCH UL grant.
-	Samsung asks if this requires putting the information in DCI and if so RAN1 needs to be involved.  LG confirms.
-	Apple asks what happens if there is no more data for that logical channel can something else go in it.
Noted
Moved from 9.3.1.3.2
R2-2603455	Configured grant and random access procedure	Ericsson, Bell Mobility	discussion
Proposal 3	To improve resource allocation in 6G, RAN2 together with RAN1, should study how to improve the granularity of the UL grants, e.g. per LCH indications.
Noted
Discussion
-	Mediatek asks if this removes the need for prioritized bit rates.  If so it simplifies UE behavior otherwise it just means more restrictions.
-	ZTE supports this direction in general but we have to be a bit careful about overhead in DCI signaling so one option is to do at LCG level.   We will need LCP with PBR as baseline, but this can help on top.
-	Lenovo thinks that this decision will impact quite a few things, as it will impact LCP, BSR, and have some concern on impact on DCI.  We can try to see if we can optimize the existing framework first before deciding such a thing.
-	Vivo would like to clarify the intention rather than the solution.    We can resolve how the UE uses the grant issue by doing LCP.
-	Huawei thikns that in 5G we can provide priority and based on that we can filter out the LCH with that priority.   ZTE thinks that we can go one level lower of granularity, LCH for example to ensure that you treat the LCH that has delay problems.
-	Xiaomi thinks that we need to ask RAN1 first.
-	Oppo and Samsung is fine to study this and the granularity should be aligned with granularity of reporting.
-	Qualcomm thinks that this proposal seems to provide more flexibility in scheduling, but this works only if the network has a more accurate buffer status and not sure we need to go into that granularity.   Maybe we can consider only a small group of logical channels that can do this type of scheduling and that would give enough flexibility.
-	Apple is not sure why the network needs this level of control, the UE is one that is most aware and has better knowledge on how LCP needs to be done to deliver the best user experience.
-	Interdigital thinks that this is a way for the scheduler to indicate to the UE to skip the normal multiplexing, but we can think more.
-	Nokia thinks that with current LCP the UE is already utilizing the grant the best way.  Wants to understand what the scenario is.   Ericsson thinks that even from 5G we knew that LCP was not sufficient.
-	CMCC thinks that this would allow some ability for the network guarantee the service for some LCHs.
Study LCP procedure and scheduling granularity to support the various types of 6G traffic.   Identify problem and scenario to solve.
Scheduling information
Reported Information
R2-2602948	Discussion on 6GR scheduling	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p005`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

```text
RAN2 to support data importance information reporting as part of scheduling information. FFS the granularity of the importance information.
R2-2603115	Uplink scheduling in 6G	Samsung	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p006`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

```text
RAN2 to consider using BSR to indicate the pending MAC CE(s) and their potential size in 6G.
R2-2603466	UP Scheduling aspects	Nokia	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p007`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

```text
At least separate PHR reporting from BSR/DSR is supported for 6G. The details on the PHR mechanism could be discussed later after the CA framework as well as the RAN1 requirement on MIMO become clearer.
Reporting granularity
R2-2603038	Discussion on scheduling	Xiaomi	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p008`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

```text
RAN2 to reuse the legacy per-LCG scheduling information reporting as the baseline.
R2-2603907	Discussion on MAC scheduling enhancements	1Finity	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p009`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

```text
RAN2 to study finer granularity of SR to enable direct UL resource allocation without separate BSR transmission.
R2-2603263	Views on 6G User Plane: Scheduling	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p010`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

```text
To reduce SR/BSR latency, RAN2 can consider using SR configuration ID to represent certain information related to the buffer status (e.g. buffer size, or presence of delay-critical data), such that network can timely allocate more appropriate UL resource even without BSR.
R2-2602940	Discussion on scheduling procedures	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p011`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

```text
Study methods to achieve more efficient use of SR resources, e.g. joint adaptation with PDCCH, dynamic de-/activation of SR resources, avoid resource partitioning, etc.
BSR/DSR triggers
R2-2603603	Further Discussion on Uplink Scheduling	Lenovo	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p012`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

```text
RAN2 to agree that for the triggering conditions for the unified uplink data status procedure in 6G, BSR and DSR triggering events specified for 5G NR are considered as a baseline.
R2-2603475	Scheduling, Scheduling Information Reporting and LCP	CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p013`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

```text
The unified scheduling information reporting can be event-triggered and periodical. The trigger events should at least consider data arrival, padding and remaining time.
R2-2604156	Views on UL scheduling	NTT DOCOMO INC..	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p014`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

```text
Study new triggering conditions to enable timely and accurate buffer information reporting in 6G.
CB-PUSCH
R2-2603263	Views on 6G User Plane: Scheduling	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p015`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

```text
RAN2 should confirm whether we aim to use CB-PUSCH for all general purposes, or only for BSR.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p016`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

```text
CB based PUSCH mechanism takes CG based transmission mechanism as the starting points, FFS on the further enhancement.
Noted
Moved from 9.3.1.3.2
R2-2603051	Framework for RACH and CB-PUSCH	ZTE Corporation, Sanechips, Samsung, China Telecom, Sony, ESA, DLR, Sateliot	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p017`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

```text
6G should avoid duplicate functionality between RACH and CB-PUSCH and minimize the specification work for CB-PUSCH by reusing RACH framework as the baseline for enabling CB-PUSCH
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p018`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

```text
For CB-PUSCH, in addition to the normal 2-step RACH mode (i.e. preamble + PUSCH), RAN2 should study whether the UE can transmit the MSGA payload part without the preamble when the UE has a valid TA
Noted
Discussion
-	Mediatek thinks that we should try to find the commonality and what is different.
After CB
-	Oppo indicates that RAN1 has made progress and companies should take these assumptions into account.   Ericsson indicates DMRS separation is supported in the evaluation and they will evaluate L1 transmission delay.
-	MEdiatek thinks that one think missing is what is the periodicity of the SR request.   Companies should indicate what they used.
-	Qualcomm thinks that we should have one common data point so we can calibrate and compare.
[POST134][018][6G UP] Simulation assumption (Mediatek)
Intended outcome: Align on any new/other remaining possible assumptions and try to converge on at least one set of parameters that everyone should try to evaluate and then allow other ranges for companies, taking RAN1 information into account.
Deadline:  2 weeks
=> Noted in R2-2604388 (Simulation assumptions in this document are agreed).
R2-2604394	CB-PUSCH progress	OPPO	discussion	Rel-20	FS_6G_Radio
Withdrawn
R2-2603050	Scheduling enhancements	ZTE Corporation, Sanechips	discussion
R2-2603090	Discussion on scheduling in 6G	Transsion Holdings	discussion	Rel-20
R2-2603164	Latency reduction techniques for 6G	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
R2-2603254	On the support for CB-PUSCH	Google	discussion	Rel-20	FS_6G_Radio
R2-2603305	6G CB-PUSCH and Scheduling information reporting	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2603329	Discussion on scheduling	China Telecom	discussion	Rel-20	FS_6G_Radio
R2-2603418	L2 scheduling framework for 6GR	InterDigital, Inc.	discussion	Rel-20	FS_6G_Radio
R2-2603454	System simulation for contention based BSR	Ericsson, T-Mobile USA, OPPO, Kyocera, WILUS Inc., LG Electronics Inc.,Turkcell, Sharp	discussion
R2-2603484	6G scheduling	NEC	discussion	Rel-20	FS_6G_Radio
R2-2603746	Latency-aware contention-based UL access and load-aware grant expectation for CB-PUSCH	Jio Platforms	discussion	Rel-20	FS_6G_Radio
R2-2603747	Predictive CB-CG resource control and latency-aware retransmission gating	Jio Platforms	discussion	Rel-20	FS_6G_Radio
R2-2603856	Consideration on 6GR Scheduling	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2604021	Contention-based BSR reporting	MediaTek Inc.	discussion	Rel-20
R2-2604120	Discussion on UL scheduling in 6G	III	discussion	Rel-20	FS_6G_Radio	R2-2601700
R2-2604162	Discussion on L2 Scheduling for 6G AI-driven Services	III, National Taiwan University	discussion	Rel-20	FS_6G_Radio
R2-2604169	MAC handling assumptions for uplink scheduling information	Rakuten Mobile, Inc	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p019`

### [6G/Rel-20 RAN2#134] `agreement` 9.3.1.3.2 Other MAC functionalities

```text
1	Support 2-step RA and 4-step RA.   Find commonalities in MAC with the aim to unify (if possible) but the design should ensure that 4 step RA can work without the need for 2-step RA
2	Indicate to RAN1 our decision to support 2-step and 4-step and take into account.  Explain that RAN2 discussed whether it is possible to do 2-step and 4-step without RACH partitioning and ask whether it is possible.
3	Study RACH designs that enable more efficient use of resources for RA load management and energy saving purposes
[AT134][010][6G UP] Random Access (Huawei)
Intended outcome: Discuss RA procedure steps for 2 and 4 step (try to understand commonalities for unified procedure) and identify any possible questions to RAN1 that we can already send and any/whether any email discussions over the summer would be helpful.
Deadline:  Thursday
R2-2604396	Summary of [AT134][010][6G UP] Random Access (Huawei)	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-a001`

### [6G/Rel-20 RAN2#134] `agreement` 9.3.1.3.2 Other MAC functionalities

```text
RA procedure for 2-step and 4-step RA
1	Take the following procedure for 2-step RA and 4-step RA as the baseline for the discussion in 6G from RAN2 point of view
4-step CBRA: Where the UE transmits the RACH preamble and waits for the network response (i.e. RAR) which schedules transmission of MSG3 in the UL
2-step CBRA: Where UE transmits RACH preamble along with the PUSCH and waits for the network response which provides RACH response as well as contention resolution
4-step CFRA: Where UE transmits dedicated RACH preamble assigned by the gNB and terminates the RA procedure upon reception of NW response
2-step CFRA: Where UE transmits dedicated RACH preamble assigned by the gNB and its corresponding PUSCH resource and terminates the RA procedure upon reception of NW response.
2	Support fallback from 2-step RA to 4-step RA to msg3 transmission when the network decodes the preamble but not the msgA-PUSCH payload. FFS RACH type switching
Unification of 2-step and 4-step RA
3	Aim to have the same length of the two windows when both 2-step and 4-step RA are configured, i.e., same as 4-step RA. FFS the start of the window for the unification.   FFS other aspects of unification after some further progress on basic procedure (e.g. format,etc).
LS to RAN1
4	Send an LS to RAN1 about the agreements above and indicate:
(a) the agreement that both 2-step and 4-step RA are supported from RAN2 point of view in 6G;
(b) asking whether it is possible to support 2-step and 4-step RA without RACH partitioning;
(c) asking about the correspondence between preamble and PUSCH in 2-step RA
[POST134][017][6G UP]  RACH (Huawei)
Intended outcome:
(a) LS to RAN1; and
(b) discuss the FFSs for 2-step and 4-step RA procedure (not dependent on RAN1 progress) keeping in mind potential unification for cases.   Understand details of possible agreed RA enhancement.
Deadline:
LS to RAN1 (one week)
The remaining discussion (long)
R2-2604385	LS on Random Access in 6G	RAN2	LS out	Rel-20	FS_6G_Radio	To:RAN1
=> Approved
Scope of the post email discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-a002`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.3.2 Other MAC functionalities

```text
In NR, RACH resources do not adapt well to short-term variations in access load, often resulting in high level of contention and access failures.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-o001`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.3.2 Other MAC functionalities

```text
Allowing segmentation for CCCH channel can enable the following:
o	Make the MSG3 payload size flexible without compromising the coverage whilst avoiding the need for preamble partitioning for MSG3/MSGA payload size indication
o	Enable more features that can wait till MSG3 (e.g. early UE type, slice indication etc) to use MSG3 based indication instead of MSG1 based indication.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-o002`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.3.2 Other MAC functionalities

```text
CCCH segmentation requires multiple-round Msg2 reception and segment transmission, which introduces complexity on UE implementation as well as additional delay for contention resolution.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-o003`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.3.2 Other MAC functionalities

```text
CCCH segmentation requires additional indication in Msg3 to indicate if there is more segment or not and/or the sequence number of each segment.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-o004`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.3.2 Other MAC functionalities

```text
If CG is to be used for bursty traffic, to improve radio efficiency, UTO-UCI and early report can be utilized.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-o005`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
The RACH framework in 6G should support:
-	4-step RA: Where the UE transmits the RACH preamble and waits for the network response (i.e. RAR) which schedules transmission of MSG3 in the UL
-	2-step RA: Where the UE transmits RACH preamble along with the associated PUSCH transmission and waits for the network response which provides RACH response as well as contention resolution
-	Fallback from 2-step RA to 4-step RA: when the network decodes the preamble but not the RACH payload
-	Qualcomm thinks that it should be failure indication to decode the payload instead of fallback
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p001`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
RAR format for RACH should support indication of TA, backoff, contention resolution, UL grant (for 4-step RA) and should enable fallback from 2-step to 4-step RA. Final design of RAR format can be left for stage-3.
Noted
R2-2603112	Discussion on RACH and configured grant	OPPO	discussion	Rel-20	FS_6G_Radio
Proposal 1	For 6G RACH, RAN2 to study a unified RACH framework including:
	A common RACH pool (i.e. for Msg1) including PRACH and/or PUSCH is configured to support different UL transmission types.
	The UE selects the resources (i.e. preamble, or preamble and payload, or payload) for Msg1 based on NW indication and/or preconfigured conditions.
	A unified RAR is design to respond the UEs performing different UL transmissions.
-	ZTE asks how can we avoid partitioning.    Oppo thinks we don’t need to differentiate.  Huawei thinks that we need to think about aNB as we would have to do blind decoding and for 4step we don’t need to as it is just a preamble.   Oppo thinks that the network can detect whether there was a preamble or a preamble and PUSCH.      ZTE thinks that this was discussed in RAN1 so we would need to ask input.
-	Interdigital thinks that we made the decisions because of legacy as well but we should study if there is a way with RAN1 input.   Nokia also thinks RAN1 needs to discuss.
Noted
Discussion
-	Ericsson thinks we should have 2-step RA only for the scenarios needed, like NTN.  ZTE thinks that the 2-step RA is useful for other cases and not just for synchronous.
-	Qualcomm thinks that the UE should have the option to implement it or not and the design should be done in a way that it doesn’t implement features it doesn’t supports.    Huawei has the same view.
-	Nokia thinks 4-step as a baseline.
-	ZTE thinks that we should wish for having the same window.  Interdigital thinks that the window length requirements come from RAN2.
R2-2602949	Considerations on 6GR Random Access and Configured Grant	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p002`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
In 6GR, taking the NR 4-step RA procedure as baseline, the 4-step RA procedure includes the following steps:
1) RACH request;
2) RACH response;
3) Msg3 payload;
4) Contention resolution.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p003`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
In 6GR, taking the NR 2-step RA procedure as baseline, the 2-step RA procedure includes the following steps:
1) RACH request and MsgA payload;
2) RACH response and Contention resolution.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p004`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
For the commonization of 4-step and 2-step RA, at least the following aspects are considered:
1) Common RA configuration parameter structure;
2) Common contention resolution determination, recovery mechanism, as well as a unified MAC PDU format;
3) Common backoff mechanism, power ramping accumulation and reset, and maximum access attempt.
RACH Resource Adaptation
R2-2602941	Discussion on other MAC functionalities	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p005`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
Study RACH designs that enable more efficient use of resources, e.g. dynamic or on-demand allocation of RACH resources, beam-specific RACH configurations, etc.
Noted
R2-2603455	Configured grant and random access procedure	Ericsson, Bell Mobility	discussion
Proposal 6	Study how to design a configuration framework for ROs such that it would be possible to bundle with sleeping opportunities in between.
Noted
R2-2603913	Discussion on other MAC functionalities	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
Proposal 1	Study methods to mitigate RA overload situation, e.g.,:
-	Dynamic indication to switch the Random Access resource set,
-	Adaptation of PRACH and MsgA PUSCH resources
Noted
R2-2603016	Random Access in 6G	Samsung	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p006`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
For efficient utilization of resources configured by multiple random access resource sets, when the UE initiates random access procedure, UE can first indicate the random access resource set UE is going to use and then perform random access procedure using the selected random access resource set.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p007`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
Dynamic switch between a set of sparsely configured random access occasions and a set of densely configured random access occasions during the random access procedure is supported in 6G.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p008`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
When the network enters network energy saving mode, only one of the multiple RACH configurations is considered active for the random access procedure initiated during the network energy saving mode.
Noted
-	Mediatek thinks that we need to be careful when designing this especially for idle mode, like dynamic handshaking between NW and UE.   Xiaomi thiks we should avoid RACH partitioning.
-	Apple thinks we need to be very careful for idle mode as it will be something supported and mandatory from day 1.
-	ZTE thinks we should discuss here for energy saving and we don’t need handshake for idle mode.   Ericsson explains that there is no intention to switch things dynamically and there are ways of providing things
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p009`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
-	Ericsson ask whether to transmit preamble when transmit preamble when UE has TA for 2 step RA is still in scope.  Companies confirm that it can be discussed when we discuss 2step procedures.  ZTE thinks that we should include the question to RAN1.   Huawei thinks that we first discuss under what scenario we should not transmit preamble but only PUSCH, the question is not clear.    Lenovo agrees haven’t really discussed this as it would change gNB behavior.   Interdigital asks what is the benefit of just transmitting PUSCH, transmitting the preamble may be beneficial for fallback and it is more reliable.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p010`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
Scope of the email disc: (a) LS to RAN1; and (b) discuss on the new issues and the FFSs for 2-step and 4-step RA procedure and potential unification of the two procedures.
CCCH segmentation
Moved from 9.3.1.1
R2-2603049	Functionality for upper user plane	ZTE Corporation, Sanechips	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p011`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
Study solutions to enable larger UL CCCH message size without impacting coverage, by supporting segmentation for UL CCCH channel
Noted
R2-2604066	Views on Random Access and Configured grants	1Finity	discussion	Rel-20
Observation#3: GroupA/GroupB preamble partitioning can be avoided if the CCCH payload in MSG3 can be transmitted in parts (i.e. segmented). For SDT the small data payload in MSG3 it can be transmitted in parts so Group/GroupB preamble partitioning can be avoided.
Observation#8: UL CCCH SDU included in MSG3 if segmented, then the excessive need for preamble partitioning can be avoided and early indications can be included in MSG3 segments.
Proposal#3: RAN2 to study the feasibility of UL CCCH message segmentation as it not only avoids excessive need for preamble partitioning but also provides flexibility in conveying multiple early indications as part of initial access procedure.
Noted
R2-2603039	Discussion on other MAC functionalities	Xiaomi	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p012`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
To support flexible Msg3/MsgA size (e.g., 56bits and 72bits), preamble partition as in NR is used instead of CCCH segmentation.
Noted
Discussion
-	Nokia doesn’t support the segmentation as it complicated everything, but if we want to increase the size we can discuss with RAN1.   Oppo agrees with Nokia and then we need to consider retransmission.  Huawei has same view and there is no requirement for larger CCCH.
Will not discuss this until we understand the CCCH size requirement much later in the 6G work
Configured Grants
Adjustment of resource allocation
R2-2603455	Configured grant and random access procedure	Ericsson, Bell Mobility	discussion
Proposal 1	Support unified CG framework with dynamic activation/deactivation/adjustment using DCI and immediate activation using RRC.
Noted
R2-2603620	Other MAC functionalities: CG and Random-access	Sony	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p013`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
From RAN2 perspective, support a single CG resource that can adapt/adjust parameters (e.g. MCS, TBS) for data variability, channel variability and data reliability, and can handle different traffic types/services.
-	Mediatek asks if this would be done with DCI.
-	Panasonic asks if it is per UE or per BWP.
Noted
Discussion
-	ZTE thinks we can agrees there will be some RRC configuration and some DCI and what we put there we can leave it to stage 3.   Ericsson thinks that we can agree for same CG configuration we support both RRC signaling and DCI signaling.
-	Vivo thinks we should wait for RAN1 response.
-	Ericsson thinks that we don’t know if we need multiple CG configurations.   Huawei thinks that we have a very good motivation to have it as we support diverse and immersive communication since the beginning.   Apple thinks that we have diverse traffic types and we agreed we need to support.
-	Mediatek doesn’t see a motivation to use multiple configured.   Qualcomm also thinks this is needed and it brings a lot of benefits without much additional cost.    Also 6G design should support bursty traffic, and we should support something similar to multi-PUSCH.     Lenovo agrees with QC, it was introduced in Rel-18.
-	Samsung thinks we should be careful to ensure that low cost devices don’t need to support DCI.
-	ZTE and Interdigital thinks that the MAC needs to work for cases where there are multiple.
Agreements on CG
1	UE can be configured with one or multiple CG configurations.  For each configuration we can allow RRC and/or DCI signaling at least for activation/deactivation.   Understanding is that more than one CG can be active at a time, but the UE transmits only on one at time per cell. Further details can be discussed in stage 3.
Higher resource efficiency
R2-2603464	Other MAC functionalities	Nokia	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p014`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
RAN2 to study ways for UE to indicate used/unused CG PUSCH resources for the purpose of increased spectral efficiency. UTO-UCI in the same format as 5G NR is not needed in 6G.
Noted
R2-2602949	Considerations on 6GR Random Access and Configured Grant	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p015`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
For the sake of higher resource efficiency, RAN2 to study UE initiating the advance indication to inform aNB about the upcoming CG utilization.
Noted
R2-2603039	Discussion on other MAC functionalities	Xiaomi	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p016`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
6G CG supports NR UTO-UCI (unused transmission occasion) to improve resource efficiency as a baseline.
Noted
Discussion
-	QC thinks that this is not a useful feature and understand the desire to improve the efficiency but they can observe the utilization and dynamically adapt the CG to make it.  Lenovo has same view as Qualcomm and we are discussing predictive reporting which is similar in terms of what it is trying to achieve.  Interdigital has the same view and also the UE has no incentive to do it.   Mediatek would like to minimize the time we spend on WI and focus on things that really matter.  Apple has same understanding, even the UE sends it not sure the network can use it.  If we want to improve resource efficiency we allow the UE to use the resource for something else like retransmission.
-	Fraunhoufer thinks that we can at least capture the intention of recovering unused resources.
-	Xiaomi thinks we can provide the information and details are FFS
-	ZTE also thinks it is useful but we can wait for RAN1.
-	Huawei thinks that the proponents can propose this in RAN1.
-	Oppo thinks that there may be some benefitis but the current UTO-UCI is not very useful as it is.
-	Samsung also thinks that the CG resource efficiency should be good.
-	Ericsson does’nt think that the reporting is useful at all, by the time the NW gets it, it doesn’t have enough time to re-cycle the resource.  The predictive reporting we are doing in RAN2 should be enough to help the network.
-	Vivo thinks we should report before the CG is used.
-	CMCC thinks that we can notify whether the resource will be used.
-	Docomo agrees that there is no incentive but from network perspective it can be useful.
No contributions expected on these aspects in RAN2
LS to RAN1
R2-2603419	Other MAC functionality	InterDigital, Inc.	discussion	Rel-20	FS_6G_Radio
Send an LS to RAN1 to inform them about the following agreements and ask them to study L1 scheduling to support them:
-	Support at least the following scheduling schemes: dynamic grant and configured grant.
-	study CG like mechanisms to address different types of traffic, including voice, bursty traffic, other periodic traffic etc.
-	Study 6G CG, which can support at least the following from RAN2 perspective:
o	CG resource immediately activated (e.g. for delay critical service) after configuration;
o	Dynamic activation/deactivation;
o	Dynamic adjustment of resource allocation (e.g. MCS, TBS and start time);
o	Higher resource efficiency
-	Add SPS
-	Add new agreements from this meeting
Action: take the RAN2 agreement into account for the L1 design
Noted
[AT134][11][6G UP] CG LS to RAN1  (Interdigital)
-	Intended outcome: Agree to LS to RAN1
-	Deadline:  Friday
R2-2604210	LS on 6G Grant Types	RAN2	LS out	Rel-20	FS_6G_Radio	To:RAN1
The LS is approved in R2-2604399
R2-2602988	Discussion on RACH and CG	NEC	discussion	Rel-21	FS_6G_Radio
R2-2603012	Discussion on MAC functionalities in 6G	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
R2-2603021	MAC processing for high data rates	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
R2-2603154	6GR MAC Functionalities	Sharp	discussion	Rel-20	FS_6G_Radio
R2-2603264	Views on 6G User Plane: Miscellaneous MAC Mechanisms	Apple	discussion	Rel-20	FS_6G_Radio
R2-2603306	6G Random Access and Configured Grant	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2603349	On random access procedure aspects	NTT DOCOMO	discussion	Rel-20	FS_6G_Radio
R2-2603476	Random Access and Configured Grant	CATT	discussion	Rel-20	FS_6G_Radio
R2-2603551	Discussion on other MAC functions	Philips International B.V.	discussion	Rel-20	FS_6G_Radio
R2-2603570	Discussion of other MAC functionalities	Lenovo	discussion	Rel-20
R2-2603857	Consideration on 6GR Random Access and CG	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2603886	Discussion on MAC functionalities in 6G	Spreadtrum, UNISOC	discussion	Rel-20
R2-2603976	Discussion on Random Access procedure	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2603977	Discussion on Configured Grant	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2604003	Discussion on 6G configured uplink grant	ASUSTeK	discussion	Rel-20
R2-2604031	Further discussion on unified RACH procedure	Google Korea LLC	discussion	FS_6G_Radio
R2-2604066	Views on Random Access and Configured grants	1Finity	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p017`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.1 Scheduling

```text
The KPI for resource efficiency at least includes UL PRB utilization.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.1-p001`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.1 Scheduling

```text
The KPIs for latency include data burst latency and/or BSR latency.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.1-p002`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.1 Scheduling

```text
Collision ratio should be considered in the evaluation.
Scenario
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.1-p003`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.1 Scheduling

```text
The TN scenario is considered as the starting point for evaluation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.1-p004`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.1 Scheduling

```text
No restriction on the traffic models (e.g. FTP3, XR and bursty eMBB) for the evaluation.
CB-PUSCH assumption
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.1-p005`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.1 Scheduling

```text
To compared with the legacy SR-BSR, the evaluation for the CB-PUSCH starts from the use case that CB-PUSCH is used for the transmission of BSR.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.1-p006`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.1 Scheduling

```text
RAN2 considers that the blind decoding complexity (e.g. DMRS and scrambling sequence) for the shared resource at the aNB should be analyzed by RAN1.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.1-p007`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.1 Scheduling

```text
For the RAN2 evaluation purpose for CB PUSCH of BSR, the followings are assumed for the CB PUSCH configuration:
1) Either dedicated or shared DMRS can be used.
2) Either C-RNTI or common RNTI can be used.
3) The typical Msg3 configuration (i.e. 1 or 2 PRBs and QPSK) is used
4) No restriction on how beam information (i.e. no beam or NW-indicated or UE-selected) is used for CB-PUSCH.
5) UE ID (e.g. C-RNTI MAC CE) is included in CB-PUSCH payload.
6) If a positive NW response is received within a timer after CB-UL transmission, the contention resolution is considered as successful.
7) The UE re-attempts CB-UL transmission when contention resolution fails.
8) HARQ retransmission is not used, i.e. the UE uses HARQ new transmission after contention resolution failure.
Question for RAN1
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.1-p008`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.1 Scheduling

```text
Provide the following question to RAN1:
Regarding how to multiplex the PUSCHs from multiple UEs on the same time-frequency resources:
o	Whether to use UE-dedicated or shared DMRS
o	Whether to use UE-dedicated RNTI or common RNTI
Other evaluation assumption
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.1-p009`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.1 Scheduling

```text
False positive SR is not mandated in the RAN2 evaluation.
Noted
R2-2602024	System simulation for contention based BSR	Ericsson, LG Electronics Inc, OPPO, T-Mobile USA, Turkcell, Kyocera, Verizon, Sharp, WILUS Inc.	discussion
Observation 1	There is a need for a low complexity and scalable solution where several hundreds of connected UEs are enabled to request fine grained UL resources every slot.
Observation 4	A pure DMRS based solution is not scalable and introduce high complexity that increases with number of UEs.
Observation 6	Randomization of DMRS selection at each CB attempt results in a better contention resolution
Observation 7	Limiting the number of DMRS and including the UE identity in the payload keeps the number of blind-decoding attempts to minimum
Observation 8	The number of transmissions per CB occasion—and consequently the collision rate—remains low because usage is limited to BSRs and only when no dedicated ULSCH resources are available.
Proposal 2	RAN2 to discuss the evaluation results of various scheduling solutions including CB BSR and the SR/BSR functionality and capture them in the TR.
R2-2602801	Report of [AT133bis][006][6G UP] CB-BSR assumption (Oppo)	OPPO	discussion	Rel-20	FS_6G_Radio
=> Revised in R2-2602810
R2-2602810	Report of [AT133bis][006][6G UP] CB-BSR assumption (Oppo)	OPPO	discussion	Rel-20	FS_6G_Radio
Discussion
-	Samsung doesn’t think that we need to ask RAN1, they are studying it anyways.
-	Vivo thinks that we anyways we have our assumptions, why are we asking.  Oppo explains that is are just RAN2 initial assumptions.
-	Nokia doesn’t understand why we are discussing this again after so many discussion.
-	Huawei thinks that it is clear that if things are not separated then it is CB-PUSCH, so dedicated DMRS is not CB-PUSCH.   ZTE thinks that the main point is what happens where there is a collision.  So when time frequency resources collide can the network differentiate using scrambling code or DMRS.  RAN1 can say that even if the DMRS are different there will still be problem.
-	Ericsson thinks that reduction of aNB blind decoding complexity would be beneficial.   Qualcomm doesn’t think it is an worry if you have small number of UEs.
Noted
| Agreements on assumptions for evaluation as the starting point in RAN2: KPI For resource efficiency evaluation: UL PRB utilization (e.g. resource efficiency as defined in TR 36.881). For latency evaluation: data burst latency or/and successful-BSR latency. Collision ratio for CB based schemes Scenario TN Bursty traffic (e.g. FTP3). Transport layer protocol (e.g. TCP) can be considered. CB-PUSCH assumption CB PUSCH resources are shared by multiple UEs for the BSR transmission Blind decoding complexity (e.g. DMRS and scrambling sequence) and DMRS miss detection probability for the shared resource at the aNB can be decided by RAN1 CB PUSCH procedure: a. Either dedicated or shared DMRS can be used. b. Either C-RNTI or common RNTI can be used. c. The typical Msg3 configuration (i.e. 1 or 2 PRBs and QPSK) is used d. No restriction on how beam information (i.e. no beam or NW-indicated or UE-selected) is used for CB-PUSCH. e. UE ID (e.g. C-RNTI MAC CE) may be included in CB-PUSCH payload in the shared DMRS case. f. If a positive NW response is received within a timer after CB-UL transmission, the contention resolution is considered as successful. g. The UE re-attempts CB-UL transmission when contention resolution fails. h. HARQ retransmission is not used, i.e. the UE uses HARQ new transmission after contention resolution failure. i. A collision occurs when more than one UEs choose the same time/frequency resource and the same DMRS sequence, and all colliding PUSCHs will fail when collision occurs. Send agreements on simulation assumptions to RAN1 as a reference Ask RAN1 for following: 1 When there is a collision in time and frequency resource, is there a way for the network to differentiate the UE and decode the payload. RAN2 discussed for evaluation purposes, DMRS, scrambling code, UE ID, but would like to ask RAN1 their view and to understand probability of differentiating the UE and decoding. 2 Kindly provide any feedback |
| --- |
R2-2602808	[Draft] LS on uplink scheduling enhancements	OPPO	LS out	Rel-20	FS_6G_Radio	To:RAN1
[POST133bis][006][6G UP] CB-BSR assumption (Oppo)
Intended outcome:  Agree to LS to RAN1
Deadline:  Wednesday, April 22nd
=> Approved in R2-2602815.
R2-2602815	LS on evaluation assumptions for contention based PUSCH transmission	RAN2	LS out	Rel-20	FS_6G_Radio	To:RAN1
=> Approved
Not treated
Finer L2 scheduling – if time allows, dependent on QoS progress-
R2-2601856	6G CB-PUSCH and scheduling information reporting	Ofinno	discussion
Proposal 4	RAN2 to study finer granularity for scheduling information reporting in 6G compared to the LCG-level granularity in 5G.
R2-2601501	Discussion on scheduling	Xiaomi	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.1-p010`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.1 Scheduling

```text
RAN2 to reuse the legacy per-LCG scheduling information reporting as the baseline.
R2-2601660	Uplink scheduling in 6G	Samsung	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.1-p011`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.1 Scheduling

```text
RAN2 to consider using BSR to indicate the pending MAC CE(s) and their potential size in 6G.
R2-2601804	Consideration on Scheduling and uplink scheduling information in 6G	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.1-p012`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.1 Scheduling

```text
Study UL grant enhancement with finer granularity, e.g., per-LCG UL grant, per-LCH UL grant.
R2-2601972	Discussion on 6G scheduling	China Telecom	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.1-p013`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.1 Scheduling

```text
RAN2 to study the new LCP design that supports dynamic adjustment of LCP parameters.
R2-2601465	Discussion on scheduling procedures	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.1-p014`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.1 Scheduling

```text
Study new LCP designs that
-	can support multiple performance objectives (e.g. throughput vs delay) in a cohesive way;
-	are more adaptive than NR in supporting new use cases such as application context awareness and dynamic QoS.
R2-2601446	Discussion on 6GR scheduling	vivo	discussion	Rel-20
R2-2601559	Discussion on scheduling information reporting	OPPO	discussion	Rel-20	FS_6G_Radio
R2-2601662	Scheduling Aspects for 6GR	SHARP Corporation	discussion
R2-2601700	Discussion on UL scheduling in 6G	III	discussion	Rel-20	FS_6G_Radio	R2-2601049
R2-2601717	UP Scheduling aspects	Nokia	discussion	FS_6G_Radio
R2-2601721	Discussion on Unified Scheduling Information Reporting	Pengcheng Laboratory	discussion
R2-2601777	Scheduling enhancements	ZTE Corporation, Sanechips	discussion
R2-2601831	Views on 6G User Plane: Scheduling	Apple	discussion	Rel-20	FS_6G_Radio
R2-2601851	6G scheduling	NEC	discussion	Rel-20	FS_6G_Radio
R2-2601908	Scheduling and Scheduling Information Reporting	CATT	discussion	Rel-20	FS_6G_Radio
R2-2601937	Discussion on Contention based UL resource	ASUSTeK	discussion	Rel-20
R2-2601953	On Dynamic QoS Requirements and L2 Scheduling Enhancements for AI-driven Services in 6G RAN	III, National Taiwan University	discussion	Rel-20
R2-2601988	Discussion on MAC scheduling enhancements	1Finity	discussion	Rel-20	FS_6G_Radio
R2-2601993	L2 scheduling framework for 6GR	InterDigital	discussion	Rel-20	FS_6G_Radio
R2-2602044	Further Discussion on Uplink Scheduling	Lenovo	discussion	Rel-20	FS_6G_Radio
R2-2602050	Discussion on scheduling in 6G	Transsion Holdings	discussion	Rel-20
R2-2602053	Latency reduction techniques for 6G	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20
R2-2602070	Discussion on Scheduling	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2602235	Discussion on scheduling enhancements for 6G	Panasonic	discussion	Rel-20
R2-2602276	Discussion on Scheduling enhancements	AUMOVIO	discussion
R2-2602397	Efficiently handling small UL packets	Fraunhofer IIS,  Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
R2-2602413	Considerations on scheduling for 6GR UP	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2602511	Further discussions on scheduling	Futurewei	discussion	Rel-20	FS_6G_Radio
R2-2602577	Contention-based BSR reporting	MediaTek Inc.	discussion	Rel-20
R2-2602607	Views on BSR trigger	NTT DOCOMO INC..	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.1-p015`

### [6G/Rel-20 RAN2#133bis] `agreement` 9.3.1.3.2 Other MAC functionalities

```text
From RAN2 point of view, at least the following principles are used:
1	The Msg1 indication is only applied to use cases which affect msg1 transmission/RAR/Msg3 scheduling and/or related procedures.
2	The Msg3 early indication is only applied to use cases which affect Msg4 scheduling and/or related procedures.
FFS what cases need msg1 indication after further progress on RAN1/RAN2 design
R2-2601502	Discussion on other MAC functionalities	Xiaomi	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-a001`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

```text
The RA design needs to consider basic NR RA-triggering events (e.g., connection management, UL synchronization, resource request, cell switch, system information request, BFR).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o001`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

```text
2-step RA offers benefits in fast access and UE energy efficiency, while 4-step RA provides wider coverage and higher reliability.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o002`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

```text
CBRA supports massive access with high efficiency, while CFRA avoids collisions for latency-sensitive and high-reliability scenarios.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o003`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

```text
MsgA/Msg3 in random access can carry initial RRC signaling and uplink data.
Proposal 1：Study RACH procedure considering at least the following aspects:
Various RACH triggering events from 6G Day 1
Both 2-step RACH and 4-step RACH
Both CBRA and CFRA
Carrying both RRC signaling and uplink data via MsgA/Msg3
Noted
R2-2601624	Discussion on other MAC  functionalities	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o004`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

```text
In NR, separate DL responses are defined for 4-step RACH (RAR) and 2-step RACH (MsgB). Although RAR and MsgB (e.g., fallbackRAR in MsgB) share similarities, they must be separately scheduled using different RNTIs. This ensures UE differentiation between the two RACH types but at a cost of reduced multiplexing flexibility and increased consumption of RNTI spaces.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o005`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

```text
In NR, the UE performs RACH fallback only after a configured number of failed attempts and strictly follows a predefined order. The mechanism disregards dynamic change of radio link quality at UE side, which may increase fallback latency and prevents the UE from selecting more suitable RACH resources.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o006`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

```text
In NR RACH, the UL carrier and BWP are selected during RACH initialization and remain unchanged thereafter, which cannot adapt to dynamic intra-cell load variations.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o007`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

```text
By enabling flexible transmission of the preamble, MSG3/MSGA payload parts, 6G can support 4-step RACH, 2-step RACH and CB-PUSCH using a unified framework for all these features
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o008`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

```text
In NR, RACH partitioning for RedCap, eRedCap, SDT, and network slicing does not impose requirements on a fundamentally different RA response message or Msg3 format. Therefore, dedicated RACH partitioning for these features is not an absolute requirement in 6G, provided that the network can identify the UE's feature through alternative mechanisms at or prior to the random access procedure.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o009`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

```text
Early identification at PRACH detection is required only for features with fundamental differences in response handling (e.g., OD-SIB1), where lack of such indication leads to incorrect monitoring or response procedures. For other features (e.g., SBFD, IAB-MT, preamble Group A/B, OD-SIs), separate RACH resource partitioning is not strictly required as the procedures remain functionally compatible with a common configuration, with any additional mechanisms providing optimization rather than necessity.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o010`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

```text
Among all these features supported by NR, some are necessary to be indicated via Msg1, some can wait for Msg3 and some require RAN1 discussion.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o011`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

```text
In NR, support of feature/feature combinations introduces significant complexity on RACH resource set selection procedure, especially when there are multiple resources supporting a subset of all features triggering this RACH procedure.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o012`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

```text
In NR, RACH resources do not adapt well to short-term variations in access load, often resulting in high level of contention and access failures.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o013`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

```text
RACH resource allocation mechanism and procedure in NR are not efficient.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o014`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

```text
Allowing segmentation for CCCH channel can enable the following:
Make the MSG3 payload size flexible without compromising the coverage whilst avoiding the need for preamble partitioning for MSG3/MSGA payload size indication
Enable more features that can wait till MSG3 (e.g. early UE type, slice indication etc) to use MSG3 based indication instead of MSG1 based indication.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o015`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

```text
MAC CEs in 6G are expected to be used to send more diverse types of messages, some of which may demand higher reliability.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o016`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

```text
MAC CEs in 6G can be designed in a more structured way to enable efficient processing and meet the stricter timing requirements expected in 6G.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o017`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
4-step contention-based Random-Access procedure is supported as the baseline.
Noted
R2-2601502	Discussion on other MAC functionalities	Xiaomi	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p001`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
In 6G, both 4-step RACH and 2-step RACH should be supported as a baseline.
Noted
R2-2601560	Discussion on RACH and configured grant	OPPO	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p002`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
For 6G RACH, RAN2 to study whether and how to solve the following problems identified from 5G RACH:
Limitation in multiplexing the RA responses across different RA types, e.g., RAR and MsgB share similarities but cannot be multiplexed into the same DL signalling.
Lack of consideration for dynamic radio link quality change in RACH fallback, e.g., RACH fallback relies solely on attempt number and follows a predefined fallback order.
Less-flexibility in dynamic load distribution, e.g., fixed UL carrier/BWP to perform RACH after initial selection.
Noted
R2-2601778	Random Access and other MAC enhancements	ZTE Corporation, Sanechips	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p003`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
6GR should support a unified framework for RACH where the UE may transmit:
Only preamble and wait for RAR before transmitting the payload part in MSG3 (similar to 4-step RACH in NR)
Preamble + payload parts together (without waiting for RAR) – similar to 2-step RACH in NR
Only RACH payload part without preamble when the UE has valid TA – contention based PUSCH transmission
Noted
R2-2602128	Discussion of other MAC functionalities	Lenovo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p004`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
RAN2 to study a unified Random-Access procedure incorporating 2-step RACH and 4-step RACH types at least for contention-based RA procedure, e.g., Common RACH resource configuration for 2-step RACH and 4-step RACH is applied.
Noted
Discussions on 2-step/4-step RACH
-	Oppo thinks that for 6G we can use a different concept than 2 step RA
-	Qualcomm thinks that 4step is sufficient.  2step RA is low access latency and low access latency is not a key KPI for idle mode and for connected if we have CB-PUSCH then we don’t need it.  Also there is implementation complexity.  Xiaomi thinks that there are cases where the UE cannot send CB-PUSCH.
-	Ericsson thinks that we should study if we need a faster way from preamble to resource allocation.
-	Lenovo thinks that faster access is an important KPI.  We should design it so from gNB perspective it is seen a single procedure so we shouldn’t rule it out yet.
-	ZTE highlights that one important use case for 2step RA is NTN, which has very long RTT, and this is essential.    On the unification, we needed different RAR formats as 2step was added in later release and now we don’t have that problem as if we design from day one we can use one format and think that 2 step RA is the baseline.   Mediatek agrees and we shouldn’t add this in later release.
-	Samsung also see the benefits and there is no reason to exclude it from study, including how to address some of the identified issues.
-	LG agrees with ZTE and Xioami about latency benefit.
-	Sharp doesn’t think it is very essential as it can only be used when the signal condition are good.
-	CMCC thinks we can study whether to unify the PRACH and address such issues.
-	Huawei thinks that if NTN is the main reason then NTN folks need to support this.   ZTE thinks that NTN is one reason but we have other reasons including CP latency reduction.
-	Nokia supports 4 steps as a baseline and if we do 2step we can’t avoid partitioning.
-	Ofinno thinks that from functional point of view we can look at a unified design.
-	Apple also thinks it is too early to exclude anything
-	DLR also thinks unification is important for CB-PUSCH and RA
-	Mediatek reminds everyone that unification just means strive to find commonalities.
Agreements on random access
1	Study “2step” and “4step” RA.  After understanding the functionality, further study how and if the random access procedure can be unified/simplified.  FFS if and whether we can include CB-PUSCH in unification discussion only after some further progress on CB-PUSCH.
2	Both CBRA and CFRA random access procedures are supported
RA Early indications
R2-2601735	Other MAC Functionalities		Nokia 	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p005`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
In 6G, RACH partitioning should be limited to features that require early identification at PRACH detection to ensure correct procedure execution (e.g., OD-SIB1). For other features such as RedCap, eRedCap, SDT, network slicing, SBFD, IAB-MT, OD-SIs and preamble Group A/B, a common RACH configuration should be supported, as they do not require distinct RA response or Msg3 formats.
Noted
R2-2601994	Other MAC functions	InterDigital	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p006`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
The Msg1 indication is only applied to use cases which affect RAR/Msg3 scheduling and/or related procedures.
-	Vivo can this also be used for msg1 retransmission.   Interidigtal explains it is not excluded as anyways it impacts RAR.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p007`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
The Msg3 indication is only applied to use cases which affect Msg4 scheduling and/or related procedures.
-	Samsung thinks that these are good principles and then we can wait for RAN1 design to decide what is needed based on the principle.
-	Huawei asks what is msg3 indication.  Interdigital explains that is redcap or msg4 PUSCH repetetition requests etc.
Noted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p008`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
RAN2 to postpone the discussion on what feature absolutely needs msg1 indication and what can wait for msg3, until it is clear about which feature will be supported as well as physical layer design related to the features are determined in RAN1.
Noted
Not treated
R2-2601624	Discussion on other MAC  functionalities	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
Observation 2-1:	Additional RACH resource could be introduced in addition to RACH resource for initial access in 6G day1 and forward compatibility issues for RACH configuration should be considered.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p009`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
Confirm the following benefits of using RACH partitioning for RACH configuration from RAN2 point of view:
Avoid duplicated parameters of RACH configuration for different features
Ease of co-configuration for features combination (e.g., SDT+ RedCap)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p010`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
If RACH resources for multiple features are needed in system information in addition to RACH resource for initial access in 6G day1, support RACH configuration by RACH partitioning.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p011`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
If RACH partition configuration is supported in 6G Day1, study how to simplify the procedure of RACH resource set selection, e.g., by simplifying the priority-based fallback for CBRA.
Not treated
Adaptive/dynamic RACH resources
R2-2601466	Discussion on other MAC functionalities	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p012`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
Study RACH designs that enable more efficient use of resources, e.g. dynamic or on-demand allocation of RACH resources, beam-specific RACH configurations, etc.
R2-2601518	Random Access in 6G	Samsung	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p013`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
For efficient utilization of resources configured by multiple random access resource sets, when the UE initiates random access procedure, UE can first indicate the random access resource set UE is going to use and then perform random access procedure using the selected random access resource set.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p014`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
Dynamic switch between a set of sparsely configured random access occasions and a set of densely configured random access occasions during the random access procedure is supported in 6G.
R2-2602092	Discussion on MAC functionalities in 6G	Spreadtrum, UNISOC	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p015`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
RAN2 to study dynamic or hybrid RACH resource allocation mechanism and procedure.
Not treated
CCCH segmentation
R2-2601778	Random Access and other MAC enhancements	ZTE Corporation, Sanechips	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p016`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
Study the following options for segmentation of CCCH channel.
Hard segmentation: Network can only decode Msg3 after all the segments are received.
Soft segmentation: Msg3 is defined as multiple messages carrying different self-contained pieces of information that can be decoded independently.
Configured grants – adaptation and NR limitations
R2-2602025	Configured grant and random access procedure	Ericsson	discussion
Observation 1	Configured allocation is not adaptive to channel conditions or traffic changes.
Observation 2	Skip uplink leads to indeterministic receiver behaviour.
Observation 3	CG’s non-adaptive and skip uplink behaviour leads to resource inefficiency.
Observation 4	NR has multiple configured grant frameworks (Type 1 and 2) which leads to complex implementations.
Proposal 1	RAN2 to discuss and agree on below issues faced in NR CG
-	Indeterministic receiver behaviour and resource wastage due to skip uplink,
-	Complexity posed by multiple CG frameworks.
-	In-adaptive to traffic and channel variations,
-	Uplink reporting unable to address resource deficiency,
-	CG retransmissions via grants handled separately from dynamic grants,
-	Restrictions on retransmissions over CG.
Noted
R2-2601502	Discussion on other MAC functionalities	Xiaomi	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p017`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
6G CG configuration should be able to allow:
- CG resource immediately usable for delay critical service;
- Dynamical activation/deactivation;
- Dynamical adjustment of CG size;
- Adaptation to jitter;
- Flexible Resource sharing/recycling.
Noted
R2-2601994	Other MAC functions	InterDigital	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p018`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
Configured Grants for 6GR support:
-	Semi-static configuration of resources;
-	Dynamic activation/deactivation of configured resources (e.g. by DCI);
-	Dynamic adaptation of a resource allocation and timing parameter without requiring RRC reconfiguration (e.g. indication of a start offset by DCI).
Noted
-	Mediatek thinks that we should at least benchmark all these dynamic CG options with dynamic grant.
| Agreements on configured grants 1 Study 6G CG, which can support at least the following from RAN2 perspective: - CG resource immediately activated (e.g. for delay critical service) after configuration; - Dynamic activation/deactivation; - Dynamic adjustment of resource allocation (e.g. MCS, TBS and start time); - Support different traffic types - Higher resource efficiency (e.g. unused resource indication, etc). 2 Inform RAN1 about our agreements and any further agreements in May meeting |
| --- |
Not treated
Configured grants - UE indication
R2-2601447	Considerations on 6GR CG and Random Access	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p019`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
RAN2 to study CG recycling mechanism on UE initiating the advance indication to inform aNB about the upcoming CG utilization.
R2-2601832	Views on 6G User Plane: Miscellaneous MAC Mechanisms	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p020`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
To improve resource efficiency of CG, the UE may first indicate its intention to use particular CG resources, before performing CG PUSCH transmission.
R2-2601807	Discussion on Configured Grants	Philips International B.V.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p021`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
RAN2 to study how to perform dynamic updates of the CG configuration.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p022`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
RAN2 to study procedures for the UE to request a change of CG configuration to the network.
MAC PDU format and MAC CEs  (if time allows)
R2-2601624	Discussion on other MAC  functionalities	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
Observation 6-1:	Not including the L field in the MAC subheader for the fixed-sized MAC CE saves only a small bit overhead but significantly increases the processing and implementation complexity.
Observation 6-2:	The 5G LCID design lacked forward scalability, forcing incremental fixes (e.g., eLCID field or LX field) that increased overhead and complexity.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p023`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
RAN2 to study the potential enhancements for MAC PDU format, e.g., for the L field and LCID design.
R2-2601466	Discussion on other MAC functionalities	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p024`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

```text
Design MAC CEs to have a versatile format suitable for multiple purposes, while easy to process and assemble.
R2-2601474	Discussion on RACH and CG	NEC	discussion	Rel-21	FS_6G_Radio
R2-2601576	Discussion on 6GR MAC Functionalities	Sharp	discussion	Rel-20	FS_6G_Radio
R2-2601857	6G Random Access and Configured Grant	Ofinno	discussion
R2-2601909	Random Access and Configured Grant	CATT	discussion	Rel-20	FS_6G_Radio
R2-2601946	Discussion on RACH partitioning for 6GR	TCL	discussion
R2-2602040	Discussion on other MAC functionalities	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
R2-2602160	Other MAC functionalities: CG and Random-access	Sony	discussion	Rel-20	FS_6G_Radio
R2-2602266	Discussion on RA procedure and CG	NTT DOCOMO	discussion	Rel-20	FS_6G_Radio
R2-2602377	Discussion on early indication in 6G RA 	ETRI	discussion	Rel-20
R2-2602414	Considerations on other MAC functionalities for 6GR UP	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2602471	Discussion on random access procedure	Google Korea LLC	discussion	FS_6G_Radio
R2-2602544	Some Views on Random Access	1Finity	discussion	Rel-20
R2-2602596	MAC processing for high data rates	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p025`

### [6G/Rel-20 RAN2#133] `agreement` 10.3.1.3 Scheduling

```text
RAN2 continues study.  RAN2 will lead the evaluation of the CB based schemes.   Determine some high level evaluation assumptions.  Identify the inputs needed from RAN1.      NOTE: check and consider LTE simulations and NTN simulations to determine what will need to be simulated.   NTN should also be taken into account.
Intention is to compare and take into account solutions with RAN1 and RAN2 solutions.   FFS which other solutions we will continue evaluating for comparison purposes (still to discuss in this meeting…)
Assumption is that dedicated SR mechanism to request UL resource is considered as a baseline mechanism, as discussed and defined in RAN1 (if defined).
[POST133][013][6G UP] Assumptions (Oppo)
Intended outcome:
Discuss questions that need to be asked to RAN1
Discuss high level simulation assumptions to be used for evaluation in RAN2
Deadline:  Long to submission deadline
Not treated
Evaluation assumptions [20 mins –offline]
Scope of use
R2-2600377	On scheduling and latency reduction	Nokia	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-a001`

### [6G/Rel-20 RAN2#133] `agreement` 10.3.1.3 Scheduling

```text
Buffer status and delay status information will be supported.   FFS any other information
Details of buffer status and delay status information and how they are formatted/unified can be discussed after some progress on overall functionality.
Early Reporting
R2-2600077	Discussion on 6GR scheduling	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-a002`

### [6G/Rel-20 RAN2#133] `agreement` 10.3.1.3 Scheduling

```text
Study early reporting of information useful for UL scheduling purposes. FFS details of the information.
Not treated
Granularity of scheduling (if time allows)
R2-2600289	Scheduling Aspects for 6GR	SHARP Corporation	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-a003`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.3 Scheduling

```text
Several aspects in the upper-layer design for contention-based UL transmission depend on physical layer designs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-o001`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.3 Scheduling

```text
Without CB PUSCH-specific statistics like average collision ratio, it is challenging to accurately evaluate its performance or configuration optimality.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-o002`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.3 Scheduling

```text
Traffic models will affect CB PUSCH collision rates differently, reinforcing the need for diverse models in simulations.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-o003`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.3 Scheduling

```text
The number of UEs, together with the CB-PUSCH resource pool size, directly affects the collision ratio on CB-PUSCH resources.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-o004`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.3 Scheduling

```text
The UE can transmit multiple SR and BSR reports to indicate data SDU arrivals within a single UL data burst, resulting in increased signaling overhead and scheduling delay.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-o005`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.3 Scheduling

```text
Flows with different service requirements can be better served with different HARQ transmission parameters (e.g. MCS, number of retransmissions)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-o006`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.3 Scheduling

```text
The LCP procedure in NR may not be sufficient in supporting more diverse traffic in 6G, due to increased presence of delay sensitive traffic such as XR and mobile AI.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-o007`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.3 Scheduling

```text
New 6G use cases such as application context awareness and adaptive QoS require LCP to be more adaptive than NR.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-o008`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.3 Scheduling

```text
The 5G "two-phase" LCP process provides a clear structure: the first phase ensures mandatory and deterministic QoS, and the second phase handles best-effort resource optimization.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-o009`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.3 Scheduling

```text
The legacy LCP mechanism, relying on static priority and PBR configurations, leads to inflexibility in handling dynamic traffic profiles and context-aware QoS requirements.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-o010`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

```text
Ask input from RAN1 on the following physical-layer aspects of contention-based UL transmission:
-	how UEs are identified when there is a contention;
-	how retransmission after a contention is handled;
-	Range of payload size.
[3 mins]
Noted
Discussion
-	Qualcomm is concerned to have RAN2 run a full blown simulation.  It is common sense the contention based has the benefits and drawback.    ZTE agrees with Qualcomm and we should cooperate with RAN1 as early as possible, payload size.   IT would be good to have some comparison.  Ericsson thinks that we need to consider resource efficiency and blind decoding complexity.   RAN2 should do this analysis especially for end-to-end latency.   We can just agree to some high level assumptions.
-	ESA explains that we introduced CB for msg3 in IoT NTN.   We did a simulation in RAN2 but we can coordinate a bit with RAN1.
-	Nokia thinks that we have some simulation activities and the traffic model would impact and not sure whether we have the expertise.   Interdigital thinks RAN1 should be involved for some aspects but it doesn’t mean they are the only group.
-	Xiaomi thinks that RAN2 can’t do such simulations.    Ericsson doesn’t think they can model protocol aspects and end-to-end considerations.
-	Apple thinks that full scale simulation may not be needed but RAN1 should be involved.
-	Vivo thinks that even the methodology needs to be done by RAN1.
-	LG thinks that the simulations should be in RAN2 as it is related to QoS but RAN1 input is needed.
-	Mediatek thinks that the drawback can be controlled by the network.   RAN1 can provide some input but only what RAN2 determines needs.
-	Samsung thinks that there are other ways like finer granularity CG.   Sharp thinks we can start the simulation to at least check if CB has clear benefits and consider the other schemes.   Vivo thinks that RAN1 is discussing other SR based solutions.
-	ZTE thinks that the one thing missing in LTE is NTN which has long RTT times.
-	Qualcomm thinks that if we use both SR like and CB based scheme, there is no point of doing evaluation.
-	ZTE thinks that we’d have to understand what things we’d need to do to make it more efficient
-	Ericsson thinks that we shouldn’t have two solutions.  Mediatek agrees.
-	Apple thinks that CB may be beneficial in some scenarios but SR is proven to work in all scenarios.   ATT thinks that SR needs to be a fallback mechanism.    Fraunhoufer agrees with Apple, the issue is that we have many problems and we should try to find the minimum set.  Xiaomi thinks that CB-PUSCH only work when collision rate is low, so we will always need SR.
-	Docomo thinks that we don’t want duplication and SR like mechanisms will always work, so it should be assumed.
-	Samsung thinks that the network has to meet the enforced QoS requirements which is the SR mechanism.
-	Ericsson understands that we haven’t agreed to have SR mechanisms but it is used as baseline for evaluation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p001`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

```text
Focus the initial study of CB-PUSCH exclusively on RRC connected mode and BSR/DSR messages.
R2-2600289	Scheduling Aspects for 6GR	SHARP Corporation	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p002`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

```text
RAN2 to study contention-based UL resources shared for both BSR and small data transmissions.
R2-2600429	Evaluation assumptions for contention based BSR	Ericsson, LG Electronics Inc., OPPO, MediaTek Inc., Sharp, NTT Docomo, Verizon, AT&T, Turkcell	discussion	Rel-20
Observation 9 Allowing UE to use CB resources to transmit data will increase the frequency of CB resource usage.
Observation 10 It is feasible and can be discussed later whether to include data using the leftover resources after the BSR is included.
Observation 11 Using HARQ for CB resources for BSRs causes problems without providing any benefits.
Observation 12 It is reasonable to allow a UE to reattempt the CB transmission if the UE didn’t receive a grant within a time after the previous transmission
Proposal 3	For transmissions using CB resources, RAN2 agrees to the following evaluation assumptions:
c.	Each transmission is triggered by BSR.
d.	Each transmission is based on HARQ disabled mode.
e.	if a response was not received within a time after the previous transmission, the BSR is reattempted. FFS whether the response is an explicit (e.g., CB MAC CE) or implicit (e.g., uplink grant addressed to C-RNTI).
UE Identification
R2-2600429	Evaluation assumptions for contention based BSR	Ericsson, LG Electronics Inc., OPPO, MediaTek Inc., Sharp, NTT Docomo, Verizon, AT&T, Turkcell	discussion	Rel-20
Observation 7 Including the UE ID in the transmission is a natural solution for contention resolution.
Observation 8 DMRS sequences is needed in transmission to provide code division multiplexing to allow multiple UEs to conduct transmissions using the same resources without interference.
Proposal 3	For transmissions using CB resources, RAN2 agrees to the following evaluation assumptions:
a.	Each transmission includes a UE ID for contention resolution.
b.	Each transmission is multiplexed with a DMRS sequence. FFS the DMRS sequence is dedicated
R2-2600773	Discussion on scheduling enhancements for 6G	Panasonic	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p003`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

```text
For contention resolution with contention-based uplink resources, the UE need not explicitly indicate UE-ID to the network.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p004`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

```text
RAN2 to consider feedback based on DMRS detection with the following options:
-	Dedicated DMRS
-	Shared DMRS
-	Network Configuration between dedicated and shared
R2-2600620	Discussion on 6G scheduling	NTT DOCOMO INC..	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p005`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

```text
RAN2 should study UE identification in coordination with RAN1.
Contention resolution
R2-2600377	On scheduling and latency reduction	Nokia	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p006`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

```text
Simulation results should include statistics, such as the average collision ratio, alongside assumptions for UE multiplexing, CB PUSCH resource size, and traffic models.
R2-2600620	Discussion on 6G scheduling	NTT DOCOMO INC.	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p007`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

```text
On contention resolution for CB-PUSCH, the followings are considered as a baseline.
	A UE can consider the contention resolution successful when the UL grant is allocated by the network.
	A UE can consider the contention resolution failure when a timer expires.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p008`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

```text
RAN2 to evaluate CB scheme from collision tolerance and coverage aspects as well as latency and resource efficiency.
R2-2600961	Considerations on scheduling for 6GR UP	CMCC	discussion	Rel-20	FS_6G_Radio
Observation 1d: CB-PUSCH has less latency with a small group of UEs, however, when the UE population grows, SR has less and stable latency compared to CB-PUSCH
Proposal 1b: RAN2 should further study the evaluation assumptions with UE population which has impact on the latency and resource usage performance for both CB-PUSCH and SR.
R2-2600245	Discussion on Scheduling	CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p009`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

```text
The UL latency reduction solutions can be compared from the following perspectives: PUSCH resource configuration, collision probability and contention resolution.
Other
R2-2600403	Contention-based BSR reporting	MediaTek Inc.	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p010`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

```text
RAN2 to study the mechanism that how the contention-based uplink resource pool is configured or indicated to UE(s).
R2-2600059	Scheduling in 6G	Samsung	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p011`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

```text
Periodic UL grants (i.e. configured grants) for fast BSR delivery is supported.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p012`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

```text
PUCCH resource to indicate usage of UL grants for BSR can be optionally configured.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p013`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

```text
For contention based BSR, 2 step RACH configuration dedicated for BSR purpose is configured. The 2 step RACH configuration is shared with multiple UEs. Preambles can be optionally assigned separately to UEs sharing the 2 step RACH configuration.
Not treated
Scheduling request
R2-2600377	On scheduling and latency reduction	Nokia	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p014`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

```text
Dedicated SR to request UL resource is to be supported for 6G, regardless of whether CB-PUSCH would be introduced.
[2 mins]
R2-2600289	Scheduling Aspects for 6GR	SHARP Corporation	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p015`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

```text
RAN2 to study finer granularity of SR to enable direct UL resource allocation without separate BSR transmission.
[2 mins]
R2-2600449	Views on 6G User Plane: Scheduling	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p016`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

```text
To reduce SR/BSR latency, RAN2 can consider using SR configuration ID to represent certain information related to the buffer status (e.g. buffer size, or presence of delay-critical data), such that network can timely allocate more appropriate UL resource even without BSR.
[2 mins]
Scheduling Information Reporting
Unified BSR/DSR
R2-2600077	Discussion on 6GR scheduling	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p017`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

```text
For a unified BSR and DSR framework in 6GR, RAN2 should study the following aspects:
-	Harmonized triggering mechanisms based on joint consideration of data arrival and/or remaining time;
-	Integrated reporting formats comprising both delay status and buffer status.
Noted
R2-2600427	Discussion on UL scheduling aspects in 6G	Lenovo	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p018`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

```text
RAN2 to study a unified UL data-related status reporting procedure in 6G which includes information on the data/buffer status as well as the delay status of the data and potential further information, e.g. importance of the data.
[2 mins]
Noted
Discussion
-	Ericsson thinks that the unification shouldn’t impact the frequency of the BSR reporting and we should design it such that DSR is not always included.
-	Lenovo thinks that if we trigger BSR why not include DRS.  The triggers can be same.
-	Apple thinks that if we have data arrival but not delayed data, there is no reason to report DRS.   Having an integrated BSR/DSR is fine but we should consider defining just BSR and just DSR and one that includes boths.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p019`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

```text
6GR to study early uplink radio resource request triggering mechanism based on the estimated burst arrival information (e.g., burst arrival time, burst size) with service-awareness.
[3 mins]
Noted
R2-2600737	L2 scheduling framework for 6GR	InterDigital	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p020`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

```text
Reporting anticipated data arrival for an UL data burst is supported (burst metrics: burst delay, number of data packet units, packet size), within the constraints set by the data burst and network configuration.
[2 mins]
Noted
R2-2600151	Discussion on scheduling and scheduling information reporting	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p021`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

```text
RAN2 to study latency reduction of UL resource request for the dynamic scheduling by the early triggering of SR before data arriving at the AS buffer.
[2 mins]
Noted
Discussion
-	Qualcomm supports early reporting for both SR and BSR and how the UE determines it its UE implementation.
-	Fraunhoufer indicates that we should be able to also provide some traffic characteristics.
-	Interdigital thinks that we also touched upon burst characteristics so those would be useful to report to the scheduler.  Mediatek asks if we report BSR and DSR don’t we provide enough information.  Interdigital explains that we’d provide burst information not the BSR per logical channel.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p022`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

```text
The buffer status is indicated per LCG.
R2-2600523	Consideration on Scheduling and uplink scheduling information in 6G	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p023`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

```text
Study following enhancements for scheduling information in 6G BDR:
-	Scheduling information with finer granularity, e.g. per-QoS flow, per-LCH, or per importance level
-	Expected size of pending MAC CE
R2-2600141	Discussion on scheduling procedures	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p024`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

```text
Support finer granularity for HARQ and allow network to schedule different logical channels by separate HARQ processes.
Data/Logical Channel Prioritization (if time allows)
R2-2600484	Discussion on scheduling in 6GR	China Telecom	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p025`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

```text
RAN2 to study the new LCP design that supports dynamic adjustment of LCP parameters.
R2-2600077	Discussion on 6GR scheduling	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p026`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

```text
RAN2 to further study LCP enhancements considering the varying traffic characteristics, e.g., delay, importance, inter-QoS flow/packet dependency.
R2-2600141	Discussion on scheduling procedures	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p027`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

```text
Study new LCP designs that
-	can support multiple performance objectives (e.g. throughput vs delay) in a cohesive way;
-	are more direct in handling congestion (e.g. UL grant for a specific LCH);
-	are more adaptive than NR in supporting new use cases such as application context awareness and adaptive QoS.
R2-2600099	Consideration on 6G UP Scheduling and retransmission	Xiaomi	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p028`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

```text
RAN2 is recommended to study an enhanced LCP framework for 6G, which includes:
-	Retention and clarification of a well-defined "two-phase" LCP process;
-	Support for the dynamic adjustment of LCP parameters, including but not limited to:
	Logical channel priority (extending beyond delay based boosting);
	Prioritized Bit Rate (PBR) and token bucket state (Bj).
R2-2600095	Discussion on 6GR scheduling	WILUS Inc.	discussion	FS_6G_Radio
R2-2600100	Discussion on DSR enhancement	Xiaomi, BYD, Ofinno, Meta, Huawei, HiSilicon, Toyota ITC	discussion	Rel-20
R2-2600166	Contention based UL channel for 6G	ZTE Corporation, Sanechips, Sony	discussion
R2-2600209	Discussion on scheduling improvements	OPPO	discussion	Rel-20	FS_6G_Radio
R2-2600211	Considerations for signaling design for contention-based scheduling	Tejas Network Limited	discussion	Rel-20
R2-2600350	Discussion on scheduling enhancements for 6G	Fujitsu	discussion	Rel-20	FS_6G_Radio
R2-2600386	On the improvements for the 6G BSR	Google	discussion	Rel-20	FS_6G_Radio
R2-2600400	Latency reduction for 6GR	Fraunhofer IIS, Fraunhofer HHI	discussion
R2-2600519	Discussion on Scheduling	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2600579	Discussion on Contention based UL resource	ASUSTeK	discussion	Rel-20
R2-2600628	Discussion on scheduling in 6G	Transsion Holdings	discussion	Rel-20
R2-2600655	6G UL scheduling	NEC	discussion	Rel-20	FS_6G_Radio
R2-2600721	Improving resource efficiency for small UL packets	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
R2-2600856	6G Scheduling and information reporting	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2600897	Discussions on scheduling enhancements	Futurewei	discussion	Rel-20	FS_6G_Radio
R2-2600973	Discussion on scheduling in 6G	DENSO CORPORATION	discussion	Rel-20
R2-2601043	Scheduling enhancements for 6GR	CEWiT	discussion	Rel-20	FS_6G_Radio
R2-2601049	Discussion on UL scheduling in 6G	III	discussion	Rel-20	FS_6G_Radio
R2-2601108	Discussion on 6GR Scheduling 	Rakuten Mobile, Inc	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p029`

### [6G/Rel-20 RAN2#132] `agreement` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

```text
1	RAN2 will study solutions on how to improve latency and UL resource efficiency of scheduling (including contention based schemes).
2	RAN2 study on CB UL will assume the following:
-	Baseline for comparison is at least the normal SR/BSR functionality we have today
-	Companies can highlight the similarities and differences between the proposed solutions with what we have today for 5G (e.g. shared CG resources with or without retransmissions, 2-step RACH like scheme without preamble etc).
-	Discussion on further assumptions is FFS based on the solutions identified.
Scheduling requests
R2-2508310	UP functionalities and requirements	Nokia, Nokia Shanghai Bell	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-a001`

### [6G/Rel-20 RAN2#132] `agreement` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

```text
To support periodic traffic like voice, as a baseline support DL SPS
For UL, continue to study CG like mechanisms to address different types of traffic, including voice, bursty traffic, other periodic traffic etc.
BSR
R2-2508408	Scheduling and Retransmission Aspects	SHARP Corporation	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-a002`

### [6G/Rel-20 RAN2#132] `agreement` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

```text
Study mechanisms to provide scheduling information (including at least buffer status reporting, delay status reporting).   FFS other scheduling information needed depending on traffic/services.   Aim to unify the framework if possible, after some progress on the detailed functionalities.
(Not treated) (If time allows)
LCP
R2-2508034	Discussion on scheduling in 6G	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-a003`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

```text
Reliance on HARQ coordination may speed up the RLC recovery loop. However, the RLC Sequence Number-window based mechanism guarantees that eventually all HARQ errors are corrected independent of HARQ degradation, and gives NW flexibility to trade off different design KPIs (latency, spectral efficiency, power, overhead, processing, etc.)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-o001`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

```text
UL data can be reliably transmitted if the UE gets HARQ feedback for UL transmissions.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-o002`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

```text
In NR, several steps/signalling interactions are required to acquire the UL grant for BSR/DSR MAC CE transmission, i.e., via SR or RACH, which increases UL transmission latency.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-o003`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

```text
Contention-based UL transmissions should not be the only option for sending SR/BSR, as its latency is not deterministic and can depend on several factors, such as periodicity of transmissions occasions, contention levels, etc.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-o004`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

```text
BSR and DSR have duplication which results in signalling overhead or even inefficiency.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-o005`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

```text
New 6G use cases such as application context awareness and adaptive QoS require LCP to be more adaptive than NR.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-o006`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

```text
The legacy LCP procedure leads to LCH starvation, resource inefficiency, and inflexibility in handling dynamic traffic requirements—particularly for delay-sensitive applications.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-o007`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

```text
Sequence number-based L2 recovery mechanism is the baseline for ARQ. ARQ to retain the requirement to achieve up to 100% reliability independent of HARQ.
-	Vivo asks what happens if HARQ is disabled.  Qualcomm explains that ARQ can still kick in.
Noted
R2-2508107	Discussion on 6G scheduling and (re-)transmission schemes	OPPO	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p001`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

```text
ARQ retransmission based on STATUS reporting is supported.
Noted
R2-2508567	Discussion UL scheduling and Retransmission protocols	Lenovo	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p002`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

```text
RAN2 to study mechanisms for locally triggered ARQ retransmissions at the transmitter side based on HARQ status and feedback.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p003`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

```text
RAN2 to study mechanisms enabling faster RLC retransmission triggered based on HARQ status or feedback, including locally triggered ARQ retransmissions at the transmitter side and explicit network indications to initiate local NACK procedures.
Noted
---
R2-2508319	Scheduling and retransmission enhancements for 6G	ZTE Corporation, Sanechips	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p004`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

```text
RAN2 should study a fast ARQ mechanism for UL where the ARQ is triggered by lower layer signalling (e.g. in DCI) to enable an immediate ARQ like retransmission from upper layers – inform RAN1 to enable the DCI signalling for this
Noted
R2-2508126	On latency reduction mechanisms for 6G eMBB traffic	MediaTek UK	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p005`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

```text
The UE is provided with explicit HARQ feedback that indicates the decoding result of UL transmissions.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p006`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

```text
Send an LS to RAN1 to take the following design requirements into consideration:
2.	HARQ feedback designed to be robust to misinterpretation
3.	HARQ feedback made available to the UE for UL transmissions
Noted
Discussion
-	LG asks why we need SN if we have HARQ feedback.   Interdigital explains that there are cases where this is needed, including NTN where there may be no HARQ.
-	Samsung thinks that this should be an optional feature.   Sharp thinks we should only support one mechanism.
-	Lenovo agrees that explicit HARQ status is beneficial.   Interdigital agree and for configured grant there is no explicit feedback.  Qualcomm agrees that we may need the status but we need to first discuss and then if we agree then we can tell RAN1.
-	Oppo explains that the UE only know if the packet has to be retransmitted but not if it was successful.  Apple agrees.  We should tell RAN1 that this is beneficial for RAN2 so please implement it.
-	Nokia also thinks that it makes sense to tell the UE why the packet is dropped.   Vivo wonders why we need to bother RAN1 as MAC CE.
-	Sony thinks that feedback would create overhead
-	Huawei thinks that RAN1 has introduced explicit feedback for CG
-	Ericsson thinks that L1 signaling should be used and we should bother RAN1.
-	LG agrees that we should be careful because for CG we would be increasing resource inefficiencies.
Agreements on HARQ - ARQ
1	Assume that sequence number-based L2 recovery mechanism is supported for ARQ
2	Study mechanisms for faster ARQ retransmissions at the transmitter side based on HARQ process status (e.g. whether the TB was successful or not).   Start with UL and can consider DL.
3	From RAN2 perspective, it is beneficial to have explicit UL HARQ process status from gNB for this purposes.  FFS on the details of explicit UL HARQ process status.
UL contention-based resources
R2-2508107	Discussion on 6G scheduling and (re-)transmission schemes	OPPO	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p007`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

```text
To reduce UL latency, RAN2 to support contention-based CG resources at least for direct BSR/DSR MAC CE transmission.
-	Xiaomi would like to understand the difference between the current shared resource and DMRS based resolution and this proposal.   Oppo considers that the 6G solution can perform more, as NR is NW implementation.   LG explains that in legacy the UE doesn’t know if it is shared or not so doesn’t need to be involved in contention resolution phase.
-	Fraunhaufer asks whether the proposal is limited to CG.  Oppo explains that it is an example.
-	Samsung asks what is the use case we are targeting as it doesn’t work for URLLC.  Oppo thinks that this to address the resource efficiency.  Samsung thinks that this will then increase latency in the cases of contention.
Noted
R2-2508034	Discussion on scheduling in 6G	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p008`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

```text
Which type of UL resources (e.g. CBUL vs CG vs PUCCH) should be used to for transmitting SR/BSR can be left to network configuration. Study techniques that can reduce transmission latency of SR over different types of UL resources.
Noted
R2-2508126	On latency reduction mechanisms for 6G eMBB traffic	MediaTek UK	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p009`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

```text
Send an LS to RAN1 to take the following design requirements into consideration:
1.	Contention-based UL PUSCH resource designed for early BSR reporting
Noted
Discussion
-	LG thinks it is important to study such types of schemes.
-	Xiaomi doubts the real motivation of this compared to real CG
-	Lenovo agrees to study but we should compare it to other schemes and see if it provides real gains.
-	Apple, Nokia thinks we can study but it is important to evaluate how much additional benefits we get when compared to what we have already.   Also RAN1 should be involved for study the collision probability etc.  ZTE thinks RAN2 can evaluate too.
-	Vivo also thinks that we need to compare all the solutions, but we can study.  Offino also thinks we can study.
-	Mediatek thinks we should study mechanism to reduce latency.  Ericsson and Sony thinks that it is both resource efficiency and latency.
-	Sony thinks we should consider other schemes as well.
-	Nokia thinks that no matter what we design it is important to have network control on what scheme being.
-	Ericsson thinks that we should study performance evaluation as well and encourages companies to also evaluate and should highlight the benefits.
-	Interdigital thinks that in the case there is no contention the benefit is latency but if there is contention then latency is a function of collision.   The network should have the tools to configure the needed scheme.
-	Huawei explains that one use case is the bursty type of data.  Huawei asks what is the benchmark and we need to discuss simulation assumptions.
-	ZTE views this also a channel for any bursty data, so the UE doesn’t have to send BSR.  So it should be generic and we need to study how much data can be sent on this.  Lenovo that one issue is that if more data is transmitted on these resources the collision probability will be increased, so let’s start with BSR and then determine if we can transmit any higher layer data.
-	Fraunhaufer thinks we need to understand the type of traffic we are trying to address it is difficult to evaluate
-	Samsung is concerned that we haven’t agreed about the current BSR so it is too early to evaluate.   Ericsson thinks that we know how the current protocols work and when we have bursty UL traffic we save quite a lot.    We looked at UL data and the issue is that it increased collision.
-	Ericsson thinks that we don’t need to go into tiny details of simulation assumption alignment.
-	Qualcomm thinks that some of these aspects depend on the PHY characteristics, so we should wait for some understanding how it works.  LG doesn’t thinks that the RAN1 progress is so important and also UL traffic is also not so important.    All we want to do is evaluate is comparison between legacy procedure and skipping the SR.   ZTE agrees with LG.   One thing we need to understand the contention resolution (e.g. whether we put an ID in the channel or if RAN1 has a way to differentiate the UE).
-	Huawei asks whether this is a RAN1 and/or RAN2 solution.  If we discuss in RAN2 we should only discuss RAN2 related aspects.
-	Xiaowei thinks we should compare with shared CG and not with SR.
-	Vivo thinks that this RAN2 solution and it should be started in RAN2, and we can use 5G baseline design for evaluation.
After offline the following were brought up
1. 	Whether UE ID is needed to address contention resolution
2.	Whether DMRS is dedicated or shared
3.	Whether to limit CB to BSR or also include data.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p010`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

```text
For scheduling information, dedicated SR to request UL resource as well as BSR/DSR like mechanism to report buffer status and delay information are to be supported for 6G, regardless of whether CB-PUSCH would be introduced.
From 10.3.1.1
Noted
R2-2508138	Discussion on scheduling, retransmissions and uplink scheduling information in 6G	Huawei, HiSilicon	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p011`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

```text
When there is no UL-SCH resource for the UE to send the scheduling information to RAN, UE sends scheduling request to the RAN for UL-SCH resource for sending such scheduling information.
Noted
Discussion
-	Xiaomi and Samsung think that it is very important to keep the dedicated SR as it is too risky in high system load scenarios.
Configured grants
R2-2508049	Discussion on 6GR scheduling and retransmission	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p012`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

```text
Both Type 1/2 configured grant in 5G are supported as the starting point, and 6GR further study the related resource efficiency enhancements, for low latency uplink resource allocation.
Noted
R2-2508848	Considerations on scheduling and retransmisson for 6GR UP	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p013`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

```text
RAN2 should study radio resource configuration and adjustment enhancement for CG to adopt service with bursty traffic.
Not treated
R2-2508127	On scheduling, retransmissions and uplink scheduling information	Nokia, Nokia Shanghai Bell	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p014`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

```text
Study a unified CG framework that satisfies at least the following requirements: 1) RRC-based configuration, 2) Flexible CG activation, 3) Flexible modification using DCI
Noted
Discussions
-	CATT thinks that CG type 1 is for delay sensitive services and type 2 is for overhead so it is very hard to unify.    Nokia agrees that those are for two for different requirements but it doesn’t mean we can’t try to find a way in 6G to unify.
-	Lenovo asks what is the difference between 2 and 3.
-	Oppo likes the idea to unify
-	sony thinks the 3rd bullet flexible modification of transmission parameters  using DCI/UCI
-	Ericsson thinks that first we must agree on the issues and then we can determine whether any enhancements are needed.
-	Apple asks what is the baseline R15 or R16 CG as baseline, they think R16 should be the baseline.
-	Interdigital thinks that the multiple CG and trying to predict the traffic, wasn’t the most useful way.   In 6G we are discussing bursty traffic so predictability is difficult so we should look at how to adapt the CG more dynamically for these types of traffic.
-	LG think that both functionalities are needed.   But current solutions are too static so we should consider something similar to what Nokia is proposing so we can unify and be more dynamic.
-	Huawei thinks that if we have bursty data we shouldn’t have CG in the first place.  So each CG enhancment has to have a reason.   We can take legacy type 1 and type 2 from the beginning as we will still have voice and urllc.
-	Samsung thinks we should first wait for what type of traffic characteristic we have then we can discuss.
-	Mediatek thinks that these discussions can be discussed together with the resource efficiency discussion.   We shouldn’t use a baseline from NR.
-	Qualcomm thinks that we should have CG in 6G and we can study enhancements but we don’t need to unify as there is no commonality between the two.  They were designed for two different reasons and have different PHY procedures.
-	Ofinno thinks we should have Rl15 as baseline.
-	ZTE indicates that we have to at least support voice and therefore we need something periodic like DL SPS. For UL we can discuss how to address repeating traffic, including voice and other types of traffic including bursty.   Lenovo agrees that we should support some form of semi-persistent schedule.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p015`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

```text
RAN2 to study a unified buffer status reporting including total buffered data volume and delay status of the buffered data.
Noted
R2-2508127	On scheduling, retransmissions and uplink scheduling information	Nokia, Nokia Shanghai Bell	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p016`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

```text
For scheduling information report, we aim at defining unified procedure for buffer status and delay status reporting, covering also the report of new types of data for 6G.
Noted
Discussion
-	Apple thinks that before we talk about unified DSR, we should first discuss whether we have DSR.
-	Qualcomm thinks we should have a unified DSR/BSR and what we include.
-	Lenovo thinks we should have a unified scheduling procedure and not just limit to DSR/BSR
-	CATT supports but asks what is the understanding on the solution.
-	Docomo thinks that we should separate whether we unify singaling or procedures. And signaling we should be careful as BSR is small so we should not impact performance.   Nokia thinks we should consider both, including triggers.  We can consider to indicate what we are reporting but the MAC CE format can be unified.   Also we can also discuss the format as we have different BSR for grant sizes.
-	Vivo asks about the triggers, if we unify do we have to report both.  Nokia thinks we can discuss.
-	Ericsson thinks we should have unified buffer related information and not limit it only to MAC CE.
-	MEdiatek asks for eMBB I don’t care about latency so do we need to report DSR.    Nokia think we can configure whether DSR I reported.
-	Huawei doesn’t think it matters at this point,we should discuss what needs to be reported, buffer status and delay.  ZTE agrees.
-	Interdigital thinks that we are going into stage 3 details, but the intention is that buffer status reporting and DSR are not separately transmitted when both pending.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p017`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

```text
Study new LCP designs that can support multiple performance objectives (e.g. throughput vs delay) in a cohesive way and be more adaptive than NR to support new use cases such as application context awareness and adaptive QoS.
R2-2508094	Consideration on 6G UP Scheduling and retransmission	Xiaomi	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p018`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

```text
Study enhanced LCP mechanism allowing dynamic adjusting of LCP parameters.
R2-2508049	Discussion on 6GR scheduling and retransmission	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p019`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

```text
LCP design in 5G is taken as a starting point, RAN2 further study LCP enhancements considering the traffic characteristics, e.g. delay, importance, inter-QoS flow/packet correlation.
R2-2508060	Addressing the SR/BSR User Plane Latency: Round-Trip Grants	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
R2-2508146	Cross-layer coordination between ARQ and HARQ for 6G user plane	KT Corp.	discussion	Rel-20	FS_6G_Radio
R2-2508225	Discussion on L2 re-transmission in 6G	Transsion Holdings	discussion	Rel-20
R2-2508235	Discussion on L2 Retransmission and Scheduling	CATT	discussion	Rel-20	FS_6G_Radio
R2-2508270	Discussion on scheduling enhancements for 6G	Fujitsu	discussion	Rel-20	FS_6G_Radio
R2-2508316	Retransmissions and scheduling aspects for 6G	Samsung	discussion	Rel-20
R2-2508344	Scheduling and retransmissions	Ericsson	discussion	Rel-20
R2-2508383	Views on 6G User Plane: HARQ and Scheduling	Apple	discussion	Rel-20	FS_6G_Radio
R2-2508439	Consideration on Scheduling, retransmissions and uplink scheduling information in 6G	LG Electronics Inc.	discussion	Rel-19	FS_6G_Radio
R2-2508523	Discussion on 6GR User plane	KDDI Corporation (TTC)	discussion	Rel-20
R2-2508544	Scheduling enhancement to address latency – initial simulation results	Sony	discussion	Rel-20	FS_6G_Radio
R2-2508596	Discussion on Scheduling and Retransmission	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2508615	UL HARQ- and CSI feedback in 6G	Ericsson	discussion	Rel-20	FS_6G_Radio
R2-2508629	6G Scheduling and (re-)transmission	Ofinno	discussion	Rel-20
R2-2508643	L2 scheduling framework for 6GR	InterDigital	discussion	Rel-20	FS_6G_Radio
R2-2508650	Discussion on UL Scheduling in 6G	Tejas Network Limited	discussion
R2-2508670	Discussion on UL scheduling improvements	NEC	discussion	Rel-20	FS_6G_Radio
R2-2508798	On scheduling and retransmission for 6G	NTT DOCOMO INC.	discussion	Rel-20	FS_6G_Radio
R2-2508904	Discussion on Re-transmissions for 6G RAN	TCL	discussion	Rel-20	FS_6G_Radio
R2-2508989	Discussion on retransmission and uplink scheduling	ETRI	discussion	Rel-20
R2-2509028	Retransmission enhancements for 6GR	CEWiT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p020`

