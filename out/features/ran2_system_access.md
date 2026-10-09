# 6GR 初始接入与系统信息

**当前进展** · 阶段：—

_尚无综述_

## 6GR 演进

### [6G/Rel-20 RAN2#134] `agreement` 9.3.2.3 System Information

```text
1	Study per-SI-message configuration of SI-window width.  During the study of the various solutions, companies should consider UE impacts and avoid frequent SI updates.
2	Study supporting use of explicit window start positions (per SI message configurable position) and/or implicit window start positions (based on the order of SI message in the scheduling list) as in NR.  Study how this works with per SI window width and UE calculations
[POST134][021][6G CP] System Information (Apple)
Intended outcome:
SI window configuration and discuss if/how/impact to support sending multiple SIs in the same window at a time
On demand SI information
SI update mechanism
Deadline:  Long
On demand SI Request Mechanism
R2-2603731	Views on 6G system information	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.3-a001`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.3 System Information

```text
The flexible SI scheduling brings marginal UEPS benefit, since existing scheduling mechanism functions well and the UE only needs to receive SIBs once within a relatively long period.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.3-o001`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.3 System Information

```text
For 6GR SI framework, the following mechanisms should be considered:
	per-SI-message configuration of SI-window start position (e.g. per schedulingInfo entry)
	per-SI-message configuration of SI-window width
Noted
R2-2603434	Discussion on system information	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
Observation 1-4: 	In NR, the implicit and explicit SI window(s) determination mechanisms can be used together to reduce the overhead of SI configurations and improve the flexibility of SI window configurability for some SI messages.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.3-p001`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.3 System Information

```text
RAN2 to study supporting a mixed use of explicit window start positions (per SI message configurable position) and implicit window start positions (based on the order of SI message in the scheduling list) as in NR.
Observation 2-3:	Only supporting the SI window granularity offset for each SI window (as si-WindowPosition introduced in NR R17) may not allow the SI window of the first SI message to start immediately after SIB1 or other common signals. This will cause an increase in the total duration for sending the common signalling, which is not beneficial for network energy saving.
Observation 2-4:	Introducing the SFN or slot granularity offset for each SI window generates unnecessary overhead, and will render the implicit SI window unusable.
Observation 2-5:	Supporting the SI window granularity offset for each SI window (as si-WindowPosition introduced in NR R17) and introducing an SFN or slot granularity offset for all SI windows (i.e., Method 2) enables the SI window of the first SI message to start immediately after SIB1 or other common signals with minimal overhead.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.3-p002`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.3 System Information

```text
RAN2 to study a configurable start position of all SI windows (with SFN or slot granularity) in addition the per SI window start position (with SI window granularity, as si-WindowPosition introduced in NR R17), so that the SI transmission can be clustered with other common broadcast signalling.
Noted
Discussion per-SI-message configuration of SI-window width?
-	Vivo
-	Huawei thinks that if we have explicit and implicit, we have a single width.   CATT also thinks that both explicit and implicit help with the shortcomings.
-	Nokia thinks it is simple, that the windows are consequitive, we should at least configure the first window, but not sure if we need the subsequent windows, may be nice.  Nokia thinks that it is not a big problem even if the length is different it is not a problem.
-	Interdigital thinks it is important to have different SI window length as we will also have different types of devices and longer time/ messages and also offset to allow for power saving.
-	CMCC minimum SI length and for larger they can use multiple of minimum SI length, so we can save bits.
-	Vivo would like to avoid impact to the UE and whats important is that the behaviour is the same from the UE side.
-	Lenovo thinks that allowing multiple SIs in in one fixed window length, is not acceptable for UEs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.3-p003`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.3 System Information

```text
On demand SI design in 6G takes the NR Msg3 based OD-SI design as starting point.
R2-2603252	Discussion on the system information for 6GR	Google	discussion	Rel-20	FS_6G_Radio
Observation 3	Msg1-based Other SI request scheme requires less UE complexity and less UE power consumption for the SI acquisition, while the Msg3-based Other SI request scheme enables one request for multiple SIs and hence can avoid massive requests.
Proposal 2	RAN2 should study both Msg1- and Msg3-based Other SI request schemes in 6G.
[20 min]
On demand SI Delivery
R2-2602953	Discussion on 6GR system information design	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.3-p004`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.3 System Information

```text
To address the problem of reserving SI window for currently non-broadcasted SI, RAN2 support the solution as follows:
-	The SI window position of SI whose broadcast status is ‘non-broadcasting’, is not pre-reserved in SIB1. Broadcast status change is performed via SIB1 modification, and follows the SI modification period like other system information changes.
-	For temporary OD-SI transmission, its reception window is indicated to the UE via the response to the SI request, or via the L1 signalling transmitted on pre-defined occasions, or the OD-SI is indicated to the UE via the response to the SI request.
R2-2603666	System Information for 6GR	InterDigital, Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.3-p005`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.3 System Information

```text
RAN2 further study the three solutions for the problem of reserving SI window for not broadcasting SI message: 1) Moving SI windows forward when some SI are not being broadcast; 2) Configuring SI windows of on-demand SI at the end of the SI transmission period; 3) SI scheduling information of dynamically allocated windows provided upon SI request
[20 min]
SI Notification
R2-2603799	AreaScope and SI scheduling	Lenovo	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.3-p006`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.3 System Information

```text
Paging DCI includes SI-modification information on which SIB(s) have been modified/ updated so that UE acquires updated information only if the updated SIB(s) is of interest to it.
[20 min]
Area specific SIB1
R2-2603181	Discussion on 6G System information	OPPO	discussion	Rel-20	FS_6G_Radio
Observation 4	Based on the parameters defined in NR SIB1, some parameters that are not related to spectrum, time/frequency resources, and scheduling may be common across multiple cells in an area.
Proposal 2	For 6G SIB1, RAN2 to study area-based SIB1 acquisition based on the following schemes:
1) Option 1: Area‑specific SIB1 enables acquisition of only the common configuration shared by all cells within the area;
2) Option 2: Area‑specific SIB1 enables acquisition of all cell configurations within the area, regardless of whether common or cell‑specific, from any cell in the area.
[20 min]
Overlapping SI
R2-2603244	System Information for 6G	Ericsson	discussion	Rel-20
Observation 1	Multiplexing SIBs/SI messages with different periodicities within the same TB is of limited use because of the limited TBS and forces a UE to decode SIBs/SI messages which it may not be interested in.
Proposal 2	The following options for transmission of multiple SI messages within an SI window can be discussed further:
- Option 1 (TDM): The SI messages are transmitted sequentially in time within the SI window. The start of the next SI message transmission is indicated dynamically on PDCCH using e.g. different SI-RNTI or indication in DCI.
- Option 2 (FDM): The SI messages are transmitted on different parts of the carrier bandwidth (e.g. using different CORESETs or BWPs). A bandwidth limited UE may need to acquire different SI messages sequentially, e.g. SI1 in the first period and SI2 in the second period.
R2-2603364	System information for 6G radio	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.3-p007`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.3 System Information

```text
RAN2 should decouple the study of SI scheduling into separate targets:
Target 1 (Prioritize): Establish an extensible and unified SI scheduling scheme as the baseline framework. Consider R17 configurable starting position as baseline.
Target 2: Mechanisms for receiving SIs in a shorter period of time. Reevaluate the realistic power-saving gains and the corresponding impacts in different directions, while concurrently comparing them against alternative NES features (e.g., OD-SIB)
[20 min]
R2-2602974	Discussion on system information design in 6GR	Xiaomi	discussion	Rel-20	FS_6G_Radio
R2-2603029	Discussion on System Information	CATT	discussion	Rel-20	FS_6G_Radio
R2-2603043	Discussion on System Information	NEC	discussion	Rel-20	FS_6G_Radio
R2-2603065	System information in 6G	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
R2-2603233	Energy Efficient System Information for 6G	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
R2-2603300	System Information in 6G	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2603327	Discussion on 6GR system information	China Telecom	discussion	Rel-20	FS_6G_Radio
R2-2603533	Discussion on 6G System Information	DENSO CORPORATION	discussion
R2-2603573	System Information for 6G	LG Electronics Inc.	discussion	Rel-20
R2-2603597	Discussion on system information for 6GR	TCL	discussion
R2-2603623	6G system information	Sony	discussion	Rel-20	FS_6G_Radio
R2-2603738	Discussion on SI clustering and scheduling mechanism	Panasonic	discussion	Rel-20
R2-2603791	Discussions on 6G System Information	Futurewei	discussion	Rel-20	FS_6G_Radio
R2-2603840	Considerations on On-demand SI	ETRI	discussion
R2-2603843	Discussion on System Information in 6GR	Sharp	discussion	Rel-20	FS_6G_Radio
R2-2603868	Discussion on 6G system information	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2603901	Discussion on system information of 6GR	Spreadtrum, UNISOC	discussion	Rel-20
R2-2603979	Discussion on System Information for 6GR	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2604030	6GR System Information Design	Samsung	discussion	FS_6G_Radio
R2-2604039	Discussion on system information for 6GR	ITL	discussion	Rel-20	FS_6G_Radio
R2-2604054	Discussion on 6G System Information	Qualcomm Incorporated	discussion
R2-2604064	System Information Provisioning in 6G	1Finity	discussion	Rel-20
R2-2604065	System Information Scheduling in 6G	1Finity, Ericsson, Rakuten Inc, NTT Docomo, NEC	discussion	Rel-20
R2-2604069	System Information Handling	Nokia	discussion	Rel-20	FS_6G_Radio
R2-2604080	Discussion on System Information Design for 6GR	CEWiT	discussion	Rel-20	FS_6G_Radio
R2-2604094	Discussion on the 6G system Information	CSCN	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.3-p008`

### [6G/Rel-20 RAN2#133bis] `agreement` 9.3.2.3 System Information

```text
1	Study periodic SI window, including configurable width of window(s), configurable start position.
2 	Study how to address the problem of reserving SI window for currently non-broadcasted SI
Multiplexing Multiple SIBs for flexible SI scheduling
R2-2602540	Discussion on 6G System Information	Qualcomm Incorporated	discussion
RAN2 can study the following directions for flexible SI scheduling enhancements, the study and evaluation should consider network saving gain, UE power consumption, UE implementation complexity, impact on SI modification, etc.
- Direction 1: SIBs with different periodicities can be transmitted into one TB, e.g. SIBs with different periodicities are mapped into one SI message (RRC PDU) or SI messages with different periodicities are multiplexed into one MAC PDU.
- Direction 2: Multiple SI messages are transmitted within one SI-window. The SI transmissions within the SI-window can be interleaved or in sequence or any pre-configured time resource pattern.
- Direction 3: Multiple SI messages can be transmitted via different frequency resources (e.g. BWPs or sub-bands). The frequency resource for each SI is pre-configured to the UE.
-	Xiaomi asks if the motivation is to shorten SI transmission and if so direction 2 won’t work.   1 and 3 would have RAN1 impact and UE complexity.  Apple agrees with Xiaomi, we should focus on simple solutions.  Oppo agrees too.
-	Qualcomm ask what is the assumption on how SI it is scheduled. Qualcomm explains that it can be transmitted over multiple frequencies at the same time.
-	Interdigital, Vivo, thinks that direction 3 has the benefit that the UE doesn’t need to decode all the other SIs.  Ofinno agrees and we may need to also take into account multi carrier impacts.
-	Mediatek still is not clear on the motivation, the UE can already receive the SI in short time and the benefits is very marginal from the UE side.
-	Xiaomi thinks that we can analyze the RAN1 impact.
-	Lenovo thinks that we should target how to make SI update more efficient.
Noted
Not treated
On-Demand SIB
R2-2602423	Discussion on 6G system information	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.3-a001`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.2.3 System Information

```text
For contributors of NR SIB1 size:
-	The main overhead lies in DL and UL BWP configurations for approximately 70% (including initial UL, initial DL, SUL, and initial DL/UL for specific features like RedCap);
-	When SUL or initial DL/UL for RedCap is configured, it means the size of the BWP-related configuration shall at least double (compared to only initial UL/DL BWP for normal link).
-	SI scheduling info, PLMN ID related list, UAC related list can vary in proportions based on different quantities configured, but in real deployment they count for approximately 15%-20%;
-	Other parameters such as timers or constants will count for less than 5%;
-	It is highly possible that the SIB1 size would exceed the 2976 bits limitation if network wants to configure multiple SI/ PLMN ID list/ UAC list and support extra features like RedCap.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.3-o001`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.2.3 System Information

```text
When SIB1 is split and part of it is moved to OSI, in worst case the latency to acquire the complete SIB1 is expected to be equal to the shortest SI message periodicity (typically 80 ms).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.3-o002`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.2.3 System Information

```text
A significant portion of the current NR SIB1 consists of UL and DL cell configurations (e.g., servingCellConfigCommon, RACH configurations, and initial BWP). Most of this information is only required when the UE actively initiates access, not when it is merely camping.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.3-o003`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.2.3 System Information

```text
Moving access information to a different SI message to solve the SIB1 size issue introduces an access delay compared to NR due to two-step acquisition and the need to acquire within an SI window. This should be avoided in 6G.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.3-o004`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.2.3 System Information

```text
Lesson learned from 5G: A large amount of SIB1 in 5G consists of system information needed to support specific features or verticals. Camping and access information specific to certain features/verticals has resulted in increase in SIB1 size and often unnecessary network/UE power consumption.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.3-o005`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.2.3 System Information

```text
Most efficient way to enhance network energy saving is to send SIB1 as seldomly as feasible
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.3-o006`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.3 System Information

```text
RAN2 to confirm that the increased latency introduced by SIB1 split is acceptable and not considered as a showstopper for the SIB1 split study. FFS whether and how to improve the latency.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.3-p001`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.3 System Information

```text
RAN2 to discuss the following three methods of SIB1 splitting and to conclude on RAN2 preference:
-	Method 1: Fields related to UE access are moved to a subSIB1;
-	Method 2: Fields that are area-specific are moved to a subSIB1;
-	Method 3: Fields that are for different device types (e.g., eMBB UEs) are moved to a subSIB1.
Noted
R2-2601507	System information in 6GR	Xiaomi	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.3-p002`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.3 System Information

```text
RAN2 can assume that the size of the information that can be split out from NR Rel-15 SIB1 (including UE access related information and paging information) ranges from about 200 bits (based on RAN5 test setup) to 12000 bits (the maximum size allowed by ASN.1 signalling, and the actual size in real deployment can be much smaller, e.g. one order of magnitude).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.3-p003`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.3 System Information

```text
RAN2 discusses whether to move UE access related information and paging information outside of SIB1, considering the main trade-off being the SIB1 size reduction at the cost of latency of access to network (if UE has not obtained the related information).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.3-p004`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.3 System Information

```text
RAN2 assumes SIB1 includes the information commonly applied to all features/device types in 6GR.
Noted
R2-2602197	System Information for 6GR	InterDigital, Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.3-p005`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.3 System Information

```text
Structure SIB1 as two separately transmitted SIBs: 1) primary SIB1 which contains at least PLMN information, (re)selection parameters and cell barring; 2) SIB1x which contains UL and DL access BW configurations, RACH resources, and access control parameters.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.3-p006`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.3 System Information

```text
Primary SIB1 and SIB1x follow scheduling principles similar to legacy SIB1 (i.e., SIB1x does not rely on SI window concept).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.3-p007`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.3 System Information

```text
SIB1x contains at least the camping and access parameters relevant to the minimum device capabilities supported by all UEs.  Additional vertical/feature specific access information or information related to other carriers can be broadcast in a different version of SIB1x.
Noted
R2-2601669	System Information Handling	Nokia	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.3-p008`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.3 System Information

```text
6G should to enable sending of SIB1 less frequently than in 5G  and enable splitting of SIB1 information flexibly without fixed information contents for different instances of SIB1
Noted
Discussion
-	Lenovo asks if the ASN.1 structure will be the same for both SIB1 and SIBx and the network can send whatever it wants.  Nokia confirms.
-	Fujitsu thinks that flexible splitting can be very complex from UE perspective.   Mediatek agrees.  Apple thinks that we should cover some principle for the splitting first and then we can consider.  Huawei doesn’t think it would be complicated for the UE as it should be following some defined rule and what can actually be split.  It can be even simpler, if SIB1x is not schedule then everything is in SIB1.   Currently there is not commercial deployment that has exceeded the size.
-	Qualcomm thinks the splitting should be fixe and SIB1 should be cell specific.
-	Apple thinks that we should first discuss how to split and area specific SIB1 should be one good direction.
-	CATT doesn’t think the flexible split is friendly to operators.
-	Docomo thinks that always splitting can add overhead as it may not need to split always.  CMCC also agrees that SIB1 splitting is good, for example area specific can go SIB1x and fixed separation.
-	Vodafone explains that in real deployment the size of SIB1 is much much smaller than the theoretical size.   Why don’t we consider putting some of the elements in SIB2 instead of having a SIBx to reduce the size.
-	Xiaomi thinks that there is no problem in NR so maybe we don’t to conclude feasibility.  ZTE explains that if we have NTN info in SIB1 the size will be much larger so there may be a problem in 6G.
-	Ericsson doesn’t think that splitting will increase the access latency as it is rare that the UE camps and wants to access at the same time.  The motivation is not only for SIB1 size limitation it is also about beam based system where there is benefits with smallest SIB1 size.
Agreements on SIB1 splitting
For now pause SIB1 splitting discussions, until further progress is made on the content of SIB1 for 6G or new requirements.
At least the following options can be discussed when the discussion resumes:
-	1: Fields related to UE access are moved to a SIB1x or another SIB;
-	2: Fields that are area-specific (if supported) are moved to a SIB1x;
-	3: Fields that are for different device types/features (e.g., eMBB UEs) are moved to a SIB1x.
Further study motivation of splitting and whether it is fixed or flexible split (e.g. simple flexible split)
Barring
R2-2602545	System Information Provisioning in 6G	1Finity	discussion	Rel-20
Proposal#1: CellBarred bit and intraFreqReselection bit is not required in the 6GR MIB.
-	Huawei thinks that the cell barring in MIB is still important to bar all UEs and it can be useful for future releases.
-	LG thinks that the benefit of having barring in MIB is not substantial.
-	Nokia doesn’t know yet if it is needed, in 5G we never used it.    But not sure if it is useful in 6G.
-	Ericsson also thinks that we can consider moving it in SIB1
Not ready to make a decision yet.  Wait until end of release to revisit it
Noted
SI Window Configuration for Flexible SI Scheduling
R2-2601573	Discussion on 6G system information	OPPO	discussion	FS_6G_Radio
Observation 8	System information clustering can be realized by adapting SI scheduling parameters (e.g., si-window length), similar to the paging clustering mechanism in NR R19 NES.
Proposal 4	For SI scheduling, RAN2 studies mechanisms to enable shorter SI transmission durations by adapting SI scheduling parameters based on network load, including:
1)	Support SI‑window position indication (similar to si-WindowPosition in NR).
2)	Support adaptation of SI‑window width.
-	Xiaomi asks if this means that they will be overlapping within window.  Oppo explains no and it is just discussing about configuring the window.
-	Interdigital asks if we have one SI-window width or multiple.  Oppo thinks both can be considered.
Noted
R2-2601709	Discussion on system information	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
Observation 4-2:	The fixed SI window start based on the SFN=0 and slot =0 in 5G results in a relatively long length of the SI window in the case of clustering/bundling transmissions of common signals, thereby causing a relatively long total duration for sending SI messages, and affecting power consumption of the network and UEs.
Observation 4-3:	The SFN or slot granularity offset can shorten the length of the SI window and the total duration for sending the common signaling.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.3-p009`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.3 System Information

```text
RAN2 to study a configurable start position of SI windows (with slot granularity) in addition the per SI window start position (with SI window granularity, as si-WindowPosition in Rel-17 in NR), so that the SI transmission can be clustered with other common broadcast signaling.
Observation 5-1:	Some OD-SI messages occupy SI window time even if they are not transmitted, thereby causing a relatively long total duration for sending SI messages, and affecting power consumption of network and UEs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.3-p010`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.3 System Information

```text
RAN2 to study a dynamic SI window allocation for OD-SI, e.g. only allocating SI windows when the related OD-SI is broadcasting.
Noted
SI messages -
enable shorter SI transmission durations (configurable window, position)
dynamic SI window allocation
-	CATT thinks that proposal 4 are interesting and Huawei’s proposal help clustering.  Qualcomm is not sure what common signaling can be clustered.   RAN1 is discussing SSB periodicity so we don’t know how to cluster.
-	LG asks how the UE know the SI window for proposal 5.
-	Vivo supports the proposal 5 direction.
-	Mediatek thinks we can start by first having configurable SI window starting point.
-	ZTE suggest to re-word SI window allocation only for broadcasted SIBs
-	Shorter the overall time for SI messages, and clustering
-	Ericsson thinks that we shouldn’t exclude the possibility of dedicated OD SI
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.3-p011`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.2.3 System Information

```text
For on-demand SI mechanism, the following can be considered in 6G:
	Support on-demand (other) SI mechanism;
	MSG3 based UE request OD SI should be baseline
	MSG3 based on-demand SI is specified as UE mandatory feature.
R2-2601738	Discussion on the system information for 6GR	Google	discussion	Rel-20	FS_6G_Radio
Observation 3	Msg1-based Other SI request scheme requires less UE complexity and less UE power consumption for the SI acquisition, while the Msg3-based Other SI request scheme enables one request for multiple SIs and hence can avoid massive requests.
Proposal 2	RAN2 should study both Msg1- and Msg3-based Other SI request schemes in 6G.
R2-2601440	Discussion on System Information	CATT	discussion	Rel-20
R2-2601491	AreaScope, SI scheduling and SIB1-Split	Lenovo	discussion	FS_6G_Radio
R2-2601529	System Information for 6G	Ericsson	discussion	Rel-20
R2-2601592	Discussion on System Information	NEC	discussion	Rel-20	FS_6G_Radio
R2-2601685	System information in 6G	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
R2-2601758	System information for 6G radio	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
R2-2601861	System Information in 6G	Ofinno	discussion
R2-2601890	Consideration on system information on 6GR	BYD	discussion
R2-2601943	Discussion on system information for 6GR	TCL	discussion
R2-2601961	System Information for 6G	LG Electronics Inc.	discussion	Rel-20
R2-2601970	Consideration on 6GR system information	China Telecom	discussion	Rel-20	FS_6G_Radio
R2-2602005	Discussion on the 6G system Information	CSCN	discussion	Rel-20	FS_6G_Radio
R2-2602038	Discussion on SI clustering and scheduling mechanism	Panasonic	discussion	Rel-20
R2-2602074	Discussion on System Information for 6GR	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2602099	Discussion on system information of 6GR	Spreadtrum, UNISOC	discussion	Rel-20
R2-2602119	On GNSS availability and area-specific SI for 6G NTN	Lenovo	discussion	Rel-20
R2-2602164	6G system information	Sony	discussion	Rel-20	FS_6G_Radio
R2-2602231	Views on 6G System Information	Apple	discussion	Rel-20	FS_6G_Radio
R2-2602362	Considerations on System Information	Sharp	discussion
R2-2602366	Considerations on SIB1 design and contents	ETRI	discussion
R2-2602475	Views on 6G System Information	NTT DOCOMO	discussion	Rel-20
R2-2602483	6GR System Information Design	Samsung	discussion	FS_6G_Radio
R2-2602508	Discussion on system information for 6GR	ITL	discussion	Rel-20	FS_6G_Radio
R2-2602512	Discussions on 6G System Information	Futurewei	discussion	Rel-20	FS_6G_Radio
R2-2602517	Discussion on 6G System Information	DENSO CORPORATION	discussion
R2-2602537	Considerations on System Information for 6G	KDDI Corporation (TTC)	discussion
R2-2602565	Discussion on System Information	CEWiT	discussion	Rel-20	FS_6G_Radio	Late
R2-2602610	Discussion on 6G System Information	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.2.3-p012`

### [6G/Rel-20 RAN2#133] `agreement` 10.3.2.3 System Information

```text
1.	SIB1 needs to provide at least:
-	Cell basic camping information to determine suitability check for camping
-	Cell barring information required for suitability check.  FFS cell barring in MIB.
-	Enough scheduling information to received at least the next SIB (e.g. SIB1x whatever it is called).
2.  Study splitting everything else not included in 1 out of SIB1 and analyse the trade-offs of such splitting on system performance.
3.  For next meeting bring concrete examples of the main contributor of SIB1 size in 5G.
Not treated
Area specific SIB1
R2-2600249	System Information for 6G	Ericsson	discussion	Rel-20
Proposal 7	Study whether a minimum set of SIB1 parameters (with a significant size) can be specified as area-wide configured.
R2-2600832	System Information Provisioning in 6G	Fujitsu	discussion	Rel-20
Observation#5: In real deployment majority of SIB1 contents for at least intra-frequency cells are same and hence no need to restrict SIB1 scope as solely cell specific. If RACH/PRACH config list is included, then this information becomes area specific. Cell selection information, serving cell common configuration, paging configuration etc for intra-frequency cells can be area specific.
Observation#6: If SIB1 is area-specific then UE needs not re-acquire SIB1 upon cell reselection where area scope of SIB1 is valid thus saving UE battery.
Proposal#2: SIB1 in 6G can be specified as either cell-specific or area-specific depending on operator deployment scenario. Whether the SIB1 is cell-specific or area-specific is indicated in MIB.
R2-2601008	Discussion on 6G System Information	Qualcomm Incorporated	discussion
Observation 3	The scheduling information in SIB1 should include the area information (e.g. area ID, version) of other SI, when UE enters this cell, UE determines whether to obtain other SI based on the area information indicated in SIB1.
Proposal 3	SIB1 should be cell specific, and UE should acquire SIB1 when entering a new cell.
Proposal 4	Initial access information (e.g. UAC, common UL configuration) can be scheduled as follows:
-	Initial access information (e.g. UAC, common UL configuration) can be included in a separate SIB from SIB1.
-	The SIB containing initial access information can be area specific.
Not treated
On Demand SI
R2-2600669	Discussion on system information of 6GR	Spreadtrum, UNISOC	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.3-a001`

### [6G/Rel-20 RAN2#133] `agreement` 10.3.2.3 System Information

```text
Study further SI scheduling mechanisms to enable transmissions of SIs in a shorter period of time
Study an a flexible SI scheduling mechanism based on window scheme
The study should take into account the tradeoffs between gains and complexity.
The design should address all devices, including the low end devices
SI Update (if time permits)
R2-2600234	System information for 6G radio	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.3-a002`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.3 System Information

```text
5G on-demand SIB1 mechanism cannot work well in the standalone mode, since UE is required to acquire the OD-SIB1 request configuration for one NES cell from other cells.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.3-o001`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.3 System Information

```text
A large amount of SIB1 in 5G consists of system information needed to support specific features or verticals.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.3-o002`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.3 System Information

```text
Lesson learned from 5G: Camping and access information specific to certain features/verticals has resulted in increase in SIB1 size and often unnecessary network/UE power consumption.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.3-o003`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.3 System Information

```text
On-demand SI can achieve energy efficiency. Compared with Msg3-based on-demand SI in IDLE/INACTIVE, Msg1-based method provides lower latency but occupies more RACH resources. And the supported on-demand SIBs in CONNECTED include posSIBs, SIB22 for ATG and so on.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.3-o004`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.3 System Information

```text
5G SI scheduling mechanism may reduce network’s scheduling and UE monitoring complexity, while reduce both network and UE’s energy efficiency when multiple SI message should be broadcasted or received.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.3-o005`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.3 System Information

```text
Mapping multiple(N) SI-message into less SI windows(<N) can reduce both network and UE’s energy consumption, while increase network’s scheduling complexity, since more SIB are transmitted in the same SI window.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.3-o006`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.3 System Information

```text
The flexible SI scheduling that aggregates SIBs of different periodicities in the same SI-window can lead to impact on UE implementation complexity or wasted UE power consumption for SI reception as listed in Table 1. If such an SI scheduling mechanism is supported, it has to be an essential UE feature, with the complexity or power consumption wastage unavoidable for every UE implementation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.3-o007`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.3 System Information

```text
It is unclear whether aggregating SIBs of different periodicities into the same SI-window can really save the NW energy consumption, with the observation that the number of SI window/duration of SI transmission can be reduced but the energy consumption within each SI-window is increased.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.3-o008`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.3 System Information

```text
The drivers for the original SI window design are still valid in 6G, but the complexity of the NR SI scheduling design(s) calls for some enhancements/simplifications.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.3-o009`

### [6G/Rel-20 RAN2#133] `observation` 10.3.2.3 System Information

```text
The problem of UEs needing to wake up for every SI change may be expected to be worse in 6G, especially if paging is monitored by a low-power radio.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.3-o010`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.3 System Information

```text
6G on-demand SIB1 design takes NR design as starting point, and RAN2 focus on non-standalone OD-SIB1 first.
Noted
R2-2601123	System Information in 6G	Nokia	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.3-p001`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.3 System Information

```text
OD-SIB procedures for 6G could be based on UE sending RACH/WUS to the cell. 6G should support methods provide WUS configuration from the cell for which SIB1 request is sent as well as providing WUS configuration from another cell (like 5G OD-SIB1) and involve RAN1 request feasibility for coverage layer on demand SIB1 support.
Noted
Discussion
-	Nokia thinks it would be nice to be able to have OD-SIB1 for standalone and RAN1 may need to provide the information in MIB like message.  Huawei agrees with Nokia and thinks that standalone can be feasible.  We shouldn’t close the door to non-standalone as we don’t know yet what RAN1 will be able to provide.
-	CMCC is fine with standalone and for non-standalone it may also depend on whether we have split SIB1, the SIB1b can be requested on demand.
-	Ericsson thinks that we have on-demand SIB1 we don’t need assisted OD-SIB1.
-	Lenovo thinks that if we don’t have OD-SIB1 then we have to ensure coverage everywhere and it kills the benefits of energy savings.  There are solutions that we should consider for 6G.
-	LG thinks that the only difference is how the WUS configuration is provided to the UE for OD-SIB1.
-	Docomo thinks that we should support it and there are other solutions that don’t require RAN1 like a configuration in the SIM
-	Xiaomi has a concerns to study the OD-SIB1 as it has impact to the UE in terms of camping delay and energy consumption.   RAN1 is discussing the scenarios.
-	CATT clarifies that we are talking about the basic SIB1 needed for access.   OD-SIB1 is beneficial for low activity times.   The MIB can carry this information but that is designed by RAN1.
-	Qualcomm shares the same concerns with Xiaomi as to transmit the WUS it may need to use full power and at the end the cell won’t be suitable for camping.
-	Fraunhoufer thinks that we have a new scenario that we didn’t have before.  5G cell that provide coverage.  If we talk about MIB we can have a table with some index.
-	Interdigital sees benefits to support OD-SIB1 and the main use case is overnight scenarios where there is no UEs.  So delay is not a big issue.   How this information can be carried can be up to RAN1, e.g. MIB or preconfigured.
-	Mediatek points out that the MIB may not be much larger than in 5G and also we don’t know what the WUS configuration would look like.
-	Vivo thinks that we can tell RAN1 that one issue is that even if the UE requests the UE can’t camp.   So we would have to avoid this useless request, so they should consider how to make this request meaningful.
-	Futurewei thinks standalone and non-standalone can be considered.
-	Fujitsu supports standalone and thinks that we have to discuss area specific SIB1.   Can indicate to RAN1 that from RAN2 point of view there is some benefits.
-	Apple also doesn’t like it from UE perspective and also if we consider the energy efficiency we need to also consider SSB.
-	Huawei thinks that there are dependencies on RAN1 but RAN2 can study it as well.   In a clustered signal configuration, the SIB1 would be transmitted as soon as WUS is transmitted so not much delay.   Mediatek points out that in RAN2 we don’t know if such clustered configuration is even possible.  We should discuss what SIB1 structure looks like.
-	Fraunhofer thinks that there are things like cell suitability and find ways to avoid it.
-	Nokia explains that the benefits is from network energy saving point of view.
-	Ericsson thinks that if we keep SSB transmission the benefits are not really there and if we go with standalone the price we have to pay may be higher than the gain.  There maybe a gain if we extend the SSB transmission to 160ms.
-	Ericsson thinks that we need to make sure that RAN1 is evaluating.
-	Ofinno thinks that there was evaluation in 5G and that’s why they are not further evaluating.   Maybe we can send an LS to make sure they are making the evaluations.  Interdigital thinks that we can send the LS to RAN1 and we assume that the WUS configuration will have to come from somewhere.
Further study of standalone OD-SIB1, will be considered after RAN1 progress on feasibility and benefits of OD-SIB1.
No discussion on OD-SIB1 expected for next RAN2 meeting
SIB1 Contents and size considerations
R2-2600406	Discussion on system information	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
Observation 4-1:	In typical or basic configuration scenarios, the current SIB1 size can already meet the requirements. However, in complex deployment scenarios the SIB1 size would be the limitation to enable more features.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.3-p002`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.3 System Information

```text
At least basic camping/access related configurations and basic SI scheduling configuration shall be included in SIB1 to avoid performance degradation (i.e., increased access delay by consuming extra time resources) in the majority of deployment scenarios.
Noted
R2-2600249	System Information for 6G	Ericsson	discussion	Rel-20
Observation 5	In NR, large SIB1 messages are transmitted over multiple symbols (e.g. 12). This is a problem especially when there is a need for beam-sweeping in many directions and multiple repetitions.
Observation 6	SIB1 size can potentially be reduced by moving parts of the SIB1 contents (e.g., access related information like UAC) to another SIB.
Noted
R2-2600441	System Information for 6GR	InterDigital France R&D, SAS	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.3-p003`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.3 System Information

```text
SIB1 contains at least the camping and access parameters relevant to the minimum device capabilities supported by all UEs.  FFS if additional vertical/feature specific information is needed and how to broadcast it in a signalling efficient way.
Noted
Discussions
Cell barring
-	CMCC and Nokia think that cell barring doesn’t need to be in the MIB.   Xiaomi cell bar indication in MIB and some addition information on cell barring.  The basic MIB barring indication should remain.
-	 CMCC thinks that we should have unified barring in MIB.
-	Lenovo thinks that we use barring in MIB to completely block the cell.   So that needs to remain there.  But the additional cell barring information can move to another SIB.  Cell access information can be moved.
-	Fujitsu thinks we should keep the cell baring we have now in SIB1
-	Apple thinks that we should first discuss the cell baring in 6G and then we can discuss whether it should be in SIB1.
-	Fraunhoufer thinks that we should optimize the way we do cell barring.
Access information
-	ZTE thinks that we need to guarantee that cell access information needs to be available in the UE before the access is initiated.  Nokia agrees but we can consider sending that less frequenty.
-	Mediatek thinks that if we split access information we need to evaluate the impact.
-	Qualcomm thinks it can be split it can be area specific.
-	CATT thinks that this is related to coverage so the smaller SIB1 the better.
-	Vivo thinks that even if it is not in the first SIB1 it can be in the essential SI, we can at least confirm that it is an essential SI that should be acquired as soon as possible.   Oppo explains that even in 5G it is in SIB2 but the UE has to acquire both SIB1 and SIB2.
-	Apple thinks that this is what contributes the most to the SIB1 size so it would better to split off.   Interdigital thinks that we should look at trade off, SIB1, latency, and should try to avoid all the different types of devices in SIB1.
-	LG thinks that UAC and RACH information should come together.
-	How to access and how to determine scheduling of other SIBs.
-	Ericsson thinks that we should look into concrete examples on the actual size of the information in the SIBs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.3-p004`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.3 System Information

```text
The Msg1 and Msg3-based SI request mechanism in NR can serve as the starting point for the 6G OD-SI procedure.
R2-2600069	Discussion on System Information	CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.3-p005`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.3 System Information

```text
RAN2 study on-demand SI in non-connected mode for 6GR only within Msg3-based method, and on-demand SIBs in connected mode for 6GR.
SI Scheduling
R2-2600949	Discussion on 6G System Information	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.3-p006`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.3 System Information

```text
6G SI-scheduling is proposed to be based on SI-window.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.3-p007`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.3 System Information

```text
RAN2 can further discuss the following two SI and SI-window mapping mechanisms:
­	SIs with different periodicity are mapped into different SI windows that doesn’t overlap with each other.
- 	SIs with different periodicity are mapped into less SI windows, in other words, some SI windows may overlap in time domain.
-	Apple asks if the SI window can be configurable or fixed length.
-	MEdiatek asks how to resolve the ambiguity in the UE side and how the UE can combine the different SIs received in the overlapping window.
Noted
R2-2600122	Discussion on System information in 6GR	Xiaomi	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.3-p008`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.3 System Information

```text
For the study on aggregating SIBs of different periodicities in the same SI window, RAN2 should first justify the benefits on the NW energy saving, and (if justified) carry out the study taking into account the impacts on UE implementation and RAN1 dependency by various options listed as follows:
	[Option 1-1]: Map the SIBs of different periodicities into different SI messages which are transmitted in the same SI window
-	Impact to UE implementation complexity: Differentiating TB corresponding to each SI in the same SI-window; Multiple broadcast HARQ processes for combining TBs of different SIs;
	[Option 1-2]: Map SIBs of different periodicities into different SI windows, but allow these SI windows to be overlapped in time domain.
-	Impact to UE implementation complexity: Differentiating TB corresponding to each SI in the overlapped SI-window; Multiple broadcast HARQ processes for combining TBs of different SIs; Multiple SI window calculations for different SIs;
	[Option 2]: Map the SIBs of different periodicities into the same SI message
-	Impact to UE power consumption: UE power waste to decode/receive uninterested SIB(s).
The study needs to take into account also potential RAN1 impacts of each option, including "How UE differentiates TBs carrying different SIs in the same/overlapped SI window based on L1 scheduling info" (for Option 1-1/1-2), " Specific MCS options and TBS limit for SI transmission/reception." (for Option 2), etc.
Noted
R2-2600234	System information for 6G radio	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.3-p009`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.3 System Information

```text
Study an approach to SI scheduling in which the window scheme is adapted for flexibility, considering as possible enhancements overlapping windows, multiple SI-RNTIs, explicit scheduling of window positions, and grouping of service-specific SIBs, considering the need for UEs to combine SI message repetitions.
Noted
Discussion
-	Nokia would like to have the flexibility to sometimes schedule the SIBs in consecutive slots but if they are big it is better to spread them a bit.
-	Ericsson thinks that if we use different windows we would needs to wait for the window to be finished.
-	Qualcomm explains that this was discussed in NR-U and there was two options, DCI indication or different RNTI.
-	Samsung thinks that we can study further.
-	Lenovo asks the real question should be for what are we designing, eMBB or other low end devices that don’t have multiple HARQ buffers also for coverage we may need to have more than one window.
-	Mediatek thinks that we should design for all devices and that would be the lowest end devices.
-	Interidigital agrees with mediatek papers and area’s of study.
-	Huawei thinks that the main problem is the ability to combine transmission of SIs in a shorter period of time.
-	Xiaomi asks what is the motivation for this enhancements.   Ericsson thinks that of course there is network energy savings but there are other cases like sending emergency messages.
-	Mediatek highlights that for UE we have four different scheduling mechanisms.  So we should have a unified solution.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.3-p010`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.2.3 System Information

```text
Study (from RAN2 perspective and cooperate with RAN1) an increase in granularity for the SI change notification, with the objective of grouping SI changes and reducing wake-up events for UEs not interested in the SIB(s) that changed.
Not treated
R2-2600081	Discussion on 6GR system information design	vivo	discussion	Rel-20
R2-2600113	On system information, paging, initial access and spectrum aggregation related aspects	Xiaomi	discussion	Rel-20	FS_6G_Radio	Withdrawn
R2-2600270	Discussion on System Information	NEC	discussion	Rel-20	FS_6G_Radio
R2-2600278	Standalone on-demand SIB1 in 6GR	Fraunhofer IIS, Fraunhofer HHI, CEWiT, Deutsche Telekom	discussion	Rel-20	FS_6G_Radio
R2-2600433	Considerations on System Information	SHARP Corporation	discussion
R2-2600487	Discussion on 6GR system information	China Telecom	discussion	Rel-20	FS_6G_Radio
R2-2600495	Consideration on system information for 6GR	BYD	discussion
R2-2600501	Discussion on System Information for 6GR	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2600545	System Information for 6G	LG Electronics Inc.	discussion	Rel-20
R2-2600554	System Information for 6GR	Samsung	discussion	FS_6G_Radio
R2-2600563	Discussion on system information for 6GR	TCL	discussion
R2-2600624	Views on SI Design	Fainity Innovation	discussion
R2-2600648	System Information in 6G	Nokia	discussion	Rel-20	FS_6G_Radio
=> Revised in R2-2601123
R2-2600691	Views on 6G System Information	NTT DOCOMO, INC.	discussion
R2-2600713	System information in 6G	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
R2-2600752	On NTN specific aspects for SI design in 6GR	Lenovo	discussion	Rel-20
R2-2600763	6G system information	Sony	discussion	Rel-20	FS_6G_Radio
R2-2600796	Deployable SI distribution	Lenovo	discussion	FS_6G_Radio
R2-2600860	System Information in 6G	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2600882	Considerations on system information	ETRI	discussion
R2-2600898	Discussions on 6G System Information	Futurewei	discussion	Rel-20	FS_6G_Radio
R2-2600970	Considerations on System Information	KDDI Corporation (TTC)	discussion
R2-2601012	System Information Design for NTN	Amazon Web Services	discussion
R2-2601034	Discussion on the 6G system Information	CSCN	discussion	Rel-20	FS_6G_Radio
R2-2601045	Discussion on System Information	CEWiT	discussion	Rel-20	FS_6G_Radio
R2-2601093	Discussion on System information design principles for 6G Radio	Rakuten Mobile, Inc	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.2.3-p011`

### [6G/Rel-20 RAN2#132] `observation` 10.3.2.3 Initial and System Access and Others

```text
If SIB1 is transmitted on demand, a UE could use any of several mechanisms to determine what uplink configuration to use to request SIB1.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.3-o001`

### [6G/Rel-20 RAN2#132] `observation` 10.3.2.3 Initial and System Access and Others

```text
RMSI (i.e., SIB1) in NR has expanded significantly with network evolution, leading to information overload. The current structure of RMSI results in suboptimal energy efficiency.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.3-o002`

### [6G/Rel-20 RAN2#132] `observation` 10.3.2.3 Initial and System Access and Others

```text
On-demand OSI and area specific SI are features in initial release of 5G, but not successfully commercialized, the pain points include:
deploying on-demand SI without deploying area specific SI will significantly reduce the benefits of on-demand SI due to frequent SI requests from UEs;
for area specific SI:
complexity for the network to determine area configurations through system information comparison among multiple gNBs and coordinate any change of SIBs to ensure that area specific SIBs in the same SI area are the same;
SIB1 cannot be area specific even if most of the content in SIB1 is the same, the UE power consumption for SIB1 is still there.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.3-o003`

### [6G/Rel-20 RAN2#132] `observation` 10.3.2.3 Initial and System Access and Others

```text
RAN2 should carefully study if it is possible to have system information (or part of SIB) being common among multiple cells
R2-2508947	Discussion on Initial and System Access in 6G	Fujitsu	discussion	Rel-20
Proposal#2: SIB1 in 6G can be specified as either cell-specific or area-specific depending on operator deployment scenario. RAN2 to further study what contents of SIB1 can be area-specific.
(Not treated) Paging
R2-2508942	Discussion on 6G Initial Access	Qualcomm Incorporated	discussion
Proposal 6	RAN2 assumes LP-WUS triggered paging monitoring will be supported from Day-1. RAN2 considers the following potential directions to simplify paging procedure
o	Direction 1: Strive to achieve an upper layer common procedure and common set of parameters if both PEI and LP-WUS paging monitoring are supported.
o	Direction 2: Study the case that only one paging monitoring mechanism (PEI or LP-WUS) is used in one cell or one area if UE and network support both, i.e. UE does not need to switch between LP-WUS and PEI monitoring in a cell.
R2-2508501	Discussion on Initial and System Access in 6GR	China Telecom	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.3-o004`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.3 Initial and System Access and Others

```text
Both always-on broadcasting and OD-OSI/SIB1 mechanism specified in NR should be inherited in 6GR. And extend NR OD-SIB1 with UE request mechanism to cover: 1) standalone OD-SIB1 (e.g. the UE can obtain OD-SIB1 request configuration from SSB of the OD-SIB1 cell); 2) cell A-assisted OD-SSB&OD-SIB1 (i.e. cell A provides the OD-SSB&OD-SIB1 request configuration of the NES cell).
-	Huawei asks how can RAN2 start discussing this without RAN1.  Apple agrees.
-	Ericsson asks if we need case2 if we have case1.
-	ZTE asks case 2 is for idle and inactive and is it UE triggered.
-	Nokia first we have to determine whether we have on demand SIB1, then discuss standalone.   RAN1 has to check if ondemand standalone SIB1 is feasible. Fraunhaufer explains that RAN1 studied the standalone case and it was feasible.   Apple thinks there was no conclusion and it still needs to be studied in 6G as initial access will be different in 6G.
-	Lenovo thinks that from Rel-19 the gains are very clear for on demand SIB1.
-	Xiaomi thinks that if we support on demand SIB1 we should support areas specific SIB1.
Noted
Discussion on area specific SI
-	Nokia thinks that we need to carefully study if there are information that can be common.    Qualcomm thinks that we should first see if we will split the SIB or not and understand what can be area based.
-	Apple supports area based information concept as it has benefits from the UE side.   OSI has benefits for network so we should also consider UE.   Lenovo thinks it has benefits, so it should be supported, but it appears that operators are not using currently.
-	Lenovo thinks that some parts of the information can be area specific.
-	Oppo thinks we should support it.
-	CMCC explains that OSI and area specific SI is very important and we hope that these features are mandatory in UEs from day.  Mediatek thinks that this has to be two ways and things are implementable and attractive for both sides.
Agreements on system information
Assume on demand SI is supported and study further.   Study further on demand SIB1 from RAN2 perspective.
Assume area specific SI is supported.  Further study what information can be common.   FFS area specific SIB1
R2-2508346	System information and access for 6G radio	MediaTek Inc.	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.3-p001`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.3 Initial and System Access and Others

```text
Study options for requesting SIB1 on demand, including how a newly-arrived UE in a cell can obtain a configuration for requesting SIB1, e.g., via a fixed uplink configuration, an indexed uplink configuration in PHY/MIB, or an explicit uplink configuration signalled in the MIB or in other SI.
Noted
SIB Scheduling
R2-2508619	Discussion on cell management and system access	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
Observation 2-1:	The current SI scheduling mechanism restricts the network's ability to enter sleep mode for energy saving.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.3-p002`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.3 Initial and System Access and Others

```text
In order to reduce the number of SI windows and thereby decrease the duration of SI transmission, RAN2 should study the mechanisms of mapping SIBs with different periodicities into one SI window.
-	Huawei explains that today we cannot schedule in the same window and we need more flexibility.
-	Transsion thinks that this may increase the TB size and there is a max size.   Huawei thinks that we can extend this in 6G and that’s why we are having this discussion.
-	Samsung is fine to study this but this may also have impact to RAN1.    Qualcomm thinks that this came up multiple times in NR and we should take another look.   Vivo and Mediatek are a concerned about the combining.
-	ZTE is good with the concept of bundling them together but we should combine this discussion with CELL DTX/DRX.
-	Nokia thinks that this is a good principle and finding a way to concatenate the transmissions in one period and how it is done it can be studied further.   We should be able to transmit the information distributed to account for different load information.
Noted
R2-2508579	Procedures for 6G Access and Spectrum Aggregation	Ericsson	discussion	Rel-20	FS_6G_Radio
Proposal 2	6GR should support that all System Information messages are broadcasted together with other common control transmissions/receptions within short time-periods that are clustered with the SSB transmissions.
Noted
Discussion
-	Samsung is fine to study this but this may also have impact to RAN1.    Qualcomm thinks that this came up multiple times in NR and we should take another look.   Vivo and Mediatek are a concerned about the combining.
-	ZTE is good with the concept of bundling them together but we should combine this discussion with CELL DTX/DRX.
-	Nokia thinks that this is a good principle and finding a way to concatenate the transmissions in one period and how it is done it can be studied further.   We should be able to transmit the information distributed to account for different load information.  Ericsson thinks we should study different methods to achieve this including lengths etc.
-	Apple is fine to study this but it has RAN1 impact as well and wonders if we also have to support dynamic SI windows.   Ericsson thinks we also need to discuss whether we have SI windows.
-	Docomo thinks that it is very important to align the SIs/SIB1 with the other clustered signals to save energy.
-	Xiaomi asks if we assume the clustering is always there and if we need two mechanisms.   Huawei thinks that this can be part of CELL_DTX mechanism for example, so we might have two, one for energy saving and normal operation.
-	Interdigital thinks that we should aim to have a solution that applies to both network energy saving and normal operation
-	Oppo thinks that bundling adds complexity from the UE perspective.  Mediatek echos Oppo’s concerns.
Study SI scheduling mechanism to enable more flexible scheduling and clustering/bundling of transmission(s) with other common signalling.  Study should also take into account UE and NW complexity.   Aim to have one mechanism if possible.
SIB1 Content
R2-2508081	On system information, paging, initial access and spectrum aggregation related aspects	Xiaomi	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.3-p003`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.3 Initial and System Access and Others

```text
6G SIB1 should include at least the following essential common information:
	Information used by the UE for cell camping (e.g. PLMN/TA info, Cell barring info, cell selection info, etc. as in 5G NR);
	Common scheduling/resource configuration information for other SI acquisition and paging monitoring (i.e. SI schedule info, broadcast channel, paging channel related info, validity of SIB, etc. as in 5G NR).
	RACH configuration for SI request (which may be included in SI scheduling info), if OD-SI is supported.
-	ZTE asks what about initial access.   Xiaomi thinks we can further study as not all UEs need to do initial access, only when service starts, so we can consider putting it in another SI.
-	Ericsson asks what is excluded, is it mainly access control information.  Xiaomi thinks that this is related to initial access and can go with RACH config.
Noted
R2-2508068	Considerations on Spectrum Aggregation, Initial and System Access	CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.3-p004`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.3 Initial and System Access and Others

```text
In order to further reduce energy consumption and the complexity for both network and UE, RAN2 study to restructure RMSI in 6GR, e.g., RMSI in NR (SIB1) is restructured into sub-RMSI1 (e.g, information for camping) and sub-RMSI2 (e.g, information for access).
-	Nokia asks if there is any UE power savings.    CATT thinks there is power saving as the UE won’t have to read the second SIB if it doesn’t have to.
-	Transsion thinks that we had it split in LTE and that comes at latency cost.  Xiaomi agrees but it came at a cost of a very big SIB.
Noted
R2-2508147	Initial and System Access for 6G	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.3-p005`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.3 Initial and System Access and Others

```text
Study a scalable size of modular SIB1 construction/transmission for 6GR
	SIB1 consists of multiple SIB1 modules i.e. different SIB1 information groups (e.g. cell access info, SI scheduling info, common channel configurations for different features or UE types, UE timer/constants and UAC info)
	SIB1 scheduling /transmission and SIB1 update/maintenance can be designed based on per-SIB1 module.
-	Samsung asks how is this different from splitting the SIBs, it is same.
Noted
R2-2508746	Observations for initial and system access	Lenovo, Aumovio	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.3-p006`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.3 Initial and System Access and Others

```text
A study for SIB1 splitting should be justified with evaluation assuming SIB1 on-demand provisioning and keeping in mind plausible PBCH load restrictions for intended cell sizes.
Noted
Discussion
-	ZTE would not to introduce any further access delay for splitting.   Also it is not clear why we are splitting as we don’t have the actual size.
-	Huawei thinks that SIB1 size depends on the configuration and in the cases where the size is acceptable (e.g. in first release of 6G) then we don’t need to split.   But if it is too big then we can consider splitting.   At the beginning we should avoid.
-	CMCC is supportive to split cell camping and initial access information.
-	Nokia thinks we first have to understand the benefits and impacts, we should also determine the target.
-	Ericsson sees the benefits of splitting as the SIB1 can become quite big.  And we should look at how to schedule them, for example in LTE we had to acquire SIB1 to acquire SIB2.
-	Qualcomm thinks that there are dependencies on other things SIB1 size, not sure about energy saving, area specific SIB1.
-	Mediatek thinks that we should ensure that the camping information is in SIB1 and we should only do this if there are benefits and make sure we are not creating access latency, causing battery consumption issues, etc.
-	Apple sees benefits for area specific information.  Vivo thinks that the minimum part of SIB1 should be the information that doesn’t change very frequently.
-	Fujitsu thinks that we need to wait for RAN1 size.  Interdigital sees benefits for splitting and even for device type.  Thinks like PLMN information etc can help if they are separate for cell reselection scenario.
Before discussing SIB1 splitting, understand SIB1 design, content and size.  Then we can revisit how and if splitting is needed taking into account benefits and UE and NW impacts, and taking access latency into account.
(Not treated ) SIB-Update
R2-2508346	System information and access for 6G radio	MediaTek Inc.	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.3-p007`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.3 Initial and System Access and Others

```text
Study (from RAN2 perspective) an increase in granularity for the SI change notification, with the objective of reducing wake-up events for UEs not interested in the SIB(s) that changed.
(Not treated) SIB Validity
R2-2508619	Discussion on cell management and system access	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.3-p008`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.3 Initial and System Access and Others

```text
Regarding on-demand SI and area-specific SI, RAN2 should:
conduct joint studies on on-demand SI and area-specific SI to maximize energy-saving gains for both the network and UEs;
simplify the deployment of SI areas, e.g., the area management in the network (identical SI identification and update synchronization) does not have to depend on inter-RAN node comparison/coordination.
R2-2508244	System Access and Carrier Aggregation in 6GR	Nokia, Nokia Shanghai Bell	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.3-p009`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.3 Initial and System Access and Others

```text
Support uneven distribution of PF/PO in 6G paging design.
Multicarrier for “IDLE”
R2-2508409	6G initial and system access	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.3-p010`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.3 Initial and System Access and Others

```text
A unified multi-cell/carrier coordinated initial and system access procedure should be supported for efficient utilization of network resources, e.g. spectrum, time and spatial domain resources, satellite orbits, to provide overall coverage, high throughput with reduced energy consumption at both network and UE side.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.3-p011`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.3 Initial and System Access and Others

```text
Multi-cell/carrier coordinated initial and system access need incorporation of the following functionalities.
UE camps in cell/carrier A (anchor cell/carrier) for system information reception, including the information for the initial access on cell/carrier B (assisting cell/carrier)
Whenever initial and system access is required, the UE determine the cell/carrier for initial and system access (e.g. preamble transmission) among all the anchor cell/carrier and assisting cells, and perform initial and system access on the cell/carrier selected.
The assisting cell/carrier can be either on TDD or FDD spectrum. For the case of FDD spectrum, the assisting cell/carrier may have both UL and DL spectrum or only have DL or UL spectrum.
The assisting cell/carrier can be either co-located or non-co-located with anchor cell/carrier. FFS whether non-co-located can be supported for the UL only assisting cell/carrier.
Whether the assisting spectrum resource should be “cell” or “carrier” is some kind of modeling issue, which can be discussed later when we have clear view on the whole function and framework.
-	Mediatek asks if we are assuming we have similar cells like in 5G and we have anchor and assistance nodes.   ZTE explains that we have two models, same concept as 5G and another one is that we have multiple cells as one cell.
Noted
R2-2508850	Initial and System Access for 6GR	Samsung	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.3-p012`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.3 Initial and System Access and Others

```text
For efficient usage of fragmented frequency spectrum, the single cell concept with fragmented carriers is supported. The N-carrier Single Cell (NSC) consists of DL/UL anchor carriers and one or more DL/UL non-anchor carrier(s). The initial access is performed on the anchor carrier of the NSC.
-	Huawei asks what is the purpose of the non-anchor carrier if initial access is done in anchor.   Samsung explains that this is similar to SUL.   Huawei thinks that if it is like SUL then initial access can be performed in non-anchor carrier.
-	Nokia asks how the UE is measuring this other carriers and what is the benefit for idle mode.
Noted
R2-2508244	System Access and Carrier Aggregation in 6GR	Nokia, Nokia Shanghai Bell	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.3-p013`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.3 Initial and System Access and Others

```text
RAN2 to study the need for multicarrier operation (carrier(s) for paging and/or random access) considering all device categories by e.g., taking into account latency and capacity requirements
Noted
Discussion
-	Nokia thinks we can study but we have quite a few things to take into account.   NEC thinks for Idle it should be second priority.
-	Qualcomm thinks it is too premature to make decisions but we can study with understanding that we have to coordinate with RAN1.
-	Interdigital thinks we should study it for IDLE and Inactive, for capacity purposes.   CMCC thinks it is beneficial for signaling.
-	LG we should consider the non-campable carrier and this depends on SSB signal existence.
-	Mediatek asks what is the purpose and we need to assess, as we have this for NBIoT and MTC, for high load scenario for devices that send small amount of data.  And we should re-asses the need for this.
-	CATT supports this to avoid fragmentation and to help the operators so they can refarm some of their spectrum.
Agreements on multicarrier
RAN2 to study the need for multicarrier operation in IDLE/INACTIVE (if supported) (carrier(s) for paging and/or system information and/or random access) by taking into account e.g. latency,  device categories/features, capacity, coverage requirements, UE power consumption/complexity, NW energy saving.  Close coordination with RAN1/RAN4 is required.
Discussion on modelling of cell is FFS and also depends on RAN1/RAN4 progress.   Discussions on this will not happen next meeting.
(Not treated) Multicarrier for CONNECTED
R2-2508672	Discussion on initial access and system information	NEC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.3-p014`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.3 Initial and System Access and Others

```text
RAN2 assume to support the CA as baseline for aggregating consecutive frequency resources of one band (as one cell) and another consecutive frequency resources of the other band (as the other cell) and study its improvements.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.3-p015`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.3 Initial and System Access and Others

```text
RAN2 assume to support the BWP as baseline at least for consecutive frequency resources within a cell and study its improvements.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.3-p016`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.3 Initial and System Access and Others

```text
RAN2 study potential usage of aggregation of multiple pieces of spectrums with coordinating with RAN1 and/or RAN4, where examples are:
	consider each part of the aggregated spectrums as a kind of BWP, and use single active BWP at a time,
	consider each part of the aggregated spectrums as a kind of BWP, and use more than one BWPs as BWP aggregation.
R2-2508409	6G initial and system access	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.3-p017`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.3 Initial and System Access and Others

```text
The spectrum aggregation for RRC connected in 6G shall consider capacity, coverage and robust enhancement, support both collocated and non-collocated deployment, Aim to weaken the distinction between PCell and SCell, Strive to achieve fast PCell change & recovery.
R2-2508452	Views on 6G Spectrum Aggregation	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.3-p018`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.3 Initial and System Access and Others

```text
RAN2 study on 6G CA should consider the following two directions:
-	Support more functions on SCell (e.g. RLM, RA-SR)
-	PCell failure recovery over SCell .
(Not treated) Access Control
R2-2508072	Discussion on initial and system access	Transsion Holdings	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.3-p019`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.3 Initial and System Access and Others

```text
The UAC, Cell status and cell reservations, RRC Reject based on MSG3 cause from 5G will be baseline for cell access control design in 6G.
R2-2508141	Discussion on 6GR Initial Access and Spectrum aggregation	OPPO	discussion	Rel-20	FS_6G_Radio
Proposal 7	For 6G access control, RAN2 study enhancement on access control based on finer granularity, by coordination with SA1/CT1.
R2-2508590	Discussion on Initial and System Access for 6GR	HONOR	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.3-p020`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.2.3 Initial and System Access and Others

```text
For 6G, RAN2 should aim to design a unified access control mechanism considering different service type (e.g., emergency call, MT, MO, or other 6G new services), and device type and NW/UE capability. Barring information could be carried in system information.
Not treated
R2-2508061	Discussion on 6G Radio Initial and System Access 	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
R2-2508147	Initial and System Access for 6G	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
R2-2508210	Considerations on initial and system access and others	SHARP Corporation	discussion
R2-2508451	Views on 6G Paging and System Information and Initial Access	Apple	discussion	Rel-20	FS_6G_Radio
R2-2508533	Views on 6G Initial Access	NTT DOCOMO, INC.	discussion
R2-2508546	Discussion on 6GR initial and system access aspects	Sony	discussion	Rel-20	FS_6G_Radio
R2-2508591	Discussion on Random Access for 6GR	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2508597	Discussion on System Information for 6GR	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2508632	Initial and system access	Ofinno	discussion	Rel-20
R2-2508673	Initial thoughts on aggregation of multiple pieces of spectrum	NEC	discussion	Rel-20	FS_6G_Radio
R2-2508683	Initial and System Access and Others for 6GR	InterDigital, Inc.	discussion	Rel-20
R2-2508821	Consideration of initial access aspects for 6GR 	Kyocera 	discussion	Rel-20
R2-2508827	Discussions on 6G initial and system access	Futurewei	discussion	Rel-20	FS_6G_Radio
R2-2508835	Discussion on 6G initial access and spectrum aggregation	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2508851	Discussion on initial and system access for 6GR	TCL	discussion
R2-2508930	Discussion on initial and system access and others of 6G	Spreadtrum, UNISOC	discussion	Rel-20
R2-2508964	Discussion on Spectrum aggregation for 6GR	TCL	discussion	Rel-20
R2-2508970	Discussion on Initial and system access	Google Korea LLC	discussion	FS_6G_Radio
R2-2508974	Considerations on Initial and System Access and Others	KDDI Corporation (TTC)	discussion
R2-2509008	Considerations for 6GR system access and carrier aggregation	Panasonic	discussion	Rel-20
R2-2509029	Initial and System Access and Others	CEWiT	discussion	Rel-20	FS_6G_Radio
R2-2509040	Discussion on 6G Initial and System Access	CSCN	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.2.3-p021`

