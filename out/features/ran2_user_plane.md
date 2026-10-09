# 6GR 用户面架构

**当前进展** · 阶段：—

_尚无综述_

## 6GR 演进

### [6G/Rel-20 RAN2#134] `agreement` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

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

```text
UDC is a cost-effective and mature feature that aligns with 6G’s core requirements: IMS service support including TN/NTN, UE power saving, and uplink coverage enhancement. UDC constitutes a necessary feature for 6G Day‑1 deployment.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-o001`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
NR’s PDCP reordering framework can lead to non-deterministic reordering delays for PDUs in the receiver, which can vary between one and two reordering timer periods.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-o002`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
5G PDCP reordering mechanism causes high Rx memory requirements at DL peak throughput and lacks ability to adapt to QoE.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-o003`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
During handover, if L2 retransmission is integrated into RLC, complex and tight interactions between DU and CU-UP should be required and many issues are expected, but there may be no issue if all L2 retransmission are integrated into the PDCP.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-o004`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
Fast ARQ with a HARQ failure indication cannot justify L2 retransmission integrated into RLC.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-o005`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
PDCP retransmissions and RLC ARQ have different triggers and purposes.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-o006`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
If the PDCP layer and the RLC layer are merged into a single layer in 6GR, one status report would be naturally supported.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-o007`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
If the PDCP layer and the RLC layer remain separate layers in 6GR, whether and how to unify the two status reports can be further studied.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-o008`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

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

```text
L3 Congestion management ECN marking is supported in UEs and NWs today.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-o010`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
Congestion management is a per-flow operation. It is implemented at the header in IP layer since there is no other control signaling available between intermediate routers and source/destination of the flow. This is not the case for RAN.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-o011`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
Legacy AM and UM are designed for services with noticeable differences and with complete differences in aspects like window operation and PDU header format. No clear benefits and motivation of a unified RLC transmission mode have been identified yet.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-o012`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

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

```text
RAN2 to consider the following enhancements for reordering:
Combining in-order delivery and out-of-order delivery;
Enhancing PDCP reordering procedure.
Noted
R2-2602938	Discussion on functionalities for upper user plane	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-p004`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

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

```text
Do not support unified L2 retransmission: Keep PDCP and RLC retransmissions separate.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-p006`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
Support only RLC status report for PDCP and RLC retransmission for AM DRB.
R2-2603345	Discussion on functionality for Upper User Plane and related functional requirements	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-p007`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
All L2 retransmission mechanisms are integrated into PDCP for common L2 retransmission functionality.
R2-2603550	Discussion on common L2 retransmissions	Philips International B.V.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-p008`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
PDCP retransmissions and RLC ARQ are separate procedures in 6GR.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-p009`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
A unified L2 status report is supported in 6GR.
Congestion Management & Packet Discarding
R2-2603854	Consideration on 6GR UP Functioanlities	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-p010`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
Support UL rate control mechanism introduced in R19 as the baseline for congestion control mechanism from AS point of view and study DL rate control in 6G. Ask SA2 whether L4S could be supported in 6G.
R2-2602938	Discussion on functionalities for upper user plane	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-p011`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
For congestion management, RAN2 focuses on solutions that do not introduce per-packet overhead. Control signaling to indicate flow congestion can be further studied to assess performance benefits.
Data transfer modes
R2-2603232	6G upper user plane functionalities	Ericsson	discussion	Rel-20	FS_6G_Radio
Proposal 5	Study common framework in 6G RLC for AM and UM operation, where retransmissions may be triggered based on FARQ or polled RLC status reporting, if configured.
R2-2602946	Considerations on User Plane functionalities	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-p012`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
Legacy AM and UM can be as baseline of 6G data transfer modes. Further enhancements to AM or UM can be studied case by case.
R2-2603586	Upper UP functionalities and requirements	Nokia	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.1-p013`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

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

```text
In the 5G NR mechanism, a single CB or CBG is not considered reliable and cannot be delivered to the MAC layer independently without successful TB CRC verification.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-o001`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.4 Other UP functionality

```text
The PHY layer HOL blocking issue could be partially solved by enabling delivery of CBs/CBGs passing CB-level CRC verification to MAC, i.e., CBs/CBGs before an error CB/CBG will not be blocked.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-o002`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.4 Other UP functionality

```text
From RAN2’s perspective, a solution to completely solve the PHY layer HOL blocking issue requires MAC to recognize the boundary of MAC subPDUs within each delivered CB/CBG.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-o003`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.4 Other UP functionality

```text
Whether TB-level CRC verification can be removed/ignored and whether CBG will be retained in 6G should be checked with RAN1.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-o004`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.4 Other UP functionality

```text
The current 5G NR approach for preparing and forwarding MAC subPDUs does not allow for early forwarding of control or data subPDUs. This results in significant latency in HARQ retransmission scenarios, when the relevant CB has already been decoded correctly.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-o005`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.4 Other UP functionality

```text
Early forwarding of MAC CEs and/or other control messages is not related to the PDCP HOL blocking issue.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-o006`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.4 Other UP functionality

```text
ARQ is only beneficial for AM mode PDUs. So, FARQ should be applied only for AM mode PDUs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-o007`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.4 Other UP functionality

```text
FARQ may benefit some of the MAC CEs which are included in the TB, however, not all MAC CEs need this and some MAC CE content may need to be reconstructed before retransmission.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-o008`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.4 Other UP functionality

```text
Type 3 (Intra-DRB HOL blocking of PDCP control PDU by PDCP data PDU at RLC Tx side) has not been an issue in 5G, as UE implementation can always prioritize transmission of PDCP control PDU. Whether it is an issue in 6G can be further confirmed based on single SN discussions.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-o009`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.4 Other UP functionality

```text
Most Type 4 (Inter-DRB HOL blocking of PDCP control PDU by PDCP data PDU at RLC Tx side) can be handled by proper NW configuration. The special case that needs RAN2 attention is when Bj<0 in the MAC LCP procedure, gating PDCP/RLC control information from being transmitted.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-o010`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.4 Other UP functionality

```text
Type 4 HOL blocking issue may not need to be resolved as L2 control/data PDU of high priority LCH should always have higher priority than L2 data/control PDU of low priority LCH.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-o011`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.4 Other UP functionality

```text
Send LS to RAN1 to inquire about the necessity and feasibility of delivering successfully decoded CBs or CBGs to the MAC layer regardless of the result of TB CRC verification.
Noted
R2-2602950	Considerations on faster ARQ retransmission and HOL blocking issues	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-p001`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.4 Other UP functionality

```text
Send an LS to RAN1 to clarify the lower layer HOL blocking issue. Ask RAN1 if it is possible to deliver the successfully decoded CB/CBG (passing CB-level CRC verification) to MAC layer.
Noted
R2-2603463	Other UP functionalities	Nokia	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-p002`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.4 Other UP functionality

```text
Study the benefits of early forwarding for various payload types: MAC CEs, Other control messages, User Data; and if such forwarding shall be “always on” (for all TBs) or “opportunistic” (for some TBs when deemed beneficial)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-p003`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.4 Other UP functionality

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

```text
HARQ status indication could be applied for RLC UM.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-p005`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.4 Other UP functionality

```text
When UL HARQ process status of NACK is received, MAC entity re-triggers MAC CE and RLC entity re-triggers RLC control PDU if included in the corresponding MAC PDU.
R2-2603052	Fast ARQ and other 6G UP enhancements	ZTE Corporation, Sanechips	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-p006`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.4 Other UP functionality

```text
For the MAC SDUs in a MAC PDU, fast ARQ is applicable only to AM mode SDUs – handling of MAC CEs in the TB is FFS (left to stage 3).
R2-2603753	Transmitter behaviour on fast ARQ trigger	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-p007`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.4 Other UP functionality

```text
Upon FARQ NACK indication, data in the uplink HARQ buffer from AM-like bearers configured with other constraints (e.g. delay budgets) are only considered for retransmission if those constraints are met.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-p008`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.4 Other UP functionality

```text
Data considered for FARQ retransmission is not subject to any specific prioritisation except those defined for LCP.
[15 min]
Higher layer HOL
R2-2602942	Discussion on other UP functionalities	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-p009`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.4 Other UP functionality

```text
For Tx HOL Blocking between control and data PDUs, RAN2 observes the following:
-	Type 3 Intra-DRB HOL Blocking can be fully handled by UE implementation. In 5G, there are no instances of type 3 HOL Blocking causing any issues in the field.
-	For Type 4 Inter-DRB HOL Blocking, RAN2 to study the blocking of PDCP and RLC control PDUs when the LCP causes Bj<0 for a long time, causing stalling and throughput reduction for this DRB.
Noted
R2-2603040	Discussion on FARQ and HOL blocking issue	Xiaomi	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-p010`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.4 Other UP functionality

```text
RAN2 to deprioritize the study of type 4 HOL blocking issue at higher layer.
Noted
R2-2603858	Consideration on 6GR HoL Blocking and Fast ARQ	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.4-p011`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.4 Other UP functionality

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

```text
A potential robustness issue for separate layer design is observed that fake PDCP PDUs may update RLC variables deliberately and block authentic packets to be processed later.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o001`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
The duplicated functions, such as re-ordering, window maintenance, status report and SDU discard, can be designed in a more efficient manner by merging PDCP and RLC.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o002`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
In merged layer, fake PDUs could be idenfitied by security function and will not update ARQ state and SN status variables deliberately. Authentic packets can still be processed when received later.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o003`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
RAN2 should study the issue of single sequence numbers for the following scenarios:
Scenario 1: Assuming no CU-DU split (or equivalent) and no Dual Connectivity.
Scenario 2: Assuming CU-DU split (or equivalent) and no Dual Connectivity.
Scenario 3: Assuming CU-DU split (or equivalent) and possible Dual Connectivity, e.g., for FR1/FR2 non-collocated deployments discussed by RANP.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o004`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
Repeating the common SN in the RLC header is redundant and increases both overhead and header processing complexity.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o005`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
Field data shows that the issue of truncation of RLC Status PDU is common for NACK-carrying RLC status PDUs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o006`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
Up to Rel-18, RLC for DRBs operated in two modes: 1) RLC UM: Minimized latency with no reliability guarantees at RLC level. 2) RLC AM: Operates at a 100% reliability with unbounded RLC latency (except for PDCP discard timer).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o007`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
RLC segmentation creates a bottleneck of processing both at transmitter and receiver. The transmitter cannot apply pre-processing. The receiver gets blocked at reassembly.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o008`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
RLC segmentation does not add any benefit at high data rates as TBs can already carry hundreds of IP packets in one piece.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o009`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
RLC segmentation is only needed for low data rate links
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o010`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
Mapping multiple QoS flows/ traffic flows to a single DRB may cause HOL blocking due to PDCP reordering.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o011`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
The static PDCP reordering mechanism is not suitable for service characteristics with dynamic QoS.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o012`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
5G PDCP reordering mechanism causes high Rx memory requirements at DL peak throughput and lacks ability to adapt to QoE.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o013`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
5G static PDCP discard timer mechanism leads to the following issues:
-	Per-packet discard timer leads to discarding of application bursts without considering if this leads to improvement of degradation of QoE.
-	Single Static timer that does not adapt to path latency variations provide a very coarse tool for controlling application delay.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o014`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
AS layer enhancements to support AQM discarding mechanism should be justified over existing SDU discard mechanism. Discussion on potential ECN enhancements depends on RAN3 discussion on CU-DU split.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o015`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
In NR, multiple compression mechanisms (ROHC, UDC, EHC) were introduced independently, but those are all compression mechanisms which have commonalities.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o016`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
UDC is a cost-effective and mature feature that aligns with 6G’s core requirements, including IMS service support, TN/NTN convergence, UE power saving, and uplink coverage enhancement. UDC constitutes a necessary feature for 6G Day‑1 deployment.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-o017`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
RAN2 to further investigate a single sequence numbering functionality on the basis of merging the PDCP and RLC layers into one layer. Otherwise, two sub-layers with two separate SNs will be retained.
Noted
R2-2601463	Discussion on functionalities for upper user plane	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p001`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
For SN-dependent functionalities, (Re)segmentation/reassembly and ARQ should be performed by RLC due to their real-time low-latency requirements.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p002`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

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

```text
RAN2 to handle the issue of PDCP control PDU under the single SN by the following:
Option 1: Assign PDCP SNs for PDCP control PDUs and trigger SN gap report to indicate discard of PDCP control PDUs;
Option 2: Assign separate PDCP SN to PDCP control PDUs;
Option 3: Transmit the control PDUs on SRB.
R2-2601723	Considerations on single SN framework	Samsung	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p005`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

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

```text
PDCP entity assigns SN, and PDCP header includes SN.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p007`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
RLC performs (re-)segmentation and ARQ by using the PDCP SN included in the PDCP header.
R2-2601991	Single SN and other upper L2 functionality	InterDigital	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p008`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
Regardless of the layer modelling, the header structure and the SN allocation mechanism should be common to functions exploiting the SN.
L2 re-transmissions
R2-2601829	Views on 6G User Plane: L2 Functionalities	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p009`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
Regardless of whether PDCP and RLC should be merged into one single layer, L2 retransmission functionality across different layers (for L2 ARQ and RRC procedures) can be integrated into a single functionality.
Noted
R2-2602041	Further Discussion of upper User Plane Functionalities	Lenovo	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p010`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

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

```text
RAN2 consider one non-transparent RLC mode for 6G, where retransmissions and acknowledgements are configurable with a common framework for RLC AM and UM.
Noted
R2-2601463	Discussion on functionalities for upper user plane	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p012`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

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

```text
RAN2 to study an atomic RLC mode, where RLC segmentation is disabled and IP packets are only delivered in one piece.
Not treated
Reordering
R2-2601906	Discussion on 6G UP Functions	CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p014`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
RAN2 to consider the following enhancements for reordering:
Combining in-order delivery and out-of-order delivery;
Adjusting PDCP reordering procedure based on service requirements dynamically.
R2-2601463	Discussion on functionalities for upper user plane	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p015`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
RAN2 to study how to enhance PDCP reordering in 6G to achieve the following goals, if possible:
Adapt to application QoE needs
Reduce memory usage at high DL throughput
Support multiple flows in a DRB with different reordering requirements
R2-2602041	Further Discussion of upper User Plane Functionalities	Lenovo	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p016`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

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

```text
RAN2 to study how to enhance PDCP/RLC discarding mechanisms in 6G to achieve the following goals, if possible
-	Adapt to application QoE and path latency variations in determining what to discard.
-	Support multiple flows in a DRB with different discard requirements.
R2-2601498	Discussion on upper user plane functionalities	Xiaomi	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p018`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
6G UP supports the timer based SDU discard.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p019`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

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

```text
RAN2 to consider SCHC as a candidate for a PDCP compression mechanism and study RAN2 impact of supporting SCHC in the 6G Study
R2-2602289	Header Compression Functionality in 6G	Orange, Ericsson, Nokia, T-Mobile USA, Turkcell, Deutsche Telekom	discussion	Rel-20	FS_6G_Radio
Observation 1	In NR, multiple compression mechanisms co-exist, i.e., ROHC, UDC, EHC, yet not all use case scenarios are covered, in particular mMTC uses, which are expected in 6G.
Proposal 1	Regarding PDCP compression framework, RAN2 considers SCHC, ROHC, UDC, and EHC mechanisms as complementary and is considering including them in 6G SI.
R2-2601577	Discussion on Upper User Plane Functionality	Sharp	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p021`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

```text
RAN2 to study a unified compression framework including ROHC, UDC, and EHC.
R2-2601906	Discussion on 6G UP Functions	CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.1-p022`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.1 Functionality for Upper User Plane and related functional requirements

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

```text
With NR’s design, data is required to remain in the RLC buffer for the RLC RTT period (>30ms), despite successful transmission of >90% of this data.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o001`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

```text
If the ACK is provided in the DCI upon HARQ process success, it would be robust to misinterpretation and can be relied upon to clear the L2 buffer.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o002`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

```text
With an ACK provided in the DCI upon HARQ process success, there is a 60-80% reduction in L2 buffer needs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o003`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

```text
The memory requirement reduction based on ACK signalling can be effectively had for free.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o004`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

```text
Explicit HARQ ACK via DCI enables the UE to prevent redundant retransmissions and ensures the reliable delivery of MAC CEs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o005`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

```text
If the ACK indicated by the UE is designed to be robust to misinterpretation, it can be used by the aNB to clear its L2 buffers leading to 60-80% reduction in aNB’s L2 buffer needs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o006`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

```text
For DL, the network is free to terminate an existing HARQ process and move to an immediate ARQ like retransmission at any point in time. For UL, this is not feasible.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o007`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

```text
HARQ-assisted DL ARQ has the potential of significantly reducing latency without increasing RLC retransmission rate.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o008`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

```text
The motivation for NACK-To-ACK/DTX-to-ACK error detection mechanism is DL RLC latency which is in RAN2 scope. The exact mechanism can be studied by RAN1.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o009`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

```text
One challenge with N2A/DTX2A error detection and reporting in DL is minimizing redundant reporting based on HARQ terminations not caused by PUCCH errors.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o010`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

```text
In DL, PUCCH errors and missed DCIs lead to residual HARQ errors, requiring an RLC retransmission at NW.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o011`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

```text
There are mainly four types of HOL blocking issue at higher layer:
Type 1 (Inter SDF intra DRB HOL blocking at PDCP Rx window);
Type 2 (Intra/Inter-SDF intra-DRB HOL blocking at RLC Tx side);
Type 3 (Intra-DRB HOL blocking of PDCP control PDU by PDCP data PDU at RLC Tx side);
Type 4 (Inter DRB HOL blocking between control PDU and data PDU at Tx side).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o012`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

```text
Simulation results show that Type 1/2 HOL blocking issue may result in 80% more delay for web page downloading.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o013`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

```text
5G radio bearer setup/release procedure cannot adapt to the application's dynamic and massive short TCP/QUIC connections in a scalable, dynamic, efficient and flexible manner.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o014`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

```text
HOL Blocking at PDCP transmitter can be adequately handled by UE/NW implementation. Some QoS-related HOL blocking can happen at RLC between Tx and ReTx buffers.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o015`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

```text
Head-of-line blocking in PDCP Rx happens when a missing SDU causes other SDUs to be held in the Rx buffer even if they belong to a different QoS flow or otherwise do not need to be delivered after the missing SDU.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o016`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

```text
For Rx HOL blocking issue, there is no advantage is supporting a single DRB with multiple Sequence Number spaces (for reordering) over multiple DRBs with a single Sequence Number space from a protocol or hardware standpoint.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o017`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

```text
With the potential large TB sizes in 6G, delivering successfully decoded portions of TB would offer performance benefits.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o018`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

```text
In the 5G NR mechanism, a single CB or CBG is not considered reliable and cannot be delivered to the MAC layer independently without successful TB CRC verification.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o019`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

```text
The PHY layer HOL blocking issue could be partially solved by enabling delivery of CBs/CBGs passing CB-level CRC verification to MAC, i.e., CBs/CBGs before an error CB/CBG will not be blocked.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o020`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

```text
From RAN2’s perspective, a solution to completely solve the PHY layer HOL blocking issue requires MAC to recognize the boundary of MAC subPDUs within each delivered CB/CBG.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o021`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

```text
Whether TB-level CRC verification can be removed and whether CBG will be retained in 6G should be checked with RAN1.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o022`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

```text
The current 5G NR approach for preparing and forwarding MAC subPDUs does not allow for early forwarding of control or data subPDUs. This results in significant latency in HARQ retransmission scenarios, when the relevant CB has already been decoded correctly.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o023`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.4 Other UP functionality

```text
Early forwarding of MAC CEs and/or other control messages is not related to the PDCP HOL blocking issue.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-o024`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

```text
From RAN2 point of view, for clearing L2 buffers in UL, an explicit indication in DCI is preferred for a given HARQ process success. It is up to RAN1 how this is signalled.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p001`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

```text
Upon reception of HARQ process success indication, the UE can clear corresponding data from the uplink L2 buffer.  The UE is not expected to continue HARQ retransmissions after this indication is received.
-	Mediatek and ZTE explain that the intention was that the ACK would be sent when the NDI is toggled rather than for every transmission.
Noted
R2-2601661	Other UP functionality in 6G	Samsung, Verizon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p002`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

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

```text
Explicit HARQ ACK is useful.
Noted
R2-2601625	Discussion on fast ARQ and HOL blockage issue	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
Observation 1-1:	UL HARQ process status of ACK is useful for fast update of the transmitting window.
Observation 1-2:	UL HARQ process status of ACK does not need to be sent for every TB and could be piggybacked when the transmission is successful and network wants to schedule the next TB on the same HARQ process with toggled NDI.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p004`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

```text
UL HARQ process status of ACK could also be supported.
DL FARQ
R2-2602599	On HARQ triggered L2 retransmissions	MediaTek Inc., T-Mobile USA	discussion	Rel-20	FS_6G_Radio	R2-2602304
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p005`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

```text
Uplink HARQ feedback for downlink data is designed to be as robust to misinterpretation as uplink data transmission.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p006`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

```text
RAN2 to send an LS to RAN1 to provide them with our design requirements to enable uplink and downlink FARQ.
Noted
R2-2601715	Other UP functionality	Nokia	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p007`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

```text
For DL fast ARQ, RAN2 discuss how to enable fast detection of NACK-to-ACK error.
Noted
R2-2601779	Fast ARQ and other 6G UP enhancements	ZTE Corporation, Sanechips	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p008`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

```text
For DL, FARQ is already feasible and is up to gNB implementation and improvements for NACK to ACK errors for HARQ feedback can be left to RAN1 study
Noted
R2-2601467	Discussion on other UP functionalities	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p009`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

```text
RAN2 to discuss the following issues based on N2A/DTX2A error detection (depending on confirmation and further guidance from RAN1)
-	UE behaviour upon N2A/DTX2A error detection, e.g., early termination of t-reassembly, New MAC CE report, etc.
-	How redundant UE reporting can be minimized.
Noted
R2-2602042	Discussion on fast ARQ support and HOL blocking	Lenovo	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p010`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

```text
RAN2 to agree on supporting fast ARQ retransmissions for DL based on UE assistance information, e.g. indication to abort further HARQ Retx(s) and trigger RLC re(tx).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p011`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

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

```text
When UL HARQ process status of NACK is received, MAC entity re-triggers MAC CE in the corresponding MAC PDU and RLC entity retriggers RLC control PDU in the corresponding MAC PDU.
R2-2601661	Other UP functionality in 6G	Samsung, Verizon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p013`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

```text
For the MAC PDU of unsuccessfully terminated uplink HARQ process, RAN2 to further discuss the retransmission, in terms of:
the MAC CE(s) included in the MAC PDU
the control PDU(s) such as status report included in the MAC PDU
R2-2601833	Views on 6G User Plane: Fast ARQ and HoL Blocking	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p014`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

```text
When NACK is received for a HARQ process, the transmitter should only trigger L2 retransmission for SDUs from AM radio bearer(s) that are multiplexed in the corresponding TB.
Higher layer HOL blocking
R2-2601503	Discussion on HOL blocking issue	Xiaomi, MediaTek Inc., CMCC, Sony	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p015`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

```text
RAN2 prioritizes the study of type 1 and 2 HOL blocking issue at higher layer.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p016`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

```text
The study of type 1/2 HOL blocking issue should take into account the following characteristics of applications' traffic:
A large amount of concurrent, dynamic and short-lived TCP/QUIC connections, e.g. more than 100;
Very diverse IP addresses targeting diverse servers, even third-party servers.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p017`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

```text
The solution to type 1/2 HOL blocking issue should take into account the scalability, latency, signalling overhead and flexibility.
Noted
R2-2601769	Discussion on L2 retransmission enhancements and HOL blocking issue	1Finity	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p018`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

```text
To address the higher layer HOL blocking issue, QoS flow awareness in PDCP layer is supported by the following options:
Option 1: Use in-band signaling, i.e., QFI is included in the header of PDCP Data PDU.
Option 2: One PDCP entity can split into multiple RLC bearers to carry different QoS flows or QoS flow groups.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p019`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

```text
RAN2 to study the following approaches for avoiding HOL blocking at receiver:
Option 1: Receiving PDCP entity maintains different queues for different QoS flows or QoS flow groups.
Option 2: QoS flows in a DRB can be configured with different in-order delivery requirements.
Noted
R2-2601467	Discussion on other UP functionalities	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p020`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

```text
HOL blocking solutions should not introduce multiple PDCP sequence number spaces within the DRB.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p021`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

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

```text
Send LS to RAN1 to inquire about the necessity and feasibility of delivering successfully decoded CBs or CBGs to the MAC layer regardless of the result of TB CRC verification.
R2-2601448	Considerations on faster ARQ retransmission and HOL blocking issues	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p023`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

```text
Send an LS to RAN1 to clarify the lower layer HOL blocking issue. Ask RAN1 if it is possible to deliver the successfully decoded CB/CBG (passing CB-level CRC verification) to MAC layer.
R2-2601995	Fast ARQ and HoL blocking	InterDigital	discussion	Rel-20	FS_6G_Radio
Observation 3.2-5: Multiplexing data on a per CB basis would potentially result to extensive segmentation and header overhead of upper layer data and is, hence, not feasible approach.
Observation 3.2-6: With CB based data decoding, the fast ARQ procedure could not be supported without unnecessary re-transmissions of already decoded data in case the HARQ feedback granularity is not increased.
Observation 3.2-7: The encoding of upper layer data should be on basis of a finite number of CB groups of a large TB for which the HARQ feedback could be individually provided.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p024`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

```text
From RAN2 perspective, being able to deliver completely/successfully received PDUs to upper layers from a not completely received TB can be beneficial if the transmitter can be immediately made aware of this.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p025`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

```text
Successful decoding of a group of CBs from a not completely received TB needs to be indicated to the transmitter to avoid unnecessary re-transmissions.
R2-2602407	Disscussion on faster ARQ retransmission and HOL blocking	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p026`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

```text
For lower layer solution for HOL blocking issue, RAN2 should wait and postpone further discussion until RAN1 completes the CB/CBG level design.
R2-2601715	Other UP functionality	Nokia	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p027`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

```text
Study the benefits of early forwarding for various payload types: MAC CEs, Other control messages, User Data
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.4-p028`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.4 Other UP functionality

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

```text
Study HOL blocking issues.   Study should address both higher layer (e.g. QoS related) and lower layer (e.g. MAC, CB) mechanism and both RX/TX.   Companies can bring evaluations and explain assumptions, etc.
Functionality of SDAP layer
R2-2601033	Discussion on SDAP	NTT DOCOMO INC.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-a002`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

```text
Both PDCP and RLC have their own SNs because they serve different functional purposes at different protocol layers.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o001`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

```text
NR RACH procedures are complicated due to 1/ redundancy caused by separate procedures defined for different RACH type; 2/ resource selection complexity introduced by RACH partitioning; 3/ complicated checks for RACH fallback.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o002`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

```text
2step RACH offers clear benefits for lowlatency connection setup and smalldata transmission.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o003`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

```text
Mitigation mechanisms for RA overload should be considered on top of the RACH partitioning framework.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o004`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

```text
RACH resource adaptation does not need to be limited to additional RACH resources and can be applied to any RACH resources configured in 6G.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o005`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

```text
It would be beneficial to study the possibility of supporting a larger Msg3/MsgA size to enable faster and more appropriate initial setup in 6G.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o006`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

```text
In NR, early indication of feature combinations by RACH partitioning leads to very inefficient use of RACH resources and overly complex signaling.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o007`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

```text
In NR, RACH resources do not adapt well to short-term variations in access load, often resulting in high level of contention and access failures.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o008`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

```text
HOL blocking issue at AS layer may be caused by the following reasons:
-	Multiple traffics are mapped to the same DRB and they are handled by the same queue;
-	Traffics from different DRBs are multiplexed in the same TB, the traffics mapped to the failed decoded CBs will block the delivery of traffics mapped to the successfully decoded CBs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o009`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

```text
The HOL blocking issue of one service flow to other service flows in the same DRB cannot be resolved by existing solution of mapping service flows to different DRBs, as it is not scalable, flexible, and results in high latency and high signalling overhead.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o010`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

```text
In NR, failure of a single code block (CB) can delay the delivery of PDUs in other CBs. This problem can be more critical in 6G with its much larger TBs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o011`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

```text
Including metadata about MAC CEs or MAC subPDUs at a start of a TB can help the receiver speed up processing of the TB.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o012`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

```text
The SDAP layer in NR requires operational effort to ensure proper data forwarding during handover and does not guarantee in-order delivery when QoS flow remapping occurs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o013`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

```text
The SDAP Rmap and RQoS mechanism in NR increases the user plane processing overhead and latency.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o014`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

```text
QFI marking is a simple function and can be merged into other protocol layer.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o015`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

```text
Reflective QoS is not efficient in 6GR.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o016`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

```text
RAN2 to study how to enhance PDCP/RLC discarding mechanisms in 6G to achieve the following goals, if possible
-	Per-packet discard timer leads to discarding of application bursts without considering if this leads to improvement of degradation of QoE;
-	Single Static timer that does not adapt to path latency variations provide a very coarse tool for controlling application delay.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-o017`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1 User plane

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

```text
RAN2 to study details of the single layer 2 SN, e.g. which protocol assigns the SN and which protocol header carries the SN in the header. Handling of control PDUs is FFS.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p001`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

```text
RAN2 to study potential L2 protocol simplification by considering a common retransmission mechanism at L2 covering RLC ARQ and PDCP retransmissions.
[2 min]
Noted
R2-2600591	Considerations on a single SN	Samsung	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p002`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

```text
For a single SN study, the PDCP sequence number is utilized as the single SN.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p003`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

```text
For a single SN study, if the RLC layer is present, it will refer to the SN field in the PDCP header and treat it as the SN in the RLC layer.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p004`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

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

```text
RAN2 to further discuss the following two issues: 1) How to handle PDCP control PDU and 2) How to address SN gap for the single SN mechanism
[2 min]
Not treated
Random Access procedure
R2-2600622	UP functionalities and requirements	Nokia	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p006`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

```text
Design a unified Random Access procedure which minimizes the need of RA partitioning, and study, together with RAN1, possible issues with RA PUSCH payload size.
[2 min]
Noted
R2-2600207	Discussion on the 6G user plane features	OPPO	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p007`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

```text
For 6G, RAN2 to support a unified and simplified RACH framework considering:
	Unified 2-step RACH and 4-step RACH.
	Unified RAR format.
	Simplified RACH partition.
	Simplified fallback procedure.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p008`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

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

```text
Study how to support scalable early indication mechanisms for diverse device types/features during random access procedure.
[2 min]
R2-2600139	Discussion on 6G user plane functionalities	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p011`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

```text
Study RACH designs that enable more efficient use of resources, e.g. explore methods to avoid RACH partitions unless truly necessary, dynamic or on-demand allocation of RACH resources, etc.
[2 min]
Head-of-line blocking and CB/CBG based data handling
R2-2600101	Discussion on HOL blocking issue	Xiaomi, MediaTek Inc., Huawei, HiSilicon, CMCC, Sony	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p012`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

```text
RAN2 agrees to study solutions to the HOL blocking from one service flow to other service flows in the same DRB, taking into account the scalability, latency, signalling overhead and flexibility.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p013`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

```text
RAN2 agrees to study solutions to the HOL blocking from failed decoded CBs to successfully decoded CBs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p014`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

```text
For the HOL block from one service flow to other service flows in the same DRB, to allow scalable, low latency, low signalling overhead and flexible solution, RAN2 considers to study the following directions:
- Scalability: reduce the cost/processing per queue;
- Latency: allow UE/BS dynamical queue setup/release;
- Signalling overhead: reduce the signalling overhead per queue;
- Flexibility: allow dynamical adjustment of queue properties (e.g. priority, bit rate).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p015`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

```text
For the HOL blocking from failed decoded CBs to successfully decoded CBs, RAN2 considers to study solution to allow delivery of successfully decoded CBs/CBGs to upper layer.
[3 min]
Noted
R2-2600139	Discussion on 6G user plane functionalities	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p016`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

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

```text
RAN2 studies whether SDAP sublayer can be merged to PDCP sublayer, i.e., PDCP can support mapping between QoS Flow and DRB, coordinating with other WGs.
[2 min]
Noted
R2-2600658	Discussion on 6G user plane functionality	Spreadtrum, UNISOC	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p018`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

```text
RAN2 to study:  1) Removing RQoS and Rmap mechanism and SDAP; 2) Moving QFI marking to other protocol layers, e.g., PDCP; 3) QoS flow to DRB mapping is specified in stage2 spec.
[2 min]
Noted
R2-2600348	Functional requirements on 6GR User plane	Fujitsu	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1-p019`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1 User plane

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

```text
Real-time mobile AI traffic has similar traffic characteristics as the traffic models developed for XR applications:
-	Periodic but has highly variable burst size;
-	Has strict delay requirement.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o001`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

```text
Non-real-time mobile AI traffic shares similar characteristics with legacy eMBB traffic, but also possess the following distinct features:
-	Aperiodic, bursty, with higher UL load;
-	Use HTTP and TCP/QUIC;
-	Has more short-lived connections than other mobile apps;
-	Has a flexible delay budget, but latency is critical to user experience.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o002`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

```text
Uplink traffic is considered for both R20 mobile AI service and the results of the study could be reused for 6G. The downlink AI traffic could be further analyzed in the 6G discussion.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o003`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

```text
The non-real-time uplink mobile AI traffic relies on reliable transport such as TCP or QUIC/UDP.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o004`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

```text
Unlike traditional uplink traffic transmission (e.g., FTP upload), mobile AI services are predominantly interactive, meaning that the latency directly affects user experience.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o005`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

```text
Interactive AI, Agentic AI and immersive traffic including real-time communication for conversational XR introduce challenging traffic patterns (uplink bursty, delay-sensitive, and of varying bitrate, latency, data arrival time and inter-burst time interval) from a system efficiency perspective.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o006`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

```text
Traffic associated with interactive AI-based services is predominantly uplink-heavy and latency-sensitive, with data sessions characterized by periodic and/or irregular UL data bursts exhibiting variable payload sizes and inter-burst intervals.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o007`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

```text
Interactive real-time services with AI assistance generate delay-critical uplink data bursts, for which bounded latency and high reliability are key performance requirements.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o008`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

```text
Efficient support for delay-critical UL bursts with low, determistic latency should be a priority.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o009`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

```text
Transmission characteristics of AI traffic include burst and non-periodic traffic patterns, multi-modality for diverse data types, enhanced reliability, and strict end-to-end latency and round-trip time requirements.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o010`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

```text
Mobile AI traffic exhibits strong heterogeneity and multi-modalities and cannot be characterized by a single or static traffic model.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o011`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

```text
Existing RAN mechanisms and QoS handling for Rel-18 and Rel-19 XR traffic may not efficiently support uplink-heavy and multi-modal AI traffic.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o012`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

```text
The rapid evolution of AI applications and transport protocols leads to unpredictable and frequently changing AI traffic patterns.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o013`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

```text
Agentic AI traffic requires sustained connectivity with predictable latency and reliability, which limits UE opportunities to save power.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o014`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

```text
Mobile AI services increasingly operate across heterogeneous multi-devices associated with the same user, rather than being confined to a single UE.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o015`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

```text
Existing system assumptions and traffic models are largely UE-centric and do not fully capture the characteristics and requirements of multi-device AI services.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o016`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

```text
6G mobile AI focuses on the  AI-native communication mechanisms,  including token communication by tokenizer localized deployment, using tokens as the minimum transmission unit and directly connecting to downstream AI application processing AI traffic. Another type is the AI source compression traffic service based on AI codec, e.g. Grace in TR 22.870.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o017`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

```text
Chatbot, as a 5G-A R20 AI traffic, typically use very short data packet sizes, including both data packets and ACK packets.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o018`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

```text
GenAI services as provided in the TR 22.870 are QoS-dynamic and delay-sensitive. The data burst may arrive periodically or a-periodically with high data rate and varying volumes.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o019`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

```text
The evaluation results given in this contribution and [3][4] show the following features for the (tokenized) AI codec traffic:
	Error-tolerance: Not all tokens need to be transmitted correctly.
	Importance: Different tokens have different transmission reliability requirement (e.g. token error rate)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o020`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

```text
RAN#110 agreed that RAN is to “ensure that any work on AI traffic characteristics in the RAN domain takes place in one place only (led by RAN2) to avoid fragmentation and duplication with feedback from SA4 on AI traffic characteristics”.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o021`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

```text
Tokenized AI communication introduces unique complexities. Proceeding without the foundational media framework from SA4 could lead to a fragmented design that fails to properly account for how these source files are decomposed.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o022`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

```text
It is not clear whether tokenized AI traffic and non-tokenized AI traffic have different traffic characteristics.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o023`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

```text
Mobile AI traffic spans multiple service types including conversational interactions, agentic/task-execution workflows, etc. Within conversational services, interactions may be realized across multiple modalities, namely, text, image, and video. Among these, text-based conversational LLM (chatbot-style) traffic is currently the most prevalent.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o024`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

```text
It is a non-trivial task to develop a traffic model that faithfully captures conversational, multi-turn GenAI traffic while keeping the complexity at a reasonably low level.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o025`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

```text
A traffic model for conversational GenAI traffic should be consistent with existing 3GPP traffic models, leveraging established statistical methods to represent key characteristics such as packet inter-arrival times and packet/burst sizes.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o026`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

```text
To facilitate a faithful and practical implementation, it is desirable for the model to be unidirectional while keeping the opposite direction in consideration, i.e., configurable to generate traffic separately for UL or DL flows.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o027`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.0 Mobile AI transmission characteristics

```text
Existing 3GPP traffic models, e.g. FTP models and XR model do not capture the bursty, multi-turn interaction pattern of conversational GenAI traffic.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-o028`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

```text
RAN2 confirm that mobile AI traffic can be broadly categorized into two types:
-	Real-time, e.g. conversational audio, augmented reality, etc;
-	Non-real-time, e.g. exchange of objects such as text, image, audio/video clips, etc between UE and server.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p001`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

```text
RAN2 adopt the traffic models developed for XR as the baseline for real-time mobile AI traffic.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p002`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

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

```text
Confirm the following traffic characteristics for R20 mobile AI discussion, which could also be applicable for 6G AI traffic discussion:
(a)	Focus on the uplink traffic for the non-real-time mobile AI service
(b)	Application layer packet for mobile AI could be fragmented to multiple packets and arrive in the AS buffer in multiple batches
(c)	Mobile AI service is interactive service with latency requirements
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p004`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

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

```text
UL data burst size could be considered as a new traffic characteristic, e.g. reporting from UE to RAN node, for Mobile AI in Rel-20 and 6GR study.
-	Oppo asks why is the burst so important.  Vivo thinks it is related to user experience.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p007`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

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

```text
The 5G-Advanced Rel-20 XR should focus on enhancements for uplink mobile AI traffic, in particular by enabling AI-traffic awareness in RAN.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p010`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

```text
The 6G QoS should support flexible and adaptive QoS handling to efficiently accommodate new and evolving AI traffic and protocol behaviors.
[3 min]
Not treated
Tokenized traffic
R2-2600965	Discussion on AI traffic for R20 6G and 5G-A	CMCC, OPPO, Huawei, HiSilicon, Fujitsu	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p011`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

```text
We can confirm with SA4 (and possibly SA1) about the above ob2 to ob5.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p012`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

```text
RAN2 should study the potential characteristics of TokenCom traffic such as error tolerance, differential importance, and context relevance, which may involve technical optimization of RAN2 by awareness of these characteristics (e.g., Packet/PDU Set/PDU level Importance Indication or error tolerant mapping to QoS).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p013`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

```text
If RAN2 can establish conclusions regarding token communication's potential features such as error tolerance, differential importance, and context relevance, we may inquire with SA4 whether these align with their research in TR 26.847, along with RAN2's considerations and implications.
[3 min]
R2-2600446	Views on 6G User Plane: Mobile AI Traffic Characteristics	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p014`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

```text
RAN2 can de-prioritize the study on tokenized traffic, until SA4 provides more feedback related to AI traffic models.
[2 min]
R2-2600206	AI traffic characteristics and coordination between RAN2 and SA4	OPPO, China Telecom, China Unicom, CSCN, CMCC, Huawei, HiSilicon, HONOR, Ofinno, NEC, Transsion Holdings	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p015`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

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

```text
RAN2 waits for SA4 progress/reply to conclude its study on media aspects for 6G before starting RAN2 discussions on tokenized traffic.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p017`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

```text
RAN2 asks SA4 whether a tokenized mobile AI traffic has a different traffic pattern from non-token-based mobile AI traffic.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p018`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

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

```text
Consider text-based conversational GenAI traffic model as a starting point for 6G AI/ML mobile traffic evaluations
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p020`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

```text
Define a conversational GenAI model for mobile AI traffic in a unidirectional UL/DL form, where UL and DL traffic profiles are specified separately but governed by a shared session/turn process
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p021`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

```text
The conversational GenAI model is parameterized with the following parameters: mean turns/session, mean think time, prompt size distribution, response size distribution, first-byte delay distribution, and streaming chunk/cadence parameters.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p022`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

```text
Default statistical distribution families, e.g., geometric, exponential, shifted lognormal/lognormal with truncation, are used for baseline evaluations of conversational GenAI model, with parameters left configurable.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.0-p023`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.0 Mobile AI transmission characteristics

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

```text
In DL, PUCCH errors and missed DCIs contribute to DL RLC errors requiring UE to correct using an RLC Status report, triggering an RLC retransmission at gNB.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-o001`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.4 Others

```text
HARQ-assisted DL ARQ has the potential of significantly reducing latency without increasing RLC retransmission rate.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-o002`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.4 Others

```text
Once RRC-configured,Type 1 CG cannot be dynamically modified, deactivated or re-activated without RRC reconfiguration
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-o003`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.4 Others

```text
Type 2 CG cannot be automatically activated upon RRC configuration and relies on the explicit DCI-based activation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-o004`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.4 Others

```text
Due to the SR delay and the CG Confirmation MAC CE, Type 2 CG adjustments are not sufficiently time-effective for dynamic, bursty traffic.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-o005`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

```text
For triggering the faster ARQ procedure in UL, the gNB includes a one-bit indication in the DCI for UL grant when NDI is toggled for the HARQ process.
[2 mins]
Noted
R2-2600246	Discussion on L2 Retransmission and CG	CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p001`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

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

```text
Upon receiving information about the unsuccessful termination of an UL HARQ process, UE triggers RLC retransmission of RLC SDU(s)/RLC SDU segment(s) included in the MAC PDU associated with the HARQ process.
[3 mins]
R2-2600167	MAC layer enhancements for 6G	ZTE Corporation, Sanechips	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p004`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

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

```text
RAN2 agree to have faster DL ARQ retransmissions at the transmitter side based on HARQ process status.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p007`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

```text
For DL data transmission, HARQ process status from UE to RAN node is beneficial when potential HARQ feedback error is detected by UE, i.e., in case of HARQ new transmission scheduling is received on certain HARQ process after HARQ NACK was sent in PUCCH.
[2 mins]
Noted
R2-2600428	Discussion on HARQ/ARQ protocol design 	Lenovo	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p008`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

```text
RAN2 to agree on supporting mechanisms for fast triggered ARQ retransmissions at the transmitter side for DL based on HARQ feedback information (ACK/NACK) and UE assistance information, e.g. indication to abort further HARQ Retx(s) and trigger RLC re(tx).
[2 mins]
Noted
R2-2600142	Discussion on HARQ, ARQ and RLC	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p009`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

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

```text
For DL HARQ process, faster ARQ retransmission can be performed based on UL HARQ feedback. The details can be left to network implementation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p011`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

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

```text
For configured grant, consider both NR CG Type 1 and Type 2 as the starting point.
[2 mins]
Noted
R2-2600368	Other aspects of UP design	Nokia	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p013`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

```text
Study a unified CG framework that allows pre-configuration, activation/deactivation and modification.
[2 mins]
Noted
R2-2600078	Considerations on faster ARQ retransmission and CG scheduling	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p014`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

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

```text
Adaptive configured grant resource allocation mechanism should be studied to better adapt the pre-allocated resources to UL service requirement based on the new mixed traffic model agreed in RAN1.
[2 mins]
R2-2600450	Views on 6G User Plane: HARQ-ARQ Coordination, LCP and CG	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p016`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

```text
For configured grant in 6GR, Rel-16 version of CG may be considered as the baseline, where multiple CG configurations can be configured per serving cell.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p017`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

```text
RAN2 can study to see if CG can be made more efficient, e.g. the CG may operate in an “on-demand” basis.
[2 mins]
R2-2600962	Considerations on fast ARQ and CG for 6GR UP	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p018`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

```text
RAN2 should study the Type-2 CG fast adjustment to address the mitigate caused by SR and CG confirmation MAC CE.
[2 mins]
R2-2600656	6G HARQ/ARQ and CG	NEC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.4-p019`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.4 Others

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

```text
Most of NR UP functions are considered essential to connect between upper layers above L2 and physical layer.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o001`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.1 Functionality for User Plane and related functional requirements

```text
NR UP protocol stack has multiple sets of duplicated functions.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o002`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.1 Functionality for User Plane and related functional requirements

```text
Considering the service types will be supported by 6GR, radio bearer and logical channel could still be helpful to fulfil the specific requirements like latency, error recovery, etc.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o003`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.1 Functionality for User Plane and related functional requirements

```text
In NR, multiple compression mechanisms, i.e., ROHC, UDC, EHC. ROHC were introduced independently, but those are all compression mechanisms which have commonalities.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o004`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.1 Functionality for User Plane and related functional requirements

```text
In 5G, the MAC-I generated for each PDCP SDU causes extra signalling overheads and UE processing capability (i.e. impacting the UE’s transmission bit rate).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o005`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.1 Functionality for User Plane and related functional requirements

```text
Data concatenation can lead to variable-sized headers with varying bit positions that are not hardware-processing friendly.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o006`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.1 Functionality for User Plane and related functional requirements

```text
Data concatenation can lead to increased segment handling and reassembly delays
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o007`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.1 Functionality for User Plane and related functional requirements

```text
Same SN used for both ARQ & (re-)segmentation functions and security & re-ordering functions is beneficial for L2 overhead reduction and efficiency improvement.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o008`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.1 Functionality for User Plane and related functional requirements

```text
In NR, failure of a single code block (CB) can delay the delivery of PDUs in other CBs. This problem can be more serious in 6G with its much larger TBs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o009`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.1 Functionality for User Plane and related functional requirements

```text
Including metadata about MAC CEs or MAC subPDUs in a TB can help the receiver speed up processing of the TB.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o010`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.1 Functionality for User Plane and related functional requirements

```text
MAC CEs in 6G can be designed in a more structured way to enable efficient processing and meet the stricter timing requirements expected in 6G.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o011`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.1 Functionality for User Plane and related functional requirements

```text
NR UP headers are variable size especially in MAC and RLC which is not hardware-friendly.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o012`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.1 Functionality for User Plane and related functional requirements

```text
The factors that cause the header length to change dynamically are as follows: the presence or absence of segmentation in RLC, and the LCID and L field in MAC.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o013`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.1 Functionality for User Plane and related functional requirements

```text
A simple way to unify header lengths is to always adopt the longer header; however, this should be avoided as it would increase the size of messages such as Message 3, which are coverage bottlenecks.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o014`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.1 Functionality for User Plane and related functional requirements

```text
In NR, early indication of feature combinations through RACH partitioning leads to very inefficient use of RACH resources.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o015`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.1 Functionality for User Plane and related functional requirements

```text
In NR, RACH resources do not adapt well to short-term variations in access load, often resulting in high level of contention and access failures.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-o016`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

```text
6GR shall support the following functionality in a higher layer(s) in UP protocol stack:
-	Mapping between QoS flows (or sub flows if/as designed by SA2) to a radio bearer in UL and DL
-	Security protection, Sequence numbering of data PDUs, ROHC Header and Data compression, and timer-based discard for delayed PDUs
-	Header compression should be parked based on plenary and data compression is UDC and it is not commercialized.    Maybe there are some compression for those.  ZTE thinks that data compression can also be applicable to DL.  Also it doesn’t mean we need to enable this for everything.
-	Duplicate detection and discard
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p001`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

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

```text
Multiple PDCP SDUs can be concatenated to a single PDCP PDU.
[2 min]
-	Xiaomi asks what specific service you are targeting and wonders if this is hardware friendly and the UE has to predict the grant.   Oppo is referring to many small packets so we have to consider the overhead of MAC-I.  The UE doesn’t need to predict anything and the number of packets to be concatenated can be pre-configured.  Qualcomm ask then does it mean that it will be concatenated and then segmented.   MEdiatek thinks that this is a big problem, latency performance, memory buffer requirements etc.
Noted
R2-2508124	On essential functionality for 6G data transfer	MediaTek UK	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p006`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

```text
As in NR, the unit of data handling in the 6G user plane stack remains at a per-packet granularity.
[2 min]
Noted
R2-2508310	UP functionalities and requirements	Nokia, Nokia Shanghai Bell	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p007`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

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

```text
RAN2 to investigate joint sequence numbering in order to improve L2 transmission efficiency in 6G.
[2 min]
-	Xiaomi asks if this depends on PDCP and RLC being combined.  Vivo thinks that it would be easier but we can study.
Noted
R2-2508381	Views on 6G User Plane: Functionalities and Processing	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p009`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

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

```text
Study new MAC PDU formats (e.g. independent CBs, including metadata about MAC CEs or MAC subPDUs in a TB) that can enable faster processing at receiver.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p011`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

```text
MAC CEs in 6G should be designed to be a flexible and versatile signalling mechanism for various purposes, while remaining easy to process and assemble.
[2 min]
R2-2508217	6GR User Plane Functionality	Sharp	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p012`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

```text
For hardware-friendly processing, 6GR UP protocol pursues fixed size header for each upper layer SDU.
[2 min]
R2-2508796	On user plane functionalities for 6G	NTT DOCOMO INC.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p013`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

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

```text
Design a unified Random Access procedure which minimizes the need of RA partitioning, and study, together with RAN1, possible issues with RA PUSCH payload size.
[2 min]
R2-2508032	Discussion on 6G user plane functionalities	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p015`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

```text
Study RACH designs that enable more efficient use of resources, e.g. avoid RACH partitions unless truly necessary, dynamic or on-demand allocation of RACH resources, etc.
[2 min]
R2-2508641	L2 requirements and functions	InterDigital	discussion	Rel-20	FS_6G_Radio
Observation 2.3.5.1-1: NR RA procedure became complex due to additions of new features in later releases of NR while there was a need to retain backwards compatibility with the legacy UEs.
Observation 2.3.5.1-2: Preamble partitioning should not be generally used as an easy tool for all types of early indication but allocated only for functions strictly requiring it, like coverage enhancements.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p016`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

```text
6GR RA procedure supports both 2-step and 4-step RA procedures as well as coverage enhancement from the beginning.
Reflective QoS:
R2-2508823	Discussions on 6G UP Functionalities and Requirements	Futurewei	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p017`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

```text
Reflective QoS is not to be considered for 6GR.
R2-2508310	UP functionalities and requirements	Nokia, Nokia Shanghai Bell	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p018`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

```text
(Re)mapping of QoS flow to RB with the use of End-Marker is retained in 6G while the necessity of Reflective QoS remains in 6G is further discussed.
[2 min]
R2-2508320	6G User plane functionality and requirements	ZTE Corporation, Sanechips	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.1-p019`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.1 Functionality for User Plane and related functional requirements

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

