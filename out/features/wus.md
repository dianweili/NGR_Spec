# 6GR 唤醒信号与运行机制

**当前进展** · 阶段：—

_尚无综述_

## 6GR 演进

### [6G/Rel-20 RAN1#126] `agreement` 10.6.1.1 Design of WUS with OFDM based sequence

```text
Study DL WUS for both basic coverage and extended coverage.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.6.1.1-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.6.1.1 Design of WUS with OFDM based sequence

```text
For DL WUS evaluations in FR1 and ~7 GHz, RAN1 assumes 1 µs and 2 ppm for maximum timing and frequency errors, Temax and Femax, respectively, prior to detecting DL WUS, at least within the same carrier as SSB.
Consider additionally potential solutions when necessary for addressing 2 µs timing error and 5 ppm frequency error, e.g.,
DL WUS processing timeline relaxation
The actual timing and frequency errors, Te and Fe, respectively, are modelled as uniform distributions, Te ~ U [-Temax, Temax ] µs and Fe ~ U [-Femax, Femax] ppm, respectively, are assumed for link level simulations.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.6.1.1-a002`

### [6G/Rel-20 RAN1#126] `agreement` 10.6.1.1 Design of WUS with OFDM based sequence

```text
Study maximum number of transmittable sequence candidates and maximum number of sequence candidates targeting a UE per DL WUS sequence resource, considering, e.g.,
Detection performance
UE complexity and energy consumption
Overhead
BS complexity
Resilience to neighbor cell interference
RRC states
Information provided by DL WUS
Basic and extended coverage
Note: A DL WUS sequence resource is the time and frequency resource of a single WUS sequence. A DL WUS MO may include multiple DL WUS sequence resources, including the same or different sequence.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.6.1.1-a003`

### [6G/Rel-20 RAN1#126] `agreement` 10.6.1.1 Design of WUS with OFDM based sequence

```text
1% BLER of the reference PDCCH at -8.1 dB SNR is assumed as the starting point of DL WUS design.
Further discussed extended coverage.
R1-2606923	Final summary of DL WUS design	Moderator (Ericsson)
Final post-meeting summary of this agenda item.
R1-2605205	Evaluation considerations for FDR-aware OFDM-based DL WUS sequence comparison	USTB
R1-2605269	Discussion on design of WUS with OFDM based sequence	Spreadtrum, UNISOC
R1-2605304	Design of WUS with OFDM based sequence	Huawei, HiSilicon
R1-2605315	Design of WUS with OFDM based sequence	Ericsson
R1-2605351	Discussion on 6G Design of WUS with OFDM based Sequence	FUTUREWEI
R1-2605397	On the design of WUS with OFDM based sequence	Nokia
R1-2605409	Discussion on 6GR DL WUS with OFDM based sequence	Quectel
R1-2605477	Discussion on design of 6GR DL WUS with OFDM based sequence	vivo
R1-2605495	Design of WUS with OFDM based sequence	Tejas Networks Limited
R1-2605509	IMU Views on DL-WuS for 6GR	IMU
R1-2605517	Discussion on Design of WUS with OFDM based sequence	Panasonic
R1-2605578	Discussion on Downlink WUS with OFDM based sequence for 6GR	Xiaomi
R1-2605602	Discussion on WUS design with OFDM-based sequence	Lenovo
R1-2605646	Discussion on the sequence design for DL WUS in 6GR	CMCC
R1-2605681	Views on DL WUS Design	Ofinno
R1-2605736	Discussion on design of WUS with OFDM based sequence	CATT
R1-2605775	Disscussion on Design of WUS with OFDM based sequence	Sharp
R1-2605785	Discuss on DL WUS with OFDM based sequence	ZTE Corporation, Sanechips
R1-2606801	Discuss on DL WUS with OFDM based sequence	ZTE Corporation, Sanechips
(Revision of R1-2605785)
R1-2605846	Discussion on design of WUS with OFDM based sequence	Samsung
R1-2606790	Discussion on design of WUS with OFDM based sequence	Samsung
(Revision of R1-2605846)
R1-2605865	Discussion on design of WUS with OFDM based sequence	NEC
R1-2605922	Discussion on the signal design of DL WUS	OPPO
R1-2605984	On design of WUS with OFDM based sequence	Sony
R1-2606003	DL WUS and operation in 6GR interface	InterDigital, Inc.
R1-2606036	Design of 6G DL WUS with OFDM based sequence	Apple
R1-2606148	Design of downlink WUS with OFDM based sequence	MediaTek Inc.
R1-2606173	Discussion on 6G DL WUS design 	Kyocera Corporation
R1-2606190	Discussion on the design of WUS based on OFDM sequence	HONOR
R1-2606206	Discussion on design of DL WUS with OFDM based sequence for 6GR	LG Electronics
R1-2606253	Discussion on design of WUS with OFDM based sequence	ETRI
R1-2606311	Discussion on design of WUS with OFDM based sequence	EURECOM
R1-2606390	DL WUS Design	Qualcomm Incorporated
R1-2606811	DL WUS Design	Qualcomm Incorporated
(Revision of R1-2606390)
R1-2606402	Discussion on design of WUS with OFDM based sequence	Google
R1-2606516	Discussion on design of WUS with OFDM based sequence	NTT DOCOMO, INC.
R1-2606580	Discussion on design of WUS with OFDM based sequence	WILUS Inc.
R1-2606602	DL WUS Design	Nordic Semiconductor ASA
R1-2606688	Discussion on design of DL-WUS with OFDM based sequence	TCL
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.6.1.1-a004`

### [6G/Rel-20 RAN1#126] `conclusion` 10.6.1.1 Design of WUS with OFDM based sequence

```text
RAN1 to down select between Zadoff-Chu sequence family and Gold sequence family for DL WUS at latest by RAN1#127.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.6.1.1-c001`

### [6G/Rel-20 RAN1#126] `agreement` 10.6.1.2 WUS operation in RRC states

```text
At least in RRC idle, study for 6GR DL WUS by considering
At least SSB is used as QCL source, the association between SSB and DL WUS monitoring occasion(s), and the QCL type(s)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.6.1.2-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.6.1.2 WUS operation in RRC states

```text
For RRC connected, study feasibility and necessity of serving cell RLM measurement by EE processing, considering at least:
UE energy saving gain
Coverage (e.g., achievable SINR/SNR) and accuracy
Measurement metrics
Impact on the EE processing complexity
Based on at least 6GR sync signal
other signals
Whether there is spec impact or not
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.6.1.2-a002`

### [6G/Rel-20 RAN1#126] `agreement` 10.6.1.2 WUS operation in RRC states

```text
Study the following cases for 6GR DL WUS monitoring occasions:
Case 1: A set of WUS monitoring occasions associated with at least one PO for a UE are TDMed, multiple sets of WUS monitoring occasions are TDMed.
Case 2: A set of WUS monitoring occasions associated with at least one PO for a UE are TDMed, multiple sets of WUS monitoring occasions are FDMed or FDMed combined with TDMed.
Case 3: A set of WUS monitoring occasions associated with at least one PO for a UE are FDMed or FDMed combined with TDMed
For case 1, 2, and 3, UE is not required to monitor more than one MO at given time.
considering at least:
Impact on the UE energy consumption
Impact on the UE complexity
Network energy gains if any
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.6.1.2-a003`

### [6G/Rel-20 RAN1#126] `agreement` 10.6.1.2 WUS operation in RRC states

```text
For collection of UE energy saving gain results for 6GR DL WUS in RRC connected, at least the following cases are considered:
Case 1:No neighboring cell RRM measurement
| Case | Schemes for triggering PDCCH monitoring | Serving cell RLM/RRM measurement | Neighboring cell RRM measurement |
| --- | --- | --- | --- |
| Case1-1 | C-DRX only | Non-EE processing | Not applicable |
| Case1-2 | C-DRX with DCP | Non-EE processing | Not applicable |
| Case 1-3 | C-DRX with DL WUS | Non-EE processing | Not applicable |
| Case 1-4 | C-DRX with DL WUS | EE processing | Not applicable |
| Case 1-5 | DL WUS | Non-EE processing | Not applicable |
| Case 1-6 | DL WUS | EE processing | Not applicable |
Case 2: with neighboring cell RRM measurement
| Case | Schemes for triggering PDCCH monitoring | Serving cell RLM/RRM measurement | Neighboring cell RRM measurement |
| --- | --- | --- | --- |
| Case 2-1 | C-DRX only | Non-EE processing | non-EE processing |
| Case 2-2 | C-DRX with DCP | Non-EE processing | non-EE processing |
| Case 2-3 | C-DRX with DL WUS | Non-EE processing | non-EE processing |
| Case 2-4 | C-DRX with DL WUS | EE processing | Non-EE processing |
| Case 2-5 | C-DRX with DL WUS | EE processing | EE processing |
| Case 2-6 | DL WUS | Non-EE processing | non-EE processing |
| Case 2-7 | DL WUS | EE processing | Non-EE processing |
| Case 2-8 | DL WUS | EE processing | EE processing |
Note 1: Neighboring cell RRM measurement includes at least intra-frequency measurement, inter-frequency measurement is up to company report. How neighboring cell RRM measurement is performed by EE processing is up to companies’ report, including power consumption. L1 measurement is up to companies’ report.
Note 2: For traffic, FTP, XR, IM can be evaluated and traffic arrvival rate is up to companies’ report
Note 3: Assumed sleep state is up to company report.
Note 4: In this evaluation, no further power scaling based on the number of occupied SSB symbols within a slot for the measurement by EE processing
Note 5: If RLM/RRM measurement is not evaluated, please report.
Note 6: it’s up to companies’ report how the evaluated C-DRX different from NR C-DRX
Note 7: it’s up to companies’ report how the evaluated DCP different from NR DCP
Note 8: when comparing different cases, companies are encouraged to at least consider the same monitoring periodicity of 6GR DL WUS and C-DRX cycle. Other periodicities are up to companies’ report.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.6.1.2-a004`

### [6G/Rel-20 RAN1#126] `agreement` 10.6.1.2 WUS operation in RRC states

```text
For collecting UE energy saving results for 6GR DL WUS:
Endorse the template for collecting UE energy saving results in R1-2606878.
R1-2606901	Final summary on 6GR DL WUS operation in RRC states	Moderator (vivo)
Final post-meeting summary for this agenda item.
R1-2606900 	Summary #5 on 6GR DL WUS operation in RRC states	Moderator (vivo)
R1-2606854	Summary #4 on 6GR DL WUS operation in RRC states	Moderator (vivo)
R1-2606853	Summary #3 on 6GR DL WUS operation in RRC states	Moderator (vivo)
R1-2605479	Summary #1 on 6GR DL WUS operation in RRC states	Moderator (vivo)
R1-2605480	Summary #2 on 6GR DL WUS operation in RRC states	Moderator (vivo)
R1-2605215	Discussion on 6G WUS Operation in RRC States	FUTUREWEI
R1-2605270	Discussion on WUS operation in RRC states	Spreadtrum, UNISOC
R1-2605305	WUS operation in RRC states	Huawei, HiSilicon
R1-2605316	WUS operation in RRC states	Ericsson
R1-2605370	WUS operation in RRC states	Lenovo
R1-2605398	On WUS operation in different RRC states	Nokia
R1-2605478	Discussions on 6GR DL WUS operation in RRC states	vivo
R1-2605518	Discussion on WUS operation in RRC states	Panasonic
R1-2605579	Discussion on Downlink WUS in RRC states for 6GR	Xiaomi
R1-2605647	Discussion on the DL WUS for 6GR	CMCC
R1-2605682	Views on DL WUS in RRC States	Ofinno
R1-2605737	Discussion on WUS operation in RRC states	CATT
R1-2605776	Discussion on WUS operation in RRC states	Sharp
R1-2605786	Discuss on DL WUS operation	ZTE Corporation, Sanechips
R1-2605847	Discussion on WUS operation in RRC states	Samsung
R1-2605859	WUS operation in RRC states	BYD
R1-2605866	Discussion on WUS operation in RRC states	NEC
R1-2605923	Discussion on 6G WUS operation in different RRC states	OPPO
R1-2605985	Discussion on WUS operation in RRC states	Sony
R1-2606004	WUS operation in RRC states for 6GR	InterDigital, Inc.
R1-2606037	6G DL WUS operation in RRC states	Apple
R1-2606149	WUS operation in RRC states	MediaTek Inc.
R1-2606176	WUS operation in RRC states	China Telecom
R1-2606191	Discussion on WUS operation in RRC states	HONOR
R1-2606207	Discussion on DL WUS operation in RRC states for 6GR	LG Electronics
R1-2606254	Discussion on WUS operation in RRC states	ETRI
R1-2606318	DL WUS operation on different bands	Vodafone, Deutsche Telekom, Orange
R1-2606391	DL WUS Operation	Qualcomm Incorporated
R1-2606403	Discussion on WUS operation in RRC states	Google
R1-2606517	Discussion on WUS operation in RRC states	NTT DOCOMO, INC.
R1-2606539	Discussion on WUS operation in RRC states	ITRI
R1-2606581	Discussion on WUS operation in RRC states for 6G Radio	WILUS Inc.
R1-2606604	DL WUS operation in RRC states	Nordic Semiconductor ASA
R1-2606653	Discussion on WUS operation in RRC states	CEWiT
R1-2606682	Discussion on UE-Side Information for DL WUS Configuration Evaluation	NICT
R1-2606696	Discussion on DL-WUS operation in RRC states	TCL
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.6.1.2-a005`

### [6G/Rel-20 RAN1#126] `agreement` 10.6.2 Uplink WUS and operation

```text
For feasibility study of DS#1b, further study the following mechanisms for UE to acquire UL WUS configuration.
Option 1: Pre-configuration and/or pre-defined in specification
Option 2: Synchronization signal(s)
Option 3: PBCH including PBCH DMRS
Option 4: Broadcast PDSCH
Option 5: Common PDCCH
Note: Combination of above options can be considered.
At least the followings are considered for further study of the above options
NW configuration flexibility
NW and UE energy saving/consumption
UE complexity
Signaling overhead
Necessary payload by taking SIB26 for NR OD-SIB1 as the reference
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.6.2-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.6.2 Uplink WUS and operation

```text
For study of necessity for UL WUS, at least followings are considered as candidates of use cases.
For UEs in idle mode, and inactive mode,
UE-initiated on-demand or adaptation procedures for one or multiple of the following signals/channels:
6GR SS/PBCH
6GR SIB1
6GR PRACH
6GR DL Reference Signal
For UEs in connected mode,
UE-initiated on-demand or adaptation procedures for one or multiple of the following signals/channels:
6GR SS/PBCH
6GR SIB1
6GR PRACH
6GR DL Reference Signal
UL data indication (including ‘no UL data’ indication)
Selection of PUSCH resource and/or PUSCH transmission parameter
UL WUS based measurement
Indication of new beam for BFR (if supported for 6GR)
With consideration of at least the following aspects:
6GR SSB/SIB1 periodicity/repetition
Coverage
UL WUS detection performance
NW and UE energy/power consumption
Latency
NW and UE complexity
Resource overhead
Necessity of UE-triggered operation compared to NW-triggered mechanisms
Which DS(s) are applicable to the above use cases
Interference aspects
Inter-node coordination
Overlapping with existing or other 6GR mechanisms that could play the same functionalities
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.6.2-a002`

### [6G/Rel-20 RAN1#126] `agreement` 10.6.2 Uplink WUS and operation

```text
For study of feasibility for UL WUS, followings are observed for DS#2a in addition to previous RAN1 agreement.
If UE transmits UL WUS to cell/carrier #2, and if cell/carrier #1 and cell/carrier #2 are non-co-located,
UE can determine UL WUS transmission power as the pre-defined TX power (e.g., maximum TX power) Further study
Whether/how to mitigate interference to the cell/carrier other than cell/carrier #2
Whether/how to handle the impact to UL WUS detection performance
Whether UE can determine path-loss estimation from cell/carrier #1 DL signals and power offset value provided by cell/carrier #1 when available/applicable.
Details on how to use path-loss estimation from cell/carrier #1 DL signals
UE can use wide/omni-directional beam or beam sweeping as UL WUS transmission beam. Further study
How to handle the impact of reduced cell coverage, when using wide/omni-directional beam.
How to determine narrow beam and whether/how to mitigate interference to the cell/carrier other than cell/carrier #2.
UE can use cell/carrier #1 SSB as timing reference for UL WUS transmission when cell/carrier #1 and cell/carrier #2 are synchronized when the timing can be maintained in UE, or when cell#1/carrier #1 provides underlay coverage for cell#2/carrier #2.
It is required to further study whether/how UE can use cell/carrier #1 SSB as timing reference for UL WUS transmission or not, when cell/carrier #1 and cell/carrier #2 are not synchronized, considering inter-cell distance, timing advance, etc.
This can cover the scenario where UE moves from cell/carrier #1 to cell/carrier #2 (where cell/carrier #1 may not provide underlay coverage for cell/carrier #2) and can maintain DL timing/frequency synchronization and UL WUS configuration for a certain period of time
It is required to further study the duration of the certain period of time with coordination with RAN4 as needed
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.6.2-a003`

### [6G/Rel-20 RAN1#126] `agreement` 10.6.2 Uplink WUS and operation

```text
RAN1 to study necessary information and required payload size for UL WUS configuration, considering at least the following information and its necessity
Time and frequency domain resource size and location of UL WUS
Mapping between 6GR synchronization signal and UL WUS occasion
Parameters to determine UL WUS transmission power
Parameters to determine UL WUS sequence/format
Parameters for UE monitoring of response to UL WUS
Cell access related information
Note: SIB26 for NR OD-SIB1 is taken as a reference
Note: The above does not preclude that some necessary information may be implicitly determined, without need of explicit payload
R1-2606824	Summary #3 of uplink WUS and operation for 6GR	Moderator (LG Electronics)
R1-2606823	Summary #3 of uplink WUS and operation for 6GR	Moderator (LG Electronics)
R1-2606822	Summary #2 of uplink WUS and operation for 6GR	Moderator (LG Electronics)
R1-2606821	Summary #1 of uplink WUS and operation for 6GR	Moderator (LG Electronics)
R1-2605216	Discussion on 6G Uplink WUS and Operation	FUTUREWEI
R1-2605271	Discussion on Uplink WUS and operation	Spreadtrum, UNISOC
R1-2605306	UL-WUS and Operation	Huawei, HiSilicon
R1-2605317	Uplink WUS and operation	Ericsson
R1-2605329	Discussion on uplink WUS and operation for 6GR	Sharp
R1-2605399	On Uplink WUS and corresponding operation	Nokia
R1-2605481	Discussions on 6GR uplink WUS and operation	vivo
R1-2605496	Uplink WUS and operation	Tejas Networks Limited
R1-2605511	IMU Views on UL-WuS for 6GR	IMU
R1-2605515	Discussion on Uplink WUS and operation	Rakuten Symphony
R1-2605580	Discussion on Uplink WUS and operation for 6GR	Xiaomi
R1-2605648	Discussion on uplink WUS and operation	CMCC
R1-2605662	Discussion on UL-WUS Aspects in 6G	NEC
R1-2605683	Views on UL WUS	Ofinno
R1-2605738	Discussion on uplink WUS and operation	CATT
R1-2605787	Discuss on UL WUS	ZTE Corporation, Sanechips
R1-2605848	Discussion on Uplink WUS and operation	Samsung
R1-2605925	Discussion on 6GR UL WUS and operations	OPPO
R1-2605960	Uplink WUS and operation for 6GR	Panasonic
R1-2605986	Discussion on the Uplink WUS and operation	Sony
R1-2606005	Uplink WUS and operation for 6GR	InterDigital, Inc.
R1-2606038	On 6G UL WUS and operation	Apple
R1-2606150	Uplink WUS and operation	MediaTek Inc.
R1-2606208	Discussion on UL WUS and operation for 6GR	LG Electronics
R1-2606255	Discussion on uplink WUS and operation for 6GR	ETRI
R1-2606276	Uplink WUS Operation	Fraunhofer IIS, Fraunhofer HHI
R1-2606299	Uplink WUS and operation	Lenovo
R1-2606392	UL WUS Design and Operation	Qualcomm Incorporated
R1-2606404	Discussion on uplink WUS and operation	Google
R1-2606440	Discussion on UL WUS	ASUSTeK
R1-2606518	Discussion on Uplink WUS and operation	NTT DOCOMO, INC.
R1-2606582	Discussion on Uplink WUS and operation for 6G Radio	WILUS Inc.
R1-2606654	Discussion on Uplink WUS for 6GR	CEWiT
R1-2606697	Discussion on uplink WUS design and operation	TCL
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.6.2-a004`

### [6G/Rel-20 RAN1#126] `agreement` 10.6.3 WUS operation with other functionalities

```text
For the study of any information carried in DL-WUS with or, if supported, without the wake-up indication, RAN1 to at least use the following common assessment criteria:
Complexity of the UE EE processing and NW’s impact (if any);
Coverage impact of the resulting payload;
DL (and, where applicable, UL) resource overhead;
Energy-saving benefit at both UE side and network side, and latency impact;
Overlapping with existing or other 6GR mechanisms that could carry the same information
Whether DL-WUS used for other functions is beneficial than the existing or other 6GR mechanisms
The agreed FAR/FDR/MDR for DL WUS are used as the threshold for FAR/FDR/MDR of the additional (non-wake-up) information and associated functionality.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.6.3-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.6.3 WUS operation with other functionalities

```text
For UEs in RRC_IDLE / RRC_INACTIVE state, RAN1 to study at least the following candidate additional functions for DL-WUS:
Candidate #1: SI-modification and/or ETWS-CMAS notification carried via DL WUS.
Candidate #2: Use DL-WUS as a trigger or indication for on-demand and/or additional RS and/or common signals/channels, if supported.
Candidate #3: Use DL-WUS to indicate PF/PO resources or RACH occasions that can be used.
Candidate #4: Study DL WUS to trigger Downlink Small Data Transmission (DL SDT) in inactive state, if supported.
R1-2606842	FL Summary #2 on WUS operation with other functionalities	Moderator (Apple Inc.)
R1-2606749	FL Summary #1 on WUS operation with other functionalities	Moderator (Apple Inc.)
R1-2605272	Discussion on WUS operation with other functionalities	Spreadtrum, UNISOC
R1-2605313	WUS operation with other functionalities	Huawei, HiSilicon
R1-2605318	WUS operation with other functionalities	Ericsson
R1-2605400	WUS Operation with other functionalities	Nokia
R1-2605482	Discussion on WUS operation with other functionalities	vivo
R1-2605581	Discussion on other functions for 6GR WUS	Xiaomi
R1-2605649	Discussion on WUS operation with other functionalities	CMCC
R1-2605684	Views on DL WUS operation with other functionalities	Ofinno
R1-2605685	WUS operation with other functionalities	Lenovo
R1-2605739	Discussion on WUS operation with other functionalities	CATT
R1-2605788	Discuss on WUS with other functionalities	ZTE Corporation, Sanechips
R1-2605849	WUS Operation with Other Functionalities	Samsung
R1-2605867	Discussion on WUS operation with other functionalities	NEC
R1-2605924	Discussion on WUS with other functionalities	OPPO
R1-2606006	WUS operation with other functionalities	InterDigital, Inc.
R1-2606039	On WUS operation with other functionalities	Apple
R1-2606151	WUS operation with other functionalities	MediaTek Inc.
R1-2606735 	WUS operation with other functionalities	MediaTek Inc.
(Revision of R1-2606151)
R1-2606209	Discussion on WUS operation with other functionalities	LG Electronics
R1-2606256	Discussion on WUS operation with other functionalities	ETRI
R1-2606393	WUS Operation with Other Functionalities	Qualcomm Incorporated
R1-2606405	Discussion on WUS operation with other functionalities	Google
R1-2606519	Discussion on WUS operation with other functionalities	NTT DOCOMO, INC.
R1-2606655	Discussion on UL WUS operation with other functionalities	CEWiT
R1-2606698	Discussion on WUS operation with other functionalities	TCL
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.6.3-a002`

### [6G/Rel-20 RAN1#124b] `agreement` 10.6.1.1 Design of WUS with OFDM-based sequence

```text
For OFDM-based WUS sequence, further study time domain (e.g., DFT preprocessing) definition and frequency domain (w/o DFT preprocessing) definition with respect to the following aspects:
Link-level performance
BS implementation complexity
UE detection complexity
Frequency domain and time domain receiver processing
PAPR performance and relevancy
Multiplexing and coexistence with other signals and channels
R1-2603355	Summary #2 of 6GR DL WUS sequence design	Moderator (Ericsson)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.6.1.1-a001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.6.1.1 Design of WUS with OFDM-based sequence

```text
In FR2-1, the same SCS is assumed for DL WUS as for the 6GR Sync signals in the same band if sync signals and data channels use the same SCS.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.6.1.1-a002`

### [6G/Rel-20 RAN1#124b] `agreement` 10.6.1.1 Design of WUS with OFDM-based sequence

```text
The baseline reference configuration for link level coverage assessment of EE processing for DL WUS detection includes the following parameters referred to NR common PDCCH.
| Aggregation level | 8 |
| --- | --- |
| # Rx antennas (PDCCH) | 4 |
| CORESET | Refer to TR38.830 |
| PDCCH payload | 40-bits (excluding CRC) |
| # Tx antennas (WUS+PDCCH) | 2 |
R1-2603445	Summary #3 of 6GR DL WUS sequence design	Moderator (Ericsson)
From Friday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.6.1.1-a003`

### [6G/Rel-20 RAN1#124b] `agreement` 10.6.1.1 Design of WUS with OFDM-based sequence

```text
Study at least the 6GR sync signals for UE sync for DL WUS reception. Further study necessity (e.g., if 6GR sync signals are found to be insufficient for DL WUS) applicability and impact of additional synchronization method for DL WUS reception (e.g., additional sync signals or DL WUS with sync functionality).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.6.1.1-a004`

### [6G/Rel-20 RAN1#124b] `agreement` 10.6.1.1 Design of WUS with OFDM-based sequence

```text
At least the following assumptions are made of EE mode for DL WUS link level evaluations:
| Carrier frequency | 700 MHz | 3.5 GHz | 7 GHz |
| --- | --- | --- | --- |
| WUS SCS | 15 kHz | 30 kHz | 30 kHz |
| Channel model | [TDL-A, 30 ns delay spread] TDL-C, 300 ns delay spread |  |  |
| UE velocity | 3km/h |  |  |
| MDR/FAR assumptions | Baseline miss-detection rate (MDR) of DL WUS is FFS % Baseline false-alarm rate (FAR*) of DL WUS is FFS % *FAR, to be defined FFS if additional values need to be specified for RRC CONNECTED and/or RRC IDLE/INACTIVE modes, respectively |  |  |
| DL WUS BW | Up to 12, 24 or 48 PRBs Max 10 MHz BW Time domain resource to be reported by companies |  |  |
| Impairment modelling | Residual Frequency error up to [5] ppm, lower values to be reported by companies with the corresponding power assumptions Residual timing error up to [2] µs, lower values to be reported by companies with the corresponding power assumptions |  |  |
| Number of information bits | up to companies to report |  |  |
| Number of Rx antennas | 1, 2 |  |  |
R1-2603446	Final Summary of 6GR DL WUS sequence design	Moderator (Ericsson)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.6.1.1-a005`

### [6G/Rel-20 RAN1#124b] `agreement` 10.6.1.2 WUS operation in RRC states

```text
For RRC connected state, study feasibility and necessity of serving cell RRM measurement by EE processing, considering at least:
UE energy saving gain
Coverage (e.g., achievable SINR/SNR) and accuracy
Measurement metrics
Impact on the EE processing complexity
Based on at least 6GR sync signal
other signals
Other measurement
Whether there is spec impact or not
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.6.1.2-a001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.6.1.2 WUS operation in RRC states

```text
For RRC connected state, study feasibility and necessity of neighbouring cell RRM measurement by EE processing, considering at least:
UE energy saving gain
Neighbouring cell measurement type, e.g., intra-frequency, inter-frequency
Neighbouring cell identification, measurement and evaluation
Neighbouring cell number limitation if any
Inter-cell interference
Coverage (e.g., achievable SINR/SNR) and accuracy
Measurement metrics
Based on at least 6GR sync signal
other signals
Impact on the EE processing complexity
the power consumption of neighbouring cell RRM measurement based on EE processing
Other limitations if any
Whether there is spec impact or not
R1-2603451	Summary #3 on 6GR DL WUS operation in RRC states	Moderator (vivo)
From Friday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.6.1.2-a002`

### [6G/Rel-20 RAN1#124b] `agreement` 10.6.1.2 WUS operation in RRC states

```text
Study 6GR OFDM sequence based DL WUS for waking up UE for at least paging purpose in RRC idle state, considering at least:
UE energy saving gain
Impact to latency, if applicable
Network overhead, complexity, and energy consumption
Distributed PO/PF and clustered PO/PF
Association between WUS monitoring occasion and PO
UE behaviors after waking-up
WUS indication granularity and the number of information bits carried by DLWUS
WUS monitoring periodicity
WUS monitoring occasions
Multi-beam operation including at least QCL assumption
Consequence of false alarm/miss detection
Other impacts, if any
Other RRC state if supported
Other functionalities of 6GR DL WUS
Same or different carriers for DL WUS and paging
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.6.1.2-a003`

### [6G/Rel-20 RAN1#124b] `agreement` 10.6.1.2 WUS operation in RRC states

```text
For the RAN1 study on DL WUS triggering PDCCH monitoring with and without C-DRX in RRC CONNECTED state, include:
DL WUS is monitored periodically based on network configuration
Once DL WUS is detected, UE starts PDCCH monitoring for a time duration, after a time offset
the time duration, time offset
whether WUS is monitored during the time duration
How UE stops PDCCH monitoring
How UE stops and starts WUS monitoring
WUS triggering PDCCH monitoring is per cell or cell group
One or more DL WUS configurations
Other details if any
R1-2603452	Final summary on 6GR DL WUS operation in RRC states	Moderator (vivo)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.6.1.2-a004`

### [6G/Rel-20 RAN1#124b] `agreement` 10.6.2 Uplink WUS and operation

```text
For study of feasibility for UL WUS, at least followings are observed for DS#1b.
For the case where prior to UL WUS, always-on 6GR synchronization signals with PBCH on the standalone cell are transmitted,
UE can acquire DL timing/frequency synchronization for UL WUS transmission at least via always-on 6GR synchronization signals and PBCH transmitted by the standalone cell.
For the case where prior to UL WUS, always-on 6GR synchronization signals without PBCH on the standalone cell are transmitted,
It is required to further study whether UE can acquire DL timing/frequency synchronization for UL WUS transmission at least via always-on 6GR synchronization signals transmitted by the standalone cell.
For both cases,
UE can determine UL WUS transmission power at least based on always-on 6GR synchronization signals transmitted by the standalone cell and information to determine UL WUS transmission power, if information is available
It is required to further study whether/how information to determine UL WUS transmission power can be delivered to UE by e.g., PBCH, predefined in spec, or other methods
It is required to further study the minimum information size/content necessary at least for UL WUS transmission/operation and how such information can be delivered to UE.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.6.2-a001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.6.2 Uplink WUS and operation

```text
For study of feasibility for UL WUS, at least followings are observed for DS#2b.
If UE transmits UL WUS to cell/carrier #1,
UE can acquire DL timing/frequency synchronization for UL WUS transmission at least via always-on 6GR synchronization signals and PBCH transmitted by cell/carrier #1.
UE can determine UL WUS transmission power at least based on always-on 6GR synchronization signals transmitted by cell/carrier #1 and information to determine UL WUS transmission power, if information is possibly available at least from cell/carrier #1.
If UE transmits UL WUS to cell/carrier #2,
For the case where prior to UL WUS, always-on 6GR synchronization signals with PBCH on cell/carrier #2 are transmitted,
UE can acquire DL timing/frequency synchronization for UL WUS transmission at least via always-on 6GR synchronization signals and PBCH transmitted by cell/carrier #2, or the feasibility and applicability by cell/carrier #1
For the case where prior to UL WUS, always-on 6GR synchronization signals without PBCH on cell/carrier #2 are transmitted,
It is required to further study whether/how UE can acquire DL timing/frequency synchronization for UL WUS transmission at least via always-on 6GR synchronization signals transmitted by cell/carrier #2, or the feasibility and applicability by cell/carrier #1
UE can determine UL WUS transmission power at least based on always-on 6GR synchronization signals transmitted by cell/carrier #2 and information to determine UL WUS transmission power, if information is possibly available at least from cell/carrier #1.
Final summary in R1-2603343.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.6.2-a002`

### [6G/Rel-20 RAN1#124] `agreement` 10.6.1.1 Design of WUS with OFDM based sequence

```text
Targeting for same coverage as 6G PDCCH in the same band, Study DL WUS coverage by considering at least the following aspects.
Missed detection rate
False alarm rate
RRC state differences
Different use cases
Reference configuration of PDCCH
R1-2601607	Summary #2 of 6GR DL WUS sequence design	Moderator (Ericsson)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.6.1.1-a001`

### [6G/Rel-20 RAN1#124] `agreement` 10.6.1.1 Design of WUS with OFDM based sequence

```text
The same SCS is assumed for DL WUS as for the 6GR Sync signals in the same band if sync signals and data channels use the same SCS.
FFS SCS of DL WUS if sync signals and data channels use different SCS in FR2-1.
R1-2601724	Summary #3 of 6GR DL WUS sequence design	Moderator (Ericsson)
From Friday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.6.1.1-a002`

### [6G/Rel-20 RAN1#124] `agreement` 10.6.1.1 Design of WUS with OFDM based sequence

```text
Study the following aspects of DL WUS design:
Time or frequency domain sequence definition
Time and frequency resource allocation
Multiplexing and coexistence with other signals and channels, including DL WUS
PAPR and BS/UE processing complexity
Network overhead and NW&UE energy efficiency
Other aspects are not precluded
R1-2601725	Final summary of 6GR DL WUS sequence design	Moderator (Ericsson)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.6.1.1-a003`

### [6G/Rel-20 RAN1#124] `agreement` 10.6.1.2 WUS operation in RRC states

```text
Study 6GR DL WUS triggering PDCCH monitoring with and without C-DRX in RRC connected state, considering at least:
UE energy saving gain
Impact to UPT, if applicable
Impact to latency, if applicable
Impact to QoS/delay budget satisfaction rate, if applicable
Network overhead/complexity
Network energy consumption
Other impacts, if any
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.6.1.2-a001`

### [6G/Rel-20 RAN1#124] `agreement` 10.6.1.2 WUS operation in RRC states

```text
For RRC idle state, study serving cell RRM measurement based on 6GR measurement signal (e.g., at least 6GR sync signal) by EE processing, considering at least:
UE energy saving gain
measurement based on EE processing together with DL-WUS monitoring vs measurement based on non-EE processing together with DL-WUS monitoring
coverage (e.g., achievable SINR/SNR) and accuracy
Impact on the EE processing complexity
For RRC idle state, study neighboring cell RRM measurement based on 6GR measurement signal (e.g., at least 6GR sync signal) by EE processing, considering at least:
UE energy saving gain
measurement based on EE processing together with DL-WUS monitoring vs measurement based on non-EE processing together with DL-WUS monitoring
Neighboring cell identification, measurement and evaluation
Neighboring cell number limitation, if any
Inter-cell interference
Coverage (e.g., achievable SINR/SNR) and accuracy
Impact on the EE processing complexity
FFS the power consumption of neighboring cell RRM measurement based on EE processing
Note: It doesn’t mean the measurement in EE processing has to be coupled with DL WUS monitoring
R1-2601723	Final summary on 6GR DL WUS operation in RRC states	Moderator (vivo)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.6.1.2-a002`

### [6G/Rel-20 RAN1#124] `agreement` 10.6.2 Uplink WUS and operation

```text
Study further necessity and feasibility of UL WUS under the following deployment scenario (DS):
DS#1: Standalone cell where UE obtains UL WUS configuration e.g., from standalone cell and/or pre-defined in the specifications
DS#1a: Prior to UL WUS, nothing transmitted on the standalone cell
DS#1b: Prior to UL WUS, always-on 6GR synchronization signals with or without PBCH on the standalone cell but no SIB1 on the standalone cell
DS#1c: Prior to UL WUS, always-on 6GR synchronization signals with PBCH on the standalone cell and periodic SIB1 on the standalone cell
Note: UL WUS is transmitted to the standalone cell
RAN1 to consider at least
Coverage target of UL WUS
How UE acquires synchronization for UL WUS
How UE decides UL WUS transmission power
RRC states for the above scenarios
Note: The above scenarios can be applicable to multi-TRP deployment scenario if TRP is transparent to UE at the time of UL WUS transmission
Note: The above scenarios are for study purposes only and do not imply 6GR support.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.6.2-a001`

### [6G/Rel-20 RAN1#124] `agreement` 10.6.2 Uplink WUS and operation

```text
Study further necessity and feasibility of UL WUS under the following deployment scenario (DS):
DS#2: Multi-cell/carrier where UE obtains UL WUS configuration from cell/carrier #1
Always-on 6GR synchronization signals with PBCH on cell/carrier #1, and SIB1 on cell/carrier #1
DS#2a: Prior to UL WUS, nothing transmitted on cell/carrier #2
DS#2b: Prior to UL WUS, always-on 6GR synchronization signals with or without PBCH on cell/carrier #2 but no SIB1 on cell/carrier #2
DS#2c: Prior to UL WUS, 6GR synchronization signals with PBCH on cell/carrier #2 and periodic SIB1 on cell/carrier #2
Note: UL WUS can be transmitted to cell/carrier #1 or cell/carrier #2
RAN1 to consider at least
Coverage target of UL WUS
How UE acquires synchronization for UL WUS
How UE decides UL WUS transmission power
Whether the cells/carriers are in the same band or not
Whether the cells/carriers are collocated or not
RRC states for the above scenarios
Whether the above scenarios can be applicable to multi-TRP deployment scenario
Note: The above scenarios are for study purposes only and do not imply 6GR support.
Final summary in R1-2601660.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.6.2-a002`

