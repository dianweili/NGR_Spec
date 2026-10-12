# 6GR 非地面网络

**当前进展** · 阶段：收敛中

6GR NTN 已形成若干研究基线：链路预算模板以既定模板和场景为基础，研究 GNSS-based、degraded 与 GNSS-less/free 操作，并支持大调度偏移及卫星辅助的上行同步。RAN1 正在推进 HARQ、随机接入、波束覆盖、多卫星干扰管理等物理层议题；RAN2 则研究跨 TN/NTN 与 NTN/NTN 的移动性、测量和 GNSS-independent RTT 机制。部分评估参数和机制已有共识，但多项方案仍处于研究或待定状态，跨工作组依赖也尚未解决。

**未决问题**

- 链路预算模板的部分行值、场景和参数仍待确定，包括 APC 损耗、天线配置及更大天线参数。
- GNSS-degraded/free 操作所需的位置获取、位置 fix 频率及 PRACH 差分时间与频率误差场景仍待明确。
- 大 RTT 下 HARQ 方案的最终选择、适用条件及其与 TN 设计的协调尚未确定。
- 大调度偏移的完整设计仍待细化，包括是否支持 UE-specific k_offset，以及与 K1/K2 等调度设计的关系。
- 多卫星干扰管理、层级波束结构及 beam footprint 覆盖比例的具体参数和适用性仍待研究。
- 移动性、测量触发、GNSS-independent RTT 与相关计时器机制仍在研究，部分议题依赖 RAN1、RANP 或后续讨论。

## 6GR 演进

### [6G/Rel-20 RAN2#134] `agreement` 9.6 NTN

针对 GNSS-free，研究非 UE-location-based mobility（包括 HO、cell selection/reselection 和 measurements）；对于 GNSS-degraded operation，等待 RAN1 进展。NTN 预计会有类似 5G 的 L2 timer 影响，待 RAN1 进一步进展后讨论，并涉及 multi-orbit operation。

```text
For GNSS free, study non UE-location-based mobility (including HO, cell selection/reselection, measurements).    Wait for RAN1 and RAN plenary progress for location-based mobility solutions where the UE location can be determined without relying on non-3GPP systems like GNSS.
For GNSS degraded, wait for RAN1 progress
Similar to 5G, L2 timer impacts are expected for NTN, but can discuss after RAN1 further progress.
Multi-orbit operation
R2-2603509	Discussion on 6G NTN	OPPO	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.6-a001`

### [6G/Rel-20 RAN2#134] `observation` 9.6 NTN

对于 GNSS-free，优先采用 non UE-location-based solutions，因为这符合 6G 的 TN/NTN harmonization 目标。

```text
For GNSS-free, non UE-location-based solutions are preferable, since they follow the 6G objective of TN/NTN harmonization.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.6-o001`

### [6G/Rel-20 RAN2#134] `observation` 9.6 NTN

在 NR-NTN 中，RACH 和 C-DRX 的关键 MAC timers 高度依赖基于 GNSS 的 RTT calculations。

```text
In NR-NTN, critical MAC timers for RACH and C-DRX are heavily dependent on GNSS-based RTT calculations.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.6-o002`

### [6G/Rel-20 RAN2#134] `proposal` 9.6 NTN

在 RAN plenary 就 NTN 中支持 RAT-dependent positioning 取得进一步进展前，RAN2 假设不具备 GNSS capability 的 UE 无法在 NTN 中获取其位置。

```text
For GNSS-free operation, RAN2 assumes that UE without GNSS capability cannot acquire its location in NTN, before RAN plenary makes further progress on the support of RAT-dependent positioning in NTN.
-	CATT thinks that there is a requirement that NTN needs to support positioning.  Xiaomi explains that in plenary they only agreed to ecid positioning.
-	Mediatek thinks that we need to wait to RAN1.
Noted
R2-2603425	Discussion on 6G NTN	InterDigital, Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.6-p001`

### [6G/Rel-20 RAN2#134] `proposal` 9.6 NTN

RAN2 等待 RAN1 关于 GNSS-degraded operation 的进展。

```text
RAN2 to wait for RAN1 progress regarding GNSS-degraded operation.
Noted
R2-2603739	Discussion on NTN mobility and GNSS-Free for 6G	THALES, Novamint, Gatehouse Satcom, Sateliot, Iridium, Ericsson, TNO, SES, ST Engineering iDirect, ESA	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.6-p002`

### [6G/Rel-20 RAN2#134] `proposal` 9.6 NTN

RAN2 研究 non-location-based mobility，以及 UE location 可在不依赖 GNSS 等 non-3GPP systems 的情况下确定的 location-based mobility solutions。

```text
RAN2 to study non-location-based mobility, as well as location-based mobility solutions where the UE location can be determined without relying on non-3GPP systems like GNSS.
Noted
Discussion on GNSS-free
-	LG also thinks that we can discuss non-location based type of solutions.
-	Huawei thinks that we should look into non-location based.
R2-2603155	Discussion on 6GR NTN Scenarios	Sharp	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.6-p003`

### [6G/Rel-20 RAN2#134] `proposal` 9.6 NTN

对于 GNSS-less/degraded operations，6GR NTN 支持 time-based mobility 和 beam-level RSRP-based mobility 作为替代触发条件。

```text
For GNSS-less/degraded operations, 6GR NTN supports time-based mobility and beam-level RSRP-based mobility as alternative triggering conditions.
Noted
R2-2604189	Discussion on the 6G NTN	Google, AUMOVIO	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.6-p004`

### [6G/Rel-20 RAN2#134] `proposal` 9.6 NTN

RAN2 将研究支持 6G NTN GNSS-independent RTT estimation 的机制；估计的 RTT 至少用于延后 RA 相关定时器的启动，并延长 C-DRX 相关定时器。讨论中提出计时器可纳入 work item 阶段，也提及可基于 DL 启动计时器；该议题记为 Noted。

```text
RAN2 to study mechanisms enabling GNSS-independent RTT estimation for 6G NTN, where the estimated RTT is at least used for delaying the start of RA related timers (e.g., ra-ResponseWindow and ra-ContentionResolutionTimer) and for extending the C-DRX related timers (e.g., drx-HARQ-RTT-TimerDL and drx-HARQ-RTT-TimerUL).
-	Mediatek thinks that this is also dependent on timers.
-	Samsung thinks that we can consider the timers as part of the work item phase.
-	Ericsson thinks that we can start the timers based on the DL too.
-	Interdigital thinks that there are different solution to consider for GNSS-free/degraded so we should maybe need to study.   Oppo agrees.  Qualcomm doesn’t understand the impact to RAN2.
Noted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.6-p005`

### [6G/Rel-20 RAN2#134] `proposal` 9.6 NTN

针对 multiorbit mobility 和 NTNTN mobility，将研究 QoS-based cell reselection，使 RRC IDLE mode UE 可优先驻留 GEO cell，并在 MT 或 MO data arrival 触发时根据 service requirements 选择接入小区。该议题记为 Noted。

```text
For multiorbit mobility and NTNTN mobility, study QoSbased cell reselection to enable RRC IDLE mode UEs to preferentially camp on GEO cell and, when triggered by MT or MO data arrival, select an appropriate cell for access based on service requirements.
-	Qualcomm asks what is mean by QoS.   Oppo explains that is a service.
Noted
R2-2603539	Discussion on 6GR NTN related designs	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.6-p006`

### [6G/Rel-20 RAN2#134] `proposal` 9.6 NTN

多轨道议题达成一致：在 TN session 继续讨论 multi-carrier idle mode，并将 multi-orbit 纳入讨论场景；至少研究 inter-frequency 场景下的 service-based reselection。还将结合 TN session 后续讨论，了解相较于 Option 1 的收益，以及特定 NTN 问题或顾虑。

```text
RAN2 to study multi-orbit operation assuming same operator:
Paging and initial access procedure:
Option 1): UE paged by GEO, and accesses via GEO, then the NW handover or redirect the UE to LEO;
Option 2): UE paged by GEO, then performs cell reselection to LEO, and performs initial access on LEO (i.e., cross-carrier paging response);
Option 3): UE paged by GEO, and directly performs initial access via LEO based assistance information provided by GEO (i.e., cross-carrier random access).
Feasibility of providing coverage information for other orbits for efficient switch including cell selection/reselection and measurement triggering.
-	Option 2 and 3 need to be studied a bit more.
-	ZTE also thinks that we should study both option 2 and 3.
-	Xioami thinks that option 2 can work for both MT and MO case, so we should prioritize that one.   ZTE thinks that option 3 can also apply for MO.    CATT agrees that the options apply to both MO and MT.
-	Huawei explains that the difference between 2 and 3 is how the information for accessing the information is provided.
-	Option 3 should be discussed in TN first and option 2 is more friendly for UE, so we can start with option 2.    ZTE thinks that when we study the multicarrier we can add multi-orbit and aim to have the same solution.
-	Ericsson asks where the power savings is.
-	Nokia asks if we increase the risks.   Thales and Qualcomm think that there are problems of UE attacking the LEO if there is false paging.   Qualcomm also explains that we have to acquire synchronization that takes a long time.    ZTE and Xioami thinks that the false paging is not specific to NTN, even in TN it not protected.   Samsung explains that network triggered mobility should be secure.  Xiaomi explains that the paging can be in both GEO and LEO.
-	Google explains that there are cons with option 2, latency increase and option 3 overhead.
-	Service based reselection can solve the problem and you don’t need to tell the UE which orbit to to respond to.
Noted
Discussion
-	MEdiatek asks if the UE is expected to monitor the other orbit.   Interdigital thinks that there can be solution on where the GEO cell tells you rather than monitoring the other orbits.  There may be deployments where there is no LEO coverage.   ZTE thinks that anyways the UE will monitor other cells without needing to know whether it is GEO or LEO
-	Fraunhofer asks if this is like a redirection and can be similar to RACH case for TN.  .
-	Ericsson asks what problem do you see and what KPI do you expect to solve with this solution.     Nokia explains that coverage is a big problem, GEO can provide coverage by LEO provides better service.     Also power is a consideration.
-	Apple thinks that GEO and LEO are on different carriers so this is similar to multi carrier idle.   So We can consider one solution for TN and NTN.   CMCC thinks that the benefit is even higher than for TN as the satellites are moving very fast, so GEO should provide some information and the let the UEs camp there.    Xiaomi thinks that it is not necessary the case that cells are in different carrier.
-	Qualcomm explains that there are regulations that you have to avoid interference so it is likely for FR1 it is on different carriers.
-	Huawei asks if we intend to specify what services should go to which orbit.  Mediatek thinks that reselection should be UE behaviour and not specify too much.
-	Qualcomm would like to make sure that we shouldn’t override the reselection frequency priority.
Agreements on multi-orbit
-	Continue the discussion on multi-carrier idle mode in TN session and include multi-orbit as one of the scenarios to be discussed.
-	Study service-based reselection at least for inter-frequency scenario.
-	Understand the gains/benefits compared to option 1 and/or any specific NTN related problems/concerns after some discussions on TN session have taken place.
TN-NTN mobility
R2-2603828	Discussion on 6G NTN mobility	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
Proposal 4 Consider the following aspects for mobility between TN and NTN:
capability handling
identification of essential measurement and handover assistance information
trigger events for measurement relaxation (i.e., skip NTN while in good coverage of TN and vice versa)
use of unique satellite ID and same formats/granularity/unit for its parameters.
Noted
R2-2602962	Further Considerations on  6GR NTN	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.6-p007`

### [6G/Rel-20 RAN2#134] `proposal` 9.6 NTN

针对 intra-RAT 6G TN-NTN cell reselection，将至少考虑以下测量启动机制：TN 到 NTN 时，以 RRM-based S-measure 作为基线；NTN 到 TN 时，可考虑 UE 与 reference location 的距离或 serving NTN cell 的 serving time。

```text
For intra-RAT 6G TN-NTN cell reselection, at least consider the following mechanism:
In case of TN to NTN mobility, RRM based S-measure for measurement initiation should be considered as baseline;
In case of NTN to TN mobility, the distance between UE and the reference location or the serving time of the serving NTN cell can be considered for measurement initiation.
-	China telecom thinks we can do better than 5G by not putting the restrictions.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.6-p008`

### [6G/Rel-20 RAN2#134] `proposal` 9.6 NTN

针对 TN/NTN 与 NTN/NTN mobility，将研究 idle/inactive 和 connected 状态下 NTN 特定的 measurement relaxation/initiation trigger conditions，例如 S-measure、reference location 和 time。原文列出了 TN 到 NTN 与 NTN 到 TN 的 measurement report 条件。

```text
For intra-RAT 6GR TN-NTN mobility, at least consider the following measurement report conditions:
For TN->NTN
Distance between UE and a reference location of the neighbor cell becomes shorter than configured threshold;
Serving cell becomes worse than the absolute threshold and distance between UE and a reference location of the neighbor cell becomes shorter than configured threshold;
For NTN->TN:
The distance between UE and a reference location of the serving cell becomes larger than configured threshold and neighbor cell become better than the absolute threshold.
Agreements on mobility
-	Study NTN specific trigger conditions for measurement relaxation/initiation for idle/inactive and connected (e.g. S-measure, reference location, time, etc) for mobility between TN/NTN and NTN/NTN.
Measurement enhancements
R2-2603509	Discussion on 6G NTN	OPPO	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.6-p009`

### [6G/Rel-20 RAN2#134] `proposal` 9.6 NTN

6G NTN 的 SMTC 和 measurement gap 设计将复用 5G NTN 的 multiple SMTC/MG、RRC IDLE UE-based SMTC adjustment，以及 RRC CONNECTED UE 的 PDD report。另将研究 beam-based SMTC configuration，以减少 signalling overhead 和 GNSS dependency。

```text
For SMTC and measurement gap design in 6G NTN:
a)	Reuse the following mechanisms from 5G NTN: multiple SMTC/MG, UE based SMTC adjustment for RRC IDLE mode UEs, PDD report for RRC CONNECTED mode UEs.
b)	Study beam based SMTC configuration to reduce signalling overhead and GNSS dependency.
R2-2604129	Solutions for 6G NTN	Ericsson, Novamint, Iridium, ESA	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.6-p010`

### [6G/Rel-20 RAN2#134] `proposal` 9.6 NTN

将研究基于 serving cell reference location 的方案，以在 6G NTN 测量定时中考虑不同卫星之间的 UE-aNB propagation delay difference。

```text
Study solutions, based on a reference location of the serving cell, to account for the UE-aNB propagation delay difference between different satellites in the measurement timing in 6G NTN.
R2-2603034	Consideration on 6G NTN design	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
R2-2603082	NTN SIB messages Design Consideration on 6G TN_NTN Mobility	T-Mobile USA Inc, Deutsche Telekom AG	discussion	Withdrawn
R2-2603204	Discussion on GNSS operations and mobility aspects	CATT	discussion	Rel-20	FS_6G_Radio
R2-2604189	Discussion on the 6G NTN	Google, AUMOVIO	discussion	Rel-20	FS_6G_Radio
R2-2603314	NTN in 6G	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2603392	Discussion on different aspects of NTN Framework	Tejas Networks Limited	discussion	Rel-20	FS_6G_Radio
R2-2603410	Consideration on mobility aspects for 6G NTN	LG Electronics Inc.	discussion
R2-2603449	Consideration on multi-orbit mobility in 6G NTN	ETRI	discussion	Rel-20
R2-2603485	Measurement and Mobility for NTN	NEC	discussion	Rel-20	FS_6G_Radio
R2-2603529	Discussion on assistance information to support mobility between TN and NTN	ITRI, Acer Incorporated	discussion	FS_6G_Radio
R2-2603558	NTN aspects for 6GR	Lenovo	discussion	Rel-20
R2-2603578	Discussion on 6G NTN	Samsung	discussion
R2-2603585	NTN for 6G	Nokia	discussion	FS_6G_Radio
R2-2603630	GNSS-degraded/GNSS-free operations on 6G NTN mobility	Sony	discussion	Rel-20	FS_6G_Radio
R2-2603631	Cell selection/re-selection in 6G multi-orbit mobility	Sony	discussion	Rel-20	FS_6G_Radio
R2-2603684	Consideration of 6G NTN mobility	China Telecom	discussion	Rel-20
R2-2603735	Views on 6G NTN	Apple	discussion	Rel-20	FS_6G_Radio
R2-2603772	Discussion on mobility framework for NTN including multi-orbit scenarios	Turkcell	discussion	Rel-20	FS_6G_Radio
R2-2603834	NTN SIB messages Design Consideration on 6G TN/NTN Mobility	T-Mobile USA Inc., Deutsche Telekom AG	discussion
R2-2603874	Considerations on 6G NTN	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2603883	Views on 6G NTN	NTT DOCOMO	discussion
R2-2603915	Mobility Aspects for 6G NTN	MediaTek Inc.	discussion
R2-2603987	Discussion on NTN for 6GR	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2604007	Discussion on 6G mobility for NTN	ASUSTeK	discussion	Rel-20
R2-2604019	Discussion on 6G NTN	1FINITY Inc.	discussion	Rel-20	FS_6G_Radio
R2-2604036	Overview of 6GR NTN mobility	Amazon Web Services	discussion
R2-2604085	Views on 6GR NTN Mobility	CEWiT	discussion	Rel-20	FS_6G_Radio
R2-2604095	Discussion on 6G NTN mobility	CSCN	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.6-p011`

### [6G/Rel-20 RAN2#132] `agreement` 10.2.2 TN/NTN integration

6G NTN 可采用 5G NTN 的部署场景（LEO、MEO、GSO）和 payload type 假设；是否研究 GNSS 取决于 RANP 及其他工作组的讨论。RAN2 将研究与 TN 设计共同处理的功能和 NTN 特定功能，包括 HARQ、mobility、initial access、uplink time and frequency pre-compensation、TA reporting、satellite switch with re-sync、beam hopping 和 discontinuous coverage；MBS、dual connection、Carrier Aggregation 和 VLEO 可在 RANP 讨论。

```text
1	The basic assumption with 5G NTN deployment scenarios (LEO, MEO, GSO) and payload type can be adopted in 6G NTN.   FFS whether we will study with and/or without GNSS, depending on RANP and other WG discussion first.
2	For 6G NTN, RAN2 will consider at least the following features/procedures to treated together with the TN design (e.g. common features/procedures):
-	HARQ
-	L2 timer handling, e.g., the timer value range should cover both TN and NTN, adaptive UP timer start time based on RTT;
-	Measurement framework (including measurement gap)
-	Mobility framework (including TN and NTN mobility)
-	TAC. e.g., support multiple TACs per PLMN in one cell;
-	SIB acquisition/design
-	PWS (Public Warning System) services over an intended area;
-	Initial access framework (including network type indiciation)
3	At least the following NTN features will be further studied in RAN2 (maybe treated in NTN specific AI).  Focus will be on RAN2 impacts.
-	Uplink time and frequency pre-compensation;
-	TA reporting;
-	Satellite switch with re-sync;
-	Beam hopping.
-	Discontinuous coverage
NOTE:  Common design can be considered if something can be applicable to TN as well later
4	The following features can be discussed in RANP
-	MBS broadcast and multicast via NTN;
-	Dual connection;
-	Carrier Aggregation.
-	VLEO
Not treated
R2-2508045	Consideration of TN and NTN Integration in 6GR	vivo	discussion	Rel-20
R2-2508077	Discussion on the general aspects of 6G NTN	Xiaomi	discussion	Rel-20	FS_6G_Radio
R2-2508130	Introduction of explicit Network Type Indicator for 6G	T-Mobile USA Inc.	discussion
R2-2508148	Discussion on TN and NTN integration	CATT, CUC	discussion	Rel-20	FS_6G_Radio
R2-2508183	Discussion on requirement for 6GR NTN	Transsion Holdings	discussion
R2-2508203	Discussion on NTN Requirements for 6GR	AST SpaceMobile	discussion	Late
R2-2508219	Discussion for TN/NTN integration	Sharp	discussion	Rel-20	FS_6G_Radio
R2-2508284	Discussion on harmonized design for TN and NTN	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
R2-2508301	Discussion on the harmonized 6GR for TN and NTN	Google	discussion	Rel-20	FS_6G_Radio
R2-2508327	On 6G TN-NTN integration	Samsung	discussion	Rel-20
R2-2508359	Initial considerations on NTN design for 6G	Nokia Denmark	discussion	Rel-20	FS_6G_Radio
R2-2508411	Harmonized Design for TN and NTN in 6G	MediaTek Inc.	discussion
R2-2508415	Overview of harmonized 6G Radio design for TN and NTN	Amazon Web Services	discussion
R2-2508448	Views on 6G NTN	Apple	discussion	Rel-20	FS_6G_Radio
R2-2508460	Discussion on 6G TN/NTN integration	Fujitsu	discussion	Rel-20	FS_6G_Radio
R2-2508491	Discussion on TN/NTN Integration	ETRI	discussion	Rel-20
R2-2508528	Views on 6G TN/NTN integration	NTT DOCOMO, INC.	discussion
R2-2508541	Discussion on 6GR TN/NTN integration	Sony	discussion	Rel-20	FS_6G_Radio
R2-2508555	TN/NTN Integration	NEC	discussion
R2-2508593	Discussion on NTN for 6GR	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2508625	NTN Integration in 6G	Ofinno	discussion	Rel-20
R2-2508639	TN/NTN integration in 6G Radio Design	InterDigital	discussion	Rel-20	FS_6G_Radio	Withdrawn
R2-2508659	Considerations on TN/NTN integration for 6GR	Lenovo	discussion	Rel-20
R2-2508703	Essential requirements for NTN and way forward in the common design with TN	Ericsson	discussion	Rel-20	FS_6G_Radio
R2-2508736	Considerations on TN/NTN integration and connected mode  mobility in 6GR	AUMOVIO	discussion
R2-2508777	6G NTN TN Harmonization Requirement	Jio Platforms	discussion	Rel-20	FS_6G_Radio	Revised
R2-2508813	Views on TN NTN integration for 6G	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
R2-2508840	Considerations on TN/NTN integration for 6GR	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2508865	TN/NTN integration in 6G Radio Design	InterDigital, Inc.	discussion	Rel-20
R2-2508869	Discussion on TN-NTN integration for 6G	LG Electronics France	discussion	Rel-20
R2-2508911	Consideration on 6G TN-NTN integration	ZTE Corporation,  Sanechips	discussion	Rel-20
R2-2508933	Discussion on TN/NTN integration	Spreadtrum, UNISOC	discussion	Rel-20
R2-2508999	ANR for NTN-TN integration	LG Uplus	discussion	Late
R2-2509006	Discussion on TN/NTN Integration	TCL	discussion	Rel-20	Withdrawn
R2-2509019	6G NTN TN Harmonization Requirement	Jio Platforms	discussion	Rel-20	FS_6G_Radio	R2-2508777
R2-2509041	Discussion on TN/NTN integration	CSCN	discussion	Rel-20	FS_6G_Radio
R2-2509048	Discussion on TN/NTN Integration and Unification	TCL	discussion	Rel-20
R2-2508416	Overview of 6GR NTN mobility	Amazon Web Services	discussion
moved from 10.4
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.2-a001`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.2 TN/NTN integration

研究 6G radio interface adaptations，以支持涵盖 VLEO、LEO、MEO、GSO 各轨道的实际 NTN 部署场景，并评估 NTN 特性对 initial access timers、HARQ、mobility management 和 paging 等的影响。讨论中 Thales 表示可先从 LEO、MEO 开始，再考虑 VLEO。

```text
Study 6G radio interface adaptations to support practical NTN deployment scenarios across all orbits (VLEO, LEO, MEO, GSO), and evaluate the impact of NTN characteristics (e.g., initial access timers, HARQ, mobility management, paging).
-	Mediatek asks if VLEO will be a common case or whether it should be discussed in RANP.  Thales indicates that we can start with LEO, MEO and later consider VLEO
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.2-p001`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.2 TN/NTN integration

6G radio access 从 Day-1 起应研究适用于 NTN 和 TN 的统一 grant-free initial access mechanism，以及支持 network energy savings 并应对 NTN 特定约束的 control plane signaling。讨论涉及高负载时是否采用 RACH-less，以及 network contention 的需要。

```text
The 6G radio access shall study from Day-1:
•	A unified grant-free initial access mechanism applicable to both NTN and TN.
•	A control plane signaling adapted to support network energy savings and address NTN-specific constraints (e.g. beam hopping techniques, reduced overhead, etc.)
-	Xiaomi asks if for high load we still go for RACH less.   Thales thinks that we need solution that allow faster connection and it also beneficial for TN.  Xiaomi explains that for high load the network needs to do contention.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.2-p002`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.2 TN/NTN integration

6G radio access 从 Day-1 起应允许根据 service 类型和 operating point，在 user plane 层动态激活或停用 retransmission mechanisms（例如 HARQ）。

```text
The 6G radio access shall from Day-1 allow to dynamically activate/deactivate the retransmission mechanisms (e.g., HARQ) at user plane level depending on the type of services and operating point
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.2-p003`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.2 TN/NTN integration

研究支持 UE 在 Idle 和 Connected modes 下从 TN 移动到 NTN、以及从 NTN 移动到 TN 的 6G procedures。讨论说明该研究是一般性的，也可考虑 NTN 到 NTN 的 5G 到 6G 移动。

```text
Study a design for 6G procedures that support mobility from TN to NTN and from NTN to TN for UEs in both Idle and Connected modes.
-	Oppo asks if this is only to 5G or considering 4G as well.   Thales explains this is general but we can consider the NTN to NTN 5G to 6G as well.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.2-p004`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.2 TN/NTN integration

研究支持 6G satellite networks 中 Idle 和 Connected modes 的 NTN-to-NTN mobility mechanisms。研究应涵盖 inter-beam、inter-cell 和 inter-satellite mobility。

```text
Study mobility mechanisms for 6G satellite networks (NTN to NTN), for both idle and connected modes. The study should address:
•	Inter-beam mobility
•	Inter-cell mobility
•	Inter-satellite mobility
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.2-p005`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.2 TN/NTN integration

RAN2 在 6GR study 中按优先级考虑 mobility mechanisms：Time-based 和 Location-based Conditional Handover（CHO）、RACH-less handover、由 MAC 触发的 cell switch mechanism（例如 LTM），以及 group handover。

```text
RAN2 to consider the following mobility mechanisms in 6GR study, in order of priority:
•	Time-based and Location-based Conditional Handover (CHO)
•	RACH-less handover
•	Cell switch mechanism triggered by MAC (e.g. LTM)
•	Group handover
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.2-p006`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.2 TN/NTN integration

讨论了 6G NTN 的基本假设和功能分类，包括 common essential features、NTN specific essential features 与 NTN specific optional features。建议 common essential features 从 Day 1 起采用 TN 和 NTN 的 harmonized design，NTN specific essential features 可讨论是否从 Day 1 支持，NTN specific optional features 可留待后续 release；具体功能范围仍有不同意见。

```text
Study the following essential NTN capabilities for supporting NTN services in 6G:
•	NTN based positioning mechanisms for Positioning, Navigation, and Timing services.
•	Network verified UE location for regulatory services
•	Geo-fencing (e.g. intended service area) for Broadcast, multicast and PWS.
[4 min]
Noted
R2-2508295	Discussion on TN and NTN integration	OPPO	discussion	Rel-20	FS_6G_Radio
Proposal 1	The basic assumption in 5G NTN, e.g., NTN scenarios, payload type, etc., can be adopted in 6G NTN and UE without GNSS capability can also be studied in 6G NTN.
-	Mediatek asks if this means GNSS resilient.
-	Vivo asks if it is both GNSS and without GNSS.  Oppo thinks with should be studied, the discussion is more for the case without GNSS
-	Apple thinks that for RAN2 we should start with GNSS and without we need RAN1 first.
Proposal 2	Define 3 types of features for NTN/TN feature discussions: common essential features, NTN specific essential features and NTN specific optional features.
-	Mediatek thinks it is a good idea to have categorizations.  For common it should be common but with some NTN small optimization.
-	CMCC thinks that all features apply to NTN.  WE should think with NTN features also apply to TN.
-	Interdigital thinks that it makes sense and proposal 6 describes what it is.
-	Qualcomm thinks that we should design TN functionalities and identify what needs to be extended, and those would be common.
-	Sharp thinks we can use this words temporarily but then later revisit, as we may have some things that are NTN specific like ephemeris free but at the end we want the design to be common.
Proposal 3	In 6G NTN, RAN2 consider the following features as common essential features:
Proposal 4	In 6G NTN, RAN2 considers the following features as NTN specific essential features:
-	NTN specific SIB acquisition;
-	Mediatek asks why this is separate, shouldn’t we have a common design.  Thales and Google agrees.
-	Satellite switch with re-sync;
-	ZTE thinks that this is like a group mobility and there may be cases that may be applicable for TN.
-	Ericsson thinks that we don’t know if this is need.  Chair explains that could be concluded that it is not needed as part of study.  Nokia thinks that we need to understand 6G first.
-	Huawei thinks that location based should be NTN specific.  CMCC thinks that location based can be considered common as it may be applicable to both TN and NTN.
-	Uplink time and frequency pre-compensation;
-	Vivo asks why this is in RAN2.  Google thinks that calculation of TA is RAN2.  Xiaomi thinks that RAN1 specifies everything.
-	Discontinuous coverage;
-	Qualcomm and Xiaomi don’t think this should be in the scope as it is for IoT NTN
-	Novamint thinks that this is an essential feature missing.   Amazon also thinks this is important to study.    Nokia agrees as we might not have coverage from day 1.   Interdigital thinks that we need to add store and forward.
-	Samsung thinks that we should assume we have connectivity in 6G.   Interdigital thinks that just like TN it takes time before we have full coverage.  Huawei agrees, initially we have sparse deployment.
-	Oppo also sees benefits to this feature.
-	Qualcomm thinks that this should be a plenary discussion.
Proposal 5	In 6G NTN, the following features belong to specific optional features which can be considered later:
-	MBS broadcast and multicast via NTN;
-	Dual connection;
-	Carrier Aggregation.
Proposal 6	In 6G NTN, RAN2 can handle the defined three NTN feature categories with the follow principle:
-	for common essential features, consider the harmonized design for TN and NTN since day1;
-	for NTN specific essential features, can be discussed whether support them since day1;
-	for NTN specific optional features, can be discussed in later release.
[4 min]
Noted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.2-p007`

### [6G/Rel-20 RAN1#126] `agreement` 10.7.1 NTN specific requirements and design

针对 6GR NTN 的 GNSS-less/free/degraded PRACH，研究以 TR 38.742 记录的差分时间和频率误差为目标，并增加 S-band LEO-300 与 Ka-band LEO-300 场景。场景细节（包括差分时间/频率误差）仍待确定（FFS）。

```text
For 6GR NTN GNSS-less/free/degraded PRACH, the differential time and frequency errors documented in TR 38.742 are taken as targets for the study with the addition of at least the following scenarios:
S-band LEO-300
Ka-band LEO-300
FFS: details of these scenarios, including differential time/frequency errors
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.7.1-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.7.1 NTN specific requirements and design

修正了 RAN1#125 关于 6GR NTN SSB 的 LLS 假设：SSB 覆盖评估的 periodicity 待报告，性能指标为 PSS/SSS 的 1% missed detection、0.1% false alarm rate，以及 PBCH 的 1% BLER；UE 不假设知道 SS/PBCH block index。公司需报告合并的 SSB 分量及数量（如有）、single-shot 检测，以及其他参数；CFO 和 timing drift 必须报告。

```text
The RAN1#125 agreement on LLS assumptions for SSB in 6GR NTN is corrected as follows:
The following parameters are used to evaluate SSB coverage for the 6GR NTN link budget template:
NOTE: Structure of NR signals / channels and other functionalities/features can be initially used for evaluation until other agenda items progress on the 6GR signals / channel structure/functionalities/features.
| Periodicity | To be reported |
| --- | --- |
| Performance metric | 1% missed detection with 0.1% false alarm rate for PSS/SSS. 1% BLER for PBCH. Performance metric for different component physical channels / signals within the SSB (i.e., PSS, SSS, PBCH) can be separately reported Note: UE is not assumed to know the SS/PBCH block index |
| SSB combining | Companies to report which component physical channels / signals within the SSB (i.e., PSS, SSS, PBCH) are combined, and how many SSBs are combined (if any). Single-shot SSB detection is also reported. |
| Other parameters | Reported by companies (including maximum CFO and timing drift rate (us/s) assumed, combining algorithm, etc). CFO and timing drift are mandatorily reported. |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.7.1-a002`

### [6G/Rel-20 RAN1#126] `agreement` 10.7.1 NTN specific requirements and design

在 6GR NTN link budget template 的 Ka/Ku band PDSCH 和 PUSCH link level evaluations 中，PT-RS configuration 为可选项；若公司将其纳入评估，需报告。

```text
For the 6GR NTN link budget template, for Ka/Ku band PDSCH and PUSCH link level evaluations, the PT-RS configuration is optional, and reported by companies if considered.
R1-2606420	Feature lead summary#3 on NTN specific requirements and design	Moderator (Qualcomm Incorporated)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.7.1-a003`

### [6G/Rel-20 RAN1#126] `agreement` 10.7.1 NTN specific requirements and design

对于 6GR NTN link budget template 的 Ka/Ku band link level evaluations，BPSK/QPSK 可选用 TR38.803 第 6.1.11.2 条的 UE 和 SAN phase noise model，并在使用时由公司报告。若评估更高阶调制，则使用该模型；此约定仅适用于 6GR NTN link budget template。

```text
For the 6GR NTN link budget template, for Ka/Ku band link level evaluations, the UE and SAN phase noise model in clause 6.1.11.2 of TR38.803 can be optionally used for BPSK/QPSK (and in that case is reported by companies) and is used for higher order modulation (if evaluated for the link budget template)
NOTE: This agreement only applies to the 6GR NTN link budget template.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.7.1-a004`

### [6G/Rel-20 RAN1#126] `agreement` 10.7.1 NTN specific requirements and design

6G NTN link budget template 至少评估表列的 S-band、Ka band 和 Ku band 场景，包括指定的 LEO、MEO、GEO 高度、仰角、beam edge 及 Outdoor 条件；部分 S-band LEO 场景还列有可选 APC。上述场景不假设 wide beam operation；公司可在相应主题提供 wide-beam 链路预算，也可提交表列以外场景的结果。

```text
For the link budget template of 6G NTN, at least the following scenarios are evaluated
NOTE: APC = “Adverse propagation conditions”
|  | LEO 300 | LEO 600 | LEO 1200 | MEO 7000 | GEO |
| --- | --- | --- | --- | --- | --- |
| S-band | 1) 30deg, beam edge, Outdoor 2) 30deg, beam edge, APC (Optional) | 1) 30deg, beam edge, Outdoor 2) 30deg, beam edge, APC (Optional) | N/A | 1) 30deg, beam edge, Outdoor | 1) 12.5deg, beam edge, Outdoor |
| Ka band | N/A | 1) 30deg, beam edge, Outdoor |  | N/A | 1) 12.5deg, beam edge, Outdoor |
| Ku band | N/A | N/A | 1) 30deg, beam edge, Outdoor | N/A | 1) 12.5deg, beam edge, Outdoor |
NOTE: In the scenarios above, no “wide beam” operation is assumed. The link budget for wide-beam operation can be provided by companies in the corresponding topic. The beam edge diameter is according to the agreed tables.
NOTE: If companies provide results for other scenarios than mentioned above, the corresponding results can be captured in link budget summary table.
R1-2606422	Feature lead summary#5 on NTN specific requirements and design	Moderator (Qualcomm Incorporated)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.7.1-a005`

### [6G/Rel-20 RAN1#126] `agreement` 10.7.1 NTN specific requirements and design

6GR NTN 的多卫星物理层研究中，将研究与星间干扰管理相关的同频干扰，并考虑 NTN 信道特性（如轨道动态导致的大且时变的 Doppler / timing offsets）。至少研究 LEO 同轨情形；其他参数（如 elevation angle）待定，并假设 UE 同一时刻仅连接一颗卫星。

```text
In 6GR NTN, under the label of “physical layer aspects of multi-satellite operation”, the following sub-aspects are studied under “physical layer aspects related to inter-satellite interference management”
Co-channel interference, taking into account characteristics of NTN channels (e.g. large and time-varying Doppler / timing offsets due to orbital dynamics)
At least for LEO same orbit.
FFS other parameters (e.g. elevation angle)
NOTE: It is assumed that the UE is only connected to one satellite at a time.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.7.1-a006`

### [6G/Rel-20 RAN1#126] `conclusion` 10.7.1 NTN specific requirements and design

6GR NTN GNSS-less/free/degraded PRACH 研究将在 common agenda item 中开展，并考虑 NTN specific agenda item（AI 10.7.1.）制定的 NTN requirements。若 common agenda item 的设计不满足 NTN requirements，可在 NTN specific agenda item 下制定 NTN specific adjustments。

```text
For the 6GR NTN GNSS-less/free/degraded PRACH study:
The study is conducted in common agenda item, taking into account the NTN requirements which are developed under NTN specific agenda item (i.e. AI 10.7.1.).
This does not preclude NTN specific adjustments to the common design if needed, which may be developed under NTN specific agenda item (i.e. AI 10.7.1) if the design from the common agenda item does not meet the NTN requirements.
[Post-126-6GR-NTN]
Email discussion on 6GR NTN requirements for GNSS-less/free/degraded PRACH (Aug 31st to Sept. 3rd).
R1-2606419	Feature lead summary#2 on NTN specific requirements and design	Moderator (Qualcomm Incorporated)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.7.1-c001`

### [6G/Rel-20 RAN1#126] `observation` 10.7.1 NTN specific requirements and design

RAN1 认为 Solution 1（HARQ feedback disabling）和 Solution 3（aNB 在收到前次 HARQ-ACK 前复用同一 HARQ process）均可行；Solution 1 已在 NR Rel-17 规定，Solution 3 受 UE out-of-order rules 限制，且现行 RAN2 规范在某些情形下可能阻止该行为。各方对两种方案的信令开销、UE 功耗、重传恢复和链路自适应影响存在不同意见；两者被认为可行不决定最终是否规定及采用哪种方案。

```text
On the issue of HARQ stalling, the following observations are drawn:
On Solution 1 (HARQ feedback disabling) and Solution 3 (aNB reusing the same HARQ process before receiving HARQ-ACK feedback for the previous transmission):
RAN1 observes that solution 1 was specified in NR Rel-17, and it is clarified in TS 38.300 that “Disabling HARQ feedback allows scheduling a HARQ process before one HARQ RTT has elapsed since last scheduled”. This solution is feasible from RAN1 perspective
From RAN1 perspective, regarding Solution 3, it is feasible to allow usage of the same HARQ process before the HARQ-ACK feedback has been processed by the base station (subject to out-of-order rules at the UE). Current RAN2 specifications for NR, however, may prevent this behavior at least in some cases (e.g. when DRX is configured).
Under solution 3, having HARQ-ACK feedback for every downlink transmission incurs in signaling overhead and corresponding UE power consumption, which is considered by some companies to be unacceptable for some NTN scenarios. Solution 1 would alleviate this issue.
Some companies indicate that the UE power consumption and overhead associated with HARQ-ACK transmission is limited, and that solution 1 removes the information on successful or unsuccessful reception of the TB and may result in recovery through RLC retransmissions which would increase signaling overhead, latency and corresponding UE power consumption. This assumes that, under solution 3, HARQ-ACK information is used for ARQ retransmissions without relying on RLC status report.
Some companies indicate that although Solution 3 does not remove the information on successful or unsuccessful reception of the TB, it will not be useful for triggering HARQ retransmissions, and therefore with solution 3 there is also a possibility of ending up in recovery through RLC retransmissions. This assumes that, under solution 3, HARQ-ACK information is not used for ARQ retransmissions without relying on RLC status report.
Under solution 3, although HARQ-ACK feedback is not used for HARQ retransmissions, some companies indicate that the HARQ-ACK information can be useful for e.g. link adaptation. Some other companies indicate that similar information can be conveyed in an alternative manner (e.g. statistical reporting, dynamic enabling/disabling of HARQ feedback under Solution 1, or disabling of HARQ feedback for some of the HARQ processes).
Some companies indicate that the potential benefits of solution 1 in terms of signaling efficiency and power consumption are not directly related to HARQ stalling. Some companies indicate that solution 1 has been specified in NR to solve the problem of HARQ stalling.
NOTE: The fact that solution 3 and solution 1 are deemed to be “feasible” has no impact on which solution (if any) would be specified.
R1-2606421	Feature lead summary#4 on NTN specific requirements and design	Moderator (Qualcomm Incorporated)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.7.1-o001`

### [6G/Rel-20 RAN1#126] `working_assumption` 10.7.1 NTN specific requirements and design

6GR NTN Ka/Ku-band link budget template 采用列明的 atmospheric loss 和 scintillation loss 数值，并设 shadow fading margin 为 0、polarization loss 为 0 dB、receiver implementation margin 为 1 dB、penetration margin 与 other losses 为 0 dB。扫描损耗按 elevation angle 和天线单元方向图增益计算；相关损耗不含雨衰，且研究特定场景不代表将研究或规定如何弥补可能的覆盖缺口。

```text
On the link budget template for 6GR NTN, the following values are used for Ka and Ku-band:
“(28a) Atmospheric loss (dB)”
For Ka-band GEO 20GHz (12.5 degree elevation): 1.2dB
For Ka band GEO 30GHz (12.5 degree elevation): 1.1dB
For Ku band GEO (12.5 degree elevation): 0.2dB
For Ka-band LEO (30 degree elevation): 0.5dB
For Ku-band LEO (30 degree elevation): 0.1dB
NOTE: These losses do not include rain loss. The values are obtained from ITU P.676 figures.
“(28b) Shadow fading margin (dB)” = 0
“(28c) Scintillation loss (dB)”
For GEO (12.5 degree elevation) Ka band, 1.1dB
For LEO (30 degree elevation) Ka band, 0.3dB
For GEO (12.5 degree elevation) Ku band, 0.3dB
For LEO (30 degree elevation) Ku band, 0.2dB
NOTE: This scintillation loss is due to tropospheric scintillation, as described in TR 38.811.
“(28d) Polarization loss (dB)” = 0dB
This is due to matching polarizations between UE and SAN antenna
“(4b-2) / (11-b2) Scanning loss (dB)” is
Calculated based on elevation angle and antenna element pattern gain for both SAN and UE (if they use antenna arrays)
NOTE: RAN1 might need to revisit the agreed antenna element pattern gain.
“(20) Receiver implementation margin (dB)” = 1dB
“(27) Penetration margin” = 0dB
“(28e) Other losses” = 0dB
NOTE: The study of a particular scenario for the link budget template does not imply that, if RAN1 determines a coverage gap for that scenario, it will be studied or specified how to close it.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.7.1-w001`

### [6G/Rel-20 RAN1#126] `working_assumption` 10.7.1 NTN specific requirements and design

6GR NTN MEO-7000 S-band 下行和上行采用表列参数，包括每波束最大带宽 5 MHz、参考波束大小 160 km、2774 个波束覆盖区及 48 个同时激活波束（1.73%）。天线参数采用 fully connected TXRU mapping，并列出相控阵或反射面天线配置、circular 极化建模及 41.08 dB 的整体天线增益。

```text
For 6GR NTN MEO-7000 S-band, the following parameters are adopted:
For downlink:
|  | MEO-7000 |
| --- | --- |
| Maximum Bandwidth per beam | 5MHz |
| Beam size (note 1) | 160km |
| Satellite EIRP density /beam (dBW/MHz) | 44 |
| Payload Total DL power level (dBW) | 26.72 |
| Aggregated EIRP (Total) (dBW) | 67.81 |
| Satellite Tx max Gain | 41.08 dBi |
| Maximum EIRP per Satellite beam (dBW) | 51 |
| Total number of beam footprints | 2774 |
| Total number of simultaneously active beams | 48 |
| % simultaneously active beams* | 1.73% |
| Note 1: Reference beam size, different beam sizes may be evaluated and reported by companies (for e.g. hierarchical beam structure) |  |
For uplink:
|  | MEO-7000 |
| --- | --- |
| Maximum Bandwidth per beam | 5 MHz |
| Beam size (note 1) | 160km |
| Satellite Rx max Gain | 41.08 dBi |
| Satellite max G/T | 12.18 dB/K |
| Total number of beam footprints | 2774 |
| Total number of simultaneously active beams* | 48 |
| % simultaneously active beams* | 1.73% |
| Note 1: Reference beam size, different beam sizes may be evaluated and reported by companies (for e.g. hierarchical beam structure) |  |
Antenna parameters:
| Frequency | S-band (i.e., 2 GHz) |
| --- | --- |
| Orbit | MEO-7000 |
| TXRU mapping (for phased antenna array) | Fully connected |
| Satellite antenna configurations Option 1: Phased antenna array i.e. (M,N,P,Mg,Ng; Mp, Np), (dH,dV), (dg,H,dg,V) if any (M, N, P, Mg, Ng; Mp, Np) - M: Number of vertical antenna elements within a panel, on one polarization - N: Number of horizontal antenna elements within a panel, on one polarization - P: Number of polarizations - Mg: Number of panels in a column; - Ng: Number of panels in a row; - Mp: Number of vertical TXRUs within a panel, on one polarization - Np: Number of horizontal TXRUs within a panel, on one polarization Note: Mp and Np may not be applicable for fully-connected TXRU. Option 2: Reflector antenna | Antenna elements: 8100 (90x90) Separation: 0.5 lambda Number of polarizations: 1 or 2. 1-pol: (M,N,P,Mg,Ng)= (90, 90, 1, 1, 1), , (dH,dV) = (0.5, 0.5) 2-pol: (M,N,P,Mg,Ng) = (90, 90, 2, 1, 1), (dH,dV) = (0.5, 0.5) |
| Satellite Polarized antenna modelling e.g., models in section 7.3.2 in TR38.901 | Circular |
| Satellite antenna element gain pattern | Table 7.3-1 in TR 38.901 Horizontal/vertical 3 dB beam width of single element (degree): 90 for H, 90 for V Element max directivity: 5dBi. An antenna efficiency of 50% is assumed which results in an effective element max gain of 2dB. The resulting overall antenna gain (after applying the array factor) is 41.08dB |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.7.1-w002`

### [6G/Rel-20 RAN1#126] `working_assumption` 10.7.1 NTN specific requirements and design

6GR NTN LEO-1200 Ku-band 采用 G/T = 6 dB/K、每波束 EIRP density = 13 dBW/MHz。天线参数采用 fully connected TXRU mapping，并列出 1296 个天线单元的反射面配置、circular 极化建模及 33.126 dB 的整体天线增益。

```text
For  6GR NTN LEO-1200 Ku-band, the following parameters are adopted
G/T = 6dB/K
EIRP density per beam = 13dBW/MHz
Antenna parameters:
| Frequency | Ku-band |
| --- | --- |
| Orbit | LEO-1200 |
| TXRU mapping (for phased antenna array) | Fully connected |
| Satellite antenna configurations Option 1: Phased antenna array i.e. (M,N,P,Mg,Ng; Mp, Np), (dH,dV), (dg,H,dg,V) if any (M, N, P, Mg, Ng; Mp, Np) - M: Number of vertical antenna elements within a panel, on one polarization - N: Number of horizontal antenna elements within a panel, on one polarization - P: Number of polarizations - Mg: Number of panels in a column; - Ng: Number of panels in a row; - Mp: Number of vertical TXRUs within a panel, on one polarization - Np: Number of horizontal TXRUs within a panel, on one polarization Note: Mp and Np may not be applicable for fully-connected TXRU. Option 2: Reflector antenna | Antenna elements: 1296 (36x36) Separation: 0.5 lambda Number of polarizations: 1 or 2. 1-pol: (M,N,P,Mg,Ng)= (36, 36, 1, 1, 1), (dH,dV) = (0.5, 0.5) 2-pol:(M,N,P,Mg,Ng) = (36, 36, 2, 1, 1), (dH,dV) = (0.5, 0.5) |
| Satellite Polarized antenna modelling e.g., models in section 7.3.2 in TR38.901 | Circular |
| Satellite antenna element gain pattern | Table 7.3-1 in TR 38.901 Horizontal/vertical 3 dB beam width of single element (degree): [90] for H, 90 for V Element max directivity: 5dBi. An antenna efficiency of 50% is assumed which results in an effective element max gain of 2dB. The resulting overall antenna gain (after applying the array factor) is 33.126dB |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.7.1-w003`

### [6G/Rel-20 RAN1#126] `working_assumption` 10.7.1 NTN specific requirements and design

6GR NTN Ka/Ku-band UE 天线采用 12 cm 配置，TXRU mapping 为 fully connected；表中分别列出 Ka-band 256 个、Ku-band 81 个天线单元的反射面配置。两种配置均采用 circular 极化建模，整体天线增益分别为 26.08 dB 和 21.08 dB；更大天线的额外参数将在后续会议讨论。

```text
For 6GR NTN Ka and Ku-band UE antenna assumptions, the following parameters are adopted:
NOTE: An additional set of parameters for a Ka and Ku band UEs with a larger antenna will be also adopted, details to be discussed in the next meeting.
| Frequency | Ka-band (12cm) | Ku-band (12cm) |
| --- | --- | --- |
| TXRU mapping (for phased antenna array) | Fully connected | Fully connected |
| Satellite antenna configurations Option 1: Phased antenna array i.e. (M,N,P,Mg,Ng; Mp, Np), (dH,dV), (dg,H,dg,V) if any (M, N, P, Mg, Ng; Mp, Np) - M: Number of vertical antenna elements within a panel, on one polarization - N: Number of horizontal antenna elements within a panel, on one polarization - P: Number of polarizations - Mg: Number of panels in a column; - Ng: Number of panels in a row; - Mp: Number of vertical TXRUs within a panel, on one polarization - Np: Number of horizontal TXRUs within a panel, on one polarization Note: Mp and Np may not be applicable for fully-connected TXRU. Option 2: Reflector antenna | Antenna elements: 256 (16x16) Separation: 0.5 lambda Number of polarizations: 1 or 2. 1-pol: (M,N,P,Mg,Ng)= (16, 16, 1, 1, 1), (dH,dV) = (0.5, 0.5) 2-pol:(M,N,P,Mg,Ng) = (16, 16, 2, 1, 1), (dH,dV) = (0.5, 0.5) | Antenna elements: 81 (9x9) Separation: 0.5 lambda Number of polarizations: 1 or 2. 1-pol: (M,N,P,Mg,Ng)= (9, 9, 1, 1, 1), (dH,dV) = (0.5, 0.5) 2-pol:(M,N,P,Mg,Ng) = (9, 9, 2, 1, 1), (dH,dV) = (0.5, 0.5) |
| Satellite Polarized antenna modelling e.g., models in section 7.3.2 in TR38.901 | Circular | Circular |
| Satellite antenna element gain pattern | Table 7.3-1 in TR 38.901 Horizontal/vertical 3 dB beam width of single element (degree): [90] for H, 90 for V Element max directivity: 5dBi. An antenna efficiency of 50% is assumed which results in an effective element max gain of 2dB. The resulting overall antenna gain (after applying the array factor) is 26.08dB | Table 7.3-1 in TR 38.901 Horizontal/vertical 3 dB beam width of single element (degree): [90] for H, 90 for V Element max directivity: 5dBi. An antenna efficiency of 50% is assumed which results in an effective element max gain of 2dB. The resulting overall antenna gain (after applying the array factor) is 21.08dB |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.7.1-w004`

### [6G/Rel-20 RAN1#126] `working_assumption` 10.7.1 NTN specific requirements and design

6GR NTN S-band link budget template 采用 atmospheric loss、shadow fading margin、scintillation loss 和 polarization loss 的列明数值，接收机实现余量为 1 dB，penetration margin 为 0 dB；扫描损耗按 elevation angle 和天线单元方向图增益计算。APC 的 other losses 设为 6–15 dB，具体值将在下次会议根据公司输入决定，且 APC 仅评估下行广播信道/信号。

```text
On the link budget template for 6GR NTN, the following values are used for S-band:
“(28a) Atmospheric loss (dB)” = 0.1dB for LEO 30 degree elevation and 0.2dB for GEO 12.5 degree
“(28b) Shadow fading margin (dB)” = 3dB
Note: Additional losses due to e.g. light indoor/in-vehicle penetration loss may be considered under APC.
“(28c) Scintillation loss (dB)” = 2.2dB
This is for the evaluated elevation angles.
“(28d) Polarization loss (dB)” = 3dB
Assumes SAN antenna is circularly polarized and UE antenna is linearly polarized
“(4b-2) /  (11-b2) Scanning loss (dB)” is
Calculated based on elevation angle and antenna element pattern gain, e.g. ~4dB for 30 degree elevation angle in LEO 600, if the SAN antenna is modeled as an array.
NOTE: RAN1 might need to revisit the agreed antenna element pattern gain.
For UEs with omni antennas (11a)/(4c) “Boresight Antenna gain” is set to
-5.5dB as baseline.
0dB can be considered optionally.
“(20) Receiver implementation margin (dB)” = 1dB
“(27) Penetration margin” = 0dB
Note: Losses due to e.g. light indoor/in-vehicle penetration loss may be considered under APC.
“(28e) Other losses”: is set to:
For outdoor UEs, 0dB
For UEs in adverse propagation condition (APC): [a value between 6dB and 15dB]
This value will be decided in the next meeting based on input from companies (values and associated scenarios).
APC is only evaluated for downlink broadcast channel / signals.
NOTE: UEs in adverse propagation conditions is per RAN guidance and is documented in TR 38.914 as 0% of users in Case 1 and 4% of users in Case 2.
NOTE: The study of a particular scenario for the link budget template does not imply that, if RAN1 determines a coverage gap for that scenario, it will be studied or specified how to close it.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.7.1-w005`

### [6G/Rel-20 RAN1#124b] `agreement` 10.7.1 NTN specific requirements and design for GNSS based operation

针对NTN中大RTT导致的HARQ stalling，研究HARQ feedback disabling、跨多个slot的PDSCH/PUSCH传输、aNB在收到前次HARQ-ACK前复用同一HARQ process，以及增加HARQ processes等方案及其适用性。上述方案可组合，是否与TN协调仍待确定。

```text
For the issue of HARQ stalling due to large RTT in NTN, study the following solutions (which may or may not have specification impact), including their applicability:
Solution 1: HARQ feedback disabling.
Solution 2: PDSCH / PUSCH transmissions that span multiple slots.
Solution 3: aNB reusing the same HARQ process before receiving HARQ-ACK feedback for the previous transmission
Solution 4: Sufficient number of HARQ processes
Note: Combination of solutions above can be considered.
FFS: Whether the above techniques can be harmonized with TN
R1-2603091	Feature lead summary#2 on NTN specific requirements and design for GNSS based operation	Moderator (Qualcomm Incorporated)
From Tuesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.7.1-a001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.7.1 NTN specific requirements and design for GNSS based operation

6GR NTN采用R1-2603091所附的link budget template；“Candidate 2”不纳入NTN考虑。

```text
For 6GR NTN, the link budget template attached to R1-2603091 is endorsed.
Note: “Candidate 2” is not considered for NTN.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.7.1-a002`

### [6G/Rel-20 RAN1#124b] `agreement` 10.7.1 NTN specific requirements and design for GNSS based operation

针对NTN卫星beam footprints多于同时激活beams的问题，研究default SSB periodicity的取值及hierarchical beam structure（例如采用不同尺寸的beams），并评估可实现的卫星覆盖比例和适用性。

```text
In 6GR NTN, for the issue of satellite having more beam footprints than simultaneously active beams, study the following solutions, including their achievable coverage ratio of satellite and applicability:
Value of default SSB periodicity
Hierarchical beam structure (e.g. using beams of various sizes)
R1-2603093	Feature lead summary#3 on NTN specific requirements and design for GNSS based operation	Moderator (Qualcomm Incorporated)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.7.1-a003`

### [6G/Rel-20 RAN1#124b] `agreement` 10.7.1 NTN specific requirements and design for GNSS based operation

6GR NTN study至少考虑FD-FDD和UE侧HD-FDD两种duplex types。主会另列出Semi-static TDD、gNB semi-static SBFD和Dynamic TDD等6GR duplexing study类型。

```text
For 6GR NTN study, RAN1 considers at least the following duplex types:
FD-FDD.
HD-FDD on UE side.
| Note the following is agreed in main session: On 6GR duplexing study, RAN1 considers at least following duplex types • FD-FDD • Semi-static TDD • gNB semi-static SBFD • HD-FDD on UE side • Dynamic TDD |
| --- |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.7.1-a004`

### [6G/Rel-20 RAN1#124b] `agreement` 10.7.1 NTN specific requirements and design for GNSS based operation

6GR NTN的“physical layer aspects of multi-satellite operation”至少研究与mobility及inter-satellite interference management相关的物理层方面及其适用性，干扰管理技术细节待定。上述两方面假设UE一次只连接一颗卫星，并预期mobility主题与RAN2协调。

```text
In 6GR NTN, under the label of “physical layer aspects of multi-satellite operation”, at least the following aspects are studied, including its applicability:
Physical layer aspects related to mobility
NOTE: Coordination with RAN2 is expected for this topic, and for some aspects RAN1 may need to wait for RAN2 to progress before discussing in RAN1.
NOTE: Companies can bring proposals on physical layer related issues related to mobility at different layers (e.g. L1/L2/L3) under this topic, and physical layer aspects of satellite selection and satellite switch.
Physical layer aspects related to inter-satellite interference management.
FFS: Details of interference management techniques.
NOTE: Companies can bring proposals on physical layer related issues related to inter-satellite interference management.
NOTE: For the two aspects above it is assumed that the UE is only connected to one satellite at a time.
NOTE: Under the label of “Multi-satellite operation” RAN1 discusses topics involving multiple satellites which may be in the same or different orbits/altitudes. Companies may bring further aspects (other than the two aspects above) under this label in future RAN1 meetings.
R1-2603362	Feature lead summary#4 on NTN specific requirements and design for GNSS based operation	Moderator (Qualcomm Incorporated)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.7.1-a005`

### [6G/Rel-20 RAN1#124b] `agreement` 10.7.1 NTN specific requirements and design for GNSS based operation

6GR NTN评估中，S-band至少为link budget计算增加MEO-7000轨道。

```text
For 6GR NTN evaluations, consider the following additional orbit for S-band, at least for link budget calculation purposes:
MEO-7000
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.7.1-a006`

### [6G/Rel-20 RAN1#124b] `agreement` 10.7.1 NTN specific requirements and design for GNSS based operation

为实现较大的scheduling offsets，6GR NTN原则上支持以NR的k_offset概念为基线并允许潜在修改，且至少支持广播k_offset。是否支持UE-specific k_offset仍待确定；若6GR不定义K1/K2等概念或其调度设计已覆盖NTN RTT范围，该协议可能修订。

```text
For 6GR NTN, for realizing large scheduling offsets, the following is supported in principle:
Reuse the k_offset concept from NR as a baseline with potential modifications.
NOTE: Under this option, additional scheduling offsets (e.g. similar to K1/K2 in NR) are assumed to be supported for scheduling flexibility, which apply in addition to k_offset.
At least broadcast (FFS whether cell or beam specific) k_offset is supported.
FFS whether UE-specific k_offset is supported.
NOTE: This agreement may be revised if 6GR does not define concepts such as K1/K2, or if the baseline design of 6GR scheduling can already cover the RTT range of NTN.
R1-2603363	Feature lead summary#5 on NTN specific requirements and design for GNSS based operation	Moderator (Qualcomm Incorporated)
From Friday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.7.1-a007`

### [6G/Rel-20 RAN1#124b] `agreement` 10.7.1 NTN specific requirements and design for GNSS based operation

RAN1将研究TA report对6GR NTN是否有益。

```text
For 6GR NTN, RAN1 to study whether TA report is beneficial.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.7.1-a008`

### [6G/Rel-20 RAN1#124b] `agreement` 10.7.1 NTN specific requirements and design for GNSS based operation

针对 6GR NTN 的 GNSS-based operation，研究 UL time-frequency pre-compensation 所需的 satellite assistance info 参数，并以 NR NTN 的 SIB19 参数为起点。

```text
For 6GR NTN, at least for GNSS-based operation, study which parameters are needed for satellite assistance info for UL time-frequency pre-compensation, considering NR NTN parameters in SIB19 as starting point.
R1-2603364	Final feature lead summary on NTN specific requirements and design for GNSS based operation	Moderator (Qualcomm Incorporated)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.7.1-a009`

### [6G/Rel-20 RAN1#124b] `conclusion` 10.7.1 NTN specific requirements and design for GNSS based operation

6GR NTN link budget template 针对 reflector antenna、phased arrays 和 UT omni antennas 给出了 antenna virtualization mode 的示例设置，涵盖 antenna gain element、scanning loss、loss to beam edge 及元素数与模拟数的关系。上述设置适用于 template 的 Transmitter 部分，Receiver 部分使用相同的 antenna virtualization mode。

```text
For the 6GR NTN link budget template, for the purpose of illustration the following figure and text describe how the assumed antenna virtualization mode can be used for different antenna types:
For reflector antenna:
Antenna gain element (4c) captures the overall antenna gain
Scanning loss (4b-2) =0
Loss to beam edge (4b-1) can be set for the satellite and may depend on the elevation angle
(1) = (2) (same # of elements as simulated)
For phased arrays:
Antenna gain element (4c) captures the per-element antenna gain
Scanning loss (4b-2) can be set according to the elevation angle
Loss to beam edge (4b-1) can be set for the satellite and may depend on the elevation angle
(2) is the number of simulated chains in LLS (either 1 or 2). (1) is the total number of antenna elements.
For UT transmitters with omni antennas
Antenna gain element (4c) captures the overall antenna gain
Scanning loss (4b-2) =0
Loss to beam edge (4b-1) = 0
(1) = (2) (same # of elements as simulated)
NOTE: The above is for the “Transmitter” part of the 6GR NTN link budget template, the same antenna virtualization mode is used for the “Receiver” part of the 6GR NTN link budget template.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.7.1-c001`

### [6G/Rel-20 RAN1#124b] `working_assumption` 10.7.1 NTN specific requirements and design for GNSS based operation

针对 S-band（2 GHz）LEO-600 和 LEO-300，采用 SAN antenna model 假设：phased antenna array 使用 fully connected TXRU mapping，卫星天线配置可为 phased antenna array 或 reflector antenna。两种轨道的天线元素数分别为 1296 和 400，整体天线增益分别为 33.126 dB 和 28.02 dB；link budget template 中需计入 50% efficiency。

```text
For 6GR NTN, for S-band LEO-600 and LEO-300, the following assumption for SAN antenna model is adopted:
Other separate assumptions may be further considered for e.g. other satellite payload types.
| Frequency | S-band (i.e., 2 GHz) | S-band (i.e., 2 GHz) |
| --- | --- | --- |
| Orbit | LEO-600 | LEO-300 |
| TXRU mapping (for phased antenna array) | Fully connected | Fully connected |
| Satellite antenna configurations Option 1: Phased antenna array i.e. (M,N,P,Mg,Ng; Mp, Np), (dH,dV), (dg,H,dg,V) if any (M, N, P, Mg, Ng; Mp, Np) - M: Number of vertical antenna elements within a panel, on one polarization - N: Number of horizontal antenna elements within a panel, on one polarization - P: Number of polarizations - Mg: Number of panels in a column; - Ng: Number of panels in a row; - Mp: Number of vertical TXRUs within a panel, on one polarization - Np: Number of horizontal TXRUs within a panel, on one polarization Note: Mp and Np may not be applicable for fully-connected TXRU. Option 2: Reflector antenna | Antenna elements: 1296 (36x36) Separation: 0.5 lambda Number of polarizations: 1 or 2. 1-pol: (M,N,P,Mg,Ng)= (36, 36, 1, 1, 1), (dH,dV) = (0.5, 0.5) 2-pol:(M,N,P,Mg,Ng) = (36, 36, 2, 1, 1), (dH,dV) = (0.5, 0.5) | Antenna elements: 400 (20x20) Separation: 0.5 lambda Number of polarizations: 1 or 2. 1-pol: (M,N,P,Mg,Ng)= (20, 20, 1, 1, 1), , (dH,dV) = (0.5, 0.5) 2-pol: (M,N,P,Mg,Ng) = (20, 20, 2, 1, 1), (dH,dV) = (0.5, 0.5) |
| Satellite Polarized antenna modelling e.g., models in section 7.3.2 in TR38.901 | Circular | Circular |
| Satellite antenna element gain pattern | Table 7.3-1 in TR 38.901 Horizontal/vertical 3 dB beam width of single element (degree): [90] for H, 90 for V Element max directivity: 5dBi. An antenna efficiency of 50% is assumed which results in an effective element max gain of 2dB. The resulting overall antenna gain (after applying the array factor) is 33.126dB | Table 7.3-1 in TR 38.901 Horizontal/vertical 3 dB beam width of single element (degree): [90] for H, 90 for V Element max directivity: 5dBi. An antenna efficiency of 50% is assumed which results in an effective element max gain of 2dB. The resulting overall antenna gain (after applying the array factor) is 28.02dB |
NOTE: For the link budget template, the 50% efficiency should be accounted for (e.g. either in the “boresight antenna element gain”, in “other losses” or in “Cable, connector, combiner, body losses, etc”).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.7.1-w001`

### [6G/Rel-20 RAN1#124b] `working_assumption` 10.7.1 NTN specific requirements and design for GNSS based operation

针对 6GR NTN 的 S-band UE antenna model（all orbits），考虑 Combination0 至 Combination3，分别对应 1、2、4、8 个 antenna elements，并列出各组合的 TXRU 数量及 Alt 1/Alt 2 天线模型候选。具体考虑哪些组合、TXRU 总数、Alt 1/Alt 2 细节及组合是否适用于特定 device types 均为 FFS。

```text
For 6GR NTN, for the UE antenna model for S-band (all orbits), consider a subset of the following combinations:
FFS: Which of the combinations are considered, Total Number of TXRU, and details of Alt 1/ Alt 2 for the antenna model.
FFS: Whether some of the combinations only apply for some device types.
| UE antenna modelling for RAN1 evaluations | Total number of antenna elements | Total number of TXRU | Alt 1: (M,N,P,Mg,Ng; Mp,Np), (dH,dV), (dg,H,dg,V) if any, or Alt 2: UT device antenna model using candidate antenna locations as described in section 7.3 in TR38.901 |
| --- | --- | --- | --- |
| Combination0 | 1 | 1T1R, | Alt 1: 1T: (M, N, P, Mg, Ng; Mp, Np)=(1, 1, 1, 1, 1; 1, 1) 1R: (M, N, P, Mg, Ng; Mp, Np)=(1, 1, 1, 1, 1; 1, 1) Alt 2: 1T 1R |
| Combination1 | 2 | 1T2R, 2T2R | Alt 1: 2R: (M, N, P, Mg, Ng; Mp, Np)=(1, 2, 1, 1, 1; 1, 2) for single polarization or (1, 1, 2, 1, 1; 1, 1) for dual polarization, (dH,dV)= (0.5, 0.5)λ Alt 2: 2R: [(1, 5), or (4, 8)] as described in section 7.3 in TR 38.901. |
| Combination2 | 4 | 1T4R, 2T4R, 4T4R | Alt 1: 4R: (M, N, P, Mg, Ng; Mp, Np)=(1, 2, 2, 1, 1; 1, 2) for dual polarization or (2, 2, 1, 1, 1; 2, 2) for single polarization, (dH,dV)= (0.5, 0.5)λ Alt 2: 4R: [(2, 4, 6, 8), or (1, 3, 5, 7)] as described in section 7.3 in TR 38.901 |
| Combination3 | 8 | 1T8R, 2T8R, 4T8R, 8T8R | Alt 1: (M, N, P, Mg, Ng; Mp, Np)= (1, 4, 2, 1, 1; 1, 4), or (2, 2, 2, 1, 1; 2, 2) for dual polarization or (2, 4, 1, 1, 1; 2, 4) for single polarization , (dH,dV)= (0.5, 0.5)λ Alt 2: (1, 2, 3, 4, 5, 6, 7, 8) as described in section 7.3 in TR38.901 |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.7.1-w002`

### [6G/Rel-20 RAN1#124] `agreement` 10.7.1 NTN specific requirements and design for GNSS based operation

NTN link budget template 以 TN link budget template 为基线。具体行和值（包括新增行）仍需进一步讨论。

```text
For NTN link budget template, RAN1 to take the TN link budget template as baseline with specific rows / values (including adding new rows) to be further discussed.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.7.1-a001`

### [6G/Rel-20 RAN1#124] `agreement` 10.7.1 NTN specific requirements and design for GNSS based operation

RAN1 将为指定的卫星轨道与频段组合定义 evaluation parameters：S-band 涵盖 LEO 300、LEO 600 和 GEO；Ka band 涵盖 LEO 600、GEO，以及方括号标注的 LEO 300、LEO 1200；Ku band 涵盖 LEO 1200 和 GEO。S-band 评估预计与 L-band 类似，且这些组合仅用于评估。

```text
RAN1 will define evaluation parameters for at least the following combinations of satellite orbit and bands:
S-band:
LEO 300, LEO 600, GEO
Ka band:
[LEO 300], LEO 600, [LEO 1200], GEO
Ku band:
LEO 1200, GEO
NOTE 1: The evaluations for S band are expected to be similar to L-band.
NOTE 2: This is only for the purpose of evaluations.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.7.1-a002`

### [6G/Rel-20 RAN1#124] `agreement` 10.7.1 NTN specific requirements and design for GNSS based operation

讨论至少用于物理层操作的 GNSS availability 时，RAN1 使用 GNSS-based、GNSS-degraded 和 GNSS-free/GNSS-less 术语，分别描述依赖具备 GNSS 接收机且满足位置精度要求、有过符合精度要求的位置 fix 但当前可能不满足，以及不依赖 GNSS 接收机或当前无可用于物理层操作的位置 fix 的网络操作模式。位置 fix 所需频率，以及能否用精度相当的非 GNSS 方式获得位置等事项仍待确定。

```text
RAN1 to use the following terminology when discussing GNSS availability at least for physical layer operation.
GNSS-based: Refers to the network mode of operation which relies on devices being equipped with a GNSS receiver and the devices can obtain a position fix within a given accuracy (e.g. 50m)
FFS: How often the UE may be required to obtain a position fix, which may be related to the required accuracy.
FFS: if position under this operation can be obtained by means other than GNSS that provides a comparable accuracy, e.g. pre-configuration for a fixed device. This may also include information other than positioning.
GNSS-degraded: Refers to the network mode of operation which relies on devices being equipped with a GNSS receiver, the devices were able to obtain a position fix at some point in time, but the devices may not currently have a position fix within a given accuracy (e.g. 50m) at the current time.
NOTE: The UE may be able to use the position fix for physical layer operation
GNSS-free/GNSS-less: Refers to the network mode of operation which does not rely on devices being equipped with a GNSS receiver, or devices are equipped with a GNSS receiver but do not have a current position fix that can be used for physical layer operation.
R1-2601470	Feature lead summary#2 on NTN specific requirements and design for GNSS based operation	Moderator (Qualcomm Incorporated)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.7.1-a003`

### [6G/Rel-20 RAN1#124] `agreement` 10.7.1 NTN specific requirements and design for GNSS based operation

6GR NTN 的目标是支持 GNSS-based、GNSS-degraded 和 GNSS-less/GNSS-free operation。

```text
6GR NTN targets to support GNSS-based operation, GNSS-degraded operation and GNSS-less/GNSS-free operation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.7.1-a004`

### [6G/Rel-20 RAN1#124] `agreement` 10.7.1 NTN specific requirements and design for GNSS based operation

6GR NTN uplink time-frequency synchronization 以 NR NTN 为基线，遵循相同原则，并引入 “uplink synchronization reference point” 概念及 satellite assistance information。至少在 GNSS-based operation 下，支持 UE 使用自身位置信息与 satellite assistance information 进行时频预补偿。

```text
6GR NTN uplink time-frequency synchronization follows the same principle as NR NTN as baseline:
The concept of “uplink synchronization reference point” is introduced in 6GR NTN.
6GR NTN provides satellite assistance information
At least for GNSS-based operation, it is supported that UE uses its own location information + satellite assistance information to perform time-frequency pre-compensation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.7.1-a005`

### [6G/Rel-20 RAN1#124] `agreement` 10.7.1 NTN specific requirements and design for GNSS based operation

6GR 支持 large scheduling offsets，以适应 satellite channel 引入的 RTT。进一步讨论两种实现选项：以 NR 的 k_offset 概念为基线并可能修改，或将较大的 RTT scheduling delays 纳入 scheduling offsets（例如类似 NR 的 K1/K2），其可对 TN 和 NTN 通用或不通用。

```text
6GR supports large scheduling offsets to accommodate the RTT introduced by the satellite channel. Further discuss how to realize these scheduling offsets:
Option 1: Reuse the k_offset concept from NR as a baseline with potential modifications.
NOTE: Under this option, additional scheduling offsets (e.g. similar to K1/K2 in NR) may be supported for scheduling flexibility, which apply in addition to k_offset.
Option 2: The large scheduling delays to accommodate the RTT are incorporated into the scheduling offsets (e.g. similar to K1/K2 in NR), which may or may not be common for TN and NTN.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.7.1-a006`

### [6G/Rel-20 RAN1#124] `agreement` 10.7.1 NTN specific requirements and design for GNSS based operation

研究 6GR NTN 在 GNSS based operation 下的 NTN specific issues/requirements，至少涵盖 uplink time-frequency synchronization、HARQ、large RTT timing relationships、coverage target、multi-satellite operation、multiple beams per satellite，以及卫星 beam footprints 多于同时激活 beams 的情况。其他方面也未被排除。

```text
Study NTN specific issues/requirements at least for the following aspects for 6GR NTN under this agenda:
Uplink time-frequency synchronization
HARQ issues: e.g. enable/disable HARQ feedback (which may include how to efficiently operate with HARQ feedback enabled/disabled), number of HARQ processes, etc.
Timing relationships with large RTT.
Coverage target
Physical layer aspects of multi-satellite operation (including multi-orbit)
Aspects related to Multiple beams per satellite
Aspects related to satellite having more beam footprints than simultaneously active beams
Other aspects are not precluded.
R1-2601681	Final Feature lead summary on NTN specific requirements and design for GNSS based operation	Moderator (Qualcomm Incorporated)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.7.1-a007`

### [6G/Rel-20 RAN1#124] `conclusion` 10.7.1 NTN specific requirements and design for GNSS based operation

6GR NTN 研究的一般原则是识别 NTN specific issues/requirements，并可在 NTN 议题下研究潜在解决方案；若可采用 common design，研究结果可在其他议题讨论，解决方案也可能扩展 TN design。若 common/extended design 无法满足 NTN requirements，可引入 NTN specific solutions；采用 common design 时优先考虑 TN performance。

```text
As a general principle for 6GR NTN study:
Under NTN agenda item, we will identify issues / requirements specific to NTN.
Potential solutions to these issues / requirements may be studied under the NTN agenda
The outcome of this study may be discussed under other agenda items if common design is possible.
These solutions may end up resulting in an extension of the TN design.
This may depend on the solution / issue / requirement
NTN specific solutions may be introduced when a common / extended design cannot meet the NTN requirements.
When targeting a common design TN performance is prioritized.
R1-2601471	Feature lead summary#3 on NTN specific requirements and design for GNSS based operation	Moderator (Qualcomm Incorporated)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.7.1-c001`

### [6G/Rel-20 RAN1#124] `conclusion` 10.7.1 NTN specific requirements and design for GNSS based operation

提交 RAN1#124b 的 link budget template 和 evaluation assumptions 输入时，鼓励公司将其放入贡献文档所附的 xls，并遵循 R1-2601471 所附 xls 的格式。

```text
When reporting inputs for the link budget template and evaluation assumptions to RAN1#124b, companies are encouraged to provide them in an xls attached to their contribution following the format of the xls attached to R1-2601471.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.7.1-c002`

