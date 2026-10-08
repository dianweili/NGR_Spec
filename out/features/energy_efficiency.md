# 6GR 能效

**当前进展** · 阶段：—

_尚无综述_

## 6GR 演进

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

