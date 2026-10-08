# 6GR 非地面网络

**当前进展** · 阶段：—

_尚无综述_

## 6GR 演进

### [6G/Rel-20 RAN1#126] `agreement` 10.7.1 NTN specific requirements and design

```text
For 6GR NTN GNSS-less/free/degraded PRACH, the differential time and frequency errors documented in TR 38.742 are taken as targets for the study with the addition of at least the following scenarios:
S-band LEO-300
Ka-band LEO-300
FFS: details of these scenarios, including differential time/frequency errors
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.7.1-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.7.1 NTN specific requirements and design

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

```text
For the 6GR NTN link budget template, for Ka/Ku band PDSCH and PUSCH link level evaluations, the PT-RS configuration is optional, and reported by companies if considered.
R1-2606420	Feature lead summary#3 on NTN specific requirements and design	Moderator (Qualcomm Incorporated)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.7.1-a003`

### [6G/Rel-20 RAN1#126] `agreement` 10.7.1 NTN specific requirements and design

```text
For the 6GR NTN link budget template, for Ka/Ku band link level evaluations, the UE and SAN phase noise model in clause 6.1.11.2 of TR38.803 can be optionally used for BPSK/QPSK (and in that case is reported by companies) and is used for higher order modulation (if evaluated for the link budget template)
NOTE: This agreement only applies to the 6GR NTN link budget template.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.7.1-a004`

### [6G/Rel-20 RAN1#126] `agreement` 10.7.1 NTN specific requirements and design

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

```text
In 6GR NTN, under the label of “physical layer aspects of multi-satellite operation”, the following sub-aspects are studied under “physical layer aspects related to inter-satellite interference management”
Co-channel interference, taking into account characteristics of NTN channels (e.g. large and time-varying Doppler / timing offsets due to orbital dynamics)
At least for LEO same orbit.
FFS other parameters (e.g. elevation angle)
NOTE: It is assumed that the UE is only connected to one satellite at a time.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.7.1-a006`

### [6G/Rel-20 RAN1#126] `conclusion` 10.7.1 NTN specific requirements and design

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

```text
For 6GR NTN, the link budget template attached to R1-2603091 is endorsed.
Note: “Candidate 2” is not considered for NTN.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.7.1-a002`

### [6G/Rel-20 RAN1#124b] `agreement` 10.7.1 NTN specific requirements and design for GNSS based operation

```text
In 6GR NTN, for the issue of satellite having more beam footprints than simultaneously active beams, study the following solutions, including their achievable coverage ratio of satellite and applicability:
Value of default SSB periodicity
Hierarchical beam structure (e.g. using beams of various sizes)
R1-2603093	Feature lead summary#3 on NTN specific requirements and design for GNSS based operation	Moderator (Qualcomm Incorporated)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.7.1-a003`

### [6G/Rel-20 RAN1#124b] `agreement` 10.7.1 NTN specific requirements and design for GNSS based operation

```text
For 6GR NTN study, RAN1 considers at least the following duplex types:
FD-FDD.
HD-FDD on UE side.
| Note the following is agreed in main session: On 6GR duplexing study, RAN1 considers at least following duplex types • FD-FDD • Semi-static TDD • gNB semi-static SBFD • HD-FDD on UE side • Dynamic TDD |
| --- |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.7.1-a004`

### [6G/Rel-20 RAN1#124b] `agreement` 10.7.1 NTN specific requirements and design for GNSS based operation

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

```text
For 6GR NTN evaluations, consider the following additional orbit for S-band, at least for link budget calculation purposes:
MEO-7000
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.7.1-a006`

### [6G/Rel-20 RAN1#124b] `agreement` 10.7.1 NTN specific requirements and design for GNSS based operation

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

```text
For 6GR NTN, RAN1 to study whether TA report is beneficial.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.7.1-a008`

### [6G/Rel-20 RAN1#124b] `agreement` 10.7.1 NTN specific requirements and design for GNSS based operation

```text
For 6GR NTN, at least for GNSS-based operation, study which parameters are needed for satellite assistance info for UL time-frequency pre-compensation, considering NR NTN parameters in SIB19 as starting point.
R1-2603364	Final feature lead summary on NTN specific requirements and design for GNSS based operation	Moderator (Qualcomm Incorporated)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.7.1-a009`

### [6G/Rel-20 RAN1#124b] `conclusion` 10.7.1 NTN specific requirements and design for GNSS based operation

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

```text
For NTN link budget template, RAN1 to take the TN link budget template as baseline with specific rows / values (including adding new rows) to be further discussed.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.7.1-a001`

### [6G/Rel-20 RAN1#124] `agreement` 10.7.1 NTN specific requirements and design for GNSS based operation

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

```text
6GR NTN targets to support GNSS-based operation, GNSS-degraded operation and GNSS-less/GNSS-free operation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.7.1-a004`

### [6G/Rel-20 RAN1#124] `agreement` 10.7.1 NTN specific requirements and design for GNSS based operation

```text
6GR NTN uplink time-frequency synchronization follows the same principle as NR NTN as baseline:
The concept of “uplink synchronization reference point” is introduced in 6GR NTN.
6GR NTN provides satellite assistance information
At least for GNSS-based operation, it is supported that UE uses its own location information + satellite assistance information to perform time-frequency pre-compensation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.7.1-a005`

### [6G/Rel-20 RAN1#124] `agreement` 10.7.1 NTN specific requirements and design for GNSS based operation

```text
6GR supports large scheduling offsets to accommodate the RTT introduced by the satellite channel. Further discuss how to realize these scheduling offsets:
Option 1: Reuse the k_offset concept from NR as a baseline with potential modifications.
NOTE: Under this option, additional scheduling offsets (e.g. similar to K1/K2 in NR) may be supported for scheduling flexibility, which apply in addition to k_offset.
Option 2: The large scheduling delays to accommodate the RTT are incorporated into the scheduling offsets (e.g. similar to K1/K2 in NR), which may or may not be common for TN and NTN.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.7.1-a006`

### [6G/Rel-20 RAN1#124] `agreement` 10.7.1 NTN specific requirements and design for GNSS based operation

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

```text
When reporting inputs for the link budget template and evaluation assumptions to RAN1#124b, companies are encouraged to provide them in an xls attached to their contribution following the format of the xls attached to R1-2601471.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.7.1-c002`

