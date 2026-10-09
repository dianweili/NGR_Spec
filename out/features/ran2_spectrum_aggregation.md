# 6GR 频谱聚合

**当前进展** · 阶段：—

_尚无综述_

## 6GR 演进

### [6G/Rel-20 RAN2#134] `agreement` 9.3.2.5 Spectrum aggregation

```text
For both CA and DC there are performance limitation because of the 10ms backhaul delays
For CA, if the backhaul delay can be transparent from the UE, CA can work up to some backhaul delay.  Some evaluations have shown that it works when X is very short, but the value of X also depends on network implementation.  If X is long, then there are protocol, performance, interface impacts and needs to be further studied.
DC is defined to handle long backhaul delays, but concerns on complexity and performance are raised, so need to study further the impact to UP, CP, and whether it can be simplified.
RAN2 needs to study for FR1 + FR2 scenario and understand the protocol impacts, performance impacts, and how if some of the requirements are met for CA and DC.
[POST134][15][6G CP] Non-ideal backhaul (Xiaomi)
Intended outcome: Impact analysis of non-collocated FR1+FR2 scenarios with backhaul delays up to 10ms.
Phase 1
Identify the protocol, interface, where/how the data is split for dual scheduler, dual PUCCH, and performance for CA framework and understand the required changes to support it.
Identify the impacts to UP, CP of supporting DC, where/how data is split, performance impacts, if and how simplified DC can work.
Understand which requirements can be met for the various solutions (e.g. deployment flexibility, aggregation)
Phase 2
Evaluation (whenever available) at protocol level and assumptions used (including scheduler assumed – companies are encouraged to ensure that dual scheduler is included in the evaluation).  Dual PUCCH is assumed for evaluation purposes.
Attempt to compare the gains, advantages, disadvantages of all solutions
Deadline:  Long
R2-2603008	Discussion on 6G spectrum aggregation	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
R2-2603023	FR1/FR2 operation – CA vs DC vs switching	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
R2-2603030	Spectrum Aggregation for Connected UE and Non-collocated scenario	CATT	discussion	Rel-20	FS_6G_Radio
R2-2603083	5G CA Mechanism Shortcomings from Operator view	T-Mobile USA Inc.	discussion	Withdrawn
R2-2603177	Discussion on multi-carrier operation and non-collocated scenarios	1Finity	discussion	Rel-20	FS_6G_Radio
R2-2603183	Discussion on 6G Spectrum aggregation and access control	OPPO	discussion	Rel-20	FS_6G_Radio
R2-2603302	Multi Carrier Operation	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2603521	Solutions for non-colocated FR1-FR2 deployments	Ericsson	discussion	Rel-20	FS_6G_Radio
R2-2603522	Aspects on 6G spectrum aggregation and multi-carrier functionalities	Ericsson, Bell Mobility	discussion	Rel-20	FS_6G_Radio	Withdrawn
R2-2603572	Discussion on spectrum aggregation for Connected state	Lenovo	discussion	Rel-20
R2-2603606	How to improve resilience aspects in 6G	NTT DOCOMO, Ericsson, FirstNet, NIST, Jio Platforms, SyncTechno Inc., Airbus, UIC	discussion	Rel-20
=> Revised in R2-2604170
R2-2603659	Further discussion on spectrum aggregation	NEC	discussion	Rel-20	FS_6G_Radio
R2-2603909	Discussion on spectrum aggregation and C-plane other aspects for 6GR 	Kyocera 	discussion	Rel-20
R2-2603981	Discussion on spectrum aggregation and access control	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2604009	Spectrum Aggregation for 6GR	MediaTek Inc.	discussion	R2-2602522
R2-2604081	Discussion on spectrum aggregation for non-collocated FR1-FR2 deployments	CEWiT	discussion	Rel-20	FS_6G_Radio
R2-2604136	Discussion on deployment Scenarios and challenges for UL/DL decoupling	KDDI Corporation (TTC)	discussion
R2-2604158	Discussion on Multi-Carrier in Connected Mode and in Non-collocated Scenario	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
R2-2604167	Discussion on 6G non-collocated spectrum aggregation	Rakuten Mobile, Inc	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-a001`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.5 Spectrum aggregation

```text
In 5G CA, due to the restriction of UL CCs no more than DL CCs, it is hard to adapt to different UL/DL traffic load, especially for the UL heavy traffic.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-o001`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.5 Spectrum aggregation

```text
In 5G CA, in some cases, such as changing the serving SCell to PCell, the execution of HO will cause unnecessary interruption and signalling overhead.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-o002`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.5 Spectrum aggregation

```text
In 5G CA, the PCell RLF will cause RRC re-establishment even if the SCell is still available, which will cause unnecessary interruption and signalling overhead as well.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-o003`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.5 Spectrum aggregation

```text
In NR, the duplex mode (TDD or FDD) and uplink/downlink directions of each frequency band are strictly specified, SUL is heavily dependent on the defined SUL carriers and UL-only SCell is not supported for NR CA.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-o004`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.5 Spectrum aggregation

```text
For deployments where the backhaul latency is significant (e.g. 10ms), single scheduler operation has significant issues in operation of HARQ, CSI, ARQ and also not feasible for inter-vendor deployment.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-o005`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.5 Spectrum aggregation

```text
On the other hand, if the backhaul latency is not large (which the nodes are still not co-located), the central scheduler can manage the delay transparently to the UE (for eg., operating ‘n’ slots in advance) such that the usual co-located CA operation can work. It can be up to NW implementation on when they can decide to use single vs dual scheduler based on their backhaul delay.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-o006`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.5 Spectrum aggregation

```text
A 10ms backhaul latency would significantly increase L2/HARQ memory buffer requirements at the due to increase in the HARQ RTT.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-o007`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.5 Spectrum aggregation

```text
A 10ms backhaul latency renders centralized scheduling decisions highly inefficient, as critical status information (e.g., BSR, CQI, PHR) becomes outdated by the time it is received by the central MAC entity.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-o008`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.5 Spectrum aggregation

```text
Relying on a single scheduler across a 10ms backhaul severely degrades the performance of latency-sensitive MAC procedures, such as SCell activation/deactivation and MAC CE transmissions.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-o009`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.5 Spectrum aggregation

```text
While a single-scheduler Carrier Aggregation architecture may be feasible for non-collocated deployments with low backhaul latency (e.g., 2ms), it is likely not feasible for latencies of upto 10ms.
Dual Scheduler Deployment – DC
R2-2603836	6G Spectrum aggregation for FR1-FR2 deployments	Verizon, Qualcomm Inc, Samsung, NTT DOCOMO, Orange	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-o010`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.5 Spectrum aggregation

```text
For dual/independent scheduler case with large backhaul delay, the user data forwarding to FR2 cell should be at least above the MAC layer (i.e. not the MAC layer).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-o011`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.5 Spectrum aggregation

```text
If multiple NW schedulers control the scheduling for the same UE on different cells, there needs to be tight coordination between these schedulers; otherwise, this can add UE HARQ requirements as well as negatively affect HARQ/ARQ and RLC performance (e.g. (re)segmentation).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-o012`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.5 Spectrum aggregation

```text
In 4G/5G, in CA, it assumed that the backhaul latency between different DL transmission points is ‘ideal’, i.e. in the order of microseconds. For non-ideal backhaul, DC is used when multiple eNB/gNB/DU are involved in transmission to the same UE.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-o013`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.5 Spectrum aggregation

```text
NR CA already supports PUCCH SCell and sTAG for non-collocation scenarios. It can be applied to non-collocated CA with non-ideal backhaul.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-o014`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.5 Spectrum aggregation

```text
In NR non-collocated CA, time-critical MAC functionalities (e.g., BSR, PHR, RACH, and SCell activation) may have degraded performances due to the backhaul delay.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-o015`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.5 Spectrum aggregation

```text
When multiple PUCCH cell groups and multiple TAGs are configured for non-collocated CA, the MAC entity remains a single logical entity, and the RLC and PDCP layers are transparent to the underlying CC topology. Hence UP handling remains consistent between co-located and non–co-located CA scenarios.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-o016`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.5 Spectrum aggregation

```text
In 6G UP, RAN2 is studying UP architecture with unified SN, along with HARQ feedback based L2 ARQ handling. While some of the agreed design assumptions of this study could influence non-co-located CA operation, RAN2 should avoid defining a separate UP architecture for the non-co-located case compared to 6G SA.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-o017`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.5 Spectrum aggregation

```text
With 5G-like DC, the flow control and separate RLC buffers will cause at least ~20% throughput reduction compared to the ideal CA throughput.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-o018`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.5 Spectrum aggregation

```text
Non-collocated CA performance with 10ms is still reasonable and provides gains over single carrier performance.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-o019`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.5 Spectrum aggregation

```text
Table-2 shows the CA with dual PUCCH group comparison with DC operation. It can be observed that CA brings in more efficiency in terms of configuration/control operation compared to DC, while sacrificing deployment and operational flexibility.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-o020`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.5 Spectrum aggregation

```text
CA also has functional inefficiencies due to single RLC and MAC functionality with the delay that the backhaul brings for L2 ARQ traversal, or certain MAC runtime operation related parameter traversal. However, if we restrict the UL to one leg (non-split bearer operation) esp. to the leg that does not require the BH traversal, CA operation would be much better than DC.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-o021`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.5 Spectrum aggregation

```text
The number of FR2 cells supported per FR1 cell limits the amount of FR1 spectrum that can be aggregated with each FR2 cell, limiting the benefit of FR1-FR2 spectrum aggregation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-o022`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.5 Spectrum aggregation

```text
Aggregating FR1 and FR2 spectrum via a 10ms non-ideal backhaul between FR1 and FR2 aNBs will impact the overall performance, both in terms of achievable throughput (due to the additional packet re-ordering delay) and latency.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-o023`

### [6G/Rel-20 RAN2#134] `observation` 9.3.2.5 Spectrum aggregation

```text
Aggregating asymmetric data rates on FR1 and FR2 may cause further performance degradation on TCP and overall lower performance than using FR2 alone.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-o024`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.5 Spectrum aggregation

```text
RAN2 addresses the following shortcomings of 5G CA for 6G carrier aggregation framework.
-	HO procedure is always triggered upon PCell change causing unnecessary interruption and signalling overhead;
-	RRC re-establishment is always triggered upon PCell RLF causing unnecessary interruption and signalling overhead.
Noted
R2-2604176	Aspects on 6G spectrum aggregation and multi-carrier functionalities	Ericsson, Bell Mobility, Far EasTone	discussion	Rel-20
Proposal 6	RAN2 to consider the following 5G CA shortcomings when studying multi-carrier operations in CONNECTED mode:
a.	PCell and SCell separation (from configuration and operation perspective)
b.	No recovery for PCell RLF
c.	Difficult to perform PCell/SCell role change
d.	Slow activation/addition of SCells (and CA in general)
e.	Static combination of carriers (UL/DL)
-	Mediatek highlights that some of this and role of PCell was linked to UCI so we should forget
Shortcoming from RAN2 point of view for 5G CA
HO procedure is always triggered upon PCell change causing unnecessary interruption and signalling overhead.   Difficult to perform PCell/SCell role change
RRC re-establishment is always triggered upon PCell RLF causing unnecessary interruption and signalling overhead.   PCell re-establishment causes all SCells to be dropped.
Slow activation/de-activation/addition of SCells (and CA in general)
PCell/SCell Roles
R2-2603863	Discussion on spectrum aggregation and non-ideal backhaul	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-p001`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.5 Spectrum aggregation

```text
For the functionalities of “6G PCell/SCell”, RAN2 is asked to agree that:
	At least the following functionalities should be supported by 6G PCarrier/PCell:
	Initial access;
	MIB/SIB/paging/SSB;
	Beam failure;
	RLM and re-establishment;
	Mobility;
	CBRA/CFRA;
	PUCCH;
	AS security input.
Measurements of PCells?
At least the following functionalities should be supported by 6G SCarrier/SCell:
	SCell activation/deactivation/dormancy;
	CFRA for synchronization;
	PUCCH (configurable);
	RLM (configurable).
Measurements of Scells?
-	Ericssons ask why we have limited the mobility to Pcell.  In LTM we can do mobility on a Scell if it is configured as a candidate Pcell.   CMCC explains that the configuration comes from PCell.  Ericsson wonders if we are talking about functionality or configurations.
-	ZTE thinks that there are different meaning of mobility.
-	Samsung is not sure that we need configurable RLM for SCell as there are concerns on UE complexity.
Noted
R2-2602954	Further discussion on spectrum aggregation in connected state	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-p002`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.5 Spectrum aggregation

```text
RAN2 aims to remove the functional distinction between PCell and SCell, allowing key functionalities traditionally anchored to the PCell to be flexibly supported on any serving cell, including, but not limited to:
-	RLM-RS and PUCCH are not necessarily configured on PCell;
-	UAC procedures can be performed independently of PCell-specific parameters.
-	Lenovo and Xiaomi understands that UAC applies only to idle.   Vivo explains that’s not the case.
-	Mediatek and Nokia thinks that it is not a CA problem even if UAC is only in SIB of PCell.
Noted
R2-2604176	Aspects on 6G spectrum aggregation and multi-carrier functionalities	Ericsson, Bell Mobility, Far EasTone	discussion	Rel-20
Proposal 7	In 6G spectrum aggregation functionalities are not implicitly tied to a primary/secondary cell. Instead, functionality is associated to each carrier/cell through explicit dedicated signalling.
-	Mediatek and Qualcomm are concerned with complexity if we allow a lot of flexibility and frequent changing of functions.
Noted
Working list
At least the following functionalities should be supported by 6G PCarrier/PCell:
MIB/Cell defining SSB/ FFS SIB/paging depending on progress on connected mode functionality
Beam failure;
RLM and re-establishment;
Mobility;
Random access
PUCCH (if supported);
AS security input (does it need to be done only by PCell?)
Measurements of PCells
SCell activation/deactivation;
At least the following functionalities should be supported by 6G SCarrier/SCell:
SCell activation/deactivation;
Random access for synchronization;
PUCCH (configurable) (if supported);
RLM (configurable).
Beam failure
Measurements of Scells?
NOTE: This functions may change depending on what is actually agreed in RAN2 and RAN1 for the non-CA functionality.
Functionality for 6G
RLM/RLF
R2-2603914	Discussion on spectrum aggregation	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
Proposal 1	Study PCell failure recovery without RRC re-establishment via reporting PCell failure to SCell.
Proposal 2	Study Radio Link Failure based on RLM over PCell and SCell(s).
R2-2604170	How to improve resilience aspects in 6G	NTT DOCOMO, Ericsson, FirstNet, NIST, Jio Platforms, SyncTechno Inc., Airbus, UIC, Turkcell	discussion	Rel-20	R2-2603606
Observation 4	5G did not introduce features which are preventive for the purpose of resiliency.
Observation 5	Addressing resiliency in the basic design of 6G and the main 6G features improves the opportunities for commercialization.
Proposal 1	6G supports additional tools (i.e., besides RLF detection and RRC re-establishment) for providing resiliency, such as:
a.	Additional triggers, e.g., loss of keep-alive signaling over UP or keep-alive signaling over CP.
b.	New UE actions, e.g., starting a handover procedure, activating a carrier.
Study RLF/RLM and recovery procedures over/for SCell
UL/DL Decoupling
R2-2603863	Discussion on spectrum aggregation and non-ideal backhaul	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-p003`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.5 Spectrum aggregation

```text
For 6G, flexible UL and DL carrier decoupling should be considered to supplement UL coverage and accommodate UE traffic characteristics. To achieve this, RAN2 is asked to take into account the requirement of flexible uplink and downlink carrier decoupling in signaling design (e.g. RRC structure) and study fast carrier/cell addition/modification/activation/deactivation schemes.
Non-collocated deployments
Single Scheduler
R2-2603733	Views on 6G spectrum aggregation	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-p004`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.5 Spectrum aggregation

```text
For the cases where the inter-node backhaul delay ‘X’ can be hidden by aNB implementations resulting in transparent CA operation at the UE, RAN2 assumes there are no additional requirements at the 6G SA UE.  FFS if RAN2 study the value of ‘X’.
-	Qualcomm thinks that what’s important is the value of X.   X can’t be larger than micro to 1ms and what X is also depends on where you draw the line in terms of performance.
-	Nokia thinks that this is a bit strange because we don’t specify scheduler but rather MAC entity.
R2-2602976	Discussion on spectrum aggregation and non-collocated non-ideal backhaul	Xiaomi	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-p005`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.5 Spectrum aggregation

```text
For protocol split between scheduler and RRU/TRP in single scheduler option of non-collocated scenarios, the identified issues are:
-	Split between MAC and PHY is challenging to implement due to tight coupling of MAC and PHY operations.
-	Split within PHY requires substantial requirements on the backhaul bandwidth due to the transmission of quantized I/Q frequency domain samples, and solution similar to NTN might be required.
-	Transparent forwarding of analog RF signals typically has microsecond level delay and does not required solution similar to NTN, but the functionality is quite limiting especially for FR2 operation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-p006`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.5 Spectrum aggregation

```text
RAN2 to deprioritize the study of single scheduler option in non-collocated scenarios.
Noted
R2-2603668	Spectrum Aggregation for 6GR	InterDigital, Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-p007`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.5 Spectrum aggregation

```text
For non-colocated FR1-FR2 deployment scenario, RAN2 to only investigate spectrum aggregation solutions that satisfy the following requirements:
a)	Support spectrum aggregation between FR1 and FR2 bands for both uplink and downlink
b)	Support up to 10 ms backhaul latency between the non-collocated FR1 and FR2 sites.
-	ZTE asks if aggregation means split bearer.  Verizon clarifies that it just means putting two carriers together and no particular solution.  ZTE thinks that we need to understand whether we have to split the bearer or ability to access the carrier.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-p008`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.5 Spectrum aggregation

```text
RAN2 6G protocol design shall support multi-vendor FR1-FR2 non-colocated deployments.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-p009`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.5 Spectrum aggregation

```text
NR-DC should be considered as baseline when evaluating solutions for 6G-6G spectrum aggregation for non-collocated FR1-FR2 scenario.
Noted
R2-2603930	Views on Spectrum Aggregation: Non-Collocated Scenario and Multi-Carrier Operation	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-p010`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.5 Spectrum aggregation

```text
As baseline, 5G CA framework to be reused for 6G-6G FR1-FR2 aggregation for only intra-aNB deployment with ideal/collocated backhaul, and operation at the UE is transparent from MAC/RLC perspective (irrespective of NW topology). Further, RAN2 confirm that DC can be used for 6G-6G FR1-FR2 aggregation for both intra-aNB and inter-aNB deployments with non-ideal backhaul.
Noted
R2-2604032	Discussion on 6G-6G Spectrum Aggregation	Samsung, Verizon	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-p011`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.5 Spectrum aggregation

```text
RAN2 takes a simplified Dual Connectivity into account, while keeping the Dual Connectivity framework for 6G-6G spectrum aggregation.
-	Huawei explains that it is because of the problems identified.
Noted
Dual Scheduler Deployment – CA Architecture
R2-2603157	Discussion on Spectrum Aggregation in 6G	Sharp	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-p012`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.5 Spectrum aggregation

```text
RAN2 to study an enhanced CA framework where time-critical MAC functionalities (e.g., BSR, PHR, RACH, and SCell activation) are handled independently by each distributed scheduler.
-	Xiaomi asks what is the UE impact on dealing with the 10ms delay.   Sharp thinks it is possible that there are no UE impacts.   Qualcomm thinks that there are delays and this creates UE problems, HARQ processes, CSI prediction.  We should ask if it works.
Noted
R2-2603675	Carrier aggregation in 6G	Nokia	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-p013`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.5 Spectrum aggregation

```text
RAN2 to conclude that non-collocated CA performance is reasonable even with 10ms BH latency.
-	Fraunhofer asks if we have considered FR1-FR2, Nokia indicates that it is only FR1-FR1.  Qualcomm thinks we can’t conclude the same for FR1-FR1 and we need to look at simulation assumptions as there are configurations/scenarios where we can show good performance.
Noted
R2-2603733	Views on 6G spectrum aggregation	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-p014`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.5 Spectrum aggregation

```text
CA operation with two PUCCH groups where the uplink operates as non-split bearer with the  (PUSCH)  towards the node that does not encounter the backhaul delay is the preferred CA based solution. For DC based solution, simplification with no SRB3, SN-based mobility and single security context with dynamic leg-switching is better than 5G NR DC.
Noted
R2-2603007	Support of 6G FR1-FR2 non-collocated deployments	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-p015`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.5 Spectrum aggregation

```text
If FR1-FR2 spectrum aggregation is really needed in case of separate schedulers within single MAC entity, CA can still be used, however the specification of the coordination within a single MAC entity is considered challenging and undesirable from RAN2 perspective.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-p016`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.2.5 Spectrum aggregation

```text
Fast switching between FR1 and FR2 via enhanced mobility procedures should also be considered as a way to exploit FR1 and FR2 non-collocated deployments in 6G, particularly for inter-vendor scenarios (FFS on the details).
-	Xiaomi and Verizon thinks that this is not aggregation.   ZTE thinks that the question do your really aggregate and live with poor performance of aggregation or do you not aggregate and live with switching.   Verizon explains that we aggregate and we are seeing excellent performance.
-	Fraunhoufer agrees with the proposal and brings a good baseline in terms of simplicity.
-	CMCC agrees with ZTE as the goal is to support the service.
-	Nokia explains that there is a large spectrum imbalance and we want to have a good performance.  Xiaomi indicates that RAN2 did a lot of evaluation for DC and concluded that the performance is good so it is strange to conclude that the performance is bad.  Qualcomm thinks that the performance is not done fairly as it is compared to collocated ideal backhaul aggregation but it is not deniable that it is better than single leg.   The problem with switching you have so much mobility events in FR2 and that’s why you need anchor concepts.   Xiaomi also thinks that this is to help with the mobility.
-	Vivo thinks switching is not good performance wize.
Noted
R2-2603521	Solutions for non-colocated FR1-FR2 deployments	Ericsson	discussion	Rel-20	FS_6G_Radio
Proposal 1	UEs in good FR2 coverage shall camp on and access FR2 directly.
Proposal 2	RAN2 to focus the work on solutions to increase the feasibility of UEs camping, accessing and operating on FR2 standalone, e.g. conditional handover to FR1 (increased robustness).
Proposal 3	In networks deployments with low latency transport (<1-2ms), a single baseband/scheduler solution with single PDCP/RLC protocol entities per bearer is feasible with LLS to distributed RUs.
Noted
Discussion
-	ZTE thinks that in case the backhaul delay is x and can be transparent to UE then CA can work.
-	Qualcomm ask if that means that beyond X it doesn’t work.    Apple thinks that X is really up to network implementation, if they can mask plain CA with no addition.   Qualcomm ask if that allows inter-vendor.
-	Ericsson explains that for the short X we can use normal CA, when the backhaul latency is long we can study.   We can maybe agree that when it is short normal CA work.    Nokia thinks that we have some consensus that CA work when CA is short, but we can’t really conclude on what X is.   We also don’t have a good understanding of what are the cases we are looking for and what are the BW, the imbalances.
-	Verizon thinks that we should capture then all solution and shown when it works, like for when you have LLS.
-	Xiaomi thinks that we need also consider deployment scenarios, identify the limitation of CA.  We how to simplify DC.
-	Samsung if X is not very short, then it won’t work.
-	Huawei thinks that even when X is long it can work.  ZTE thinks that even in long X it can be transparent to the UE, but when X is long there will be performance impact.
-	Qualcomm thinks that from performance point of view it doesn’t work, we should design a system that work.   Docomo agrees with Qualcomm.  Docomo explains that even if in their deployment X was very very very short, they deployed DC.
-	Mediatek agrees with ZTE and Huawei, the performance will be impacted no matter what.   With dual PUCCH everything works fine.
-	CMCC thinks that CA works.
-	LG reminds that in R12 we started study the impact of long delays (up to 60ms) and we agreed that 10ms was the longest that we could provide the throughput required.    In LTE we had 1ms TTI and now we have subms TTIs, but with short TTI the performance is greatly degraded, and if we need study X we need to study again.
-	Nokia would like to understand what is the reference we are comparing to.   We should compare to single carrier FR2 rather than ideal CA.    Focus on flow control, protocol impacts, how MAC works, how data path works.  There is a big bandwidth imbalance that we never studied in LTE.   Qualcomm explains that if you do just FR2 you will have too many mobility events.  Nokia thinks that if you have a mobility issue you have it for DC as well, we just need to understand the issue.    Ericsson would prefer a more complex study than a complex specification.   The system capacity gains decrease when there are delays so we just need to understand what are impact, how we provide feedback, where we split the data etc.
-	Verizon one consideration is the BW required for supported cases of LLS and fronthaul bandwidth as initial studies showed that it can’t be scalable.    Performance, scalability, how much bandwidth it requires, and inter-vendor.   Solutions should be compared for the scenario FR1 and FR2.  Apple we can cover the what is required for inter-vendor.
-	Mediatek also reminds about the split bearer UP complexity and also 10ms delay is very long.   The problems with split bearer would look the same regardless of CA and DC and we would resolve things in similar way and result in similar performance.
-	Huawei thinks we need to consider coverage for both UL and DL of FR2.   Fraunhaufer thinks that we need to split the scenarios, when we have DL but no UL
-	ZTE thinks that we need to compare with single carrier as FR2 on it’s on can have better performance than aggregation with FR1.    Verizon thinks that the scenario from plenary is FR2 and FR1 aggregation.
-	ZTE thinks that throughput imbalance should be considered.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.2.5-p017`

