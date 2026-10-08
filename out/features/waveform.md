# 6GR 波形与帧结构

**当前进展** · 阶段：—

_尚无综述_

## 6GR 演进

### [6G/Rel-20 RAN1#126] `agreement` 10.2.1 Waveform

```text
Agree on the embedded template for UL PAPR reduction scheme results collection in section 4.5 of R1-2606804.
Companies having evaluation results are encouraged to fill the template and upload it into the draft folder indicated by FL by 27th August EOD.
R1-2606804	Feature Lead summary #3 on 6G waveform	Moderator (Nokia)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.2.1-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.2.1 Waveform

```text
Endorse the updated observations in section 3.5 in R1-2606804
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.2.1-a002`

### [6G/Rel-20 RAN1#126] `agreement` 10.2.1 Waveform

```text
Complete the following list of UL PAPR reduction techniques for further down-selection
Option 1: FDSS with no spectrum extension or truncation
Transparent / non-transparent
Modulation: Pi/2 BPSK / QPSK
Applicable SE range: FFS
Option 2: FDSS with spectrum extension
Transparent / non-transparent
Modulation: Pi/2 BPSK / QPSK / 16QAM
Applicable SE range: FFS
Option 3: FDSS with spectrum truncation
Transparent / non-transparent
Modulation: Pi/2 BPSK
Applicable SE range: FFS
FFS: condition on when to apply finally selected option/scheme
Note: target to down select transparent / non-transparent and modulation (at least on 16QAM) for above options at RAN1#126bis
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.2.1-a003`

### [6G/Rel-20 RAN1#126] `agreement` 10.2.1 Waveform

```text
For DFT size before SE/ST is applied, at least option 1 is supported, and whether option 2 is supported or not is further discussed and to be decided by RAN1#127
Option 1: 12 * 2x3y5z subcarriers.
Option 2: X * 2x3y5z subcarriers, where X = 4.
FFS: upper bound on applicable number of RBs for option 2
R1-2606805	Feature Lead summary #4 on 6G waveform	Moderator (Nokia)
R1-2606806	Feature Lead summary #5 on 6G waveform	Moderator (Nokia)
Final post-meeting summary on this agenda item.
[Post-126-6GR-waveform] – Karri (Nokia)
Email discussion to collect additional evaluation results from 28th to 30th Sept.
Note: additional evaluation results captured into the template should also be submitted in contribution for Oct. meeting.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.2.1-a004`

### [6G/Rel-20 RAN1#124b] `agreement` 10.2.1 Waveform

```text
Prioritize the following cases in the RAN1 study on UL coverage improvements through low UL PAPR enhancement for DFT-s-OFDM, based on Table in 5.3.1 of R1-2603312:
FDSS [for π/2 BPSK, QPSK, 16QAM]
Opt1: Transparent filter
Filter defined through transmitter requirement such as spectrum flatness by RAN4
Opt2: non-transparent filter
Filter coefficients specified in RAN1
Note: This includes all the listed FDSS filtering variants
FDSS for [π/2 BPSK, QPSK, 16QAM] with spectral extension
For FDSS part,
Opt1: Transparent filter
Filter defined through transmitter requirement such as spectrum flatness by RAN4
Opt2: non-transparent filter
Filter coefficients specified in RAN1
Note: This includes all the listed variants of the spectrum extension
FDSS for π/2 BPSK with spectral truncation
For FDSS part,
Opt1: Transparent filter
Filter defined through transmitter requirement such as spectrum flatness by RAN4
Opt2: non-transparent filter
Filter coefficients specified in RAN1
Note: This includes all the listed variants of the spectrum truncation
Note: At least one variant of spectral extension, offset-QPSK with smaller DFT size can result in the same signal as the FDSS for π/2 BPSK-ST
Note: companies are encouraged to report whether transparent CFR is used or not
R1-2603313	Feature Lead summary #4 on 6G waveform	Moderator (Nokia)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.2.1-a001`

### [6G/Rel-20 RAN1#124b] `conclusion` 10.2.1 Waveform

```text
The study on the following listed proposals is noted. Further discussion on these is not planned under the waveform agenda item in RAN1 unless tasked by RAN at or after RAN#112.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.2.1-c001`

### [6G/Rel-20 RAN1#124b] `observation` 10.2.1 Waveform

```text
Max-rank = 2 for UL DFT-s-OFDM
Companies report negligible SNR loss from DFT-s-OFDM with larger number of aNB Rx antenna elements, such as at least 16 or 32. Link level loss with 4 layers has not been studied. A lower number of aNB antenna elements may result with SNR loss at the receiver
All companies acknowledge that when the UE is Tx power limited, there is a Tx power gain from DFT-s-OFDM, highest reported gain of around 2.5dB.
The system level impact depends on scenario and scheduling strategy due to vastly differing probabilities for UE to be power limited and use rank=2, as well as the used traffic model and the assumed number of aNB Rx antenna elements. The reference setup to compare with varied and had also an impact to the findings, including also system loading, link adaptation, scheduling strategy, the used UE antenna model and the number of aNB Rx antenna elements.
Two companies reported cases with average system level throughput loss [R1-2601827, R1-2602177], of which one company indicated cell edge throughput loss [R1-2602177]. One company reported no average and cell-edge system level throughput gain [R1-2602254], while 6 companies reported cases with average system level throughput gains and/or cell edge throughput gains [R1-2602004, R1-2603056, R1-2602468, R1-2603008, R1-2603286 , R1-2601921].
Codebook for multi-layer UL DFT-s-OFDM
The lower PAPR property of DFT-s-OFDM is diminished with coherent precoders due to mixing of two (or more) layers for each power amplifier.
RAN1#124 agreed to focus the DFT-s-OFDM studies to non-coherent CB only (with the exception of lower number of layers than Tx antennas) for 2Tx UE for waveform evaluation purposes.
Four companies report moderate system level gains for DFT-s-OFDM non-coherent codebook only relative to CP-OFDM non-coherent codebook [R1-2603056, R1-2602468, R1-2603008, R1-2603286], while two companies report system level loss for DFT-s-OFDM non-coherent codebook only relative to CP-OFDM non-coherent codebook [R1-2601827, R1-2602177].
One company reports system level gains also for DFT-s-OFDM with coherent codebook relative to CP-OFDM with coherent codebook [R1-2602468].
Six companies report system level gains for DFT-s-OFDM with non-coherent multi-layer codebook and coherent single-layer codebook relative to CP-OFDM with coherent single/multi-layer codebook [R1-2602426, R1-2602468, R1-2602004, R1-2603008, R1-2603286, R1-2601921], while one company reports no system level gain for DFT-s-OFDM with non-coherent multi-layer codebook and coherent single-layer codebook relative to CP-OFDM with coherent single/multi-layer codebook [R1-2602254].
Dynamic waveform switching
One company observes comparable system level performance for DWS among DFT-s-OFDM for both 1- and 2-layer and CP-OFDM with both 1-layer and 2-layer compared to DWS among DFT-s-OFDM for only 1-layer and CP-OFDM for both 1- and 2-layer for full buffer traffic only and observes gain for non-full buffer traffic [R1-2603286].
One company observes system level loss of DFT-s-OFDM for both 1- and 2-layer compared to DFT-s-OFDM for only 1-layer and CP-OFDM for both 1- and 2-layer with waveform switching [R1-2601827].
One company observes comparable system level performance for DWS among DFT-s-OFDM for both 1- and 2-layer and CP-OFDM with both 1-layer and 2-layer compared to DWS among DFT-s-OFDM for only 1-layer and CP-OFDM for both 1- and 2-layer. [R1-2602254].
One company observes system level performance loss of DFT-s-OFDM for 1-layer and DFT-s-OFDM/CP-OFDM for 2-layer compared to DFT-s-OFDM for only 1-layer and CP-OFDM for both 1-layer and 2-layer with waveform switching [R1-2602177].
Note: this observation is not intended to be captured as it is in TR.
R1-2603314	Feature Lead summary #5 on 6G waveform	Moderator (Nokia)
Presented in Friday session
R1-2603315	Feature Lead summary #6 on 6G waveform	Moderator (Nokia)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.2.1-o001`

### [6G/Rel-20 RAN1#124b] `proposal` 10.2.1 Waveform

```text
Company providing evaluation (please include the Tdoc#)
Based on your results, indicate if you believe that the proposal should be considered for potential inclusion to 6GR
TR (downlink)
ZTE (R1-2602275)
ZTE: YES
DFT-s-OFDM with enhanced time domain resource multiplexing
ZTE (R1-2602275)
ZTE: YES
GFB-OFDM
ZTE (R1-2602275)
ZTE: YES
SLM
ZTE (R1-2508856)
CATT（R1-2602492）
ZTE: YES
CATT: YES
Zak-OTFS-over-OFDM
Cohere (R1-2602263)
Cohere: YES
Zak-OTFS
Cohere (R1-2602263)
Cohere: YES
Interlace OFDM
Spectral Precoding
NICT(R1-2602831)
NICT: YES
OSDM
Sheffield (R1-2602259)
Shef: YES
CP-OFDM with time-domain precoding
PCL (R1-2602302)
PCL: YES
DFT-s-OFDM with flexible frequency domain mapping (e.g., frequency domain data-DMRS multiplexing)
QC (R1-2603008)
CATT（R1-2602492）
QC: Yes
CATT: Yes
Multi-Tx Enhancement for DFT-s-OFDM
QC (R1-2603008)
IITH, Wisig (R1-2602880)
QC: Yes
IITH, Wisig: Yes
Two-segment DFT-S-OFDM
CATT（R1-2602492）
CATT:Yes
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.2.1-p001`

### [6G/Rel-20 RAN1#124] `agreement` 10.2.1 Waveform

```text
Extend the RAN1#123 endorsed table to characterize each (waveform) proposal as a potential RAN1 observation as follows to cover also impacts to transmitter and receiver processing operation:
|  | Description |
| --- | --- |
| Name of the proposal |  |
| Motivation of the proposal | E.g. TN, NTN, ISAC, etc… |
| Applicable link direction | DL/UL/both |
| Enhancement to CP-OFDM? | No/Yes |
| Enhancement to DFT-s-OFDM? | No/Yes |
| Additional OFDM-compatible waveform? | No/Yes |
| Target channel(s)/signal(s) | PDCCH/PDSCH/PUCCH/PUSCH/xxx |
| Target modulation |  |
| Motivation / use case | Improved spectral efficiency, … |
| Key Metric / KPI | Spectral efficiency, … |
| Key spec impact foreseen |  |
| MRSS compatibility | Please explain |
| Multiplexing/coexistence with other waveforms | Please explain |
| Multi-user multiplexing | Please explain |
| MIMO compatibility | Please explain |
| Implementation/operation impacts on transmitter processing | Please explain |
| Implementation/operation impacts on receiver processing | Please explain |
R1-2600787	Feature Lead summary #2 on 6G waveform	Nokia
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.2.1-a001`

### [6G/Rel-20 RAN1#124] `agreement` 10.2.1 Waveform

```text
For the evaluations of spectrum extension and spectrum truncation for UL low-PAPR solutions, the number of subcarriers A before extension / truncation is
Option 1: 12 * 2x3y5z subcarriers
Option 2: 2x3y5z subcarriers
FFS: whether the maximum value for A is needed
Note: Companies are encouraged to investigate above options and bring inputs to RAN1#124bis.
Note: the occupied bandwidth B is given in terms of number of RBs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.2.1-a002`

### [6G/Rel-20 RAN1#124] `agreement` 10.2.1 Waveform

```text
NR Rel-15 DFT-s-OFDM should be used as the baseline reference when evaluating the gains of UL low-PAPR proposals.
R1-2600788	Feature Lead summary #3 on 6G waveform	Nokia
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.2.1-a003`

### [6G/Rel-20 RAN1#124] `agreement` 10.2.1 Waveform

```text
Following metrics are used for SLS evaluations for multi-layer UL DFT-s-OFDM and CP-OFDM studies.
User perceived throughput (UPT), including:
High percentile (90%)
mean
median
cell edge (5 & 10-percentile)
Optional for full buffer traffic only: cell average throughput
Companies are encouraged to report the CDF of instantaneous UL TX power across all UEs
Companies are encouraged to report the statistics on the UL TX rank.
Companies are encouraged to report the statistics on the applied MCS.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.2.1-a004`

### [6G/Rel-20 RAN1#124] `agreement` 10.2.1 Waveform

```text
Following metrics are used for LLS evaluation for multi-layer UL DFT-s-OFDM and CP-OFDM studies.
BLER curves (for a subset of NR MCS (covering whole range with spanning), HARQ re-transmissions disabled) for same transmission rank, for same resource allocation and same transmission power for DFT-s-OFDM and CP-OFDM
Companies may derive Link-level throughput vs SNR based on BLER curves
Netgain
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.2.1-a005`

### [6G/Rel-20 RAN1#124] `agreement` 10.2.1 Waveform

```text
For 2-layer/2Tx UL DFT-s-OFDM and CP-OFDM studies, following two cases are considered.
UE capable of only non-coherent precoder
For UL CP-OFDM and DFT-s-OFDM rank-2 transmission, only non-coherent precoder option is allowed.
UE capable of fully-coherent precoder
For UL CP-OFDM rank-2 transmission, all NR precoder options are allowed.
For UL DFT-s-OFDM rank-2 transmission, only non-coherent precoder option is allowed.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.2.1-a006`

### [6G/Rel-20 RAN1#124] `agreement` 10.2.1 Waveform

```text
For the multi-layer UL DFT-s-OFDM and CP-OFDM studies, the NR reference should be evaluated assuming the Release 16 full power mode 1 to be enabled.
R1-2600789	Feature Lead summary #4 on 6G waveform	Nokia
From Friday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.2.1-a007`

### [6G/Rel-20 RAN1#124] `agreement` 10.2.1 Waveform

```text
The following UL low-PAPR proposals for DFT-s-OFDM are for further consideration:
Non-AI-ML-based
FDSS (R1-2601092, R1-2600751, R1-2600801, R1-2600823, R1-2600914, R1-2601156)
FDSS – spectrum extension (R1-2600027, R1-2601092, R1-2600823, R1-2600751, R1-2600914, R1-2601156, R1-2600261)
FDSS – spectrum truncation for π/2 BPSK (R1-2601268, R1-2601212, R1-2601092, R1-2601156)
Tone Reservation (R1-2600261, R1-2600716, R1-2601268)
For π/2 BPSK or other modulation orders
GMSK-Approximation based FDSS (R1-2600823)
3-tap filter based FDSS (R1-2508684)
CFR-SE (R1-2600499)
Offset-QAM or π/2-PAM with FDSS-spectrum truncation (R1-2600909, R1-2600138, R1-2601268, R1-2600751)
Offset-QAM or π/2-PAM with FDSS-spectrum extension (R1-2600909, R1-2600138, R1-2600751, R1-2600823)
Interpolation-based modulation (R1-2600261)
AFDM based on DFT-s-OFDM (R1-2600999, R1-2601019)
AI-ML-based
AI/ML-based waveform (R1-2600499, R1-2600751)
Note: tdoc numbers described in each proposal provide information on the proposal for further consideration, and it does not mean these tdocs support the proposal.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.2.1-a008`

### [6G/Rel-20 RAN1#124] `conclusion` 10.2.1 Waveform

```text
DFT-s-OFDM waveform including related enhancements for 6GR Downlink will be no further discussed as part of AI 10.2.1.
Note: for DL signal (e.g., SS, WUS, sensing), it may or may not be separately discussed in corresponding AI.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.2.1-c001`

### [6G/Rel-20 RAN1#124] `conclusion` 10.2.1 Waveform

```text
Studies on UL coverage improvements through low UL PAPR enhancement for DFT-s-OFDM are to be handled with high priority in AI 10.2.1.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.2.1-c002`

### [6G/Rel-20 RAN1#124] `conclusion` 10.2.1 Waveform

```text
Studies on DFT-s-OFDM for multi-rank UL MIMO are to be handled with high priority in AI 10.2.1.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.2.1-c003`

### [6G/Rel-20 RAN1#124] `conclusion` 10.2.1 Waveform

```text
Further clarifications on evaluations of UL low-PAPR proposals for DFT-s-OFDM:
In the evaluation assumptions, companies should disclose the necessary knowledge (e.g., filter coefficients, extension scheme, …) of the waveform at the receiver to process if any.
R1-2601696	Feature Lead summary #5 on 6G waveform	Moderator (Nokia)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.2.1-c004`

