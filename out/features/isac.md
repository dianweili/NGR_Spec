# ISAC 通感一体

**当前进展** · 阶段：—

_尚无综述_

## 6GR 演进

### [6G/Rel-20 RAN2#134] `agreement` 9.5 ISAC

```text
1	From RAN2 perspective, study both UEs and TRPs operating as TX and/or RX Ses across all modes
2	Further study what radio aspects/configuration/report, control aspects (and what is controlled) are done by SF/aNB
3	For SE selection need to further understand the criteria, which nodes (UE, aNB, SF) need to be involved, and what information is required to perform the selection and how aNB and SF coordinate.   Consider sensing entity selection/re-selection in the case of moving target mobility in this study.
4	Study service continuity in the case of UE sensing entity moving
RRC states – if time allows
R2-2603273	On ISAC procedures, protocols, etc.	Apple Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.5-a001`

### [6G/Rel-20 RAN2#134] `proposal` 9.5 ISAC

```text
Support both UEs and TRPs operating as Tx and/or Rx SEs.
Noted
R2-2602961	Discussion on RAN2 ISAC in 6G	vivo, CAICT	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.5-p001`

### [6G/Rel-20 RAN2#134] `proposal` 9.5 ISAC

```text
From the perspective of UE roles, a UE can be a sensing signal transmitter and/or sensing signal receiver according to the sensing mode.  The study of sensing procedures can be categorized into the following:
UE as sensing signal transmitter
UE as sensing signal receiver
Noted
Sensing mode prioritization
R2-2604084	Discussion on ISAC Aspects from RAN2 Perspective	CEWiT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.5-p002`

### [6G/Rel-20 RAN2#134] `proposal` 9.5 ISAC

```text
RAN2 should structure the study of UE-involved sensing in the following order of priority:
UE as sensing Rx: UE measurements of DL sensing reference signals (TRP-UE DL bistatic)
UE as sensing Tx: UE transmission of UL sensing reference signals (UE-TRP UL bistatic)
UE-to-UE sensing: UE transmit/receive for UE-UE bistatic and UE monostatic scenarios.
Noted
R2-2603216	Discussion on wireless sensing	OPPO	discussion	Rel-20
RAN2 should avoid prioritizing bi-static over mono-static sensing in the initial stage of the ISAC study, as the fundamental UE functionalities (transmission and reception of reference signals) are procedurally similar from an L2 perspective.
Noted
Discussion
-	Xiaomi doesn’t think we need to prioritize.   Mediatek would like to have a harmonized solutions.
SF location and functions
R2-2603117	Initial views on 6G ISAC study	Samsung	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.5-p003`

### [6G/Rel-20 RAN2#134] `proposal` 9.5 ISAC

```text
Sensing protocol design should serve the sensing procedure, and consider at least the following issues which may need inputs from RAN3 and SA2:
What function(s) is needed in RAN and Sensing Function (SF) respectively to support the sensing procedure;
Where the SF entity locates, in CN or in RAN
Noted
R2-2604122	Comparing RRC and LPP alike for Sensing Procedure	Ericsson, Bell Mobility	discussion	Rel-20
Proposal 1	The Sensing Function is a Network Function located in Core Network.
Noted
R2-2603259	Protocols and procedures for sensing	MediaTek Inc.	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.5-p004`

### [6G/Rel-20 RAN2#134] `proposal` 9.5 ISAC

```text
The sensing function controls the sensing service procedures (including reception/measurement configuration for an Rx SE), and the serving aNB controls the radio resource allocation to a Tx UE SE.
Noted
R2-2603190	Procedures and Protocol Aspects for Sensing	Qualcomm Incorporated	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.5-p005`

### [6G/Rel-20 RAN2#134] `proposal` 9.5 ISAC

```text
The Rx and Tx Sensing Entities (i.e., UEs and/or TRPs) participating in a sensing session are selected and controlled by the Sensing Function (SF).
Noted
Discussion
-	Xiaomi explains that for 5G the roles of SF connectivity with sensing entity including UE and TRP, service sensing information/configuration, and data transport.   Ericsson thinks that in 5G there is no UE involvement.
-	Interdigital thikns that we need to have a radio part that will terminate in aNB and a service part that can be in serving function.  Some thinks like measurements are not clear where they would be.
-	Qualcomm thinks termination is more relate to transport.
-	CMCC and Opp thinks that data transfer should be in aNB for latency purposes.
-	Ericsson thinks that SA2 is discussing the sensing selection from the registered UE but the final selectin should be done aNB as there are other considerations.
-	Apple agrees that there will be some service related functions that go to SF and some radio resource that go aNB.   There will be cases where SF selects but there are cases where the UE selects itself.   We should keep in mind sensing assisted communications.   Xiaomi and interdigital thinks that we should first focus on how to support service function.
-	ATT also thinks that sensing selection should be in aNB as it doesn’t have all information.
-	KPN thinks that there are some cases that there are some cases that SF happens in SF but in some cases aNB needs to be involved.
-	Interdigital thinks that we need to discuss how the selection is done first
-	Xiaomi thinks that we need to have SF do the sensing data processing.
-	Huawei thinks we need to better understand what is configuration and for selection the aNB should make a final decision
-	Nokia thinks that one node triggers and selects the selection but the entities need to coordinate.
-	Vodafone asks if we can do sensing in idle mode, and we should restrict to RRC connected mode.  MEdiatek thinks we should not restrict for connected mode.  Xiaomi thinks that there are two scenarios.
-	Qualcomm thinks that SF has to do the final check based on many information.  If the gNB wants to use the sensing service the aNB already includes the UEs that can participate in the sensing.
UE capability framework
R2-2603900	Discussion on procedures and protocol aspects for ISAC	Spreadtrum, UNISOC	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.5-p006`

### [6G/Rel-20 RAN2#134] `proposal` 9.5 ISAC

```text
Discuss whether the UE ISAC capability reporting can reuse the unified 6G UE capability framework
R2-2603986	Discussion on ISAC	HONOR	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.5-p007`

### [6G/Rel-20 RAN2#134] `proposal` 9.5 ISAC

```text
RAN2 may first identify the basic ISAC UE capabilities (e.g., sensing modes, reporting levels, etc.) based on the outcomes of 5G-Advanced, and further extend the UE capabilities in line with the ongoing 6G discussions
R2-2604059	Views on 6G ISAC	NTT DOCOMO INC.	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.5-p008`

### [6G/Rel-20 RAN2#134] `proposal` 9.5 ISAC

```text
RAN2 to study UE sensing capability reporting procedures to enable the network to determine whether a UE can participate in sensing-related procedures, while avoiding binding UE capability reporting directly to specific sensing modes or service models.
Capability reporting
R2-2602971	Considerations for 6G ISAC in RAN2	Xiaomi	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.5-p009`

### [6G/Rel-20 RAN2#134] `proposal` 9.5 ISAC

```text
For the UE capability reporting procedure, the UE shall report both higher-layer sensing capabilities (e.g., supported sensing modes, calculation capabilities) and AS-layer sensing capabilities (e.g., RS-related capabilities) to the SF. The UE shall also report AS-layer sensing capabilities to the RAN as part of the UE AS capability.
R2-2603929	Discussion on 6G ISAC	ZTE Corporation, Beijing Digital Nebula, Sanechips	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.5-p010`

### [6G/Rel-20 RAN2#134] `proposal` 9.5 ISAC

```text
UE sends the sensing capability to serving aNB using Uu interface. SF can retrieve UE sensing capability via the aNB or AMF, if needed.
Sensing configuration protocol
R2-2603273	On ISAC procedures, protocols, etc.	Apple Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.5-p011`

### [6G/Rel-20 RAN2#134] `proposal` 9.5 ISAC

```text
RAN2 to study UE-SF interactions with LPP-like protocol to allow e.g. sensing configuration signalling.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.5-p012`

### [6G/Rel-20 RAN2#134] `proposal` 9.5 ISAC

```text
RAN2 to study UE-gNB interactions with RRC signalling to allow e.g. RAN to dynamically adapt sensing configurations to the dynamic radio conditions.
Noted
R2-2603187	Discussion on 6G ISAC	NEC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.5-p013`

### [6G/Rel-20 RAN2#134] `proposal` 9.5 ISAC

```text
RAN2 to study how sensing configurations are configured/activated, modified, or deactivated/released through RRC signaling or higher-layer application protocols.
Noted
R2-2603563	Discussion for ISAC in 6G	Lenovo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.5-p014`

### [6G/Rel-20 RAN2#134] `proposal` 9.5 ISAC

```text
The sensing configuration is transmitted from SenF/RAN node to sensing UE by a request or unsolicited way, and can be transmitted by broadcast signalling or dedicated to the sensing UE.
Noted
Discussion
-	Xiaomi thinks that for sensing assisted communication RAN1 agreed to study an option that data goes to the gNB.   Ericsson thinks that the plenary has agreed to have sensing assisted communication but we should strive for a common protocol that works for both communication and sensing.
-	Qualcomm thinks that the main point is who is the consumer of the sensing of the data and we will have transport mechanisms to carry.
-	Vivo UE as Rx entity (this needs to be further discussed and UE Tx entity (configuration is mainly about the UL reference signal)
-	CMCC thinks that we need RRC protocol for data processing.   ZTE thinks we should first understand why we need a new protocol, RRC can do this.  We can’t get rid of RRC no matter what, even if we have a new protocol.   Xiaomi explains that the consumer can be UE, SF, AF.  The SF needs to stay involved.  CATT thinks that we can rely on RRC.
-	Huawei thinks that we need to wait for RAN1 what data is being carried.
-	Xiaomi explains that there is cooperative sensing and there needs to be a SF.
-	CeWit thinks that we need to understand who does the processing and results calculated.
-	LG thinks that we need to consider the two cases.
-	Kyocera thinks that we should discuss broadcast and dedicated
-	Nokia thinks what are the content and the termination points and then we can talk the protocol.
Sensing configuration contents
R2-2603654	Discussion on RAN2 aspects of sensing	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.5-p015`

### [6G/Rel-20 RAN2#134] `proposal` 9.5 ISAC

```text
Sensing configuration is provided by the aNB, including:
Configuration of sensing resources, sensing signals, etc.
Configuration of measurement data report, e.g., content, triggering conditions.
Measurement and reporting
R2-2603563	Discussion for ISAC in 6G	Lenovo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.5-p016`

### [6G/Rel-20 RAN2#134] `proposal` 9.5 ISAC

```text
RAN2 to discuss whether to use 6G RRC measurement framework for sensing measurement, or to design LPP-like sensing measurement framework.
R2-2603098	Sensing functionalities and procedures	CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.5-p017`

### [6G/Rel-20 RAN2#134] `proposal` 9.5 ISAC

```text
The UE transmits the sensing measurement data to aNB and it is visible at aNB. How the sensing measurement data are processed at aNB and whether/how the sensing measurement data are forwarded to SF are in RAN3 scope.
R2-2603654	Discussion on RAN2 aspects of sensing	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.5-p018`

### [6G/Rel-20 RAN2#134] `proposal` 9.5 ISAC

```text
Regarding how to report sensing measurement data from UE to RAN, RAN2 should wait for the discussion in RAN1 on the measurement data content.
Sensing data transfer
R2-2602971	Considerations for 6G ISAC in RAN2	Xiaomi	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.5-p019`

### [6G/Rel-20 RAN2#134] `proposal` 9.5 ISAC

```text
For sensing data characteristics and termination point:
Data size: Depends on sensing version and the reported data (e.g., final results or intermediate results)
Latency: Less relaxed latency;
Termination point: SF;
Data Consumer: sensing service consumer (i.e., AF, UE, and NF);
Whether sensing report is transferred via CP, UP or data plane (if defined) depends on the size of sensing data and latency requirement.
Service continuity
R2-2603117	Initial views on 6G ISAC study	Samsung	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.5-p020`

### [6G/Rel-20 RAN2#134] `proposal` 9.5 ISAC

```text
For service continuity, RAN2 to study sensing continuity for a moving target and sensing continuity of a mobile sensing UE (consider both connected and idle/inactive UE).
Noted
R2-2603486	Discussion on Sensing Entity (Re)Selection	LG Electronics Inc.	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.5-p021`

### [6G/Rel-20 RAN2#134] `proposal` 9.5 ISAC

```text
Sensing Entity (re)selection is supported by UE capability reporting procedures, including reactive response and proactive unsolicited procedures, to ensure service continuity during the movement of Sensing Entities or sensing objects.
Noted
Discussion
-	Apple thinks sensing target mobility is an optimization but UE mobility is a based functionality.
-	Nokia thinks that we first need to a have a baseline.
-	CMCC and Xioami thinks that the moving target mobility is important.
-	MediaTek thinks that moving target mobility is really entity selection/reselection and the mobile sensing UE moving is continuity at service level.
-	Lenovo thinks we need to consider sensing mode change
-	ATT thinks that we should consider stationary UEs.
-	Nokia thinks that we should take into account whether location information can help.   Apple thinks that TRP location would also be great to have.   Ericsson points out that there are cases where there operator controlled SE UEs.
-	Huawei thinks that the SE UE mobility shouldn’t impact our 6G mobility mechanism design.   Xiaomi thinks that the SE UE mobility and measurements will not be impacted.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.5-p022`

### [6G/Rel-20 RAN2#134] `proposal` 9.5 ISAC

```text
RAN2 to study how ISAC procedures can be enabled in RRC_IDLE/INACTIVE (or their 6G equivalents), without prejudice to the final 6G RRC state model
R2-2603251	On 6G ISAC aspects	Nokia 	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.5-p023`

### [6G/Rel-20 RAN2#134] `proposal` 9.5 ISAC

```text
RAN2 assumes UEs involved in sensing procedures to be in RRC_CONNECTED state. Other UE (sub)states may be studied when sufficient progress is made on their definition as well as sensing procedures
R2-2603074	Discussion on ISAC in 6G	Sharp	discussion
paper not following proposal limit will not be treated
R2-2603313	RAN2 considerations for ISAC	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2603335	Discussion on ISAC	China Telecom	discussion	Rel-20	FS_6G_Radio
R2-2603385	Discussion on ISAC	Panasonic	discussion
R2-2603391	Discussion on ISAC for 6GR 	Tejas Networks Limited	discussion	Rel-20	FS_6G_Radio
R2-2603487	Uu Enhanced Procedures and Protocol for 6G ISAC	Hanbat National University	discussion
R2-2603628	Discussion on various aspects related to ISAC	Sony	discussion	Rel-20	FS_6G_Radio
R2-2603670	Procedures and protocol aspects for ISAC	InterDigital, Inc.	discussion	Rel-20	FS_6G_Radio
R2-2603679	Discussion on 6GR ISAC Framework	Google	discussion	Rel-20	FS_6G_Radio
R2-2603757	Characteristics of sensing entities and signaling framework in 6G ISAC	AT&T, FirstNet	discussion	FS_6G_Radio
R2-2603783	Views on ISAC	Fraunhofer IIS, Fraunhofer HHI	discussion	R2-2602302
R2-2603936	Discussion on RAN2 aspects of ISAC	China Unicom	discussion	Rel-20	FS_6G_Radio	Withdrawn
R2-2603938	Analysis of ISAC	Kyocera	discussion
R2-2603940	Discussion on RAN2 aspects of ISAC	China Unicom, UESTC, SUTD, Queen Mary University of London	discussion	Rel-20	FS_6G_Radio
R2-2603953	Discussion on ISAC for 6GR	CMCC	discussion	Rel-20	FS_6G_Radio
=> Revised in R2-2604180
R2-2604180	Discussion on ISAC for 6GR	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2604123	Procedures and Protocol Aspects for Sensing	KPN N.V.	discussion	Rel-20	FS_6G_Radio
R2-2604147	Discussions on 6G ISAC	ROBERT BOSCH GmbH	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.5-p024`

### [6G/Rel-20 RAN2#133bis] `agreement` 9.5 ISAC

```text
1	RAN2 can study what is required to support sensing functionalities/procedures assuming there will be a sensing function.  Where the sensing function is located is up to other WGs (e.g. SA2/RAN3).    Study can consider where the functionalities/procedures would need to be logically located.
2	Study at least the following RAN2 aspects:
UE capability reporting procedures,
Sensing configuration procedures
Sensing reporting procedures (e.g. measurements)
Transport of data/control signaling
Sensing Entity Selection (including re-selection)
Not treated
R2-2601544	General considerations on RAN2 6G ISAC	CATT	discussion	Rel-20	FS_6G_Radio
R2-2601707	Discussion on wireless sensing	OPPO	discussion	Rel-20	Late
R2-2601825	On sensing modes, protocols, and architecture	Apple Inc.	discussion	Rel-20	FS_6G_Radio
R2-2601899	Discussion on 6G ISAC	ZTE Corporation, Beijing Digital Nebula, Sanechips	discussion	Rel-20	FS_6G_Radio
R2-2601963	Discussion on 6G ISAC in Day 1	LG Electronics Inc.	discussion	Rel-20
R2-2601975	Discussion on ISAC	China Telecom	discussion	Rel-20	FS_6G_Radio
R2-2602047	Discussion on ISAC	Google	discussion	Rel-20	FS_6G_Radio
R2-2602054	Initial Considerations for 6GR ISAC Use Cases	Hanbat National University	discussion	Rel-20
R2-2602126	Discussion for ISAC in 6G	Lenovo	discussion	Rel-20
R2-2602169	Discussion on various aspects related to sensing	Sony	discussion	Rel-20	FS_6G_Radio
R2-2602302	Views on ISAC	Fraunhofer IIS, Fraunhofer HHI	discussion
R2-2602318	Sensing protocol(s) and procedures	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.5-a001`

### [6G/Rel-20 RAN2#133bis] `observation` 9.5 ISAC

```text
RAN has agreed that 6GR on ISAC at least supports use cases of detection and/or tracking of passive objects (at least including UAVs, human, vehicles and AGVs), and communication assistance.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.5-o001`

### [6G/Rel-20 RAN2#133bis] `observation` 9.5 ISAC

```text
Different sensing modes and interaction assumptions create different RAN2 impacts, especially once UE involvement is introduced.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.5-o002`

### [6G/Rel-20 RAN2#133bis] `observation` 9.5 ISAC

```text
The aNB monostatic and aNB-aNB bistatic sensing modes have no RAN2 impact.
Proposal 1a：The study of aNB monostatic and aNB-aNB bistatic sensing modes is left to other working groups. And the study of UE-UE bistatic and UE monostatic sensing modes is pending the progress of other working groups.
Noted
R2-2601615	On 6G ISAC	Nokia	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.5-o003`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.5 ISAC

```text
RAN2 study on ISAC aims at a generic procedure and protocol design that can accommodate all the supported sensing modes and meet the requirements of the supported use cases.
-	CMCC indicates that not all modes have UE impacts.   Docomo agrees.
-	Xiaomi thinks that even for other cases we may have some things that we can have the same design.
Noted
R2-2601527	Discussion on 6G ISAC higher layer procedures and protocols	T-Mobile USA Inc.	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.5-p001`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.5 ISAC

```text
RAN2 sensing technology protocols and procedures should enable a wide range of 6G sensing use cases, using TR 22.870 as a starting point. RAN2 should consider both outdoor and indoor deployments to address a wide range of potential use cases.
Noted
Sensing modes
R2-2602388	RAN2 ISAC Impacts	Ericsson, Verizon	discussion	Rel-20
Observation 2	RAN2 should do prioritization on which sensing modes should be studied first as it will be difficult to pursue all sensing modes at once.
Proposal 1	RAN2 studies UE-TRP, TRP-UE bistatic modes before pursuing UE to UE bistatic, UE monostatic sensing modes.
Noted
R2-2602170	RAN2 Scope and Considerations for 6G ISAC	Rakuten Mobile, Inc	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.5-p002`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.5 ISAC

```text
RAN2 identifies the first-phase sensing modes and interaction assumptions that introduce distinct RAN2 impacts, and prioritizes those as the starting point for the work.
Noted
R2-2601699	Discussion on RAN2 aspects of sensing	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.5-p003`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.5 ISAC

```text
For an initial 6G ISAC study, RAN2 prioritizes a baseline involving mono-static aNB sensing and an extension to bi-static aNB sensing. Sensing modes involving UEs are not precluded.
Noted
R2-2602236	Procedures and protocol aspects for ISAC	InterDigital	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.5-p004`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.5 ISAC

```text
The study should address the UE-involved sensing work in the following order:
1) UE measurements of DL sensing reference signals;
2) UE transmission for UL sensing reference signals; and
3) UE transmit/receive sensing signals for UE to UE scenario.
-	ZTE asks why is bullet 3 separate as it is covered by bullet 2 and why do we need an order.   Interdigital thinks that for 3 we’d focus on the difference like resource allocation and that would have to be done after we understand 1 and 2.  If we start with 1, we look at configuration, protocol, and validation of measurements and those things have less dependency.
Noted
R2-2601824	On UE-centric sensing	Apple Inc., MediaTek Inc., ASUSTek, OPPO, Google, vivo, Lenovo	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.5-p005`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.5 ISAC

```text
Define UE-centric sensing as a mode where the UE acts as the initiator of the sensing session, the sole Rx sensing entity, the sole processor of the sensing data to produce sensing results, and the sole final consumer of the sensing results. The UE and/or other sensing entities may transmit sensing signals.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.5-p006`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.5 ISAC

```text
Study UE-centric sensing operation mode, as applicable to UE monostatic, network-to-UE bistatic/multi-static and UE-to-UE bistatic/multi-static modes.
-	Ericsson asks what are the key questions that need to be answered.   Apple thinks that this implies that we need to support mono static and UE TRP bistatic to be supported, maybe it becomes a subset of UE based.
-	Tmobile is concerned about the network involvement.   Apple explains the network is in control about the resource usage, but we are just not reporting measurements to the network, it stays in UE.     Docomo also has the same concern.
-	ZTE thinks that this is not sensing mode it is a service type that should be studied in SA2 then RAN2 can discuss this after SA2.   Ericsson agrees.   Apple thinks that we have understand who process the results, in positioning it is called version.   ZTE thinks that is also SA2 scope and that is specified in SA2 as a service.  Xiaomi thinks who does the measurements/calculation is in RAN2.   Interdigital agrees it is service modelling and we are opening the door to not knowing where the measurements go also not clear if this can meet the KPIs.
-	Nokia thinks we should avoid these scenarios as we don’t know what and how it works so we should have some understanding on what to expect and request from other WGs.   See first what the network offers and then evolve.
Noted
Discussion
-	Xiaomi asks what would be different between TRP-UE and UE-to-UE as from protocol perspective it is the same.   Ericsson explains that some cases there procedures would be different in SA2 etc.
-	Interdigital thinks that the main thing to address is do the work in a certain order, we first need to find what is common in terms of procedures across use cases and coordination with other groups, whatever is related to UE selection, capabilities, configurations, measurements, protocol architecture and other aspects like transmission we need to wait for RAN1/RAN4.   Xiaomi agrees those are good procedures as a baseline.  Qualcomm thinks that we should first start with architecture.   Samsung thinks that we can look at the procedures in common.
-	Qualcomm the main difference is whether we have monostatic or bi-static and we should consider the different modes to enable them with a common framework.  RAN3 was involved in stage 3 work.
-	Mediatek thinks that it is not productive to talk about sensing modes, but rather about procedures like in interdigital proposal.
-	Xiaomi thinks that we should think of RAN2 impacts.
-	Oppo doesn’t think we can exclude monostatic.
-	CMCC thinks that we should prioritize but we have some dependencies where the SF is located
-	Apple thinks that we can either do bottom up or bottom down and we shouldn’t make the same as SL.
-	Ericsson thinks that we should look at whether it is a RRC like procedure with configuration or something like LPP which is transparent to aNB.  Architecture is a big term which is also SA2 and RAN3 work.   Ericsson indicates that we did it for positioning but this is not the same.  Also we agree that we should start with DL and UL procedure and understand who is receiving.
Sensing architecture and protocol
R2-2601459	Discussion on RAN2 Scope and Cross-WG Dependencies for 6G ISAC	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.5-p007`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.5 ISAC

```text
As to the sensing architecture, RAN2 can assume that there is an SF (sensing function) in the core network responsible for sensing management and sensing data processing to facilitate the subsequent discussion. Whether the SF can be deployed in other nodes, e.g., RAN node, can be left to other WGs (e.g., RAN3).
Noted
R2-2601699	Discussion on RAN2 aspects of sensing	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.5-p008`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.5 ISAC

```text
The sensing architecture should be discussed in SA2 and RAN3 first.
Noted
R2-2601823	Procedures and Protocol Aspects for Sensing	Qualcomm Incorporated	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.5-p009`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.5 ISAC

```text
RAN2 should study an end‑to‑end (SF–UE) Sensing Protocol that is independent of the underlying transport layers.
Noted
Discussion
-	Mediatek agrees with Qualcomm and it is a UE terminated protocol so there is a lot of radio resource management so it does belong to RAN2.  The alternative would be like 3G positioning.
-	Ericsson thinks that we need to take care of the implementation complexity as positioning wasn’t implemented.   We should learn about our mistakes and how we can make things simpler.   CMCC thinks it can RAN based or LPP based.   CATT agrees.   Xiaomi thinks that positioning wasn’t supported because of LPP but rather because there was no use case, and anyways in 3G it was RRC based.
-	Mediatek Sensing function controls the sensing operation procedures and the base station controls the radio resource allocation to the UE sensing entity.
-	Ericsson thinks that we can assume that the SF is logically in the CN.  CMCC thinks in 5GA it is in RAN.  Xiaomi thinks it is a deployment decision.  Interdigitial doesn’t think it matters where it is located as long as it is a logical function and what needs to be visible to the RAN is what matters.
-	Oppo thinks that we need to understand the type of data characteristics to also understand where data needs to go.
Not treated
Sensing procedure
R2-2602364	Initial views on 6G ISAC study	Samsung	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.5-p010`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.5 ISAC

```text
Sensing procedure includes at least:
UE capability reporting,
Sensing assistance information transfer,
Sensing measurement and reporting configuration,
Sensing measurement reporting (i.e., sensing data transfer).
-	Apple would like to make sure that not all these procedures will be required at the end.
-	Qualcomm thinks that UE assistance includes reference signal configuration resources for transmitter and receiver.  This are UE requests.
Sensing information transfer
R2-2602456	Views on 6G ISAC	NTT DOCOMO	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.5-p011`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.5 ISAC

```text
RAN2 should define the initial ISAC/Sensing study scope to include UE sensing capability signalling, sensing configuration and activation procedures, and UE-to-network sensing data reporting.
R2-2602369	Sensing modes, Interaction models, and RAN2 Impact for 6G ISAC	AT&T	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.5-p012`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.5 ISAC

```text
RAN2 discusses whether existing RRC signaling procedures are sufficient to support sensing framework in terms of connection control, configuration management, resource management, UE capability signaling, and UE authorization
Not treated
Sensing configuration
R2-2601699	Discussion on RAN2 aspects of sensing	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.5-p013`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.5 ISAC

```text
Sensing configuration is provided by aNB, including
Configuration of sensing resources, sensing signals, etc.
Configuration of measurement data report, e.g., content, format, triggering conditions.
Not treated
Sensing entity selection
R2-2602089	Discussion on RAN2 considerations for ISAC in 6G	Tejas Network Limited	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.5-p014`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.5 ISAC

```text
RAN2 shall discuss internally and co-ordinate with SA2 and RAN3 for defining a generalized framework for sensing entity selection.
R2-2601515	Insight on 6G ISAC in RAN2	Xiaomi	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.5-p015`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.5 ISAC

```text
RAN2 confirms the below two assumptions of sensing service request and further study RAN2 impact:
Sensing service request for a UE, i.e., select a specific UE as sensing entity;
Sensing service request for an Area, i.e., sensing entity is selected based on sensing area.
Not treated
Sensing measurement and reporting
R2-2602333	Discussion on ISAC in 6G	Sharp Laboratories of America	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.5-p016`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.5 ISAC

```text
RAN2 to study whether existing mechanisms for configuration and measurement reporting are sufficient to support ISAC. Details FFS.
R2-2601727	Discussion on 6G ISAC	NEC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.5-p017`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.5 ISAC

```text
Study reusing communication measurement framework to accommodate ISAC-related measurements
R2-2602081	Discussion on ISAC	HONOR	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.5-p018`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.5 ISAC

```text
RAN2 could study the traffic characteristics of sensing data based on RAN1 simulation results and assumptions, evaluate the impact on scheduling mechanisms, and align with the ongoing 6G ISAC study in RAN1.
Service continuity
R2-2602434	Discussion on ISAC for 6GR	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.5-p019`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.5 ISAC

```text
For Service Continuity, both movement of sensing entity or/and sensing target should be considered.
-	Mediatek asks what impact CMCC sees.  CMCC and Qualcomm explains that when sensing target moves we need to re-select and then we also have sensing entity that can move.   ZTE is concerned if we have “and” as it would be complicated if they both move.
-	Interdigital thinks service continuity can be viewed as sensing entity selection.   CMCC thinks that the selection only considers Uu interface but we should also consider aNB interface.
-	Apple doesn’t like the word service continuity.
-	AT&T thinks that all sensing UEs are stationary so there is no need for this.  Nokia has similar concerns with mobility and should we make an assumption single cell mobility.    ZTE doesn’t thinks we can’t assume stationary and sensing requirement cannot be stationary.  Apple UEs are not stationary.
Noted
R2-2601869	Initial RAN2 considerations for ISAC	Ofinno	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.5-p020`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.5 ISAC

```text
To discuss the RRC states applicable for ISAC operation. 6G should at least support UEs in RRC_CONNECTED and study the feasibility of enabling ISAC in low power (sub)states (RRC IDLE, INACTIVE) to optimize UE energy efficiency.
Noted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.5-p021`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.1 Evaluations

```text
For Rel-20 6G ISAC performance evaluation, adopt the following minimum UE-UE (2D) distance evaluation assumption for baseline cases/configurations.
|  | Scenario | Minimum UE-UE (2D) distance |
| --- | --- | --- |
| Sensing UAV | UMa-AV | 1 m |
|  | SMa | 1 m |
| Sensing Human | UMa | 1 m |
|  | Indoor Hotspot (Indoor-office) | 1 m |
| Sensing Vehicle | Urban Grid | Determined by the agreed UE distribution |
|  | Highway | Determined by the agreed UE distribution |
| Sensing AGV | Indoor Factory (SH) | 1 m |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.1-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.1 Evaluations

```text
For Rel-20 6G ISAC performance evaluation, for baseline cases/combinations of sensing AGV in Indoor Factory (SH), the following parameters are assumed for clutters.
| Clutter density: | 20% |
| --- | --- |
| Clutter height: | 2 m |
| Clutter size: | 10 m |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.1-a002`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.1 Evaluations

```text
For Rel-20 6G ISAC performance evaluation, for object detection and/or tracking, the MDP (missed detection probability) and the FAP type 2 (false alarm probability type 2) are calculated as follows:
Missed detection probability
where,
-	 is the number of missed targets in the drop n, i.e., the true target not associated with any detected object.
-	 is the number of true targets in the drop n.
-	 is total number of drops with at least one target per drop.
FFS: same MDP definition as 5GA ISAC study should also be evaluated
False alarm probability Type-2
where,
-	 is the number of detected objects but not associated with any true targets in the drop n.
-	 is the total number of detected objects in the drop n.
-	 is number of drops with at least one detected object.
FFS: same FAP type-2 definition as 5GA ISAC study should also be evaluated
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.1-a003`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.1 Evaluations

```text
For Rel-20 6G ISAC performance evaluation, for object detection and/or tracking, when data fusion from multiple sensing nodes/pairs is applied:
Instead of using detected objects per sensing node/pair, the jointly determined object(s) fused from detected objects of multiple sensing nodes/pairs will be used for association between detected object(s) and true target(s), calculating MDP, FAP Type 2 and positioning/velocity accuracy.
Companies to report the method/algorithm to obtain the jointly fused object(s) from detected objects of multiple sensing nodes/pairs.
R1-2605743	Moderator summary #2 on ISAC evaluations	Moderator (CATT)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.1-a004`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.1 Evaluations

```text
For Rel-20 6G ISAC evaluation on SAC (sensing assisted communication), companies are encouraged to evaluate and report at least one of the following:
Scope 1: Evaluate performance of sensing measurement/result, which will be used to assist communication;
Scope 2: Evaluate performance of communication, with and without assistance of sensing measurement/result. The sensing measurement/result to assist communication can be:
Ideal sensing measurement/result
Non-ideal sensing measurement/result, and company to report how to model error/offset of non-ideal factors for non-ideal sensing measurement/result
Real sensing measurement/result, which is obtained from simulation
Note: companies to report which is used in their simulation.
For Rel-20 6G ISAC evaluation on SAC, for Scope 2:
The communication use case(s) in AI 10.8.2 are encouraged
Companies to report whether the location and/or velocity information of communication UE and/or TRP is needed or not in their SAC algorithm/mechanism
Note: this does not imply specifying exchange of location and/or velocity information between UE and TRP
Companies to report the time-frequency resource cost due to sensing for SAC and necessary details on the definition of the time-frequency resource cost based on TR38.765 as starting point
Comparison with benchmark and benchmark details should also be reported as well as other necessary details if any
Companies are encouraged to use communication-related performance metrics as agreed in communication agendas
Companies are encouraged to use baseline/benchmark mechanism as agreed in communication agendas for comparison; Use of state-of-the-art mechanism without assistance of sensing measurement/result for comparison is not precluded
Companies are encouraged to use additional communication-related evaluation assumptions (if necessary but not discussed/agreed in AI 10.8.1) as agreed in communication agendas
Note: How to draw conclusion/observation is a separate discussion.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.1-a005`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.1 Evaluations

```text
For Rel-20 6G ISAC evaluation on SAC, for Scope 1, the following sensing measurement/results and corresponding performance metrics are considered:
Delay/Doppler/angle/power/phase related information of the ISAC channel
Performance metric:
RMSE of delay of the path(s) used to assist communication
RMSE of Doppler the path(s) used to assist communication
RMSE of angles (one or more of AOD, ZOD, AOA, ZOA) of the path(s) used to assist communication
RMSE of power of the path(s) used to assist communication
FFS: details on the power of the path(s)
FFS: RMSE of phase of the path(s) used to assist communication
Companies to report how to select the path(s), how to derive RMSE from multiple paths and how such sensing measurement/result of the paths(s) is able to assist communication
Note: when evaluated, companies are not required to report every metric
Enrivonment (large surface, wall) that reconstructed by sensing
Performance metric:
Mean value of absolute perpendicular distance from the sensed specular reflection point to the ground-truth plane
Mean value of absolute perpendicular distance from the ground truth specular reflection point to the reconstructed plane
Note: when evaluated, companies are not required to report every metric
EO type-2 should be modeled in the simulation in this case
Companies are not required to evaluate and report every sensing measurement/result.
Note: In Scope 1, the performance metrics for detecting object for the purpose of SAC are the same as those for object detection and/or tracking, and thus already included in Rel-20 6G ISAC object detection and/or tracking study.
Note 2: How to draw conclusion/observation is a separate discussion.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.1-a006`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.1 Evaluations

```text
For Rel-20 6G ISAC evaluation on SAC, for evaluation assumptions, the evaluation assumptions of baseline cases/combinations of object detection and/or tracking are reused as starting point. In addition, one or more of the following adjustment may be considered:
Dropping of sensing target is optional
In case reconstruction of enrivonment (large surface, wall that modeled by EO type-2) is evaluated, additional sensing capable UEs can be dropped for reconstructing environment
Other adjustment is not precluded
Companies should report the adjustments (if any) with necessary details when reporting simulation results.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.1-a007`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.1 Evaluations

```text
Templates (excel files) in R1-2606863 are adopted to collect evaluation results of object detection and/or tracking in AI 10.8.1.
Additional tdoc file(s) will also be used to collect companies input in details, which may include but not limited to:
Details on sensing RS/resource
Details on method/algorithm for detection
Details on method/algorithm for tracking
Details on inter-site/intra-site interference modelling, if modelled
Details on method/algorithm to select sensing STx-SRx pair(s)
Details on method/algorithm to obtain the jointly fused object(s) from detected objects of multiple sensing nodes/pairs, if data fusion is applied
Details on the sensing capable UE dropping
Note: Further revision is not precluded, depending on future discussion
R1-2606863	Result collection templates for object detection and/or tracking		Moderator (CATT)
R1-2605744	Moderator summary #3 on ISAC evaluations	Moderator (CATT)
R1-2605745	Moderator summary #4 on ISAC evaluations	Moderator (CATT)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.1-a008`

### [6G/Rel-20 RAN1#126] `conclusion` 10.8.1 Evaluations

```text
No consensus to introduce UAV-UE as sensing capable UE in the baseline case/combination of sensing UAV in Rel-20.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.1-c001`

### [6G/Rel-20 RAN1#126] `conclusion` 10.8.1 Evaluations

```text
No consensus to remove CPE UE in Indoor-office (Indoor Hotspot) for the baseline case/combination of sensing Human in Rel-20.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.1-c002`

### [6G/Rel-20 RAN1#126] `conclusion` 10.8.1 Evaluations

```text
For Rel-20 6G ISAC performance evaluation, for baseline cases/combinations, it is clarified that ‘convex hull’ refers to ‘convex hull of the TRP deployment’ in Indoor Hotspot (Indoor office) and Indoor Factory evaluation assumptions.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.1-c003`

### [6G/Rel-20 RAN1#126] `conclusion` 10.8.1 Evaluations

```text
For Rel-20 6G ISAC performance evaluation of object detection and/or tracking, for baseline cases/combinations, it is clarified that the scenario Indoor Hotspot (Indoor-office) for sensing Human is ‘open office’, but not ‘mixed office’, as defined in TR 38.901.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.1-c004`

### [6G/Rel-20 RAN1#126] `conclusion` 10.8.1 Evaluations

```text
No consensus to remove CPE UE in Indoor Factory for the baseline case/combination of sensing AGV in Rel-20.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.1-c005`

### [6G/Rel-20 RAN1#126] `conclusion` 10.8.1 Evaluations

```text
No consensus to introduce AGV-UE as sensing capable UE in the baseline case/combination of sensing AGV in Rel-20.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.1-c006`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.2 Aspects of integration with communication

```text
In addition to theoretical characteristics analysis, companies are encouraged to do at least one of followings to evaluate RE pattern of sensing RS in 10.8.2
Full SLS with or without cooperative sensing as 10.8.1 (Option 1 from RAN1#125) for sensing performance evaluation
SLS with non-cooperative sensing (i.e., no fusion) (Option 2 from RAN1#125) at least for sensing measurement performance evaluation
LOS condition is always assumed for each STX-target-SRX link
Simplified SLS with single STX and single SRX (Option 3 from RAN1#125) at least for sensing measurement performance evaluation
LOS condition is always assumed for each STX-target-SRX link
Note: detailed modelling is up to company report
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.2-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.2 Aspects of integration with communication

```text
Study on a sensing RS resource consisting of one or multiple component RS.
Study the following options for component RS
Component RS can be RS for communication is reused for sensing
Component RS can be enhanced RS for sensing, taking reuse of RS for communication as starting point
Component RS can be dedicated RS for sensing
Note: The multiple component RS of a sensing RS resource can be of single or multiple RS types.
Companies to provide necessity, theoretical analysis, performance evaluation and specification impacts on the above options and the sensing RS resource in next RAN1 meetings.
Note: RE pattern of the sensing RS resource is union set of all REs of all component RS
FFS: details of component RS
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.2-a002`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.2 Aspects of integration with communication

```text
Study the following two options to generate a sensing RS resource
Option 1: A sensing RS resource has single antenna port, which can be precoded or non-precoded
Option 2: A sensing RS resource can have multiple antenna ports, which can be precoded or non-precoded
Companies to provide necessity, theoretical analysis, performance evaluation and specification impacts on the above options in next RAN1 meetings.
FFS impact on measurement reporting and assistance information
R1-2605587	Summary #3 on integration with communication for ISAC	Moderator (Xiaomi)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.2-a003`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.2 Aspects of integration with communication

```text
The following metrics for a path are to be studied in 6G ISAC
Delay information defined per path
Option 1: Receive time difference between a path and a reference path, e.g., RSTD like
Option 2: Receive time difference between a path and a reference time, e.g., RTOA like
FFS reference time
Option 3: Receive time of a path minus a transmission time, e.g., Rx-Tx time difference like
FFS transmission time
Doppler information defined per path
FFS absolute or relative/differential Doppler information
Angle information defined per path
FFS absolute or relative/differential angle information, implicit/indirect angle information
FFS how to derive angle
RSRP/SINR/amplitude/phase defined per path
FFS how to derive phase
Quality/uncertainty/confidence defined per path
FFS ambiguity handling of delay/Doppler/angle of a path
Further discuss the additional metrics for a path
Micro-Doppler
RCS
Association among paths
Other metrics are not precluded
FFS reference path
FFS definition of path
Note: the necessity, applicable sensing modes, achievable sensing performance, reporting aspects (e.g., overhead) of above metrics can be discussed separately
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.2-a004`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.2 Aspects of integration with communication

```text
The following metrics of a scattering point or an object are to be studied in 6G ISAC from RAN1 perspective
3D or 2D location
Option1: Absolute location
Option2: Relative location referred to a reference location
FFS reference location
3D or 2D velocity
Option1: Measured true 3D/2D velocity
Option2: Scalar of radial velocity
Uncertainty/confidence
association of measurements of a scattering point/object
FFS ambiguity handling of delay/Doppler/angle of a scattering point
Further discuss the additional metrics for a scattering point/object
Power related information if applicable, e.g., RCS
Micro-Doppler
Other metrics are not precluded
FFS definition of scattering point/object
Note: the necessity, applicable sensing modes, and achievable sensing performance, reporting aspects (e.g., overhead) of above metrics can be discussed separately
R1-2605588	Summary #4 on integration with communication for ISAC	Moderator (Xiaomi)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.2-a005`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.2 Aspects of integration with communication

```text
The metrics of consecutive samples in delay/Doppler/angle profiles are to be studied in 6G ISAC
FFS: whether/how to apply window(s) of consecutive samples in delay/Doppler/angle profile
Note: the necessity, applicable sensing modes, and achievable sensing performance, reporting aspects (e.g., overhead) of above metrics can be discussed separately
R1-2605589	Summary #5 on integration with communication for ISAC	Moderator (Xiaomi)
Final post-meeting summary for this agenda item.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.2-a006`

### [6G/Rel-20 RAN1#126] `conclusion` 10.8.2 Aspects of integration with communication

```text
On UE-side measurement report, measurement Level A from NR ISAC is not considered for 6G ISAC study in Rel-20.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.2-c001`

### [6G/Rel-20 RAN1#126] `working_assumption` 10.8.2 Aspects of integration with communication

```text
The following representative use cases for sensing assisted communication is/are selected for study in Rel-20 ISAC
Sensing assisted beam management
[Sensing assisted CSI acquisition and reporting]
Note: companies can also study other use cases for sensing assisted communication
Note: In AI10.8, physical layer design discussions are limited to sensing related aspects
R1-2605586	Summary #2 on integration with communication for ISAC	Moderator (Xiaomi)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.2-w001`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.3 Waveform and frame structure

```text
The following options are further studied for RS sequence enhancement for sensing based on ZC sequence based on CP-OFDM.
Opt. 1 ZC sequence optimization
Opt. 2 Frequency domain quadratic-phase RS sequence .
FFS: details of B, C, D
FFS: A as constant or whether/how to define A as function of m
Note: intention of A(m) here is different from FDSS
[Opt. 3 Time domain RS sequence generation based on transform precoding]
Opt. 4 Time domain spanning ZC sequence across OFDM symbols
RS sequence enhancement should identify:
the benefits/drawbacks based on comprehensive comparison with NR Gold sequence for TRP transmission and NR ZC sequence for UE transmission as benchmark for evaluation
applicability/necessity to TRP-transmission based sensing
applicability/necessity to UE-transmission based sensing
Discussion on the other solutions will continue.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.3-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.3 Waveform and frame structure

```text
The following options are further studied for RS enhancement for sensing based on Gold sequence based on CP-OFDM.
Gold sequence optimization (e.g., initialization)
Gold sequence modulated by pi/2 BPSK with transform precoding for UE transmission
Gold sequence modulated by pi/2 BPSK for CP-OFDM
Time domain spanning Gold sequence across OFDM symbols
RS sequence enhancement should identify:
the benefits/drawbacks based on comprehensive comparison with NR Gold sequence for TRP transmission and NR ZC sequence for UE transmission as benchmark for evaluation
applicability/necessity to TRP-transmission and/or UE-transmission based sensing
Other solutions are not precluded.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.3-a002`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.3 Waveform and frame structure

```text
For effective CP length extension for sensing, further study the necessity (including whether implementation based solution can solve the issue or not) and the following candidate solutions.
Transmission of successive N OFDM symbols that carries sensing RS
FFS: details of generation method
FFS: value N
Freq. domain comb pattern for sensing RS
FFS: details of generation method including comb size
FFS: combination of successive N OFDM symbols and freq. comb pattern
Time gap after/before/within OFDM symbol carrying sensing RS, without changing OFDM symbol duration/structure of 6GR communication design
FFS: location of the time gap
FFS: duration of the time gap
FFS: benefits/drawbacks/spec impact
FFS: applicable sensing mode and scenario
FFS: supported excess delay
FFS: other solutions are not precluded
R1-2606565	Summary #3 on waveform and frame structure for 6G ISAC	Moderator (LGE)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.3-a003`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.3 Waveform and frame structure

```text
Peak-to-Sidelobe Ratio (PSLR), Integrated Sidelobe Ratio (ISLR), and Main lobe width are defined based on AF as follows.
Definition of power
Opt 1. Power is defined in delay-Doppler domain
Opt 2. Power is defined in delay domain with zero or non-zero Doppler cut
Main lobe width is defined as the width of AF measured at the points where the power drops to half (-3 dB) of the peak main lobe power (3dB width).
Main lobe region (M) is the region corresponding to the first ‘null-to-null’ region from the main lobe.
Side lobe region (S) is defined as the entire region except the first ‘null-to-null’ region from the main lobe
, where PML=maximum power within the main lobe region, PSL=maximum power within the sided lobe region
Opt 1.  ,
Opt 2.  ,
, where IML=power integrated within the main lobe region, ISL=power integrated within the sided lobe region
Opt 1. ,
Opt 2. ,
R1-2606566	Summary #4 on waveform and frame structure for 6G ISAC	Moderator (LGE)
R1-2606567	Summary #5 on waveform and frame structure for 6G ISAC	Moderator (LGE)
Final post-meeting summary for this agenda item.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.3-a004`

### [6G/Rel-20 RAN1#126] `working_assumption` 10.8.3 Waveform and frame structure

```text
Linear Ambiguity Function (AF) is defined as:
Opt 1.  in delay-Doppler domain
where  is the delay shift,  is the Doppler frequency,  is the sampling interval
Opt 2.  in delay-Doppler domain,
where  is the delay shift,  is the Doppler frequency,  is the sampling interval, ,  is the number of samples in CP, N is the number of samples in OFDM symbol without CP, M is the number of OFDM symbols.
Circular Ambiguity Function (AF) is defined as:
Opt 1.  in delay-Doppler domain,
where  is the delay shift,  is the Doppler frequency,  is the sampling interval, N is the number of samples in OFDM symbol without CP
Opt 2a.
where p is Doppler index,  is delay index, ,  is the number of samples in CP, N is the number of samples in OFDM symbol without CP, M is the number of OFDM symbols, X is the spectrum of x.
Opt 2b.  in delay-Doppler domain,
where  is the delay shift,  is the Doppler frequency,  is the sampling interval, ,  is the number of samples in CP, N is the number of samples in OFDM symbol without CP, M is the number of OFDM symbols.
Opt 3.  in delay domain of single symbol
where  is the delay shift,  is the Doppler frequency,  is the sampling interval, N is the number of samples in OFDM symbol without CP, x’ is the received signal
Note: down-selection on Linear/Circular AF and options for evaluation will be discussed separately.
Note: companies should report assumption about receiver processing and observation window.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.3-w001`

### [6G/Rel-20 RAN1#126] `working_assumption` 10.8.3 Waveform and frame structure

```text
Linear Cross Ambiguity Function(CAF) is defined as:
Opt 1.  in delay-Doppler domain,
where  is the delay shift,  is the Doppler frequency,  is the sampling interval
Opt 2.  in delay-Doppler domain,
where  is the delay shift,  is the Doppler frequency,  is the sampling interval, ,  is the number of samples in CP, N is the number of samples in OFDM symbol without CP, M is the number of OFDM symbols.
Circular Cross Ambiguity Function(CAF) is defined as:
Opt 1.  in delay-Doppler domain,
where  is the integer delay shift,  is the Doppler frequency,  is the sampling interval, N is the number of samples in OFDM symbol without CP
Opt 2a.   in delay-Doppler domain,
where p is Doppler index,  is delay index, ,  is the number of samples in CP, N is the number of samples in OFDM symbol without CP, M is the number of OFDM symbols, X and Y are the spectrums of x and y respectively.
Opt 2b.  in delay-Doppler domain,
where  is the delay shift,  is the Doppler frequency,  is the sampling interval, ,  is the number of samples in CP, N is the number of samples in OFDM symbol without CP, M is the number of OFDM symbols.
Opt 3.  in delay domain of single symbol
where  is the delay shift,  is the Doppler frequency,  is the sampling interval, N is the number of samples in OFDM symbol without CP, y’ is the received signal
Note: down-selection on Linear/Circular CAF and options for evaluation will be discussed separately.
Note: companies should report assumption about receiver processing and observation window.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.3-w002`

### [6G/Rel-20 RAN1#124b] `agreement` 10.8.1 Evaluations

```text
For Rel-20 6G sensing performance evaluation of object detection and/or tracking, the following cases/combinations are considered as baseline cases/combinations.
| Sensing target | Indoor or outdoor | Scenario | Carrier frequency |
| --- | --- | --- | --- |
| UAV | Outdoor | UMa-AV, SMa | 4 GHz, ~7 GHz, 30 GHz (for UMa-AV only) |
| Human | Outdoor | UMa | 4 GHz, ~7 GHz, 30 GHz |
|  | Indoor | Indoor Hotspot | 4 GHz, ~7 GHz, 30 GHz |
| Vehicle | Outdoor | Urban Grid, Highway | 4 GHz, ~7 GHz, 30 GHz (for Urban Grid only) |
| AGV | Indoor | Indoor factory (SH) | 4 GHz, ~7 GHz, 30 GHz |
Note: sensing mode(s) for each row will be discussed
Other cases/combinations can also be evaluated, reported and collected from companies.
Note: In this agreement, no intention to de-prioritize other scenarios or carrier frequencies.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.8.1-a001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.8.1 Evaluations

```text
Companies are encouraged to bring input to the evaluation on communication assistance in next meeting, including but not limited to:
Necessity of evaluation on communication assistance
For proponents, provide: what to sense and, if necessary, what/how to assist communication
What metric of sensing is to be defined
Whether/what metric related to communication is to be defined
Whether performance target/KPI is to be defined, for either sensing metric or communication metric
Necessary channel model extension
Necessary update of evaluation methodology on top of 5G NR sensing evaluation methodology
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.8.1-a002`

### [6G/Rel-20 RAN1#124b] `agreement` 10.8.1 Evaluations

```text
Companies are encouraged to bring input to the sensing mode related evaluation assumptions in next meeting, using the following table as starting point. The values in current table are example values based on the input and discussion in RAN1#125.
Note1: This is not intended to specify all sensing modes.
Note2: This does not mean any sensing mode is applicable to any scenario/use case.
Note3: Other parameters/values for each sensing mode can also be discussed.
| Sensing mode | Parameter | Value |
| --- | --- | --- |
| TRP mono-static | Sensing Tx/Rx operating simultaneously or not | Simultaneously, or not simultaneously (FFS: with/without switching time and value if any) |
|  | BS antenna isolation | For Around 7 GHz and below 7 GHz: Option 1: 80 dB Option 2: 65 dB For 30 GHz: Option 1: 100 dB Option 2: 72 dB Option 3: 85 dB |
|  | BS transmit power | Simultaneously: min { BS transmit power in Table of ISAC system configuration, BS Rx saturation power + BS antenna isolation}, assuming the BS Rx saturation power = -28 dBm Not simultaneously: Follow BS transmit power in the table of general evaluation assumption |
|  | BS self-interference impact | The residual leakage interference/noise is modelled e.g., by additional additive white Gaussian noise, -174 + 10log10(BW) + X dBm in BW Hz, BW is simulated bandwidth, X = {-Infinity, 0, 5} is up to company report. Note: X = -Infinity corresponds to not modelling self-interference. |
| UE mono-static | UE type for sensing | Companies to report |
|  | Sensing Tx/Rx operating simultaneously or not | FFS |
|  | UE transmit power | FFS |
|  | UE Antenna isolation | FFS |
|  | UE Self-interference impact | FFS |
|  | Availability of UE location, velocity and orientation | Option 1: Known, ideally (baseline) Option 2: Known, with error. FFS distribution of error in each aspect (e.g. location, speed, orientation). Option 3: Unknown, rely on actual measurement Note: UE location, velocity and orientation are individually determined |
| TRP-TRP bi-static | Timing/frequency error | Option 1: Ideal (baseline) Option 2: With error, FFS value range and model of the distribution Note: timing error and frequency error are individually determined |
|  | Coherency and phase continuity among symbols within a CPI | Option 1: Always coherent Option 2: Coherency is assumed under some conditions; FFS: Conditions |
| UE-UE bi-static | UE type for sensing | Companies to report |
|  | Timing/frequency error | Option 1: Ideal (baseline) Option 2: With error, FFS value range and model of the distribution Note: timing error and frequency error are individually determined |
|  | Availability of UE location, velocity and orientation | Option 1: Known, ideally (baseline) Option 2: Known, with error. FFS distribution of error in each aspect (e.g. location, speed, orientation). Option 3: Unknown, rely on actual measurement Note: UE location, velocity and orientation are individually determined |
|  | Coherency and phase continuity among symbols within a CPI | Option 1: Always coherent Option 2: Coherency is assumed under some conditions; FFS: Conditions |
| TRP-UE bi-static | UE type for sensing | Companies to report |
|  | Timing/frequency error | Option 1: Ideal (baseline) Option 2: With error, FFS value range and model of the distribution Note: timing error and frequency error are individually determined |
|  | Availability of UE location, velocity and orientation | Option 1: Known, ideally (baseline) Option 2: Known, with error. FFS distribution of error in each aspect (e.g. location, speed, orientation). Option 3: Unknown, rely on actual measurement Note: UE location, velocity and orientation are individually determined |
|  | Coherency and phase continuity among symbols within a CPI | Option 1: Always coherent Option 2: Coherency is assumed under some conditions; FFS: Conditions |
| UE-TRP bi-static | UE type for sensing | Companies to report |
|  | Timing/frequency error | Option 1: Ideal (baseline) Option 2: With error, FFS value range and model of the distribution Note: timing error and frequency error are individually determined |
|  | Availability of UE location, velocity and orientation | Option 1: Known, ideally (baseline) Option 2: Known, with error. FFS distribution of error in each aspect (e.g. location, speed, orientation). Option 3: Unknown, rely on actual measurement Note: UE location, velocity and orientation are individually determined |
|  | Coherency and phase continuity among symbols within a CPI | Option 1: Always coherent Option 2: Coherency is assumed under some conditions; FFS: Conditions |
Final summary in R1-2602522.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.8.1-a003`

### [6G/Rel-20 RAN1#124b] `conclusion` 10.8.1 Evaluations

```text
For Rel-20 6G ISAC evaluation, the attributes (e.g. antenna pattern, mobility, etc.) of different UEs are for the purpose of evaluation discussion. No intention to study or specify diverse device type.
R1-2602519	FL summary #2 on ISAC evaluations	Moderator (CATT)
R1-2602520	FL summary #3 on ISAC evaluations	Moderator (CATT)
R1-2602521	FL summary #4 on ISAC evaluations	Moderator (CATT)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.8.1-c001`

### [6G/Rel-20 RAN1#124b] `working_assumption` 10.8.1 Evaluations

```text
For Rel-20 6G ISAC performance evaluation,
evaluate object detection and/or tracking for the following sensing targets/objects: UAV, human, vehicle, AGV;
discuss further on evaluation on communication assistance.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.8.1-w001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.8.2 Aspects of integration with communication

```text
On RS for ISAC, study at least the following aspects, considering sensing performance, resource overhead and impact to communication
RS for communication is reused for sensing
Enhanced RS for sensing, taking reuse of RS for communication as starting point
Note: Part of or all of the RS may be used for communication purpose, and it does not mean the final decision on whether the enhanced RS is used for communication purpose is to be made in this agenda.
Dedicated RS for sensing
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.8.2-a001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.8.2 Aspects of integration with communication

```text
Study RE patterns of RS for sensing, considering sensing performance, resource overhead and impact to communication.
Note: enhancements on RS sequence if any will be discussed in agenda 10.8.3.
R1-2602591	Summary #3 on integration with communication for ISAC	Moderator (Xiaomi)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.8.2-a002`

### [6G/Rel-20 RAN1#124b] `agreement` 10.8.2 Aspects of integration with communication

```text
On measurement for ISAC, study at least the following aspects.
Measurement definitions/levels for TRP-side measurement, taking the measurement Levels studied in NR ISAC as starting point
Measurement definitions/levels for UE-side measurement
Impacts of non-ideal factors on measurement
Other aspects are not precluded
Note: this discussion may or may not mean there is specification impact
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.8.2-a003`

### [6G/Rel-20 RAN1#124b] `agreement` 10.8.2 Aspects of integration with communication

```text
On measurement report for ISAC, study at least the following aspects and applicable scenarios (e.g., sensing modes, targets, etc.) from RAN1 perspective.
Measurement reporting mechanism from UE
Option 1A: The UE measurements and/or assistance information if needed from UE can be directly sent to aNB
Option 1B: The UE measurements and/or assistance information if needed from UE can be sent to SF
Measurement reporting mechanism from aNB
Option 2A: The aNB measurements and/or assistance information if needed from aNB can be directly sent to UE
Option 2B: The aNB measurements and/or assistance information if needed from aNB can be sent to SF
The study may require cross-WG coordination.
Note: combination of multiple options is not precluded.
Note: measurements in each option may be different
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.8.2-a004`

### [6G/Rel-20 RAN1#124b] `agreement` 10.8.2 Aspects of integration with communication

```text
On measurement report for ISAC, study impacts from at least the following aspects from RAN1 perspective
Measurement reporting mechanism
E.g., Periodic, semi-persistent, aperiodic, event-triggered report as starting point
Reporting signaling e.g., L1, L2, higher layer, etc.
Other aspects are not precluded
The study may require cross-WG coordination.
Final summary in R1-2602592.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.8.2-a005`

### [6G/Rel-20 RAN1#124b] `agreement` 10.8.3 Waveform and frame structure

```text
CP-OFDM waveform as defined for 6GR is the starting point for 6G ISAC waveform study.
Study on enhancements on CP-OFDM or other waveforms is not precluded.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.8.3-a001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.8.3 Waveform and frame structure

```text
6GR communication frame structure is the starting point for 6G ISAC frame structure study, in at least the following aspects.
Frame/sub-frame/slot/symbol structure
CP length
SCS
Enhancements on frame structure/above aspects are not precluded.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.8.3-a002`

### [6G/Rel-20 RAN1#124b] `agreement` 10.8.3 Waveform and frame structure

```text
Companies are encouraged to provide views on necessity/pros/cons/metrics of LLS and/or SLS and pros/cons/metrics of theoretical waveform characteristics analysis, for evaluation of ISAC waveform and/or integration with communication, to RAN1#125 meeting.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.8.3-a003`

### [6G/Rel-20 RAN1#124b] `agreement` 10.8.3 Waveform and frame structure

```text
CP-OFDM is used as the benchmark for evaluating the benefits of sensing waveforms.
R1-2602984	Summary #4 on waveform and frame structure for 6G ISAC	LG Electronics
Presented in Thursday session.
Final summary in R1-2602985.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.8.3-a004`

### [6G/Rel-20 RAN1#124] `agreement` 10.8.1 Evaluations

```text
For Rel-20 study, adopt the updated TP in Moderator’s evaluation summary attached in R1-2600466 into TR38.769.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.8.1-a001`

### [6G/Rel-20 RAN1#124] `agreement` 10.8.1 Evaluations

```text
In addition to energy harvesting/storage assumptions used to obtain the reported data rates from companies are provided and agreed in RAN1#123, the followings (highlighted in red) are further provided during the Rel-20 study,
| Source | Energy harvesting/storage assumptions |
| --- | --- |
| Source [NEC] | Energy source: Solar energy Energy storage capacity: 10~100µF with voltage of 3V For device 2b, 10~100µF with voltage of 3V, i.e., 30~300uJ; For device C, 0.5~5mF with voltage of 3V, i.e., 1.5~15mJ; Reported data rate: 1 kbps or 5 – 7 kbps Other information: Device 2b and Device C harvest energy at similar rate. |
| Source [FUTUREWEI] | Energy sources: Solar, thermal, vibration etc. Energy storage capacity: For device 2b with 500uW peak power consumption: 0.5 milli-joules or 500 F using 2V power supply Low rate: 0.1kbps: ~5000 J /~5000 F Middle rate: 1kbps: ~500 J /~500 F High rate: 5kbps: ~100 J /~100 F For device C with 10mW peak power consumption: 10 milli-joules or 10000 F using 2V power supply Low rate: 0.1kbps: ~100 mJ /~100 mF Middle rate: 1kbps: ~10mJ /~10 mF High rate: 5kbps: ~1 mJ /~1000 F Reported data rate: 0.1kbps, 1kbps, 5kbps Other information: It is observed that using RF energy harvesting is challenging as the energy source for Device 2b based on the following description. Typical leakage current for 500 F capacitors is at least higher than 3 A. With a supply voltage of 2 volts, the leakage current translates to ~ -22.2 dBm leakage power. Using RF harvesting is challenging in this case. For the maximum message size, 1000 bits is assumed for single PRDCH/PDRCH transmission. The rated voltage is 2V and min voltage is 1.4V (70% of the rated voltage). It should be noted that the reported capacity is for single PRDCH/PDRCH transmission. To sustain whole procedure of DT, DO-DTT, DO-A, larger capacity is required. |
| Source [CATT] | Energy source: Solar Energy storage capacity: ~100mF Reported data rate: 0.1kbps, 1kbps, 5~7kbps, 48~60kbps Other information: Assumptions of power consumption: 100uW and 1mW for R2D reception 200uW and 5mW for D2R transmission |
| Source [Samsung] | Energy source: Solar Energy storage capacity: >10μJ5μJ for device 2b, 100μJ30μJ for device C Reported data rate: 5.3 kbps for DL 20 bits, 6.7 kbps for UL 20 bits, 7.2 kbps for DL 96 bits, 8.4 kbps for UL 96 bits; with an average of 40% charging time |
| Source [Ericsson] | Energy source: RF signal/ Solar Energy storage capacity: Device 2b: 10s µF to a few 100 µF Device C: a few mF Reported data rates: 1kbps, 7kbps, and 50 kbps Other information: For device 2b: with tx power of -10dBm we considered the power consumption of 400 µW, to transmit 400 bits with the data rate of 1 kbps, the needed storage capacity is around 140 µF. For device C: with tx power of 5dBm we considered the power consumption of 12.6 mW, to transmit 400 bits with the data rate of 1 kbps, the needed storage capacity is around 4.5 mF. |
R1-2600463	FL summary #2 for Ambient IoT: “9.3.1 Evaluations”	Moderator (Huawei)
From Tuesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.8.1-a002`

### [6G/Rel-20 RAN1#124] `agreement` 10.8.1 Evaluations

```text
For Rel-20 study, adopt the following TPs into section 7.3 of TR38.769.
| ------ Start of TP------ RAN1 has evaluated the coverage for Device 2b and Device C respectively. Evaluation results from companies in terms of different achievable cell edge data rate and achievable maximum distance under different scenarios, penetration margins and Tx power have been observed for R2D and D2R in the tables of following sub-sections. For R2D coverage, based on evaluation results, the achievable cell edge data rate and achievable maximum distance are observed at least for the following scenarios For cell edge data rate around 1 kbps, For UMa NLOS pathloss model, penetration margin 0 dB Device 2b: the achievable maximum distance is at least 500 meters at BLER 10% when BS Tx power is from 33dBm to 43dBm and at BLER 1% when BS Tx power is from 38dBm to 43dBm. The achievable maximum distance can be smaller or larger than 500 meters at BLER 1% (about 370~1800 meters) when BS Tx power is 33dBm Device C: the achievable maximum distance is at least 500 meters at BLER 10% and 1% when BS Tx power is from 33dBm to 43dBm For UMa NLOS pathloss model, penetration margin 20 dB Device 2b: the achievable maximum distance can be smaller or larger than 500 meters at BLER 10% (about 190~1340 meters) and at BLER 1% (about 110~1000 meters) when BS Tx power is from 33dBm to 43dBm Device C: the achievable maximum distance is at least 500 meters at BLER 10% and 1% when BS Tx power is from 33dBm to 43dBm For cell edge data rate around 5~7 kbps, For UMa NLOS pathloss model, penetration margin 0 dB Device 2b: the achievable maximum distance is at least 500 meters at BLER 10% when BS Tx power is from 38dBm to 43dBm and at BLER 1% when BS Tx power is 43dBm. The achievable maximum distance can be smaller or larger than 500 meters at BLER 10% (about 480~2300 meters) when BS Tx power is 33dBm and at BLER 1% (about 210~1700 meters) when BS Tx power is from 33dBm to 38dBm Device C: the achievable maximum distance is at least 500 meters at BLER 10% when BS Tx power is from 33dBm to 43dBm and at BLER 1% when BS Tx power is from 38dBm to 43dBm. The achievable maximum distance can be smaller or larger than 500 meters at BLER 1% (about 430~1500 meters) when BS Tx power is 33dBm For UMa NLOS pathloss model, penetration margin 20 dB Device 2b: the achievable maximum distance can be smaller or larger than 500 meters at BLER 10% (about 150~1280 meters) and at BLER 1% (about 70~710 meters) when BS Tx power is from 33dBm to 43dBm Device C: the achievable maximum distance is at least 500 meters at BLER 10% when BS Tx power is 43dBm. The achievable maximum distance can be smaller or larger than 500 meters at BLER 10% (about 280~1070 meters) when BS Tx power is from 33dBm to 38dBm and at BLER 1% (about 130~810 meters) when BS Tx power is from 33dBm to 43dBm For D2R coverage, based on evaluation results, the achievable cell edge data rate and achievable maximum distance are observed at least for the following scenarios For cell edge data rate around 0.1 kbps, For UMa NLOS pathloss model, penetration margin 0 dB Device 2b: the achievable maximum distance is smaller than 500 meters at BLER 10% (about 80~370 meters) and BLER 1% (about 40~300 meters) when device Tx power is -20dBm. The achievable maximum distance can be smaller or larger than 500 meters at BLER 10% (about 150~660 meters) and at BLER 1% (about 80~540 meters) when device Tx power is -10dBm Device C: the achievable maximum distance is at least 500 meters at BLER 10% and 1% when device Tx power is from -3dBm to 5dBm For UMa NLOS pathloss model, penetration margin 20 dB Device 2b: the achievable maximum distance is smaller than 500 meters at BLER 10% (about 20~200 meters) and at BLER 1% (10~160 meters) when device Tx power is from -20dBm to -10dBm Device C: the achievable maximum distance is at least 500 meters at BLER 10% when device Tx power is 5dBm. The achievable maximum distance can be smaller or larger than 500 meters at BLER 10% (about 320~680 meters) when device Tx power is from -3dBm to 0dBm and at BLER 1% (about 260~730 meters) when device Tx power is from -3dBm to 5dBm For cell edge data rate around 1 kbps, For UMa NLOS pathloss model, penetration margin 0 dB Device 2b: the achievable maximum distance can be smaller or larger than 500 meters at BLER 10% (about 110~810 meters) and at BLER 1% (about 50~600 meters) when device Tx power is -10dBm. The achievable maximum distance is smaller than 500 meters at BLER 10% (about 60~450 meters) and BLER 1% (about 30~230 meters) when device Tx power is -20dBm. Device C: the achievable maximum distance is at least 500 meters at BLER 10% when device Tx power is from 0dBm to 5dBm and at BLER 1% when device Tx power is 5dBm. The achievable maximum distance can be smaller or larger than 500 meters at BLER 10% (about 460~1230 meters) when device Tx power is -3dBm and at BLER 1% (about 310~1090 meters) when device Tx power is from -3dBm to 0dBm For UMa NLOS pathloss model, penetration margin 20 dB Device 2b: the achievable maximum distance is smaller than 500 meters at BLER 10% (about 20~250 meters) and at BLER 1% (about 10~180 meters) when device Tx power is from -20dBm to -10dBm Device C: the achievable maximum distance can be smaller or larger than 500 meters at BLER 10% (about 230~600 meters) when device Tx power is 5dBm. The achievable maximum distance is smaller than 500 meters at BLER 10% (about 140~450 meters) when device Tx power is from -3dBm to 0dBm and at BLER 1% (about 100~450 meters) when device Tx power is from -3dBm to 5dBm. For cell edge data rate around 5~7 kbps, For UMa NLOS pathloss model, penetration margin 0 dB Device 2b: the achievable maximum distance can be smaller or larger than 500 meters at BLER 10% (about 100~680 meters) when device Tx power is -10dBm. The achievable maximum distance is smaller than 500 meters at BLER 10% (about 60~270 meters) when device Tx power is -20dBm and at BLER 1% (about 40~390 meters) when device Tx power is from -20dBm to -10dBm Device C: the achievable maximum distance can be smaller or larger than 500 meters at BLER 10% (about 300~1220 meters) and at BLER 1% (about 240~960 meters) when device Tx power is from -3dBm to 5dBm For UMa NLOS pathloss model, penetration margin 20 dB Device 2b: the achievable maximum distance is smaller than 500 meters at BLER 10% (about 20~150 meters) and at BLER 1% (10~120 meters) when device Tx power is from -20dBm to -10dBm Device C: the achievable maximum distance is smaller than 500 meters at BLER 10% (about 90~380 meters) and at BLER 1% (70~300 meters) when device Tx power is from -3dBm to 5dBm ------ End of TP ------ |
| --- |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.8.1-a003`

### [6G/Rel-20 RAN1#124] `agreement` 10.8.1 Evaluations

```text
For Rel-20 study, RAN1 has identified the followings
Device C achieves better coverage than Device 2b for both R2D and D2R
Device 2b is applicable to outdoor scenarios for short distance e.g. 50-200m
Device C is applicable to outdoor scenarios for both short and large distance e.g. 50-500m
Note: Necessity of Device 2b and C in terms of aspects other than coverage is up to RAN decision
R1-2600464	FL summary #3 for Ambient IoT: “9.3.1 Evaluations”	Moderator (Huawei)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.8.1-a004`

### [6G/Rel-20 RAN1#124] `agreement` 10.8.1 Evaluations

```text
RAN1 observes 5 dBm as the maximum transmit power for Device C to achieve maximum coverage in outdoor scenarios.
Values between -3dBm and 5dBm are feasible to achieve different coverage.
This does not preclude RAN to select any value(s) between -3 dBm and 5 dBm as maximum transmit power for Device C.
Final summary in R1-2601637.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.8.1-a005`

## 5G-A 历史事件

<details><summary>展开（原文，无中文摘要）</summary>

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
The definition on time stamp from existing specifications, e.g., TS 38.455, TS 38.355, TS 37.355 are reused as baseline.
No more discussion on time stamp is expected from RAN1 study perspective.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a001`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
From RAN1 perspective, the measurement of Level D reported from RAN is per gNB.
Note: RAN1’s understanding is that gNB can associate with one or multiple TRPs.
R1-2601381	Summary #2 on evaluations for NR ISAC	Moderator (Xiaomi)
From Tuesday session
R1-2601594	TP on Reference_6.2_6.3.0_6.3.1_AnnexB in TR 38.765	Moderator (Xiaomi)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a002`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
The Text Proposal to TR 38.765 in R1-2601594 is endorsed.
R1-2601595	TP on 6.3.2 in TR 38.765	Moderator (Xiaomi)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a003`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
The Text Proposal to TR 38.765 in R1-2601595 is endorsed.
R1-2601596	TP on 6.3.3 in TR 38.765	Moderator (Xiaomi)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a004`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
The Text Proposal to TR 38.765 in R1-2601596 is endorsed
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a005`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
From RAN1 perspective, on measurement quantization of Level C/D for position/velocity measurement, quantization methods in existing specifications, e.g., TS 23.032, TS 38.455, TS 38.355, TS 37.355 can be considered.
From RAN1 perspective, on measurement quantization of Level C for delay/angle measurement, quantization methods in existing specifications, e.g., TS 38.133 can be considered.
For Doppler measurement, same number of quantized bits as radial velocity can be considered.
Note: above does not take into account the potential impact from measurement quantization on the sensing performance.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a006`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
The velocity measurement of Option C1/C3/C4 is radial velocity.
R1-2601382	Summary #3 on evaluations for NR ISAC	Moderator (Xiaomi)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a007`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
The following Text Proposal to Conclusion section in TR 38.765 is endorsed.
| The performance for UAV sensing use case with gNB monostatic sensing is evaluated based on the evaluation assumptions in Annex A (including UMa-AV, Sensing Tx/Rx operating simultaneously, FR1), with detailed assumptions and modelling reported by the companies as captured in Annex B. Among all the reported evaluation results as captured in Annex B, Baseline 1 (high BS TX power 52dBm with 80dB antenna isolation) By utilizing measurements from multiple or all TRPs, results from 9/10 sources achieve the performance objectives. By utilizing measurements from single TRP, results from 3/11 sources achieve the performance objectives. Baseline 2 (low BS TX power 37dBm with 65dB antenna isolation) By utilizing measurements from multiple or all TRPs, results from 7/9 sources achieve the performance objectives. By utilizing measurements from single TRP, results from 2/9 sources achieve the performance objectives |
| --- |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a008`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
The velocity measurement of Option D1/D4 is 3D velocity, optional radial velocity.
Note: in the deployment where 3D velocity cannot be reported, Level D should not be reported.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a009`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
The velocity measurement of Option C2/C5 is radial velocity.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a010`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
Confirm the definition of measurement Level B by removing the square brackets
Level B: Amplitude and phase profile of delay, and/or Doppler, and/or angle per TRP for a given time stamp by using window(s) of the [consecutive] samples in at least one profile of delay, and/or Doppler and/or angle domain
R1-2601383	Summary #4 on evaluations for NR ISAC	Moderator (Xiaomi)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a011`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
From RAN1 perspective, the following methods can be considered to define the quantization for the measurements of Level A/B,
e.g., floating point, uniform scalar, non-uniform scalar
other quantization method is not precluded.
Note: above doesn’t take into account the potential impact from the measurement quantization on sensing performance.
Note: No more discussion on measurement quantization on Level A/B is expected in the study item from RAN1 perspective.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a012`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
From RAN1 perspective, the metric related to power can be considered for Level C measurement report.
From RAN1 perspective, the metric related to power (if applicable) can be considered for Level D measurement report.
Note: metric related to power may be different from those defined for communication and between Level C and Level D.
From RAN1 perspective, confidence metrics for the measurements can be considered for Level C/D measurement report.
No more discussion on the metric related to power and confidence metrics is expected in the study item from RAN1 study perspective.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a013`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
For Level C, at least the following examples of assistance information are identified as needed to assist the further processing at Sensing Function. The assistance information may or may not be provided by RAN.
Location of TRP if at least delay/range, Doppler/radial velocity or angle is reported.
If a measurement is reported in LCS, LCS to GCS transformation information.
For level D, if radial velocity is not reported, no assistance information is identified from RAN1 perspective.
No more discussion on the assistance information on Level C/D from RAN to SF is expected in the study item from RAN1 perspective.
R1-2601384	Summary #5 on evaluations for NR ISAC	Moderator (Xiaomi)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a014`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
From RAN1 perspective, on measurement quantization of Level C/D for confidence metric, the existing specifications, e.g., TS 23.032, TS 38.455, TS 38.355, TS 37.355 can be considered.
Note: above does not take into account the potential impact from measurement quantization on the sensing performance.
Note: No more discussion on measurement quantization on Level C/D for the metric related to power and confidence metric is expected in the study item from RAN1 perspective
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a015`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
For Level A/B, at least the following examples of assistance information are identified as needed to assist the further processing at Sensing Function. The assistance information may or may not be provided by RAN.
Level A
Location of TRP
Step size in delay domain if samples in delay domain is reported
Time information related to OFDM symbols used for measurement
Antenna configuration and/or beam information
Level B
Location of TRP
LCS to GCS transformation information
Information related to sampling of delay, doppler and/or angle profile
Additional assistance information is not precluded
No more discussion on the assistance information on Level A/B from RAN to SF is expected in the study item from RAN1 perspective
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a016`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
The payload size estimation of each measurement level/option for NR ISAC can be done by the following formulas
Level A: Msubcarrier* Ncpi *Mtxport*Nrxport*Ntrp*(Nquan1+ Nquan2)
Where,
Msubcarrier: number of subcarriers in a OFDM symbols
Ncpi: number of OFDM symbols within CPI
Mtxport: number of reference signal antenna port for sensing purpose
Nrxport: number of Rx antenna ports
Ntrp: number of TRPs for payload size calculation
Nquan1: number of quantized bits for amplitude
Nquan2: number of quantized bits for angle
Level B:
Delay-Doppler Profile: Mdelay *Ndoppler *Mtxport* Nrxport *Ntrp *(Nquan1+ Nquan2)
Delay-angle Profile: Mdelay * Ncpi *Mtxport*Nangle *Ntrp *(Nquan1+ Nquan2)
Delay-Doppler-angle Profile: Mdelay *Ndoppler *Mtxport*Nangle *Ntrp *(Nquan1+ Nquan2)
Delay Profile: Mdelay *Ncpi*Mtxport*Nrxport *Ntrp *(Nquan1+ Nquan2)
Where,
Mdelay: number of delay samples in the window
Ndoppler: number of Doppler samples in the window
Nangle: number of angle samples in the window
Level C:
C1/C2/C3: Np1*Ntrp *
C4/C5: Np2*Ntrp *
Where,
Np1 is total number of paths
Np2 is total number of points
Nparam is 5 including e.g.,
C1/C3/C4: delay, Doppler, horizontal angle, vertical angle, power measurement
C2/C5: position (x, y, z), radial velocity, power measurement
Nquan,i: number of quantized bits
Ntrp: number of TRPs for payload size calculation
Level D:
Nobject*Ngnb * for options D1/2
Mpoints* Ngnb * for options D3/4
Where,
Nobject is total number of targets
Mpoints is total number of scattering points of all targets
Ngnb is fixed to 1
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a017`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
The following assumptions on the parameters can be used to estimate payload size of different Levels/Options of measurements for NR ISAC for calculation purpose
| Parameters | Assumptions | Relation to maximum payload calculation |
| --- | --- | --- |
| Nsubcarriers | 3276 for 100MHz, 30kHz SCS |  |
| Ncpi | Min 64, medium 160, max 320 symbols per CPI |  |
| Mtxport | 1, medium 4, max 9 | Note: value obtained based on evaluation assumptions |
| Nrxport | 64 |  |
| Ntrp | 3 |  |
| Ngnb | 1 |  |
| Nquan1, i.e., amplitude | Min 16, medium 16, max 32 |  |
| Nquan2, i.e., phase | Min 16, medium 16, max 32 |  |
|  | Min 16, medium 16, max 32 |  |
| Mdelay | Min 288 (CP length, UMa) Medium/max: 467 for 2*570m (UMa) Max: 1436 for 2*1732m (RMa) |  |
| Ndoppler | same as Ncpi |  |
| Nangle | B2/B3: 32, 360 | Note: value obtained based on evaluation assumptions Note: 32 assumes non-uniform sampling Note: 360 assumes uniform oversampling |
| Np | 30, 60, 120 | to calculate min/medium/max for Level-C Note: value obtained based on evaluation assumptions |
| Nobject for D1/D2 | 15 | Note: value obtained based on evaluation assumptions |
| Mpoints for D3/D4 | 20 | Note: value obtained based on evaluation assumptions |
For Level C
Nparam=5 parameters for measurements
For Level D
Nparam=7 parameters for measurements
for D2/D3/D4, one more parameter of target ID is assumed
Note: for B2/B3, minimum value and maximum value can be different between non-uniform sampling case and uniform oversampling case
Note: RAN1 does not require all the parameters to take the minimum values at the same time or the maximum values at the same time
Note: above does not take into account the potential impact from measurement quantization on the sensing performance.
Note: above does not take into account the potential impact of different Levels/Options on the sensing performance.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a018`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
The following Text Proposal to Conclusion section in TR 38.765 is endorsed.
| The study in physical layer has identified a number of Levels/Options for measurement report as described in Clause 5. Different Levels/Options for measurement report are associated with different payload overhead, assistance information and other higher layer aspects. |
| --- |
R1-2601668	Updated evaluation results of NR ISAC	Moderator (Xiaomi)
R1-2601669	Updated evaluation details on NR ISAC reported by companies	Moderator (Xiaomi)
R1-2601385	Summary #6 on evaluations for NR ISAC	Moderator (Xiaomi)
R1-2601701	Summary #7 on evaluations for NR ISAC	Moderator (Xiaomi)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a019`

### [5G-A/Rel-19 RAN1#124] `conclusion` 9.5.1 Evaluation assumptions and performance evaluation

```text
From RAN1 perspective, the issue on ambiguity handling in delay/range, Doppler/radial velocity, angle, position and 3D velocity measurements is identified, but not further discussed in Rel-20 NR ISAC.
Note: it does not prevent further discussion in future.
Note: this issue may or may not be addressed by NW implementation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-c001`

### [5G-A/Rel-19 RAN1#124] `conclusion` 9.5.1 Evaluation assumptions and performance evaluation

```text
No further discussion on the assistance information from SF to RAN is expected in Rel-20 NR ISAC from RAN1 study perspective.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-c002`

### [5G-A/Rel-19 RAN1#123] `agreement` evaluation-assumptions-and-performance-e-3b5540f0 Evaluation assumptions and performance evaluation

```text
In section 6.2 Performance evaluation results in TR 38.765,
Multiple configurations of the following parameters are defined to respectively analyze the evaluation results
At least Two baseline configurations 1 & 2 are defined for evaluation purpose
|  | Parameters | Configuration 1 Baseline | Configuration 2 Baseline |
| --- | --- | --- | --- |
| 1 | Scenario | (UMa-AV, 500m) | (UMa-AV, 500m) |
| 2 | Sensing Tx/Rx operating simultaneously or not | Sensing Tx/Rx operating simultaneously | Sensing Tx/Rx operating simultaneously |
| 3 | Carrier frequency | 4 or 4.9GHz | 4 or 4.9GHz |
| 4 | Max BS Tx power | 52 dBm | 37 dBm |
| 5 | BS antenna configuration | (M, N, P, Mg, Ng, Mp, Np) Tx: (8,8,2,1,1;4,8) Rx: (8,8,2,1,1;4,8) = (0.5, 0.8)λ, +45°/-45° polarization | (M, N, P, Mg, Ng, Mp, Np) Tx: (8,8,2,1,1;4,8) Rx: (8,8,2,1,1;4,8) = (0.5, 0.8)λ, +45°/-45° polarization |
| 6 | Number of targets per sector in center site | N=5 | N=5 |
| 7 | Target vertical distribution | 25-300m | 25-300m |
Additional configurations can be defined for other assumptions of the parameters, based on reported evaluation results in RAN1 #124.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-evaluation-assumptions-and-performance-e-3b5540f0-a001`

### [5G-A/Rel-19 RAN1#123] `agreement` evaluation-assumptions-and-performance-e-3b5540f0 Evaluation assumptions and performance evaluation

```text
Companies should report whether a same target is modeled in the ISAC channel of single, multiple or all STXs/SRXs
Company should report how to determine the single or multiple STXs/SRXs for a target
The details of STX/SRX determination will be captured along with the corresponding evaluation results in the TR for NR ISAC
If the evaluation results are derived by measurement reports from multiple/all STXs/SRXs, companies should report how measurement reports from multiple/all STXs/SRXs are used
R1-2509239	Summary #2 on evaluations for NR ISAC	Moderator (Xiaomi)
R1-2509240	Summary #3 on evaluations for NR ISAC	Moderator (Xiaomi)
R1-2509241	Summary #4 on evaluations for NR ISAC	Moderator (Xiaomi)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-evaluation-assumptions-and-performance-e-3b5540f0-a002`

### [5G-A/Rel-19 RAN1#123] `agreement` evaluation-assumptions-and-performance-e-3b5540f0 Evaluation assumptions and performance evaluation

```text
From RAN1 perspective, the following measurements that may be reported from RAN are identified in the study of NR ISAC. Note: Down selection of Level(s)/Option(s) for recommendation can be discussed separately.
Level A: Raw data per Tx antenna port per OFDM symbol per RX antenna port per TRP for a given time stamp
Option A1: Amplitude and phase samples in time/delay domain of the estimated channel, i.e., Amplitude and phase values of channel impulse response
Option A2: Amplitude and phase per subcarrier in frequency domain of the estimated channel
Level B: Amplitude and phase profile of delay, and/or Doppler, and/or angle per TRP for a given time stamp by using window(s) of the [consecutive] samples in delay, Doppler and/or angle domain
Option B1: Delay-Doppler profile per Tx antenna port per Rx antenna port, which includes the amplitude and phase samples distributed across different delays and Doppler shifts.
Option B2: Delay-Angle profile per Tx antenna port per OFDM symbol, which includes the amplitude and phase samples distributed across different delays and spatial angles (e.g., Angle of Arrival).
Option B3: Delay-Doppler-Angle profile per Tx antenna port, which includes the amplitude and phase samples distributed across delay, Doppler, and angle domains.
Option B4: Delay profile per Tx antenna port per OFDM symbol per Rx antenna port, which includes the amplitude and phase samples distributed across different delays.
Note: Level B is applicable for either LCS or GCS
Level C: per detected path/point measurements per Tx antenna port per TRP which may be reflected/scattered from scattering point(s).
Option C1: Delay/range, Doppler/velocity, one or multiple 3D angles, and [power/confidence metric] per detected path for a given time stamp.
A path is associated with one couple {delay/range, Doppler/velocity, [power/confidence metric]}, and one or multiple 3D angles.
Option C2: Doppler/velocity, position, and [power/confidence metric] per detected path for a given time stamp.
A path is associated with one doppler/velocity, [power/confidence metric], one or multiple positions
Option C3: Delay/range, Doppler/velocity, 3D angle, and [power/confidence metric] per detected path for a given time stamp.
A path is associated with one delay, and one or multiple triple {Doppler/velocity, 3D angle, [power/confidence metric]}
Option C4: Delay/range, Doppler/velocity, 3D angle, and [power/confidence metric] per detected point for a given time stamp
A point is associated with one range/delay, one Doppler/velocity, one 3D angle
Option C5: Position, velocity, and [power/confidence metric] per detected point for a given time stamp
A point is associated with one position, one velocity
FFS: Velocity can be
Opt 1: radial velocity
Opt 2: 3D velocity
Note:
Position can be defined in either LCS or GCS
Angle can be defined in either LCS or GCS
Ambiguity issue will be further discussed
3D angle refers to a pair of horizontal and vertical angles
Level D: Object/target level measurement [per TRP or per gNB]
One or more value pair(s) {position, velocity} in GCS for a given time stamp is reported for a detected object/target,
Option D1: Only one value pair {position, velocity} in GCS for a given time stamp is reported for a detected object/target. The association of multiple measurements across different time stamps for the same detected object/target is not reported.
Option D2: Only one value pair {position, velocity} in GCS for a given time stamp is reported for a detected object/target. The association of multiple measurements across different time stamps for the same detected object/target is reported.
Option D3: One or more value pairs {position, velocity} in GCS for a given time stamp are reported for a detected object/target. The association of multiple measurements across different time stamps for the same detected object/target is reported.
Option D4: One or more value pairs {position, velocity} in GCS for a given time stamp are reported for a detected object/target. The association of multiple measurements across different time stamps for the same detected object/target is not reported.
Note: Ambiguity issue can be further discussed if any
Note: velocity is 3D velocity for Option D2/D3
FFS: velocity can be radial velocity or 3D velocity for Option D1/D4
Note: the possible information from RAN to SF for further processing can be further discussed for all levels
Note: the possible information from SF to RAN can be further discussed for all levels
Note: confidence metric can be further discussed for options of Level C/D
Note: definition of time stamp for each of all options of all Levels can be further discussed
For Level A/B/C, Tx antenna port means reference signal antenna port for sensing purpose
R1-2509242	Summary #5 on evaluations for NR ISAC	Moderator (Xiaomi)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-evaluation-assumptions-and-performance-e-3b5540f0-a003`

### [5G-A/Rel-19 RAN1#123] `agreement` evaluation-assumptions-and-performance-e-3b5540f0 Evaluation assumptions and performance evaluation

```text
RAN1 confirms the performance objectives in the early agreement from RAN1 #122bis by removing the brackets
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-evaluation-assumptions-and-performance-e-3b5540f0-a004`

### [5G-A/Rel-19 RAN1#123] `agreement` evaluation-assumptions-and-performance-e-3b5540f0 Evaluation assumptions and performance evaluation

```text
The following performance objectives are adopted for evaluation purpose of NR ISAC.
Metric
Value
Missed detection Probability
[5]%
False Alarm Probability Type 1
[5]%
False Alarm Probability Type 2
[5]%
Horizontal Positioning Accuracy
[10] m with confidence level 90%
Vertical Positioning Accuracy
[10] m with confidence level 90%
Velocity Accuracy
[5] m/s with confidence level 90%
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-evaluation-assumptions-and-performance-e-3b5540f0-a005`

### [5G-A/Rel-19 RAN1#123] `agreement` evaluation-assumptions-and-performance-e-3b5540f0 Evaluation assumptions and performance evaluation

```text
Confidence level of the X% represents X percentile point of the cumulative distribution function (CDF) of the estimation errors.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-evaluation-assumptions-and-performance-e-3b5540f0-a006`

### [5G-A/Rel-19 RAN1#123] `agreement` evaluation-assumptions-and-performance-e-3b5540f0 Evaluation assumptions and performance evaluation

```text
Up to company to report evaluation results for UAV tracking in NR ISAC study.
Proponent company should clarify the details on how target trajectory is modeled
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-evaluation-assumptions-and-performance-e-3b5540f0-a007`

### [5G-A/Rel-19 RAN1#123] `agreement` evaluation-assumptions-and-performance-e-3b5540f0 Evaluation assumptions and performance evaluation

```text
The following general procedure for performance evaluation of NR ISAC is to be captured in TR 38.765.
Simulation parameter configuration
Sensing scenario generation, including the deployment of sensing Tx/Rx (STXs/SRXs)
Dropping N target(s), where N is equal to 0 or larger than 0
Channel generation and STX/SRX determination for the targets
Sensing signal generation and passing the sensing signal to the generated channel
Sensing signal processing at each SRX, optionally, sensing signal processing based on fusion from multiple STXs/SRXs
E.g., optionally, sensing signal processing based on tracking
Sensing performance metric calculation.
Note: company should report the details on sensing signal processing and ISAC channel generation
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-evaluation-assumptions-and-performance-e-3b5540f0-a008`

### [5G-A/Rel-19 RAN1#123] `agreement` evaluation-assumptions-and-performance-e-3b5540f0 Evaluation assumptions and performance evaluation

```text
The following evaluation assumptions for optional FR2-1 carrier frequency are considered for evaluation of NR ISAC
| Parameters | Values |
| --- | --- |
| Scenario | UMi-AV |
| Carrier Frequency | 30 GHz |
| System bandwidth | 400 MHz |
| SCS | 120 kHz |
| Inter-BS (2D) distance | 200 m |
| BS antenna configurations | (M,N,P,Mg,Ng;Mp,Np) = (16,16,2,2,1;1,1), (dH,dV) = (0.5, 0.5 or 0.8)λ, +45°/-45° polarization for whole panel; (16,16,2,1,1;1,1) for Tx and (16,16,2,1,1;1,1) for Rx |
| Beam set at TRxP | Up to company report |
| Antenna isolation | 80 ~ 100 dB |
| Max BS Tx power | 30 dBm |
| BS noise figure | 7 dB |
Up to company to report evaluation results and additional configuration information for FR2-1.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-evaluation-assumptions-and-performance-e-3b5540f0-a009`

### [5G-A/Rel-19 RAN1#123] `agreement` evaluation-assumptions-and-performance-e-3b5540f0 Evaluation assumptions and performance evaluation

```text
The attached template in R1-2509242 (Proposal 5.3-1-rev2) is used as starting point for evaluation results collection.
R1-2509243	Summary #6 on evaluations for NR ISAC	Moderator (Xiaomi)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-evaluation-assumptions-and-performance-e-3b5540f0-a010`

### [5G-A/Rel-19 RAN1#123] `conclusion` evaluation-assumptions-and-performance-e-3b5540f0 Evaluation assumptions and performance evaluation

```text
Sensing service latency and refreshing rate are not considered as performance metrics for evaluation of NR ISAC.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-evaluation-assumptions-and-performance-e-3b5540f0-c001`

### [5G-A/Rel-19 RAN1#122] `agreement` evaluation-assumptions-and-performance-e-3b5540f0 Evaluation assumptions and performance evaluation

```text
Horizontal/vertical positioning accuracy are agreed as performance metrics for NR ISAC.
It is defined as the absolute value of the difference between the estimated horizontal/vertical position and the corresponding true position of a sensing target.
Note: in RAN1 evaluations, there should be only one estimated horizontal/vertical position corresponding to the true position of a sensing target.
R1-2506478	Summary #3 on evaluations for NR ISAC	Moderator (Xiaomi)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-evaluation-assumptions-and-performance-e-3b5540f0-a001`

### [5G-A/Rel-19 RAN1#122] `agreement` evaluation-assumptions-and-performance-e-3b5540f0 Evaluation assumptions and performance evaluation

```text
The following evaluation parameters are agreed for the evaluation on NR ISAC.
| Parameters | Assumptions |
| --- | --- |
| Scenario | UMa-AV, Optional RMa-AV |
| Carrier frequency | Mandatory: one value either 4 GHz or 4.9GHz. optional for FR1: 6 GHz [optional for FR2: 28 GHz] |
| System bandwidth | 100 MHz |
| Numerology | SCS = 30kHz |
| BS Layout | Hexagonal grid, 7 macro sites, 3 sectors per site. See Note1 3 sectors with 30, 150, 270 degrees |
| Inter-BS (2D) distance | Uma-AV: 500m, optional 1000m, RMa-AV: 1732m |
| BS antenna height | 25m for UMa-AV, 35m for RMa-AV |
| Wrap-round | No wrap-round |
Note1: target(s) are dropped only in the center site, and inter-BS interference is not modelled.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-evaluation-assumptions-and-performance-e-3b5540f0-a002`

### [5G-A/Rel-19 RAN1#122] `agreement` evaluation-assumptions-and-performance-e-3b5540f0 Evaluation assumptions and performance evaluation

```text
The following evaluation parameters are agreed for the evaluation on NR ISAC.
| Parameters | Assumptions |
| --- | --- |
| Target type | UAV with small size (0.3m x 0.4m x 0.2m) |
| Target distribution when target(s) are dropped | N = 5 targets per sector in the center site. Optional: N is uniformly distributed from 1 to 10. Horizontal plane: uniformly distributed in a sector Vertical plane: Uniformly distributed between 25m and 300m, optionally distributed between 1.5m and 300m |
| Mobility | horizontal speed: uniformly distributed between 0 and 180km/h vertical speed: 0km/h |
Note: N=0 will be discussed in a later proposal in relation to false alarm.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-evaluation-assumptions-and-performance-e-3b5540f0-a003`

### [5G-A/Rel-19 RAN1#122] `agreement` evaluation-assumptions-and-performance-e-3b5540f0 Evaluation assumptions and performance evaluation

```text
The following evaluation parameters are agreed for the evaluation on NR ISAC.
| Parameters | Assumptions |
| --- | --- |
| Minimum BS-target 3D distance | 10 m |
| Minimum target-target (3D) distance | 10 m |
| Target outdoor/indoor proportion | 100% outdoor |
| LOS/NLOS | LOS and NLOS |
| Orientation | Random in horizontal domain |
| RCS model | RCS model 1 for UAV with small size |
R1-2506479	Summary #4 on evaluations for NR ISAC	Moderator (Xiaomi)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-evaluation-assumptions-and-performance-e-3b5540f0-a004`

### [5G-A/Rel-19 RAN1#122] `agreement` evaluation-assumptions-and-performance-e-3b5540f0 Evaluation assumptions and performance evaluation

```text
For the purpose of performance metric calculation, association of the detected object(s) and the true target(s) should fulfil at least the following conditions:
One true target is associated with at most one detected object.
One detected object is associated with at most one true target.
The same association applies to miss detection, false alarm probability Type 2 (if defined) and positioning/velocity accuracy.
Companies to report the method used for association of the detected object(s) and the true target(s).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-evaluation-assumptions-and-performance-e-3b5540f0-a005`

### [5G-A/Rel-19 RAN1#122] `agreement` evaluation-assumptions-and-performance-e-3b5540f0 Evaluation assumptions and performance evaluation

```text
Missed detection probability is agreed as performance metric for NR ISAC.
It is defined as the conditional probability of not detecting the presence of a target when the target is actually present in the simulation area.
Where,
is the number of missed targets in the drop n, i.e., the true target not associated with any detected object.
is the number of true targets in the drop n.
is total number of drops with at least one target per drop.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-evaluation-assumptions-and-performance-e-3b5540f0-a006`

### [5G-A/Rel-19 RAN1#122] `agreement` evaluation-assumptions-and-performance-e-3b5540f0 Evaluation assumptions and performance evaluation

```text
False alarm probability is agreed as performance metric for NR ISAC.
For cases without true target dropped in simulation area, False alarm probability Type 1 is computed and reported
For cases with true targets dropped in simulation area, False alarm probability Type 2 is computed and reported
Note: both False alarm probability Types are mandatory
KPI values for False alarm probability Type 1 and 2 can be discussed separately.
Definitions:
False alarm probability Type 1 (no target dropped in simulation area): An object is detected when there is no target present in simulation area is considered a false alarm.
Where,
equal to 1 if at least one object is detected when there is no target dropped in the simulation area in the drop n, otherwise  equal to 0.
is the total number of drops without targets in the simulation area.
False alarm probability Type 2 (targets dropped in simulation area): An object is detected but not associated with any true targets in the simulation area is considered as a false alarm.
Where,
is the number of detected objects but not associated with any true targets in the drop n.
is the total number of detected objects in the drop n.
FFS:
Option 1:  is number of drops (N)
Option 2:  is number of drops with at least one detected object
Note: the number of targets should be reported by companies when providing False alarm probability Type 2.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-evaluation-assumptions-and-performance-e-3b5540f0-a007`

### [5G-A/Rel-19 RAN1#122] `agreement` evaluation-assumptions-and-performance-e-3b5540f0 Evaluation assumptions and performance evaluation

```text
Velocity accuracy is agreed as performance metric for NR ISAC.
Velocity accuracy is defined as the absolute value of the difference between the estimated velocity and the corresponding true velocity of a sensing target.
For single TRP monostatic sensing,
The radial velocity accuracy can be estimated
The true radial velocity is the projection of true velocity on the direction from TRP to target for TRP monostatic.
The true velocity accuracy can be estimated.
Final summary in R1-2506480.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-evaluation-assumptions-and-performance-e-3b5540f0-a008`

### [5G-A/Rel-19 RAN1#122] `agreement` maintenance-on-channel-modelling-for-int-848a421f Maintenance on channel modelling for Integrated Sensing And Communication (ISAC) for NR

```text
TP #4.1-1 in section 4.1 of R1-2506473 is endorsed for TR 38.901 v19.0.0.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-maintenance-on-channel-modelling-for-int-848a421f-a001`

### [5G-A/Rel-19 RAN1#122] `agreement` maintenance-on-channel-modelling-for-int-848a421f Maintenance on channel modelling for Integrated Sensing And Communication (ISAC) for NR

```text
TP #4.3-2-rev2 in section 4.3.1 of R1-2506473 is endorsed for TR 38.901 v19.0.0.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-maintenance-on-channel-modelling-for-int-848a421f-a002`

### [5G-A/Rel-19 RAN1#122] `agreement` maintenance-on-channel-modelling-for-int-848a421f Maintenance on channel modelling for Integrated Sensing And Communication (ISAC) for NR

```text
Update parameter component names in the Tables in Section 7.9.6.2 to align with the parameter component names in 7.9.2.1 i.e. respectively replacing  with .
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-maintenance-on-channel-modelling-for-int-848a421f-a003`

### [5G-A/Rel-19 RAN1#122] `agreement` maintenance-on-channel-modelling-for-int-848a421f Maintenance on channel modelling for Integrated Sensing And Communication (ISAC) for NR

```text
TP #4.4-2-rev1 in section 4.4.1 of R1-2506473 for TR 38.901 v19.0.0.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-maintenance-on-channel-modelling-for-int-848a421f-a004`

### [5G-A/Rel-19 RAN1#122] `agreement` maintenance-on-channel-modelling-for-int-848a421f Maintenance on channel modelling for Integrated Sensing And Communication (ISAC) for NR

```text
TP #4.4-4 in section 4.4.2 of R1-2506473 for TR 38.901 v19.0.0.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-maintenance-on-channel-modelling-for-int-848a421f-a005`

### [5G-A/Rel-19 RAN1#122] `agreement` maintenance-on-channel-modelling-for-int-848a421f Maintenance on channel modelling for Integrated Sensing And Communication (ISAC) for NR

```text
TP #4.4-5 in section 4.4.3 of R1-2506473 for TR 38.901 v19.0.0.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-maintenance-on-channel-modelling-for-int-848a421f-a006`

### [5G-A/Rel-19 RAN1#122] `agreement` maintenance-on-channel-modelling-for-int-848a421f Maintenance on channel modelling for Integrated Sensing And Communication (ISAC) for NR

```text
Add the missing square in the parameter  in Section 7.9.4.2 step 4, i.e.,
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-maintenance-on-channel-modelling-for-int-848a421f-a007`

### [5G-A/Rel-19 RAN1#122] `agreement` maintenance-on-channel-modelling-for-int-848a421f Maintenance on channel modelling for Integrated Sensing And Communication (ISAC) for NR

```text
TP #4.6-12 and #4.6-13 in section 4.6.5 of R1-2506473 for TR 38.901 v19.0.0.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-maintenance-on-channel-modelling-for-int-848a421f-a008`

### [5G-A/Rel-19 RAN1#122] `agreement` maintenance-on-channel-modelling-for-int-848a421f Maintenance on channel modelling for Integrated Sensing And Communication (ISAC) for NR

```text
TP #4.7-1 in section 4.7.1 of R1-2506473 for TR 38.901 v19.0.0.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-maintenance-on-channel-modelling-for-int-848a421f-a009`

### [5G-A/Rel-19 RAN1#122] `agreement` maintenance-on-channel-modelling-for-int-848a421f Maintenance on channel modelling for Integrated Sensing And Communication (ISAC) for NR

```text
The value for best sensing Tx-Rx pairs to be selected for the target should be set to
N=2 for TRP-TRP monostatic
N=1 for TRP-TRP bistatic
Add in the Table 7.9.6.3-1 the following row:
| STX/SRX selection | Best N = 4 STX-SRX pairs to be selected for the target, with the following exceptions for FR1: For TRP-TRP monostatic sensing, N=2 For TRP-TRP bistatic sensing, N=1 |
| --- | --- |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-maintenance-on-channel-modelling-for-int-848a421f-a010`

### [5G-A/Rel-19 RAN1#122] `agreement` maintenance-on-channel-modelling-for-int-848a421f Maintenance on channel modelling for Integrated Sensing And Communication (ISAC) for NR

```text
TP #4.9-1 in section 4.9.1 of R1-2506473 for TR 38.901 v19.0.0.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-maintenance-on-channel-modelling-for-int-848a421f-a011`

### [5G-A/Rel-19 RAN1#122] `agreement` maintenance-on-channel-modelling-for-int-848a421f Maintenance on channel modelling for Integrated Sensing And Communication (ISAC) for NR

```text
TP #4.8-7-rev2 in section 4.8.4 of R1-2506473  for TR 38.901 v19.0.0.
R1-2506474	Summary #2 on channel modelling for ISAC	Moderator (Xiaomi)
R1-2506475	Summary #3 on channel modelling for ISAC	Moderator (Xiaomi)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-maintenance-on-channel-modelling-for-int-848a421f-a012`

### [5G-A/Rel-19 RAN1#122] `agreement` maintenance-on-channel-modelling-for-int-848a421f Maintenance on channel modelling for Integrated Sensing And Communication (ISAC) for NR

```text
The TP below is endorsed for TR 38.901 v19.0.0.
| <Start of Changes> 7.9.5.5 Lower power clusters In addition to the clusters/rays in background channel generated in Clause 7.9.4.2, more clusters/rays using NLOS propagation condition can be generated between a sensing Tx and a sensing Rx for bi-static sensing or between a sensing Tx and a reference point r, where r=0, 1, 2 for mono-static sensing to simulate the weak rays in the background channel. The following procedure is applicable for bistatic sensing or for monostatic sensing. Step 1: Generate a first background channel for bi-static sensing and for referenc point r for mono-static sensing according to Clause 7.9.4.2. Step 2: Generate a second background channel for bi-static sensing and for reference point r for mono-static sensing according to Clause 7.9.4.2 including utilizing the same DS, ASA, ASD, ZSA, ZSD, , as used for the first step, if applicable, with the following revised parameters: 1) The number of clusters (N in Clause 7.5) is increased to 360; 2) The number of ray per cluster (M in Clause 7.5) is reduced to 1; 3) If LOS condition is assumed in Step 1, use NLOS condition to generate DS, ASA, ASD, ZSA, and ZSD values. Step 3: The power of the clusters/rays in the second background channel is scaled down by , and is added to the first background channel, where, dB, is the maximum power of the NLOS clusters in the first background channel for bi-static sensing and is the maximum power of the NLOS clusters for reference point r in the first background channel. The final background channel is 7.9.5-15a for bi-static sensing mode and 7.9.5-15b for mono-static sensing. (7.9.5-15a) (7.9.5-15b) <End of Changes> |
| --- |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-maintenance-on-channel-modelling-for-int-848a421f-a013`

### [5G-A/Rel-19 RAN1#122] `agreement` maintenance-on-channel-modelling-for-int-848a421f Maintenance on channel modelling for Integrated Sensing And Communication (ISAC) for NR

```text
The following TP is endorsed for TR 38.901 v19.0.0.
| 7.9.4.2. Background channel <omitted text> Step 2: Generate 3 reference points (RPs) for the STX/SRX. Draw the 2D distance between the STX/SRX and each RP and the height of each RP respectively by and with parameters defined in Table 7.9.4.2-1/2. Note that and are random values generated by the shape-rate parameterized Gamma distribution . With uniform distribution within range , draw the LOS AOD (ϕLOS,AOD) between the STX/SRX and the first RP. The LOS AOD is further rotated by and to respectively derive the LOS AOD from the STX/SRX to the second and third RPs. Consequently, the 3D location of each RP can be calculated. <omitted text> |
| --- |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-maintenance-on-channel-modelling-for-int-848a421f-a014`

### [5G-A/Rel-19 RAN1#122] `agreement` maintenance-on-channel-modelling-for-int-848a421f Maintenance on channel modelling for Integrated Sensing And Communication (ISAC) for NR

```text
TP #4.5-2 in section 4.5.2 of R1-2506474 is endorsed for TR 38.901 v19.0.0, with the deletion of the last “and )”.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-maintenance-on-channel-modelling-for-int-848a421f-a015`

### [5G-A/Rel-19 RAN1#122] `agreement` maintenance-on-channel-modelling-for-int-848a421f Maintenance on channel modelling for Integrated Sensing And Communication (ISAC) for NR

```text
The following TP is endorsed for TR 38.901 v19.0.0
--------------------------------------- Start of TP for TR 38.901 ---------------------------------------
Step 3: Assign NLOS propagation condition to the channel between the STX/SRX and each of the 3 RPs.
Note: O2I is not applicable.
--------------------------------------- End of TP for TR 38.901 ---------------------------------------
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-maintenance-on-channel-modelling-for-int-848a421f-a016`

### [5G-A/Rel-19 RAN1#122] `agreement` maintenance-on-channel-modelling-for-int-848a421f Maintenance on channel modelling for Integrated Sensing And Communication (ISAC) for NR

```text
The TP below is endorsed for TR 38.901 v19.0.0
--------------------------------------- Start of TP for TR 38.901 ---------------------------------------
| 7.9.1 Scenarios <Unrelated part omitted> Table 7.9.1-3: Evaluation parameters for Human (indoor and outdoor) sensing scenarios |
| --- |
Parameters
Indoor Values
Outdoor Values
Minimum 3D distances between STX/SRX and sensing target
For TRP monostatic and TRP-TRP bistatic sensing modes, the minimum 2D distance between STX/SRX and the sensing target is 0 m
For UE monostatic and UE-UE bistatic sensing modes, the minimum 2D distance between STX/SRX and the sensing target is 1 m (as specified in TR 38.858)
For TRP monostatic and TRP-TRP bistatic sensing modes, the minimum 2D distances between STX/SRX and the sensing target are 10 m for UMi scenarios and 35 m for UMa scenarios
For UE monostatic and UE-UE bistatic sensing modes, the minimum 2D distance between STX/SRX and the sensing target is 1 m (as specified in TR 38.858)
Minimum 3D distance between sensing targets
Option 1: At least larger than the physical size of a sensing target
Option 2: Fixed value, 1m
Option 1: At least larger than the physical size of a sensing target
Option 2: Fixed value, 1m
NOTE 1: 	N=0 may be considered for the evaluation of false alarm
--------------------------------------- End of TP for TR 38.901 ---------------------------------------
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-maintenance-on-channel-modelling-for-int-848a421f-a017`

### [5G-A/Rel-19 RAN1#122] `agreement` maintenance-on-channel-modelling-for-int-848a421f Maintenance on channel modelling for Integrated Sensing And Communication (ISAC) for NR

```text
Replace “between pairs of STX/SRX and sensing target” by ‘between pairs of STX/SRX and sensing target’ in TR38.901.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-maintenance-on-channel-modelling-for-int-848a421f-a018`

### [5G-A/Rel-19 RAN1#122] `agreement` maintenance-on-channel-modelling-for-int-848a421f Maintenance on channel modelling for Integrated Sensing And Communication (ISAC) for NR

```text
In Table 7.9.6.1-3, the minimum distance between STX/SRX and sensing target should be:
Min distances based on min TRP/UE distances defined in TR37.885.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-maintenance-on-channel-modelling-for-int-848a421f-a019`

### [5G-A/Rel-19 RAN1#122] `agreement` maintenance-on-channel-modelling-for-int-848a421f Maintenance on channel modelling for Integrated Sensing And Communication (ISAC) for NR

```text
The TP below is endorsed for TR 38.901 v19.0.0.
--------------------------------------- Start of TP for TR 38.901 ---------------------------------------
| 7.9.6 Calibration |
| --- |
Table 7.9.6.1-2. Simulation assumptions for large scale calibration for Human sensing targets
Parameters
Indoor Values
Outdoor Values
Minimum 3D distances between STX/SRX and sensing target
For TRP monostatic and TRP-TRP bistatic sensing modes, the minimum 2D distance between STX/SRX and the sensing target is 0 m
For UE monostatic and UE-UE bistatic sensing modes, the minimum 2D distance between STX/SRX and the sensing target is 1 m (as specified in TR 38.858)
For TRP monostatic and TRP-TRP bistatic sensing modes, the minimum 2D distances between STX/SRX and the sensing target are 10 m for UMi scenarios and 35 m for UMa scenarios
For UE monostatic and UE-UE bistatic sensing modes, the minimum 2D distance between STX/SRX and the sensing target is 1 m (as specified in TR 38.858)
<Unrelated part omitted>
--------------------------------------- End of TP for TR 38.901 ---------------------------------------
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-maintenance-on-channel-modelling-for-int-848a421f-a020`

### [5G-A/Rel-19 RAN1#122] `agreement` maintenance-on-channel-modelling-for-int-848a421f Maintenance on channel modelling for Integrated Sensing And Communication (ISAC) for NR

```text
The reference for calibrations R1-2504950 is replaced by R1-2506518 in TR38.901.
R1-2506518	ISAC channel model calibration results	Moderator (AT&T)	(rev of R1-2506462, rev of R1-2506225)
Comeback for draft CR incorporating all the endorsed TPs – Yingyang (Xiaomi)
From Friday session
R1-2506616	ISAC channel model calibration results	Moderator (AT&T)	(rev of R1-2506518)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-maintenance-on-channel-modelling-for-int-848a421f-a021`

### [5G-A/Rel-19 RAN1#122] `agreement` maintenance-on-channel-modelling-for-int-848a421f Maintenance on channel modelling for Integrated Sensing And Communication (ISAC) for NR

```text
The previous agreement is modified  as follows
The reference for calibrations R1-2504950 is replaced by R1-2506616 in TR38.901.
R1-2506577	CR to incorporate new agreements on ISAC CM	Xiaomi, AT&T
(Rel-19, 38.901, FS_Sensing_NR, CR0029, Cat F) is agreed.
MCC: Delete "draft" from the title before submission to RANP.
Final summary in R1-2506578.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-maintenance-on-channel-modelling-for-int-848a421f-a022`

### [5G-A/Rel-19 RAN1#122] `working_assumption` maintenance-on-channel-modelling-for-int-848a421f Maintenance on channel modelling for Integrated Sensing And Communication (ISAC) for NR

```text
The following TP is agreed for TR 38.901 v19.0.0
| --------------------------------------- Start of TP for TR 38.901 --------------------------------------- Step 4: Generate the channel between the STX/SRX and each of the 3 RPs using Step 3 to Step12 of Clause 7.5 and Clause 7.6.10 with parameters derived by Table 7.9.3-3, with updates as follows. - In Step 7 of Clause 7.5, the arrival angles are respectively equal to the departure angles . The rays in a cluster with less than 50, 80 and 90 degrees respectively for scenario UMi, UMa and RMa are dropped. The dropping is not applicable to other sensing scenarios. - Step 8 of Clause 7.5 is not applicable, except that the random coupling of AOD angles n,m,AOD with ZOD angles within a cluster n or within a sub-cluster in the case of two strongest clusters. Apply the same coupling in the corresponding arrival angles . - The absolute time of arrival in clause 7.6.9 is applied with d3D replaced by , where is the height of the STX/SRX. Three are independently generated and respectively applied to the 3 channels between the STX/SRX and the 3 RPs. NOTE: In the UT monostatic sensing in UMa and UMi scenario, the ZOD offset should be set as 0. --------------------------------------- End of TP for TR 38.901 --------------------------------------- |
| --- |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-maintenance-on-channel-modelling-for-int-848a421f-w001`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
Confirm the following working assumption with updates in red.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a001`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
The agreement on bistatic RCS for vehicle is reused for large size UAV and AGV.
For large size UAV, k₁=6.05 and k₂=1.33
For AGV, k₁=12 and k₂=1.45
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a002`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
AGV can be modelled with multiple scattering points.
The values/pattern of component A*B1 are generated by the following parameters
|  | in [°] | in [°] | in [°] | in [°] |  |  | Range of in [°] | Range of in [°] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Front | 0° | 13.68° | 90° | 13.68° | 13.00 | 30.26 | [0,180] | [0,360] |
| Left | 90° | 15.53° | 75° | 20.03° | 7.27 | 24.53 | [0,180] | [0,360] |
| Back | 180° | 12.49° | 90° | 11.89° | 10.98 | 28.24 | [0,180] | [0,360] |
| Right | 270° | 15.53° | 75° | 20.03° | 7.27 | 24.53 | [0,180] | [0,360] |
| Roof | / | / | 0° | 11.44° | 11.77 | 29.03 | [0,180] | [0,360] |
Note: For the scattering point associated with roof of the AGV, .
Note: the measurements from companies are done by AGV option 1.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a003`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
The bistatic RCS of UAV with small size is modelled as
The values/pattern of A*B1 is given by
Component A, i.e., : same as component A of mono-static RCS for UAV of small size
dB, where  is the bi-static angle between incident ray and scattered ray,  is within 0 and 180 degree
The effect of forward scattering  is -Inf in Rel-19
Component B2: same as component B2 of mono-static RCS for UAV of small size
The bistatic RCS of Human with RCS model 1 is modelled as
The values/pattern of A*B1 is given by
Component A, i.e., : same as component A of mono-static RCS for Human with RCS model 1
dB, where  is the bi-static angle between incident ray and scattered ray,  is within 0 and 180 degree
The effect of forward scattering  is -Inf in Rel-19
Component B2: same as component B2 of mono-static RCS for Human with RCS model 1
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a004`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
On the monostatic RCS of human with RCS model 2,
The values/pattern of component A*B1 are generated by the following parameters:
|  | in [°] | in [°] | in [°] | in [°] |  |  | Range of in [°] | Range of in [°] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Front | 0 | 216.65 | 90 | 55.7 | 2.14 | 7.7 | [0,180] | [-90, 90] |
| Back | 180 | 216.65 | 90 | 55.7 | 2.14 | 7.7 | [0,180] | [90,270] |
The standard deviation of component B2 is 3.94 dB.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a005`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
The agreement on bistatic RCS for vehicle with single scattering point is reused to model bistatic RCS of human with RCS model 2.
k1=0.5714 and k2=0.1
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a006`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
The following values of the RCS component A are applied to both monostatic and bistatic RCS of the target.
UAV with large size: -5.85 dBsm
Human with RCS model 2: -1.37 dBsm
Note: measurement is based on adult
Vehicle: 11.25 dBsm
Note: measurement is based on vehicle type 1 and 2
AGV: -4.25 dBsm
Note: measurement is based on AGV option 1
Note: component A on its own may not fully reflect the RCS in the target channel. This note will not be captured in the TR.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a007`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
The mean and standard deviation values of XPR of sensing target AGV for monostatic sensing and bistatic sensing are (9.60, 6.85) dB.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a008`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
In order to generate Tx-target link, target-Rx link and the background channel between a RSU-type UE and another node (TRP, pedestrian UE, vehicle UE, RSU-type UE), the following reference TRs are adopted:
| Case | Tx/Rx | Rx/Tx | Existing TRs as starting point |
| --- | --- | --- | --- |
|  | TRP | RSU-type UE | Highway and Urban grid B2R link in section 6 of TR 37.885 |
|  | RSU-type UE | normal UE | Highway and Urban grid V2V link in section 6 of TR 37.885, with antenna height at RSU is 5m |
|  | RSU-type UE | RSU-type UE | Highway and Urban grid V2V link in section 6 of TR 37.885, with antenna height at RSU is 5m |
|  | RSU-type UE | vehicle UE | Highway and Urban grid V2V link in section 6 of TR 37.885, with antenna height at RSU is 5m |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a009`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
The initial random phase (generated in Step 10, section 7.5, TR38.901) is the same for the same ray in Tx-target link and target-Rx link of a target for monostatic sensing.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a010`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
For UMi-AV and RMa-AV with aerial UE as sensing transmitter or receiver, the values of parameters to generate background channel for UT monostatic sensing are provided in the following table:
| Scenario | UT monostatic sensing |  |  |
| --- | --- | --- | --- |
|  | UMi-AV | RMa-AV |  |
| Distribution of 2D distance between Tx and reference points |  |  |  |
|  |  |  |  |
|  |  |  |  |
| Distribution of height of reference points |  |  |  |
|  |  |  |  |
|  |  |  |  |
Note 1: Distributions of height and distance of reference point are not subject to geographical constraints on TRP for the corresponding deployment scenario.
Note 2: The reference points for generating the UT monostatic background channel have the same velocity as UT.
Note 3: In the UT monostatic sensing in UMa and UMi scenario, the ZOD offset in the background channel should be set as 0
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a011`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
To generate the background channel for TRP monostatic sensing and UT monostatic sensing, ‘ +’ is used to model the absolute delay between the Tx and each reference point.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a012`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
Power threshold for path dropping after concatenation is up to -40dB for target channel for option 3. Up to company to choose a value in the implementation.
Power threshold for path dropping after concatenation is up to -25dB for target channel for option 0. Up to company to choose a value in the implementation.
For calibrations for both option 0 and option 3, power threshold for path dropping after concatenation is -40dB for target channel.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a013`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
To generate the absolute delay model for sensing scenarios Urban grid, highway and HST, for both target channel and background channel:
For Urban grid, the values of parameters for  of scenarios UMa are reused.
For Highway, the values of parameters for  of scenarios RMa and UMa are reused for FR1 and FR2 respectively.
For HST, the values of parameters for  of scenarios RMa and UMa are reused for FR1 and FR2 respectively.
Note: no measurements on  of the 3 scenarios are submitted in Rel-19.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a014`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
Spatial consistency is not modelled for
the links that are generated referring to channel models with parameter values of different communication scenarios
E.g., between TRP-target/UT link in one scenario and target/UT-UT link in another scenario
the background channels for TRP monostatic sensing of different TRPs
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a015`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
Spatial consistency is not modelled between TRP-target/UT link and target/UT-UT link for sensing scenario UMi, InH and InF.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a016`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
Spatial consistency is not modelled between TRP-TRP link and any other links for ISAC channel.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a017`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
Spatial consistency can be enabled for multiple scattering points of a target.
Spatial consistency, if enabled, for the links between BS/UT and multiple scattering points of a target are modelled as if multiple scattering points are multiple targets.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a018`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
The existing horizontal correlation distance in Table 7.6.3.1-2 in TR38.901 is used as the correlation distance for 3D spatial consistency for ISAC channel at least for UAV scenario, within same ‘Applicability range in terms of aerial UE height (defined in 36.777)’.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a019`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
EO type-2 can be modelled in NLOS condition.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a020`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
In sensing scenario UMi, UMa, if the height of a scattering point of target is less than 1.5m, for pathloss calculation,
use hUT 1.5 m for breakpoint distance (dBP) calculation
Note: hUT 1.5 m is only used for dBP calculation. The exact h_UT of the scattering point is still used to determine all other parameters of ISAC channel, e.g., delay, AOD/ZOD/AOA/ZOA, etc.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a021`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
On background channel modelling,
Spatial consistency is not supported for TRP monostatic sensing across different TRPs
Spatial consistency is not supported for UE monostatic sensing across different UEs
Spatial consistency is not supported across different Reference Points for same TRP for TRP monostatic sensing
Spatial consistency is not supported across different Reference Points for same UE for UE monostatic sensing
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a022`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
RCS component B2 of different direct/indirect paths of a target in the target channel are generated independently.
On the RCS component B2 of a direct/indirect path of a target in the target channel, the same value of B2 applies to a path before the value of B2 is updated.
Note: whether/how/when to update B2 can be discussed in evaluation phase or up to companies’ choices
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a023`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
XPR of different direct/indirect paths of a target in the target channel are generated independently.
On the XPR of a direct/indirect path of a target in the target channel, the same value of XPR applies to a path before the value of XPR is updated.
Note: whether/how/when to update XPR can be discussed in evaluation phase or up to companies’ choices
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a024`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
Initial random phase of different direct/indirect paths of a target in the target channel are generated independently.
On the initial random phase of a direct/indirect path of a target in the target channel, the same value of initial random phase applies to a path before the value of initial random phase is updated.
Note: whether/how/when to update initial random phase can be discussed in evaluation phase or up to companies’ choices
R1-2504163	Summary #3 on ISAC channel modelling	Moderator (Xiaomi)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a025`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
The follow TP is used generate the power (except for the impact of polarization matrix of EO type-2) of the ray specular reflected by an EO type 2 in the STX-SPST link or SPST-SRX link.
| 7.9.5.2 Type-2 environment object < Unchanged text omitted > In Step 10 in Clause 7.9.4.1, for a NLOS ray specularly reflected by a type-2 EO, if present, in the SPST-SRX link and the STX-SPST link is determined as follows. - If the STX-SPST link is in LOS condition, - If the STX-SPST link is not in LOS condition, , where is the pathloss of STX-SPST link assuming LOS condition. - If the SPST-SRX link is in LOS condition, - If the SPST-SRX link is not in LOS condition, , where is the pathloss of SPST-SRX link assuming LOS condition. < Unchanged text omitted > |
| --- |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a026`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
To generate the absolute delay model for sensing scenarios UMi-AV, UMa-AV and RMa-AV, for both target channel and background channel,
For the TRP-TRP link and TRP- terrestrial UE link, the values of parameters for  of scenarios UMi, UMa and RMa are respectively reused.
For the terrestrial UE- terrestrial UE link, the values of parameters for  of scenarios UMi are reused.
For the TRP- aerial UE link, the values of parameters for  of scenarios UMi, UMa and RMa are respectively reused.
For the terrestrial UE- aerial UE link, the values of parameters for  of scenarios UMi are reused.
For the aerial UE- aerial UE link, the values of parameters for  of scenarios UMi are reused.
Note: no measurements on  of the scenarios UMi-AV, UMa-AV and RMa-AV are submitted in Rel-19.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a027`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
Remove the brackets for first sub-bullet under Step 4 for Clause 7.9.4.2 in the CR to TR 38.901.
On the absolute delay of the background channel for both TRP and UE monostatic sensing, three  are independently generated and respectively applied to the 3 channels between the STX/SRX and the 3 RPs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a028`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
To generate the channel between an aerial UE and a normal UE,
The LOS probability is generated by:
| Low-UAV | Mid-UAV | High-UAV |
| --- | --- | --- |
| UMi in Table 7.4.2-1 in TR 38.901 for UMi-AV/UMa-AV/RMa-AV | UMi-AV in Table B-1 in TR 36.777 for BS to mid UAV region for UMi-AV/UMa-AV/[RMa-AV] RMa-AV in Table B-1 in TR 36.777 for BS to mid UAV region | UMi-AV in Table B-1 in TR 36.777 for BS to [high] UAV region for UMi-AV/UMa-AV/[RMa-AV] RMa-AV in Table B-1 in TR 36.777 for BS to mid UAV region |
The pathloss and shadow fading are generated using TRP-aerial UE link of UMi-AV in Annex A and B of TR 36.777 by setting hBS =1.5m for FR1.
Note:
The height ranges of low-UAV, Mid-UAV and High-UAV are defined following the applicability range in terms of aerial UE height in Table B-1: LOS probability in TR 36.777
The second height range for UMi-AV is further divided into 2 regions, i.e., [22.5, 100] and [100, 300] for mid-UAV and high-UAV, respectively.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a029`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
The polarization matrix  of a direct/indirect path i of a scattering point of a target is defined in LCS.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a030`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
To generate the channel between a first aerial UE with height h1 and a second aerial UE with height h2, abs(h1-hBS) <= abs(h2-hBS),
The LOS probability between the two aerial UEs is generated by:
|  | Low-UAV | Mid-UAV | High-UAV |
| --- | --- | --- | --- |
| Low-UAV | UMi in Table 7.4.2-1 in TR 38.901 for UMi-AV/UMa-AV/RMa-AV | UMi-AV in Table B-1 in TR 36.777 for BS to mid UAV region for UMi-AV/UMa-AV/[RMa-AV] RMa-AV in Table B-1 in TR 36.777 for BS to mid UAV region | UMi-AV in Table B-1 in TR 36.777 for BS to [high] UAV region for UMi-AV/UMa-AV/[RMa-AV] RMa-AV in Table B-1 in TR 36.777 for BS to mid UAV region |
| Mid-UAV | UMi-AV in Table B-1 in TR 36.777 for BS to mid UAV region for UMi-AV/UMa-AV/[RMa-AV] RMa-AV in Table B-1 in TR 36.777 for BS to mid UAV region | UMa-AV in Table B-1 in TR 36.777 for BS to mid UAV region for UMi-AV/UMa-AV RMa-AV in Table B-1 in TR 36.777 for BS to mid UAV region | 1 |
| High-UAV | UMi-AV in Table B-1 in TR 36.777 for BS to [high] UAV region for UMi-AV/UMa-AV/[RMa-AV] RMa-AV in Table B-1 in TR 36.777 for BS to mid UAV region | 1 | 1 |
The pathloss and shadow fading between two aerial UEs are generated using TRP-aerial UE link of UMi-AV in Annex A and B of TR 36.777 by setting height of TRP equal to the height of the first aerial UE.
Note:
The height ranges of low-UAV, Mid-UAV and High-UAV are defined following the applicability range in terms of aerial UE height in Table B-1: LOS probability in TR 36.777
The second height range for UMi-AV is further divided into 2 regions, i.e., [22.5, 100] and [100, 300] for mid-UAV and high-UAV, respectively.
R1-2504164	Summary #4 on ISAC channel modelling	Moderator (Xiaomi)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a031`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
Update the agreements on LOS probability calculation for channel between an aerial UE and a normal UE as follows.
| Low-UAV | Mid-UAV | High-UAV |
| --- | --- | --- |
| UMi in Table 7.4.2-1 in TR 38.901 for UMi-AV/UMa-AV/RMa-AV | UMi-AV in Table B-1 in TR 36.777 for BS to mid UAV region for UMi-AV/UMa-AV/[RMa-AV] RMa-AV in Table B-1 in TR 36.777 for BS to mid UAV region for RMa-AV | UMi-AV in Table B-1 in TR 36.777 for BS to high UAV region for UMi-AV/UMa-AV/[RMa-AV] RMa-AV in Table B-1 in TR 36.777 for BS to high UAV region for RMa-AV |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a032`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
Update the agreements on LOS probability calculation for channel between two aerial UE as follows.
|  | Low-UAV | Mid-UAV | High-UAV |
| --- | --- | --- | --- |
| Low-UAV | UMi in Table 7.4.2-1 in TR 38.901 for UMi-AV/UMa-AV/RMa-AV | UMi-AV in Table B-1 in TR 36.777 for BS to mid UAV region for UMi-AV/UMa-AV/[RMa-AV] RMa-AV in Table B-1 in TR 36.777 for BS to mid UAV region for RMa-AV | UMi-AV in Table B-1 in TR 36.777 for BS to high UAV region for UMi-AV/UMa-AV/[RMa-AV] RMa-AV in Table B-1 in TR 36.777 for BS to high UAV region for RMa-AV |
| Mid-UAV | UMi-AV in Table B-1 in TR 36.777 for BS to mid UAV region for UMi-AV/UMa-AV/[RMa-AV] RMa-AV in Table B-1 in TR 36.777 for BS to mid UAV region for RMa-AV | UMa-AV in Table B-1 in TR 36.777 for BS to mid UAV region for UMi-AV/UMa-AV RMa-AV in Table B-1 in TR 36.777 for BS to mid UAV region | 1 |
| High-UAV | UMi-AV in Table B-1 in TR 36.777 for BS to high UAV region for UMi-AV/UMa-AV/[RMa-AV] RMa-AV in Table B-1 in TR 36.777 for BS to high UAV region for RMa-AV | 1 | 1 |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a033`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
To determine the LOS condition of any link in ISAC channel model, when EO type-2 is modelled, the following two options are agreed as solutions:
Option A: If type-2 EO is in the LOS ray of the link, the LOS probability is p, p=0, and otherwise use the LOS probability equation defined in existing TRs to determine the LOS/NLOS condition
Option C: Use the LOS probability equation to determine the LOS/NLOS condition of the link.
Note1: in which conditions/scenarios to use option A or option C can be determined in future evaluations.
Note2: as already agreed, monostatic background channel is always NLOS.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a034`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
EO type-2 can be optionally modelled in background channel when EO type-2 is modelled in target channel.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a035`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
The existing blockage model A/B procedures can be reused to model the blocking effect due to a target as an optional feature
Applicable to the LOS/NLOS rays in the background channel of the target
Applicable to the LOS/NLOS rays in the Tx-target and target-Rx link of another target
The location, orientation and size of the target as a blocker is known before applying the blockage model A/B.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a036`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
The square brackets on formula 7.9.5-10 (copied below) in the draft CR are removed
The effective polarization matrix of the type-2 EO reflection path is given by
[	(7.9.5-10)]
Encourage companies to check and compare with the results that can be obtained with Alt2 and Alt3 below. If problem is found, RAN1 will revise TR 38.901 by new CR.
Alt2
[	(7.9.5-10)]
with reusing the legacy transformation method for deriving  and .
Alt3
[	(7.9.5-10)]
Where,
.  represents the normal vector of the incident plane. , in which  and .  represents the spherical basis vector of incident ray in vertical direction.   represents the spherical basis vector of incident ray in horizontal direction. .
.  represents the polar basis vector of scattering ray in vertical direction.  represents the polar basis vector of scattering ray in horizontal direction. . .
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-a037`

### [5G-A/Rel-19 RAN1#121] `conclusion` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
The component B2 of two different targets are generated independently.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-c001`

### [5G-A/Rel-19 RAN1#121] `conclusion` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
The component XPR/initial random phase of two different targets are generated independently.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-c002`

### [5G-A/Rel-19 RAN1#121] `conclusion` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
No further study on power normalization of target channel and background channel of ISAC channel in Rel-19
Note: sub-section “7.9.5.3 Power normalization across target channel and background channel” in the TR remains as a placeholder with the following text.
To combine the target channel and the background channel, an alternative scheme of power normalization can be applied to keep the same/similar channel power as the background channel without sensing target.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-c003`

### [5G-A/Rel-19 RAN1#121] `conclusion` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
Other than RCS for human, vehicle, AGV, UAV, no other RCS for other objects is introduced in Rel-19.
Future studies are not precluded for adding RCS of other objects/sizes for modelling target or EO type-1, based on validation results from companies.
R1-2504165	Summary #5 on ISAC channel modelling	Moderator (Xiaomi)
From Friday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-c004`

### [5G-A/Rel-19 RAN1#121] `conclusion` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
Delete subsection 7.9.6 from the draft CR. For ISAC, no enhancement to existing TR38.901 LLS channel model is introduced in Rel-19.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-c005`

### [5G-A/Rel-19 RAN1#121] `conclusion` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
There is no consensus to introduce an exact formula for micro-Doppler in Rel-19. The placeholder in the channel impulse response is kept in the draft CR.
Final summary in R1-2504945.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-c006`

### [5G-A/Rel-19 RAN1#121] `working_assumption` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
For vehicle with single/multiple scattering points, the bistatic RCS is generated by
The values/pattern of A*B1 of bistatic RCS is given by:
where
is applied to the  within 0~180 degrees. k1= 6 and k2=1.65.  is the bistatic angle between the incident ray and scattering ray within the plane of incident direction () and scattering direction ().
The angles of () are the projections of the bisector angle on the vertical plane and the horizontal plane, respectively.
FFS: RCS value when  is 180 degrees
The effect of forward scattering  is -Inf in Rel-19
5 sets of parameters Applicable Range of  and Applicable Range of  are applicable as defined for the monostatic RCS of vehicle with single/multiple SPSTs
Continue study on a new formula for  to resolve the issue of angular discontinuity.
The new formula should retain following property: the linear bistatic RCS for a vehicle with single scattering point is the sum of the bistatic RCS of the multiple scattering points of the vehicle
the following formula can be a reference for the study
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-channel-modelling-fa5b802a-w001`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
Updates to Table 7.9.1-1: Evaluation parameters for UAV sensing scenarios are as follows:
| Parameters | Value |
| --- | --- |
| Applicable communication scenarios | UMi, UMa, RMa, SMa UMi-AV, UMa-AV, RMa-AV [36.777] |
| Unintended/Environment objects, e.g., types, characteristics, mobility, distribution, etc. | Can be considered in future evaluations |
NOTE1:	calibration for the UAV scenario is performed for UMa-AV scenario, but UMi-AV, RMa-AV, UMi, UMa, RMa, SMa can be considered for future evaluations of the UAV sensing target scenarios.
NOTE2:	A percentage of TRPs/UEs that have sensing capabilities may be considered for future evaluations.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-deployment-scenarios-75cbe2f1-a001`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
Updates to Table 7.9.1-2: Evaluation parameters for Automotive sensing scenarios are as follows:
| Parameters | Values |
| --- | --- |
| Applicable communication scenarios | Highway, Urban Grid. UMi, UMa, RMa, SMa. NOTE1 |
| Environment Objects, e.g., types, characteristics, mobility, distribution, etc. | EO Type 2 for Urban Grid up to 4 walls modelled as EO type 2, per building of size 413m x 230m x 20m. Additional building sizes, building heights, materials, etc., can be considered in future evaluations |
NOTE1:	calibration for the automotive scenario will be performed for Highway and Urban Grid scenarios. UMi, UMa, RMa, SMa and related calibration parameters can be considered for future evaluations of the automotive sensing target scenarios.
NOTE2:	A percentage of TRPs/UEs that have sensing capabilities may be considered for future evaluations.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-deployment-scenarios-75cbe2f1-a002`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
Updates to Table 7.9.1-3: Evaluation parameters for Human (indoor and outdoor) sensing scenarios as follows:
| Parameters | Indoor Values | Outdoor Values |
| --- | --- | --- |
| Applicable communication scenarios NOTE1 | Indoor office, indoor factory Indoor room [TR38.808] | UMi, UMa, RMa, SMa |
| Minimum 3D distance between sensing targets | Option 1: At least larger than the physical size of a sensing target Option 2: Fixed value, 1 m. | Option 1: At least larger than the physical size of a sensing target Option 2: Fixed value, 1 m. |
| Environment Objects, e.g., types, characteristics, mobility, distribution, etc. | Can be considered in future evaluations | Can be considered in future evaluations |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-deployment-scenarios-75cbe2f1-a003`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
Updates to Table 7.9.1-4: Evaluation parameters for Automated Guided Vehicles sensing scenarios as follows:
| Parameters | Value |  |
| --- | --- | --- |
| Sensing Target | Physical characteristics (e.g., size) | Size (L x W x H) Option 1: 0.5m x 1.0m x 0.5m Option 2: 1.5 m x 3.0m x 1.5 m Material, Additional sizes, and AGV size distribution can be considered in future evaluations |
| Minimum 3D distance between sensing targets | Option A: At least larger than the physical size of a target Option B: Fixed value, 5 m. |  |
| Environment objects, e.g., types, characteristics, mobility, distribution, etc. | Can be considered in future evaluations |  |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-deployment-scenarios-75cbe2f1-a004`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
Updates to Table 7.9.1-5: Evaluation parameters for objects creating hazards sensing scenarios as follows:
| Parameters | Value |  |
| --- | --- | --- |
| Applicable communication scenarios NOTE1 | Highway, Urban grid, HST (High Speed Train) UMi, UMa, RMa, SMa |  |
| Sensing Target | 3D mobility | Horizontal velocity: up to 10 km/h for humans and animals Additional velocities, trajectory can be considered in future evaluations |
| Environment objects, e.g., types, characteristics, mobility, distribution, etc. | EO Type 2 for Urban Grid up to 4 walls modelled as EO type 2, per building of size 413m x 230m x 20m. Additional building sizes, building heights, materials, etc., can be considered in future evaluations |  |
NOTE1:	calibration for objects creating hazards scenario can be performed for Highway and Urban Grid scenarios. UMi, UMa, RMa, SMa and HST and related calibration parameters can be considered for future evaluations of the objects creating hazards scenarios.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-deployment-scenarios-75cbe2f1-a005`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
Updates to Table 7.9.7.1-3. Simulation assumptions for large scale calibration for Automotive sensing targets as follows:
| Parameters | Values |
| --- | --- |
| Scenario | For FR1: Urban Grid (ISD=500m, BS height=25m) Highway (ISD=1732m, BS height=35m) For FR2: Urban Grid (ISD=250m, BS height=25m) Highway (ISD=500m, BS height=25m) |
| Component A of the RCS for each scattering point | 11.25 dBsm |
| Wrapping Method | No wrapping method is used if interference is not modelled, otherwise geographical distance based wrapping. |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-deployment-scenarios-75cbe2f1-a006`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
Clarification for metrics for Simulation assumptions for full calibration sensing targets as follows:
| The power threshold for path dropping after concatenation for target channel | -40dB |
| --- | --- |
| The power threshold for removing clusters in step 6 in section 7.5, TR 38.901 for background channel | -25dB |
| Metrics | Coupling loss for target channel Coupling loss for background channel (in case of monostatic sensing, this is the linear sum of coupling losses between Tx/Rx and all reference points) Note: CDFs can be separately generated for target channel, background channel CDF of Delay Spread and Angle Spread (ASD, ZSD, ASA, ZSA) For monostatic sensing mode: delay spread and angle spread of the background channel is calculated separately for each reference point based on paths from all reference points. Definition of Delay Spread is similar to the definition of angle spread in Annex A of TR 25.996, Definition of Angle Spread can ref to Annex A of TR 25.996. |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-deployment-scenarios-75cbe2f1-a007`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
Updates to Table 7.9.7.2-2: Simulation assumptions for full calibration for Human sensing targets as follows:
| Parameters | Indoor Values | Outdoor Values |
| --- | --- | --- |
| (u, std) for XPR of target | (19.81, 4.25) dB | (19.81, 4.25) dB |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-deployment-scenarios-75cbe2f1-a008`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
The following introductory text is added before each of the ISAC deployment scenarios;
ISAC-UAV
In the ISAC-UAV scenario, the sensing targets are outdoor UAVs below or above the buildings in urban or rural areas. Monostatic or bistatic sensing can be performed using TRPs and/or UEs, including UEs on other UAVs.
ISAC-Automotive
In the ISAC-Automotive scenario, the sensing targets are passenger vehicles or trucks and buses traveling on roads and streets in urban and rural areas. Monostatic or bistatic sensing can be performed using TRPs and/or UEs, including UEs on other vehicles and roadside UEs (RSU-type UEs).
ISAC-Human
In the ISAC-Human scenario, the sensing targets are children and adult persons in indoor (room, office, factory) and outdoor (urban, rural) locations. Monostatic or bistatic sensing can be performed using TRPs and/or UEs in the corresponding communication scenarios.
ISAC-AGV
In the ISAC-AGV scenario, the sensing targets are automated guided vehicles (AGVs) inside a factory. Monostatic or bistatic sensing can be performed using TRPs and/or UEs in the corresponding communication scenario.
ISAC-Objects creating hazards
In the ISAC-Objects creating hazards scenario, the sensing targets are adult humans and children and animals in communication scenarios involving vehicles or high-speed trains. Monostatic or bistatic sensing can be performed using TRPs and/or UEs, including UEs on other vehicles and roadside UEs (RSU-type UEs).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-deployment-scenarios-75cbe2f1-a009`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
Updates to 7.9.7.1-4: Simulation assumptions for large scale calibration for AGV sensing targets as follows:
| Parameters | Values |
| --- | --- |
| Component A of the RCS for each scattering point | -4.25 dBsm Note: based on AGV option 1 |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-deployment-scenarios-75cbe2f1-a010`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
Updates to 7.9.7.2-4: Simulation assumptions for full calibration for AGV sensing targets as follows:
| Parameters | Values |
| --- | --- |
| (u, std) for XPR of target | (9.60, 6.85) dB |
R1-2504364	FL Summary #2 on ISAC Scenarios and Calibrations	Moderator (AT&T)
From Friday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-deployment-scenarios-75cbe2f1-a011`

### [5G-A/Rel-19 RAN1#121] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
Resolve square brackets for Table 7.9.1-4: Evaluation parameters for Automated Guided Vehicles sensing scenarios:
| Sensing Target | 3D mobility | Horizontal velocity with random straight-line trajectory Option 1: Uniform distribution in the range of up to 30 km/h Option 2: Fixed velocities {3, 10} km/h |
| --- | --- | --- |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-deployment-scenarios-75cbe2f1-a012`

### [5G-A/Rel-19 RAN1#121] `conclusion` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
Channel model for ISAC for SMa scenario will not be fully studied in Rel-19.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_121/) · `RAN1-121-isac-deployment-scenarios-75cbe2f1-c001`

### [5G-A/Rel-19 RAN1#120b] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
In order to generate Tx-target link, target-Rx link and the background channel, the above table on reference TRs (excluding the already agreed part) is adopted for the mapping between reference TRs and a pair of nodes (STX, SRX, target).
Note: continue discussion for updating the table with RSU type UE.
FFS: the generation of background channel based on reference TRs is subject to the addition of low-energy clusters.
Case
Node 1
Node 2
Existing TRs as starting point
1
TRP
TRP
Highway
TRP-UE link of scenario RMa in section 7 of TR 38.901 by setting hUE=35m for FR1
TRP-TRP link of scenario UMa following the option based on TR 38.901 defined in section A.3 of TR 38.858
Urban grid
TRP-TRP link of scenario UMa following the option based on TR 38.901 defined in section A.3 of TR 38.858
HST
TRP-UE link of scenario RMa in section 7 of TR 38.901 by setting hUE=35m for FR1
TRP-TRP link of scenario UMa in section A.3 of TR 38.858 for FR2
4
TRP
aerial UE
UMa-AV, UMi-AV, and RMa-AV
Reuse the channel model of scenario UMa-AV, UMi-AV, and RMa-AV of FR1 for FR2
5
normal UE
normal UE
For pedestrian type UE:
Highway and Urban grid
P2P link in section 6 of TR 37.885
HST
TRP-UE link of scenario RMa in section 7 of TR 38.901 for FR1, e.g., hBS=1.5m, UE-UE link of scenario UMa following the option based on TR 38.901 defined in section A.3 of TR 38.858 for FR2
6
normal UE
vehicle UE
UMi, UMa, RMa
UE-UE link of scenario UMi, UMa following the option based on TR 38.901 defined in section A.3 of TR 38.858
TRP-UE link of scenario RMa defined in section 7 of TR 38.901 by setting hBS =1.5m
For pedestrian type UE:
Highway and Urban grid
V2P link in section 6 of TR 37.885
7
normal UE
aerial UE
UMi-AV, UMa-AV, and RMa-AV
TRP-aerial UE link of UMi-AV in Annex A and B of TR 36.777 by setting hBS =1.5m for FR1
LOS probability is not reused, FFS new LOS probability
FFS pathloss model, shadowing fading
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120b/) · `RAN1-120b-isac-channel-modelling-fa5b802a-a001`

### [5G-A/Rel-19 RAN1#120b] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
To generate the parameters (in the steps before concatenation), the large-scale parameters and the small-scale parameters used to generate the Tx-target link are respectively the same as that of the target-Rx link for monostatic sensing, where departure angle on one link and arrival angle on the other link are reciprocal.
FFS: whether this applies to initial phase
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120b/) · `RAN1-120b-isac-channel-modelling-fa5b802a-a002`

### [5G-A/Rel-19 RAN1#120b] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
Normalization on the product of three polarization matrixes of a direct/indirect path generated by stochastic cluster, i.e., CPMtx,sp,rx= CPMsp,rx . CPMsp . CPMtx,sp is supported
The scaling factor is
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120b/) · `RAN1-120b-isac-channel-modelling-fa5b802a-a003`

### [5G-A/Rel-19 RAN1#120b] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
Power normalization of target channel after path dropping of the target channel is not supported.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120b/) · `RAN1-120b-isac-channel-modelling-fa5b802a-a004`

### [5G-A/Rel-19 RAN1#120b] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
On the monostatic RCS for human with RCS model 2
The monostatic RCS for a scattering point of the target is generated by
The values/pattern A*B1, i.e.,  is deterministic based on incident/scattered angles
Where,
FFS how many rows of the values/pattern A*B1 are defined for the target
Note: each row has a defined applicable range of  and
Note: whether the RCS is elevation angle dependent or dependent on both elevation and horizontal angles can be separately discussed
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120b/) · `RAN1-120b-isac-channel-modelling-fa5b802a-a005`

### [5G-A/Rel-19 RAN1#120b] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
The following mean and standard deviation values of XPR of targets are agreed for monostatic sensing and bistatic sensing as follows:
UAV: (13.75, 7.07) dB
Human: (19.81, 4.25) dB
Vehicle: (21.12, 6.88) dB
R1-2502554	Summary #2 on ISAC channel modelling	Moderator (Xiaomi)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120b/) · `RAN1-120b-isac-channel-modelling-fa5b802a-a006`

### [5G-A/Rel-19 RAN1#120b] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
When spatial consistency is enabled, the 1-by-1 random coupling generated by concatenation Option 3 is not updated per simulation drop even if Tx, target, Rx positions change during simulation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120b/) · `RAN1-120b-isac-channel-modelling-fa5b802a-a007`

### [5G-A/Rel-19 RAN1#120b] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
The following working assumption is confirmed.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120b/) · `RAN1-120b-isac-channel-modelling-fa5b802a-a008`

### [5G-A/Rel-19 RAN1#120b] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
On background channel for mono-static sensing, the following details are provided:
reference points are dropped for one Tx, based on the Gamma distribution for distance and height of reference point.
The LOS AOD between Tx and the first reference point, which is denoted as AOD1, is generated based on uniform distribution .
The LOS AOD between Tx and the second reference point is AOD1 +
The LOS AOD between Tx and the third reference point is AOD1 +
The background channel is generated based on the channel generated as in existing TR between the real Tx and the reference point assuming NLOS condition.
The antenna field pattern and array orientation of reference point are set same as Tx.
Arrival angles for both azimuth and elevation  and  are set equal to departure angles.
The absolute delay model d3D and  as agreed for bistatic sensing for the same sensing scenario applies. Down-select one option from the following:
Option 0: no scaling factor is applied to d3D.
Option 1: An offset is applied to d3D, i.e., d3D-c1.
Option 2: A scaling factor d_s is multiplied to d3D, i.e., d3D*d_s. d_s is a value within range [0, 1].
Note: The adjustment of absolute delay doesn’t impact the generation of NLOS clusters between the Tx and each reference point.
The mono-static background channel for the Tx would be sum of channels of the links between the Tx and all related reference points, which is
FFS: Doppler frequency in background channel for monostatic sensing.
The rays in a stochastic cluster with ZOA at BS less than D degree are dropped.
D=[90] for RMa.
D=[60] for UMa.
D=[50] for UMi.
Note: this threshold for ZOA is not applicable to other sensing scenarios.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120b/) · `RAN1-120b-isac-channel-modelling-fa5b802a-a009`

### [5G-A/Rel-19 RAN1#120b] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
To generate the background channel, the power threshold (-25 dB) for removing clusters in step 6 in section 7.5, TR 38.901 is reused.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120b/) · `RAN1-120b-isac-channel-modelling-fa5b802a-a010`

### [5G-A/Rel-19 RAN1#120b] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
The ISAC background channel can be generated between a sensing Tx and a sensing Rx or RP (relevant for monostatic case) via the following steps:
Step 1: generate a first set of clusters/rays according to TR 38.901(or other related TRs)
Step 2: generate a second set of NLOS clusters/rays according to TR 38.901 (or other related TRs), where the power of the second set of clusters/rays should be scaled down such that
is the power of the NLOS cluster with the strongest power from the first set.
is the power of the n-th cluster from the second set.
Where, N is the number of clusters, M is the number of rays within each cluster, value of G relates to power
N=360, M=1, G = -25dB, no further change from 38.901, 36.777, 38.858 (i.e., utilizing the same DS, ASA, ASD, ZSA, ZSD, ,  as used for the first step).
The step 2 is an additional modeling component.
For email discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120b/) · `RAN1-120b-isac-channel-modelling-fa5b802a-a011`

### [5G-A/Rel-19 RAN1#120b] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
For human as a sensing target with a single scattering point, the height of the scattering point is 1.5 m.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120b/) · `RAN1-120b-isac-channel-modelling-fa5b802a-a012`

### [5G-A/Rel-19 RAN1#120b] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
In sensing scenario UMi, UMa, RMa, if the height of a scattering point of target is less than 1.5m, for pathloss calculation, down-selection one of the options below:
Option 4: use  in Table 7.4.1-1: Pathloss models in TR 38.901.
Option 5: use hUT 1.5 m for pathloss calculation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120b/) · `RAN1-120b-isac-channel-modelling-fa5b802a-a013`

### [5G-A/Rel-19 RAN1#120b] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
For sensing scenario UMi, UMa, RMa, UMi-AV, UMa-AV and RMa-AV, the height of a scattering point of a target is used to calculate the LOS probability and pathloss, regardless of the lower bound in the existing TRs that are referred to generate ISAC channel.
FFS for the case where the height of a scattering point of target is less than 1.5m in sensing scenario UMi, UMa, RMa.
For email approval
[FL3] Proposal 4.2.1-1
On the monostatic RCS of UAV of large size,
The values/pattern of component A*B1 are generated by the following parameters
|  |  |  |  |  |  |  | Applicable Range of | Applicable Range of |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Left | 90° | 7.13° | 90° | 8.68° | 7.43 | 14.30 | [45°,135°] | [45°,135°] |
| Back | 180° | 10.09° | 90° | 11.43° | 3.99 | 10.86 | [45°,135°] | [135°,225°] |
| Right | 270° | 7.13° | 90° | 8.68° | 7.43 | 14.30 | [45°,135°] | [225°,315°] |
| Front | 0° | 14.19° | 90° | 16.53° | 1.02 | 7.89 | [45°,135°] | [-45°,45°] |
| Bottom | / | / | 180° | 4.93° | 13.55 | 20.42 | [135°,180°] | [0°,360°] |
| Roof | / | / | 0° | 4.93° | 13.55 | 20.42 | [0°,45°] | [0°,360°] |
When  is in the range [0°,45° ] or [135°,180°],
The standard deviation of component B2 is 2.50 dB
For email approval
[FL3] Proposal 4.2.3-1
On the monostatic RCS of AGV with single scattering point,
The values/pattern of component A*B1 are generated by the following parameters
|  |  |  |  |  |  |  | Applicable Range of | Applicable Range of |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Left | 90° | 19.45° | 75° | 19.45° | 7.33 | 17.59 | [30°,180°] | [45°,135°] |
| Back | 180° | 13.68° | 90° | 13.68° | 11.01 | 21.27 | [30°,180°] | [135°,225°] |
| Right | 270° | 19.45° | 75° | 19.45° | 7.33 | 17.59 | [30°,180°] | [225°,315°] |
| Front | 0° | 13.68° | 90° | 13.68° | 13.02 | 23.29 | [30°,180°] | [-45°,45°] |
| Roof | / | / | 0° | 16.57° | 11.79 | 22.05 | [0°,30°] | [0°,360°] |
When  is in the range [0°,30° ),
The standard deviation of component B2 is 2.51 dB
Final summary in R1-2503146.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120b/) · `RAN1-120b-isac-channel-modelling-fa5b802a-a014`

### [5G-A/Rel-19 RAN1#120b] `proposal` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
The values of the parameters to generate background channel for TRP monostatic and UE monostatic sensing for each sensing scenario are provided in the following table.
FFS parameter values for other scenarios (e.g. indoor factory).
Email discussion/approval checking the values after April meeting, including validation for newly agreed parameters.
The email discussion includes all scenarios, TRP monostatic and UE monostatic.
The email discussion includes how to merge results provided by companies.
| Scenario | Uma / Urban grid / Highway (FR2) / HST(FR2), (TRP monostatic) | UMi, (TRP monostatic) | Rma / Highway (FR1) / HST(FR1) . (TRP monostatic) | Indoor office (TRP monostatic) | Indoor office (UE monostatic) |  |
| --- | --- | --- | --- | --- | --- | --- |
| Distribution of 2D distance between Tx and reference points 1 |  | 10.3370 | 6.1996 | 6.2025 | 4.236 | 4.3733 |
|  |  | 0.1317 | 0.1558 | 0.0391 | 0.19255 | 0.4457 |
|  |  | 68.7778 | 15.2697 | 1.2940 | 4.99 | 4.6302 |
| Distribution of height of reference points |  | 16.2253 | 12.0487 | 0.0007 | 1.3293 | 0.2974 |
|  |  | 1.9218 | 2.3261 | 5.0146 | 0.1442 | 0.4103 |
|  |  | 2.6142 | 0.0157 | 0.0522 | 13.19 | 2.9711 |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120b/) · `RAN1-120b-isac-channel-modelling-fa5b802a-p001`

### [5G-A/Rel-19 RAN1#120b] `working_assumption` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
Reuse the channel model of scenario UMa-AV, UMi-AV, and RMa-AV of FR1 for FR2
The corresponding parameter values in FR2 are used
8
vehicle UE
vehicle UE
Highway and Urban grid
V2V link of scenario Highway and Urban grid in section 6 of TR 37.885
UMi, UMa, and RMa
UE-UE link of scenario UMi, UMa following the option based on TR 38.901 defined in section A.3 of TR 38.858
TRP-UE link of scenario RMa defined in section 7 of TR 38.901 by setting hBS =1.5m
9
aerial UE
aerial UE
UMi-AV, UMa-AV, RMa-AV
TRP-aerial UE link of UMi-AV in Annex A and B of TR 36.777 by setting height of TRP equal to the height of the first aerial UE for FR1
LOS probability is not reused, FFS new LOS probability
FFS pathloss model, shadowing fading, angular spread
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120b/) · `RAN1-120b-isac-channel-modelling-fa5b802a-w001`

### [5G-A/Rel-19 RAN1#120b] `working_assumption` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
Reuse the channel model of scenario UMa-AV, UMi-AV, and RMa-AV of FR1 for FR2
The corresponding parameter values in FR2 are used
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120b/) · `RAN1-120b-isac-channel-modelling-fa5b802a-w002`

### [5G-A/Rel-19 RAN1#120b] `working_assumption` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
Absolute delay model (referring to 7.6.9 in TR 38.901 as starting point) is a mandatory feature for both target channel and background channel for ISAC for UMi, UMa, InH, InF
Related model referring to  values from 7-24GHz study item
R1-2502555	Summary #3 on ISAC channel modelling	Moderator (Xiaomi)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120b/) · `RAN1-120b-isac-channel-modelling-fa5b802a-w003`

### [5G-A/Rel-19 RAN1#120b] `working_assumption` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
For vehicle with single/multiple scattering points, the bistatic RCS is generated by
The values/pattern of A*B1 of bistatic RCS is given by:
where
is applied to the  within 0~180 degrees. k1= 6 and k2=1.65.  is the bistatic angle between the incident ray and scattering ray within the plane of incident direction () and scattering direction ().
The angles of () are the projections of the bisector angle on the vertical plane and the horizontal plane, respectively.
FFS: RCS value when  is 180 degrees
The effect of forward scattering  is -Inf in Rel-19
5 sets of parameters Applicable Range of  and Applicable Range of  are applicable as defined for the monostatic RCS of vehicle with single/multiple SPSTs
Continue study on a new formula for  to resolve the issue of angular discontinuity.
The new formula should retain following property: the linear bistatic RCS for a vehicle with single scattering point is the sum of the bistatic RCS of the multiple scattering points of the vehicle
the following formula can be a reference for the study
Note: the working assumption agreed on Thursday was updated on Friday as follows: k1= 6 and k2=1.65
R1-2502556	Summary #4 on ISAC channel modelling	Moderator (Xiaomi)
From Friday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120b/) · `RAN1-120b-isac-channel-modelling-fa5b802a-w004`

### [5G-A/Rel-19 RAN1#120b] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
For the purposes of large scale calibration for UAV sensing targets, the following revised calibration parameters are proposed below in Table x. Note that the change bars are against the agreements from RAN1#120.
Table x. Simulation assumptions for large scale calibration for UAV sensing targets
| Parameters | Values |
| --- | --- |
| Scenario | UMa-AV |
| Sensing mode | TRP monostatic, TRP-TRP bistatic, TRP-UE bistatic, UE-UE bistatic |
| Target type | UAV of small size (0.3m x 0.4m x 0.2m) |
| Sectorization | Single 360-degree sector can be assumed |
| Carrier Frequency | FR1: 6 GHz FR2: 30 GHz |
| BS antenna configurations | Single dual-pol isotropic antenna |
| BS Tx power | FR1: 56dBm FR2: 41dBm |
| Bandwidth | FR1: 100MHz FR2: 400MHz |
| BS noise figure | FR1: 5dB FR2: 7dB |
| UT antenna configurations | Single dual-pol isotropic antenna; (M,N,P,Mg,Ng;Mp,Np) = (1,1,2,1,1;1,1) |
| UT noise figure | FR1: 9dB FR2: 10dB |
| UT height | 1.5m for terrestrial UTs, |
| UT Tx power | 23dBm |
| UT Distribution | • The overall number of UTs is 30 uniformly distributed in the center cell. • All of the UTs are either terrestrial UTs or aerial UTs, all outdoors. • Vertical distribution of aerial UE: Fixed height value of 200 m. • FR1 is assumed for aerial UE. |
| Sensing target distribution | 1 target uniformly distributed (across multiple drops) within the center cell. Vertical distribution: Fixed height value of 200 m. |
| Component A of the RCS for each scattering point | -12.81 dBsm |
| Minimum 3D distances between pairs of Tx/Rx and sensing target | 10 m |
| Wrapping Method | No wrapping method is used if interference is not modelled, otherwise geographical distance based wrapping |
| Coupling loss for target channel | power scaling factor (pathloss, shadow fading, and RCS component A included): |
| Sensing Tx/Rx selection | Best N = 4 Tx-Rx pairs to be selected for the target. NOTE1: Based on the Tx-Rx pairs with the smallest power scaling factor of the target channel. |
| Metrics | Coupling loss for target channel Coupling loss for background channel (in case of monostatic sensing, this is the coupling loss between Tx and one reference point) Note: CDFs can be separately generated for target channel, background channel |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120b/) · `RAN1-120b-isac-deployment-scenarios-75cbe2f1-a001`

### [5G-A/Rel-19 RAN1#120b] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
For the purposes of full calibration for UAV sensing targets, the following calibration parameters are proposed below in Table x.
Table x. Simulation assumptions for full calibration for UAV sensing targets
| Parameters | Values |
| --- | --- |
| Scenario | UMa-AV |
| Sensing mode | TRP monostatic, TRP-TRP bistatic, TRP-UE bistatic, UE-UE bistatic |
| Target type | UAV of small size (0.3m x 0.4m x 0.2m) |
| Sectorization | Single 360-degree sector can be assumed |
| Carrier Frequency | FR1: 6 GHz FR2: 30 GHz |
| BS antenna configurations | Single dual-pol isotropic antenna |
| BS Tx power | FR1: 56dBm FR2: 41dBm |
| Bandwidth | FR1: 100MHz FR2: 400MHz |
| BS noise figure | FR1: 5dB FR2: 7dB |
| UT antenna configurations | Single dual-pol isotropic antenna; (M,N,P,Mg,Ng;Mp,Np) = (1,1,2,1,1;1,1) |
| UT noise figure | FR1: 9dB FR2: 10dB |
| UT height | 1.5m for terrestrial UTs |
| UT Tx power | 23dBm |
| UT Distribution | The overall number of UTs is 30 uniformly distributed in the center cell. All of the UTs are either terrestrial UTs or aerial UTs, all outdoors. Vertical distribution of aerial UE: Fixed height value of 200 m. FR1 is assumed for aerial UE. |
| Sensing target distribution | 1 target uniformly distributed (across multiple drops) within the center cell. Vertical distribution: Fixed height value of 200 m. |
| RCS for each scattering point | Component A: -12.81 dBsm Component B1: 0 dB Component B2: 3.74 dB for standard deviation The same values are used for monostatic RCS and bistatic RCS |
| Minimum 3D distances between pairs of Tx/Rx and sensing target | 10 m |
| Wrapping Method | No wrapping method is used if interference is not modelled, otherwise geographical distance based wrapping |
| Fast fading model | TR 36.777 Annex B.1.3 |
| (u, std) for XPR of target | Mean 13.75 dB, deviation 7.07 dB |
| The power threshold for path dropping after concatenation for target channel | FFS |
| The power threshold for removing clusters in step 6 in section 7.5, TR 38.901 for background channel | FFS |
| Coupling loss for target channel | By definition, need to consider all direct and indirect paths. The following parameters are included in the calculation: power scaling factor (pathloss, shadow fading, and RCS component A included) for small scale RCS B1/B2 and power of rays in Tx-target/target-Rx links (), Tx/Rx antenna pattern, 3 polarization matrixes, i.e., |
|  |  |
| Sensing Tx/Rx selection | Best N = 4 Tx-Rx pairs to be selected for the target. NOTE1: Based on the Tx-Rx pairs with the smallest power scaling factor of the target channel. |
| Absolute delay | The model of UMa scenario defined in TR 38.901 7-24GHz channel modeling [ref] is reused for UMa-AV for all sensing modes. |
| Metrics | Coupling loss for target channel Coupling loss for background channel (in case of monostatic sensing, this is the linear sum of coupling losses between Tx/Rx and all reference points) Note: CDFs can be separately generated for target channel, background channel CDF of Delay Spread and Angle Spread (ASD, ZSD, ASA, ZSA). Definition of Delay Spread is similar to the definition of angle spread in Annex A of TR 25.996, Definition of Angle Spread can ref to Annex A of TR 25.996. |
R1-2502733	FL Summary #3 on ISAC Scenarios and Calibrations	Moderator (AT&T)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120b/) · `RAN1-120b-isac-deployment-scenarios-75cbe2f1-a002`

### [5G-A/Rel-19 RAN1#120b] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
For the purposes of large scale calibrations for Automotive sensing targets, the following parameters are proposed below in Table x.
FFS: which type of UE is used for UT in different sensing mode
FFS: impact of spatial consistency, if any, in case of vehicle with 5 scattering points
FFS: cell layout for ISD = 250 m
Table x. Simulation assumptions for large scale calibration for Automotive sensing targets
| Parameters | Values |
| --- | --- |
| Scenario | For FR1: Urban Grid (ISD=500m, BS height=25m) Highway (ISD=1732m, BS height=35m) For FR2: Urban Grid (ISD=250m, BS height=25m) Highway (ISD=500m, BS height=35m) |
| Sensing mode | TRP monostatic, TRP-TRP bistatic, TRP-UE bistatic, UE-UE bistatic, UE monostatic |
| Target type | Vehicle type 2 [TR37.885] |
| Sectorization | Single 360-degree sector can be assumed |
| Carrier Frequency | FR1: 6 GHz FR2: 30 GHz |
| BS antenna configurations | Single dual-pol isotropic antenna |
| BS Tx power | FR1: 56dBm FR2: 41dBm |
| Bandwidth | FR1: 100MHz FR2: 400MHz |
| BS noise figure | FR1: 5dB FR2: 7dB |
| UT antenna configurations | Single dual-pol isotropic antenna, (M,N,P,Mg,Ng;Mp,Np) = (1,1,2,1,1;1,1) |
| UT noise figure | FR1: 9dB FR2: 10dB |
| UT height | 1.5m for pedestrian type UE 5m for RSU type UE 1.6m for vehicle type UE |
| UT Tx power | 23dBm |
| UT Distribution | Per TR37.885 |
| Sensing target distribution | Per TR37.885: - Option A - Vehicle type distribution: 100% vehicle type 2. - Clustered dropping is not used. - Highway: one target uniformly distributed (across multiple drops) within the simulation region. Vehicle speed is 140 km/h in all the lanes as baseline. - Urban Grid: one target is uniformly distributed (across multiple drops) within the center road grid. Vehicle speed is 60 km/h in all the lanes as baseline. NOTE: vehicle is dropped with 5 scattering points (front/left/right/back/roof) and each point has one location, or vehicle is dropped with 1 scattering points |
| Component A of the RCS for each scattering point | -20dBsm |
| Minimum 3D distances between pairs of Tx/Rx and sensing target | 10 m |
| Wrapping Method | As defined in urban grid/highway scenario |
| Coupling loss for target channel | Power scaling factor (pathloss, shadow fading, and RCS component A included) |
| Sensing Tx/Rx selection | Best N= Tx-Rx pairs to be selected for the target. For urban grid N = 4 For Highway N = 4 NOTE: Based on the Tx-Rx pair with the smallest power scaling factor of the target channel. |
| Metrics | Coupling loss for target channel Coupling loss for background channel (in case of monostatic sensing, this is the coupling loss between Tx and one reference point) Note: CDFs can be separately generated for target channel, background channel |
Final summary in R1-2502734.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120b/) · `RAN1-120b-isac-deployment-scenarios-75cbe2f1-a003`

### [5G-A/Rel-19 RAN1#120] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
For bistatic/monostatic RCS
RCS values/pattern for a scattering point of a target for bistatic sensing is generated by A*B1*B2 (i.e., Option 3 from the agreement in RAN1 #118bis)
RCS values/pattern obtained by setting the same incident/scattered angle in the RCS model for bistatic sensing should be aligned with RCS for monostatic sensing
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120/) · `RAN1-120-isac-channel-modelling-fa5b802a-a001`

### [5G-A/Rel-19 RAN1#120] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
RCS model and application in ISAC channel generation
To define the RCS model (RCS=A*B1*B2) for a scattering point of a target, when the target type is vehicle, large size UAV, human with RCS model 2, AGV
The values/pattern of the product of component A and B1, i.e., A*B1 is given per target type, expressed in dBsm scale
Component A is expressed in dBsm scale. B1 is dependent on A*B1 and value of component A.
A is equal to a single value per target type
FFS: this allows different values for the same target type with different size, if needed
FFS: this allows different values for monostatic and bistatic sensing, if needed
Component B2 follows log-normal distribution. The mean  and variance  used to characterize  satisfied a fixed relation .
In the procedure of generating ISAC target channel, B1*B2 is applied after coupling of rays for a STX-SPST link and the corresponding SPST-SRX link before path dropping
In the procedure of generating ISAC target channel, the following power scaling factor is applied in the last step in target channel generation (i.e., step 14 in the running CR).
Where,
is pathloss between Tx and SPST, where  is the distance between Tx and SPST
is pathloss between Rx and SPST, where  is the distance between SPST and Rx
is the value of RCS component A
are shadow fading respectively generated for the Tx- SPST link and SPST -Rx link referring to step 4 in section 7.5, TR 38.901
Note: for monostatic sensing,
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120/) · `RAN1-120-isac-channel-modelling-fa5b802a-a002`

### [5G-A/Rel-19 RAN1#120] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
RCS upper bound: k equals to 3 is adopted to derive the upper bound of RCS component B2, kσ, where σ is the standard deviation of B2 in dB.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120/) · `RAN1-120-isac-channel-modelling-fa5b802a-a003`

### [5G-A/Rel-19 RAN1#120] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
For reducing options for reference TRs: for sensing scenario UMi, UMa, RMa, InH, InF, UMi-AV, UMa-AV, and RMa-AV, the reference TR to generate a TRP-TRP channel is:
TRP-TRP link of scenario UMi, UMa, InH, and InF following the option based on TR 38.901 defined in section A.3 of TR 38.858
For InF, hUE is changed to the same height as the BS
TRP-UE link of scenario RMa defined in section 7 of TR 38.901 by setting hUE=35m
FFS: whether to add very low power clusters
R1-2501000	Summary #2 on ISAC channel modelling	Moderator (Xiaomi)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120/) · `RAN1-120-isac-channel-modelling-fa5b802a-a004`

### [5G-A/Rel-19 RAN1#120] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
For vehicle with single/multiple scattering points:
For mono-static, the RCS=A*B=A*B1*B2 for a scattering point of a vehicle is generated by
The values/pattern A*B1, i.e.,  is deterministic based on incident/scattered angles
Where,
,
,
For example, in case of vehicle with multiple scattering points:
|  |  |  |  |  |  |  | Applicable Range of | Applicable Range of |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Left | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Back | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Right | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Front | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Roof | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
Note: the applicable angular range is 360 degrees per row in horizontal domain in case of vehicle with multiple scattering points, and the applicable angular range is < 360 degrees per row in horizontal domain in case of vehicle with a single scattering point.
FFS: angular continuity
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120/) · `RAN1-120-isac-channel-modelling-fa5b802a-a005`

### [5G-A/Rel-19 RAN1#120] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
The existing spatial consistency model in TR 38.901 is reused to model correlation of links between one TRP and different STs/UEs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120/) · `RAN1-120-isac-channel-modelling-fa5b802a-a006`

### [5G-A/Rel-19 RAN1#120] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
Spatial consistency is not modelled at least for the following links
Case 1: the links from/to two non-co-located TRPs
Link TRP1-X and link TRP2-X, where node X can be a target, a UE or another TRP
Link TRP1-X and link TRP2-Y, where node X, Y can be a target, a UE or another TRP
Case 2: the two links with different LOS/NLOS condition
Case 3: background channel for monostatic vs. any link (Tx-ST, ST-Rx, background channel) for bistatic
R1-2501001	Summary #3 on ISAC channel modelling	Moderator (Xiaomi)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120/) · `RAN1-120-isac-channel-modelling-fa5b802a-a007`

### [5G-A/Rel-19 RAN1#120] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
For sensing scenario UMi, UMa, RMa, InH, InF, UMi-AV, UMa-AV, and RMa-AV, the reference TR to generate a UE-UE channel is
UE-UE link of scenario UMi, UMa, InH, and InF following the option based on TR 38.901 defined in section A.3 of TR 38.858
TRP-UE link of scenario RMa defined in section 7 of TR 38.901 by setting hBS =1.5m
FFS: whether to add very low power clusters
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120/) · `RAN1-120-isac-channel-modelling-fa5b802a-a008`

### [5G-A/Rel-19 RAN1#120] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
The reference TR to generate a TRP-UE channel is
| TRP | normal UE | UMi, UMa, RMa, InH, InF, UMi-AV, UMa-AV, and RMa-AV Option 1: TRP-UE link of scenario UMi, UMa, RMa, InH, and InF in section 7 of TR 38.901 Highway and Urban grid Option 1: P2B link of scenario Highway and Urban grid in section 6 of TR 37.885 HST Option 1: TRP-UE link of scenario RMa in section 7 of TR 38.901 for FR1 and TRP-UE link of scenario UMa in section 7 of TR 38.901 for FR2 |
| --- | --- | --- |
| TRP | vehicle UE | Highway and Urban grid Option 1: V2B link of scenario Highway and Urban grid in section 6 of TR 37.885 UMi, UMa, and RMa Option 1: TRP-UE link of scenario UMi, UMa, and RMa in section 7 of TR 38.901 |
| TRP | aerial UE | UMa-AV, UMi-AV, and RMa-AV Option 1: TRP-aerial UE link of scenario UMa-AV, UMi-AV, and RMa-AV in section Annex A and B of TR 36.777 for FR1 FFS reuse the channel model of scenario UMa-AV, UMi-AV, and RMa-AV of FR1 for FR2 |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120/) · `RAN1-120-isac-channel-modelling-fa5b802a-a009`

### [5G-A/Rel-19 RAN1#120] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
For mono-static, the following values of component A, B2 are agreed for UAV of small size
Component A: -12.81 dBsm
Component B1: 0 dB (already agreed in RAN1#118bis)
Component B2:
standard deviation: 3.74 dB
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120/) · `RAN1-120-isac-channel-modelling-fa5b802a-a010`

### [5G-A/Rel-19 RAN1#120] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
For mono-static, the following values of component A, B2 are agreed for RCS model 1 of human
Component A: -1.37 dBsm
Component B1: 0 dB (already agreed in RAN1#118bis)
Component B2:
standard deviation: 3.94 dB
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120/) · `RAN1-120-isac-channel-modelling-fa5b802a-a011`

### [5G-A/Rel-19 RAN1#120] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
When absolute delay model  is configured, it applies to all NLOS clusters in each of Tx-target and target-Rx links and background channel.
For bistatic sensing: Different values of  are separately generated for the Tx-target link, target-Rx link and the background channel
For monostatic sensing: the same value of  is used for Tx-target link and target-Rx link, and a different value of  is separately generated for the background channel
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120/) · `RAN1-120-isac-channel-modelling-fa5b802a-a012`

### [5G-A/Rel-19 RAN1#120] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
To generate the LOS ray and NLOS clusters for the multiple scattering points, each scattering point is separately handled as if a different target with single scattering point.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120/) · `RAN1-120-isac-channel-modelling-fa5b802a-a013`

### [5G-A/Rel-19 RAN1#120] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
The LOS condition between Tx/Rx and each of the multiple scattering points of a same target are individually generated
The pathloss between Tx/Rx and each of the multiple scattering points of a same target are individually generated
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120/) · `RAN1-120-isac-channel-modelling-fa5b802a-a014`

### [5G-A/Rel-19 RAN1#120] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
For a target with single/multiple scattering points, the 3D location of each scattering point is defined in the evaluation assumptions.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120/) · `RAN1-120-isac-channel-modelling-fa5b802a-a015`

### [5G-A/Rel-19 RAN1#120] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
Spatial consistency is needed to model correlation of the following links from ST-UT links and UT-UT links
Case 5: links between same UT and two nodes X/Y, subjected to correlation distance, i.e., link UT1-X and link UT1-Y, where nodes X/Y can be target or UT
Case 6: links between same target and two nodes X/Y, subjected to correlation distance, i.e., link target1-X and link target1-Y, where nodes X, Y are different UTs
Case 7: link X1-Y1 and link X2-Y2, subjected to correlation distance, where X1, X2, Y1, Y2 are 4 different nodes
FFS: Spatial consistency between multiple scattering points of the same target
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120/) · `RAN1-120-isac-channel-modelling-fa5b802a-a016`

### [5G-A/Rel-19 RAN1#120] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
Correlation type is introduced for large scale parameter, cluster specific parameter and ray specific parameter of ST-UT links and UT-UT links
Definition of link Correlated: parameters for any two links between STs/UTs are correlated, subjected to correlation distance.
Table 4: Correlation type for links between STs/UTs
| Parameters | Correlation type |
| --- | --- |
| Delays | link Correlated |
| Cluster powers | link Correlated |
| AOA/ZOA/AOD/ZOD offset | link Correlated |
| AOA/ZOA/AOD/ZOD sign | link Correlated |
| Random coupling | link Correlated |
| XPR | link Correlated |
| Initial random phase | link Correlated |
| LOS/NLOS states | link Correlated |
| Blockage (Model A) | All-correlated |
| O2I penetration loss | All-correlated |
| Indoor distance | All-correlated |
| Indoor states | All-correlated |
Note: it is not precluded more parameters for spatial consistency can be discussed and added in the table
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120/) · `RAN1-120-isac-channel-modelling-fa5b802a-a017`

### [5G-A/Rel-19 RAN1#120] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
If a target is modelled with multiple scattering points,
The number of scattering points of the target is generated in the beginning of the simulation and kept unchanged in the whole simulation
The number and locations of the scattering points of the target (if it is a vehicle) are common to each pair of sensing Tx/Rx
RAN1 assumes no ray is scattered from one scattering point to another scattering point of the same target
RCS values of the multiple scattering points are individually determined
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120/) · `RAN1-120-isac-channel-modelling-fa5b802a-a018`

### [5G-A/Rel-19 RAN1#120] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
To model polarization matrix  of a direct/indirect path i of a scattering point of a target
in Rel-19 study item (e.g., UAV, human, vehicle, AGV), , , i.e.,
Where,
is XPR ratio is randomly generated by log-normal distribution per target type
The initial random phase  is uniformly distributed within
FFS: spatial consistency of random phase when a scattering point moves
FFS: whether the base station rotation procedure in 38.901 can be reused to support rotation of the target
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120/) · `RAN1-120-isac-channel-modelling-fa5b802a-a019`

### [5G-A/Rel-19 RAN1#120] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
For target channel
The power threshold for removing clusters in step 6 in section 7.5, TR 38.901, i.e., -25 dB is reused to generate Tx-target link and target-Rx link
The power threshold for path dropping after concatenation is relaxed to [X=-40] dB
For background channel
The power threshold for removing clusters in step 6 in section 7.5, TR 38.901, i.e., [-25 dB] is reused to generated the background channel
FFS: whether to add additional very low power clusters
FFS: The reference power for removing cluster is the min (max. Tx-target link cluster power, max. target-Rx link cluster power)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120/) · `RAN1-120-isac-channel-modelling-fa5b802a-a020`

### [5G-A/Rel-19 RAN1#120] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
If EO type-2 is modelled in an indirect path, only specular reflection is modeled for EO type-2
polarization of the indirect path is product of polarization matrix of the target-Rx link, the target, and the Tx-target link, i.e., CPMtx,sp,rx= CPMsp,rx . CPMsp . CPMtx,sp
For the specular reflected ray generated by a EO type-2 in the Tx-target link or the target-Rx link (i.e., Tx-EO type-2-target, or target-EO type-2-Rx), CPMtx,sp or CPMsp,rx is the polarization matrix of EO type-2
To generate polarization matrix of EO type-2, the procedure in [R1-2409394, R1-2410648] is taken as starting point
FFS applicability if the surface of EO type-2 is tilted
Final summary in R1-2501002.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120/) · `RAN1-120-isac-channel-modelling-fa5b802a-a021`

### [5G-A/Rel-19 RAN1#120] `working_assumption` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
For modelling background channel for monostatic sensing:
Solution A: (previous Option 1)
drop N reference point(s) following certain distribution, and then the background channel is generated based on the channel generated as in existing TR between the real Tx and the reference point for a scenario.
The distance between Tx and the reference point, and the height of the reference point follow Gamma distribution,
1
FFS: value of N (N<4)
FFS: whether to add additional very low power clusters
FFS: any update to parameters e.g. angular distribution and delay spread
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120/) · `RAN1-120-isac-channel-modelling-fa5b802a-w001`

### [5G-A/Rel-19 RAN1#120] `working_assumption` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
Absolute delay model (referring to 7.6.9 in TR 38.901 as starting point) is a mandatory feature for both target channel and background channel for ISAC for UMi, UMa, InH, InF
Related model referring to  values from 7-24GHz study item
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120/) · `RAN1-120-isac-channel-modelling-fa5b802a-w002`

### [5G-A/Rel-19 RAN1#120] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
For ISAC channel modelling calibration, RAN1 considers both large-scale and full-scale calibration to include parameters and values for at least the following:
large scale parameters, where fast fading is not included
full-scale calibration parameters, which includes fast fading.
NOTE0: one part of calibration work does not include additional components and does not include spatial consistency
FFS: whether spatial consistency is specified as an additional component for ISAC CM
NOTE1: additional calibrations including spatial consistency can also be considered case by case for different scenarios.
NOTE2: Inclusion of EO in ISAC CM calibrations can also be considered case by case for different scenarios.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120/) · `RAN1-120-isac-deployment-scenarios-75cbe2f1-a001`

### [5G-A/Rel-19 RAN1#120] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
Calibration of ISAC CM includes separate calibration of the target channel and of the background channel
FFS: additional calibration for the combined channel (combination of target and background channel).
R1-2501078	FL Summary #3 on ISAC Scenarios and Calibrations	Moderator (AT&T)
Presented in Thursday morning session.
R1-2501574	FL Summary #4 on ISAC Scenarios and Calibrations	Moderator (AT&T)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120/) · `RAN1-120-isac-deployment-scenarios-75cbe2f1-a002`

### [5G-A/Rel-19 RAN1#120] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
For the purposes of large scale calibration for UAV sensing targets, the following calibration parameters are proposed below in Table x.
Table x. Simulation assumptions for large scale calibration for UAV sensing targets
| Parameters | Values |
| --- | --- |
| Scenario | UMa-AV |
| Sensing mode | TRP monostatic, TRP-TRP bistatic, TRP-UE bistatic, UE-UE bistatic Note: further down-selection of the sensing modes for UAV sensing is not precluded |
| Sectorization | 3 sectors per cell site: 30, 150 and 270 degrees |
| Carrier Frequency | FR1: 6 GHz FR2: 30 GHz |
| BS antenna configurations | Single dual-pol isotropic antenna |
| BS Tx power | FR1: 56dBm FR2: 41dBm |
| Bandwidth | FR1: 100MHz FR2: 400MHz |
| BS noise figure | FR1: 5dB FR2: 7dB |
| UT antenna configurations | (M,N,P,Mg,Ng;Mp,Np) = (1,1,2,1,1;1,1) |
| UT noise figure | FR1: 9dB FR2: 10dB |
| Sensing target distribution | 1 target uniformly distributed (across multiple drops) within the center cell. Vertical distribution: Fixed height value of 200 m. |
| Component A of the RCS for each scattering point | a fixed value of A |
| Minimum 3D distances between pairs of Tx/Rx and sensing target | 10 m |
| Wrapping Method | No wrapping method is used if interference is not modelled, otherwise geographical distance based wrapping |
| Metrics | Coupling loss (based on LOS pathloss) FFS: how to select sensing Tx and Rx FFS: additional metrics, wideband SIR and SINR based on RSRP if interference is modelled. |
Final summary in R1-2501607.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_120/) · `RAN1-120-isac-deployment-scenarios-75cbe2f1-a003`

### [5G-A/Rel-19 RAN1#119] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
Bistatic RCS values for a scattering point of a target are obtained by fixing an incident direction in LCS of target and varying the scattered directions in LCS of target; then changing to other incident direction.
R1-2410012	Summary #2 on ISAC channel modelling	Moderator (Xiaomi)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_119/) · `RAN1-119-isac-channel-modelling-fa5b802a-a001`

### [5G-A/Rel-19 RAN1#119] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
To generate indirect paths of NLOS ray + NLOS ray in the target channel
Option 0 is recommended, i.e., ray level full convolution between Tx-target link and target-Rx link for radio propagation Case 1/2/3/4
Option 3 to generate a reduced number of indirect paths of NLOS ray + NLOS ray is recommended, i.e., ray level 1-by-1 random coupling between Tx-target link and target-Rx link is supported for radio propagation Case 1/2/3/4
If number of rays in the two links are different, e.g., M1, M2 respectively for link 1 and link 2,
If M1<M2, randomly M1 rays are selected in link 2, otherwise randomly M2 rays are selected in link 1
Other methods are up to company choice for complexity reduction
Both option 0 and 3 will be calibrated independently. Company should report which option is used in calibration
The power threshold for path dropping is X=[-25] dB
X is relative to the strongest indirect path in the target channel
FFS: further power normalization of target channel is performed after path dropping,
Note: power normalization when target channel and background channel are combined can be discussed separately
FFS The set of remaining indirect paths can be updated during movement of Tx, target or Rx
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_119/) · `RAN1-119-isac-channel-modelling-fa5b802a-a002`

### [5G-A/Rel-19 RAN1#119] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
The following RCS models are supported when human is modelled with single scattering point for monostatic, where different RCS values and/or models can be supported for human due to different size, shape, frequency, etc.
Model 1
B1=0 dB
A is mean RCS value
B2 is modelled using log-normal distribution
Model 2
B1 have dependency on incident/scattered angles, with further down-selection among the alternatives below:
Alt 1: formulated similar as the antenna radiation power pattern in 38.901
Alt 2: a function
Alt 3: Lookup table
B2 is modelled using log-normal distribution
FFS RCS component A
FFS: conditions for using which model
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_119/) · `RAN1-119-isac-channel-modelling-fa5b802a-a003`

### [5G-A/Rel-19 RAN1#119] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
The following RCS model is supported when vehicle is modelled with single scattering point for monostatic, where different RCS values can be supported for vehicle due to different size, shape, frequency, etc.
B1 have dependency on incident/scattered angles, with further down-selection among the alternatives below:
Alt 1: formulated similar as the antenna radiation power pattern in 38.901
Alt 2: a function
Alt 3: Lookup table
B2 is modelled using log-normal distribution
FFS RCS component A
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_119/) · `RAN1-119-isac-channel-modelling-fa5b802a-a004`

### [5G-A/Rel-19 RAN1#119] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
When vehicle is modelled with multiple scattering points for monostatic, where different RCS values can be supported for vehicle due to different size, shape, frequency, etc.
the recommended five scattering points are located in front, left, back, right and roof side of the vehicle
the following RCS model is supported for each scattering point
B1 have dependency on incident/scattered angles, with further down-selection among the alternatives below:
Alt 1: formulated similar as the antenna radiation power pattern in 38.901
Alt 2: a function
Alt 3: Lookup table
B2 is modelled using log-normal distribution
FFS RCS component A
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_119/) · `RAN1-119-isac-channel-modelling-fa5b802a-a005`

### [5G-A/Rel-19 RAN1#119] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
EO type-1 (when modelled) is modelled in the same way as a sensing target in the ISAC channel model.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_119/) · `RAN1-119-isac-channel-modelling-fa5b802a-a006`

### [5G-A/Rel-19 RAN1#119] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
If blockage/forward scattering between sensing targets is not considered, a propagation path from Tx to Rx interacting with more than one sensing targets is not modelled.
FFS whether/how blockage/forward scattering can be modelled in the target channel.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_119/) · `RAN1-119-isac-channel-modelling-fa5b802a-a007`

### [5G-A/Rel-19 RAN1#119] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
Doppler for a target including both macro-Doppler and micro-Doppler can be modeled using a unified formula,
Where,
is the spherical unit vector at receiver for the link from Rx to the scattering point
is the spherical unit vector at transmitter for the link from Tx to the scattering point
is the spherical unit vector at the scattering point for the link from the scattering point to Rx
is the spherical unit vector at the scattering point for the link from the scattering point to Tx
Dual mobility model in 7.6.10, TR 38.901 is used as start point to model Doppler effect  due to movement of stochastic clusters, i.e.,
is only applicable for indirect path
Support one term of  for indirect path of LOS ray+NLOS ray, NLOS ray+LOS ray
Support two terms of   for indirect path of NLOS ray+NLOS ray
Doppler is separately determined for each of the multiple scattering points of a target
can include macro-Doppler and/or micro-Doppler motion,
FFS: maximum speed of moving scatterers
FFS: ratio of moving scatterers among all scatterers
R1-2410013	Summary #3 on ISAC channel modelling	Moderator (Xiaomi)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_119/) · `RAN1-119-isac-channel-modelling-fa5b802a-a008`

### [5G-A/Rel-19 RAN1#119] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
The following options are supported to generate the combined ISAC channel
Option 1: The ISAC channel of a pair of sensing Tx/Rx is obtained by summing the target channel(s) and background channel, i.e., power normalization is not performed.
Option 2: As an additional modelling component, power normalization is performed when summing the target channel(s) and background channel, to keep the same/similar channel power as the background channel without target. Down select between
Alt 1: Power normalization on both target channel and background channel
Alt 2: Power normalization on background channel only
Alt 3: the target channel of a target will replace one cluster in the background channel
FFS Blockage is modelled for the background channel due to sensing target and/or EO type-2
FFS condition to select option, e.g. depending on scenario, sensing mode, number of target/EO type-2
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_119/) · `RAN1-119-isac-channel-modelling-fa5b802a-a009`

### [5G-A/Rel-19 RAN1#119] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
To model the polarization matrix of a direct/indirect path at a scattering point of an object other than EO type-2, the polarization matrix of the scattering point, i.e.,  is modelled by  and initial random phases , i.e.,
The initial random phase  is [uniformly distributed within
FFS correlation between
FFS specular reflection
FFS: CPM normalization
The following options are considered for further study, down select one option from the following
Option 1: ,  is generated for path i, where  is XPR ratio
is randomly generated by log-normal distribution. FFS mean/variance of the distribution
Option 2: ,  are variables generated for path i
Option 3:  are variables generated for path i
defined in LCS
Option 4: ,  is generated for path i
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_119/) · `RAN1-119-isac-channel-modelling-fa5b802a-a010`

### [5G-A/Rel-19 RAN1#119] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
The finite size of the EO type-2 affects identification of specular reflection point. In the target channel, EO type-2 is modelled only if the specular reflection point is in the area of the EO type-2.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_119/) · `RAN1-119-isac-channel-modelling-fa5b802a-a011`

### [5G-A/Rel-19 RAN1#119] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
Component B2 of RCS is upper bounded by kσ dB for the log-normal distribution, where σ is the standard deviation of B2 in dB. FFS the value of k.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_119/) · `RAN1-119-isac-channel-modelling-fa5b802a-a012`

### [5G-A/Rel-19 RAN1#119] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
When the EO type-2 is modelled in the target channel, down select between the following options to determine the LOS condition of the Tx-target link and target-Rx link
Option A: If type-2 EO is in the LOS ray of one link, the link is determined as NLOS condition, and otherwise use the LOS probability equation to determine the LOS/NLOS condition
FFS changes to the LOS probability defined in existing TRs
FFS details on blockage by EO type-2
Option B: Use the LOS probability equation to determine the LOS/NLOS condition of one link, and then the impacts of type-2 EO is modeled by a blockage model.
Final summary in R1-2410014.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_119/) · `RAN1-119-isac-channel-modelling-fa5b802a-a013`

### [5G-A/Rel-19 RAN1#119] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
For UAV sensing target scenarios, the following table is agreed for deployment scenario parameters/values using the agreements from RAN1#118 as a baseline:
The detailed scenario description in this clause can be used for channel model calibration.
ISAC-UAV
Details on ISAC-UAV scenarios are listed in Table x.
Table x. Evaluation parameters for UAV sensing scenarios
| Parameters | Value |  |
| --- | --- | --- |
| Applicable communication scenarios | UMi, UMa, RMa [38.901] UMi-AV, UMa-AV, RMa-AV |  |
| Sensing transmitters and receivers properties | Rx/Tx Locations | Rx/Tx locations are selected among the TRPs and UEs locations in the corresponding communication scenarios. NOTE1: This may include aerial UEs for UMi-AV, UMa-AV, RMa-AV communication scenarios. In this case, other Rx/Tx properties (e.g. mobility) are also taken from the corresponding communication scenario. |
| Sensing target | LOS/NLOS | LOS and NLOS |
|  | Outdoor/indoor | Outdoor |
|  | 3D mobility | Horizontal velocity: uniform distribution between 0 and 180km/h, if horizontal velocity is not fixed to 0. Vertical velocity: 0km/h, optional {20, 40} km/h NOTE2: 3D mobility can be horizontal only or vertical only or a combination for each sensing target FFS: time-varying velocity. NOTE 3: time-varying velocity may be considered for future evaluations. |
|  | 3D distribution | Horizontal plane: Option A: N targets uniformly distributed within one cell. Option B: N targets uniformly distributed per cell. Option C: N targets uniformly distributed within an area not necessarily determined by cell boundaries. FFS: Value of N, defined area, and other distributions N = {1, 2, 3, 4, 5} NOTE4: N=0 may be considered for the evaluation of false alarm Vertical plane: Option A: Uniform between 1.5m and 300m. Option B: Fixed height value chosen from {25, 50, 100, 200, 300} m assuming vertical velocity is equal to 0. FFS Other options are not precluded. NOTE5: target(s) are outside the minimum distance to the Tx/Rx |
|  | Orientation | Random in horizontal domain |
|  | Physical characteristics (e.g., size) | Size: Option 1: 1.6m x 1.5m x 0.7m Option 2: 0.3m x 0.4m x 0.2m FFS: Material(s), Structure, Other size(s) |
| Minimum 3D distances between pairs of Tx/Rx and sensing target | Option B: Min distances based on min. TRP/UE distances defined in TR36.777 as a starting point. NOTE5: the sensing target is assumed in the far field of sensing Tx/Rx Option C: Min. distance is larger than the min. far-field distance of the sensing Tx/Rx |  |
| Minimum 3D distance between sensing targets | Option 1: At least larger than the physical size of a target Option 2: 10 meters |  |
| [Unintended/Environment objects, e.g., types, characteristics, mobility, distribution, etc.] | FFS |  |
NOTE:	A percentage of TRPs/UEs that have sensing capabilities may be considered for future evaluations.
R1-2410338	FL Summary #2 on ISAC Deployment Scenarios	Moderator (AT&T)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_119/) · `RAN1-119-isac-deployment-scenarios-75cbe2f1-a001`

### [5G-A/Rel-19 RAN1#119] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
For Automotive sensing target scenarios, the following table is agreed for deployment scenario parameters/values using the agreements from RAN1#118-bis as a baseline:
The detailed scenario description in this clause can be used for channel model calibration.
ISAC-Automotive
Details on ISAC-Automotive scenarios are listed in Table x.
Table x. Evaluation parameters for Automotive sensing scenarios
| Parameters | Values |  |
| --- | --- | --- |
| Applicable communication scenarios | Highway, Urban Grid. NOTE1 |  |
| Sensing transmitters and receivers properties | Rx/Tx locations are selected among the TRPs and UEs (e.g., VRU, vehicle, RSU-type UEs) locations in the corresponding communication scenario. NOTE2 FFS: Additional option: ISD between TRPs of Urban Grid is 250m |  |
| Sensing target | LOS/NLOS | LOS and NLOS (including NLOSv) |
|  | Outdoor/indoor | Outdoor |
|  | Mobility (horizontal plane only) | Based on TR37.885 mobility for urban grid or highway scenario |
|  | Distribution (horizontal) | Based on dropping in TR37.885 per urban grid or highway communication scenario |
|  | Orientation | Lane direction in horizontal plane |
|  | Physical characteristics (e.g., size) | Type 1/2 (passenger vehicle) Type 3 (truck/bus) Vehicle type distribution per TR 37.885 as a starting point FFS: Other sizes, additional distributions, and vehicle types, e.g. one new type of e-scooter/motorcycle/bike |
| Minimum 3D distances between pairs of Tx/Rx and sensing target | Option 1: Min distances based on min. TRP/UE distances defined in TR37.885 as a starting point. Option 2: Min. distance is larger than the min. far-field distance of the sensing Tx/Rx NOTE3: the sensing target is assumed in the far field of sensing Tx/Rx |  |
| Minimum 3D distance between sensing targets | Option 1: At least larger than the physical size of a sensing target Option 2: Fixed value, [10] m. value of x is FFS |  |
| Environment Objects, e.g., types, characteristics, mobility, distribution, etc. | EO Type 2 for Urban Grid FFS: details, e.g. up to 4 walls modelled as EO type 2, per building of size [413m x 230m x 20m]. FFS: number of buildings, how many walls are modelled, additional building sizes, etc. |  |
NOTE1:	Calibration for UMi, Uma, RMa is not performed for the automotive scenario, but UMi, Uma, RMa can be considered for future evaluations of the automotive sensing target scenarios. Calibration for UMi, Uma, RMa is expected to be performed for another sensing scenario.
NOTE2:	A percentage of TRPs/UEs that have sensing capabilities may be considered for future evaluations.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_119/) · `RAN1-119-isac-deployment-scenarios-75cbe2f1-a002`

### [5G-A/Rel-19 RAN1#119] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
For Human (indoor and outdoor) sensing target scenarios, the following table is agreed for deployment scenario parameters/values using the agreements from RAN1#118-bis as a baseline:
The detailed scenario description in this clause can be used for channel model calibration.
ISAC-Human
Details on ISAC-Human scenarios are listed in Table x.
Table x. Evaluation parameters for Human (indoor and outdoor) sensing scenarios
| Parameters | Indoor Values | Outdoor Values |  |
| --- | --- | --- | --- |
| Applicable communication scenarios NOTE1 | Indoor office, indoor factory [TR38.901] Indoor room [TR38.808] | UMi, Uma, RMa [TR38.901] |  |
| Sensing transmitters and receivers properties | Rx/Tx Locations NOTE 2 | Rx/Tx locations are selected among the TRPs and UE locations in the corresponding communication scenario | Rx/Tx locations are selected among the TRPs and UE locations in the corresponding communication scenario |
|  | Rx/Tx Mobility for UEs | Option 1: 0km/h Option 2: 3km/h Option 3: Uniform distribution between 0km/h and 3km/hr | Option 1: 0km/h Option 2: 3km/h Option 3: Uniform distribution between 0km/h and 10km/hr |
| Sensing target | LOS/NLOS | LOS and NLOS | LOS and NLOS |
|  | Outdoor/indoor | Indoor | Outdoor |
|  | 3D mobility | Option 1: 0km/h Option 2: 3km/h Option 3: Uniform distribution between 0km/h and 3km/hr (horizontal plane with random direction straight-line trajectory) | Option 1: 0km/h Option 2: 3km/h Option 3: Uniform distribution between 0km/h and 10km/hr (horizontal plane with random direction straight-line trajectory) |
|  | 3D distribution | N targets uniformly distributed over the horizontal area of the convex hull of the TRP deployment FFS: Value of N NOTE1: N=0 may be considered for the evaluation of false alarm | Option A: N targets uniformly distributed within one cell. Option B: N targets uniformly distributed per cell. Option C: N targets uniformly distributed within an area not necessarily determined by cell boundaries. Uniform in horizontal plane NOTE1: N=0 may be considered for the evaluation of false alarm |
|  | Orientation | Random over the horizontal area | Random over the horizontal area |
|  | Physical characteristics (e.g., size) | Size (Length x Width x Height): Child: 0.2m x 0.3m x 1m Adult Pedestrian: 0.5m x 0.5m x 1.75m | Size (Length x Width x Height): Child: 0.2m x 0.3m x 1m Adult Pedestrian: 0.5m x 0.5m x 1.75m |
| Minimum 3D distances between pairs of Tx/Rx and sensing target | Option 1: Min. distance is larger than the min. far-field distance of the sensing Tx/Rx Option 2: Min distances defined in TR 38.901 and TR36.843 and TR38.859as a starting point NOTE2: the sensing target is assumed in the far field of sensing Tx/Rx | Option 1: Min. distance is larger than the min. far-field distance of the sensing Tx/Rx Option 2: Min distances defined in TR 38.901 and TR36.843 and TR38.859 as a starting point NOTE3: the sensing target is assumed in the far field of sensing Tx/Rx |  |
| Minimum 3D distance between sensing targets | Option 1: At least larger than the physical size of a sensing target Option 2: Fixed value, [x] m. value of x is FFS | Option 1: At least larger than the physical size of a sensing target Option 2: Fixed value, [x] m. value of x is FFS |  |
| Environment Objects, e.g., types, characteristics, mobility, distribution, etc. | FFS, based on outcome for AI 9.7.2 | FFS, based on outcome for AI 9.7.2 |  |
NOTE1:	For the human (indoor and outdoor) sensing targets, additional communication scenarios can be considered for future evaluations. Channel model calibration for Urban Grid with outdoor humans is expected to be performed from Objects creating hazards on the road/railway sensing scenarios.
NOTE2:	A percentage of TRPs/UEs that have sensing capabilities may be considered for future evaluations.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_119/) · `RAN1-119-isac-deployment-scenarios-75cbe2f1-a003`

### [5G-A/Rel-19 RAN1#119] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
For AGV sensing target scenarios, the following table is agreed for deployment scenario parameters/values using the agreements from RAN1#118-bis as a baseline:
The detailed scenario description in this clause can be used for channel model calibration.
ISAC-AGV
Details on ISAC-AGV are listed in Table x.
Table x. Evaluation parameters for Automated Guided Vehicles
| Parameters | Value |  |
| --- | --- | --- |
| Applicable communication scenarios NOTE1 | InF (TR38.901 including Table 7.8-7) |  |
| Sensing transmitters and receivers properties NOTE2 | Rx/Tx location are selected among the TRPs and UEs location in the corresponding communication scenario Rx/Tx Mobility for UEs Option 1: 0 km/h Option 2: 3km/h Option 3: Uniform distribution between 0km/h and 3km/h |  |
| Sensing target | LOS/NLOS | LOS and NLOS |
|  | Outdoor/indoor | Indoor |
|  | 3D mobility | Horizontal velocity with random straight-line trajectory Option 1: Uniform distribution in the range of up to 30 km/h Option 2: Fixed velocities [3, 10] km/h |
|  | 3D distribution | Option A: Uniformly distributed in the convex hull of the horizontal BS deployment Option B: Uniformly distributed in horizontal plane |
|  | Orientation | Horizontal plane only |
|  | Physical characteristics (e.g., size) | Size (L x W x H) Option 1: 0.5m x 1.0m x 0.5m Option 2: 1.5 m x 3.0m x 1.5 m FFS: Material, Additional sizes, and AGV size distribution |
| Minimum 3D distances between pairs of Tx/Rx and sensing target | Option 1: Min. distance is larger than the min. far-field distance of the sensing Tx/Rx from the sensing target Option 2: Min distances based on min. TRP/UE distances defined in TR38.901 NOTE: the sensing target is assumed in the far field of sensing Tx/Rx |  |
| Minimum 3D distance between sensing targets | Option A: At least larger than the physical size of a target Option B: Fixed value, [x] m. value of x is FFS |  |
| Environment objects, e.g., types, characteristics, mobility, distribution, etc. | FFS |  |
NOTE1:	For the AGV sensing targets, additional communication scenarios can be considered for future evaluations.
NOTE2:	A percentage of TRPs/UEs that have sensing capabilities may be considered for future evaluations.
NOTE3:	RAN1 can further discuss narrowing down the number of sub-scenarios of InF
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_119/) · `RAN1-119-isac-deployment-scenarios-75cbe2f1-a004`

### [5G-A/Rel-19 RAN1#119] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
For Objects creating hazards sensing target scenarios, the following table is agreed for deployment scenario parameters/values using the agreements from RAN1#118-bis as a baseline:
The detailed scenario description in this clause can be used for channel model calibration.
ISAC-Hazards
Details on ISAC-Hazards are listed in Table x.
Table x. Evaluation parameters for objects creating hazards
| Parameters | Value |  |
| --- | --- | --- |
| Applicable communication scenarios NOTE1 | Highway, Urban grid, HST (High Speed Train) |  |
| Sensing transmitters and receivers properties NOTE2 | Rx/Tx Locations | Rx/Tx locations are selected among the TRPs and UEs (e.g., VRU, vehicle, RSU-type UEs) locations in the corresponding communication scenarios. FFS: Option 2 Additional option ISD between TRPs of Urban Grid is 250 m |
| Sensing target | LOS/NLOS | LOS and NLOS |
|  | Outdoor/indoor | Outdoor |
|  | 3D mobility | Horizontal velocity: up to [10] km/h for humans and animals FFS: Additional velocities, trajectory |
|  | 3D distribution | Uniformly distributed in horizontal plane |
|  | Orientation | Random distribution in horizontal plane |
|  | Physical characteristics (e.g., size) | For human/pedestrians: Child: 0.2m x 0.3m x 1m Adult: 0.5m x 0.5m x 1.75m For animals: Size: 1.5m x 0.5m x 1 m FFS: other types/sizes of targets may be considered for future evaluations |
| Minimum 3D distances between pairs of Tx/Rx and sensing target | Option 1: Min. distance is larger than the min. far-field distance of the sensing Tx/Rx from the sensing target Option 2: based on min TRP/UE distances defined in TR37.885 and TR38.802 and TR36.843 and TR38.859 NOTE: the sensing target is assumed in the far field of sensing Tx/Rx |  |
| Minimum 3D distance between sensing targets | Option 1: At least larger than the physical size of a sensing target Option 2: Fixed value, [10] m. value of x is FFS |  |
| Environment objects, e.g., types, characteristics, mobility, distribution, etc. | EO Type 2 for Urban Grid FFS: details, e.g. up to 4 walls modelled as EO type 2, per building of size [413m x 230m x 20m]. FFS: number of buildings, how many walls are modelled, additional building sizes, etc. |  |
NOTE1:	For the objects creating hazards sensing targets, additional communication scenarios can be considered for future evaluations.
NOTE2:	A percentage of TRPs/UEs that have sensing capabilities may be considered for future evaluations.
[Post-119-ISAC-01] – Jerome (AT&T)
Email discussion on simulation assumptions for channel model calibration, from January 8th-17th:
Companies are encouraged to provide initial channel model calibration assumptions, parameters, and values
Jerome to collect inputs, provide potential consolidated tables, proposals for consideration by January 17th
Decision: The discussions are to be carried over to RAN1#120.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_119/) · `RAN1-119-isac-deployment-scenarios-75cbe2f1-a005`

### [5G-A/Rel-19 RAN1#118b] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
RAN1 strives to define a single option per target per monostatic/bistatic sensing mode from the following two options to generate RCS values/patterns for a scattering point of a target.
Option 2: The RCS=A*B of a scattering point can be generated by
The component A is commonly applied to any incident/scattered angles at the scattering point
A is [mean] RCS value. FFS value(s) A
Note: Mean RCS value is defined as the mean value of the distribution of RCS
The component B
B is generated by [log-normal] distribution, the related [log-normal] distribution has mean μ=1 and variance V, FFS σ2
B is separately generated for each direct/indirect path at the scattering point. FFS correlation dependent on the incident/scattered angles of the direct/indirect paths
FFS whether/how power of all generated direct/indirect paths need to be normalized considering impact of RCS
Option 3: The RCS=A*B=A*B1*B2 of a scattering point can be generated by
The component A is commonly applied to any incident/scattered angles at the scattering point
FFS: A = 1 m2 or [mean] RCS value
Note: Mean RCS value is defined as the mean value of the distribution of RCS
The component B is further split into B1, B2, i.e., B=B1*B2
B1 is deterministic based on incident/scattered angles
FFS: B1 is defined by a function or by a table
B2 is generated by [log-normal] distribution, the related [log-normal] distribution has mean μ=1 and variance V, FFS σ2
B2 is separately generated for each direct/indirect path at the scattering point. FFS correlation dependent on the incident/scattered angles of the direct/indirect paths
FFS whether/how power of all generated direct/indirect paths need to be normalized considering impact of RCS
R1-2408099	Summary #2 on ISAC channel modelling	Moderator (Xiaomi)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_118b/) · `RAN1-118b-isac-channel-modelling-fa5b802a-a001`

### [5G-A/Rel-19 RAN1#118b] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
RCS Option 3 is selected to model RCS of UAV with single scattering point for monostatic
B2 of UAV is modelled using log-normal distribution for monostatic
Different mean RCS values can be supported for UAV due to different size, shape, frequency, etc.
For UAV of small size (option 2 for UAV size in UAV parameters table)
B1=1
A is mean RCS value
For UAV of large size (option 1 for UAV size in UAV parameters table)
B1 have dependency on incident/scattered angles
A is mean RCS value
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_118b/) · `RAN1-118b-isac-channel-modelling-fa5b802a-a002`

### [5G-A/Rel-19 RAN1#118b] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
To model the effect of polarization for each direct/indirect path:
Polarization of a direct/indirect path is product of polarization matrix of Tx-target link, the target, and the target-Rx link
Total polarization of a direct/indirect path is CPMtx,sp,rx= CPMsp,rx . CPMsp . CPMtx,sp
For a LOS ray from Tx to target or from target to Rx,  for CPMtx,sp or CPMsp,rx
For a NLOS ray generated by a stochastic cluster from Tx to target or from target to Rx, CPMtx,sp or CPMsp,rx is generated by XPR ratio  and initial random phases referring to TR 38.901 as start point
FFS how to normalize on CPMtx,sp,rx
FFS CPMsp of a scattering point of the target
FFS: how to model the effect of polarization when EO type-2 is present.
R1-2408100	Summary #3 on ISAC channel modelling	Moderator (Xiaomi)
R1-2408101	Summary #4 on ISAC channel modelling	Moderator (Xiaomi)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_118b/) · `RAN1-118b-isac-channel-modelling-fa5b802a-a003`

### [5G-A/Rel-19 RAN1#118b] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
A single direct path is modeled for a scattering point of target
In each of the Tx-target and target RX links, the first NLOS cluster is generated with same delay as the LOS ray (when the absolute delay modelling of  as in section 7.6.9, TR 38.901 is not applied) and with the same direction as the LOS ray.
FFS how to generate NLOS cluster when  is applied.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_118b/) · `RAN1-118b-isac-channel-modelling-fa5b802a-a004`

### [5G-A/Rel-19 RAN1#118b] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
In order to generate each of the Tx-target link and target-Rx link in the target channel, the large scale and small scale parameters defined in existing 3GPP TRs, e.g., TR 38.901. TR 36.777, TR 37.885, TR 38.858, TR 38.859, TR 38.802, TR 38.854, etc. are used as starting point.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_118b/) · `RAN1-118b-isac-channel-modelling-fa5b802a-a005`

### [5G-A/Rel-19 RAN1#118b] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
On the background channel for TRP-TRP and UE-UE bistatic sensing mode, the large scale and small scale parameters defined in TR 38.901, TR 38.858, 37.885, 38.859 are used as starting point.
Update on values of the LSP/SSP parameters can be discussed based on validation data acquired by measurement or ray-tracing model.
FFS The power threshold for removing clusters in step 6, i.e., -25 dB is revised to X<-25 dB. FFS X.
FFS whether/how to resolve the inconsistency between TRP-TRP channel according to TR 38.858 and the TRP-target (UAV) channel according to TR 36.777 when UAV and TRP are set to same height.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_118b/) · `RAN1-118b-isac-channel-modelling-fa5b802a-a006`

### [5G-A/Rel-19 RAN1#118b] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
3D spatial consistency needs to be studied for at least UAV scenario.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_118b/) · `RAN1-118b-isac-channel-modelling-fa5b802a-a007`

### [5G-A/Rel-19 RAN1#118b] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
In LOS condition between sensing Tx/Rx and target, the power of LOS ray is generated following power of LOS ray in TR 38.901.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_118b/) · `RAN1-118b-isac-channel-modelling-fa5b802a-a008`

### [5G-A/Rel-19 RAN1#118b] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
The following options are to be studied for the concatenation of Tx-target and target-Rx link in the target channel
Direct path (if present) is always kept
Indirect paths of LOS+NLOS, NLOS+LOS (if present) are generated
On other indirect paths of NLOS + NLOS
Option 0: ray level full convolution between Tx-target link and target-Rx link for radio propagation Case 1/2/3/4
Option 0A: ray level full convolution between Tx-target link and target-Rx link only for radio propagation Case 4
Option 1: cluster level full convolution between Tx-target link and target-Rx link, then 1-by-1 coupling rays within each pair of clusters for radio propagation Case 1/2/3/4
Option 1A: cluster level full convolution between Tx-target link and target-Rx link, then 1-by-1 coupling rays within each pair of clusters only for radio propagation Case 4
Option 2: cluster level 1-by-1 coupling between Tx-target link and target-Rx link, then 1-by-1 coupling rays within each pair of clusters for radio propagation Case 1/2/3/4
Option 2A: cluster level 1-by-1 coupling between Tx-target link and target-Rx link, then 1-by-1 coupling rays within each pair of clusters only for radio propagation Case 4
Option 3: ray level 1-by-1 coupling between Tx-target link and target-Rx link for radio propagation Case 1/2/3/4
Option 3A: ray level 1-by-1 coupling between Tx-target link and target-Rx link only for radio propagation Case 4
Note: reducing the number of rays per cluster and/or reducing the number of clusters can be considered for the options above
Any indirect path with power metric less than [threshold] is dropped
the power metric of a path is the product of power of a ray in Tx-target link, power of a ray in target-Rx link and RCS of the pair of rays
FFS power normalization of target channel after path dropping
FFS the set of remaining indirect paths can be updated during movement of Tx, target or Rx
Final summary in R1-2409280.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_118b/) · `RAN1-118b-isac-channel-modelling-fa5b802a-a009`

### [5G-A/Rel-19 RAN1#118b] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
For Automotive sensing target scenarios, the following table is used as a starting point for deployment scenario parameters/values.
The detailed scenario description in this clause can be used for channel model calibration.
Note: Additional parameters, value/value ranges are not precluded.
Table x. Evaluation parameters for Automotive sensing scenarios
| Parameters | Values |  |
| --- | --- | --- |
| Applicable communication scenarios | Highway, Urban Grid. NOTE1 |  |
| Sensing transmitters and receivers properties | Rx/Tx locations are selected among the TRPs and UEs (e.g., VRU, vehicle, RSU-type UEs) locations in the corresponding communication scenario. NOTE2 FFS: Option 2: ISD between TRPs of Urban Grid is 250 meters |  |
| Sensing target | LOS/NLOS | LOS and NLOS (including NLOSv) |
|  | Outdoor/indoor | Outdoor |
|  | Mobility (horizontal plane only) | Based on TR37.885 mobility for urban grid or highway scenario |
|  | Distribution (horizontal) | Based on dropping in TR37.885 per urban grid or highway communication scenario |
|  | Orientation | Lane direction in horizontal plane |
|  | Physical characteristics (e.g., size) | Type 1/2 (passenger vehicle) Type 3 (truck/bus) Vehicle type distribution per TR 37.885 as a starting point FFS: Other sizes, additional distributions, and vehicle types, e.g. one new type of e-scooter/motorcycle/bike |
| Minimum 3D distances between pairs of Tx/Rx and sensing target | Option 1: Min distances based on min. TRP/UE distances defined in TR37.885 as a starting point. Option 2: Min. distance is larger than the min. far-field distance of the sensing Tx/Rx |  |
| Minimum 3D distance between sensing targets | Option 1: At least larger than the physical size of a sensing target Option 2: Fixed value, [x] m. value of x is FFS |  |
| Environment Objects, e.g., types, characteristics, mobility, distribution, etc. | EO Type 2 for Urban Grid FFS: details, e.g. 4 walls (as EO type 2) per building of size [413mx230mx20m] |  |
NOTE1: calibration for UMi, Uma, RMa is not performed for the automotive scenario, but UMi, Uma, RMa can be considered for future evaluations of the automotive sensing target scenarios. Calibration for UMi, Uma, RMa is expected to be performed for another sensing scenario.
NOTE2: A percentage of TRPs/UEs that have sensing capabilities may be considered for future evaluations.
R1-2408761	FL Summary #2 on ISAC Deployment Scenarios	Moderator (AT&T)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_118b/) · `RAN1-118b-isac-deployment-scenarios-75cbe2f1-a001`

### [5G-A/Rel-19 RAN1#118b] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
For Human sensing target scenarios, (indoor and outdoor), the following table is used as a starting point for deployment scenario parameters/values.
The detailed scenario description in this clause can be used for channel model calibration.
Note: Additional parameters, value/value ranges are not precluded.
Table x. Evaluation parameters for Human (indoor and outdoor) sensing scenarios
| Parameters | Indoor Values | Outdoor Values |  |
| --- | --- | --- | --- |
| Applicable communication scenarios NOTE1 | Indoor office, indoor factory [TR38.901] Indoor room [TR38.808] | UMi, Uma, RMa [TR38.901] |  |
| Sensing transmitters and receivers properties | Rx/Tx Locations NOTE 2 | Rx/Tx locations are selected among the TRPs and UE locations in the corresponding communication scenario | Rx/Tx locations are selected among the TRPs and UE locations in the corresponding communication scenario |
|  | Rx/Tx Mobility for UEs | Option 1: 0km/h Option 2: 3km/h Option 3: Uniform distribution between 0km/h and 3km/hr | Option 1: 0km/h Option 2: 3km/h Option 3: Uniform distribution between 0km/h and 10km/hr |
| Sensing target | Outdoor/indoor | Indoor | Outdoor |
|  | 3D mobility | Option 1: 0km/h Option 2: 3km/h Option 3: Uniform distribution between 0km/h and 3km/hr (horizontal plane with random direction straight-line trajectory) | Option 1: 0km/h Option 2: 3km/h Option 3: Uniform distribution between 0km/h and 10km/hr (horizontal plane with random direction straight-line trajectory) |
|  | 3D distribution | N targets uniformly distributed over the horizontal area of the convex hull of the TRP deployment FFS: Value of N | Uniform in horizontal plane |
|  | Orientation | Random over the horizontal area | Random over the horizontal area |
|  | Physical characteristics (e.g., size) | Size (Length x Width x Height): Child: 0.2m x 0.3m x 1m Adult Pedestrian: 0.5m x 0.5m x 1.75m | Size (Length x Width x Height): Child: 0.2m x 0.3m x 1m Adult Pedestrian: 0.5m x 0.5m x 1.75m |
| Minimum 3D distances between pairs of Tx/Rx and sensing target | Option 1: Min. distance is larger than the min. far-field distance of the sensing Tx/Rx Option 2: Min distances defined in TR 38.901 as a starting point | Option 1: Min. distance is larger than the min. far-field distance of the sensing Tx/Rx Option 2: Min distances defined in TR 38.901 as a starting point |  |
| Minimum 3D distance between sensing targets | Option 1: At least larger than the physical size of a sensing target Option 2: Fixed value, [x] m. value of x is FFS | Option 1: At least larger than the physical size of a sensing target Option 2: Fixed value, [x] m. value of x is FFS |  |
| Environment Objects, e.g., types, characteristics, mobility, distribution, etc. | FFS, based on outcome for AI 9.7.2 | FFS, based on outcome for AI 9.7.2 |  |
NOTE1: For the human (indoor and outdoor) sensing targets, additional communication scenarios can be considered for future evaluations. Channel model calibration for Urban Grid with outdoor humans is expected to be performed from Objects creating hazards on the road/railway sensing scenarios.
NOTE2: A percentage of TRPs/UEs that have sensing capabilities may be considered for future evaluations.
R1-2408762	FL Summary #3 on ISAC Deployment Scenarios	Moderator (AT&T)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_118b/) · `RAN1-118b-isac-deployment-scenarios-75cbe2f1-a002`

### [5G-A/Rel-19 RAN1#118b] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
For Automated Guided Vehicles (AGV) target scenarios, the following table is used as a starting point for deployment scenario parameters/values.
The detailed scenario description in this clause can be used for channel model calibration.
Note: Additional parameters, value/value ranges are not precluded.
Table x. Evaluation parameters for Automated Guided Vehicles
| Parameters | Value |  |
| --- | --- | --- |
| Applicable communication scenarios NOTE1 | InF (TR38.901 including Table 7.8-7) |  |
| Sensing transmitters and receivers properties NOTE2 | Rx/Tx location are selected among the TRPs and UEs location in the corresponding communication scenario Rx/Tx Mobility for UEs Option 1: 0 km/h Option 2: 3km/h Option 3: Uniform distribution between 0km/h and 3km/h |  |
| Sensing target | LOS/NLOS | LOS and NLOS |
|  | Outdoor/indoor | Indoor |
|  | 3D mobility | Horizontal velocity with random straight-line trajectory Option 1: Uniform distribution in the range of up to 30 km/h Option 2: Fixed velocities [3, 10] km/h |
|  | 3D distribution | Option A: Uniformly distributed in the convex hull of the horizontal BS deployment Option B: Uniformly distributed in horizontal plane |
|  | Orientation | Horizontal plane only |
|  | Physical characteristics (e.g., size) | Size (L x W x H) Option 1: 0.5m x 1.0m x 0.5m Option 2: 1.5 m x 3.0m x 1.5 m FFS: Material, Additional sizes, and AGV size distribution |
| Minimum 3D distances between pairs of Tx/Rx and sensing target | Option 1: Min. distance is larger than the min. far-field distance of the sensing Tx/Rx from the sensing target Option 2: Min distances based on min. TRP/UE distances defined in TR38.901 |  |
| Minimum 3D distance between sensing targets | Option A: At least larger than the physical size of a target Option B: Fixed value, [x] m. value of x is FFS |  |
| Environment objects, e.g., types, characteristics, mobility, distribution, etc. | FFS |  |
NOTE1: For the AGV sensing targets, additional communication scenarios can be considered for future evaluations.
NOTE2: A percentage of TRPs/UEs that have sensing capabilities may be considered for future evaluations.
NOTE3: RAN1 can further discuss narrowing down the number of sub-scenarios of InF
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_118b/) · `RAN1-118b-isac-deployment-scenarios-75cbe2f1-a003`

### [5G-A/Rel-19 RAN1#118b] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
For objects creating hazards, the following proposals are suggested to be discussed by RAN1:
For objects creating hazards use cases, RAN1 to consider the following table as a starting point for deployment scenario parameters/values.
The detailed scenario description in this clause can be used for channel model calibration.
Note: Additional parameters, value/value ranges are not precluded.
Table x. Evaluation parameters for objects creating hazards
| Parameters | Value |  |
| --- | --- | --- |
| Applicable communication scenarios NOTE1 | Highway, Urban grid, HST (High Speed Train) |  |
| Sensing transmitters and receivers properties NOTE2 | Rx/Tx Locations | Rx/Tx locations are selected among the TRPs and UEs (e.g., VRU, vehicle, RSU-type UEs) locations in the corresponding communication scenarios. FFS: Option 2: ISD between TRPs of Urban Grid is 250 meters |
| Sensing target | LOS/NLOS | LOS and NLOS |
|  | Outdoor/indoor | Outdoor |
|  | 3D mobility | Horizontal velocity: up to [10] km/h for humans and animals FFS: Additional velocities, trajectory |
|  | 3D distribution | Uniformly distributed in horizontal plane |
|  | Orientation | Random distribution in horizontal plane |
|  | Physical characteristics (e.g., size) | For human/pedestrians: Child: 0.2m x 0.3m x 1m Adult: 0.5m x 0.5m x 1.75m For animals: Size: 1.5m x 0.5m x 1 m FFS: other types of targets |
| Minimum 3D distances between pairs of Tx/Rx and sensing target | Option 1: Min. distance is larger than the min. far-field distance of the sensing Tx/Rx from the sensing target Option 2: based on TR37.885 and TR38.802 |  |
| Minimum 3D distance between sensing targets | Option 1: At least larger than the physical size of a target Option 2: Fixed value, [x] m. value of x is FFS |  |
| Environment objects, e.g., types, characteristics, mobility, distribution, etc. | EO Type 2 for Urban Grid FFS: details, e.g. 4 walls (as EO type 2) per building of size [413mx230mx20m] |  |
NOTE1: For the objects creating hazards sensing targets, additional communication scenarios can be considered for future evaluations.
NOTE2: A percentage of TRPs/UEs that have sensing capabilities may be considered for future evaluations.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_118b/) · `RAN1-118b-isac-deployment-scenarios-75cbe2f1-a004`

### [5G-A/Rel-19 RAN1#118] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
If RCS related coefficient of a scattering point is included in small scale, the RCS related coefficients are separately determined for different pairs of incident/scattered ray(s) at the scattering point.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_118/) · `RAN1-118-isac-channel-modelling-fa5b802a-a001`

### [5G-A/Rel-19 RAN1#118] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
For radio propagation Case 1, for modelling the target channel of a target with single scattering point,
To model a direct path, a single LOS ray from Tx to target and a single LOS ray from target to Rx are generated
AoA/ZoA of the direct path at Rx, AoD/ZoD of the direct path at target are generated at least based on the 3D location of target and Rx in the global coordinate system
AoD/ZoD of the direct path at Tx, AoA/ZoA of the direct path at target are generated at least based on the 3D location of Tx and target in the global coordinate system
The Delay of the direct path = (d3D_tx_target + d3D_target_rx)/c
The Doppler of the direct path is generated by spherical unit vectors by AoD/ZoD at Tx, by spherical unit vectors by AoA/ZoA at Rx, and velocity of Tx, target and Rx
The power of the direct path is generated as the product of the power of the LOS ray from Tx to target, the power of the LOS ray from target to Rx, and the effect of RCS
FFS initial phase
FFS how to model RCS, polarization of target
FFS number of direct paths
FFS on detailed modelling of indirect path(s)
FFS applicability of direct path generation to each scattering point when the target is modelled as multiple scattering points
R1-2406300	Summary #2 on ISAC channel modelling	Moderator (Xiaomi)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_118/) · `RAN1-118-isac-channel-modelling-fa5b802a-a002`

### [5G-A/Rel-19 RAN1#118] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
For the target channel of a target with single scattering point, when stochastic cluster is used to model an indirect path in the target channel,
An indirect path in small scale is modelled by concatenation of path(s) from Tx to target and from target to Rx, i.e., Option 1 in the agreement of RAN1 #117
AoD/ZoD/AoA/ZoA from Tx to target or from target to Rx are
generated for a LOS ray at least based on the 3D location of Tx/Rx and target in the global coordinate system
stochastically generated for a NLOS ray using section 7, 38.901 as starting point
Delay is sum of delay of LOS/NLOS ray from Tx to target and the LOS/NLOS ray from target to Rx
Doppler is generated by spherical unit vector by AoD/ZoD at Tx and velocity of Tx, by spherical unit vector by AoA/ZoA at Rx and velocity of Rx, and by spherical unit vectors by AoA/ZoA/AoD/ZoD at target and velocity of target
FFS The mobility of stochastic clutter
The power of the indirect path is generated as the product of the power of the LOS/NLOS ray from Tx to target, the power of the LOS/NLOS ray from target to Rx and the effect of RCS
FFS initial phase
FFS how to model effect of RCS at target
FFS whether/how to model polarization at target
FFS How to reduce complexity
FFS applicability of the indirect path generation to each/a single scattering point when the target is modelled as multiple scattering points
R1-2406301	Summary #3 on ISAC channel modelling	Moderator (Xiaomi)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_118/) · `RAN1-118-isac-channel-modelling-fa5b802a-a003`

### [5G-A/Rel-19 RAN1#118] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
The impact of a scattering point of the target in the target channel is modelled by a scalar RCS value  times a complex-valued 2x2 polarization matrix , i.e.,
FFS whether  is angular/ray-dependent or independent.
FFS whether polarization matrix  is modelled assuming specular reflection or random coefficient for diffraction or scattering.
FFS whether polarization matrix  is explicitly modelled or merged with other polarization matrixes from Tx to target and/or from target to Rx.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_118/) · `RAN1-118-isac-channel-modelling-fa5b802a-a004`

### [5G-A/Rel-19 RAN1#118] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
For modeling stochastic cluster in background channel, in order to define the background channel for TRP-UE and UE-TRP bistatic sensing mode,
The large scale and small scale parameters defined in TR 38.901, TR 37.885, TR 36.777 are used as start point
In order to define the background channel for TRP-TRP and UE-UE bistatic sensing mode,
RAN1 to study how to model background channel
Option 1: The large scale and small scale parameters defined in TR 38.901, TR 38.858, 37.885, 38.859 are used as start point.
Option 2: New channel model based on measurement results or ray-tracing model validated by experimental results.
FFS whether/how to do power normalization between target channel and background channel.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_118/) · `RAN1-118-isac-channel-modelling-fa5b802a-a005`

### [5G-A/Rel-19 RAN1#118] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
In order to define the background channel for TRP and UE mono-static sensing mode,
RAN1 to study how to model the background channel
Option 1: randomly drop at least one virtual Rx, and then the background channel is generated based on the channel generated as TR 38.901 between the real Tx and each virtual Rx for a scenario.
FFS EO is modelled in the background channel.
Option 2: New channel model based on measurement results or ray-tracing model validated by experimental results or radar literatures.
FFS EO is modelled in the background channel.
Option 3: the locations of clusters in the target channel are deterministically generated, then the background channel is generated using the clusters with the determined locations.
Other options are not precluded.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_118/) · `RAN1-118-isac-channel-modelling-fa5b802a-a006`

### [5G-A/Rel-19 RAN1#118] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
When EO type-2 is modelled, specular reflection is considered to model EO type-2 using section 7.6.8 of TR 38.901 as reference
As starting point, the effect of type-2 EO (i.e., in the path node1-EO-node2) is modelled as , b is a scaling factor (e.g., c equals to  relative to LOS ray in section 7.6.8 in TR 38.901)
FFS any update to
FFS any update taking EO orientation into account
FFS any changes based on section 7.6.8 of TR 38.901 if EO type-2 has finite size
FFS whether diffraction and scattering can be considered in addition to specular reflection
EO type-2 is an optional modelling component if supported in a sensing scenario
FFS which deployment scenario(s) EO type-2 will apply
Final summary in R1-2406302.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_118/) · `RAN1-118-isac-channel-modelling-fa5b802a-a007`

### [5G-A/Rel-19 RAN1#118] `working_assumption` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
The RCS related coefficient of a scattering point can be modelled with two components, i.e., linear value RCS = A*B
A first RCS component A () is included in large scale
FFS the first RCS component is deterministic or stochastic
FFS The first component is dependent on incident and scattered directions at target
A second RCS component B (unit ratio) is included in small scale
FFS The second component is dependent on incident and scattered directions at target
FFS the second RCS component is deterministic or stochastic or combination
Note: RCS component A or B can be disabled by setting its linear value to 1
Whether to disable a component can be discussed per target type
FFS how to determine A and B for each target
FFS whether/how to model polarization impact at target
FFS whether/how to normalize power accounting for target channel and background channel
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_118/) · `RAN1-118-isac-channel-modelling-fa5b802a-w001`

### [5G-A/Rel-19 RAN1#118] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
General principles for all sensing target deployment scenarios should consider the following:
“Sensing mode” is removed in the scenario tables, but may be included in the evaluation/calibration phase. Per the SI, all sensing modes are possible for the deployment scenarios.
“Sensing area” may be addressed as part of the sensing target distribution and/or Tx/Rx characteristics and/or cell layout.
R1-2406875	FL Summary #3 on ISAC Deployment Scenarios	Moderator (AT&T)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_118/) · `RAN1-118-isac-deployment-scenarios-75cbe2f1-a001`

### [5G-A/Rel-19 RAN1#118] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
For UAV sensing target scenarios, the following table is agreed for deployment scenario parameters/values using the agreements from RAN1#117 as a baseline.
Note: Additional parameters, value/value ranges are not precluded.
The detailed scenario description in this clause can be used for channel model calibration.
ISAC-UAV
Details on ISAC-UAV scenarios are listed in Table x.
Table x. Evaluation parameters for UAV sensing scenarios
| Parameters | Value |  |
| --- | --- | --- |
| Applicable communication scenarios | UMi, UMa, RMa [38.901] UMi-AV, UMa-AV, RMa-AV |  |
| Sensing transmitters and receivers properties | Rx/Tx Locations | Rx/Tx locations are selected among the TRPs and UEs locations in the corresponding communication scenarios. Note1: This may include aerial UEs for UMi-AV, UMa-AV, RMa-AV communication scenarios. In this case, other Rx/Tx properties (e.g. mobility) are also taken from the corresponding communication scenario. |
| Sensing target | Outdoor/indoor | Outdoor |
|  | 3D mobility | Horizontal velocity: uniform distribution between 0 and 180km/h, if horizontal velocity is not fixed to 0. Vertical velocity: 0km/h, optional {20, 40} km/h NOTE2: 3D mobility can be horizontal only or vertical only or a combination for each sensing target FFS: time-varying velocity. |
|  | 3D distribution | Horizontal plane: Option A: N targets uniformly distributed within one cell. Option B: N targets uniformly distributed per cell. Option C: N targets uniformly distributed within an area not necessarily determined by cell boundaries. FFS: Value of N, defined area, and other distributions Vertical plane: Option A: Uniform between 1.5m and 300m. Option B: Fixed height value chosen from {25, 50, 100, 200, 300} m assuming vertical velocity is equal to 0. FFS Other options are not precluded. Note2: target(s) are outside the minimum distance to the Tx/Rx |
|  | Orientation | Random in horizontal domain |
|  | Physical characteristics (e.g., size) | Size: Option 1: 1.6m x 1.5m x 0.7m Option 2: 0.3m x 0.4m x 0.2m FFS: Material(s), Structure, Other size(s) |
| Minimum 3D distances between pairs of Tx/Rx and sensing target | Option B: Min distances based on min. TRP/UE distances defined in TR36.777 as a starting point. Option C: Min. distance is larger than the min. far-field distance of the sensing Tx/Rx |  |
| Minimum 3D distance between sensing targets | Option 1: At least larger than the physical size of a target Option 2: 10 meters |  |
| [Unintended/Environment objects, e.g., types, characteristics, mobility, distribution, etc.] | FFS |  |
Note: further down-selection between the options in the table is not precluded.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_118/) · `RAN1-118-isac-deployment-scenarios-75cbe2f1-a002`

### [5G-A/Rel-19 RAN1#118] `conclusion` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
RAN1 will consider the recommendations for the physical characteristics (e.g., sizes, shapes, materials, velocities, etc.) of sensing targets and objects provided in 5GAA LS (R1-2405964), along with the relevant characteristics defined in 3GPP TRs, within the scope of the Rel-19 study item.
No LS response from RAN1 to 5GAA is necessary.
R1-2405964 is proposed to be NOTED.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_118/) · `RAN1-118-isac-deployment-scenarios-75cbe2f1-c001`

### [5G-A/Rel-19 RAN1#117] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
Multiple sensing targets can be modelled in the ISAC channel of a pair of sensing Tx and sensing Rx
FFS whether to model a propagation path from Tx to Rx interacting with more than one sensing target
The same sensing target can be modelled in the ISAC channels of multiple pairs of sensing Tx and Rx
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_117/) · `RAN1-117-isac-channel-modelling-fa5b802a-a001`

### [5G-A/Rel-19 RAN1#117] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
For discussion purpose, the propagation paths in the target channel are classified
The direct path, i.e., LOS ray from Tx to target + LOS ray from target to Rx
The indirect paths, i.e., any propagation path other than the direct path, including
LOS ray from Tx to target + NLOS ray from target to Rx
NLOS ray from Tx to target + LOS ray from target to Rx
NLOS ray from Tx to target + NLOS ray from target to Rx
For radio propagation Case 1,
For a direct path, the following parameters are [deterministically] generated at least based on the geometry location of Tx, target and Rx
AoA/ZoA at Rx
AoD/ZoD at Tx
AoA/ZoA/AoD/ZoD at target
delay
FFS initial phase
Doppler
FFS power/polarization including the impact of RCS
FFS the number of direct path(s) for a target
FFS on detailed modelling of indirect path(s)
FFS on details of modelling of indirect paths in  radio propagation Case 2/3/4
To generate the channel coefficients of direct/indirect path(s) in the target channel, the channel coefficient generation function in step 11 in section 7.5 of TR 38.901 (e.g., formula 7.5-22) is used as the start point
Note: modification to step 11 is deemed necessary
FFS adding impact of small scale RCS
FFS Doppler
R1-2404634	Summary #2 on ISAC channel modelling	Moderator (Xiaomi)
R1-2404635	Summary #3 on ISAC channel modelling	Moderator (Xiaomi)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_117/) · `RAN1-117-isac-channel-modelling-fa5b802a-a002`

### [5G-A/Rel-19 RAN1#117] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
Spatial consistency should be supported for ISAC channel
Spatial consistency should be supported based on movement of sensing Tx, sensing target and/or sensing Rx
FFS EO handling
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_117/) · `RAN1-117-isac-channel-modelling-fa5b802a-a003`

### [5G-A/Rel-19 RAN1#117] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
When the stochastic cluster is used to generate the indirect paths in the target channel of a target
The stochastic cluster generation in section 7, TR 38.901 is used as starting point.
FFS a stochastic cluster is generated between Tx and Rx satisfying Tx-target-Rx geometry, or between Tx/Rx and target
FFS modification to stochastic cluster generation in section 7, TR 38.901
FFS use of sub-cluster to model the indirect paths
Note: RAN1 continues studying using EO to generate the indirect paths in the target channel of a target
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_117/) · `RAN1-117-isac-channel-modelling-fa5b802a-a004`

### [5G-A/Rel-19 RAN1#117] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
When the stochastic cluster is used to model indirect path in the target channel
For bistatic, the LOS condition from Tx to target and from target to Rx is determined separately for a target
FFS: The correlation of LOS condition of Tx-target and Rx-target links of a target
For monostatic, a same LOS condition is determined for Tx to target and target to Rx
The LOS condition from Tx to target and/or from target to Rx is determined with the LOS probability
The probability schemes in existing 3GPP TRs, e.g., TR 38.901. TR 36.777, TR 37.885, etc. are considered as start point
FFS: How to consider the impacts of target height on LOS probability.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_117/) · `RAN1-117-isac-channel-modelling-fa5b802a-a005`

### [5G-A/Rel-19 RAN1#117] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
When stochastic cluster is used to model indirect path in the target channel, down-select between the following options
Option 1: modelled by concatenation of path(s) from Tx to target and from target to Rx
For each of the Tx-target link and target-Rx link,
The parameters delay, power, angle, [initial phase], [Doppler] of NLOS ray(s) in the link Tx-to-Target or Target to RX are generated
FFS following cluster generation in section 7, 38.901
The target channel is generated by concatenating the parameters of the Tx-target link and target-Rx link.
FFS on Convolutional or 1-by-1 coupling or 1-to-many coupling
FFS how to combine the clusters in target channel and the clusters in background channel
Option 2: modelled by Tx-to-Rx path(s) satisfying Tx-target-Rx geometry of the direct path
The parameters delay, power, angle, initial phase of a stochastic (sub-)cluster between Tx and Rx are generated following cluster generation in section 7, 38.901
The parameters [delay], [power], [angle], [Doppler] of the (sub-)cluster are updated by the target property
FFS how to combine the clusters in target channel and the clusters in background channel
Final summary in R1-2404636.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_117/) · `RAN1-117-isac-channel-modelling-fa5b802a-a006`

### [5G-A/Rel-19 RAN1#117] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
For each of the sensing target deployment scenarios using the template agreed in RAN#116-bis, the following principles apply:
For defining sensing Tx and sensing Rx properties (e.g., cell layout, BS antenna height, and minimum distance), scenario parameter values for the applicable communication scenarios in 38.901 are considered as a starting point. Updates to these evaluation parameter values for ISAC scenarios will consider the following:
aerial UEs parameter values as defined in TR 36.777
indoor room scenario parameter values defined in TR 38.808
automotive scenario parameter values as defined in TR 37.885, 38.859 for Urban grid/Highway
Minimum distances between Tx/Rx and target are not defined in the existing communications scenarios and shall be included in the sensing target deployment scenarios.
Note: Only deviation from the existing evaluation parameters in the applicable communication scenarios need to be explicitly defined in the ISAC scenario tables.
For defining sensing target properties, as a baseline
Evaluation parameter values can be taken from additional TRs, e.g., TR 36.777, 37.885, 38.859, etc.
Size of sensing targets based on TR 22.837, 37.885 (e.g. for automotive), 38.901 (e.g. for AGV size), etc
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_117/) · `RAN1-117-isac-deployment-scenarios-75cbe2f1-a001`

### [5G-A/Rel-19 RAN1#117] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
For ISAC deployment scenarios, carrier frequency, bandwidth, and SCS are not included in the evaluation parameters templates for sensing scenarios, but may be included in the evaluation/calibration phase.
R1-2404487	FL Summary #2 on ISAC Deployment Scenarios	Moderator (AT&T)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_117/) · `RAN1-117-isac-deployment-scenarios-75cbe2f1-a002`

### [5G-A/Rel-19 RAN1#117] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
For UAV sensing target scenarios, the following table is used as a starting point for deployment scenario parameters/values.
Note: Additional parameters, value/value ranges are not precluded.
Table x. Evaluation parameters for UAV sensing scenarios
| Parameters | Value |  |
| --- | --- | --- |
| Applicable communication scenarios | UMi, UMa, RMa [38.901] UMi-AV, UMa-AV, RMa-AV |  |
| Sensing transmitters and receivers properties | Rx/Tx Locations | Rx/Tx locations are selected among the TRPs and UEs locations in the corresponding communication scenario Note1: this may include aerial UEs for UMi-AV, UMa-AV, RMa-AV communication scenarios. [In this case, other Rx/Tx properties (e.g. mobility) are also taken from the corresponding communication scenario.] |
|  |  |  |
|  |  |  |
| Supported sensing modes | [All 6 sensing modes] |  |
| Sensing target |  |  |
|  | Outdoor/indoor | Outdoor |
|  | 3D mobility | Horizontal velocity: Up to 160 km/h [FFS specific velocity(ies) or random distribution] [FFS vertical plane velocity] |
|  | 3D distribution | [Uniform between a minimum and maximum height] [Uniform in horizontal domain at a given height] |
|  | Orientation | Random in horizontal domain |
|  | Physical characteristics (e.g., size) | UAV object type(s) [FFS] |
| [Sensing area] |  |  |
| Minimum 3D distances between pairs of Tx/Rx and sensing target/[unintended objects] | FFS |  |
| Minimum 3D distance between sensing targets | FFS |  |
| [Unintended/Environment objects, e.g., types, characteristics, mobility, distribution, etc.] | FFS |  |
R1-2404488	FL Summary #3 on ISAC Deployment Scenarios	Moderator (AT&T)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_117/) · `RAN1-117-isac-deployment-scenarios-75cbe2f1-a003`

### [5G-A/Rel-19 RAN1#117] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
RAN1 agrees to the following revised evaluation parameters values for the UAV sensing target scenarios:
| Parameters | Value |
| --- | --- |
| Sensing transmitters and receivers properties | Rx/Tx locations are selected among the TRPs and UEs locations in the corresponding communication scenario Note 1: Other Rx/Tx properties (e.g. mobility) can also be taken from the corresponding communication scenario. Note 2: This may include aerial UEs as Rx/Tx that can be selected among locations in the UMi-AV, UMa-AV, RMa-AV communication scenarios. |
|  |  |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_117/) · `RAN1-117-isac-deployment-scenarios-75cbe2f1-a004`

### [5G-A/Rel-19 RAN1#116b] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
The following cases of radio propagation in the target channel are considered for the study
| Case | Tx-target | Target-Rx |
| --- | --- | --- |
| 1 | LOS condition | LOS condition |
| 2 | LOS condition | NLOS condition |
| 3 | NLOS condition | LOS condition |
| 4 | NLOS condition | NLOS condition |
Case 1/2/3/4 can be considered for bistatic sensing mode
At least Case 1/4 can be considered for monostatic sensing mode
Note: It doesn’t imply the channel response for each link is separately generated then concatenated
FFS how to determine LOS condition and NLOS condition, e.g., based on LOS probability, or determined based on geometrical locations of environment object (EO).
In LOS condition, line of sight ray(s) are present between Tx/Rx and target, and there may or may not exist non-line of sight ray(s) between Tx/Rx and target too
In NLOS condition, there only exist non-line of sight ray(s) between Tx/Rx and target.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_116b/) · `RAN1-116b-isac-channel-modelling-fa5b802a-a001`

### [5G-A/Rel-19 RAN1#116b] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
In the target channel between Tx and Rx, scattering of a sensing target can be modelled as single scattering point or multiple scattering points
FFS one or multiple incoming/output rays corresponding to a scattering point
FFS how to select single or multiple scattering points for the target, e.g. depending on the distance between target and Tx/Rx, size/shape of target, etc.
Note: the sensing target can be assumed in far field of sensing Tx/Rx.
FFS details to model the single or multiple scattering points.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_116b/) · `RAN1-116b-isac-channel-modelling-fa5b802a-a002`

### [5G-A/Rel-19 RAN1#116b] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
RCS of a physical object shows dependency to at least the following factors:
Type of the object
The size of the object
The material of the object
The shape of the object
Orientation of the object
FFS: Distance between Tx/Rx and the object
The incident angle and scatter angle
The carrier frequency
polarization of the transmitter and receiver
FFS Temporal or spatial consistency
FFS antenna pattern
FFS whether/how to model the above factors in the CR, e.g. with an RCS model with a scattering point
R1-2402682	Summary #3 on ISAC channel modelling	Moderator (Xiaomi)
Presented in Thursday session
R1-2403715	Summary #4 on ISAC channel modelling	Moderator (Xiaomi)
From Friday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_116b/) · `RAN1-116b-isac-channel-modelling-fa5b802a-a003`

### [5G-A/Rel-19 RAN1#116b] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
EO is a non-target object with known location.
FFS other known parameters of the EO
FFS details on EO modeling
The following options for EO modeling are considered for further study
Option 1: EO is modelled different from a sensing target
Applicable at least for an EO having extremely large size (referred as EO type-2 for discussion purpose)
FFS modeled similar to section 7.6.8 ground reflection in TR 38.901
FFS EO modeling impacts the target channel and/or the background channel
Option 2: EO is modeled same/similar as a sensing target
Applicable for an EO having comparable physical characteristics as a sensing target, (referred as EO type-1 for discussion purpose)
FFS Applicable for EO type-2
FFS EO modeling impacts the target channel and/or the background channel
Option 3: EO is modeled and its location is determined from a stochastic clutter generated following the cluster generation in TR 38.901
FFS details
Option 4: EO is not modelled
Other options are not precluded
Note: it is not precluded that multiple options can be supported in the channel modelling
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_116b/) · `RAN1-116b-isac-channel-modelling-fa5b802a-a004`

### [5G-A/Rel-19 RAN1#116b] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
The following options are considered for further study to model the target channel for a target
Option 1: modelled by concatenation of path(s) from Tx to target and from target to Rx
Option 2: modelled by Tx-to-Rx path(s) satisfying Tx-target-Rx geometry
Option 3: combination of Option 1 and Option 2
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_116b/) · `RAN1-116b-isac-channel-modelling-fa5b802a-a005`

### [5G-A/Rel-19 RAN1#116b] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
If a target is modelled with single scattering point, the following options to model RCS of the target are considered for further study.
Option 1: Random RCS value generated by a statistical distribution, depending on the factor(s) having impacts on the RCS modelling.
FFS the distribution.
FFS the factor(s)
Option 2: Deterministic RCS value is defined by a function and/or a table, depending on the factor(s) having impacts on the RCS modelling
Note: Constant RCS for a target type can be a special case of Option 2
FFS the factor(s)
FFS details of function and/or table
Option 3: combination of Option 1 & 2, e.g., RCS value is generated by combining a deterministic component and a randomly generated component.
FFS application of each option to large scale fading and/or small scale fading
FFS target with multiple scattering points
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_116b/) · `RAN1-116b-isac-channel-modelling-fa5b802a-a006`

### [5G-A/Rel-19 RAN1#116b] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
Interested companies are encouraged to submit validation results together with their proposal for ISAC channel modeling
Up to each company to select the way for validation
Option 1: Experimental results
Option 2: Experimental results to validate a ray-tracing model, then the ray-tracing based results to validate the ISAC channel model
Note: the layout of the scenario used for validation is up to company choice
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_116b/) · `RAN1-116b-isac-channel-modelling-fa5b802a-a007`

### [5G-A/Rel-19 RAN1#116b] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
ISAC channel model for link level simulation is to be discussed after the system level channel model is sufficiently stable with basic functionalities.
Final summary in R1-2403716.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_116b/) · `RAN1-116b-isac-channel-modelling-fa5b802a-a008`

### [5G-A/Rel-19 RAN1#116b] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
RAN1 agrees the following ISAC terminology with minor modifications as follows:
For ISAC channel modelling, RAN1 uses the sensing related terminology as defined in TS22.137 or TR22.837 as a starting point for discussion purposes with the following definitions:
Sensing transmitter: the TRP or a UE that sends out the sensing signal which the sensing service will use in its operation. A sensing transmitter can be located in the same or different TRP or a UE as the sensing receiver.
Sensing receiver: the TRP or a UE that receives the sensing signal which the sensing service will use in its operation. A sensing receiver can be located in the same or different TRP or a UE as the sensing transmitter.
Sensing target: target that need to be sensed by deriving characteristics of the objects within the environment from the sensing signal.
Background environment: background (clutter and/or environmental objects) that are not the sensing target(s).
Mono-static sensing: sensing where a sensing transmitter that transmits a sensing signal and a sensing receiver that receives the sensing signal are co-located in the same TRP or UE.
Bi-static sensing: sensing where a sensing transmitter that transmits a sensing signal and a sensing receiver that receives the sensing signal are not co-located in the same TRP or UE.
Multi-static sensing: sensing where there are multiple sensing transmitters and/or multiple sensing receivers, for a sensing target.
Sensing signal: Transmissions on the 3GPP radio interface that can be used for sensing purposes.
R1-2403049	FL Summary #2 on ISAC Deployment Scenarios	Moderator (AT&T)
Presented in Wednesday session
R1-2403050	FL Summary #3 on ISAC Deployment Scenarios	Moderator (AT&T)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_116b/) · `RAN1-116b-isac-deployment-scenarios-75cbe2f1-a001`

### [5G-A/Rel-19 RAN1#116b] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
Any TRP and/or UE location in the corresponding communication scenario can be selected as sensing transmitters and receivers locations. FFS: other possible sensing transmitters and receivers locations.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_116b/) · `RAN1-116b-isac-deployment-scenarios-75cbe2f1-a002`

### [5G-A/Rel-19 RAN1#116b] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
The following table can be used by companies to propose values for each sensing target.
Additional parameters/rows can be added if needed
Table x. Evaluation parameter template for sensing scenarios
| Parameters | Value |  |
| --- | --- | --- |
| Applicable communication scenarios |  |  |
| Sensing transmitters and receivers properties |  |  |
| Supported sensing modes |  |  |
| Sensing target | Outdoor/indoor |  |
|  | 3D mobility |  |
|  | 3D distribution |  |
|  | Orientation |  |
|  | Physical characteristics (e.g., size) |  |
| [Unintended/Environment objects] | Types |  |
|  | 3D mobility |  |
|  | 3D distribution |  |
|  | Orientation |  |
|  | Physical characteristics (e.g., size) |  |
| [Sensing area] |  |  |
| Minimum 3D distances between pairs of Tx/Rx/sensing target/[unintended objects] |  |  |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_116b/) · `RAN1-116b-isac-deployment-scenarios-75cbe2f1-a003`

### [5G-A/Rel-19 RAN1#116] `agreement` isac-channel-modelling-fa5b802a ISAC channel modelling

```text
The common framework for ISAC channel model is composed of a component of target channel and a component of background channel,
Target channel  includes all [multipath] components impacted by the sensing target(s).
FFS details of the target channel
Background channel  includes other [multipath] components not belonging to target channel
FFS details of the background channel
FFS whether/how to model environment object(s), i.e., object(s) with known location, other than sensing target(s)
FFS whether/how to model propagation path(s) between the target(s) and the environment object(s)
FFS whether/how to model propagation path(s) between the target(s) and the stochastic clutter(s)
Note: the notation HISAC can be revised later if needed
Final summary in R1-2401496.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_116/) · `RAN1-116-isac-channel-modelling-fa5b802a-a001`

### [5G-A/Rel-19 RAN1#116] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
For progressing ISAC study, the following sensing targets and existing communication scenarios will be considered as a starting point:
Note1: the table below does not imply that the sensing target will be placed at positions defined for UEs and BSs in the scenarios in the right column.
Note2: the table below does not imply that UEs are necessarily placed at positions defined for UEs in the scenarios in the right column.
Note3: the existing communication scenarios are listed with the intent to use the evaluation parameters defined for those scenarios, as a starting point.
| Sensing Targets | scenarios |
| --- | --- |
| UAVs | RMa-AV, UMa-AV, UMi-AV (TR 36.777) |
| Humans indoors | InF, Indoor Office, [Indoor Room (TR 38.808)], [UMi, UMa] |
| Humans outdoors | UMi, UMa, [RMa] |
| Automotive vehicles (at least outdoors) | Highway, Urban grid, UMa, UMi, RMa |
| Automated guided vehicles (e.g. in indoor factories) | InF |
| Objects creating hazards on roads/railways (examples defined in TR 22.837) | Highway, Urban grid, HST |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_116/) · `RAN1-116-isac-deployment-scenarios-75cbe2f1-a001`

### [5G-A/Rel-19 RAN1#116] `agreement` isac-deployment-scenarios-75cbe2f1 ISAC deployment scenarios

```text
For ISAC channel modelling, RAN1 uses the sensing related terminology as defined in TS22.137 or TR22.837 as a starting point for discussion purposes with the following definitions:
Sensing transmitter: the TRP or a UE that sends out the sensing signal which the sensing service will use in its operation. A sensing transmitter can be located in the same or different TRP or a UE as the sensing receiver.
Sensing receiver: the TRP or a UE that receives the sensing signal which the sensing service will use in its operation. A sensing receiver can be located in the same or different TRP or a UE as the sensing transmitter.
Sensing target: target that need to be sensed by deriving characteristics of the objects within the environment from the sensing signal.
Background environment: background (clutter and/or environmental objects) that are not the sensing target(s).
Mono-static sensing: sensing where the sensing transmitter and sensing receiver are co-located in the same TRP or UE.
Bi-static sensing: sensing where the sensing transmitter and sensing receiver are in different TRPs or UEs.
Multi-static sensing: sensing where there are multiple sensing transmitters and/or multiple sensing receivers, for a sensing target.
Sensing signal: Transmissions on the 3GPP radio interface that can be used for sensing purposes.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_116/) · `RAN1-116-isac-deployment-scenarios-75cbe2f1-a002`

</details>

