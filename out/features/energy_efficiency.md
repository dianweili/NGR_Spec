# 6GR 能效

**当前进展** · 阶段：—

_尚无综述_

## 6GR 演进

### [6G/Rel-20 RAN2#134] `observation` 9.3.3.3 Energy efficiency

```text
Static CDRX timer operations lead to unnecessary PDCCH monitoring at least in following cases:
	Case 1: Active inactivity timer when no data activity (e.g. blind UL scheduling before data arrival in UE).
	Case 2: Active inactivity timer when no subsequent transmission (e.g. measurements and CP signalling).
	Case 3: Active HARQ retransmission timer when retransmission is not valid (e.g. if PDCP discarding).
	Case 4: Not support multiple traffics/services and/or dynamic delay requirements during one connection.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.3-o001`

### [6G/Rel-20 RAN2#134] `observation` 9.3.3.3 Energy efficiency

```text
To enable CDRX timer adaptation in 6G, both NW-initiated solution and UE-initiated solution can be considered to adopt to the dynamics of DL and UL traffics.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.3-o002`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.3 Energy efficiency

```text
Design a single discontinuous monitoring framework for connected mode, including:
-	UE starts monitoring PDCCH for a configured timer duration upon receiving the DL WUS or upon the arrival of the periodic CDRX occasion;
-	The same actions for DL WUS and CDRX:
 UE stays awake for a certain time period when the UE is scheduled on PDCCH during the timer duration;
 UE starts monitoring potential retransmission scheduling when the UE is scheduled on PDCCH during the timer duration.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.3-p001`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.3 Energy efficiency

```text
A single timer, applicable to both DL WUS and CDRX, is defined to stay awake for a certain time period when the UE is scheduled on PDCCH.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.3-p002`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.3 Energy efficiency

```text
A timer (e.g., retransmission timer) for the purpose of monitoring retransmission scheduling is also applicable to both DL WUS and CDRX when the UE is scheduled on PDCCH.
-	Qualcomm ask if WUS and DRX can have different cycles.  CATT thinks it can be configurable.
-	NEC asks what is the WUS monitoring.
Noted
R2-2603435	Discussion on network and UE energy efficiency	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.3-p003`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.3 Energy efficiency

```text
For single UE discontinuous monitoring framework, RAN2 to study the following UE behaviour steps:
	C-DRX operation: UE starts Timer 1 (onDuration-like) for PDCCH monitoring according to Cycle 1 (C-DRX cycle). If the UE is scheduled on PDCCH, it (re)starts Timer 2 (InactivityTimer-like) for extended PDCCH monitoring;
	DL WUS operation with C-DRX: UE monitors DL WUS according to Cycle 2 (DL WUS Occasion cycle), if the detected DL WUS targets to itself, UE starts Timer 3 (after a time offset) for PDCCH monitoring. If the UE is scheduled on PDCCH, it (re)starts Timer 4 (InactivityTimer-like) for extended PDCCH monitoring.
Discussion
-	Nokia asks what is the motivation for different timers.    Huawei thinks that DL WUS has the benefit of being more energy efficient so we can benefit from it and have more frequent monitoring occasions.  Nokia thinks that we can consider the cycle to be different we can consider, but other timers we have to see why they would be different.
-	ZTE also doesn’t see a benefit for different onduration timers.   Huawei thinks main benefit is cycle anyways.    But if we have a short timer for the cycle then the on duration can be smaller so you don’t have to wake up too ofter.
-	Timer 1 and 3 can be the same if they are aligned.
Discussion on DRX and WUS cycle
-	Vivo thinks that main benefit from WUS comes from short cycle.   And all the timer behavior should be the same and we can align the behavior.
-	Offinno ask if we have different cycle, does that mean that we are doing 1 to N.
-	Qualcomm thinks that different cycles make no difference according to simulation results and in cell edge the coverage is worst.   Ericsson thinks that if you configure a short DRX cycle or a short WUS cycle, the WUS case should be more energy efficient.   Vivo thinks that if we monitor the RRM and L1 measurements then we would see the benefits.
-	CMCC thinks that we should design something that is aligned so the timers can be same and configurable.
-	ZTE thinks that the cycle is decided based on service requirements and we’d up configuring the same cycle.   The short DRX cycle is short enough.   Mediatek thinks they made a good point and we would need to understand why it is acceptable for WUS to have a different cycle than DRX as we are offering the same service.
-	Sony thinks that we can configure them separately and we need to the WUS indicating to monitor.
-	Panasonic thinks that there is a case where the WUS is telling the UE to not start the DRX timers and that benefit is useful.
-	Oppo thinks that we should one cycle for both as a baseline and for different cycles it is the same as WUS without DRX.
-	Samsung thinks that the two cycles shouldn’t be associated together
-	Lenovo and Panasonic thinks the cycles should be different.  LG thinks they should be aligned.
-	Nokia thinks we can at least agree that it can be the same and we can continue studying whether it can
-	Vivo thinks that we should consider two cycles one for PDCCH monitoring and one for measurements.   Qualcomm indicates that RAN4 is studying how to handle measurements so we shouldn’t have it bundled with measurement requirements.
-	Qualcomm explains that in 5G we have an indication by RRC whether the UE can wake up without indication or not.
Agreements for the study of C-DRX and WUS configured together
For the purpose of the discussion to find commonalities, we assume the following, but this doesn’t mean that WUS can be configured without DRX.  That will be studied separately.
For C-DRX we assume the following parametrs are needed (DRX cycle, Timer x( onDuration-like), and Timer y(inactivitytimer like))
For WUS we assume the following timer (WUS cycle, Timer x (PDCCH monitor timer), Timer y (inactivitytimer)
For the study of C-DRX and WUS configured - FFS UE behavior if WUS is not received and DRX is configured.  FFS if the cycles can same or different.  FFS if the timers x and y can be same or different.
R2-2603589	Further Views On 6GR Energy Efficiency	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.3-p004`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.3 Energy efficiency

```text
The single discontinuous monitoring framework is designed based on the C-DRX like mechanism, the DL-WUS is considered as an optional feature which shall work together with the C-DRX like mechanism.
R2-2602968	Discussion on 6G power efficiency	Xiaomi	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.3-p005`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.3 Energy efficiency

```text
For UEs that support DL-WUS, the network can configure DL-WUS with or without (or aligned/not aligned) C-DRX cycle for PDCCH monitoring.
C-DRX Enhancements and Adaptation
R2-2603711	6G CDRX timer adaptation	Apple, ZTE Corporation, Lenovo, NEC, Xiaomi, Qualcomm, Ofinno, InterDigital, OPPO	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.3-p006`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.3 Energy efficiency

```text
As a starting point, the UE C-DRX can be configured to periodically monitor PDCCH according to C-DRX onDuration timer, inactivity timer, HARQ RTT timer and HARQ retransmission timer.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.3-p007`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.3 Energy efficiency

```text
Conclude that a pain point of 5G C-DRX is unnecessary PDCCH monitoring due to static timer operation, i.e., CDRX timer values are fixed once configured, regardless of data scheduling activity, subsequent transmissions, retransmission validity, or the traffic type.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.3-p008`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.3 Energy efficiency

```text
Support dynamic adaptation of CDRX timer(s) in the 6G discontinuous PDCCH monitoring procedure with and without DL WUS. FFS which CDRX timer(s) can be adapted. FFS details of adaptation solution.
-	Huawei thinks that we should avoid solutions that increase the signaling from the network otherwise it will never be deployed.   Apple thinks that the network can indicate with DL WUS the timer.   Huawei would like to see something that targets group of UEs as well.
-	Nokia asks what is the problem we are trying to address.
-	Ericsson thinks it could be nice but not sure how much signaling from network
-	LG asks why we don’t talk about dynamic cycle
-	Mediatek would like to ensure that we don’t risk mis synchronization.
-	Offinno think that we can also think of dynamic switching of pre-configured parameters.
Noted
Study if and how to reduce unnecessary PDCCH monitoring, taking into account network complexity, signaling overhead, etc.
R2-2603846	Consideration on Energy efficiency for 6G	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.3-p009`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.3 Energy efficiency

```text
In 6G, RAN2 should consider configuring multiple DRX patterns to better accommodate multi-flow with various traffic characteristics for improved energy efficiency.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.3-p010`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.3 Energy efficiency

```text
RAN2 should consider mechanisms to enable fast DRX pattern switching in response to traffic pattern change and dynamic QoS requirements.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.3-p011`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.3 Energy efficiency

```text
RAN2 studies how to reduce unnecessary PDCCH monitoring on all serving cells during onDuration time.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.3-p012`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.3 Energy efficiency

```text
RAN2 consider to apply DRX configuration per DRX group or per serving cell.
R2-2603849	Energy Efficiency for 6G: Network and UE Perspectives	Ericsson	discussion	Rel-20	FS_6G_Radio
Proposal 2	For 6G C-DRX, study UE-specific monitoring configurations based on activity, triggering event, and service type, considering recent scheduling activity.
Proposal 3	Study connected mode DRX for 6G, including:
	Identify different PDCCH/WUS monitoring windows for different UE activities.
	A window can be configured with L1 and L2 PDCCH monitoring features.
	When the active window changes the L1 and L2 configuration that is used changes accordingly.
	The active window can change when:
O a timer expires
O a window is activated periodically
O there is an event e.g. UL or DL data arrives
O signalling is received, e.g. WUS detection
 Study the need for separate Inactivity Timers for UL and DL data for further UE power saving
 Study unified signalling to change the active window i.e. avoid separate L1 and L2 signalling to adapt PDCCH/WUS monitoring.
Network Energy Efficiency
Network Sleeping Opportunities
R2-2602968	Discussion on 6G power efficiency	Xiaomi	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.3-p013`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.3 Energy efficiency

```text
For idle/inactive state, use implicit mechanism, e.g. to rely on SI update or layer 1 signaling if network wants to change SSB/paging/SI/RACH configurations in the cell when entering/leaving the sleeping opportunities
Noted
R2-2603712	Views on 6G energy efficiency	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.3-p014`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.3 Energy efficiency

```text
Support 6G explicit NW TX/RX sleeping pattern at least for RRC_CONNECTED UEs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.3-p015`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.3 Energy efficiency

```text
On signaling of 6G explicit NW TX/RX sleeping pattern, support both RRC configuration and UE group common lower layer indication for its dynamic activation / deactivation.
Noted
Discussion on connected
-	Ericsson thinks that if we align with C-DRX there is no reason for masking any further.  Also the network would never increase signaling for no reason.   ZTE thinks that C-DRX is only aligned for CELL DTX but not for cell DRX.  Also whenever we configure the UE with power saving we would need to provide a lot of PHY configurations so there is a lot overhead.    Fraunhoufer also explains that there would be a lot of things that need to be configured.  Docomo agrees with Ericsson.
-	Xiaomi explains that C-DRX cannot control everything from DTX like SSB monitoring.
-	Offinno asks what is the range of turning off the cell, is it the SSB periodicity or would the cells be off more than that.    Ericsson thinks that SSB periodicity will define the sleeping period is the thinking for now for PCell.   Can’t be further than that as the network will have to transmit.   Nokia agrees we can’t sleep more than common signals that need to be transmitted.
-	Huawei thinks it is a bit hard to determine whether we need it or now.
-	Nokia thinks that in connected mode DRX is variable and they can be triggered at any time so there is no way to control the sleeping.  Having a pattern would be helpful.
For idle the aim is to have an implicit network sleeping opportunity mechanism (if possible)
[POST134][013][6G] NW Energy saving (CATT)
Intended outcome:
For connected mode:
Which signals are muted during NW sleep and when is the NW expected to sleep
Discuss UE behavior during the nw sleep for connected mode and expected NW behavior (including measurements and data transmission)
Understand what UE behaviour would benefit from explicit signaling
Understand how implicit works and what signlaing is used to understand the network signaling overhead
Deadline:  Long
UE/NW behavior during sleep
R2-2603031	Discussion on 6G Energy Efficiency	CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.3-p016`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.3 Energy efficiency

```text
If the network of 6G is sleep in DL:
connected UEs at least don’t need to monitor DL semi-persistent scheduling, nor monitor PDCCH for new transmissions.
non-connected UEs:
Option 1: do not need to monitor common reference signal, paging and system information.
Option 2: monitor with sparse period for common RS, paging and system information.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.3-p017`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.3 Energy efficiency

```text
If 6G network is sleep in UL, RAN2 consider the following options for UEs in all states:
Option 1: No transmission of any data or signal.
Option 2: No transmission of any data or signal except initiating Random Access procedure.
UE and NW alignment
R2-2603554	Discussion on energy efficiency for network and UE	Lenovo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.3-p018`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.3 Energy efficiency

```text
To achieve energy efficiency, also to align NES and UE power saving, the resource management may be considered per traffic and UE basis
R2-2603423	6G Energy Efficiency	InterDigital, Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.3-p019`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.3 Energy efficiency

```text
Support adaptation of UE power saving configuration based on NW energy saving operation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.3-p020`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.3 Energy efficiency

```text
UE adapts C-DRX cycle configuration to align with the active cell DTX/DRX configuration.
R2-2602968	Discussion on 6G power efficiency	Xiaomi	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.3-p021`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.3 Energy efficiency

```text
For connected state, the legacy time-domain periodic/fixed cell DTX/DRX pattern is taken as baseline. RAN2 to further study the need of dynamic control of cell DTX/DRX based on network indications to balance between preserving network energy saving and providing better performance for delay-sensitive traffic.
R2-2602957	Discussion on 6GR UE PowSav and NES	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.3-p022`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.3 Energy efficiency

```text
Study DL WUS to trigger on-demand PDCCH monitoring during the cell DTX non-active period in RRC_CONNECTED mode.
R2-2602992	Discussion on 6G Energy Efficiency	China Telecom	discussion
R2-2603163	Implicit vs Explicit Cell DTX/DRX	Fraunhofer IIS, Fraunhofer HHI, CEWiT	discussion	Rel-20	FS_6G_Radio
R2-2603189	C-DRX, DL-WUS and single discontinuous monitoring framework	Nordic Semiconductor ASA	discussion
R2-2603197	Discussion on 6G energy efficiency 	NEC 	discussion	Rel-20	FS_6G_Radio
R2-2603310	Energy efficiency in 6G	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2603323	Discussion on energy efficiency	Sharp	discussion	Rel-20
R2-2603508	Discussion on energy efficiency in 6G	OPPO	discussion	Rel-20	FS_6G_Radio
R2-2604179	Discussion on energy efficiency for network and UE	Lenovo	discussion	Rel-20
R2-2603626	Discussions on energy efficiency in connected and idle mode.	Sony	discussion	Rel-20	FS_6G_Radio
R2-2603671	Discussion on 6G UE Energy Efficiency	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
R2-2603755	On the modelling of single DRX framework	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
R2-2603779	Latency for some critical applications	TOYOTA ITC, Xiaomi, BMW, Volkswagen AG, Hyundai Motor Company, AUMOVIO, BOSCH, DENSO CORPORATION, BYD	discussion
R2-2603792	Discussions on 6G Energy Efficiency	Futurewei	discussion	Rel-20	FS_6G_Radio
R2-2603818	Discussion on 6G energy and power saving features	Qualcomm Inc	discussion
R2-2603841	Discussions on Single discontinuous monitoring framework	ETRI	discussion
R2-2603869	Discussion on 6G energy efficiency	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2603882	Views on 6G Energy Efficiency	NTT DOCOMO	discussion
R2-2603898	Discussion on energy saving of 6GR	Spreadtrum, UNISOC	discussion	Rel-20
R2-2603922	Considerations for Energy Saving in 6GR 	Samsung	discussion	Rel-20
R2-2603983	Discussion on Energy Efficiency	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2604005	Discussion on energy efficiency	ASUSTeK	discussion	Rel-20
R2-2604008	Discussion on Energy Efficiency aspects of 6GR	Rakuten Symphony	discussion	Rel-20
R2-2604015	Discussion on network and UE energy efficiency	1FINITY Inc.	discussion	Rel-20	FS_6G_Radio
R2-2604018	 Discussion on 6G Energy Efficiency	Transsion Holdings	discussion
R2-2604071	Network and UE Energy Efficiency	Nokia	discussion	Rel-20	FS_6G_Radio
R2-2604082	Discussion on Explicit Cell DTX/DRX for Energy efficiency in 6GR	CEWiT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.3-p023`

### [6G/Rel-20 RAN2#133bis] `agreement` 9.3.3.3 Energy efficiency

```text
1	For next meeting using these baseline steps, further study the points of commonalities and how to enable these functions with the aim to define a single discontinuous monitoring framework.
2	For next meeting companies should focus on modelling of how this work.
3	FFS on details of the two schemes, for example, timers of PDCCH monitoring, periodicity of monitoring, whether it is a single one, different one, aligned not alignedetc.
4	Do NOT use option 1-1 and 1-2 terminology.
Not treated
DL WUS without C-DRX
R2-2601939	Discussion on energy efficiency	ASUSTeK	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.3-a001`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.3.3 Energy efficiency

```text
DLWUS Options 1-2 can configure its periodicity independently of C-DRX and achieve periodic PDCCH monitoring functionality similar to C-DRX.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.3-o001`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.3.3 Energy efficiency

```text
DLWUS option 1-1 can be used to indicate whether needed to wake up for the next CDRX period and has better power saving gain than DCP.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.3-o002`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.3 Energy efficiency

```text
C-DRX without DL-WUS is adopted as baseline UE power saving solution.
Noted
Discussion
-	Mediatek would like to avoid doing the same as 5G, doing things piecemeal approach.
-	Apple, NEC, Interdigital, Xiaomi, Lenovo, ZTE, Qualcomm supports the proposal.   NEC thinks that other approaches requires more signaling.   Interdigital thinks we can design them together but we should at least understand that C-DRX can be configured without DL WUS.   Xioami thinks we can avoid too many solutions when we talk about C-DRX and DL-WUS together.
-	CATT is fine to take this as a reference.
-	Huawei doesn’t like this proposal as we should first discuss what does it mean to have C-DRX without DL WUS.   Vivo also doesn’t think we should make this decision.
-	Nokia and Docomo think C-DRX is the main mechanism in 5G and may be baseline.  Qualcomm also thinks that this is a proven mechanism so we should take it as a baseline.   Ericsson is already comfortable to consider C-DRX like mechanism as a baseline and see how it would look like.
The network can configure C-DRX-like mechanism without DL-WUS.   RAN2 will focus discussion to understand how it looks like in 6G.
DL WUS together with C-DRX
R2-2602078	Discussion on Energy Efficiency	HONOR	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.3-p001`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.3 Energy efficiency

```text
For DL WUS together with C-DRX, support to study both option 1-1 and option 1-2.
Noted
R2-2602472	Views on 6G Energy Efficiency	NTT DOCOMO	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.3-p002`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.3 Energy efficiency

```text
RAN2 to study C-DRX with dynamic wake-up mechanism. For the dynamic wake-up mechanism, whether to introduce DCP or DL-WUS should be justified after the DL-WUS design details are determined and evaluated within RAN1 discussions.
-	Ericsson asks why we are considering DCP.   Docomo explains that it is up to RAN1.
Noted
R2-2602495	Discussion on 6G Energy Efficiency	Transsion Holdings	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.3-p003`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.3 Energy efficiency

```text
Study and define a single discontinuous monitoring framework for 6G that clearly defines the interaction between a single, unified DL WUS and C-DRX, covering the three baseline modes of operation.
-	ZTE ask how we can incorporate all these three cases.
Noted
Discussion
-	Apple supports to start looking at option 1-1 and 1-2 and not wait for RAN1 to finish all the details.
-	Huawei thinks it is very important to have a single monitoring framework and this can work with all three directions, depending on what is configured.   We can take option 1-2 to work with C-DRX.   From UE perspective they both work the same.
-	ZTE thinks that we have two options because we had different coverage, but in 6G study the DL WUS will have the same coverage so option 1-2 wouldn’t get the benefit as in 5G.   So 1-1 can be the baseline.  LG thinks that option 1-2 is beneficial because it can wake up timely.
-	Interdigital thinks that 1-1 is WUS occasion is aligned with CDRX and 1-2 is WUS occasion is not aligned with on duration.   Vivo doesn’t think the options were related to coverage time.
-	Panasonic thinks it should be similar and we just need to discuss to what is the timer anchored to.
-	Lenovo also thinks that 1-1 can be the baseline.
-	Oppo also thinks we should start with WUS occasion is aligned with CDRX occasion.  If it is not aligned it would have more impacts to RAN1.
-	Ericsson thinks we shouldn’t mention 1-1 and 1-2 and we should just have the single PDCCH monitoring framework and consider both L1 and L2 monitoring aspects.   Today we have many independent operations L1 and L2 and we have to configure.
-	Vivo thinks that as a babystep we can say that the DL WUS can be monitored during inactive time.
-	Qualcomm thinks we can monitoring during on duration both, and we should wait for RAN1 misdetection rates we can discuss the mechanisms related to that.
-	NEC thinks we can study both but we should aim for a unified solution.
-	Xiaomi thinks that both options should be studied as 1-1 is for periodic and 1-2 for bursty traffic.
-	Samsung thinks that option 1-2 is DL WUS without CDRX.
-	Ofino agrees that we shouldn’t talk about 1-1 and 1-2 but talk about the requirements.
-	Interdigital thikns we can add to the previous agreement that it can be aligned or not aligned with onduration.
| Agreements on Baseline UE behaviour steps UE periodically monitors a signal (DL WUS)/channel (PDCCH) for connected mode For DL WUS - If DL WUS is received for that UE, the UE starts monitoring PDCCH for a timer duration - If DL WUS is not received or received but not for that UE after a DL WUS monitoring period the UE may go back to sleep (this step may change based on RAN1) For CDRX - UE monitors PDCCH for a timer duration. If it doesn’t receive anything after a monitoring period it goes back to sleep. If the UE is scheduled on PDCCH during the timer duration it stays awake for certain time period. Same for both cases above once UE starts PDCCH monitoring for a timer duration. Actions after are the same. |
| --- |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.3-p004`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.3 Energy efficiency

```text
For DL WUS without C-DRX, the operation could be similar to Option 1-2 of LP-WUS operation while removing C-DRX cycle.
R2-2601747	Discussion on 6G energy efficiency 	NEC	discussion	Rel-20	FS_6G_Radio
Proposal-3: for the solution of DL-WUS without C-DRX, DL-WUS is monitored based on its own periodicity and DL-WUS can indicate to start an active timer during which the UE monitors PDCCH.
R2-2602424	Discussion on 6G energy efficiency	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.3-p005`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.3 Energy efficiency

```text
Whether to support DL-WUS without C-DRX should consider the specification effort in different working groups and RAN1 progress on signalling design.
R2-2602217	Views on 6G energy efficiency	Apple	discussion	Rel-20	FS_6G_Radio	Late
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.3-p006`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.3 Energy efficiency

```text
RAN2 first study “C-DRX without DL WUS” and “DL WUS together with C-DRX”, and postpone the study of “DL WUS without C-DRX” unless triggered by RAN1. Rel-19 LP-WUS option 1-2 like option should be studied under the direction of “DL WUS together with C-DRX”.
NW and UE sleeping opportunities
R2-2601885	Considerations for Energy Saving in 6GR	Samsung	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.3-p007`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.3 Energy efficiency

```text
The 6GR Cell DTX/DRX mechanism will include the concept of Active Duration, defining the period during which the UE receives downlink signals, scheduled uplink resources, and transmits uplink signals.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.3-p008`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.3 Energy efficiency

```text
The 6GR Cell DTX/DRX mechanism will operate on a cycle-based framework, alternating between Active Duration and non-Active Duration, similar to the NR.
Noted
R2-2601513	Discussion on 6G energy efficiency	Xiaomi	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.3-p009`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.3 Energy efficiency

```text
To enable network sleeping opportunities and avoid the mismatch between the UE and the network, the UE needs to know following information:
For RRC_CONNECTED: the time-domain cell DTX/DRX pattern (e.g., periodic/fixed parameters) and potentially more dynamic triggerings of cell DTX/DRX, which are used for RRC_CONNECTED UE to determine the available UL/DL signals/resources;
Noted
R2-2602394	Energy Efficiency for 6G: Network and UE Perspectives	Ericsson	discussion	Rel-20	FS_6G_Radio
Proposal 3 RAN2 will aim to specify all aNB transmissions/receptions configurations with sufficient flexibility that enable NW energy savings, i.e., no need for Cell DTX/DRX feature in 6G.
Noted
Discussion
-	Nokia asks what flexibility is missing in 5G.   Ericsson explains that in 5G we only had it in connected.
-	CATT thinks Ericsson’s proposal is only for idle.  Ericsson explains that it is for all modes.
-	Huawei thinks that we have two ways, implicit and explicit patterns.  Not sure which one is better, but even if we go with explicit more configurability/flexibility is needed, so we should discuss what we want to achieve.   Docomo agrees with Ericsson.  From operator perspective we want to avoid duplication.
-	Interdigital thinks that we need to know at least when it is allowed to transmit and in connected mode this is not clear how it can without a pattern.   This can be aligned with idle mode.   Apple and Qualcomm agrees that the UE needs to be aware of what is happening and pattern and it is also important to achieve power savings for both UE and NW.   Ericsson clarifies that the intention is not to let the UE know, the network will provide the configuration (like RACH resources, etc).    Interdigital asks if the network needs to reconfigure all resources, like RACH, CSI config, etc.  Apple doesn’t think that configuration is the same as network sleeping or not.
-	Fraunhaufer agrees with Ericsson.
-	Qualcomm asks if Ericsson wants to have further granularity
-	Xiaomi also thinks that we should keep the static pattern.
-	Oppo thinks that for idle mode the UE doesn’t need to be explicit but for idle it is important.
-	Vivo agrees with Ericsson for idle mode, but for connected the DTX/DRX achieves a good balance for UE and NW power saving.
-	Ofinno asks how would it work for connected UEs as each UE has it’s own configuration and points out that when NES is activated the sleeping time should be higher than normal CDRX.
-	Ericsson explains for DL we just use CDRX, and for UL we can provide an SR configuration of when the UE can transmit in uplink.
-	ZTE thinks that this comes at a cost.  Everytime it switches it has to provide again the configuration and that is high signaling cost as there would be a ot of configuration that would need to be provided to the UE.
-	Nokia thinks it makes sense for idle mode.  For connected mode maybe there are a few things to consider.  Huawei agrees and idle and connected should be treated differently.
-	Mediatek that it is important for the UE to receive some signals for measurements like SSB measurements.   CATT agrees and thinks we should discussion UE behavior.
For next meeting, look at both implicit and explicit mechanisms.   For implicit mechanism, proponents should explain how it would work, which configuration would need to be changed for every transition, and how to ensure that the UE can benefit as well.   For explicit mechanism, further details on how it would work and what level of flexibility to have.   Also discuss UE behavior during the sleeping opportunities for both mechanisms.
Not treated
Joint NW NES and UE power saving
R2-2601710	Discussion on network and UE energy efficiency	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.3-p010`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.3 Energy efficiency

```text
RAN2 to study: Cell DTX design aligned with UE discontinuous monitoring framework operating with DL WUS;
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.3-p011`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.3 Energy efficiency

```text
RAN2 to study clustered UL/DL data transmission for joint network and UE energy saving.
R2-2602394	Energy Efficiency for 6G: Network and UE Perspectives	Ericsson	discussion	Rel-20	FS_6G_Radio
Proposal 5  RAN2 should strive for a design that enables the NW to flexibly configure aligned DL and UL transmission occasions in connected mode, both per UE and across UEs or groups of UEs within a cell.
R2-2601989	Discussion on network and UE energy efficiency	1Finity	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.3-p012`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.3 Energy efficiency

```text
RAN2 to study efficient mechanisms to align between the UE DRX and sleeping opportunities in NW (e.g., Cell DTX/DRX).
Not treated
DRX configuration adaptation (if time allows)
R2-2602406	Consideration on Energy efficiency for 6G	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.3-p013`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.3 Energy efficiency

```text
In 6G, RAN2 should consider multiple DRX configurations (i.e., more than two DRX configurations) to better accommodate multi-flow with various traffic characteristics for improved energy efficiency.
R2-2602477	Discussion on energy efficiency in 6G	OPPO	discussion	Rel-20	FS_6G_Radio
Proposal 3	Support a single DRX configuration in 6G without introducing multiple DRX configurations to accommodate different traffic patterns.
R2-2601747	Discussion on 6G energy efficiency 	NEC	discussion	Rel-20	FS_6G_Radio
Proposal-1: for the solution of C-DRX without DL-WUS, take 5G C-DRX as baseline, further study adaptive C-DRX mechanism in 6G, e.g., dynamical change on C-DRX pattern (e.g., cycle, active timer, offset, etc.).
R2-2601442	Discussion on 6G Energy Efficiency	CATT	discussion	Rel-20
R2-2601456	Discussion on 6GR UE PowSav and NES	vivo	discussion	Rel-20
R2-2601488	Discussion on 6G energy efficiency and discontinuous monitoring framework	China Telecom	discussion
R2-2601671	Network and UE energy efficiency	Nokia	discussion	Rel-20	FS_6G_Radio
R2-2601731	C-DRX, DL-WUS and single discontinuous monitoring framework	Nordic Semiconductor ASA	discussion	Rel-20
R2-2601866	Energy efficiency in 6G	Ofinno	discussion
R2-2601945	Discussion on energy efficiency for 6GR	TCL	discussion
R2-2601998	Energy efficiency for 6GR	InterDigital	discussion	Rel-20	FS_6G_Radio
R2-2602000	Discussion on energy efficiency	Sharp	discussion	Rel-20
R2-2602107	Discussion on energy saving of 6GR	Spreadtrum, UNISOC	discussion	Rel-20
R2-2602135	Discussion on energy efficiency for network and UE	Lenovo	discussion	Rel-20
R2-2602167	Discussions on energy efficiency in idle mode.	Sony	discussion	Rel-20	FS_6G_Radio
R2-2602189	Views On 6GR Energy Efficiency	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
R2-2602306	On the time domain framework for power savings	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
R2-2602314	Discussion on 6G energy and power saving features	Qualcomm Inc	discussion
R2-2602346	Latency for some critical applications	TOYOTA ITC, BMW, AUMOVIO	discussion	FS_6G_Radio
=> Revised in R2-2602515
R2-2602515	Latency for some critical applications	TOYOTA ITC, BMW, AUMOVIO, DENSO CORPORATION, BOSCH, Hyundai Motor Company	discussion	FS_6G_Radio	R2-2602346
R2-2602367	Discussion on DL-WUS and UE DRX	ETRI	discussion
R2-2602400	6G Radio: Energy efficiency by default	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
R2-2602406	Consideration on Energy efficiency for 6G	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
R2-2602449	Discussion on DL-WUS operation	WILUS Inc.	discussion	Rel-20	FS_6G_Radio
R2-2602477	Discussion on energy efficiency in 6G	OPPO	discussion	Rel-20	FS_6G_Radio
R2-2602513	Discussions on 6G Energy Efficiency 	Futurewei	discussion	Rel-20	FS_6G_Radio
R2-2602567	Discussion on Energy efficiency in 6GR	CEWiT	discussion	Rel-20	FS_6G_Radio	Late
R2-2602586	Discussion on Energy Efficiency aspects of 6GR	Rakuten Symphony	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.3-p014`

### [6G/Rel-20 RAN2#133] `agreement` 10.3.3.3 Energy efficiency

```text
1	Single DRX configuration active at a time.   Discuss at later time whether there is a need to have multiple configuration and what is the use case.
2	Pain point in 5G - too many options DRX, LP-WUS option 1-1, option 1-2, DCP, and different features designed in different releases
3	Study the following:  “C-DRX without DL WUS”, “DL WUS together with C-DRX” and “DL WUS without C-DRX” assuming RAN1 will design a DL WUS.
4	Aim to define a single discontinuous monitoring framework.  This includes UE periodical monitoring of wake up signalling and follow up actions of PDCCH monitoring upon the wake up
Interaction with NW sleeping opportunities/ cell DTX/DRX
R2-2600650	Network and UE energy efficiency in 6G Nokia	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.3-a001`

### [6G/Rel-20 RAN2#133] `agreement` 10.3.3.3 Energy efficiency

```text
Study what the UE would need to know to be able to operate in all RRC states if the network is going to sleep.
As a starting point, for UL at least the UE need to know the UL resources and when it can send things in the UL
As a starting point for DL, the UE needs to know when the NW may send something in the DL (e.g. resources, reference signals for measurements, etc).
Not treated
Dynamic NW sleeping opportunities/ cell DTX/DRX [15 mins]
R2-2600405	Discussion on network and UE energy efficiency	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.3-a002`

### [6G/Rel-20 RAN2#133] `observation` 10.3.3.3 Energy efficiency

```text
6G is expected to introduce a broader range of traffic types, e.g., metaverse and multimodal interactive services with the combination of video, audio, sensor data and tactile feedback, each with distinct latency, periodicity, data volume, and burstiness characteristics, thereby requiring differentiated or service aware CDRX configuration with multiple parameter values for multiple traffic patterns.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.3-o001`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.3 Energy efficiency

```text
In 6G, RAN2 should consider to configure and enable multiple DRX configuration (i.e. more than two DRX configuration).
-	Apple asks if the intention is that a single DRX is active a time.   LG thinks that we should have multiple running.
[2 mins]
Noted
R2-2600931	Discussion on 6G energy and power saving features	Qualcomm Incorporated	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.3-p001`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.3 Energy efficiency

```text
Support a single DRX configuration with multiple parameter values for a UE to accommodate different traffic patterns of a service.
[2 mins]
Noted
Discussion
-	Apple agrees with the intention but the simultaneous DRX is not necessary.
-	Xiaomi thinks that multiple configuration active at the same time is complex and also not good for power saving.
-	Huawei doesn’t thinks we need to complicate the DRX with multiple configuration and for other use cases we will design other things that may address the different range of traffic types.   Vivo agrees with Huawei and don’t think that there are any use cases.
-	CATT asks how you control the different parameters.   Qualcomm explains that it can be linked to the traffic flow and depending on the traffic we’d adapt the timers.
-	Mediatek would like to keep it simple and then we should take baby steps on what do we need to change and how often.
-	Nokia thinks that we have to remind everyone that DRX is deployed and working very well and we haven’t seen any real problems.
-	ZTE indicates that we have two DRX groups for FR1 and FR2
DL-WUS - C-DRX interaction
R2-2600751	Discussion on energy efficiency for network and UE	Lenovo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.3-p002`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.3 Energy efficiency

```text
RAN2 to study following DL-WUS schemes for UEs in RRC_CONNECTED state in 6GR:
•     Scheme1: DL-WUS to work together with c-DRX like mechanism, UE performs PDCCH monitoring within the c-DRX on-duration timer, when DL-WUS is detected before the timer.
•     Scheme2: DL-WUS to decouple with c-DRX like mechanism, UE performs PDCCH monitoring in a newly defined timer when DL-WUS is detected.
-	Xiaomi asks if this is similar to Option 1-2
Noted
R2-2600950	Discussion on 6G energy efficiency	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.3-p003`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.3 Energy efficiency

```text
Following DL-WUS use cases can be considered for RRC_CONNECTED UE power saving:
1.   DCP-like DL-WUS whose monitoring occasion locates at a configured time offset before the start of drx-onDurationTimer and can be used to indicate UE’s wake up for PDCCH monitoring in the related C-DRX on-duration timer.
2.   DL-WUS for dynamic PDCCH monitoring during C-DX active period.
-	ZTE ask which time will be stopped.   CMCC is open for the scheme but we should focus on meeting the requirements.
3.   LP-WUS option 1-2 like DL-WUS that can triggers the UE to perform PDCCH monitoring in an extra/aperiodic on duration timer.
-	Samsung asks if the WUS cycle is less than DRX cycle.
-	Nokia explains that RAN1 is discussing single Low power receiver.
[3 mins]
Noted
R2-2600650	Network and UE energy efficiency in 6G	Nokia	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.3-p004`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.3 Energy efficiency

```text
Study further which of these options are preferred configurations from RAN2 perspective: “C-DRX without DL WUS”, “DL WUS together with C-DRX” and “DL WUS without C-DRX”
[2 mins]
Noted
R2-2600690	Views on 6G Energy Efficiency	NTT DOCOMO, INC.	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.3-p005`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.3 Energy efficiency

```text
RAN2 to study C-DRX with dynamic wake-up mechanism. For the dynamic wake-up mechanism, whether to introduce DCP or DL-WUS should be justified after the DL-WUS design details are determined and evaluated within RAN1 discussions.
[2 mins]
Noted
Discussion
-	Qualcomm thinks that we should not base our decision on 5G WUS design.
-	Apple thinks that we have too many options for 5G
-	Huawei supports studying all three options
-	Qualcomm thinks DRX alone has been there so should be supported.   DL WUS with DRX should be the baseline.  We can’t rely solely on DL WUS as it is not guaranteed that it will be received, so we need a fall back for the handset design.   So we have concerns with DL WUS without C-DRX
-	Vivo thinks that we need to discuss detailed mechanism in RAN2.    RAN1 is discussing and studying the DL WUS reliability.
-	Ericsson is ok to discuss these options but we should aim to not have all options in the table.
-	ZTE asks if the intention is that DL WUS is mandatory like CDRX.   Xiaomi thinks LP WUS cannot be mandatory.
-	Xiaomi thinks that we should discuss all options and then let RAN1 deal with this.
-	Interdigital thinks that we should study the requirements and use cases/scenarios.
-	Apple asks what does the third option mean without DRX. Xiaomi explains that it means there is no DRX parameters/timers, there is just WUS.
-	CATT thinks that if DL WUS cannot offer the same coverage as paging then it cannot used on it’s own.   But RAN1 is discussing these issues so we can consider it.
-	Docomo thinks we should discuss the options.
-	Mediatek wants to avoid multiple solutions, we should have one framework for time domain power saving.
-	LG indicates that RAN1 is studying OFDM based LP WUS so the coverage shouldn’t be a concern.  Also agrees that we should have one framework and not have increased complexity.
-	Nordic semiconductor thinks that we should include DL WUS in the signle framework from the beginning.
-	ZTE thinks that we can at least agree that DRX without DL WUS is supported.
-	Vivo thinks that we can’t for RAN1 to finish, it will take the whole release. We can study them all and make decision what will be supported after RAN1 has progressed. The WUS without DRX will be configured without the DRX cycle but some of the timers will be needed.
-	RAN1 is discussing option 1-2 so we can wait but we can take 1-1 as a starting point.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.3-p006`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.3 Energy efficiency

```text
6G supports cell DTX/ as well as UE C-DRX. Additionally, aligning cell DTX/DRX with UE CDRX is supported possible but allowing also UE CDRX and cell DTX/DRX having different active time lengths.
[2 mins]
Noted
R2-2600581	Discussion on energy efficiency	ASUSTeK	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.3-p007`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.3 Energy efficiency

```text
For RRC_Connected UEs, the UE DRX configuration is aligned with the cell DTX configuration.
[2 mins]
Noted
R2-2600462	Views on 6G energy efficiency	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.3-p008`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.3 Energy efficiency

```text
RAN2 assume that 5G Cell DTX/DRX mechanism is the starting point to achieve Network sleeping opportunities in 6G, i.e. explicit periodic active/inactive pattern is configured by the NW. FFS its detailed mechanism.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.3-p009`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.3 Energy efficiency

```text
To achieve more flexibility for both UE and NW, Cell DTX/DRX can be configured with UE CDRX or without UE CDRX in 6G.
[3 mins]
Noted
Discussion on cell DTX/DRX mechanism
-	 Nokia thinks that we should allow the cell DTX/DRX behavior but whether it is explicit or implicit can be a stage 3 details.
-	CMCC supports Nokia and Apple proposals.
-	Lenovo thinks that cell DTX and DRX should be discussed separately.   For cell DTX we should study if the network can configure it wihtou having to tell the UE anything.   For cell DRX we need to consider the emergency call scenario.
-	Huawei supports cell DTX and DRX but 5G shouldn’t be the baseline as we had a lot of restrictions.
-	Docomo think we should support
-	Xiaomi thinks that the periodic patterns should be periodic.   Qualcomm thinks that we need to ensure that the impact ot UE is minimized so aligning the patterns with the UE active times is desirable.
-	CATT thinks we should study the details to improve it and make it more aligned.
-	Oppo thinks that the DTX is good for energy saving but it impacts the UE side so we should at least allow some form of mechanism for the UE to wake up the network for some type of delay sensitive traffic.
-	Fraunhofer thinks we should also design from scratch and consider whether it aligns with idle mode as well.
-	Interdigital thinks as a starting point we should have a periodic cell dtx/drx monitoring and can study further how to align with C-DRX and whether it is implicit or explicit.
-	NEC thinks we need to consider the idle mode as well as it may be beneficial for the UE to be aware
-	ZTE thinks we should design a new cell DTX DRX.
-	Ericsson would like to do it implicitly via configuration provided to the UE.   This doesn’t mean that it is done in a periodic basis.
-	Lenovo also thinks we should ensure that it works for idle/inactive/connected mode.
-	Apple is concerned that if it is network behaviour the UE won’t know when the NW is sleeping and we should have some UE behaviour to align the expectation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.3-p010`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.3 Energy efficiency

```text
RAN2 to study joint and simplified (e.g., to avoid duplication) design for flexible cell DTX and flexible UE C-DRX.
[2 mins]
R2-2600126	Discussion on 6G energy efficiency	Xiaomi	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.3-p011`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.3 Energy efficiency

```text
In 6G, for joint UE/network power saving in connected state, consider following directions:
- For fixed-pattern (e.g. cell DTX/DRX-like, C-DRX like) UE/network sleeping opportunities, align UE sleeping cycle with network sleeping cycle (e.g. one is multiple times of the other)
- For dynamic-pattern (e.g. UE’s and cell’s active/non-active periods are triggered by signaling) UE/network sleeping opportunities, design energy efficient signaling to trigger cell’s active/non-active periods and UE’s active/non-active periods.
[3 mins]
R2-2600086	Discussion on 6GR UE PowSav and NES	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.3-p012`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.3 Energy efficiency

```text
For further study of cell DTX/DRX like mechanism, cell DTX need not be tightly coupled with only UE C-DRX like NR Rel-18, and should take DL WUS into consideration which may work w/wo UE C-DRX.
[2 mins]
R2-2600607	Discussion on network and UE energy efficiency	Fujitsu	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.3-p013`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.3 Energy efficiency

```text
RAN2 to study how to ensure the UE’s QoS with enabling sleeping opportunities in NW (e.g., Cell DTX/DRX).
[2 mins]
R2-2600071	Discussion on Energy Efficiency	CATT	discussion	Rel-20	FS_6G_Radio
R2-2600096	Discussion on 6GR Energy Efficiency	WILUS Inc.	discussion	FS_6G_Radio	Withdrawn
R2-2600382	Discussion on energy efficiency 	NEC	discussion	Rel-20	FS_6G_Radio
R2-2600422	Energy efficiency considerations with WUS and DRX	Nordic Semiconductor ASA	discussion	Rel-20
R2-2600502	Discussion on Energy Efficiency	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2600542	Discussion on energy efficiency in connected state	Sharp	discussion	Rel-20
R2-2600565	Discussion on energy efficiency for 6GR	TCL	discussion
R2-2600665	Discussion on energy saving of 6GR	Spreadtrum, UNISOC	discussion	Rel-20
R2-2600687	Discussion on 6G energy efficiency	China Telecom	discussion
R2-2600698	Discussion on energy efficiency in 6G	OPPO	discussion	Rel-20	FS_6G_Radio
R2-2600715	Energy efficiency in 6G	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
R2-2600739	Energy efficiency for 6GR	InterDigital	discussion	Rel-20	FS_6G_Radio
R2-2600766	Discussions on energy efficiency aspects on aspects related to SSB and monitoring alignment	Sony	discussion	Rel-20	FS_6G_Radio
R2-2600846	On the time domain framework for power savings	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
R2-2600865	Energy efficiency in 6G	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2600883	Discussions on 6G energy saving features	ETRI	discussion
R2-2600899	Discussions on 6G Energy Efficiency	Futurewei	discussion	Rel-20	FS_6G_Radio
R2-2600976	Considerations for Energy Saving in 6GR	Samsung	discussion
R2-2600977	Energy Efficiency for 6G: Network and UE Perspectives	Ericsson	discussion	Rel-20
R2-2601046	Discussion on Energy efficiency	CEWiT	discussion	Rel-20	FS_6G_Radio
R2-2601066	6G Radio: Energy efficiency by default 	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
R2-2601109	Discussion on Energy Efficiency aspects of 6GR	Rakuten Mobile, Inc	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.3-p014`

### [6G/Rel-20 RAN2#132] `agreement` 10.3.3.2 Energy efficiency

```text
Study further how to achieve sleeping opportunities (e.g. CELL DTX/DRX) for connected mode.
There are benefits from NW perspective to aligning the sleeping opportunities (e.g. CELL_DTX/DRX) across different states.
For non-connected state wait for further progress on the design common signal/SI/paging/RA, etc design from RAN2 and other WGs.
R2-2508243	Network and UE energy efficiency in 6GR	Nokia, Nokia Shanghai Bell	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.2-a001`

### [6G/Rel-20 RAN2#132] `agreement` 10.3.3.2 Energy efficiency

```text
As a starting point for UE sleeping opportunities, assume C-DRX like mechanism is supported.  Study further details of C-DRX like mechanism.
Study DL WUS.   Study whether and how it interacts/work together with C-DRX like scheme.  Take RAN1 progress into account with respect to L1 power saving features.   Aim to avoid duplicate functionalities.
Study interaction with NW sleeping opportunities (e.g. CELL DTX/DRX)
Not treated
R2-2508940	Discussion on  energy efficiency for network and UE	Lenovo	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.2-a002`

### [6G/Rel-20 RAN2#132] `observation` 10.3.3.2 Energy efficiency

```text
Separate cell DTX and UE C-DRX mechanisms were defined in different 5G releases with duplicated UE behaviours and additional restrictions between cell DTX and UE C-DRX. To obtain the energy saving gain coming from longer sleep duration, the cell DTX should be aligned with UE C-DRX, especially considering a flexible UE C-DRX.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.2-o001`

### [6G/Rel-20 RAN2#132] `observation` 10.3.3.2 Energy efficiency

```text
In 6G, cell-DTX and cell-DRX mechanisms can be further optimized jointly with UE’s DRX or preferences to maximize energy efficiency for both network and UEs while ensuring performance expectations.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.2-o002`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.2 Energy efficiency

```text
Study Cell DTX/DRX in all RRC states, including impact on common signal and channel transmission and UE specific transmission and reception.
-	Huawei asks if the intention is to have the same solution for both.  ZTE thinks it can be the same but the parameters can be different.
-	Xiaomi asks if for CELL DRX we are covering RACH resources.
-	Nokia asks if we concatenate the common signals do we need to do anything extra.   ZTE thinks that we can have the concatenation or determining CELL DTX pattern based on these transmission patterns.
-	Apple supports this but has some concerns about idle mode as it impacts initial access.   Oppo thinks that we need to wait for RAN1.
-	Mediatek thinks that the behaviour can be very different.
-	CMCC thinks that CELL DTX is per cell configuration and we don’t need to worry about legacy and if we don’t do it in both it would make it useless.
-	Docomo CELL DTX/DRX in idle mode we should avoid duplication.
-	Lenovo thinks we should separate the discussion as the network can take care of the configuration of the common signals.
-	Ofinno thinks that functionality should be common in all states.   But we need to discuss details first before we know the details.   And we need to consider both the UE and NW.
-	Interdigital thinks that we agreed on Tuesday to have SIBs grouped together with common signals and the intention here is to align user dedicated channels/tx with the idle mode common channels.
-	Qualcomm thinks that we can wait a bit.
-	Samsung asks whether this is per cell.  ZTE thinks it is per cell but it can be for multiple cell.
-	Huawei thinks that connected mode has less dependency on RAN1.
Noted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.2-p001`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.2 Energy efficiency

```text
Study Cell DTX/DRX and UE DRX to be jointly designed, considering UEs with or without UE DRX configurations.
Noted
Not treated
R2-2508519	Discussion on network and UE energy efficiency	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.2-p002`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.2 Energy efficiency

```text
RAN2 to study joint and simplified (e.g., to avoid duplication) design for flexible cell DTX and flexible UE C-DRX.
R2-2508754	Discussion on 6G energy and power saving features	Qualcomm Incorporated	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.2-p003`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.2 Energy efficiency

```text
RAN2 starts the study on the applicability of joint optimization with cell-DTX and DRX and UE DRX or UE preferences in 6G.
C-DRX
R2-2508754	Discussion on 6G energy and power saving features	Qualcomm Incorporated	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.2-p004`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.2 Energy efficiency

```text
UE DRX is adopted as a key feature in 6G to support energy and power saving for both UEs and network nodes.
Noted
-	Xiaomi, Oppo and Vivo thinks that UE sleeping opportunities are very important regardless of whether we have WUS or not.  Vivo thinks we should evaluate wake up mechanisms and ensure we don’t have too many mechanisms.
-	Apple thinks that C-DRX should be as a starting point and how low power wus can be analyzed further.
-	NEC agrees as C-DRX doesn’t require network signaling.   Samsung, Docomo, Nokia, Interdigital agrees we need to keep C-DRX.
-	Huawei thinks that WUS will be studied as a mechanism as RAN1 agreed it will be studied.
-	Interdigital thinks that we need to see how c-drx works together with nw energy savings.
-	LG thinks LP WUS should also be a baseline.
-	Ericsson thinks we should have C-DRX but we should avoid having multiple solutions in L1 and L2.  Agree that we should have WUS with cDRX.
- 	CMCC thinks cdrx in an important commercialized feature so should be kept, and LP WUS we should wait for RAN1.
-	Ofinno thinks that we need to consider l1 features too.
-	CATT thinks that cDRX should be the starting point.
-	Vivo would like to avoid duplication of CDRX.   Vivo would like to ensure that we only DL WUS on it own.  Qualcomm doesn’t thinks that just DL WUS should be supported.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.2-p005`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.2 Energy efficiency

```text
RAN2 to study enhancements to the C-DRX scheme in 6G, e.g. support of multiple active DRX configurations or adaptive DRX operation, to improve UE power efficiency.
R2-2508613	Energy Efficiency for 6G: Network and UE Perspectives	Ericsson	discussion	Rel-20	FS_6G_Radio
Observation 4	In NR, the effective UE DRX activity is determined by both MAC-layer C-DRX timers and PHY-layer PDCCH monitoring configurations.
Proposal 2	For 6GR, allow configuration of multiple DRX window types in connected mode (analogous to NR C-DRX "OnDuration", "drx-InactivityTimer"), each associated with separate PHY-layer configurations (e.g., search space, TDRA configuration, bandwidth) preconfigured via RRC.
WUS
R2-2508928	Discussion on energy saving of 6GR	Spreadtrum, UNISOC	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.2-p006`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.2 Energy efficiency

```text
Study the decoupling of LP-WUS and C-DRX for connected mode in 6G day-1.
R2-2508296	Discussion on energy efficiency in 6G	OPPO	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.2-p007`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.2 Energy efficiency

```text
For RRC CONNECTED state UEs, RAN2 studies more simplified UE power saving features, e.g., support wake-up signal operation without DRX.
R2-2508613	Energy Efficiency for 6G: Network and UE Perspectives	Ericsson	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.2-p008`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.2 Energy efficiency

```text
For 6GR, allow WUS-based triggering of specific "OnDuration" window configurations, enabling energy-efficient receiver reactivation with appropriate PHY setting.
--
R2-2508519	Discussion on network and UE energy efficiency	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.2-p009`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.2 Energy efficiency

```text
RAN2 to study DL WUS for IDLE mode, including DL WUS for paging.
R2-2508940	Discussion on  energy efficiency for network and UE	Lenovo	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.2-p010`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.2 Energy efficiency

```text
RAN2 to study LP-WUS/WUR as one of candidate UE power saving techniques for all RRC states in 6GR, including:
•	To support LP-WUS/WUR for paging reception as a candidate for day1 feature, taking 5G NR design as baseline.
•	To study further RRM measurement relaxation/offloading on LR, e.g., for neighboring cell measurement in RRC_INACTVIVE/IDLE state, etc.
•	To study using LR for e.g., RRM/RLM/BFD measurements in RRC_CONNECTED mode.
R2-2508054	Discussion on 6GR UE PowSav and NES	vivo	discussion	Rel-20
R2-2508064	6G Radio: Energy efficiency by default	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
R2-2508069	Discussion on Energy Efficiency	CATT	discussion	Rel-20	FS_6G_Radio
R2-2508075	Discussion on energy efficiency in 6G	Transsion Holdings	discussion
R2-2508084	Discussion on 6GR energy efficiency	Xiaomi	discussion	Rel-20	FS_6G_Radio
R2-2508216	Energy efficiency in 6GR	Sharp	discussion
R2-2508377	Views on RAN2 study directions of 6G Network and UE energy efficiency	Apple	discussion	Rel-20	FS_6G_Radio	Withdrawn
R2-2508453	Views on 6G Energy Efficiency	Apple	discussion	Rel-20	FS_6G_Radio
R2-2508462	Discussion on network and UE energy efficiency	Fujitsu	discussion	Rel-20	FS_6G_Radio
R2-2508473	Considerations for Energy Saving in 6GR	Samsung	discussion	Rel-20	FS_6G_Radio
R2-2508527	Views on 6G Energy Efficiency	NTT DOCOMO, INC.	discussion
R2-2508634	6G Energy saving framework	Ofinno	discussion	Rel-20
R2-2508645	Energy efficiency for 6GR	InterDigital	discussion	Rel-20	FS_6G_Radio
R2-2508674	Discussion on possible approaches for energy efficiency	NEC	discussion	Rel-20	FS_6G_Radio
R2-2508677	Views on Energy Efficiency	Fainity Innovation	discussion
R2-2508765	Discussion on Energy Efficiency aspects of 6GR	Rakuten Mobile, Inc	discussion	Rel-20
R2-2508825	Consideration on Energy efficiency for 6G	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
R2-2508831	Discussion on 6G energy efficiency	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2508858	Discussion on energy efficiency for 6GR	TCL	discussion
R2-2508863	Design considerations for the energy efficiency framework	MediaTek UK	discussion	Rel-20	FS_6G_Radio
R2-2508986	Discussion on 6G energy efficiency	China Telecom	discussion	Rel-20	FS_6G_Radio
R2-2508997	Discussion on energy efficiency for 6GR	ITL	discussion	Rel-20
R2-2509030	Discussion on energy efficiency in 6G	CEWiT	discussion	Rel-20	FS_6G_Radio
R2-2509072	6G and UE power saving simplification considerations	Nordic Semiconductor	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.2-p011`

### [6G/Rel-20 RAN1#126] `agreement` 10.4.1 Operation in idle mode

```text
For further study of initial access for idle mode multi-carrier operation, consider at least the following potential use cases:
UC-1: UL coverage enhancement / DL-UL coverage imbalance
UC-2: RACH capacity / offloading / load balancing
UC-3: Network energy saving / common-signaling reduction
Other use cases are not precluded.
For each identified use case, study whether and under which conditions multiple-carrier operation in idle mode provides additional benefit over existing mechanisms.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.4.1-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.4.1 Operation in idle mode

```text
For study of multiple carriers where for initial access a UE can utilize resources for UL (Msg1, etc) or for both UL (Msg1, etc.) and DL (Msg2, etc.) in one carrier other than the carrier where the UE obtains the system information providing configuration for those resources, consider the following potential scenarios for the set of candidate physical carriers for which resources are provided for initial access:
S1: 1 DL physical carrier + N UL physical carriers, where N > 1
S2: M DL physical carriers + 1 UL physical carrier, where M > 1
S3: M DL physical carriers + N UL physical carriers, where M > 1 and N > 1
Note 1: The carrier where the UE obtains the system information and other candidate physical carrier(s) are counted above.
Note 2: For a given UE and a given initial access procedure, UE may use only a subset of the candidate physical carrier.
Note 3: The inclusion of a scenario for study does not imply agreement to support it. The need and applicable use cases/deployment scenarios for each scenario are subject to further study.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.4.1-a002`

### [6G/Rel-20 RAN1#126] `agreement` 10.4.1 Operation in idle mode

```text
For study of multiple carriers where for initial access a UE can utilize resources for UL (Msg1, etc) or for both UL (Msg1, etc.) and DL (Msg2, etc.) in one carrier other than the carrier where the UE obtains the system information providing configuration for those resources,
As a baseline, a single selected physical carrier is used per link direction throughout an attempt of an RACH procedure.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.4.1-a003`

### [6G/Rel-20 RAN1#126] `agreement` 10.4.1 Operation in idle mode

```text
For further study of multiple carriers where for initial access a UE can utilize resources for UL (Msg1, etc) or for both UL (Msg1, etc.) and DL (Msg2, etc.) in one carrier other than the carrier where the UE obtains the system information providing configuration for those resources, consider at least the following deployment conditions:
D1: co-located carriers for which a common timing/frequency synchronization relationship can be assumed
D2: co-located carriers for which a common timing/frequency synchronization relationship cannot be assumed
D3: non-collocated carriers for which a common timing/frequency synchronization relationship cannot be assumed
Other relevant deployment assumptions, including carrier frequency relationship / band separation, numerology / duplexing configuration and UE RF/baseband capability, are considered as applicable.
Note: whether a common timing/frequency synchronization relationship can be assumed is from UE perspective.
R1-2605534	FL summary #1 of multiple carrier operation in idle mode	Moderator (Xiaomi)
R1-2605535	FL summary #2 of multiple carrier operation in idle mode	Moderator (Xiaomi)
R1-2605536	FL summary #3 of multiple carrier operation in idle mode	Moderator (Xiaomi)
R1-2605537	FL summary #4 of multiple carrier operation in idle mode	Moderator (Xiaomi)
R1-2605224	Multiple carrier operation in idle mode	FUTUREWEI
R1-2605290	Discussion on multiple carrier operation in idle mode	Huawei, HiSilicon
R1-2605338	Discussion on multiple carrier operation in idle mode	Spreadtrum, UNISOC
R1-2605405	On multicarrier operation in idle mode	Nokia
R1-2605435	Discussion on multiple carrier operation in idle mode	ZTE Corporation, Sanechips
R1-2605440	6G multi-carrier operation in idle mode	Ericsson
R1-2605457	Discussion on 6GR multi-carrier operation in idle mode	vivo
R1-2605533	Discussion on 6GR spectrum utilization for idle mode	China Mobile Com. Corporation
R1-2605544	Discussion on multi-carrier operation in idle mode	Xiaomi
R1-2605654	Discussion on 6GR spectrum utilization for idle mode	China Mobile Com. Corporation
R1-2605673	Views on Multiple carrier operation in Idle mode	Ofinno
R1-2605755	Discussion on multiple carrier operation in idle mode	CATT
R1-2605759	Discussion on multiple carrier operation in idle mode	KT Corp.
R1-2605772	Multi-carrier operation in idle mode	Sharp
R1-2605854	Multi-carrier operation in IDLE mode	Samsung
R1-2605897	Discussion on multicarrier operations in idle mode	NEC Corporation
R1-2605940	Multiple carrier operation in idle mode	OPPO
R1-2605949	Discussion on Multi-carrier operation in Idle mode 	LG Electronics Inc.
R1-2605992	Multi-carrier operation in Idle	InterDigital, Inc.
R1-2606044	On 6GR multi-carrier operation in IDLE mode 	Apple (UK) Limited
R1-2606111	Discussion on multiple carrier operation in idle mode	China Telecom
R1-2606134	Multiple carrier operation in idle mode	MediaTek Inc.
R1-2606166	Multiple carrier idle mode operation of 6GR air interface 	Panasonic
R1-2606295	Discussion on multi-carrier operation in idle mode	ETRI
R1-2606337	Multiple carrier operation in idle mode	Lenovo
R1-2606346	Discussion on 6GR Multi-Carrier Operation in IDLE mode	Philips International B.V.
R1-2606373	Multi-carrier operation in idle mode	Qualcomm Incorporated
R1-2606406	Discussion on MC operation in idle mode	Google
R1-2606425	Multiple carrier operation in idle mode	AT&T
R1-2606525	Discussion on operation in idle mode	NTT DOCOMO, INC.
R1-2606547	Discussion on multiple carrier operation in idle mode	Quectel
R1-2606583	Discussion on multi-carrier operation in idle mode for 6GR 	WILUS Inc.
R1-2606588	Considerations on multi-carrier operation in idle mode	TCL
R1-2606671	Discussion on operation in idle mode	KDDI Corporation
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.4.1-a004`

### [6G/Rel-20 RAN1#126] `agreement` 10.4.2 Operation in connected mode

```text
Study UL transmission switching across carriers in 6GR, at least considering the following:
Whether/how to achieve unified design for all UL signals/channels
Signaling for switching, e.g., dynamic and/or semi-static switching
Number of Tx chains
Number of carriers
Switching gap
Interaction with carrier aggregation operation
Coordination with other WG(s), e.g., RAN4 (as needed)
Note: SRS antenna switching is separately discussed under UL CSI agenda
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.4.2-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.4.2 Operation in connected mode

```text
Study DL reception switching across carriers in 6GR, at least considering the following:
Applicable scenario(s) (e.g., the scenario(s) considered for NR LB-CA), including identify the scenario(s)
Coordination with other WG(s), e.g., RAN4 (as needed)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.4.2-a002`

### [6G/Rel-20 RAN1#126] `agreement` 10.4.2 Operation in connected mode

```text
For 6GR multiple carrier operation in connected mode, study mechanisms for fast enabling/disabling access to additional carriers, considering at least the following:
UE power saving and/or NW energy saving
Carrier states
How to enable/disable
Assumed NW-side requirements/conditions
Assumed UE-side requirements
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.4.2-a003`

### [6G/Rel-20 RAN1#126] `agreement` 10.4.2 Operation in connected mode

```text
For 6GR multiple carrier operation in connected mode, study mechanisms for PXSCH resource allocation, considering at least the following:
A PXSCH confined within a carrier
A PXSCH over multiple carriers
Applicable scenario and condition
Coordination with other WG(s), e.g., RAN4 (as needed)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.4.2-a004`

### [6G/Rel-20 RAN1#126] `agreement` 10.4.2 Operation in connected mode

```text
For 6GR multiple carrier operation in connected mode, study mechanisms for scheduling PXSCH, considering at least the following:
Self-carrier scheduling
Note: self-carrier scheduling is that a DCI on a carrier schedules a PXSCH on a same carrier
Cross-carrier scheduling
Note: cross-carrier scheduling is that a DCI on a carrier schedules a PXSCH on another carrier
Multi-carrier scheduling
Note: multi-carrier scheduling is that a DCI on a carrier schedules a single PXSCH across multiple carriers, or individual PXSCH per carrier
Coordination with other WG(s), e.g., RAN4 (as needed)
Applicable scenario and condition for the above mechanism(s)
Multiple slot scheduling will be discussed separately in other agenda.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.4.2-a005`

### [6G/Rel-20 RAN1#126] `agreement` 10.4.2 Operation in connected mode

```text
For the study of bandwidth operation with single carrier operation in CONNECTED mode for a UE in 6G, at least consider the following:
A “6GR-BW” should comprise at least a frequency location and the number of contiguous PRBs within a carrier.
Study the necessity that any other parameter (s) are associated to a “6GR-BW” operation
Note: RAN1 strives to minimize the number of parameter(s) that is associated with a “6GR-BW”
Signal(s)/channel(s) transmission/receiving associated to a “6GR-BW”
Benefit(s) and necessity of switching of “6GR-BW” for DL and/or UL, and potential mechanisms for switching
R1-2606907	FL summary#6 on MC operation in connected mode	Moderator (NTT DOCOMO)
Final post-meeting summary for this agenda item.
R1-2605212	Multiple carrier operation in connected mode	FUTUREWEI
R1-2605253	Discussion on multiple carrier operation in connected mode	Spreadtrum, UNISOC
R1-2605311	Discussion on multiple carrier operation in connected mode	Huawei, HiSilicon
R1-2605381	On multicarrier operation in connected mode	Nokia
R1-2605441	6G multi-carrier operation in connected mode	Ericsson
R1-2605458	Discussion on 6GR multi-carrier operation in connected mode	vivo
R1-2605562	Discussion on multi-carrier operation in connected mode	Xiaomi
R1-2605630	Discussion on multiple carrier operation in connected mode	CMCC
R1-2605674	Views on multiple carrier operation in connected mode	Ofinno
R1-2605716	Discussion on multiple carrier operation in connected mode	CATT
R1-2605760	Discussion on multiple carrier operation in connected mode	KT Corp.
R1-2605777	Multi-carrier operation in connected mode	Sharp
R1-2605855	Multi-carrier operation in connected mode	Samsung
R1-2605885	Discussion on multicarrier operations in connected mode	NEC
R1-2605887	Views on 6GR multi-carrier operation in connected mode	ZTE Corporation, Sanechips
R1-2605930	Multiple carrier operation in connected mode	OPPO
R1-2605948	Discussion on Multi-carrier operation in Connected mode	LG Electronics
R1-2605969	Considerations on multi-carrier operation in connected mode	Sony
R1-2606021	On 6GR multi-carrier operation in connected mode	Apple
R1-2606065	Multi-carrier operation in connected mode for 6GR air interface	NVIDIA
R1-2606078	Discussion on multiple carrier operation in connected mode	China Telecom
R1-2606130	Multiple carrier operation in connected mode	Lenovo
R1-2606142	Multiple carrier operation in connected mode	MediaTek Inc.
R1-2606168	Multiple carrier connected operation of 6GR air interface	Panasonic
R1-2606211	Discussion on multi carrier operation in connected mode	1Finity
R1-2606237	Discussion on multi-carrier operation in connected mode	ETRI
R1-2606288	Multi-carrier operation in connected mode	InterDigital, Inc.
R1-2606374	Bandwidth adaptation and multi-carrier operation in connected mode	Qualcomm Incorporated
R1-2606426	Multiple carrier operation in connected mode	AT&T
R1-2606500	Discussion on operation in connected mode	NTT DOCOMO, INC.
R1-2606548	Discussion on multiple carrier operation in connected mode	Quectel
R1-2606589	Considerations on multi-carrier operation in connected mode	TCL
R1-2606639	Multiple Carrier Operation in Connected Mode	Google
R1-2606672	Discussion on operation in connected mode	KDDI Corporation
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.4.2-a006`

### [6G/Rel-20 RAN1#124b] `agreement` 10.4 Energy efficiency

```text
Adopt  column of PDCCH-only BW scaling table for all other DL signal/channel processing
For S_MaxBW value, companies to report which option assumed (Option A: S_MaxBW=0; Option B: S_MaxBW={0.3 for MaxBW = 200%, 1.0 for MaxBW = 400%}).
|  | Scaling Factor |
| --- | --- |
| <=25% | 0.80 + S_MaxBW |
| 100% | 1.00 + S_MaxBW |
| 200% | 1.60 + S_MaxBW |
| 400% | 3.20 |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.4-a001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.4 Energy efficiency

```text
Adopt UL CA scaling for 2CC as
For inter-band CA (assuming 2 RFs), power scaling factor w.r.t. 1CC is 1.5
For intra-band CA (assuming Single RF), at least the following power scaling factor is applied:
| @ 0 dBm | @ 23 dBm | @ 26 dBm |
| --- | --- | --- |
| 1.2 | 1.05 | 1.05 |
Scaling on power consumption assuming all CCs are activated, and no implication on carrier activation/deactivation delay.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.4-a002`

### [6G/Rel-20 RAN1#124b] `agreement` 10.4 Energy efficiency

```text
Power scaling factor for UL 2Tx antennas w.r.t. 1TX is 1.5
Note: 2TX antennas are in the same frequency band
R1-2603353	Summary #2 of 6GR Energy Efficiency Study	Moderators (Ericsson, MediaTek)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.4-a003`

### [6G/Rel-20 RAN1#124b] `agreement` 10.4 Energy efficiency

```text
The relative power values for CAT 2.1 are the same as the relative power values for CAT 2 across all reference configuration sets 1-4.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.4-a004`

### [6G/Rel-20 RAN1#124b] `agreement` 10.4 Energy efficiency

```text
Transition times for CAT 2.1 in Set 4 are aligned with the agreed values for Sets 1, 2, and 3, i.e.,
Light sleep: 100 milliseconds
Deep sleep: 2 seconds
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.4-a005`

### [6G/Rel-20 RAN1#124b] `agreement` 10.4 Energy efficiency

```text
Relative transition energy values for CAT 2.1 in Set 4 are
Light sleep: 210
Deep sleep: 6300
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.4-a006`

### [6G/Rel-20 RAN1#124b] `agreement` 10.4 Energy efficiency

```text
The power consumption of SBFD operation in BS, using a factor of its antennas,  and  , and a fraction of the spectrum,  and  for DL and UL operation, respectively, is modelled according to:
where  is the static power in SBFD operation in BS,  and  are factors due to DL and UL SBFD operation.
R1-2603443	Summary #4 of 6GR Energy Efficiency Study	Moderators (Ericsson, MediaTek)
From Friday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.4-a007`

### [6G/Rel-20 RAN1#124b] `agreement` 10.4 Energy efficiency

```text
Power scaling for UL BW with 200% BW ratio factor is 1.2 for 0 dBm TX power level.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.4-a008`

### [6G/Rel-20 RAN1#124b] `agreement` 10.4 Energy efficiency

```text
For CA reception based on one RF chain, power scaling factor for PDCCH-only is defined as:
(Bandwidth scaling factor for single CC reception with the same total bandwidth) + X  (CC number - 1)
X = [0.2] if the above assumes PDCCH monitoring per CC
X = 0 if PDCCH monitoring only on one CC
FFS: other cases
The scaling factor assumes all CCs are activated. There is no implication on carrier activation/deactivation delay.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.4-a009`

### [6G/Rel-20 RAN1#124b] `agreement` 10.4 Energy efficiency

```text
For CA reception based on multiple RF chains, overall power scaling factor is defined as:
(Power scaling factor for CA reception based on one RF chain) + Y  (CC number - 1)
where
Y models additional power scaling factor with each extra RF chain
Y = [0.3] for reception of PDCCH + PDSCH, PDCCH-only and other signals/channels
FFS: Same or different Y value for CC BW different from the reference configuration
The scaling factor assumes the same number of RF chains as the CC number and that all CCs are activated. There is no implication on carrier activation/deactivation delay.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.4-a010`

### [6G/Rel-20 RAN1#124b] `agreement` 10.4 Energy efficiency

```text
For evaluation purpose, EE processing power values for 10 MHz BW is 1.2x of the corresponding power values of 5MHz BW.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.4-a011`

### [6G/Rel-20 RAN1#124b] `agreement` 10.4 Energy efficiency

```text
Include UE power consumption values for the RRM measurements without EE processing as follows:
Serving cell RRM: 100
Serving & neighbour cell RRM:
| N: Number of cells for intra-frequency measurement | Synchronous case | Asynchronous case |  |  |
| --- | --- | --- | --- | --- |
|  | FR1 | FR2 | FR1 | FR2 |
| N=8 | 150 | 225 | 170 | 285 |
| N=4 | 120 | 195 | 140 | 255 |
Assume the neighbour cells are known cells
The above power values are based on 100MHz reference configuration. BW scaling for other DL signal/channel processing is applied if the active BW is different from the reference.
BW and antenna scaling rules can be applied
Note: FR1 includes ~7GHz, and FR2 includes 24.25 GHz – 52.6 GHz
R1-2603444	Final Summary of 6GR Energy Efficiency Study	Moderators (Ericsson, MediaTek)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.4-a012`

### [6G/Rel-20 RAN1#124] `agreement` 10.4 Energy efficiency

```text
For NES evaluation purposes and relative comparison of different candidate energy saving schemes for 6GR, define the following baseline network configurations
SSB with 20 ms periodicity, at least for single cell
SIB1, if available, company to report assumed periodicity from {20 ms, 160 ms}
RO, if available, with 10/20 ms periodicity
Furthermore, to assist comparisons
Companies to report ,  and  values for BS processing of the above signal(s)/channel(s)
Companies to report the average network load in %
Companies can evaluate and report other configuration(s) with justification
Note: The corresponding evaluation is not intended for energy efficiency comparison with 5G/NR.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.4-a001`

### [6G/Rel-20 RAN1#124] `agreement` 10.4 Energy efficiency

```text
The following transition times are adopted for BS models CAT1 and CAT2, if supported, for BS reference configuration Set 4:
| Power state | BS Category 1, Set 4 | BS Category 2, Set 4 |
| --- | --- | --- |
| Deep sleep | 50 ms | 10 s |
| Light sleep | 6 ms | 640 ms |
FFS: whether delta value is needed due to larger number of TXRU
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.4-a002`

### [6G/Rel-20 RAN1#124] `agreement` 10.4 Energy efficiency

```text
The following relative transition energies are adopted for BS models CAT1 and CAT2, if supported, for BS reference configuration Set 4:
| Power state | BS Category 1, Set 4 | BS Category 2, Set 4 |
| --- | --- | --- |
| Deep sleep | 1075 | 31500 |
| Light sleep | 163 | 1344 |
FFS: whether delta value is needed due to larger number of TXRU
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.4-a003`

### [6G/Rel-20 RAN1#124] `agreement` 10.4 Energy efficiency

```text
IF a BS model CAT 2.1 (2-plus) is introduced, it has the following transition energy characteristics for Set 1-3. FFS: Set 4:
| Transition Time (Deep Sleep) | Transition Time (Light Sleep) | Additional Transition Energy (Deep Sleep) | Additional Transition Energy (Light Sleep) |
| --- | --- | --- | --- |
| 2 s | 100 ms | 3400 | 170 |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.4-a004`

### [6G/Rel-20 RAN1#124] `agreement` 10.4 Energy efficiency

```text
Include the following UL long PUCCH/PUSCH/PRACH power values in the UE power model:
Note: UE reference configuration is 1TX chain
| TX Power | Relative Power |
| --- | --- |
| 0 dBm | 250 (agreed; reference only) |
| 10 dBm (X4) | 340 |
| 15 dBm (X5) | 410 |
| 20 dBm (X6) | 560 |
| 23 dBm | 700 (agreed; reference only) |
| 26 dBm (X7) | 1100 |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.4-a005`

### [6G/Rel-20 RAN1#124] `agreement` 10.4 Energy efficiency

```text
Adopt the following cross-slot scheduling scaling for evaluation for 6GR UE power consumption model:
|  | Scaling | Comment |
| --- | --- | --- |
| PDCCH-only | Power of cross-slot scheduling is 0.7x same-slot scheduling | Applicable for FR1 (including around 7GHz) and FR2 (including 24.25 GHz – 52.6 GHz). |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.4-a006`

### [6G/Rel-20 RAN1#124] `agreement` 10.4 Energy efficiency

```text
Include the following DL antenna scaling factors in 6GR UE power consumption model:
Note: Applicable for FR1 (including around 7GHz) and FR2 (including 24.25 GHz – 52.6 GHz), where, for FR2, number of DL antenna assumed is up to [4]
FFS: Scaling for 8Rx
| UE Rx Antenna Configuration | Scaling |
| --- | --- |
| 6Rx | 1.4 × 4Rx |
| 4Rx | 1.0 |
| 2Rx | 0.7 × 4Rx |
| 1Rx | 0.7 × 2Rx |
R1-2601605	Summary #4 of 6GR Energy Efficiency Study	Moderators (Ericsson, MediaTek)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.4-a007`

### [6G/Rel-20 RAN1#124] `agreement` 10.4 Energy efficiency

```text
RAN1 to further define reference configuration for UEs with 20MHz or smaller bandwidth.
FFS: Same scaling rules (without SMaxBW) are applied to both reference configurations.
FFS: Reuse/extend the reference configuration and power values from NR TR 38.875.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.4-a008`

### [6G/Rel-20 RAN1#124] `agreement` 10.4 Energy efficiency

```text
Update PDCCH+PDSCH bandwidth scaling table in the 6GR UE power model with the following values
Subject to adaptation delay = Tmin, no larger than NR BWP switch delay (Type 2)
SMaxBW can be zero, or the other option: 0.15 and 0.5 for MaxBW = 200% and 400%, respectively. Company to report which option is assumed in their evaluation.
| ΓB | ΓTput=1 | ΓTput=1/2 | ΓTput=1/4 |
| --- | --- | --- | --- |
| 25% | 0.40 + SMaxBW | - | - |
| 100% | 1.00 + SMaxBW | - | - |
| 200% | 2.10 + SMaxBW | 1.50 + SMaxBW | - |
| 400% | 4.60 | 3.20 | 2.40 |
If adaptation delay  is allowed, scaling factor for  can be 0.4 or the other option: 0.3. Company to report which option is assumed in their evaluation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.4-a009`

### [6G/Rel-20 RAN1#124] `agreement` 10.4 Energy efficiency

```text
Update PDCCH-only bandwidth scaling table in the 6GR UE power model with the following values:
Subject to adaptation delay = Tmin, no larger than NR BWP switch delay (Type 2)
SMaxBW can be zero, or the other option: 0.3 and 1.0 for MaxBW = 200% and 400%, respectively. Company to report which option assumed in their evaluation.
| ΓB | ΓTput=1 | ΓTput<=1/2 |
| --- | --- | --- |
| 25% | 0.80 + SMaxBW | - |
| 100% | 1.00 + SMaxBW | - |
| 200% | 1.60 + SMaxBW | 1.30 + SMaxBW |
| 400% | 3.20 | 2.40 |
If adaptation delay  is allowed, scaling factor for  can be 0.8 or the other option: 0.6. Company to report which option is assumed in their evaluation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.4-a010`

### [6G/Rel-20 RAN1#124] `agreement` 10.4 Energy efficiency

```text
Include the following bandwidth scaling table for micro sleep in the 6GR UE power model:
Subject to adaptation delay = Tmin, no larger than NR BWP switch delay (Type 2)
SMaxBW can be zero, or the other option: 0.3 and 1.0 for MaxBW = 200% and 400%, respectively. Company to report which option assumed in their evaluation.
| ΓB | Scaling factor |
| --- | --- |
| 25% | 0.80 + SMaxBW |
| 100% | 1.00 + SMaxBW |
| 200% | 1.60 + SMaxBW |
| 400% | 3.20 |
If adaptation delay  is allowed, scaling factor for  can be 0.8 or the other option: 0.6. Company to report which option is assumed in their evaluation.
The following scaling w.r.t. DL antenna number is also applied to micro sleep:
| #RX antenna | Scaling factor |
| --- | --- |
| #RX = 1 | 0.6 |
| #RX = 2 | 0.7 |
| #RX = 4 | 1.0 |
| #RX = 6 | 1.4 |
FFS: Whether the above scaling rules is applicable to light sleep
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.4-a011`

### [6G/Rel-20 RAN1#124] `agreement` 10.4 Energy efficiency

```text
For EE Processing 2-RX in FR1, adopt the following values:
| Sleep State | 2-RX | 1-RX (agreed; reference only) |
| --- | --- | --- |
| Micro sleep (X1) | 14 | 10 |
| Light sleep (X2) | 17 | 12 |
| Deep/Ultra-deep (X3) | 21 | 15 |
If EE processing reception time is X symbols within a slot, the power value is scaled by (X/14).
FFS: whether to scale additional energy overhead
FFS: Values for 10MHz BW
R1-2601687	Summary #5 of 6GR Energy Efficiency Study	Moderators (Ericsson, MediaTek)
From Friday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.4-a012`

### [6G/Rel-20 RAN1#124] `agreement` 10.4 Energy efficiency

```text
BS model CAT 2.1 is introduced. All BS models CAT 1, CAT 2 and CAT 2.1 may be used for evaluations in 6GR SI.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.4-a013`

### [6G/Rel-20 RAN1#124] `agreement` 10.4 Energy efficiency

```text
In EE evaluations, to adapt a BS’s number of active antenna TXRU to {1/2 and 1/4} of the total number of antenna TXRU and to adapt the associated circuitry.
FFS:
Power model for BS
Power states
State transitions
Application of scaling of BS for static and/or dynamic parts
Coverage, throughput aspects in UL and DL
BS models and reference configuration compatibility
Applicable signals and channels, related procedures and RRC states
Latency aspects
UE power consumption and complexity aspects
BS complexity
Use cases (e.g., UE-initiated on-demand SIB1)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.4-a014`

### [6G/Rel-20 RAN1#124] `agreement` 10.4 Energy efficiency

```text
For CA reception based on one RF chain, power scaling factor is same as that of bandwidth scaling with the same total bandwidth.
Scaling on power consumption assuming all CCs are activated, and no implication on carrier activation/deactivation delay.
FFS: Separated scaling for slots with PDCCH-only
FFS: Scaling for CA reception based on more than one RF receive chains.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.4-a015`

### [6G/Rel-20 RAN1#124] `agreement` 10.4 Energy efficiency

```text
Adopt the following UL scaling for 6GR UE power consumption model:
|  | Scaling | Comment |
| --- | --- | --- |
| Short PUCCH | Short PUCCH power = 0.3 x uplink power (Assume short PUCCH of 1-symbol) | Applicable for FR1 (including around 7GHz) and FR2 (including 24.25 GHz – 52.6 GHz). |
| SRS | SRS power = 0.3 x uplink power (Assume SRS of 1-symbol) | Applicable for FR1 (including around 7GHz) and FR2 (including 24.25 GHz – 52.6 GHz). |
FFS: Scaling for different symbol numbers
R1-2601688	Summary #6 of 6GR Energy Efficiency Study	Moderators (Ericsson, MediaTek)
R1-2601690	Final summary of 6GR Energy Efficiency Study	Moderators (Ericsson, MediaTek)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.4-a016`

