# 6GR 多天线系统

**当前进展** · 阶段：—

_尚无综述_

## 6GR 演进

### [6G/Rel-20 RAN1#126] `agreement` 10.5.1.1 Synchronization acquisition and beam measurement

```text
For the link budget evaluations in around 7 GHz for coverage gap identification, the assumptions for the receiver noise figure are 9 dB and 5 dB for DL and UL respectively (agreed in RAN1#124)
Send an LS to RAN4 about the assumptions for information only.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.1.1-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.1.1 Synchronization acquisition and beam measurement

```text
For the link budget evaluations for the coverage gap identification, no update to the cell area reliability for initial-access related signals/channels, i.e., 95% for control channel, SSB and SIB1 and 90% for other channels that are capable of HARQ retransmissions but HARQ retransmissions are not assumed.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.1.1-a002`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.1.1 Synchronization acquisition and beam measurement

```text
Support Resource block boundaries alignment between NR and 6GR on a MRSS carrier.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.1.1-a003`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.1.1 Synchronization acquisition and beam measurement

```text
In 6GR, aNB-side semi-static SBFD is supported.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.1.1-a004`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.1.1 Synchronization acquisition and beam measurement

```text
One 6GR SSB spans 20 RBs
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.1.1-a005`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.1.1 Synchronization acquisition and beam measurement

```text
For one 6G SSB, the number of RBs for PSS is 12 RBs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.1.1-a006`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.1.1 Synchronization acquisition and beam measurement

```text
Study the following aspects for 6GR PSS
Sequence type
Option 1: m-sequence
Option 2: ZC-based sequence
Option 3: Other sequence
Sequence length
Option 1: 127
Option 2: 127<L<=144
Number of sequences
Number of symbols for PSS
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.1.1-a007`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.1.1 Synchronization acquisition and beam measurement

```text
Study the following aspect for 6GR SSS
Sequence type
Gold sequence as a benchmark
FFS: Other sequences
Sequence length
Option 1: 127
Option 2: > 127
Number of sequences
Number of symbols for SSS
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.1.1-a008`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.1.1 Synchronization acquisition and beam measurement

```text
Final LS R1-2606913 with following contents is agreed.
1. Overall Description:
In the study of “Re-use of existing 5G mid-band (~3.5GHz) site grid for 6G deployments in at least around 7 GHz and targeting comparable coverage to 5G mid-band”, RAN1 made an agreement that for the link budget evaluations in around 7 GHz for coverage gap identification, the assumptions for the receiver noise figure are 9 dB and 5 dB for DL and UL respectively. There is no implication that RAN4 should use the same assumption.
2. Actions:
To RAN4
ACTION: RAN1 would like to respectfully inform RAN4 about the above receiver noise figure assumptions.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.1.1-a009`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.1.1 Synchronization acquisition and beam measurement

```text
The coverage gap between ~7GHz and 5G mid-band for different signals and channels during initial access are identified in the following tables.
Table X: Coverage gap between 7.0 GHz and 5G mid-band (3.5 GHz) for different signals and channels during initial access for UMa O2I
| Signals/channels | Number of Sample(s) | Coverage gap (trimmed mean) | Standard Deviation (w/o outlier) |
| --- | --- | --- | --- |
| PSS/SSS w/o combining | 11 | -7.24 | 1.63 |
| PBCH w/o combining | 9 | -8.32 | 1.83 |
| PSS/SSS w/ 4 combining | 8 | -4.08 | 1.30 |
| PBCH w/ 4 combining | 14 | -3.09 | 1.62 |
| SIB1 PDCCH | 17 | -5.56 | 1.63 |
| SIB1 PDSCH | 16 | -6.91 | 1.68 |
| Msg2 PDSCH | 11 | -3.96 | 2.61 |
| Msg4 PDSCH | 13 | -4.11 | 1.77 |
| PRACH format 0 | 14 | -2.73 | 1.43 |
| PRACH format B4 | 14 | -4.80 | 2.19 |
| PRACH format C2 | 11 | -8.37 | 1.21 |
| Msg3 PUSCH | 20 | -8.68 | 1.67 |
| Msg5 PUSCH | 11 | -13.00 | 2.98 |
| PUCCH format 1 | 13 | -3.64 | 2.33 |
Comparing the coverage between 3.5GHz and 2.6GHz in UMa O2I, there is 4.5 dB difference for Msg 3, which is assumed to be applicable for all signals/channels.
Table X: Coverage gap between 7.0 GHz and 5G mid-band (3.5 GHz) for different signals and channels during initial access for UMa O2O
| Signals/channels | Number of Sample(s) | Coverage gap (trimmed mean) | Standard Deviation (w/o outlier) |
| --- | --- | --- | --- |
| PSS/SSS w/o combining | 5 | -2.81 | 0.33 |
| PBCH w/o combining | 4 | -1.51 | 0.13 |
| PSS/SSS w/ 4 combining | 6 | 1.13 | 2.15 |
| PBCH w/ 4 combining | 9 | 1.69 | 1.52 |
| SIB1 PDCCH | 8 | -1.28 | 0.65 |
| SIB1 PDSCH | 9 | -2.92 | 1.33 |
| Msg2 PDSCH | 6 | 0.21 | 2.61 |
| Msg4 PDSCH | 7 | -1.06 | 1.64 |
| PRACH format 0 | 8 | 2.54 | 0.57 |
| PRACH format B4 | 7 | 0.22 | 1.68 |
| PRACH format C2 | 7 | -4.09 | 1.47 |
| Msg3 PUSCH | 11 | -3.75 | 1.11 |
| Msg5 PUSCH | 6 | -10.19 | 3.01 |
| PUCCH format 1 | 5 | -0.03 | 1.12 |
Comparing the coverage between 3.5GHz and 2.6GHz in UMa O2O, there is 2.58 dB difference for Msg 3, which is assumed to be applicable for all signals/channels.
Table X: Coverage gap between 7.0 GHz and 5G mid-band (3.5 GHz) for different signals and channels during initial access for SMa O2I
| Signals/channels | Number of Sample(s) | Coverage gap (trimmed mean) | Standard Deviation (w/o outlier) |
| --- | --- | --- | --- |
| PSS/SSS w/o combining | 5 | -3.64 | 0.44 |
| PBCH w/o combining | 3 | -2.16 | N/A |
| PSS/SSS w/ 4 combining | 4 | -1.27 | 1.47 |
| PBCH w/ 4 combining | 7 | 1.11 | 0.99 |
| SIB1 PDCCH | 7 | -1.80 | 0.60 |
| SIB1 PDSCH | 7 | -3.35 | 1.21 |
| Msg2 PDSCH | 5 | 0.68 | 2.01 |
| Msg4 PDSCH | 5 | -1.91 | 1.35 |
| PRACH format 0 | 7 | 1.88 | 0.59 |
| PRACH format B4 | 5 | -1.40 | 1.54 |
| PRACH format C2 | 6 | -5.23 | 1.09 |
| Msg3 PUSCH | 7 | -4.01 | 0.41 |
| Msg5 PUSCH | 5 | -11.76 | 2.88 |
| PUCCH format 1 | 4 | -0.22 | 0.89 |
Table X: Coverage gap between 7.0 GHz and 5G mid-band (3.5 GHz) for different signals and channels during initial access for SMa O2O
| Signals/channels | Number of Sample(s) | Coverage gap (trimmed mean) | Standard Deviation (w/o outlier) |
| --- | --- | --- | --- |
| PSS/SSS w/o combining | 5 | -2.81 | 0.33 |
| PBCH w/o combining | 3 | -1.42 | N/A |
| PSS/SSS w/ 4 combining | 4 | -0.50 | 1.25 |
| PBCH w/ 4 combining | 7 | 1.92 | 1.03 |
| SIB1 PDCCH | 7 | -1.18 | 0.67 |
| SIB1 PDSCH | 7 | -2.67 | 1.21 |
| Msg2 PDSCH | 5 | 1.07 | 2.40 |
| Msg4 PDSCH | 5 | -0.85 | 1.24 |
| PRACH format 0 | 7 | 2.60 | 0.61 |
| PRACH format B4 | 5 | -0.82 | 1.17 |
| PRACH format C2 | 6 | -4.60 | 1.05 |
| Msg3 PUSCH | 7 | -3.21 | 0.49 |
| Msg5 PUSCH | 5 | -11.13 | 2.88 |
| PUCCH format 1 | 4 | 0.56 | 0.67 |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.1.1-a010`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.1.1 Synchronization acquisition and beam measurement

```text
For the MaxCL requirement in TR 38.914, companies are encouraged to provide MaxCL evaluations based on the following assumptions:
Assumptions used for maxCL calculations in TR38.914:
Table 5.1.20.1-2: MaxCL calculation assumptions
| UE Tx power | 23dBm |
| --- | --- |
| DL Tx power | 46dBm |
| BS receiver noise figure | 5dB |
| UE receiver noise figure | 9dB |
| Interference margin | 0dB |
Note: DL Tx power is 46dBm per 20 MHz and scales with wider bandwidth.
Carrier frequency, duplex and SCS
FDD, carrier frequency: 0.7 GHz, 15kHz SCS
TDD, carrier frequency: 2.6 GHz, 30kHz SCS
UE speed: 3kmh
Channel model
TDL-C with 300ns delay spread
DL: 2T2R and 2T1R
UL: 1T2R
Signals/channels to be evaluated
DL: NR PSS/SSS, PBCH, Common PDCCH, SIB1 PDSCH, Msg2/4 PDSCH
UL: NR PRACH format C2/B4/0, MSG3 PUSCH, MSG5 PUSCH (companies to report assumption of the payload of actual transmission),  MSG4 PUCCH Format 1
The simulation assumptions in section A.1 in TR38.830 are used as a starting point.
The payload for NR SIB1 PDSCH is 1200 bits.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.1.1-a011`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.1.1 Synchronization acquisition and beam measurement

```text
Capture the evaluation results from companies on NES evaluations into the TR
Note: Evaluation results can be updated in the next meeting.
| Company | BS Cat | Load (RU) | Configuration | 40 ms | 80 ms | 160 ms |
| --- | --- | --- | --- | --- | --- | --- |
| Mid-band (~2-4 GHz) — NES gains vs 20 ms baseline |  |  |  |  |  |  |
| CEWiT [R1-2606646] | Cat 1 | 5% / 10% / 20% | SLS 21-cell, SIB1 retained at 20 ms | – | 23.4% / 19.3% / 16.4% | 24.9% / 20.8% / 17.5% |
| CEWiT [R1-2606646] | Cat 1 | 5% / 10% / 20% | SLS 21-cell, SIB1 and common signals CLUSTERED | – | 51% / 47.8% / 45.4% | 56.3% / 52.7% / 49.5% |
| OPPO [R1-2605917] | Cat 1 / Cat 2 / Cat 2.1 | 0% | — | 32% / 20% / 20% | 67% / 31% / 31% | 81% / 36% / 62% |
| OPPO [R1-2605917] | Cat 1 / Cat 2 / Cat 2.1 | Low NA | — | 23% / 16% / 16% | 40% / 23% / 24% | 49% / 27% / 30% |
| OPPO [R1-2605917] | Cat 1 / Cat 2 / Cat 2.1 | Light NA. | — | 15% / 11% / 11% | 24% / 16% / 16% | 28% / 19% / 19% |
| OPPO [R1-2605917] | Cat 1 / Cat 2 / Cat 2.1 | Med NA | — | 9% / 7% / 7% | 14% / 11% / 11% | 17% / 12% / 13% |
| Samsung [R1-2605823] | Cat 1 / Cat 2 | 0% | — | 36% / 26.2% | 72.3% / 39.3% | 85.6% / 45.8% |
| Samsung [R1-2605823] | Cat 1 / Cat 2 | 14% | — | 19.5% / 5.2% | 29.5% / 13.6% | 34.7% / 14.6% |
| Qualcomm [R1-2606375] | Cat 1 / Cat 2 | 0% | — | 18% / 3.7% | 57% / 5.5% | 78% / 6.5% |
| Qualcomm [R1-2606375] | Cat 1 / Cat 2 | 5% | — | 11% / 3.1% | 18% / 4.5% | 19% / 5.5% |
| Qualcomm [R1-2606375] | Cat 1 / Cat 2 | 15% | — | 5% / 2.1% | 8% / 3.7% | 9% / 4.2% |
| Ericsson [R1-2605521] | Cat 1 | 0% / 4% | — | 13% / 12% | 62% / 38% | 80% / 62% |
| Ofinno [R1-2605675] | Cat 1 / Cat 2 | 0% | Set 1 | 11% / 8% | 72% / 12% | 84% / 14% |
| Ofinno [R1-2605675] | Cat 1 / Cat 2 | 0% | Set 2 | 21% / 11% | 59% / 16% | 78% / 19% |
| Ofinno [R1-2605675] | Cat 1 / Cat 2 | 0% | Set 3 | 12% / 37% | 87% / 55% | 93% / 64% |
| Spreadtrum [R1-2605254] | Cat 2.1 | 0% | — | 12.48% | 18.71% | – |
| ZTE [R1-2605431] | Cat 1 | 0% | SSB + SIB1 + PRACH all at 160 ms | – | – | 53.5% |
| ZTE [R1-2605431] | Cat 1 | Low n.s. | SSB + SIB1 + PRACH at 160 ms | – | – | 32.9% |
| Lenovo [R1-2606336] | Cat 1 | 0% | Clustered SSB | – | 23.5% | 61% |
| Lenovo [R1-2606336] | Cat 1 | 0% | Non-clustered SSB | 20.5% | 57% | 77.5% |
| HONOR [R1-2606186] | Cat 1 | 0% | 20 → 160 ms | – | – | 80% |
| InterDigital [R1-2605686] | Cat 1 / Cat 2 / Cat 2.1 | ~5% | Single beam | 49.4%/3.9%/3.9% | 53.1%/5.9%/43.1% | 54.9%/6.9%/45.1% |
| InterDigital [R1-2605686] | Cat 1 / Cat 2 / Cat 2.1 | ~25% | Single beam | 15.4%/1.6%/1.6% | 17.3%/2.4%/15.4% | 18.2%/2.9%/17.9% |
| InterDigital [R1-2605686] | Cat 1 / Cat 2 / Cat 2.1 | ~5% | 4 beams | 48.4%/13.5%/13.5% | 58.7%/20.3%/49.2% | 63.8%/23.8%/53.7% |
| InterDigital [R1-2605686] | Cat 1 / Cat 2 / Cat 2.1 | ~25% | 4 beams | 19.1%/7.3%/6.3% | 24.1%/9.7%/21.3% | 26.8%/11.5%/25.1% |
| Huawei [R1-2605291] | Cat 1 | 0% / 4% / 8% | 8 beams, no AD-SS | baseline | 19% / 18% / 17% | 31% / 30% / 28% |
| Huawei [R1-2605291] | Cat 1 | 0% / 4% / 8% | 4 beams, no AD-SS | baseline | 30% / 22% / 20% | 44% / 37% / 33% |
| Huawei [R1-2605291] | Cat 1 | 0% / 4% / 8% | 8 beams, WITH AD-SS | baseline | 12% / 12% / 11% | 21% / 20% / 19% |
| Huawei [R1-2605291] | Cat 1 | 0% / 4% / 8% | 4 beams, WITH AD-SS | baseline | 22% / 15% / 13% | 31% / 25% / 23% |
| Nokia (R1- 2601832 | Cat 2 | 0% | SSB and SIB1 same periodicity and in consegutive slots, 8 beams | 27% | 41% | 48% |
| Nokia (R1- 2601832) | Cat 2.1 | 0% | SSB and SIB1 same periodicity and in consegutive slots, 8 beams | 27% | 41% | 66% |
| Xiaomi [R1-2605563] | Cat 1/Cat 2 | 0% | SS#0 period of 20ms, PO period of 1.28s, RO period of 10ms | 39.3%/9.3% | 45% / 13.1% | 49% / 15.9 |
| Mid-band (~2–4 GHz), reference configuration Set 1 (TDD, FR1), 8 beams / 64 ports — NES gains vs 20 ms baseline |  |  |  |  |  |  |
| MediaTek [R1-2606847] | Cat 1 / Cat 2 | Low (0 < L ≤ 15%) | SSB + SIB1 + RO, un-clustered | 17.2% / 4.6% | 37.7% / 7.7% | 49.9% / 9.3% |
| MediaTek [R1-2606847] | Cat 1 / Cat 2 | Low (0 < L ≤ 15%) | No SIB1 (SSB + RO only), un-clustered | 26.6% / 9.5% | 43.0% / 10.5% | 52.9% / 11.1% |
| MediaTek [R1-2606847] | Cat 1 / Cat 2 | Low (0 < L ≤ 15%) | SSB + SIB1 + RO, clustered | 13.0% / 2.4% | 30.8% / 2.6% | 44.4% / 1.4% |
| MediaTek [R1-2606847] | Cat 1 / Cat 2 | Low (0 < L ≤ 15%) | No SIB1 (SSB + RO only), clustered | 22.1% / 6.5% | 36.1% / 5.1% | 46.7% / 3.4% |
| MediaTek [R1-2606847] | Cat 1 / Cat 2 | Light (15 < L ≤ 30%) | SSB + SIB1 + RO, un-clustered | 8.1% / 2.8% | 15.2% / 4.2% | 19.9% / 5.0% |
| MediaTek [R1-2606847] | Cat 1 / Cat 2 | Light (15 < L ≤ 30%) | No SIB1 (SSB + RO only), un-clustered | 12.6% / 5.3% | 18.1% / 6.3% | 22.1% / 5.7% |
| MediaTek [R1-2606847] | Cat 1 / Cat 2 | Light (15 < L ≤ 30%) | SSB + SIB1 + RO, clustered | 1.2% / −2.4% | 4.5% / −5.1% | 11.2% / −6.3% |
| MediaTek [R1-2606847] | Cat 1 / Cat 2 | Light (15 < L ≤ 30%) | No SIB1 (SSB + RO only), clustered | 5.3% / 0.4% | 6.9% / −3.0% | 13.0% / −4.6% |
| MediaTek [R1-2606847] | Cat 1 / Cat 2 | Medium (30 < L ≤ 50%) | SSB + SIB1 + RO, un-clustered | 4.5% / 2.0% | 7.7% / 2.6% | 9.7% / 3.0% |
| MediaTek [R1-2606847] | Cat 1 / Cat 2 | Medium (30 < L ≤ 50%) | No SIB1 (SSB + RO only), un-clustered | 7.3% / 3.8% | 10.1% / 4.6% | 11.6% / 3.4% |
| MediaTek [R1-2606847] | Cat 1 / Cat 2 | Medium (30 < L ≤ 50%) | SSB + SIB1 + RO, clustered | −0.8% / −2.4% | 1.2% / −3.6% | 4.7% / −4.8% |
| MediaTek [R1-2606847] | Cat 1 / Cat 2 | Medium (30 < L ≤ 50%) | No SIB1 (SSB + RO only), clustered | 2.0% / −0.2% | 3.0% / −1.6% | 6.1% / −3.0% |
| Around 7 GHz (Set 4) — NES gains vs 20 ms baseline |  |  |  |  |  |  |
| vivo [R1-2605459] | Cat 1 / Cat 2 / Cat 2.1 | 0% | N=1 (no repetition) | 36% / 24% / 24% | 68% / 36% / 36% | 83% / 43% / 63% |
| vivo [R1-2605459] | Cat 1 / Cat 2 / Cat 2.1 | 0% | N=2 | 2% / 0% / 0% | 48% / 24% / 24% | 72% / 36% / 55% |
| vivo [R1-2605459] | Cat 1 / Cat 2 / Cat 2.1 | 0% | N=4 | – | 4% / 0% / 0% | 50% / 23% / 39% |
| CMCC [R1-2605631] | Cat 1 / Cat 2.1 | 0% | 8 beams | 34.7% / 23.1% | 52.9% / 33.6% | 69.4% / 51% |
| NTT DOCOMO [R1-2606501] | Cat 1 / Cat 2 | 10% | Clustered signal + clustered data occasions | 53% / 46% | 70% / 56% | 77% / 60% |
| CATT [R1-2605717] | Cat 1 | 0% | L=4 beams | – | 76.6% | 87.1% |
| CATT [R1-2605717] | Cat 1 | 0% | L=8 beams | – | 75.6% | 86.8% |
| Huawei [R1-2605291] | Cat 1 | 0% / 4% / 8% | 8 beams, no AD-SS | baseline | 16% / 15% / 9% | 25% / 22% / 15% |
| Huawei [R1-2605291] | Cat 1 | 0% / 4% / 8% | 16 beams, no AD-SS | baseline | 6% / 5% / 5% | 14% / 13% / 12% |
| Huawei [R1-2605291] | Cat 1 | 0% / 4% / 8% | 8 beams, WITH AD-SS | baseline | 10% / 5% / 4% | 15% / 13% / 11% |
| Huawei [R1-2605291] | Cat 1 | 0% / 4% / 8% | 8 beams, no AD-SS | baseline | 16% / 15% / 9% | 25% / 22% / 15% |
| Band not stated — NES gains vs 20 ms baseline |  |  |  |  |  |  |
| Apple [R1-2606022] | Cat 1 / Cat 2 / Cat 2.1 | 0% | — | 32.7% / 21.9% / 21.9% | 61.3% / 32.8% / 32.8% | 79.7% / 38.2% / 56.3% |
| Apple [R1-2606022] | Cat 1 / Cat 2 / Cat 2.1 | 9.8% | — | 24.5% / 17.2% / 17.2% | 43.8% / 25.8% / 25.8% | 56.1% / 30% / 38.7% |
| Apple [R1-2606022] | Cat 1 / Cat 2 / Cat 2.1 | 22% | — | 16.6% / 12.5% / 12.5% | 28.8% / 18.7% / 18.7% | 36.3% / 21.8% / 26.2% |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.1.1-a012`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.1.1 Synchronization acquisition and beam measurement

```text
For SSB transmission, study
Option 1:
For a given frequency band, a single set of values for {X, Y, M} is predefined in default 6GR SSB periodicity
Non-adjustable number of repetitions of transmitted SSBs
Note: for discussion purpose,
X: the max number of candidate 6GR SSBs in a 6GR SSB burst
Y: the max number of candidate 6GR SSB burst(s) in a default 6GR SSB periodicity
M: the max number of candidate 6GR SSB repetitions within a default 6GR SSB periodicity
Option 2:
For a given frequency band, a single set of values for {X, Y, M} is predefined in default 6GR SSB periodicity and the actual number of repetitions of transmitted SSBs can be adjusted by the aNB
FFS: how to adjust the actual number of repetitions of transmitted SSBs including potential restrictions
Note: for discussion purpose,
X: the max number of candidate 6GR SSBs in a 6GR SSB burst
Y: the max number of candidate 6GR SSB burst(s) in a default 6GR SSB periodicity
M: the max number of candidate 6GR SSB repetitions within a default 6GR SSB periodicity
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.1.1-a013`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.1.1 Synchronization acquisition and beam measurement

```text
RAN1 to study and evaluate the following solutions
Option 1:
SSB repetition within one SSB period and UE is assumed to at least support SSB combining within one SSB period
160 ms default SSB periodicity for initial cell search
Option 2:
SSB repetition within one SSB period and UE is assumed to at least support SSB combining within one SSB period
80 ms default SSB periodicity for initial cell search
Option 3:
UE is assumed to at least support SSB combining across different SSB periods
40 ms default SSB periodicity for initial cell search
Option 4:
SSB repetition within one SSB period and UE is assumed to at least support SSB combining within one SSB period and support SSB combining across different SSB periods
40 ms default SSB periodicity for initial cell search
Option 5:
UE is assumed to at least support SSB combining across different SSB periods
20 ms default SSB periodicity for initial cell search
To mitigate the UE impact with longer SSB periodicity in Option 1/2/3/4, RAN1 to study the following solutions
Solutions to reduce cell search complexity and latency
Additional synchronization signals
Clustered allocations of SSB, SIB1 and paging
Other solutions are not precluded
FFS: Additional configurable SSB periodicities
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.1.1-a014`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.1.1 Synchronization acquisition and beam measurement

```text
Draft LS R1-2606890 is endorsed in principle.
Final LS R1-2606891 is approved.
R1-2606890	Draft LS on Time plan for SSB design in RAN1&RAN4	Rapporteur (NTT DOCOMO, INC.) [RAN WG1]
R1-2606725 	FL summary #5 of Synchronization acquisition and beam measurement	Moderator (Huawei)
R1-2606724 	FL summary #4 of Synchronization acquisition and beam measurement	Moderator (Huawei)
R1-2606723 	FL summary #3 of Synchronization acquisition and beam measurement	Moderator (Huawei)
R1-2606722 	FL summary #2 of Synchronization acquisition and beam measurement	Moderator (Huawei)
R1-2606721	FL summary #1 of Synchronization acquisition and beam measurement	Moderator (Huawei)
R1-2605213	6G Synchronization Acquisition and Beam Measurement	FUTUREWEI
R1-2605254	Discussion on synchronization acquisition and beam measurement	Spreadtrum, UNISOC
R1-2605291	Synchronization acquisition and beam measurement for 6GR	Huawei, HiSilicon
R1-2605375	Discussion on synchronization acquisition and beam measurement	TCL
R1-2605382	On  synchronization acquisition and beam measurement	Nokia
R1-2605419	Discussion on Synchronization acquisition and beam measurement	Jio Platforms
R1-2605431	Discussion on Synchronization acquisition and beam measurement	ZTE Corporation, Sanechips
R1-2605459	Discussions on 6GR synchronization acquisition and beam measurement	vivo
R1-2605492	Synchronization acquisition and beam measurement	Tejas Networks Limited
R1-2605506	Discussion on Synchronization acquisition and beam measurement for 6GR	LG Electronics
R1-2605512	IMU Views on 6GR Initial Access	IMU
R1-2605521	Synchronization acquisition and beam measurement	Ericsson Inc.
R1-2605563	Discussion on synchronization acquisition and beam measurement for 6GR	Xiaomi
R1-2605631	Discussion on synchronization acquisition and beam measurement	CMCC
R1-2605675	Views on 6GR Synchronization Acquisition	Ofinno
R1-2605686	Synchronization acquisition and beam measurement	InterDigital, Inc.
R1-2605717	Discussion on synchronization acquisition and beam measurement	CATT, CICTCI
R1-2605761	Discussion on synchronization acquisition and beam measurement	KT Corp.
R1-2605823	Discussion on synchronization acquisition and beam measurement for 6GR	Samsung
R1-2605874	Discussion on synchronization acquisition and beam measurement during initial access	NEC
R1-2605917	Discussion on Synchronization acquisition and beam measurement for 6GR	OPPO
R1-2605959	Initial access design for 6GR	Panasonic
R1-2605965	Discussion on Synchronization Acquisition and Beam Measurement	PML
R1-2605970	6GR Synchronisation and Beam Management	Sony
R1-2606000	Frame structure and coverage	Nordic Semiconductor ASA
R1-2606022	Synchronization acquisition and beam measurement	Apple
R1-2606079	Discussion on synchronization acquisition and beam measurement	China Telecom
R1-2606100	Discussion on synchronization acquisition and beam measurement	1Finity
R1-2606143	Views on synchronization acquisition and beam measurement	MediaTek Inc.
R1-2606186	Discussion on synchronization acquisition and beam measurement	HONOR
R1-2606238	Discussion on synchronization acquisition and beam measurement	ETRI
R1-2606266	Discussion on design of the synchronization	Transsion Holdings
R1-2606275	Synchronization Acquisition and Beam Measurement for 6GR	Fraunhofer IIS, Fraunhofer HHI
R1-2606319	Initial access and SSB operation across different carriers	Vodafone, Deutsche Telekom, Orange
R1-2606336	Discussion on Synchronization signal design and measurement 	Lenovo
R1-2606338	Discussion on synchronization acquisition and beam measurement	Sharp
R1-2606375	Synchronization acquisition and beam measurement	Qualcomm Incorporated
R1-2606399	Discussion on synchronization acquisition and beam measurement	Google
R1-2606427	On resource block alignment between LTE, NR, and 6GR	AT&T, Bouygues Telecom, BT, Deutsche Telecom, Ericsson, FirstNet, KT Corp., Nokia, Orange, Spark NZ, Telecom Italia, Verizon, Vodafone
R1-2606439	Discussion of synchronization of 6GR	ASUSTeK
R1-2606442	Discussion on on-demand signal/channel for initial access	NICT
R1-2606453	Discussion on Synchronization Acquisition and Beam Measurement for 6GR	Fainity Innovation
R1-2606479	Discussion on synchronization acquisition and beam measurement	CSCN
R1-2606501	Discussion on synchronization acquisition and beam measurement	NTT DOCOMO, INC.
R1-2606549	Discussion on synchronization acquisition and beam measurement	Quectel
R1-2606574	Discussion on synchronization acquisition and beam measurement	WILUS Inc.
R1-2606600	Views and Discussion on 6GR Synchronization and Frame Structure	Indian Institute of Tech (M)
R1-2606646	Synchronization acquisition and beam measurement	CEWiT
R1-2606665	Discussion on synchronization acquisition and beam measurement	KDDI CORPORATION.
R1-2606684	Synchronization acquisition and beam measurement	ITL
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.1.1-a015`

### [6G/Rel-20 RAN1#126] `working_assumption` 10.5.1.1 Synchronization acquisition and beam measurement

```text
For 6GR, one SSB is defined by a single value of X
One 6GR SSB spans X (4<=X<=7) OFDM symbols within a slot
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.1.1-w001`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.1.2 PRACH and RACH procedure

```text
Update the scenario characteristic table for PRACH design study (changes in RED):
| Carrier Frequency | Around 700 MHz | Around 2 GHz | Around 4 GHz | Around 7 GHz | Around 30 GHz |
| --- | --- | --- | --- | --- | --- |
| Duplex Scheme | FDD | FDD, TDD, SBFD | TDD, SBFD | TDD, SBFD | TDD, SBFD |
| ISD [m] | 200, 500, 1299, 1732, 5000, 100000 | 20, 200, 250, 500, 1299, 1732, | 20, 50, 200, 250, 500, 1299, 1732, | 20, 50, 200, 250, 500, 1299, 1732, | 1732 |
| Distance derived from ISD [m] (see NOTE 1) | 133, 333, 866, 1155, 3333, 10000, 100000 | 13, 133, 167, 333, 866, 1155 | 13, 33, 133, 167, 333, 866, 1155 ATG: 100000 FWA: 10000 | 13, 33, 133, 167, 333, 866, 1155 ATG: 100000 FWA: 10000 | FFS |
| Max Cell range [m] (see NOTE 2) | 100000 | 1155 | Mobile: 1155 ATG: 100000 FWA: 10000 | Mobile: 1155 ATG: 100000 FWA: 10000 | FFS |
| RTT derived from distance [us] (see NOTE 3) | 0.89, 2.22, 5.77, 7.7, 22.2, 666.7 | 0.09, 0.89, 1.11, 2.22, 5.77, 7.7 | 0.09, 0.89, 1.11, 2.22, 5.77, 7.7, FWA: 66.7 ATG: | 0.09, 0.89, 1.11, 2.22, 5.77, 7.7, FWA: 66.7 ATG: |  |
| Max RTT [us] (see NOTE 4) | 666.7 | 7.7 | Mobile: 7.7 ATG: FWA: 66.7 | Mobile: 7.7 ATG: FWA: 66.7 | FFS |
| Target Delay Delay Spread (see NOTE 5) | FFS | FFS | FFS | FFS | FFS |
| Preamble Duration (see NOTE 6) |  |  |  |  |  |
| UE Mobility Values [km/h] | 30, 40, 100, 120 (for 3.333 km cell range), 160 (for 100km cell range), 200 | 3, 30, 40, 100, 120, 200, [NTN: 3, 250, 1500] | 3, 30, 40, 120, 200, HST: 500 ATG: 1500 | 3, 30, 40, 120, 200 HST: 500 ATG: 1500 | FFS |
| Max UE Mobility [km/h] (see NOTE 7) | 160 (for 100km cell range) 120 (for 3.333km cell range) 200 (for 1.155km cell range) | 200 [NTN: 1500] | 200 HST: 500 ATG: 1500 | 200 HST: 500 ATG: 1500 | FFS HST: 500 |
| Max Doppler Shift [Hz] (see NOTE 8) | 259.3 | 741 | 1482 HST: 3704 ATG: | 2593 HST: 6482 ATG: | HST: 27778 |
| NOTE 1: Distance derived from ISD is calculated by “ISD*2/3”. ATG and single cell with large coverage directly provides cell range with ISD. NOTE 2: Max Cell range is the maximum value of ‘Distance derived from ISD’ NOTE 3: RTT derived from distance is calculated by ‘Distance derived from ISD *2/3e8’. NOTE 4: Max RTT is the maximum value of ‘RTT derived from distance’ NOTE 5: Details of Target delay is FFS. Delay spread is the additional delays that may need to considered in addition to max RTT NOTE 6: Details of preamble duration is FFS. NOTE 7: Max mobility is the maximum of ‘Mobility values’ NOTE 8: Max doppler shift for TN was based on ‘UE mobility [km/h] * 1000/3600 * (Carrier Freq [Hz]/3e8)*2’ |  |  |  |  |  |
Note: Notes from RAN1 #125 agreement still apply to the table above.
Note: For modelling of the doppler, each individual path follows TR 38.901
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.1.2-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.1.2 PRACH and RACH procedure

```text
For the study of preamble format reduction, below template is adopted for companies to provide set of preamble design targets that provide enablement of 6GR use cases and deployment scenarios. Please provide minimal set of preamble design targets that companies believe is the best representation for 6GR, including information on how the representative preamble design targets for 6GR is selected.
A row represented Preamble design targets are represented by {Carrier Frequency, Delay (Max RTT + Delay Spread), Doppler Shift} tuple.
| Identifier (company + Index) | Carrier Frequency | Delay (Max RTT + Delay Spread) | Doppler Shift | Notes (any information to additional share, e.g., sequence length, occupied BW, SCS, number of sequence repetition, preamble duration, frame structure restrictions, information on derivation, motivation, etc) |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.1.2-a002`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.1.2 PRACH and RACH procedure

```text
For study of whether the maximum number of preambles per RO is increased beyond 64, take into account at least:
the justification and use case for the capacity increase (e.g., load model, access rate per cell, target collision probability, availability of ROs in time/frequency);
the available root-sequence pool and the resulting inter-cell reusing for the assumed sequence length; and
Note: Preamble sequence, format, as well as availability of ROs in time/frequency are taken into account when calculating available sequence pool and reuse.
the resulting Miss detection, Type-1 (intra-cell), and Type-2 (inter-cell) false-detection performance under PRACH transmission load in the network.
Companies are asked to provide information on detection algorithm and detection metric thresholds (and adaptation strategies, if any) used for evaluations.
associated transmitter/receiver complexity, and random access latency
R1-2606818	Summary of contributions on Random Access and RA Procedures	Moderator (InterDigital, Inc)
R1-2606817	Summary of contributions on Random Access and RA Procedures	Moderator (InterDigital, Inc)
R1-2606816	Summary of contributions on Random Access and RA Procedures	Moderator (InterDigital, Inc)
R1-2606815	Summary of contributions on Random Access and RA Procedures	Moderator (InterDigital, Inc)
R1-2605242	Discussion on PRACH and RACH procedure for 6GR	BYD
R1-2605255	Discussion on 6GR PRACH and RACH procedure	Spreadtrum, UNISOC
R1-2605292	PRACH and RACH procedure for 6GR	Huawei, HiSilicon
R1-2605355	PRACH and RACH procedure	EURECOM
R1-2605376	Discussion on PRACH and RACH procedure	TCL
R1-2605383	On PRACH and RACH procedure	Nokia
R1-2605420	Discussion on PRACH and RACH procedure design for 6GR	Jio Platforms
R1-2605432	Discussion on PRACH and RACH procedure	ZTE Corporation, Sanechips
R1-2605460	Discussions on 6GR RACH design and RA procedures	vivo
R1-2605493	Discussion on PRACH and RACH procedure	Tejas Networks Limited
R1-2605507	Discussion on PRACH and RACH procedure for 6GR	LG Electronics
R1-2605516	Discussion on PRACH and RACH procedure for 6GR	Fraunhofer HHI,Fraunhofer IIS
R1-2605564	Discussion on PRACH and RACH procedure for 6GR	Xiaomi
R1-2605632	Discussion on 6GR PRACH design and RACH procedure	CMCC
R1-2605676	Views on 6GR RACH and RACH Procedure	Ofinno
R1-2605718	Discussion on PRACH and RACH procedure	CATT, CICTCI
R1-2605762	Discussion on PRACH and RACH procedure	KT Corp.
R1-2605824	Discussion on PRACH and RACH procedure design for 6GR	Samsung
R1-2605875	Discussion on PRACH and RACH procedure for 6GR	NEC
R1-2605918	RACH of 6GR air interface	OPPO
R1-2605971	6GR PRACH and RACH procedure	Sony
R1-2606002	PRACH and RA procedure for 6GR air interface	InterDigital, Inc.
R1-2606023	PRACH and RACH Procedure	Apple
R1-2606740	PRACH and RACH Procedure	Apple
(Revision of R1-2606023)
R1-2606045	Discussion on PRACH and RACH procedure	Panasonic
R1-2606060	Discussion on PRACH design and RACH procedure	Sharp
R1-2606080	Discussion on PRACH and RACH procedure	China Telecom, China Unicom
R1-2606101	Discussion on PRACH and RACH procedure	1Finity
R1-2606144	Views on PRACH and RACH procedure	MediaTek Inc.
R1-2606171	PRACH and RACH procedure for 6GR	Lenovo
R1-2606239	Discussion on 6GR PRACH and RACH procedure	ETRI
R1-2606267	Discussion on RACH design	Transsion Holdings
R1-2606300	RACH evaluation and RACH procedure for 6GR	Korea Testing Laboratory
R1-2606376	PRACH and RACH procedure	Qualcomm Incorporated
R1-2606400	Discussion on PRACH and RACH procedure	Google
R1-2606454	Discussion on PRACH and RACH procedure design for 6GR	Fainity Innovation
R1-2606475	Discussion on PRACH and RACH procedure	Ericsson
R1-2606502	Discussion on PRACH and RACH procedure	NTT DOCOMO, INC.
R1-2606742	Discussion on PRACH and RACH procedure	NTT DOCOMO, INC.
(Revision of R1-2606742)
R1-2606551	Discussion on PRACH and RACH procedure	Quectel
R1-2606625	Discussion on RACH procedure	ASUSTeK
R1-2606647	PRACH and RACH procedure	CEWiT
R1-2606702	Discussion on PRACH and RACH procedure	Indian Institute of Tech (M)
R1-2606739 	Discussion on PRACH and RACH procedure	Indian Institute of Tech (M)
(Revision of R1-2606702)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.1.2-a003`

### [6G/Rel-20 RAN1#126] `conclusion` 10.5.1.2 PRACH and RACH procedure

```text
To report the following details for PRACH evaluations:
Receiver algorithm details, including:
Detection threshold strategy:
threshold configured to address false alarm only (impacting miss detection)
Example 1) Threshold is determined based on noise variance
threshold configured to address false alarm (impacting miss detection) and false detection probability jointly
Example 2) Threshold is determined based on noise variance, inter-sequence interference + noise estimated from measurements outside the window of the detected peak
Detection metric is normalized by interference+noise estimate, where the estimate is derived (e.g., maximum or median of the detection metric) from the detection metric outside the window around the detected peak within the NCS duration of the preamble. The detection peak window can be +/- estimated/approximated channel delay.
Example 3) Threshold is determined based on noise variance, sequence interference estimated from measurement of total receive signal power of a RO
In case of ZC sequence detection with Restricted Set A and B, details of detection algorithm to handle the detection sidelobes.
For False alarm statistics, which option used for false alarm (and determination of detection threshold)
Option 1) if BS performs detection on a RO, the false alarm event happens for a preamble sequence detection, and a false alarm event is counted for the preamble sequence (false alarm event may happen multiple times within a RO for across the multiple preamble sequences). In this case, the denominator used to compute false alarm probability is the number of preambles to be detected (per RO).
Option 2) if BS performs detection on a RO, the false alarm event happens for any preamble sequence detection, and the a single false alarm event counted for a RO. In this case, denominator used to compute false alarm probability is 1 (per RO).
Relative Tx power assumption of UEs (and any pathloss measurement and RF impairment modeling, if used)
User distribution per RO, for example
Same number of users transmitting PRACH preamble in each RO
Varying number of users transmitting PRACH preamble in each RO (may be based on traffic characteristics)
Preamble sequence selection
For example, NR ZC provides information on number of root sequences, number of cyclic shifts, and Ncs value among the 64 preamble set used for evaluation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.1.2-c001`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.1.3 Bandwidth operation

```text
For initial access, confirm the RAN1#125 Working Assumption that the frequency location and bandwidth of the SIB1-PDSCH are determined independently of the UE's bandwidth capability
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.1.3-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.1.3 Bandwidth operation

```text
For single-carrier operation, RAN1 to define one common resource block grid (CRB grid) across UEs for the DL of the given carrier for 6GR.
For single-carrier operation, RAN1 to define one common resource block grid (CRB grid) across UEs for the UL of the given carrier for 6GR.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.1.3-a002`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.1.3 Bandwidth operation

```text
For initial access in a single-carrier cell,
The schedulable frequency resources of SIB1-PDSCH contains the frequency location and bandwidth of the CORESET for SIB1-PDCCH monitoring.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.1.3-a003`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.1.3 Bandwidth operation

```text
For initial access in a single-carrier cell,
For option 2, further study
Alt 1: The schedulable frequency resources of SIB1-PDSCH are predefined without explicit signaling in MIB.
Alt 2: The schedulable frequency resources of SIB1-PDSCH are explicitly signaled in MIB, subject to minimum/limited impact to MIB coverage/overhead.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.1.3-a004`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.1.3 Bandwidth operation

```text
Single numerology is adopted for the common RB (CRB) grid for 6GR single-carrier operation for a given band.
R1-2605214	6G Bandwidth Operation	FUTUREWEI
R1-2605256	Discussion on bandwidth operation	Spreadtrum, UNISOC
R1-2605293	Bandwidth operation for 6GR	Huawei, HiSilicon
R1-2605384	On aspects of bandwidth operation in 6GR	Nokia
R1-2605421	Bandwidth operation for 6GR	Jio Platforms
R1-2605433	Discussion on bandwidth operation	ZTE Corporation, Sanechips
R1-2605461	Discussions on 6GR bandwidth operation during and right after initial access	vivo
R1-2605494	Discussion on Initial Access Bandwidth operation	Tejas Networks Limited
R1-2605508	Discussion on Bandwidth Operation for 6GR	LG Electronics
R1-2605565	Discussion on bandwidth operation for 6GR	Xiaomi
R1-2605592	Bandwidth operation	Ericsson
R1-2605633	Discussion on bandwidth operation for 6GR	CMCC
R1-2605677	Views on Bandwidth operation	Ofinno
R1-2605719	Discussion on bandwidth operation	CATT
R1-2605763	Discussion on bandwidth operation during initial access	KT Corp.
R1-2605825	Bandwidth operation	Samsung
R1-2605876	Discussion on bandwidth operation for idle mode	NEC
R1-2605919	Bandwidth operation for 6GR	OPPO
R1-2605950	Bandwidth Operation	Lenovo
R1-2605972	6GR bandwidth operation	Sony
R1-2605991	Bandwidth operation for 6GR 	InterDigital, Inc.
R1-2606024	Bandwidth operation in initial access and idle mode	Apple
R1-2606064	Discussion on bandwidth operation	Panasonic
R1-2606081	Discussion on bandwidth operation for 6GR	China Telecom
R1-2606102	Discussion on bandwidth operation	1Finity
R1-2606145	6G Bandwidth Operation	MediaTek Inc.
R1-2606167	Discussion on Bandwidth operation for 6GR air interface	Sharp
R1-2606228	Discussion on bandwidth operation	DENSO CORPORATION
R1-2606240	Discussion on bandwidth operation	ETRI
R1-2606377	Bandwidth operation	Qualcomm Incorporated
R1-2606401	Discussion on bandwidth operation	Google
R1-2606503	Discussion on bandwidth operation	NTT DOCOMO, INC.
R1-2606524	Discussion on bandwidth operation	Transsion Holdings
R1-2606570	Discussion on bandwidth operation	TCL
R1-2606575	Discussion on bandwidth operation	WILUS Inc.
R1-2606622	Discussion on bandwidth operation	ASUSTeK
R1-2606648	Discussion on Bandwidth Operation	CEWiT
R1-2606685	Bandwidth operation for 6GR	ITL
R1-2606703	Discussion on bandwidth operation for 6GR	Kookmin University
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.1.3-a005`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.1 Downlink transmission scheme(s) for downlink control channels

```text
At least aggregation levels of 1, 2, 4, 8, 16 are supported for 6GR PDCCH.
Note: A CCE aggregation level is not used when the number of CCE in a CORESET is smaller than the aggregation level.
R1-2606612	Feature Lead summary #2 on PDCCH Transmission Schemes	Moderator (Nokia)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.1-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.1 Downlink transmission scheme(s) for downlink control channels

```text
A CCE consists of 6 REGs for 6GR PDCCH
REGs in a REG bundle are contiguous in frequency and time.
At least REG-bundle size of 6 REGs is supported
FFS a need for other sizes.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.1-a002`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.1 Downlink transmission scheme(s) for downlink control channels

```text
For the study of precoding granularity consider the following options from the UE perspective:
Option 1: Precoding granularity is only a single REG bundle
Option 2: The same precoder is used for all contiguous REGs in a CORESET
Option 3: The same precoder is used for multiple contiguous REG bundles in time/frequency within the PDCCH candidate
Option 4: The same precoder is used for multiple contiguous REG bundles in time/frequency.
R1-2606613	Feature Lead summary #3 on PDCCH Transmission Schemes	Moderator (Nokia)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.1-a003`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.1 Downlink transmission scheme(s) for downlink control channels

```text
Both contiguous and non-contiguous frequency-domain resource allocation are supported for 6GR CORESET.
At least 6-PRB 6GR PDCCH CORESET frequency-domain resource allocation granularity is supported
FFS a need, feasibility and conditions for other CORESET granularities
R1-2606614	Feature Lead summary #4 on PDCCH Transmission Schemes	Moderator (Nokia)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.1-a004`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.1 Downlink transmission scheme(s) for downlink control channels

```text
PDCCH payload bit-level scrambling before modulation is used for 6GR PDCCH.
FFS: Details
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.1-a005`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.1 Downlink transmission scheme(s) for downlink control channels

```text
Companies are encouraged to provide the analysis for comparison of MU-MIMO schemes (based on orthogonal and/or non-orthogonal DMRS) and single-layer, single-port, single-user PDCCH considering
The necessity to introduce orthogonal DMRS for 6GR PDCCH
At least the following two cases:
Case1: double resources for two paired MU-MIMO UEs than for a single user and the same total power are assumed from NW point of view
Case 2: the same resources for single user and two paired MU-MIMO users and the same total power are assumed from NW point of view
Performance based on link level and/or system level evaluations (e.g., BLER, spectrum efficiency)
Used models and criteria on the user pairing for MU-MIMO based on orthogonal multi-port DMRS and/or non-orthogonal single-port DMRS
Assumptions on the UE receiver
Assumptions on UE specific precoding
Impacts on UE complexity
Assumed channel model (at least CDL channel model for link level evaluations)
Assumed DCI size
Note: The discussion of the utilization of orthogonal DMRS ports for other purposes (e.g. intercell-interference mitigation) than MU-MIMO is not precluded.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.1-a006`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.1 Downlink transmission scheme(s) for downlink control channels

```text
Study the need, feasibility including at least UE complexity and benefits of CSI acquisition for PDCCH.
Note: Solutions, if found to be feasible and needed, shall be coordinated with the other AIs.
R1-2606615 Feature Lead summary #5 on PDCCH Transmission Schemes	Moderator (Nokia)
Final post-meeting summary for this agenda item.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.1-a007`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
Support the following for 6GR DL DMRS
For X = 2, Nmax = 48
For X = 1, FFS Nmax where Nmax<= 24
The CDM group structure is comb-based including at least comb-2
FFS Applicable cases for comb-2
The indication of the co-scheduled UE information includes at least one of the following: the DMRS port(s) information or CDM group information or the FD-OCC despreading length information for the co-scheduled UE
Note:
X is the TD-OCC length
Nmax is the maximum number of orthogonal DMRS ports
The maximum number of orthogonal DMRS ports that a UE can support is a separate discussion in WI phase
AI/ML based DMRS overhead reduction is a separate discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.2-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
For codeword-to-layer mapping for PDSCH:
For PDSCH rank 1—4, down-select from the following alternatives:
Alt 1: 1 CW for rank 1—4
Alt 2: 1 CW for rank 1, 2 CWs for rank 2—4
Alt 3: 1 CW for rank 1, 2 CWs for rank 2, 3 CWs for rank 3, 4 CWs for rank 4
Further study whether the codeword-to-layer mapping is fixed or flexible
Note: Above does not preclude different modulation order per layer(s) within a codeword
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.2-a002`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
For codeword-to-layer mapping for PDSCH:
For PDSCH rank up to 5—8, down-select from the following alternatives:
Alt 1: 1 CW for rank 5—8
Alt 2: 2 CWs for rank 5—8
Alt 3: 4 CWs for rank 5—8
Alt 4: 5 CWs for rank 5, 6 CWs for rank 6, 7 CWs for rank 7, 8 CWs for rank 8
Further study whether the codeword-to-layer mapping is fixed or flexible
Note: Above does not preclude different modulation order per layer(s) within a codeword
Note: Codeword-to-layer mapping for rank > 8 can be further discussed subject to outcome of discussion on maximum number of layers per UE
R1-2606677	FL Summary #3 on DL Transmission Scheme for DL Shared Channel	Moderator (Ericsson), Moderator (Google)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.2-a003`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
For AI based receiver for PDSCH DMRS overhead reduction
Study Sub-case A (orthogonal sparse DMRS) including at least the following
AI/ML receiver assumption for evaluation purpose
Including model input, output, and label
Label quality impact including label acquisition method and how it is made in practice
Generalization and scalability performance
Model inference complexity and number of parameters
Data collection and performance monitoring
MU-MIMO pairing aspects
PDSCH processing delay
Relevant specification impact(s)
Other study aspects are not precluded
Study Sub-case B and consider how to address the following challenge aspects for Sub-case B (SIP)
Inter-layer interference, inter-UE interference, and inter-cell interference handling
PAPR
Whether/how to perform Rnn estimation
UE Coexistence
Power allocation between DMRS and data
High UE implementation complexity
Other challenge aspects are not precluded
Study the list under Sub-case A
Strive to down-select up to one sub-case
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.2-a004`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
For BS antenna configurations at around 2 GHz, update RAN1#124-bis agreements as follows:
Around 2 GHz
4 TXRUs, 32 AEs, (M, N, P, Mg, Ng; Mp, Np) = (8, 2, 2, 1, 1; 1, 2), (dH, dV) = (0.5, 0.50.8), (“Outdoor Combination 1”)
32 TXRUs, 128 AEs, (M, N, P, Mg, Ng; Mp, Np) = (8, 8, 2, 1, 1; 2, 8), (dH, dV) = (0.5, 0.5)
64 TXRUs, 192 AEs, (M, N, P, Mg, Ng; Mp, Np) = (12, 8, 2, 1, 1; 4, 8), (dH, dV) = (0.5, 0.5), (“Outdoor Combination 2”)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.2-a005`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
For BS antenna configurations at around 4 GHz, update RAN1#124-bis agreements as follows:
Around 4 GHz
4 TXRUs, 32 AEs, (M, N, P, Mg, Ng, Mp, Np) = (8, 2, 2, 1, 1; 1, 2), (dH, dV) = (0.5, 0.8), (“Outdoor Combination 0”)
32 TXRUs, 128 AEs, (M, N, P, Mg, Ng, Mp, Np) = (8, 8, 2, 1 ,1; 2, 8), (dH, dV) = (0.5, 0.80.5) , (“Indoor Combination 12”)
64 TXRUs, 192AEs, (M, N, P, Mg, Ng; Mp, Np) = (12, 8, 2, 1, 1, 4, 8). (dH, dV) = (0.5, 0.8), (“Outdoor Combination 1”)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.2-a006`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
For maximum number layers per UE for PDSCH, down-select one of the following options:
Option 1: Up to 8 layers
Option 2: Up to 12 layers
Option 3: Up to 16 layers
Note: The UE capability is a separate discussion for normative work.
R1-2606678	FL Summary #4 on DL Transmission Scheme for DL Shared Channel	Moderator (Ericsson), Moderator (Google)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.2-a007`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
Study (semi-)open-loop transmission and whether/how to support specification-non-transparent schemes for PDSCH
Consider, at least, high-mobility scenario, scenarios with outdated CSI, and UE specific/common PDSCH
Consider specification-transparent and closed-loop schemes as performance baselines
FFS: Impact on DMRS
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.2-a008`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
Regarding the set of coordinated TRPs for multi-TRP transmission for PDSCH:
For discussion purposes, consider the following definitions for set of serving TRPs, the set of interference-coordination TRPs, and set of coordinated TRPs:
The set of serving TRPs per UE (of cardinality up to ) and the set of interference-coordination TRPs per UE (of cardinality up to ) are subsets of the set of coordinated TRPs at the NW (of cardinality up to )
Further study:
The maximum number of serving TRPs per UE,
The maximum number of interference-coordination TRPs per UE,
The maximum number of coordinated TRPs at the NW,
Standard impact, if any
Note: TRP may not be specified in 6G specification
Note: The above does not preclude the multiple subsets of serving TRPs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.2-a009`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
Consider the following for the co-schedule UE information indication/assumption for a target UE
Study at least the following options for the DMRS ports for the co-scheduled UEs
Option 0: The aNB indicates the CDM group(s) without data
Option 1: The aNB indicates the CDM group(s) for the co-scheduled UEs
Option 2: The aNB indicates the DMRS ports for the co-scheduled UEs within the same CDM group as the target UE
Option 3: The aNB indicates the FD-OCC despreading length
Option 4: The aNB indicates the DMRS port(s) for the co-scheduled UEs
Study at least the following options for modulation order and/or coding scheme for the co-scheduled UEs
Option 1: The aNB indicates modulation order for co-scheduled UE(s)
Option 2: The aNB indicates modulation order and coding scheme for co-scheduled UE(s)
Option 3: The target UE may assume modulation order and/or coding scheme for co-scheduled UE(s)
Study at least the following options on the frequency domain DMRS density for the co-scheduled UE(s)
Option 1: The target UE can assume the frequency domain DMRS density for the co-scheduled UE(s) is the same as the target UE
Option 2: The aNB indicates the frequency domain DMRS density for the co-scheduled UE(s)
Study at least the following options for the QCL/TCI for co-scheduled UE(s)
Option 1: The target UE can assume the QCL/TCI for the co-scheduled UE(s) is the same as the target UE
Option 2: The aNB indicates the QCL/TCI for the co-scheduled UE(s)
Option 3: The target UE may determine any QCL/TCI information for co-scheduled UE(s).
Support that a target UE can assume the time-domain location for the co-scheduled UE’s DMRS should be the same as the target UE’s DMRS
FFS: The target UE can assume the PRG allocation for the co-scheduled UE(s) is the same as the target UE
FFS: The target UE can assume the DMRS sequence for the co-scheduled UE(s) is the same or different as the target UE
FFS: Whether the information above can be optional or not with regard to different types of UE receivers
FFS: When the target UE can assume there is no co-scheduled UEs
FFS: For each item above, the DCI bit count per co-scheduled UE and its scaling with the number of co-scheduled UEs
R1-2606679	FL Summary #5 on DL Transmission Scheme for DL Shared Channel	Moderator (Ericsson), Moderator (Google)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.2-a010`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
With respect to the agreement below from RAN1#124bis, the following changes in red are made:
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.2-a011`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
For evaluation of DMRS for PDSCH, the following aspects are considered for further study:
Candidates for FD-OCC length: 2, 3, 4, 6, 8, 12, 16, 24, x
Candidates for TD-OCC length: 1 (i.e., single-symbol DMRS), 2, 4, x
Candidate for number of CDM groups: 2, 3, 4, 6, 8, 12, x
CDM group structure, e.g., comb-based, block-based, etc.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.2-a012`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
Support the DMRS for PDSCH based on the Gold sequence initialized based on at least a scrambling ID or physical cell ID
FFS: How the scrambling ID is indicated
FFS: Other factors for the sequence initialization
FFS: The number of scrambling IDs used to generate Gold sequence
FFS: Details on the Gold sequence generator
FFS: Additional supplementary sequence to reduce cross-correlation
FFS: How to facilitate PAPR reduction property
FFS: How to mitigate inter-port interference
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.2-a013`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
Consider the following for 6GR DMRS for single-slot based PDSCH for further evaluation and down-selection
X=1, L = {1, 2, 3, 4, 5, 6}
X=2, L = {1, 2, 3}
Note:
X is the TD-OCC length
L is the number of units of consecutive DMRS symbols
FFS: How to determine the value of L if multiple values are supported
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.2-a014`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
Support PT-RS transmitted at least within the FDRA for the PDSCH
FFS: Whether PT-RS is transmitted from partial bandwidth or the whole bandwidth
FFS: Frequency-domain pattern of the PT-RS
Support PT-RS transmitted at least within the TDRA for the PDSCH
PT-RS is not present in the DMRS symbol
FFS: Symbols for PT-RS
Study the conditions for the PT-RS presence
Study the maximum number of PT-RS ports
Study PT-RS and DMRS port association
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.2-a015`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
For TDRA for PDSCH contained within a single slot:
For starting symbol  and number of symbols, , down-select from the following options:
Option 1:
Option 2:
Note: DMRS design is discussed separately
Study to consider, at least, impact on network energy saving and spectrum efficiency
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.2-a016`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
Study of multi-TRP transmission of single PDSCH scheduled by a single DCI to consider, at least, the following schemes assuming ideal backhaul:
Dynamic point selection (DPS)
Coherent joint transmission (CJT)
Single Frequency Network (SFN), at least, for HST scenario
Consider NR HST-SFN as a starting point
Time division multiplexing (TDM) repetition
Further study whether to consider also the following schemes:
Frequency division multiplexing (FDM) repetition
Non-coherent joint transmission (NC-JT)
Companies to report target use cases for each of the schemes
FFS: Whether above multi-TRP transmission schemes are transparent from UE perspective.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.2-a017`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
Further study whether to consider the following schemes for study of multi-TRP transmission of multiple PDSCHs scheduled by multiple DCIs assuming non-ideal backhaul:
Non-coherent joint transmission (NC-JT)
FFS: Fully overlapping, partially overlapping, and non-overlapping NC-JT
Companies to report target use cases for each of the schemes
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.2-a018`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.3 Uplink transmission scheme(s) for uplink channels

```text
For codebook based PUSCH transmission for 6GR, study the following coherency types of UL precoder
Non-coherent type
Partial-coherent type
Full-coherent type
Full-power transmission precoder is separately discussed.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.3-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.3 Uplink transmission scheme(s) for uplink channels

```text
For codebook based PUSCH transmission for 6GR, study fixed codebook for full-coherent precoder type considering the following options and aspects:
Option 1. Reuse NR UL codebook
Option 2. Grassmannian codebook
Option 3. Per-element phase/amplitude quantization targeting SVD precoder approximation
Option 4. DFT based precoder
Other option(s) are not precluded.
Consider different antenna architectures and different waveforms
Whether/how to separately or commonly design 2TX/3TX/4TX/8TX codebook
Whether to keep constant modulus property
Whether/how to consider UE PA (power amplifier) constraint
Whether/how to define single-layer precoder only, and indicating a combination of precoder(s)
Consider different codebook size and precoder indication overhead
Whether/how to separately or commonly design codebook for CP-OFDM and DFT-S-OFDM.
Note: Partial/non-coherent precoder type are separately discussed.
Note: Per-layer power control is separately discussed.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.3-a002`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.3 Uplink transmission scheme(s) for uplink channels

```text
For evaluation on coherent UL MIMO based PUSCH transmission for 6GR, at least the RF coherence requirements for coherent UL MIMO defined in TS38.101-1/2 are used as baseline
Companies to report
Other additional RF coherence requirements can be reported by companies (optional)
TX coherency error model
R1-2605830	FL Summary #2 on Uplink transmission scheme(s) for uplink channels	Moderator (Samsung)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.3-a003`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.3 Uplink transmission scheme(s) for uplink channels

```text
Support both of the following methods to convey the UCI over physical channel:
Method 1: Define a UCI dedicated physical channel, i.e., Physical Uplink Control Channel (PUCCH)
Method 2: UCI carried on PUSCH
Note: Whether/how to support each UCI type (e.g., HARQ-ACK, CSI) on PUSCH with/without data is up to other agendas
Further study on Option 3 per agreement in RAN1#124
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.3-a004`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.3 Uplink transmission scheme(s) for uplink channels

```text
For transmission scheme(s) for 6GR PUCCH formats, study at least the followings aspects:
Scheme(s) with sequence(s) without DMRS
Scheme(s) with DMRS and/or channel coding
Note: It does not mean that scheme(s) with DMRS only is considered
RAN1 strives for smaller number of formats for 6GR PUCCH, e.g., up to 2 or 3 formats.
Study at least the following point(s) for differentiation among 6GR PUCCH formats
UCI payload size
Transmission scheme
Waveform
Modulation schemes
The number of OFDM symbols/PRBs for one PUCCH resource
Multi-user multiplexing scheme(s)/capability/capacity
The study shall consider NR PUCCH formats as the benchmark
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.3-a005`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.3 Uplink transmission scheme(s) for uplink channels

```text
Support the following for UL DMRS for 6GR PUSCH at least based on CP-OFDM waveform
For X = 2, Nmax = 48
For X = 1, FFS: Nmax where Nmax<= 24
The CDM group structure is comb-based including at least comb-2
FFS: Applicable cases for comb-2
Note:
X is the TD-OCC length
Nmax is the maximum number of orthogonal DMRS ports
AI/ML based DMRS overhead reduction is a separate discussion
FFS: Maximum number of orthogonal DMRS ports for DFT-s-OFDM
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.3-a006`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.3 Uplink transmission scheme(s) for uplink channels

```text
For DMRS based on TD-OCC-X for a single-slot based PUSCH, the TD-OCC-X is applied to X consecutive symbols for DMRS
Consider the same spacing between every X DMRS symbols
Study how to identify the spacing between every X DMRS symbols
FFS: whether there is any exception
The number of DMRS symbols in a slot is L*X, and study the candidate value of L as follows
For X = 1, L = {1, 2, 3, 4, 5, 6}
For X = 2, L = {1, 2, 3}
If multiple candidate values of L are supported, study how to determine the value of L
Study at least the following options for the time-domain location of the first DMRS symbol
Option 1: The first DMRS symbol is fixed as the first symbol allocated for the PUSCH
Option 2: The candidate DMRS symbol(s) are fixed in a slot and the actual first DMRS symbol is the first candidate DMRS symbol within the TDRA for the PUSCH
Option 3: The first DMRS symbol is indicated by the network relative to the first symbol of the PUSCH
R1-2605831	FL Summary #3 on Uplink transmission scheme(s) for uplink channels	Moderator (Samsung)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.3-a007`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.3 Uplink transmission scheme(s) for uplink channels

```text
For 6GR PUSCH transmission, study AI based receiver for PUSCH DMRS overhead reduction at least considering the followings:
Candidate(s) of low overhead DMRS pattern
Subcase A
At least Comb-based low overhead DMRS pattern in frequency domain
FFS: time domain
Subcase B in power domain
Note: For a given low overhead DMRS pattern, it is transparent to the UE the type of receiver  (AI or non-AI) used at the network.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.3-a008`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.3 Uplink transmission scheme(s) for uplink channels

```text
For study on AI based receiver for PUSCH DMRS overhead reduction, subcase C is deprioritized.
R1-2605832	FL Summary #4 on Uplink transmission scheme(s) for uplink channels	Moderator (Samsung)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.3-a009`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.3 Uplink transmission scheme(s) for uplink channels

```text
For codeword-to-layer mapping for PUSCH in 6GR:
For PUSCH rank 1—4, down-select from the following alternatives:
Alt 1: 1CW for rank 1—4
Alt 2: 1CW for rank 1, 2CWs for rank 2—4
Alt 3: 1CW for rank 1, 2CWs for rank 2, 3CWs for rank 3, 4CWs for rank 4
Further study whether the codeword-to-layer mapping is fixed or flexible
Note: Above does not preclude different modulation order per layer(s) within a codeword
Note: Above does not preclude different power allocation per layer
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.3-a010`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.3 Uplink transmission scheme(s) for uplink channels

```text
For codeword-to-layer mapping for PUSCH in 6GR:
For PUSCH rank up to 5—8, down-select from the following alternatives:
Alt 1: 1CW for rank 5—8
Alt 2: 2CWs for rank 5—8
Alt 3: 4CWs for rank 5—8
Alt 4: 5CWs for rank 5, 6CWs for rank 6, 7CWs for rank 7, 8CWs for rank 8
Further study whether the codeword-to-layer mapping is fixed or flexible
Note: Above does not preclude different modulation order per layer(s) within a codeword
Note: Above does not preclude different power allocation per layer
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.3-a011`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.3 Uplink transmission scheme(s) for uplink channels

```text
The following is endorsed  as Draft an LS to RAN4 regarding the 6GR the RF coherence requirements.
1 Overall description:
RAN1 are studying UL MIMO codebooks for 6G and have reached the following agreements:
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.3-a012`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.3 Uplink transmission scheme(s) for uplink channels

```text
For codebook based PUSCH transmission for 6GR, study fixed codebook for full-coherent precoder type considering the following options and aspects:
Option 1. Reuse NR UL codebook
Option 2. Grassmannian codebook
Option 3. Per-element phase/amplitude quantization targeting SVD precoder approximation
Option 4. DFT based precoder
Other option(s) are not precluded.
Consider different antenna architectures and different waveforms
Whether/how to separately or commonly design 2TX/3TX/4TX/8TX codebook
Whether to keep constant modulus property
Whether/how to consider UE PA (power amplifier) constraint
Whether/how to define single-layer precoder only, and indicating a combination of precoder(s)
Consider different codebook size and precoder indication overhead
Whether/how to separately or commonly design codebook for CP-OFDM and DFT-S-OFDM.
Note: Partial/non-coherent precoder type are separately discussed.
Note: Per-layer power control is separately discussed.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.3-a013`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.3 Uplink transmission scheme(s) for uplink channels

```text
For evaluation on coherent UL MIMO based PUSCH transmission for 6GR, at least the RF coherence requirements for coherent UL MIMO defined in TS38.101-1/2 are used as baseline
Companies to report
Other additional RF coherence requirements can be reported by companies (optional)
TX coherency error model
RAN1 are currently using the coherent UL MIMO requirements in TS38.101-1/2 as baselines for evaluations including coherence imperfections. RAN1 would like to know if the amplitude/phase errors in these requirements will be revisited for 6G, especially for devices that support more than two port UL MIMO transmission.
RAN1 have not so far agreed to models of coherence imperfections for codebook evaluations, and so such models are determined by each company. Therefore, while RAN1 can continue investigations, RAN1 would welcome suggestions on amplitude/phase error modeling for 6G UEs so that these may be used to refine RAN1’s evaluations.
2	Actions
To RAN4
ACTION: 	RAN1 respectfully asks RAN4 if the amplitude/phase errors in current coherent UL MIMO requirements in TS38.101-1/2 will be revisited for 6G, especially for devices that support more than two port UL MIMO transmission. While RAN1 can continue investigations, RAN1 would also welcome suggestions on amplitude/phase error modeling for UL MIMO.
The corresponding final LS in R1-2606899 is Approved.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.3-a014`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.3 Uplink transmission scheme(s) for uplink channels

```text
For codebook based PUSCH transmission for 6GR, a fixed codebook is further clarified as follow:
For a given precoder indication size, a set of precoder(s) in fixed codebook is pre-defined/specified in the specification
Note: All 5G NR DL/UL codebooks are fixed codebook.
Note: Per agreement in RAN1#124bis, a fixed codebook is a codebook which is pre-defined in specification.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.3-a015`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.2.3 Uplink transmission scheme(s) for uplink channels

```text
For codebook based PUSCH transmission for 6GR, study configurable codebook considering the following options and aspects:
Option 1. Downloadable codebook
NW determines a set of precoder(s)/matrices.
From NW, UE is configured with a set of precoder(s)/matrices.
After NW acquires UL CSI, an UL precoder within the set of precoder(s) is indicated by NW to UE.
Option 2. Uploadable codebook
UE determines a set of precoder(s) and reports to NW.
From NW, UE is configured with a set of precoder(s).
After NW acquires UL CSI, an UL precoder within the set of precoder(s) is indicated by NW to UE.
Whether to consider constant modulus property
Whether/how to indicate/obtain UE’s relevant information
How to construct hybrid approach between fixed codebook and configurable codebook
Memory burden / implementation complexity for UE/NW side
Applicable scenario/use case (e.g., applicable number of antenna ports)
How to consider PAPR increase and UE power constraint
R1-2605833	FL Summary #5 on Uplink transmission scheme(s) for uplink channels	Moderator (Samsung)
Final post-meeting summary for this agenda item.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.2.3-a016`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For the 6GR codebook design for CSI report, study a W1W2 only structure for the low-resolution scheme with the following considerations at least for RI=1-4:
W1-structure
SD basis
NR oversampled 2D-DFT basis is a baseline
FFS on other basis, e.g., basis constructed from combined 2D DFT beams
FFS on alphabet set for combination coefficients for the basis constructed from combined 2D DFT beams
SD basis selection
eType-I Scheme-B like unrestricted orthogonal DFT beam selection in 2D direction is a baseline
FFS on orthogonal basis selection in at least 1D direction, or non-orthogonal basis selection
Layer-specific/layer-group-specific SD basis selection
FFS on basis-to-layer (layer-group) mapping, e.g., ordering or no ordering
FFS on the maximum number of SD basis vector selection
W2-structure
Layer-specific/layer-group-specific inter-polarization co-phase selection
FFS: inter-polarization amplitude
Alphabet set for inter-polarization co-phase: BPSK, QPSK
FFS: details for each rank
FFS: for WB, whether to consider or not 8-PSK in addition to BPSK and QPSK
FFS on RI>4
Strive for having a unified codebook scheme for all supported ranks by 6G
FFS: details on whether/how to accommodate passive array with smaller number of ports
Note: UE implementation complexity is to be considered in the design of SD-basis and co-phasing selection, including the number of candidate combinations and the associated search complexity.
Note: CBSR discussion will be discussed separately
Note: For discussion of low resolution scheme, eType-1 Scheme-A and eType-II with L=1 are precluded
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.1-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
On defining the CSI-RS pattern in M1 slots and M2 RBs, support both M1 and M2 can be larger than or equal to 1
For M1,
For the number of CSI-RS ports smaller than or equal to X, only M1=1 is supported.
For the number of CSI-RS ports larger than X, support M1 can be larger than 1
FFS value of X
FFS for M2
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.1-a002`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For CSI-RS for CSI acquisition in 6GR, design on CSI-RS and CSI assumes the maximum number of CSI-RS ports is 256.
Final decision on the maximum number of CSI-RS ports (128, 256 or 512) is to be made in RAN1#127
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.1-a003`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
On the design of CDM group size and type for 6G CSI-RS, study and evaluate the following detailed candidates in addition to the ones supported in NR
For Option 2-2: Larger CDM size
Candidate 2-2-1: cdm16-FD4-TD4
Candidate 2-2-2: cdm16-FD2-TD8
Candidate 2-2-3: cdm16-FD8-TD2
Candidate 2-2-4: cdm16-FD16
Candidate 2-2-5: cdm32-FD4-TD8
Candidate 2-2-6: cdm32-FD8-TD4
Candidate 2-2-7: cdm64-FD8-TD8
Candidate 2-2-8: cdm12y-FD12-TDy, where y = {1, 2, 4}
For Option 2-3: New CDM type for NR CDM size
Candidate 2-3-1: cdm4-FD4
Candidate 2-3-2: cdm8-FD4-TD2
Candidate 2-3-3: cdm8-FD8
Companies to report the applicable number of CSI-RS ports for each candidate in the simulation
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.1-a004`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For CSI-RS sequence in 6G, take the NR PN sequence and mapping as the baseline for evaluation, further study the following aspects
How to achieve low-PAPR for pre-coded CSI-RS by sequence and/or mapping, compared to NR PN sequence and its mapping
Handle the case with high inter-cell interference /how to handle the case with high inter-cell interference
CSI-RS sharing for different frequency density
On sequence initialization, take NR UE specific configuration for initialization as the baseline, study whether other options are needed
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.1-a005`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For 6G CSI-RS, study the following options to address the potential PAPR issue caused by precoded CSI-RS
Option 1: BS implementation-based approach, e.g., use UE-transparent CDM-specific small cyclic shifts, or use small CDM group size
Option 2: Map the PN sequence to the global subcarrier indices in the whole bandwidth sequentially
Option 3: Multiply the PN sequence with an additional CDM group-specific scrambling sequence
Option 4: Multiply the PN sequence with an additional port-specific scrambling sequence
Option 5: Apply segmented phase rotation on the PN sequence
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.1-a006`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For 6GR codebook design for CSI report, study whether/how to address near-field (NF) propagation as follows:
Evaluation scenario:
7GHz band scenarios
Same SLS methodology is assumed as agreed EVM for CSI evaluation, with NF channel modeling
Centralized TXRU array (single TRP) architecture
Assess the following:
Regular UPT stats
Percentage of UEs impacted by NF and its impact on UPT
Companies to report how to define NF UEs, e.g., UEs within Rayleigh distance or scaling of Rayleigh distance for calibration purpose
Whether/how the NF transmission issue (if identified) needs be addressed:
SRS-based CSI acquisition
via fixed codebook design
with NR fixed DFT basis or port-selection basis (e.g., large-array into multiple sub-arrays analogous to CJT extension/multiple-panel)
with new fixed basis (e.g., SD basis utilizing distance domain or other)
with basis combined from DFT beams/port selection
via DLable codebook/basis
via AI-based CSI compression
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.1-a007`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For the study of non-AI/AI based CSI prediction in frequency/spatial/time domain at UE or NW side, adopt the templates in the following documents for collecting companies’ results.
LLS: [10.5.3.1] CSI prediction simulation result collection template _LLS_v1_Mod.xlsx in R1-2605468
SLS: [10.5.3.1] CSI prediction simulation result collection template _SLS_v1_Mod.xlsx in R1-2605468
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.1-a008`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For CSI-RS sharing Use case 2: Sharing a common set or subset of REs among CSI-RS with different frequency densities, study the following alternatives for discussing frequency density common sequence mapping
Alt 1: Generate sequence for higher frequency density first, from which extract lower frequency density sequence
Alt 2: Generate sequences for lower frequency density first, which are concatenated to form higher frequency density sequence
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.1-a009`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For CSI-RS sharing Use case 1: Sharing a common set or subset of REs among CSI-RS with different number of ports, taking Level 1 (Sharing granularity is CDM group level) as baseline,
Study Level 2 (Sharing granularity can be smaller than a CDM group), with the following sub-levels
Level 2-1: CDM group of the target CSI-RS is decoded without assuming the knowledge of any reference CSI-RS pattern
Level 2-2: CDM group of the target CSI-RS is decoded assuming the knowledge of  a reference CSI-RS pattern
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.1-a010`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For the evaluation on downloadable/configurable codebook/basis for CSI report, the following is considered additionally on top of the agreement in RAN 1 #125:
Type-I-like scheme:
Option-1A:
, where  is a 2N1N2-dimensional precoding vector for layer , and  is the number of layers
is determined by UE from a downloadable/configurable codebook, and company reports the size of the downloadable/configurable codebook
Option-1B:,
,  is a N1N2-dimension SD basis for layer
(wideband) is determined by UE from a downloadable/configurable SD basis set, and company reports the size of the downloadable/configurable SD basis set
W2 is either SB or WB
Type-II-like scheme:
Option-2A: ,
(wideband) is determined by UE from a downloadable/configurable SD basis set for layer , and/or  is determined by UE from a downloadable/configurable FD basis set, and L is the number of selected SD basis
Note: if FD basis set is not based on downloadable/configurable FD basis set, DFT FD basis set is assumed in the simulation.
Option-2B: ,
(wideband) is determined by UE from a downloadable/configurable SD-FD basis pair set for layer l, and L is the number of selected SD/FD basis vector pairs
Companies report the basis/precoding vector quantization assumption, if applicable
Companies report how the NW determines downloadable/configurable basis/codebook
Companies report the orthogonality of the downloadable/configurable basis/ precoding vector and the assumption for basis/ precoding vector selection (whether the selection is layer-common or layer-specific)
Strive to have common codebook structure with fixed codebook, if applicable
Companies are encouraged to compare with fixed codebook as well as AI-based CSI compression
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.1-a011`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For the 6GR codebook design for CSI report, study a W1W2Wf structure as a starting point for the high-resolution scheme with the following considerations for RI=1-4:
W1-structure
SD basis
NR oversampled 2D-DFT basis is a baseline
FFS on other basis
FFS on alphabet set for combination coefficients for the basis constructed from combined 2D DFT beams
SD basis selection
Down-select from the following options:
Opt1. L=1 only, Layer-specific/group-specific SD basis selection
Opt2. L≥1 Layer-specific/group-specific SD basis selection
Opt3. L>1 Layer-common SD basis selection
eType-II orthogonal DFT beam selection in 2D direction is a baseline
FFS orthogonal basis selection in at least 1D direction
FFS non-orthogonal L basis selection, e.g., basis vector- specific (q1, q2) selection
FFS orthogonal L basis selection, non-orthogonal basis selection across different layers, e.g., orthogonal DFT beam selection in 2D direction for each layer with layer-specific (q1, q2) selection
FFS whether/how to further optimize SD basis selection, e.g., using layer-common in combination with layer-specific/layer group-specific
FFS whether to consider RI>4
Wf-structure
eType-II layer-specific FD basis selection as a baseline
FFS on whether/how to further optimize FD compression, e.g., delay-domain pre-alignment per-basis prior to FD compression
W2-structure
Linear combining (LC) coefficient scheme (ref/diff amps, phase, SCI) analogous to Rel-16 NR eType-II as a starting point
FFS: details on alphabet sets on LC coefficients
Whether to support bitmap for indicating the location of NZCs as well as a parameter for the maximum number of NZCs
FFS parameter combination (PC) design
Note: UE implementation complexity is to be considered in the design of SD-basis selection, including the additional complexity of inter-layer interference mitigation for layer-specific schemes.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.1-a012`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For 6GR CSI-RS, study CSI-RS design to achieve low CSI-RS overhead considering the following possible directions
Direction 1: Sparse CSI-RS in frequency/spatial domain
Consider AI and/or non-AI prediction to reconstruct the channel at UE and/or NW side
Study sparse pattern
Direction 2: Use non-orthogonal CSI-RS ports
Study the use of cyclic shifts or scrambling sequences across CSI-RS RBs, or non-orthogonal cover code
Inter CSI-RS port interference leakage is to be considered in the evaluations
Note: Combinations of the directions can be considered.
Note: At least total CSI-RS overhead, performance and UE/NW complexity are to be studied
Note: Companies to report the assumed CSI-RS time-domain behavior including CSI-RS periodicity in the evaluations
Note: companies to report how CSI-RS overhead can be reduced from system perspective
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.1-a013`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For evaluation on CPI reporting in SD/FD/TD, study the following options of form of CPI:
Option 1: Channel covariance matrix/spectrum, e.g., ,  in form of basis matrix and associated coefficients and/or power, wherein  is in port/frequency domain
FFS: Whether orthogonal or non-orthogonal bases are used for compression
FFS: Whether off-diagonal coefficients in additional to diagonal coefficients of full or subset of
FFS: Whether CPI in SD/FD/TD domains are reported separately or jointly
Option 2: Channel covariance matrix in form of quantization of decomposed channel covariance matrices, e.g., EVD, QR
Option 3: Normalized correlation
FFS: whether CPIs in different domains are reported separately or jointly
Option 4: Channel matrix (utilizing the explicit CSI report)
Option 5: Explicit system parameter, e.g., codebook parameter, RS parameter.
Companies to provide details of applicable use cases for the above options.
Companies report calculation assumption of the channel covariance matrix/spectrum, e.g., average over time domain, average over frequency domain, average over spatial domain.
Note: Strive for common report quantities for use cases for a certain domain, if applicable.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.1-a014`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For the evaluation of stand-alone reporting for CJT calibration report, consider the following aspects:
Reporting quantities of Rel-19 CJTC-Dd/F/P can be candidates
xTRP delay offset report
Study dynamic range ADO and resolution MFO
Rel-19 CJTC-Dd dynamic range and resolution can be considered as a starting point
FFS: other candidate values of ADO and MDO
xTRP frequency offset report
Study dynamic range AFO and resolution MFO
Rel-19 CJTC-F dynamic range and resolution can be considered as a starting point
FFS: other candidate values of AFO and MFO
xTRP phase offset report
Study resolution MP and frequency granularity (WB, SB)
Rel-19 CJTC-P resolution can be considered as a starting point
FFS: other candidate values of MP
Companies to report how to acquire mTRP CSI for evaluation, e.g., SRS-based CSI acquisition or CJT CSI report
Companies to report the modeling of CJT calibration report, including reporting periodicity, residual offset and fluctuation, all under realistic assumption
Companies to report assumption of measurement accuracy error levels
FFS on measurement RS requirement, e.g., frequency density and bandwidth, # of RS symbols, the gap between RS symbols
Assumption on algorithms to determine delay/frequency/phase offset report
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.1-a015`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For the study of explicit CSI feedback, the evaluation considers the following aspects:
Form of explicit CSI
Opt-A: information facilitating NW reconstruction of the channel matrix H (e.g., NRX x NTX) per frequency granularity unit
Note:  NRX does not necessarily mean the number of UE Rx physical antenna(s)
Opt-B: information facilitating NW reconstruction of H’H per frequency granularity unit
Companies to report compression/quantization scheme used for the evaluation
Handling of link adaptation via at least one of the following options
Opt-1: CQI/RI information in another report (e.g., based on CSI-RS or DMRS)
Opt-2: Assistance information (e.g., L1-SINR, L1-RSRP, Interference-plus-noise (IpN) information) in the same explicit CSI report or another report
Opt-3: the explicit feedback considering pre-whitening channel or channel covariance
Note: other options are not precluded.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.1-a016`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
Draft LS R1-2606904 is endorsed in principle.
Final LS R1-2606905 is approved.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.1-a017`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For evaluation on precoded CSI-RS without considering CSI-RS overhead reduction:
Assume cell-specific wideband precoded CSI-RS, e.g., the number of precoded CSI-RS ports is same as the number of TXRUs at aNB
Company reports the precoder of CSI-RS, and information/how to determinate the precoder.
The following CSI feedback scheme can be considered for the evaluation:
Option 1: Type I-like (W1W2) and/or eType II-like (W1W2Wf) CSI reporting with port-selection (PS) basis
Option 2: Type I-like (W1W2) and/or eType II-like (W1W2Wf) CSI reporting with NR DFT basis with reconstruction information
Option 3: Type I-like (W1W2) and/or eType II-like(W1W2Wf) CSI reporting with NR DFT basis (CSI-RS port precoder is transparent to UE)
Company report how NW utilized the reported CSI for PDSCH precoder determination.
FFS on other basis, e.g., the basis constructed from combined 2D DFT beams/ port-selection (PS) basis
Benchmark:
Type I and eType II codebook with non-precoded CSI-RS
Companies report the QCL related assumptions
Note: Precoded CSI-RS with less density in spatial domain is to be discussed separately.
Note: downloadable basis/precoder (e.g. FD basis/precoder associated with each precoded CSI-RS port) can be considered additionally with precoded CSI-RS and the assumption/consideration for downloadable basis is taken into account
Note: the PAPR issue of precoded CSI-RS is to be studied.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.1-a018`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For the evaluation on the benefit of early CSI triggering/reporting, considering the following aspects:
Potential scenarios/use cases:
UE transition from IDLE/INACTIVE to CONNECTED mode,
During activation of serving cells /carriers
Mobility
Note: Early beam report is to be discussed separately
Other use cases are not precluded.
For each potential use case, studying details of
Report quantities for each use case
RS for measurement
Benchmark
KPI
Note: Strive to minimize Msg 1 impact.
Note: Both measured and predicted CSI can be considered, if appliable.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.1-a019`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For the evaluation on PDSCH DMRS-based CSI for PDSCH link adaptation, the following is consideration:
For channel measurement, the DMRS port(s) associated with data is considered as the baseline
FFS on whether to consider DMRS port(s) allocated with PDSCH but not associated with the data
For interference measurement (when needed), company to report how to acquire interference information.
Company to report the UE assumptions for DMRS-based CSI calculation.
R1-2606902	Feature lead summary #9 on DL-based CSI acquisition	Moderator (Samsung), Moderator (vivo)
R1-2606876	Feature lead summary #8 on DL-based CSI acquisition	Moderator (Samsung), Moderator (vivo)
R1-2606875	Feature lead summary #8 on DL-based CSI acquisition	Moderator (Samsung), Moderator (vivo)
R1-2606873	Feature lead summary #7 on DL-based CSI acquisition	Moderator (Samsung), Moderator (vivo)
R1-2605835	Feature lead summary #1 on DL-based CSI acquisition	Moderator (Samsung), Moderator (vivo)
R1-2605836	Feature lead summary #3 on DL-based CSI acquisition	Moderator (Samsung), Moderator (vivo)
R1-2605837	Feature lead summary #5 on DL-based CSI acquisition	Moderator (Samsung), Moderator (vivo)
R1-2605466	Feature lead summary #2 on DL-based CSI acquisition	Moderator (Samsung), Moderator (vivo)
R1-2605467	Feature lead summary #4 on DL-based CSI acquisition	Moderator (Samsung), Moderator (vivo)
R1-2605468	Feature lead summary #6 on DL-based CSI acquisition	Moderator (Samsung), Moderator (vivo)
R1-2605221	Discussion on aspects of downlink-based CSI acquisition for 6GR air interface	FUTUREWEI
R1-2605226	6GR CSI: Aspects of Downlink-based CSI Acquisition	InterDigital, Inc.
R1-2605260	Discussion on aspects of downlink-based CSI acquisition for 6GR	Spreadtrum, UNISOC
R1-2605298	Aspects of downlink-based CSI acquisition	Huawei, HiSilicon
R1-2605320	Aspects of downlink-based CSI acquisition	MediaTek Inc.
R1-2605334	Discussion on aspects of downlink-based CSI acquisition	ZTE Corporation, Sanechips
R1-2605352	Some aspects of Downlink-based CSI Acquisition	Kyocera Corporation
R1-2605388	On downlink-based CSI acquisition in 6GR	Nokia
R1-2605411	Discussion on aspects of downlink-based CSI acquisition	KT Corp.
R1-2605426	On downlink-based CSI acquisition in 6GR	Jio Platforms
R1-2605465	Discussion on aspects of downlink-based CSI acquisition for 6GR	vivo
R1-2605466	Feature lead summary #2 on DL-based CSI acquisition	Moderator (Samsung), Moderator (vivo)
R1-2605467	Feature lead summary #4 on DL-based CSI acquisition	Moderator (Samsung), Moderator (vivo)
R1-2605468	Feature lead summary #6 on DL-based CSI acquisition	Moderator (Samsung), Moderator (vivo)
R1-2605487	Discussion on aspects of downlink-based CSI acquisition for 6GR	NICT
R1-2605490	Aspects of downlink-based CSI acquisition	Tejas Networks Limited
R1-2605527	IMU Views on DL-Based CSI Acquisition	IMU
R1-2605569	Discussion on DL CSI acquisition for 6GR	Xiaomi
R1-2605596	Discussion on DL-based CSI acquisition and CSI-RS design	TCL
R1-2605637	Discussion on downlink-based CSI acquisition	CMCC
R1-2605678	Views on Aspects of downlink-based CSI acquisition	Ofinno
R1-2605723	On downlink-based CSI acquisition for 6GR	CATT
R1-2605834	Discussion on downlink-based CSI acquisition	Samsung
R1-2605870	Discussion on downlink-based CSI acquisition	NEC
R1-2605913	Discussion on downlink based CSI acquisition	OPPO
R1-2605938	Discussion on Aspects of Downlink-Based CSI Acquisition for 6GR	Pengcheng Laboratory, BUPT, X-NET
R1-2605952	Aspects of downlink-based CSI acquisition	Lenovo
R1-2605961	Discussion on Aspects of Downlink-based CSI Acquisition	Google
R1-2605976	Discussion of aspects of downlink-based CSI acquisition	Sony
R1-2606028	On downlink-based CSI acquisition	Apple
R1-2606054	Aspects of downlink-based CSI acquisition for 6GR study	Intel
R1-2606085	Discussion on aspects of downlink-based CSI acquisition	China Telecom, BUPT
R1-2606105	Discussion on downlink-based CSI acquisition	1Finity
R1-2606117	Discussion on aspects of downlink-based CSI acquisition	LG Electronics
R1-2606172	Discussion on DL-based CSI acquisition	IIT Kanpur
R1-2606188	Discussion on downlink-based CSI acquisition	HONOR
R1-2606210	Discussion on Aspects of Downlink-Based CSI Acquisition for 6GR	BUPT,X-NET,PCL,University of Surrey
R1-2606215	Discussion on downlink CSI acquisition	Southeast University
R1-2606244	Discussion on downlink-based CSI acquisition	ETRI
R1-2606282	PCA-Based Projection Matrix Design for JSCM-based CSI compression	NTU
R1-2606296	CSI Acquisition improvement for non-constant modulus codebook 	Orange
R1-2606313	Interference Coordination / Management for 6G Fixed Wireless Access	T-Mobile USA Inc., Ericsson, MediaTek, Verizon
R1-2606325	Downlink-based CSI acquisition for 6GR air interface	NVIDIA
R1-2606381	Aspects of downlink-based CSI acquisition	Qualcomm Incorporated
R1-2606791	Aspects of downlink-based CSI acquisition	Qualcomm Incorporated
(Revision of R1-2606381)
R1-2606431	Aspects of DL-based 6GR Channel Acquisition	AT&T
R1-2606445	Aspects of downlink-based CSI acquisiton	Sharp
R1-2606507	Discussion on Aspects of downlink-based CSI acquisition	NTT DOCOMO, INC.
R1-2606530	Views on aspects of downlink-based CSI Acquisition	Ericsson
R1-2606301	Massive MIMO for 6GR NTN	PML
R1-2606536	Discussion on CSI prediction and CSI-RS overhead reduction	ITRI
R1-2606553	Discussion on aspects of the DL-based CSI acquisition	Quectel
R1-2606571	Discussion on downlink based CSI acquisition	Shanghai Jiao Tong University, Toyota
R1-2606572	Discussion on DL-based CSI Acquisition for 6G	Panasonic
R1-2606599	Discussion on downlink CSI acquisition for 6GR	Indian Institute of Tech (M)
R1-2606619	Discussions on DL-based CSI acquisition design	CAICT, BJTU
R1-2606632	Downlink CSI acquisition aspects for 6G	Fraunhofer IIS, Fraunhofer HHI
R1-2606649	Views on DL based CSI acquisition	CEWiT
R1-2606691	Discussion on Aspects of Downlink-based CSI Acquisition	Rakuten Symphony
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.1-a020`

### [6G/Rel-20 RAN1#126] `conclusion` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For the 6GR codebook design for CSI report, for discussion purposes, based on the previous agreements, the following separate category is used:
Category for resolution: low- and high-resolution, comprising at least the following criteria:
Target scenario (e.g., SU-MIMO, MU-MIMO)
Feedback overhead
UE complexity in CSI calculation
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.1-c001`

### [6G/Rel-20 RAN1#126] `observation` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For performance evaluation of maximum number of ports of CSI-RS for CSI acquisition in 6GR, the following is observed for around 7GHz
Under eType II-like CSI feedback assumption
For 256 ports
[3] sources show 256-port provides [+5 ~ +20]% system-level throughput gain compared with 128-port at cell average
[1] sources show 256-port provides [+3 ~ +34]% system-level throughput gain compared with 128-port at cell edge
[1] source shows 256-port provides [+5]% system-level throughput gain compared with 128-port at cell average, and [62]% system-level throughput loss compared with 128-port at cell edge
[1] source shows 256-port provides [+18]% system-level throughput gain compared with 128-port at cell center
For 512 ports
[1] source shows 512-port provides [+15 ~ +31]% system-level throughput gain compared with 256-port at cell average, while [1] source shows 512-port provides [7]% system level throughput loss  ~ [+1]% system-level throughput gain compared with 256-port at cell average
[1] source shows 512-port provides [+31 ~ +55]% system-level throughput gain compared with 256-port at cell edge
[1] source shows SRS based CSI acquisition suffers [+26 ~ +72]% SE loss compared with 512-port CSI-RS
Under Type I-like CSI feedback assumption
For 256 ports
[3] sources show 256-port provides [+5 ~ +25]% system-level throughput gain compared with 128-port at cell average
[3] sources show 256-port provides [+5 ~ +61]% system-level throughput gain compared with 128-port at cell edge
[1] sources shows 256-port provides [+8]% system-level throughput gain compared with 128-port at cell average, and [50]% system-level throughput loss compared with 128-port at cell edge
[1] source shows 256-port provides [+1 ~ +17]% system-level throughput gain compared with 128-port at cell center
[1] source shows 256-port causes up to [60 ~ 84]% link-level throughput loss compared with 128-port at -10dB SNR. The loss shrinks and vanishes when SNR increases, and [+2 ~ +3]% gain is observed after -6 or -4 dB SNR, depending on CDL modelling.
[1] sources shows the link-level SNR loss of 256-port compared with 128-port is smaller than [0.3] dB at low SNR range
[1] source shows 256-port provides [3]% link-level SE loss compared with 128-port, whereas the required SNR of 128-port and 256-port converge to reach the same 1% BLER operation point
For 512 ports
[2] sources show 512-port provides [10]% system-level throughput loss ~ [+3]% system-level throughput gain compared with 256-port at cell average
[1] sources show 512-port provides [6]% system-level throughput loss ~ [+3]% system-level throughput gain compared with 256-port at cell edge
[1] sources show 512-port provides [8]% system-level throughput loss ~ [+2]% system-level throughput gain compared with 256-port at cell center
[1] source shows 512-port provides [+22 ~ +52]% system-level throughput gain compared with 256-port at cell average
[1] source shows 512-port provides [+51 ~ +86]% system-level throughput gain compared with 256-port at cell edge
[1] source shows 512-port provides [2]% link-level SE loss compared with 256-port, whereas the required SNR of 512-port is [2] dB higher than 256-port to reach the same 1% BLER operation point
Under ideal CSI feedback assumption
For 256 ports
[4] sources show 256-port provides [+10 ~ +47]% system-level throughput gain compared with 128-port at cell average
[4] sources show 256-port provides [+10 ~ +77]% system-level throughput gain compared with 128-port at cell edge
[1] sources show 256-port provides [0 ~ +35]% system-level throughput gain compared with 128-port at cell center
For 512 ports
[2] sources show 512-port provides [+4 ~ +19]% system-level throughput gain compared with 256-port at cell average
[1] source show 512-port provides [+3 ~ +33]% system-level throughput gain compared with 256-port at cell edge
[1] sources show 512-port provides [63]% system-level throughput loss compared with 256-port at cell edge
[1] sources show 512-port provides [0]% system-level throughput gain compared with 256-port at cell center
Note: for each individual source, the above results are from a same number of antennas at BS side, when comparing different numbers of ports.
Note: the above results do not model UCI error in the simulations.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.1-o001`

### [6G/Rel-20 RAN1#126] `observation` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For the potential PAPR impact and potential solutions for PAPR reduction for JSCM-based CSI compression, the following options have been studied in RAN 1, until RAN 1 #126:
Option 0: Compression outputs are directly mapped to DFT-s-OFDM or CP-OFDM uplink transmission as modulation constellation without any additional operation
Option 1: Compression outputs are mapped to certain discrete constellation, and then mapped to DFT-s-OFDM or CP-OFDM uplink transmission, at least considering the following as the discrete constellation
NR modulation constellations, e.g., 16QAM, 64QAM, 256QAM, 1024QAM
Other modulation constellations, e.g., 64APSK, constellation point pruning from NR QAM, other customized (fixed) constellations
Note: To reduce PAPR (by achieving uniform distribution of JSCM symbols), regularization can be additionally considered as part of loss function as implementation
Note: the training may or may not be aware of the mapping.
Option 2: Compression outputs are mapped/restricted, e.g., with restricted amplitude(s), and then mapped to DFT-s-OFDM or CP-OFDM uplink transmission as modulation constellation
Note: on top of Option 0/1/2, PAPR restriction during the training with or without additional activation layer, as part of loss function, can be considered.
Other solutions or potential issues related to PAPR can be further studied.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.1-o002`

### [6G/Rel-20 RAN1#126] `observation` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
The following observations on PAPR/Cubic metric/output power variation (cross OFDM symbols) have been made for the above options at least for projection-matrix-based compression for JSCM, until RAN 1 #126:
With DFT-s-OFDM as uplink waveform,
For Option 0: 13 sources showed without any additional operation, PAPR @CCDF= 0.1% of JSCM increases by 1.5~2dB compared to conventional 16-/64-/256-QAM constellation, and ~3dB compared to conventional QPSK constellation.
4 sources showed that with Kronecker-based matrices, the PAPR @CCDF= 0.1% additionally increases by 1~2.5dB.
1 source showed with PAPR aware training, the PAPR @CCDF= 0.1% is ~0.2dB lower or 0.1dB higher compared to conventional 16-QAM.
1 source showed with PAPR aware training, the PAPR @CCDF= 0.1% is ~0.3dB lower compared to conventional 256-QAM.
1 source showed clipping aware training, the PAPR @CCDF= 0.1% is 9dB.
1 source showed that with PAPR aware training towards 6RB, the PAPR @CCDF= 0.1% is about ~6dB (comparable to QPSK), however, if the number of RBs used in inference is 1RB, the PAPR @CCDF= 0.1% increased to 8dB (i.e., 2dB higher than QPSK).
1 source showed that JSCM followed by 2-stage PAPR reduction (first stage trainable constellation mapper followed by second stage adaptive PAPR reduction block), the PAPR @CCDF= 0.1% can be reduced to 4dB (PAPR = 8dB @CCDF= 0.01%).
1 source showed the cubic metric @CCDF=0.1% increases ~2.9dB compared to conventional QPSK.
1 source showed JSCM output power variation across OFDM symbols is larger than 1K-QAM PUSCH with assumption of frequency first, time second mapping of JSCM outputs to allocated REs (on to 12 subcarriers in freq domain).
For Option 1: 13 companies showed that the PAPR can be reduced but remain higher than conventional QAM
By mapping to conventional constellations, e.g., 64-QAM or 256-QAM,
13 sources showed PAPR @CCDF= 0.1% can be reduced but remain 0.2~1dB higher than conventional 64-QAM/256-QAM,
1 source showed PAPR @CCDF= 1% can be ~0.5dB lower than conventional constellation, i.e., 64-QAM/256-QAM with scaling of the compression outputs before mapping to the discrete constellations and the training is not aware of the mapping.
1 source showed with regularization as part of loss function and then mapping to 64-QAM, the PAPR is comparable to conventional 64-QAM.
2 sources showed that with Kronecker-based matrices, the PAPR @CCDF= 0.1% is ~0.2 dB higher than conventional 64-QAM (12 subcarriers and 1024 FFT, or 12 subcarriers and 128 FFT). 1 source showed that with Kronecker-based matrices, the PAPR @CCDF= 0.1% is ~1.5dB higher than conventional 64-QAM (64 subcarriers with 2048-FFT).
1 source showed, that varying the number of Resource Elements (REs) impacts the PAPR:
Dedicated model: with 32 REs, the PAPR at CCDF = 0.1% can be ~0.5 dB lower than that of a conventional 64-QAM constellation. However, with 48 or 64 REs, the PAPR is either comparable to or ~0.3 dB higher than conventional 64-QAM.
Scalable model: With 32 REs, the PAPR is comparable to conventional 64-QAM. However, with 48 or 64 REs, the PAPR at CCDF = 0.1% can be ~0.7 dB or 1.8 dB higher, respectively, than conventional 64-QAM.
1 source showed that different loss functions during training may lead to differences in the statistical distribution/probability of the mapped constellation points from the compression outputs. Specifically, the PAPR @ CCDF = 0.1% might vary by 0.3 dB to 1 dB.
By mapping to other modulation constellations,
1 source showed with mapping to 64APSK, the PAPR @CCDF= 0.1% is 0.2 dB higher than conventional 64-QAM.
2 sources showed with mapping to constellation point pruning from NR QAM, PAPR @CCDF= 0.1% is comparable or up to 1dB lower comparing to conventional constellation, i.e., 64-QAM or 256-QAM.
For Option 2: By mapping/restricting, some companies showed that the PAPR can be reduced to comparable to conventional QPSK or 16-QAM
4 sources showed with mapping to constant amplitude, PAPR is comparable to conventional QPSK and 2 sources showed PAPR @CCDF= 0.1% is ~0.5dB lower than conventional QPSK.
2 sources showed with mapping to annular constellation, with scaling factor = 0.5, the PAPR is comparable to conventional 16-QAM.
1 source showed that with mapping to annular constellation, with dense matrix or with Kronecker-based matrices, the PAPR @CCDF= 0.1% is reduced to 8.5dB.
1 source showed with both the maximum and minimum amplitudes, the PAPR @CCDF= 1% is comparable to conventional QPSK. And with peak limited only, the PAPR @CCDF= 1% is ~0.4dB higher than conventional 16-QAM.
Note: no multiplexing with other UL transmission is assumed in the above evaluation.
Note: 12 to 72 of subcarriers are assumed with 128, 1024 or 2048 or 4096 FFT size.
With CP-OFDM as uplink waveform,
For Option 0(without and additional operation) and. for Option 1, by mapping to conventional constellations, e.g., 64-QAM or 256-QAM,
5 sources showed the PAPR of JSCM is comparable to conventional 16-/64-/256-QAM.
1 source showed for 1 RB, the PAPR @CCDF= 0.1% is 1dB higher than conventional 16-/64-/256-QAM.
1 source showed the cubic metric @CCDF=0.1% increases ~1.9dB compared to conventional QPSK
For Option 1,
By mapping to conventional constellations, e.g., 64-QAM or 256-QAM,
4 sources showed the PAPR of JSCM is comparable to conventional 16-/64-/256-QAM.
By mapping to other modulation constellations,
1 source showed with mapping to constellation point pruning from NR QAM, PAPR is comparable conventional QPSK, or conventional 16-/64-/256-QAM.
For Option 2: By mapping/restricting,
1 source showed with mapping to constant amplitude or annular constellation the PAPR is comparable to conventional QPSK/16-QAM.
1 source showed with both the maximum and minimum amplitudes, the PAPR @CCDF= 1% is about 7.2dB (2.8dB lower than conventional QPSK). And with peak limited only, the PAPR is comparable to conventional QPSK/16QAM.
Note: no multiplexing with other UL transmission is assumed in the above evaluation.
Note: 12 to 72 of subcarriers is assumed with 1024 or 2048 FFT size.
Note: in the above observations, for conventional modulations for both DFT-s-OFDM and CP-OFDM waveform, no additional PAPR reduction technique is considered.
Note: the observation can be further updated based on new results in future meetings.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.1-o003`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.2 Aspects of uplink-based CSI acquisition

```text
For SRS, at least cyclic-shift and/or comb-offset are supported.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.2-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.2 Aspects of uplink-based CSI acquisition

```text
Study whether/how TD-OCC can be supported together with SRS repetition to enable multiplexing of SRS ports, and at least take the following aspects into consideration:
OCC lengths: e.g., TD-OCC2, TD-OCC4, other lengths
Whether it is applicable to intra- and inter-UE multiplexing of SRS ports
TD-OCC related interference randomization scheme
The non-orthogonality incurred by partial dropping
Channel variation in time domain
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.2-a002`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.2 Aspects of uplink-based CSI acquisition

```text
For at least increasing SRS capacity/reducing overhead/improve coverage purposes sparse SRS patterns with comb values larger than 8, study at least comb 12 and 16 with consideration of at least the following aspects.
SRS sequences
MPR and PAPR/CM impact
Max number of cyclic shifts for the corresponding comb value
Minimum available bandwidth and its corresponding sequence
Channel estimation performance
Applicable RB sizes (e.g., RB size >= 8)
Any other performance impacts
FFS other comb values.
Note: RAN4 input on maximum power boosting is needed
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.2-a003`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.2 Aspects of uplink-based CSI acquisition

```text
Support cross-slot SRS transmission at least for consecutive S+U slots
FFS: whether to support cross-slot SRS transmission spanning any two consecutive slots, e.g., U+U slots.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.2-a004`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.2 Aspects of uplink-based CSI acquisition

```text
Study at least the following aspects of precoded SRS
Intended usage (e.g., for UL CSI and/or DL CSI)
Feasibility under specific UE architectures (e.g., xTyR configurations for DL CSI)
Gain compared to non-precoded SRS, accounting for practical impairments (e.g., PAPR/CM loss, realistic UE reciprocity, and UE coherency assumptions)
Methods for precoder derivation of precoded SRS:
Method-1: Determined by NW (e.g., derived from the measurements of SRS and indications from NW)
Method-2: Determined (with/without reported) by UE via DL measurement
FFS: UE UL/DL reciprocity calibration
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.2-a005`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.2 Aspects of uplink-based CSI acquisition

```text
For SRS of 6GR, study the following frequency hopping aspects
A single-level frequency hopping
hopping over bandwidth with one or multiple frequency hops
Two-level frequency hopping
First level: hopping over BW with one or multiple frequency hops
Second level: hopping within each frequency hop of the first-level hopping
For single or two levels, consider at least the following options
Nested tree-like frequency hopping pattern
Sequential hopping pattern
Pattern following RB offset provided by NW
With/without Intra-repetition hopping in the second level
Note: the case with larger DL BW than UL BW will be discussed separately
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.2-a006`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.2 Aspects of uplink-based CSI acquisition

```text
To support maximum SRS bandwidth beyond 272 PRBs in a carrier, consider the following options:
Option 1: Table based approach (similar to NR)
Option 1-1:
Refer to the bandwidth entries for up to 272 PRBs in the table from NR
Introduce new SRS bandwidth entries from 272 to [544] PRBs
Option 1-2:
Scale up the SRS bandwidth entries in the table from NR by integer factor, e.g. value of 2 or 4
Option 1-3:
The overall SRS bandwidth is divided into more than one part, in which each part can reuse SRS bandwidth entries in the table from NR.
Option 2: Flexible SRS bandwidth determination and frequency hopping
Replace the existing table-based SRS bandwidth determination with parameter-based frequency hopping pattern determination provided by NW
R1-2605725	Moderator summary#1 on uplink-based CSI acquisition	Moderator (CATT)
R1-2605726	Moderator summary#2 on uplink-based CSI acquisition	Moderator (CATT)
R1-2605727	Moderator summary#3 on uplink-based CSI acquisition	Moderator (CATT)
R1-2605728	Moderator summary#4 on uplink-based CSI acquisition	Moderator (CATT)
R1-2605222	Aspects of uplink-based CSI acquisition	FUTUREWEI
R1-2605227	6GR CSI: Aspects of Uplink-based CSI Acquisition	InterDigital, Inc.
R1-2605261	Discussion on aspects of uplink-based CSI acquisition for 6GR	Spreadtrum, UNISOC
R1-2605299	Aspects of uplink-based CSI acquisition	Huawei, HiSilicon
R1-2605321	Aspects of uplink-based CSI acquisition	MediaTek Inc.
R1-2605335	Discussion on aspects of uplink-based CSI acquisition	ZTE Corporation, Sanechips
R1-2605389	On uplink-based CSI acquisition in 6GR	Nokia
R1-2605414	 Discussion on 6G uplink based CSI acquisition	Pengcheng Laboratory
R1-2605427	On uplink-based CSI acquisition for 6GR	Jio Platforms
R1-2605469	Discussion on aspects of uplink-based CSI acquisition for 6GR	vivo
R1-2605491	Aspects of uplink-based CSI acquisition	Tejas Networks Limited
R1-2605525	Discussion on aspects of uplink-based CSI acquisition	TCL
R1-2605570	Discussion on UL CSI acquisition for 6GR	Xiaomi
R1-2605638	Discussion on uplink-based CSI acquisition	CMCC
R1-2605689	Aspects of uplink-based CSI acquisition	Lenovo
R1-2605724	Views on uplink-based CSI acquisition for 6GR	CATT
R1-2605838	Discussion on UL-based CSI acquisition and SRS design	Samsung
R1-2605856	Views on uplink-based CSI acquisition	Ericsson
R1-2605871	Discussion on uplink-based CSI acquisition	NEC
R1-2605914	Discussion on uplink based CSI acquisition	OPPO
R1-2605962	Discussion on Aspects of Uplink-based CSI Acquisition	Google
R1-2605977	Discussion of aspects of uplink-based CSI acquisition	Sony
R1-2605995	Discussion on aspects of uplink-based CSI acquisition	Ofinno
R1-2606029	On UL based CSI acquisition for 6GR	Apple
R1-2606057	Discussion on aspects of uplink-based CSI acquisition	Panasonic
R1-2606086	Discussion on aspects of uplink-based CSI acquisition	China Telecom
R1-2606106	Discussion on uplink-based CSI acquisition	1Finity
R1-2606118	Discussion on aspects of uplink-based CSI acquisition	LG Electronics
R1-2606245	Discussion on uplink-based CSI acquisition	ETRI
R1-2606382	Aspects of uplink-based CSI acquisition	Qualcomm Incorporated
R1-2606432	Aspects of UL-based 6GR Channel Acquisition	AT&T
R1-2606446	Aspects of uplink-based CSI acquisition	Sharp
R1-2606508	Discussion on Aspects of uplink-based CSI acquisition	NTT DOCOMO, INC.
R1-2606550	Uplink-based CSI acquisition for 6GR air interface	NVIDIA
R1-2606606	Discussion on aspects of uplink-based CSI acquisition 	Rakuten Mobile, Inc
R1-2606620	Aspects of uplink-based CSI acquisition	CAICT, BJTU
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.2-a007`

### [6G/Rel-20 RAN1#126] `observation` 10.5.3.2 Aspects of uplink-based CSI acquisition

```text
For 6GR SRS sequence, the following candidate options are observed:
Option 1: Enhanced ZC sequence design based on sampling a piecewise LFM chirp at a rate higher than the sweeping bandwidth, e.g., [R1-2606382]
Option 2: Time-domain/Frequency-domain design e.g., Costas-based \ sequence design, e.g., [R1-2605321]
Option 3: Sequence construction via concatenation of segments of ZC sequence, with each rotated by a per-segment phase offset, e.g., [R1-2605724]
Option 4: Sequence construction via concatenation of sequence blocks, with each rotated by a per-block phase offset, e.g., [R1-2605856]
Option 5: Sequence construction via concatenation of sequence blocks, without separate phase rotation per block, e.g., [R1-2605856]
Option 6: Enhancements to ZC sequence root selection, e.g., time-domain root selection for ZC-based sequence, e.g., [R1-2606029], configurability of  value by aNB , e.g.,  [R1-2605389], new ZC root determination equation for frequency domain ZC sequence mapping , e.g., [R1-2605838], [R1-2605570], [R1-2606508]
Option 7: ZCbased sequences as in NR, and expand the sequencegroup number (e.g., from 30 to 46, 58 or 70) and the basesequence number (e.g., from 2 to 3, 4, 5 or 6) to enlarge the SRS rootsequence pool, e.g., [R1-2605335]
Option 8: Polynomial phase sequence, e.g.,  , e.g., [R1-2605299]
Option 9: Phase optimized ZC sequence, i.e., based on Gerchberg-Saxton algorithm, e.g., [R1-2605962]
Option 10: Enhanced CGS with expanded phase-rotation alphabets (e.g., 64-PSK or higher) and/or with new lengths, e.g., [R1-2605469]
Option 11: ZC and CGS sequences in NR with bandwidth allocation≤272 RBs
Study how to support larger SRS bandwidth
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.2-o001`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.3 Other aspects

```text
Support single-port RS in addition to SSB for finer time and frequency tracking as a baseline for connected mode for 6GR.
Note: It does not preclude further study on multi-port RS for finer time and frequency tracking.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.3-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.3 Other aspects

```text
For the evaluation of joint DL/UL based CSI acquisition, at least take the following baseline for use case 1
Baseline#1: DL CSI acquisition based on SRS only
Baseline#2: DL CSI acquisition based on CSI-RS only
Additionally consider the Rel-19 UE antenna model defined in TR 38.901.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.3-a002`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.3 Other aspects

```text
For the evaluation of joint DL/UL based CSI acquisition, additionally consider the following KPIs
UPT
Intermediate KPI (e.g., SGCS, NMSE)
RS overhead
Feedback overhead
Computation complexity and model complexity, if any
Storage complexity, if any
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.3-a003`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.3 Other aspects

```text
Use the following template to collect the simulation results for use case 1:
| Simulation assumptions on scenario, MIMO scheme, e.g., carrier frequency, channel model, antenna port layouts at aNB and antenna port layouts at UE, etc. |  |
| --- | --- |
| Assistance information |  |
| How to obtain and report, e.g., format and quantization, the assistance information |  |
| How to use the assistance information |  |
| CSI-RS and CSI report configuration, if any |  |
| SRS configuration |  |
| Performance gain compared with baseline schemes |  |
| Observations in terms of the agreed KPIs |  |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.3-a004`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.3 Other aspects

```text
Use the following template to collect the simulation results for use case 2:
| Simulation assumptions on scenario, MIMO scheme, e.g., carrier frequency, channel model, antenna port layouts at aNB and UE etc. |  |
| --- | --- |
| Assistance information |  |
| How to obtain and report the assistance information |  |
| How to use the assistance information for MCS and RI selection. |  |
| CSI-RS and CSI report configuration, if any |  |
| SRS configuration |  |
| Performance gain compared with baseline schemes |  |
| Observations in terms of the agreed KPIs |  |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.3-a005`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.3 Other aspects

```text
For the evaluation of joint DL/UL based CSI acquisition, at least take the following baseline for use case 2
Baseline #1: DL CSI acquisition based on precoded CSI-RS and SRS, where PDSCH precoder is determined based on SRS, and rank and MCS follows the non-PMI report based on precoded CSI-RS.
Companies to report details about how the network determines the CSI-RS precoder
Baseline#2: DL CSI acquisition based on both SRS and CSI-RS, where UE reports CRI/PMI/RI/CQI based on CSI-RS, and network determines rank and MCS based on the SRS channel estimation and the reported CRI/PMI/RI/CQI
Companies to report details about how network determines rank and MCS based on the SRS channel estimation and the reported CRI/PMI/RI/CQI
It does not mean that CRI-RI-CQI report is supported.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.3-a006`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.3 Other aspects

```text
Further study the following proposal and strive to make agreement for RAN1#126bis meeting
Support of both periodic RS in addition to SSB and aperiodic RS for fine time and frequency tracking at least for connected mode in 6GR as baseline
UE in connected mode uses periodic RS and uses aperiodic RS, for finer time and frequency tracking
Periodic RS
RS with periodicity including at least 20ms, 40ms, 80ms and, if different, then maximum periodicity of SSB
FFS: Whether periodic RS for finer time and frequency tracking can be used in idle mode
Note: Periodicities of SSB will not be discussed in this agenda
Aperiodic RS
Conditions under which aperiodic RS is used, e.g. long periodicities for periodic RS
FFS: Whether aperiodic RS is associated with another periodic or aperiodic RS
Following options are considered
Option 1: RS other than PDSCH DMRS or PDCCH DMRS
Option 2: PDSCH DMRS or PDCCH DMRS
Note: DMRS pattern/design will not be discussed in this agenda
Aperiodic RS may have the same or different structure/pattern from that of periodic RS
Note 1: Whether and how to use SSB for finer time and frequency tracking is up to UE implementation
Note 2: The agreed KPI in RAN1#124 along with RS overhead should be considered for the study of the time/frequency/spatial domain factors for the periodic and aperiodic RS for finer time and frequency tracking targeting the following use cases:
Single/Multi-TRP
Single/Multi-carrier
Larger DL channel BW, e.g., up to 400MHz.
For both periodic and aperiodic RS, details on time/frequency/spatial domain factor are separately studied based on the agreed candidates in RAN1#124bis and RAN1#125
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.3-a007`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.3 Other aspects

```text
On top of agreement in RAN1#125, further study and evaluate the following sub use cases for joint DL/UL CSI acquisition use case 1
Use case 1A: Assisting SRS channel estimation, e.g., interference mitigation and channel interpolation
Use case 1B: Assisting aNB side compensation for SRS reception with SRS power imbalance
Use case 1C: CSI feedback and SRS fusion for full dimension channel matrix acquisition
Use case 1D: Assisting SRS configuration
R1-2606931	Final FL summary on other aspects related to CSI	Moderator (Lenovo)
Final post-meeting summary for this agenda item.
R1-2605223	Other Aspects for CSI acquisition	FUTUREWEI
R1-2605228	6GR CSI: Other Aspects	InterDigital, Inc.
R1-2605262	Discussion on other aspects of CSI acquisition and report for 6GR	Spreadtrum, UNISOC
R1-2605300	Other aspects for MIMO operation	Huawei, HiSilicon
R1-2605322	Time/frequency tracking and joint DL/UL CSI acquisition	MediaTek Inc.
R1-2605336	Discussion on other aspects of CSI acquisition and channel tracking	ZTE Corporation, Sanechips
R1-2605390	Other aspects of 6GR physical layer operation	Nokia
R1-2605470	Discussion on other aspects of CSI acquisition for 6GR	vivo
R1-2605571	Discussion on RS for time/frequency tracking	Xiaomi
R1-2605639	Discussion on other aspects of CSI acquisition and report	CMCC
R1-2605657	Other aspects of CSI acquisition	TCL
R1-2605694	Discussion on other aspects of CSI acquisition for 6GR	Lenovo
R1-2605729	Views on other aspects for MIMO operation in 6GR	CATT
R1-2605839	Discussion on other aspects on CSI acquisition and report	Samsung
R1-2605872	Discussion on other aspects for CSI and reference signals	NEC
R1-2605915	Discussion on TRS and Joint DL/UL CSI	OPPO
R1-2605963	Discussion on Other Aspects of CSI Acquisition	Google
R1-2605978	Discussion of other aspects of CSI acquisition	Sony
R1-2605996	Discussion on other aspects of CSI acquisition and report	Ofinno
R1-2606030	On other aspects of CSI acquisition	Apple
R1-2606107	Discussion on other aspects related to CSI	1Finity
R1-2606119	Discussion on TRS and joint DL/UL based CSI	LG Electronics
R1-2606246	Discussion on other aspects of CSI acquisition	ETRI
R1-2606383	Other aspects of CSI acquisition and reporting	Qualcomm Incorporated
R1-2606792	Other aspects of CSI acquisition and reporting	Qualcomm Incorporated
(Revision of R1-2606383)
R1-2606433	Other Aspects of 6GR CSI Acquisition	AT&T
R1-2606509	Discussion on Other aspects of CSI acquisition and report	NTT DOCOMO, INC.
R1-2606532	On RS for fine T/F synchronization and other CSI-related aspects	Ericsson
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.3-a008`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.4 Beam management for downlink and uplink

```text
For the study on requirement/functionality of DL RS for beam measurement, for inter-symbol NW/UE-side beam sweeping, the following is considered:
Study the following time-domain behavior of DL RS for beam measurement: aperiodic, semi-persistent and periodic.
At least support the functionality for UE to assume whether DL RSs are transmitted with same DL Tx spatial filter(s) or not.
Note: Sync-signal design is not considered herein
At least following aspects to be considered for DL RS for beam measurement:
UE complexity,
Energy efficiency,
RS overhead,
Measurement performance, and corresponding coverage.
Beam measurement/sweeping latency
Multiplexing with other data and RS
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.4-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.4 Beam management for downlink and uplink

```text
Regarding QCL framework,
At least support the following QCL properties for DL:
Doppler shift, Doppler spread, average delay, delay spread, and spatial Rx parameter
FFS: Whether/how to introduce average gain as a QCL property.
FFS: Other QCL properties
FFS: Where/how/when to use above QCL properties.
FFS: Source QCL-RS
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.4-a002`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.4 Beam management for downlink and uplink

```text
Regarding UE initiated beam management, at least the following procedure can be considered
Event detection for triggering UL transmission
UL transmission procedure
NW response, if any, to UL transmission procedure
UE behavior, if any, after receiving NW response.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.4-a003`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.4 Beam management for downlink and uplink

```text
Regarding UE initiated beam management, at least for a single-TRP operation, on event detection for triggering UL transmission, the following can be studied for Event-1 and Event-2.
Event evaluation metric/threshold,
Current/serving DL RS determination,
Candidate DL RS identification, if applicable.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.4-a004`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.4 Beam management for downlink and uplink

```text
For the study on beam measurement and report regarding DL beam measurement and report procedure on DL RS(s) for multi-TRP scenario(s), the following can be considered on Case-1:
Regarding L1-RSRP calculation, NR L1-RSRP definition can be used as the starting point.
FFS: Whether any other extension of L1-RSRP definition is needed, e.g., TRP-specific or port-specific L1-RSRP.
Regarding RS measurement requirements,
Study the need of a functionality of enabling UE to a) differentiate DL RSs from different TRPs within a cell, or b) differentiate DL RSs across cells for DL beam measurement and report.
Regarding report content/format,
Information of identifying DL RS can be included in the report as a starting point, besides for L1-RSRP
FFS: the following report content can be studied:
N DL RSs per selected TRP or per measured TRP
M DL RSs across different TRPs
FFS: Whether/How to include the information of selected TRP in the report.
FFS: other metrics, e.g., L1-SINR.
Note (Case-1): To identify/report the preferred N>1 DL beams per NW TRP/panel or across NW TRP(s)/panel(s) for supporting multi-TRP/panel transmission scheme(s).
Note: Above TRPs may belong to a same cell or different cells.
Note (for the study purpose): The above study at least considers the following transmission schemes: TDMed and DPS transmission scheme, if supported.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.4-a005`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.4 Beam management for downlink and uplink

```text
For the study on spatial/temporal/frequency domain beam measurement/prediction (relevant to AI/ML or non-AI/advanced schemes), the following is considered:
Regarding spatial/temporal domain DL Tx beam prediction and management on multi-TRP/cell(intra/inter-cell), at least support the case that the cells/TRPs corresponding to the predicted beam(s) (Set-A) are within the set of cells/TRPs corresponding to the measured beam(s) (Set-B).
FFS: Other cases that the case that at least one of the cells/TRPs corresponding to the predicted beam(s) (Set-A) are outside the set of cells/TRPs corresponding to the measured beam(s) (Set-B).
Regarding frequency domain beam measurement/prediction (cross-frequency), at least support the collocated scenarios of source and target frequencies (using same height of NW antenna(s)).
FFS: Non-collocated scenarios of source and target frequencies.
FFS: How to ensure the training and inference consistency for UE-side model, e.g., association ID.
FFS: Whether/how to indicate the combination coefficient(s), W, between measured beams (set B) for computation of the target beams (set A), e.g., matrix-based approach (from NW to UE).
Predicted results of Set-A is derived based on W and measured results of Set-B
FFS: Report content
Whether/how to report confidence level associated with reported beam, e.g., inaccurate, invalid prediction
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.4-a006`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.4 Beam management for downlink and uplink

```text
Study target usage/necessity and procedure of UE UL beam sweeping
From RAN1 perspective, as a baseline, Tx beam of UL channel/RS may be determined according to DL-RS.
Note: UE beam correspondence is assumed RAN1
Send an LS to RAN4
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.4-a007`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.4 Beam management for downlink and uplink

```text
Draft LS R1-2606909 is endorsed in principle.
Final LS R1-2606910 is agreed.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.4-a008`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.4 Beam management for downlink and uplink

```text
Regarding UE initiated beam management, on a single-TRP operation, on UL transmission procedure, the following can be studied for Event-1 and Event-2.
Candidate-1a: First UL channel + Second UL channel
First channel (e.g., PUCCH, PRACH) is to at least notify event occurrence;
Second channel (e.g., PUSCH) is to carry a beam report
Candidate-1b: First UL channel + SRS
First channel (e.g., PUCCH) is to at least notify event occurrence;
SRS can be used for NW DL-Tx/UL-Rx beam determination.
Candidate-2a: First UL channel at least notifying event occurrence
First UL channel can be PUCCH, PUSCH, or PRACH.
Candidate-2b: SRS used for NW DL-Tx/UL-Rx beam determination
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.4-a009`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.4 Beam management for downlink and uplink

```text
For network-initiated beam reporting in 6GR,
Study the following time-domain behavior of beam reporting: aperiodic, semi-persistent, periodic.
Support DL RS identifier as another report quantity in a beam report, when applicable.
Note: DL RS may be measured or predicted by the UE.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.4-a010`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.4 Beam management for downlink and uplink

```text
Regarding DL beam measurement and report procedure, for the study on NW determination of refined analog beam(s), including the feasibility and necessity, the following is considered:
Potential use cases:
To improve beam-forming gain/throughput via generating NW refined analog beam(s) based on UE report which may be different from measured beams
Studying the details of:
Benchmark: Companies report the benchmark in evaluation.
Benchmark #1 Beam selection from a set of measured beams
Benchmark #2 Beam selection from a set of measured beams plus candidate analog beams (for subsequent transmission)
RS measurement requirements
Potential report content (based on the measured beams):
Applicable frequency range
Others are not precluded.
Note: NW implementation information is not disclosed.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.4-a011`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.3.4 Beam management for downlink and uplink

```text
Regarding NW initiated beam indication, study transmission configuration indicator (TCI) framework involving both joint and separate DL/UL TCI state(s) for both single-TRP/cell/carrier and multi-TRP/cell/carrier operations
Regarding joint-DL/UL TCI state(s), study joint-DL/UL TCI state(s) at least apply to PDSCH, and PUSCH;
FFS: what other target channel(s)/RS(s) which shall/can follow the TCI state, including CSI-RS, SRS, PDCCH, PUCCH and PRACH
Regarding separate DL/UL TCI state, study the following
DL-TCI state(s) at least apply to PDSCH;
FFS: The target channel(s)/RS(s) which shall/can follow the DL-TCI state, including CSI-RS, and/or PDCCH
UL-TCI state(s) at least apply to PUSCH;
FFS: The target channel(s)/RS(s) which shall/can follow the UL-TCI state, including SRS, and PRACH, and/or PUCCH
FFS: At least for joint-DL/UL TCI state/DL-TCI state, one state comprises at least one source QCL-RS, and each source QCL-RS is associated with at least one QCL property.
The joint-DL/UL TCI state can also used for determining UL TX beam
FFS: Other transmission parameter(s) for DL and UL associated with the TCI state (e.g., power control parameters, TAG, etc), besides for QCL properties.
FFS: At least for UL-TCI state, one state comprises at least one reference signal, if applicable, for determining UL TX beam.
FFS: Other transmission parameter(s) for UL associated with the TCI state (e.g., power control parameters, TAG, etc), besides for UL TX beam.
Note: TCI state is for the purpose of discussion
R1-2606908 	Moderator summary #5 on beam management for DL and UL	Moderator (ZTE)
R1-2606933	Moderator summary #6 on beam management for DL and UL	Moderator (ZTE)
Final post-meeting summary for this agenda item.
R1-2605220	Discussion on beam management for downlink and uplink for 6GR air interface	FUTUREWEI
R1-2605241	Beam management for downlink and uplink	Kyocera Corporation
R1-2605263	Discussion on beam management for downlink and uplink for 6GR	Spreadtrum, UNISOC
R1-2605297	Beam management for downlink and uplink	Huawei, HiSilicon
R1-2605323	DL and UL beam management	MediaTek Inc.
R1-2605337	Discussion on beam management for downlink and uplink	ZTE Corporation, Beijing Digital Nebula, Sanechips
R1-2605373	Beam management for downlink and uplink in 6GR	InterDigital, Inc.
R1-2605391	On beam management for downlink and uplink in 6GR	Nokia
R1-2605471	Discussion on beam management for 6GR downlink and uplink	vivo
R1-2605528	Collection on pending topics for 6GR beam management for DL and UL	Moderators (ZTE, Apple)
R1-2605572	Discussion on beam management for downlink and uplink	Xiaomi
R1-2605591	Discussion on beam management for 6GR downlink and uplink	BeammWave AB
R1-2605594	Discussion on beam management for downlink and uplink	TCL
R1-2605600	Discussion on Beam Management for Uplink and Downlink	Tejas Network Limited
R1-2605640	Discussion on beam management for downlink and uplink transmission	CMCC
R1-2605679	Views on Beam Management	Ofinno
R1-2605699	Discussion on beam management for downlink and uplink in 6GR	Lenovo
R1-2605730	Views on beam management for 6GR	CATT
R1-2605840	Discussion on beam management for downlink and uplink in 6GR	Samsung
R1-2605878	Beam management for downlink and uplink	NEC
R1-2605916	Discussions on 6GR multi-beam operation	OPPO
R1-2605942	Discussion on beam management for downlink and uplink	Ericsson
R1-2605979	Discussion on beam management for downlink and uplink	Sony
R1-2606031	On beam management aspects for downlink and uplink	Apple
R1-2606087	Discussion on beam management for downlink and uplink	China Telecom
R1-2606108	Discussion on beam management for downlink and uplink	1Finity
R1-2606120	Discussion on beam management for downlink and uplink	LG Electronics
R1-2606127	Beam Management for Downlink and Uplink	Google
R1-2606247	Discussion on beam management for 6GR	ETRI
R1-2606384	Beam Management for Downlink and Uplink	Qualcomm Incorporated
R1-2606434	Aspects of 6GR Beam Management Framework	AT&T
R1-2606472	Beam management for downlink and uplink	Sharp
R1-2606510	Discussion on Beam management for downlink and uplink	NTT DOCOMO, INC., NTT, Inc.
R1-2606569	Discussion on Beam Management Procedures for 6GR	Panasonic
R1-2606585	Discussion on Digital Twin Generated Training Data for AI/ML-based Beam Management in 6GR			Shanghai Jiao Tong University
R1-2606592	Discussion on beam management for downlink and uplink	NICT
R1-2606634	On beam management for downlink and uplink in 6GR 	Fraunhofer IIS, Fraunhofer HHI
R1-2606650	Views on Beam management for Downlink and Uplink	CEWiT
R1-2606695	Discussion on Selected Beam Management Aspects for 6GR Downlink and Uplink	Rakuten Symphony
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.3.4-a012`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.4 Downlink control channel, scheduling and HARQ operation

```text
Dynamically scheduled retransmission via DCI is regarded as a baseline for both CG PUSCH and SPS PDSCH in 6GR.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.4-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.4 Downlink control channel, scheduling and HARQ operation

```text
Study whether/how to support dynamic adjustment of parameters for both CG PUSCH and SPS PDSCH operations.
FFS the details, including what needs to be changed from NR mechanisms and why
R1-2606528	FL summary #2 for 10.5.4.2 DL/UL transmission without dynamic scheduling	1Finity
R1-2606529	FL summary #3 for 10.5.4.2 DL/UL transmission without dynamic scheduling	1Finity
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.4-a002`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.4 Downlink control channel, scheduling and HARQ operation

```text
For a given CG PUSCH configuration which is not immediately activated in 6GR, the configuration is dynamically (re)activated/deactivated. Study how to support dynamic (re)activation/deactivation for the CG configuration.
For a given CG PUSCH configuration which is immediately activated in 6GR,
Study whether/how to support dynamic deactivation for the CG configuration.
Study whether/how to support dynamic (re)activation for the CG configuration.
If dynamic (re)activation/deactivation is not supported for this case, the CG configuration can be released/deactivated only by RRC signaling.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.4-a003`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.4 Downlink control channel, scheduling and HARQ operation

```text
For a given SPS PDSCH configuration in 6GR,
The SPS PDSCH configuration can be activated/deactivated by DCI.
Note: the SPS PDSCH configuration can be released by RRC.
FFS activation by RRC
R1-2606733	FL summary #4 for 10.5.4.2 DL/UL transmission without dynamic scheduling	1Finity
R1-2606734	FL summary #5 for 10.5.4.2 DL/UL transmission without dynamic scheduling	1Finity
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.4-a004`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.4.1 Downlink control channel, scheduling for downlink and uplink transmission

```text
For Option 1 of the physical channels/signals for the two stages in two-stage DCI study,
Same or different CORESET for the 1st stage and 2nd stage of a two-stage DCI can be considered
[Same or] different SSS for the 1st stage and 2nd stage of a two-stage DCI can be considered, if SSS is supported for the 2nd stage
FFS if SSS is not supported for the 2nd stage
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.4.1-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.4.1 Downlink control channel, scheduling for downlink and uplink transmission

```text
For Option 2 of the physical channels/signals for the two stages in two-stage DCI study
Option 2-1: The 2nd-stage uses PDCCH with modifications
Same or different CORESET for the 1st stage and 2nd stage of a two-stage DCI can be considered
[Same or] different SSS for the 1st stage and 2nd stage of a two-stage DCI can be considered, if SSS is supported for the 2nd stage
FFS if SSS is not supported for the 2nd stage
Study at least the following modifications beyond what supported for 1st stage:
Additional aggregation level(s) and/or flexible position (with the granularity of CCE) of the 2nd stage
Resource determination without hash function
Higher order modulation for the 2nd stage
Option 2-2: The 2nd stage uses a PDSCH transmission scheme with at least the following exceptions/restrictions
Polar code is used
QPSK is used, FFS higher order modulation
Single-layer transmission is the baseline
FFS restriction on TDRA
FFS others
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.4.1-a002`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.4.1 Downlink control channel, scheduling for downlink and uplink transmission

```text
Study multiple PXSCH transmissions for a single carrier using a single DCI and whether to support at least the followings by considering related scenarios/benefits,
Case 1: multiple slots, each slot contains at most one PXSCH
Note: for above study, followings are assumed
each PXSCH carries different TB
single DCI schedules multiple PDSCH
single DCI schedules multiple PUSCH
single DCI is single stage or two stage
R1-2606048	FL summary #3 for downlink control and DL/UL scheduling	Moderator (CMCC, Apple)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.4.1-a003`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.4.1 Downlink control channel, scheduling for downlink and uplink transmission

```text
RAN1 to study at least Cell-specific, Group-specific DCI and UE-specific DCI for 6GR, with the following functions:
UE-specific DCI, including:
One scheduling on DL/UL transmission by using fallback DCI  (e.g., single-layer transmission),
Applicability for RRC connected state, and FFS applicability for other RRC states.
One scheduling on DL/UL transmission by using non-fallback DCI (e.g., multi-layer transmission), where the DCI content depends on UE-specific RRC configuration;
Non-scheduling/pure control information indication
Note: a scheduling DCI can contain non-scheduling/control information
Cell-specific DCI and random access procedure DCI, including:
Scheduling on common signals/channels, e.g.,
Scheduling of system information;
Scheduling of paging messages;
Scheduling on random access procedure (e.g., scheduling of Msg2/Msg4 in DL, scheduling of Msg3 retransmission· in UL);
Non-scheduling/pure control information indication
Group-specific DCI, including:
Group-common information or group of UEs’ information indication.
For the fallback and non-fallback DCI design, the following principles apply:
Fallback DCIs are defined for CSS
Fallback DCI does not depend on UE-specific RRC configuration;
FFS: details of CSS
Note: applicable for UE-specific RRC reconfigurations
FFS whether fallback DCIs for USS considering use cases.
Non-fallback DCI can be dependent on RRC-configurable
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.4.1-a004`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.4.1 Downlink control channel, scheduling for downlink and uplink transmission

```text
Study at least the following mechanisms for DCI Container size determination (at least for RRC connected state), with the details as below:
For Alt 1:
the container size(s) is implicitly derived from the RRC configuration,
E.g., the size for a given DCI container is the maximum possible size based on RRC configurations for the applicable functionalities.
For Alt 2:
the container size(s) are explicitly signalled by the network via RRC
For Alt 3’:
DCI container size(s) is not dependent on UE-specific RRC configuration
This is e.g., cell-specific DCI and random access procedure DCI in common search space. Details FFS.
FFS: Padding/reservation
FFS: need for truncation
FFS: need for size determination during bandwidth adaptation.
Regarding UE’s DCI monitoring size budget, for a single carrier operation,
FFS: the maximum number of container sizes for a UE to monitor (e.g., for BD purpose) is Xmax.
FFS: Whether the maximum number of container sizes for a UE to monitor (e.g., for BD purpose) for UE’s RNTI (e.g., C-RNTI) is Ymax.
FFS: whether the limitation is per slot or across slots
FFS: for multi-carrier cases
FFS minimum container size.
FFS maximum container size.
FFS maximum number of container sizes for two stage DCI
Note: Using a combination of the above alternatives for different use cases is not precluded
R1-2606049	FL summary #4 for downlink control and DL/UL scheduling	Moderator (CMCC, Apple)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.4.1-a005`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.4.1 Downlink control channel, scheduling for downlink and uplink transmission

```text
For the evaluation of two-stage DCI vs single-stage DCI, consider at least the following DCI container sizes (not including CRC) as starting point:
Single-stage DCI: 40-bit, 60-bit, 140-bit
Two-stage DCI
For Option A,
1st-stage: 20-bit if it uses PDCCH
2nd-stage: same as single-stage DCI
For Option A,
1st-stage: 40-bit if it uses PDCCH
2nd-stage: same as single-stage DCI
For Option B,
1st-stage: 40-bit if it uses PDCCH
2nd-stage: (single-stage DCI size minus 20-bit)
24-bit CRC is the default.
Other values of DCI container size are not precluded.
Companies are encouraged to report used/modified assumptions, other assumptions and corresponding justifications
R1-2606925	FL summary #4 for downlink control and DL/UL scheduling	Moderator (CMCC, Apple)
Final post-meeting summary for this agenda item.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.4.1-a006`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.4.3 HARQ related Aspects

```text
For the study of downlink HARQ-ACK feedback granularity smaller than TB-level and the corresponding mechanism, candidate options in RAN1#125 are categorized as follow.
Category A (HARQ-ACK schemes):
NR CBG HARQ-ACK feedback as comparison baseline
XOR-based retransmission feedback
CB/CBG-level HARQ-ACK feedback of high-probability error patterns / codebook-based compressed feedback
2D lattice-based CBs feedback
Category B (feedback mechanisms/procedures may be applicable on top of a Category A scheme):
Non-uniform CB-to-CBG mapping feedback
Two-stage feedback
Mixture of TB-level and CBG-level feedback
Per-PDSCH on-demand request of CBG-level feedback
Enabling/disabling of CBG-level HARQ-ACK feedback
HARQ-ACK feedback enabling/disabling for some of CBGs
At least a common set of evaluation assumptions are to be determined in this meeting for Category A.
FFS same/additional evaluation assumptions are to be applied for Category B.
R1-2606798	FL summary #2 for AI 10.5.4.3: 6GR HARQ related aspects	Moderator (OPPO)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.4.3-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.4.3 HARQ related Aspects

```text
In 6GR, study whether/how to address the case where the UE’s HARQ soft buffer is insufficient (e.g., all HARQ processes across all carriers/cells requiring retransmissions for soft combining simultaneously with maximum TBS), considering the possibility of the case and the different ways to address the case
R1-2606799	FL summary #3 for AI 10.5.4.3: 6GR HARQ related aspects	Moderator (OPPO)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.4.3-a002`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.4.3 HARQ related Aspects

```text
For study of 6G HARQ-ACK codebook based on NR Type-1 codebook as starting point, consider at least the following
Whether / how to reduce the codebook payload size
Whether / how to reduce codebook construction complexity
For study of 6G HARQ-ACK codebook based on NR Type-2 codebook as starting point, consider at least the following
Whether/how to achieve additional robustness against the DCI(s) missing including last DCI(s) missing
Whether the counting / accumulating indication is confined within a cell or a set of cells
For study of 6G HARQ-ACK codebook based on NR (e)Type 3 codebook as starting point, consider at least the following
Whether/how to achieve additional robustness against missing the DCI triggering the feedback
Whether / how to reduce codebook payload size
FFS for each codebook type:
HARQ-ACK bit ordering
Determination of HARQ-ACK codebook payload size
For relaxing the need for tight coordination between schedulers, determine which codebook type(s) should be considered
Scheduling complexity
How to carry HARQ-ACK bits for a DCI that does not schedule a PDSCH, for at least (e)type 3 codebook
Whether/how to support standalone operation
FFS: other approaches
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.4.3-a003`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.4.3 HARQ related Aspects

```text
For the study of downlink HARQ-ACK feedback granularity smaller than TB-level, the following common set of simulation assumptions are to be used for evaluating Category A HARQ-ACK schemes:
| # | Parameter | Assumptions |
| --- | --- | --- |
| 1 | Evaluation methodology | LLS / SLS(optional) with link adaptation |
| 2 | Carrier frequency | 4 GHz Optional: 7GHz |
| 3 | Channel bandwidth | 100MHz, SNR points reported by company Optional: 400MHz, SNR points reported by company |
| 4 | Subcarrier spacing | 30kHz |
| 5 | Channel model | TDL-A 30ns, CDL-C 100ns Optional: TDL-C 100ns, CDL-A 30ns, CDL-B 30ns |
| 6 | UE speed / Doppler | 3km/h Optional: 30km/h, 80km/h |
| 7 | MIMO configuration | 4Rx UE; Rank: company to report (fixed to 1, 2, 4 or adaptive rank) |
| 8 | Receiver functions | Realistic channel estimation Precoding and receiver type to be reported |
| 9 | Link adaptation | OLLA enabled Target BLER 10% Optional: Other target BLER value |
| 10 | NR CBG HARQ-ACK feedback as comparison baseline | NR range 2/4/6/8 Optional: 16 for 400MHz, and other value(s) |
| 11 | Metrics | (Average) feedback overhead per TB Ratio of retransmitted CB(s)/CBG(s) size to original TB size Impact on DL control overhead Optional: Spectrum efficiency / UE throughput / UE power consumption |
Note: Companies are encouraged to report any other assumptions/metric (e.g., traffic model, cell throughput) used in their SLS
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.4.3-a004`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.4.3 HARQ related Aspects

```text
For Method 1 (dynamic indication of HARQ-ACK feedback timing and resource in DCI), study the timing scheme of the HARQ-ACK feedback timing indication, including at least:
Alt 1: counting/offset in physical slots
Alt 2: counting/offset in available slots
FFS: how the available slots are defined/applied
Study also the HARQ-ACK feedback timing indication value range/set (e.g., number of candidate values) under each alternative.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.4.3-a005`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.4.3 HARQ related Aspects

```text
In 6GR, to address the issues mentioned in RAN2 LS if needed, study DCI indication for a given UL HARQ process status based on the following approaches:
Approach 1: DCI scheduling PUSCH indicating the status of the previously transmitted TB(s) associated with the same HARQ ID within same HARQ entity
Approach 2: A DCI other than DCI scheduling PUSCH indicating UL HARQ process status for one or multiple HARQ processes
Approach 3: DCI scheduling PUSCH indicating the status of TB(s) in the last transmitted PUSCH associated with the same HARQ ID within same HARQ entity
R1-2606800	FL summary #4 for AI 10.5.4.3: 6GR HARQ related aspects	Moderator (OPPO)
Final post-meeting summary for this agenda item.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.4.3-a006`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.4.4 Handling of potential multiple uplink transmissions

```text
For 6GR, for the discussion in the collision-handling in 10.5.4.4 agenda item, operation with single PHY priority (as opposite to having two PHY-level priorities) is prioritized for future discussions in Rel-20 6G study.
FFS: whether two PHY priorities should be considered.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.4.4-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.4.4 Handling of potential multiple uplink transmissions

```text
For handling of potential multiple UL transmissions in 6GR, study collision-handling procedures at least for simplification and reduction of UE/aNB complexity with considering performance impacts, e.g., including
Simplify the resource determination/mapping
Reduce the complexity on the timeline determination
Reduce the dependency between transmissions on different carriers
Simplify/reduce collision-handling cases
R1-2606708	FL summary#3 on handling of potential multiple uplink transmissions	Moderator (MediaTek)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.4.4-a002`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.4.4 Handling of potential multiple uplink transmissions

```text
For collision handling between PUCCH and PUSCH across multiple carriers, study the following mechanisms:
Simultaneous transmission on different carriers
Multiplexing and/or prioritization
FFS: Applicable scenarios
Note: Collision handling among other channels/signals will be discussed separately.
R1-2606709	FL summary#4 on handling of potential multiple uplink transmissions	Moderator (MediaTek)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.4.4-a003`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.5 Other physical layer signals, channels and procedure

```text
Support the following EVM of LLS for evaluating CB PUSCH:
| Parameters | Values |
| --- | --- |
| Carrier frequency | 4 GHz |
| SCS | 30 kHz |
| Waveform | CP-OFDM DFT-s-OFDM |
| System BW | 20 MHz |
| RB allocation for PUSCH | 2 RBs and 14 symbols as starting point. Other values can be reported by company |
| MCS for PUSCH | MCS index 0 in Table 5.1.3.1-1 of TS38.214 as baseline Other value can be reported by company |
| PUSCH payload size | 56, 64 or 112 bits Company to report their choice. For 112 bits, company to report the RB allocation for PUSCH. |
| Number of simultaneous UEs in one CB PUSCH transmission. | 1, 2, 3, 4, |
| Channel model | CDL-A or TDL-A in TR 38.901 Company to report the choice. |
| Delay spread | 100 ns |
| Channel correlation between simultaneous UEs | Consider three cases: Randomly selected UEs. e.g, in CDL-A, use random UE AoA. Low channel correlation, High channel correlation, Company to report the details. |
| UE speed | 3 km/h Other values can be reported by the company. |
| UE Tx antenna configuration | 1 Tx antenna |
| BS Rx antenna configuration | 4, 8, 64 Rx antennas BS antenna geometry (M, N, P) is reported by company. |
| Channel estimation | Realistic |
| Receiver | MMSE-IRC |
| DMRS configuration | Rel-15 NR Type 1 DMRS Configuration to be reported by company, including total number of ports. |
| Distribution of SNR of different UEs | Option 1: equal SNR Option 2: Unequal SNR, The SNR is uniformly distributed in [x - Y, x + Y] (dB) where x is the per UE average SNR in dB. Values of Y can be reported by companies. Company to report the details |
| Performance metric | BLER of PUSCH reception SINR loss @1% BLER and @10% BLER with respect to single-UE transmission Optional: BLER error floor y% starting from x dB if any, company to report the definition of error floor False alarm rate and miss detection rate of DMRS port, or sequence (company to report the number of DMRS ports and number of sequences used in blind detection, detection method) Other metric can be reported by company. |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.5-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.5 Other physical layer signals, channels and procedure

```text
For the study of multi-bit SR for requesting UL resources in 6G:
Focus the study and evaluation on the following candidate reporting content:
Quantized buffer size.
Note: this candidate is for evaluation purpose only.
Study and determine whether/how the reported information in multi-bit SR can assist the BS to better schedule uplink resource for the UE
Study and determine for multi-bit SR:
Applicable and non-applicable scenarios for multi-bit SR, including cell load (low/high) and target packet size (small/large).
Whether and how to accommodate dynamic/flexible range of payload size of UL data.
Excess granted resource caused by buffer size quantization.
Study and evaluate the required/maximal bit size and study the quantization method.
With the same aggregated UL resource overhead of multi-bit SR and 1-bit SR+ scheduled PUSCH for BSR, evaluate UL transmission scheduling latency performance of multi-SR vs the mechanism of 1-bit SR + BSR (the waiting time for next SR transmission occasion is included).
Evaluate the link coverage of multi-bit SR transmission in PUCCH with 1-bit SR coverage as baseline.
Compare the multi-bit SR carrying quantized buffer size with the solution of using multiple 1-bit SR configurations to indicate the same target quantized buffer size, considering the resource overhead and UL transmission scheduling latency.
Other candidate reporting contents can also be evaluated
E.g., delay status report, LCH/LCG ID, predicted traffic timing information.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.5-a002`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.5 Other physical layer signals, channels and procedure

```text
For remote interference management for 6GR:
At least support wireless-based RIM framework specified in 5G/NR as starting point for 6GR.
Further study whether to support backhaul-based RIM framework.
Support the following two types of RIM-RS:
RIM-RS Type 1: transmitted by victim BS to indicate the existence of remote interference
RIM-RS Type 2: transmitted by aggressor BS to detect if remote interference still exists.
The RIM RS shall carry the following information:
BS group ID
‘Enough/Not enough’ indication in RIM-RS Type 1
‘Near/Far’ indication in RIM RS type 1.
FFS: the RIM RS can carry 6G specific information.
FFS: the RIM RS to carry duplex specific information, e.g., TDD frame structure, SBFD  subband/symbol configuration.
FFS the time-domain and frequency domain design of RIM RS, the sequence in RIM RS, and the configuration methods of RIM RS, time location of RIM RS.
FFS whether CSI-RS can be reused as RIM RS.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.5-a003`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.5 Other physical layer signals, channels and procedure

```text
For BS-to-BS CLI handling in 6GR, recommend to support information exchange between BSs and study the following candidate information exchange content:
The slot configuration in TDD and time/frequency configuration of SBFD.
The configuration of BS-to-BS CLI measurement RS: CSI-RS and/or 6GR SSB.
The BS-to-BS CLI measurement results.
DL Tx beam(s) information.
Recommended and non-recommended beam.
BS-to-BS CLI mitigation request.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.5-a004`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.5 Other physical layer signals, channels and procedure

```text
Study UE-initiated UE-to-UE CLI (UEI CLI) reporting with considering the following details:
The definition of CLI event is: when at least one RSRP/RSSI measurement larger than a configured threshold for a given time length, the CLI event is triggered.
FFS: other CLI-related event(s).
Study and determine the measurement metric for CLI event detection:
Option 1: non-filtered L1-RSRP/L1-RSSI
Option 2: filtered L1-RSRP/L1-RSSI.
Study the CLI event detection procedure, report procedure and report contents.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.5-a005`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.5 Other physical layer signals, channels and procedure

```text
For UE-to-UE CLI measurement in 6GR, the followings are recommended:
Support RSRP and RSSI as the measurement metrics
Wideband RSSI measurement is supported.
FFS on subband RSSI measurement.
Support to use SRS for RSRP measurement
Support to use CLI RSSI measurement resource for RSSI measurement
For SBFD, UE measures the UE-to-UE CLI in UL subband
FFS: For SBFD, whether the UE can measure CLI in UL subband in the time duration of DL reception.
FFS: whether the UE measures the UE-to-UE CLI in DL subband in SBFD.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.5-a006`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.5 Other physical layer signals, channels and procedure

```text
For UE-to-UE CLI reporting in 6GR, study L1 network-controlled CLI reporting with considering the followings:
Study The latency requirement for CLI reporting to determine the necessity of L1 network-controlled CLI reporting.
Consider periodic, semi-persistent and aperiodic reporting.
Study the applicable scenarios for each reporting mechanism.
Consider the following two reporting content options:
Option 1: N strongest RSRP or RSSI and corresponding resource indicators. The UE reports RSRP/RSSI for the strongest one and differential RSRP/RSSI for the other N-1.
Option 2: a bit-map reporting with each bit corresponding each measurement resource, and bit value = 1 indicating the RSRP/RSSI measurement is above a configured threshold.
Study the benefit of each reporting content.
Further study the following additional reporting content:
UE reports the time information corresponding to the measurement resource with the largest RSRP/RSSI measurement.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.5-a007`

### [6G/Rel-20 RAN1#126] `agreement` 10.5.5 Other physical layer signals, channels and procedure

```text
Study non-transparent PUSCH resource muting mechanism for handling BS-to-BS CLI in 6GR and at least consider the following aspects:
The muting mechanism specified in NR rel-19 is the starting point for study.
Pattern(s) of resource muting.
Including study whether/how to support flexible muting patterns for resource efficiency.
Whether/how to support dynamic/flexible adjustment of symbol position of muting resource.
Whether/how to support dynamic disable/enable muting.
Whether/how the TBS determination should consider the muting pattern in one PUSCH transmission.
Whether/how same symbol power can be maintained between muting and non-muting
Impact of multiplexed UCI in PUSCH
Performance comparison between non-transparent and transparent PUSCH resource muting mechanism.
R1-2606468	FL Summary #1 for 10.5.5	Moderator (OPPO)
R1-2606469	FL Summary #2 for 10.5.5	Moderator (OPPO)
R1-2606470	FL Summary #3 for 10.5.5	Moderator (OPPO)
R1-2605268	Discussion on other physical layer signals, channels and procedure	Spreadtrum, UNISOC
R1-2605303	Other physical layer signals and procedures	Huawei, HiSilicon
R1-2605331	On other physical layer signals, channels, and procedures in 6GR 	MediaTek Inc.
R1-2605341	Other physical layer signals, channels and procedure	Ericsson
R1-2606779	Other physical layer signals, channels and procedure	Ericsson
(Revision of R1-2605341)
R1-2605354	SR design for 6GR	Kyocera Corporation
R1-2605359	Other physical layer signals, channels and procedures	InterDigital, Inc.
R1-2605396	On other physical layer signals, channels and procedures in 6GR	Nokia
R1-2605418	Discussion on 6G other physical layer signals, channels and procedure	ZTE Corporation, Sanechips
R1-2605476	Discussion on other physical layer signals, channels and procedure for 6GR	vivo
R1-2605501	Discussion on Other Physical Layer Signals, Channels and Procedure	Tejas Networks Limited
R1-2605577	Further considerations on 6GR UE reporting mechanism for requesting uplink resource	Xiaomi
R1-2605645	Discussion on interference measurements, report and management	CMCC
R1-2605680	Views on Other physical layer signals, channels and procedure	Ofinno
R1-2605735	Discussion on other physical layer signals, channels and procedure for 6GR	CATT
R1-2605845	Discussion on other physical layer signals, channels and procedure	Samsung
R1-2605886	Discussion on Other physical layer signals, channels and procedure	NEC
R1-2605933	Discussion on other physical layer signals, channels and procedure	OPPO
R1-2605964	Discussion on Other Physical Layer Signals and Procedures	Google
R1-2605983	Considerations on CB PUSCH for BSR	Sony
R1-2606035	On other physical layer signals, channels and procedure	Apple
R1-2606071	Discussion on Other physical layer signals, channels and procedure	TCL
R1-2606164	Discussion on UE reporting mechanism for requesting uplink resource in 6GR	LG Electronics
R1-2606252	Discussion on other physical-layer signals and procedure	ETRI
R1-2606317	Discussion on multi-bit SR and contention-based PUSCH	Fainity Innovation
R1-2606389	Other physical layer signals, channels and procedure	Qualcomm Incorporated
R1-2606436	On Other Physical Layer Aspects of the 6GR Framework	AT&T
R1-2606473	Discussions on other physical layer signals, channels and procedure	Sharp
R1-2606515	Discussion on Other physical layer signals, channels and procedure	NTT DOCOMO, INC.
R1-2606556	Discussion on other physical layer signals, channels and procedure	Quectel
R1-2606579	Discussion on other physical layer signals, channels and procedure	WILUS Inc.
R1-2606597	Discussion on other physical layer signals, channels, and procedures in 6GR	CSCN
R1-2606701	RF interference detection, classification, and mitigation for 6G Radio (6GR)	MITRE-FFRDC, National Spectrum Consortium, DISA, Lockheed Martin, VIAVI Solutions, AST SpaceMobile
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.5-a008`

### [6G/Rel-20 RAN1#126] `conclusion` 10.5.5 Other physical layer signals, channels and procedure

```text
Company to report the LLS results as the format in the following table:
| BS Rx configurations | Payload size and corresponding PUSCH RB allocation. | Waveform, Channel model and channel correlation assumptions | Configuration of DMRS port and DMRS sequence | Distribution of SNR of different UEs | DMRS ports/scramble IDs among simultaneous UEs. e.g., UEs use different DMRS ports, UEs use same DMRS ports but different scramble IDs. | Evaluation results Note: company to report, for BLER results, whether blind detection on DMRS port and sequence is used or not. |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  | SNR loss @10% BLER for 2,3,4 UEs w.r.t single UE transmission | SNR loss @1% for 2,3,4 UEs w.r.t single UE transmission | Optional: BLER error floors for 2,3,4 UEs: yes or no, and if yes, starting SNR and level of BLER error floor. | Miss detection and false alarm rate of DMRS port or sequence. |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.5.5-c001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.0 General aspects and frameworks

```text
For the RAN1 study of “Re-use of existing 5G mid-band (~3.5GHz) site grid for 6G deployments in at least around 7 GHz and targeting comparable coverage to 5G mid-band”, if link budget template candidates 1 is used to calculate the metric(s), the coverage gap between ~7GHz and 5G mid-band is calculated as follows
Coverage gap = MPL1 – MPL2 – PL_diff [– additional margin]
[FFS: detailed value of additional margin]
Note:
MPL1: MPL of the evaluated signal/channel in ~7GHz
MPL2: MPL of the bottleneck channel in 5G mid-band (e.g., Rel-15 NR Msg3 for initial/random access procedure)
PL_diff = 20*log10(f1 / f2), where f1 and f2 are the carrier frequency for ~7GHz and 5G mid-band, respectively
R1-2603224	FL summary #3 of General aspects and frameworks	Moderator (Huawei, Xiaomi)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.0-a001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.0 General aspects and frameworks

```text
RAN1 to discuss beamforming gain for DL broadcast channel and UL channel and to align the interpretation of the following parameters in link budget template candidate 1
(4b) Antenna gain correction factor at antenna gain component 3 & antenna gain component 4 of transmitter (dB)
(5b) Antenna gain correction factor at antenna gain component 2 of transmitter (dB)
(11b) Antenna gain correction factor at antenna gain component 3 & antenna gain component 4 of receiver (dB)
(11bis-b) Antenna gain correction factor at antenna gain component 2 of receiver (dB)
(15) Receiver interference density
(27) Penetration margin (dB): Whether account for the indoor distance in the pathloss calculation in O2I scenarios
(25) Shadow fading margin (function of the cell area reliability and lognormal shadow fading std deviation) (dB): Function definition and whether handoff gain is accounted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.0-a002`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.0 General aspects and frameworks

```text
For the RAN1 study of “Re-use of existing 5G mid-band (~3.5GHz) site grid for 6G deployments in at least around 7 GHz and targeting comparable coverage to 5G mid-band”, companies are encouraged to at least provide the link budget results for the following signals/channels during initial access in around 7GHz:
DL:NR PSS/SSS, SSB, Common PDCCH, SIB1 PDSCH, Msg2/4 PDSCH
UL:NR PRACH format C2/B4/0, MSG3 PUSCH, MSG5 PUSCH (companies to report assumption of the payload of actual transmission),  MSG4 PUCCH Format 1
The simulation assumptions in section A.1 in TR38.830 are used as a starting point.
The payload for NR SIB1 PDSCH is 1200 bits.
FFS: other parameters
R1-2603225	FL summary #4 of General aspects and frameworks	Moderator (Huawei, Xiaomi)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.0-a003`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.0 General aspects and frameworks

```text
For the 6GR smallest maximum UE bandwidth for at least one lower-tier device, RAN1 agrees the following observations for the alternatives agreed in RAN1#124:
According to NR Rel-18 eRedCap study for a device supporting a single FDD band with spectrum allocation no smaller than 20MHz, when comparing on the basis of same PHY peak rate (~10 Mbps), the additional UE modem complexity reduction of Alt 2 compared with Alt 1 is ~10%, and the additional UE modem complexity reduction of Alt 3 compared with Alt 1 is ~5%.
HD-FDD 1-Rx UE modem complexity reduction estimates from the eRedCap SI
| Closest RAN1#124 alternative for smallest maximum 6G UE bandwidth | Modem complexity reduction option in eRedCap SI TR 38.865 | Modem complexity reduction relative to eRedCap Option PR1 (Alt 1) |
| --- | --- | --- |
| Alt 1 | Option PR1 | 0% |
| Alt 2 | Option BW1 | 10% |
| Alt 3 with 5 MHz BB for all channels | Option BW2 | 7% |
| Alt 3 with 5 MHz BB for PxSCH only | Option BW3 | 4% |
FD-FDD 1-Rx UE modem complexity reduction estimates from the eRedCap SI
| Closest RAN1#124 alternative for smallest maximum 6G UE bandwidth | Modem complexity reduction option in eRedCap SI TR 38.865 | Modem complexity reduction relative to eRedCap Option PR1 (Alt 1) |
| --- | --- | --- |
| Alt 1 | Option PR1 | 0% |
| Alt 2 | Option BW1 | 8% |
| Alt 3 with 5 MHz BB for all channels | Option BW2 | 5% |
| Alt 3 with 5 MHz BB for PxSCH only | Option BW3 | 4% |
Placeholder for companies to provide more UE complexity analysis based on inputs to RAN1#125, e.g., multi-band devices.
R1-2603457	FL summary #5 of General aspects and frameworks	Moderators (Huawei, Xiaomi)
From Friday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.0-a004`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.0 General aspects and frameworks

```text
From frequency domain resource mapping perspective, study TB/CB/CBG mapping within a PDSCH with frequency domain resource allocation between 200MHz and 400MHz considering the following options:
Option A: A TB can span up to 400MHz
Option B: A TB can span up to 200MHz
FFS details
Note: For both options, whether multiple TBs are time domain multiplexed within a PDSCH due to other restrictions will be separately discussed in agenda item 10.5.2.2.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.0-a005`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.0 General aspects and frameworks

```text
For the study of link direction determination for dynamic TDD, consider the following options:
Option 1:
TDD pattern is based on DL, UL and flexible symbols
TDD pattern is semi-statically configured
No dynamic slot format indication as in NR
For dynamically scheduled single transmission/reception in flexible symbols, UE link direction is determined only based on scheduling DCI
Study transmissions/receptions without associated DCI in flexible symbols (if configured)
Option 2:
Semi-statically configured TDD pattern is based on DL, UL and flexible symbols
Dynamically indicated TDD pattern is based on DL, UL and guard symbols
Dynamically indicated TDD pattern indicates DL, UL or guard symbols for flexible symbols according to semi-statically configured TDD pattern
The TDD pattern should be provided to the UE with sufficient processing time to apply the TDD pattern change
UE link direction is determined based on TDD pattern
Option 3:
TDD pattern, based on DL, UL and guard symbols (i.e. no flexible symbols)
UE is dynamically indicated with a TDD pattern out of predefined/preconfigured TDD pattern
The TDD pattern should be provided to the UE with sufficient processing time to apply the TDD pattern change
Other options are not precluded
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.0-a006`

### [6G/Rel-20 RAN1#124b] `conclusion` 10.5.0 General aspects and frameworks

```text
For the RAN1 study of “Re-use of existing 5G mid-band (~3.5GHz) site grid for 6G deployments in at least around 7 GHz and targeting comparable coverage to 5G mid-band”, to align the usage of the correction factors of BS antenna gain of common beams in co-site deployment evaluation, the following are observed as the common understanding
the total antenna gain of common beam is assumed to be unchanged/comparable if the beamwidth of SSB beams is unchanged, regardless of whether the number of BS antenna elements or BS TxRUs increases or not.
The total BS antenna gain above refers to the sum value of entry (4)+(5)+(11bis) in the link budget table.
The total antenna gain of BS UL common beam is expected not to be smaller than that of BS DL common beam if the beamwidth of SSB beams is unchanged.
Note:
(4) Total antenna gain at antenna gain component 3 & antenna gain component 4 of transmitter = (4a) – (4b) (dB)
(5) Total antenna gain at antenna gain component 2 of transmitter = (5a) - (5b) (dB) Note: zero for uplink
(11bis) Total antenna gain at antenna gain component 2 of receiver = (11bis-a) - (11bis-b) (dB) Note: zero for downlink
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.0-c001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.1.1 Synchronization acquisition and beam measurement

```text
For discussion purpose, the following terminologies are defined
6GR SSB burst: one 6GR SSB or multiple 6GR SSBs each with a different index compose a 6GR SSB burst
6GR SSB burst set: one or multiple 6GR SSB burst(s) compose a 6GR SSB burst set
Note: Whether and how to use the ’6GR SSB burst set’ is up to companies to report.
6GR SSB periodicity: The time interval at which an SSB within a given SSB burst repeats in time
Note: “index” is only for illustration purpose to identify a 6GR SSB within a 6GR SSB burst, whether and how to specify the terminologies will be further discussed.
Note: all below examples are only used for improving understanding about above terminologies
Example 1: 4 SSBs within a SSB burst (no repetition), 1 SSB burst within 1 SSB burst set
Example 2: 4 SSBs within a SSB burst (4 consecutive repetitions), 1 SSB burst within 1 SSB burst set
Example 3-1: 16 SSBs within a SSB burst (4 consecutive repetitions), 1 SSB burst within 1 SSB burst set
Example 3-2: 16 SSBs within a SSB burst (4 consecutive repetitions), 4 SSB bursts within 1 SSB burst set
Example 4-1: 16 SSBs within a SSB burst (4 interleaved repetitions), 1 SSB burst within 1 SSB burst set
Example 4-2: 4 SSBs within a SSB burst (4 interleaved repetitions), 4 SSB bursts within 1 SSB burst set
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.1.1-a001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.1.2 PRACH and RACH procedure

```text
Adopt the following definition for miss detection probability and false alarm probability for RAN1 study (not intended for 6GR requirements)
Note: Definition of evaluation metrics are for the purpose of alignment of definition among companies. Companies are encouraged to provide information on evaluation metrics reported and the implication and importance of the evaluation metric in the contributions with evaluations.
Miss detection probability
Total probability of following events (for a preamble transmission):
Not detecting the preamble for a RO that was sent among the target preambles of the detecting BS
Correct preamble detection but with the wrong timing estimation
For correct preamble detection, the (residual) timing estimation error should be less than CP/2 of data symbol, e.g., SCS = 30kHz, CP/2 = 1.2 us
False alarm probability
Probability of detecting any target preamble for a RO when no transmission has occurred (only noise)
Adopt the following definition for metrics for evaluations for RAN1 study (not intended for 6GR requirements)
Note: Not all metrics may be applicable for all evaluation scenarios, and it is up to companies to provide appropriate metric(s) for information. The definitions are for the purpose of alignment of definition among companies. Companies are encouraged to provide information on evaluation metrics reported and the implication and importance of the evaluation metric in the contributions with evaluations.
Miss detection probability considering frequency estimation
Total probability of following events (for a preamble transmission):
Not detecting the preamble for a RO that was sent among the target preambles of the detecting BS
Correct preamble detection but with the wrong timing estimation and/or frequency estimation
For correct preamble detection,
the (residual) timing estimation error should be less than CP/2 of data symbol, e.g., SCS = 30kHz, CP/2 = 1.2 us, and
the (residual) frequency estimation error of PRACH detection should be less than some target value. Target value to be reported by company.
Type 1 false detection probability (intra-cell)
Probability of detecting different preamble(s) for a RO than the one that was sent among the target preambles of the detecting BS.
Type 1 false detection rate (intra-cell)
A = number of preamble(s) for a RO detected other than the one that was sent among the target preambles of the detecting BS
B = Sum of A for all ROs that contain preamble transmission
C = Total number of preamble transmission across all ROs
Type 1 false detection rate = B divided by C
Type 2 false detection probability (inter-cell)
Probability of detecting any target preamble for a RO when no transmission has occurred in the cell of detecting BS and transmission has occurred in another cell
Mixed false detection probability
Probability of detecting multiple preambles (two or more) of which one of the detected preamble is correctly detected (multiple preamble detection for the detecting BS) for a RO when only one preamble among the target preambles of the detection BS was sent.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.1.2-a001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.1.2 PRACH and RACH procedure

```text
Study base sequences and preamble sequence generation/construction methods for 6GR PRACH taking into account one or more of the following aspects:
detection performance (possibly including TA estimation performance, handling of frequency offset, miss-detection, false alarm, false detection, auto-correlation/cross correlation properties, etc)
detection complexity for BS
implementation complexity for UE
Cubic metric/PAPR
supported sequence lengths & associated SCS of a sequence
[Preambles per random access occasion (RO) ]
Inter-cell interference
Coexistence with 5G NR PRACH sequences
Note 1: Benchmark various performance metric(s) and considerations against 5G NR PRACH design as baseline
Note 2: base sequences for 5G NR PRACH are ZC sequence, and preamble sequence generation is done via (time domain) cyclic shift of a ZC root sequence (base sequence) to create a specific preamble sequence.
Note 3: companies are encouraged to provide the following information:
detailed information for the sequence generation and construction of a preamble for PRACH
correlation properties (compared to NR PRACH sequences, including correlation with NR PRACH sequences)
Cubic metric/PAPR (at least compared to NR PRACH sequences)
Applicable scenarios
R1-2603325	Summary #4 of discussion on Random Access and RA Procedures	Moderator (InterDigital, Inc.)
Presented in Thursday session.
R1-2603390	Summary #5 of discussion on Random Access and RA Procedures	Moderator (InterDigital, Inc.)
From Friday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.1.2-a002`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.1.2 PRACH and RACH procedure

```text
Replace the working assumption and agree on evaluation parameters for random access as follows:
Link Level Assumption Parameters for Random Access
| Assumptions | Value |
| --- | --- |
| Carrier frequency | Refer to AI 10.1 |
| Duplex | Select among the following candidates: FDD, TDD |
| Carrier frequency & Duplex | 0.7 GHz, FDD 2 GHz, FDD 4 GHz, TDD 7 GHz, TDD 15 GHz, TDD 30 GHz, TDD |
| System Bandwidth | 3MHz, 5 MHz, 10 MHz, 100 MHz |
| (Shared channel) Numerology | 700 MHz carrier frequency: 15 kHz 2 GHz carrier frequency: 15 kHz [3.5/4]4 GHz carrier frequency: 30 kHz 7 GHz carrier frequency: [30] kHz [14/15]15 GHz carrier frequency: FFS[30] kHz 30 GHz carrier frequency: 120 kHz |
| Antenna Configuration at the TRP | Select among the following candidates: For TDL: - 1T1R, 2T2R, 4T4R, FFS: 16T16R, 64T64R For CDL: (M,N,P,Mg,Ng; Mp, Np) - FFS: For TDL: - 2T2R, 2T4R - (optional) 1T1R, 1T2R, 4T4R For CDL: (M,N,P,Mg,Ng; Mp, Np) - 700 MHz: (8, 4, 2, 1, 1; 1, 4), (dH, dV) = (0.5, 0.5)λ (Outdoor Combination 2) - 2 GHz: (12, 8, 2, 1, 1; 4, 8), (dH, dV) = (0.5, 0.5)λ (Outdoor Combination 2) - For 4 GHz: (M, N, P, Mg, Ng, Mp, Np) = (8, 2, 2, 1, 1; 1, 2), (dH, dV) = (0.5, 0.8) - 7 GHz: (24, 16, 2, 1, 1; 4, 16), (dH, dV) = (0.5, 0.8)λ (Outdoor Combination 1) - 15 GHz: (32, 32, 2, 1, 1; 4, 16), (dH, dV) = (0.5, 0.5)λ (Outdoor Combination 2) - 30 GHz: (16, 8, 2, 4, 2; 1, 1), (dH, dV) = (0.5, 0.5)λ (Outdoor Combination 1) Antenna radiation pattern: based on SLS EVM (from Agenda 10.1) |
| Antenna Configuration at the UE | For TDL: 1T2R, 2T2R, 2T4R For CDL: - FFS: 0.7, 2, [3.5/4], 7 GHz - handheld UT model with 1T2R, 2T2R, 2T4R - FFS: - 700MHz, 2 GHz, 4 GHz: Combination 2 - handheld UT model (from Clause 7.3.2 of TR38.901) with 1T2R - 700 MHz, 2 GHz, 4 GHz, 7 GHz, 15 GHz: combination 3 - handheld UT model (from Clause 7.3.2 of TR38.901) with 2T2R, 2T4R - 30 GHz: Config 1 of 30GHz UT Antenna configuration for SLS EVM (from Agenda 10.1) Antenna radiation pattern: based on SLS EVM (from Agenda 10.1) |
| Channel estimation | Realistic |
| Channel Model | Select among following DS candidates: 10, 30, 100, 300, 1000 ns FFS: other DS values |
| Mobility | Select among the following candidates: 3 km/h, 30km/h, 120 km/h, 500km/h, 1000 km/h |
| RF Impairment modeling | Phase noise (if modeled): Follow the models in R1-165685 Frequency offset (if modeled): - TRP: uniform distribution +/- 0.05 ppm - UE: uniform distribution +/- 0.1 ppm For FR2, modeling of phase noise is recommended. For small SCS PRACH preambles (e.g. 1.25kHz or 5kHz) modeling of frequency offset is recommended. |
Additional Link Level Assumption Parameters for PRACH Evaluations
| Carrier Frequency | 700 MHz | 2 GHz | [3.5/4]4 GHz | 7 GHz | [14/15]15 GHz | 30 GHz |
| --- | --- | --- | --- | --- | --- | --- |
| Channel Model (baseline, other model usage not precluded) | FFS: TDL-A - DS = 30 ns TDL-C - DS = 100 ns, 300 ns, (optional) 1000 ns FFS: other models | FFS TDL-C - DS = 100 ns, 300 ns, (optional) 1000 ns | TDL-A - DS = 30 ns TDL-C - DS = 100 ns, 300 ns, (optional) 1000 ns FFS: CDL-C - DS = 100, 300 ns (see Note 1) FFS: other models | TDL-C - DS = 100, 300 ns FFS: CDL-C - DS = 100, 300ns (see Note 1) FFS: other models | FFS TDL-C - DS = 100 ns CDL-C - DS = 100 ns (see Note 1) | FFS CDL-C DS = 30 ns (see Note 1) |
| UE speed | 3, 120 km/h, 500 km/h (optional) 30, 1000km/h | FFS 3 km/h (optional) other values | 3 km/h (optional) other values |  |  |  |
| RF Impairments modeling | TRP: uniform distribution +/- 0.05 ppm UE: uniform distribution +/- 0.1 ppm |  |  |  |  |  |
| Initial timing Offset | Timing uncertainty derived from cell radius Companies to report time modelling details (e.g., min, max, distribution, etc.) |  |  |  |  |  |
| RO assumption | Number of preambles per RO –32, 64, 128,512 Other values: up to companies to report Number of UEs per RO – 1, 2, 4, 8 |  |  |  |  |  |
| PRACH Sequence & Format | Companies to provide detailed information on sequence used (e.g., sequence type, length, CP/GP lengths, SCS, cyclic shift values, repetition, etc). |  |  |  |  |  |
| Target Performance | 0.1% False Alarm 1% miss-detection |  |  |  |  |  |
| NOTE 1: The CDL table is translated so that the strongest cluster’s AoD and AoA occur at a random angle for both the antenna panels of TRP and UE in the local coordinate systems. ZoD and ZoA is assumed to be unchanged. The value of the random angle is selected to be uniformly distributed from +30 to -30 degree. The random value is chosen independently for both AoD and AoA. CDL angle scaling is based on Clause 7.7.5.1 of TR38.901 v19.1.0. |  |  |  |  |  |  |
Link Level Parameters for PUSCH of Msg.3 or Msg.5 for FR1
| Parameter | Value |
| --- | --- |
| Frequency hopping | w/ or w/o frequency hopping For w/ frequency hopping: inter-slot hopping with repetition |
| Number of UE transmit chains | 1, 2 |
| Number of DMRS symbol | w/o frequency hopping: 3, w/ frequency hopping: 2 for each hop |
| Waveform | Company to report |
| HARQ configuration | For eMBB, whether HARQ is adopted is reported by companies. For VoIP, w/ HARQ. The maximum number of HARQ transmission (limited by frame structure and latency requirements) can be reported by companies. |
| PUSCH Msg 3 Repetitions | FFS w/ or w/o repetition - For w/ repetition, repetition number: 1, 2, 4, 8 w/ or w/o DMRS bundling w/ or w/o OCC |
| PUSCH duration | 14 OS [28] OS |
| Number of PRBs | [2, 3, 4] |
| TBS | [56] bits companies to report other values FFS: values |
| Other parameters | Reported by companies. |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.1.2-a003`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.1.2 PRACH and RACH procedure

```text
Adopt the following parameters for MsgA of 2-step RACH.
Additional Parameters for MsgA of 2-step RACH
| Parameters | Values |
| --- | --- |
| MsgA PRACH format | Company to report |
| Waveform (data part) | Company to report (among agreed waveform from agenda 10.2) |
| The number of PUSCH symbols & PUSCH mapping type | 14, Type A; [6], Type B as optional |
| 1) Total Number of PRBs for MsgA PUSCH Or 2) number of PRBs per PUSCH occasion Note: either of them should be aligned for scheme comparison | [6, 12] Or [1,2,3] |
| PUSCH DMRS overhead | [2 or 3] DMRS symbols |
| Frequency hopping for MsgA PUSCH | w/ or w/o frequency hopping |
| TBS | [72] bits as starting point, other values are not precluded |
| Number of UEs | 1 as a starting point; 2 or more for evaluation of shared PUSCH occasion |
| Timing offset | Uniform [0, RTT] |
| HARQ transmission | Disabled |
| Receiver | MMSE-IRC as baseline |
| Channel estimation | Realistic for both channel estimation and TO/FO estimation. Ideal can be considered for calibration, if needed. |
| Target BLER | [10%, 1%] for 1st transmission of MsgA as starting points. |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.1.2-a004`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.1.2 PRACH and RACH procedure

```text
Study and Identify at least the following set of deployment scenario characteristics for 6GR RACH preamble format design:
target round trip time (RTT)/maximum cell radius
target time duration of preamble
target doppler/UE mobility
target duplex scheme, PRACH SCS, and frequency ranges
Study and identify required preamble formats that correspond to the identified use cases.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.1.2-a005`

### [6G/Rel-20 RAN1#124b] `observation` 10.5.1.2 PRACH and RACH procedure

```text
Simplification of preamble formats compared to NR PRACH preamble formats is generally desired.
Final summary in R1-2603391.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.1.2-o001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.1.3 Bandwidth operation

```text
Study for idle mode,
Whether and how to define a common resource block grid in single-carrier operation.
R1-2602843	FL Summary 3 on 6GR Bandwidth Operation	Moderator (MediaTek Inc.)
Presented in Thursday session:
R1-2603455	FL Summary 4 on 6GR Bandwidth Operation	Moderator (MediaTek Inc.)
From Friday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.1.3-a001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.1.3 Bandwidth operation

```text
For discussions on frequency location and bandwidth for UEs during initial access and idle mode, "frequency location" is defined as the starting position of the bandwidth.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.1.3-a002`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.1 Downlink transmission scheme(s) for downlink control channels

```text
6GR Control Resource Set (CORESET) to be defined for 6GR PDCCH
CORESET defines at least duration in time and frequency resources used for PDCCH
6GR Search Space (SS) set to be defined for 6GR PDCCH.
A 6GR search space set defines at least a set of PDCCH candidates for a UE to monitor
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.1-a001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.1 Downlink transmission scheme(s) for downlink control channels

```text
REG consists of multiple REs.
REG occupies one OFDM symbol in the time domain.
FFS for the REG allocation in frequency domain.
CCE consists of a set of REGs.
FFS how to map a set of REGs to the CCE including the number of REGs per CCE.
FFS REG indexing
PDCCH candidate corresponds to one or multiple CCE(s).
The exact number of CCEs used for a single PDCCH candidate equals the Aggregation Level (AL) at least for PDCCH without repetition.
Below Working Assumption from RAN1#124 is not necessarily to be confirmed.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.1-a002`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.1 Downlink transmission scheme(s) for downlink control channels

```text
Study both non-interleaved and interleaved CCE-to-REG mapping for 6GR PDCCH.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.1-a003`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.1 Downlink transmission scheme(s) for downlink control channels

```text
At least QPSK modulation is used for 6GR PDCCH.
FFS necessity and feasibility of additional modulation(s) other than QPSK to be used for 6GR PDCCH.
R1-2603246	Feature Lead summary #3 on PDCCH Transmission Schemes	Moderator (Nokia)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.1-a004`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.1 Downlink transmission scheme(s) for downlink control channels

```text
Study CCE aggregation mechanism for 6GR PDCCH
Consider ALs 1, 2, 4, 8, 16 as baseline
Study the necessity, feasibility, and use-cases for supporting of higher and other ALs, e.g., 32.
It is necessary to consider at least the number of REGs within one CCE, and the number of REs within one REG.
Study the necessity and use-cases of PDCCH repetition for 6GR PDCCH, considering at least the following:
Intra-slot repetitions
Inter-slot repetitions
Study the duration of CORESET in OFDM symbols
Consider 1, 2, 3 symbols as baseline
Study the necessity, feasibility and use-cases for supporting the CORESET durations longer than 3.
Study the trade-offs/relation among PDCCH repetition, CORESET duration, and the usage of Aggregation Levels.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.1-a005`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.1 Downlink transmission scheme(s) for downlink control channels

```text
Study details of frequency-domain resource allocation for both contiguous and non-contiguous frequency-domain resource allocation for 6GR CORESET.
R1-2603247	Feature Lead summary #4 on PDCCH Transmission Schemes	Moderator (Nokia)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.1-a006`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.1 Downlink transmission scheme(s) for downlink control channels

```text
Study CRC scrambling, e.g., by an RNTI, for 6GR PDCCH.
Study PDCCH payload bit-level scrambling before modulation for 6GR PDCCH.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.1-a007`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.1 Downlink transmission scheme(s) for downlink control channels

```text
Common Search Space (CSS) set and UE-Specific Search Space (USS) set to be defined for 6GR PDCCH.
A SS set is associated with at least one CORESET
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.1-a008`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.1 Downlink transmission scheme(s) for downlink control channels

```text
Study the necessity, feasibility, and ways of dynamic sharing and/or semi-static assignment of time-frequency resources of 5G and 6G PDCCH transmission for MRSS, ensuring 6GR performance
The above is considered from the NW perspective in a way transparent to the UE.
R1-2603248	Feature Lead summary #5 on PDCCH Transmission Schemes	Moderator (Nokia)
From Friday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.1-a009`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.1 Downlink transmission scheme(s) for downlink control channels

```text
Hash function to be defined for 6GR PDCCH.
Hash function can be used to determine the CCE index of a 6GR PDCCH candidate associated with a SS set.
FFS hash function design for 6GR PDCCH.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.1-a010`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.1 Downlink transmission scheme(s) for downlink control channels

```text
For 6GR PDCCH DMRS, study at least
How to define DMRS resource mapping.
How to define DMRS sequence generation and initialization.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.1-a011`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.1 Downlink transmission scheme(s) for downlink control channels

```text
Support at least slot-level PDCCH monitoring with minimum periodicity of 1 slot for 6GR.
The details of the slot-level PDCCH monitoring are FFS
Study whether and how to support PDCCH monitoring other than slot-level
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.1-a012`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.1 Downlink transmission scheme(s) for downlink control channels

```text
For the study of 6GR PDCCH transmit diversity consider at least the following:
Single-port DMRS-based PDCCH transmission as a baseline
The necessity and feasibility of the UE non-transparent transmission scheme compared to the transparent
Precoder granularity, e.g., REG bundle.
For information
R1-2603464	Collection of Simulation parameters for PDCCH	Moderator (Nokia)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.1-a013`

### [6G/Rel-20 RAN1#124b] `conclusion` 10.5.2.1 Downlink transmission scheme(s) for downlink control channels

```text
NR and 6GR CORESETs are RAT-specific and configured independently.
A 6GR UE operating in 6G network is only configured with 6GR CORESET(s).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.1-c001`

### [6G/Rel-20 RAN1#124b] `working_assumption` 10.5.2.1 Downlink transmission scheme(s) for downlink control channels

```text
REG consists of multiple REs.
CCE consists of a set of REGs.
PDCCH candidate corresponds to one or multiple CCE(s).
REG bundle consists of a set of REGs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.1-w001`

### [6G/Rel-20 RAN1#124b] `working_assumption` 10.5.2.1 Downlink transmission scheme(s) for downlink control channels

```text
REG bundle consists of a set of REGs.
R1-2603245	Feature Lead summary #2on PDCCH Transmission Schemes	Moderator (Nokia)
From Tuesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.1-w002`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
For FDRA for PDSCH on a single physical carrier:
Support both bitmap-based (“Type 0”) and RIV-based (“Type 1”) mapping
Support dynamic switching between bitmap-based mapping and RIV-based mapping
Further study, at least, the following aspects:
Granularity for bitmap-based and RIV-based mapping, considering support for wider bandwidth (more than 275 PRBs)
Whether there are restrictions for 400 MHz CBW in case of two RF chains at the UE
Note: Decision to study scheduling across multiple physical carriers is subject to agreements in other agenda items
R1-2603212	FL Summary #4 on DL Transmission Scheme for DL Shared Channel	Moderator (Ericsson), Moderator (Google)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.2-a001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
Support PT-RS for PDSCH at least for FR2
Study whether PT-RS is necessary for FR1 and around 7GHz
If PT-RS for FR1/around 7GHz is supported, strive to have a unified design for all bands
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.2-a002`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
The phase noise model defined in TR38.803 is used for further evaluation unless further update from RAN4
Send an LS to RAN4 to check if RAN4 has plan to update it and when it will be updated
R1-2603413	Draft LS on Phase Noise Model for 6GR study	Google
Thursday decision: Draft LS R1-2603413 is endorsed in principle. Final LS is approved in R1-2603453.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.2-a003`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
Study the DMRS assumption for MU-MIMO considering at least the following aspects
Network indication or UE assumption of DMRS CDM group/ports/density/pattern/symbol(s) for co-scheduled UE(s)
Network indication of number of CDM groups without data as in NR
Network indication to assist the UE’s OCC despreading
Network indication or UE assumption of the DMRS sequence for the co-scheduled UE(s)
Network indication or UE assumption of the modulation order(s) for the co-scheduled UE(s)
Network indication or UE assumption of the QCL/TCI information for the co-scheduled UE(s)
Network indication or UE assumption of PRG allocation for the co-scheduled UE(s)
R1-2603213	FL Summary #5 on DL Transmission Scheme for DL Shared Channel	Moderator (Ericsson), Moderator (Google)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.2-a004`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
For CPE configuration, details follow corresponding agreements in Agenda 10.1 and 10.5.2.3.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.2-a005`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
For traffic model for SLS EVM, support:
NFB FTP model 1/3 with,
500 kB packet size
20%, 50%, and 70% resource utilization
FTP 3-extension 1 model can be optionally considered
10 or 30 UEs per cell for applicable models
FB model can be optionally considered, for technical performance requirements (TPR)
Other traffic models and packet sizes are not precluded (companies to report)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.2-a006`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
Study PDSCH and RS for PDSCH based on the following additional SLS EVM assumptions for HST scenario
Note: Other parameters follow agreements on SLS EVM for non-HST scenario
Note: LLS EVM parameters for HST scenario are separately discussed
| Parameter | Value |
| --- | --- |
| Carrier frequency and duplex | Around 4 GHz, TDD Around 7 GHz, TDD Around 30 GHz, TDD |
| Channel model | TR 38.901 with spatial consistency (optional) |
| Scenario and deployment at around 4 and 7 GHz | Rural macro, 500 m or 1732 m ISD between RRH sites, two TRxPs per RRH site, one or more RRH sites connected to a BBU, with RRH site to railway track distance: 100 m Inter-track distance: 6 m Train length: 400 m Train width: 3.38 m |
| Scenario and deployment at around 30 GHz | Rural macro, 500, 1732 m between BBU sites, one or more RRH sites connected to 1 BBU, one TRxP per RRH site, with RRH site to railway track distance: 5 m Inter-RRH site distance: [580 m, 580 m, 572 m] Inter-track distance: 6 m Train length: 400 m Train width: 3.38 m |
| UE speed | Rural macro: outdoor (350km/h, 500km/h) |
| Number of UEs per cell and UE distribution | 300 (assuming 1000 passengers per train and at least 30% activity ratio) 100% of users in train Companies to report how UEs at distributed in train |
| Resource utilization | 50%, 70%, 90% |
| Multi-TRP scenario | Maximum number of coordinated TRPs is 2, 4, 8 or 16 Other number of coordinated TRPs are not precluded |
| CSI-RS periodicity | 10 ms (optional) 20 ms (baseline) 40 ms (optional) 80 ms (optional) |
| BS transmit power (for 20 MHz) | For around 0.7—7 GHz 49 dBm For around 30 GHz 33 dBm Note: BS Tx power scales up with bandwidth proportionally under the limitation of the maximum BS Tx power is 56 dBm Other BS transmit powers are not precluded (companies to report) |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.2-a007`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
For TDRA for PDSCH:
Support a single mapping type, at least for PDSCH within a single slot
Support flexible starting symbol
Study which symbol(s) can be the starting symbol
Study number of symbols
Granularity is 1 symbol
Further study DMRS position(s)
Study time offset from the scheduling PDCCH, considering UE processing capabilities
Study whether/how to support a single PDSCH transmission crossing slot boundary
Including the maximum PDSCH duration
Including whether the single PDSCH transmission can occupy contiguous or non-contiguous symbols
Including impact on performance and complexity
Including maximum TB size limit
Note: If cross-slot boundary PDSCH transmission is supported, a single mapping type is supported also for cross-slot PDSCH transmission
Study whether/how to support PDSCH repetition
Note: Whether/how to schedule multiple PDSCH transmissions using a single DCI is up to DCI content discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.2-a008`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
For channel parameter estimation for LLS EVM:
Practical channel parameter estimation (baseline)
Companies to report channel parameter estimation, e.g., delay spread, Doppler spread, delay, SNR, etc. (optional)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.2-a009`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
Study the sequence of DMRS for PDSCH considering at least the following aspects
PAPR
Inter-sequence interference
Scrambling ID indication
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.2-a010`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
For low overhead DMRS with AI/ML receiver for PDSCH reception, link level simulation is used for further study
The performance comparison is based on the following metrics
Eventual KPI: BLER/SE/throughput
Complexity KPI: FLOPs, the number of parameters
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.2-a011`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
For evaluation of DMRS for PDSCH, the following aspects are considered for further study:
Candidates for FD-OCC length: 2, 3, 4, 6, 8, 12, 16, 24, x
Candidates for TD-OCC length: 1 (i.e., single-symbol DMRS), 2, 4, x
Candidate for number of CDM groups: 2, 3, 4, 6, 8, 12, x
CDM group structure, e.g., comb-based, block-based, etc.
R1-2603458	FL Summary #6 on DL Transmission Scheme for DL Shared Channel	Moderators (Ericsson, Google)
From Friday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.2-a012`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
For SLS EVM for non-HST scenario:
Revise the RAN1#124 agreement as follows:
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.2-a013`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
Study PDSCH and RS for PDSCH based on the following SLS EVM assumptions
Note: Additional EVM assumptions for AI/ML based DMRS overhead reduction can be further discussed.
Note: EVM assumption for HST scenarios will be treated separately
| Parameter | Value |
| --- | --- |
| Carrier frequency and duplex | Around 0.7 GHz, FDD Around 2 GHz, FDD Around 4 GHz, TDD Around 7 GHz, TDD Around 30 GHz, TDD |
| Subcarrier spacing | 15 kHz for FDD 30 kHz for TDD and around 2—7 GHz 120 kHz for TDD and around 30 GHz |
| Waveform | CP-OFDM |
| Channel model | TR 38.901 (Rel-19) |
| Scenario | Suburban macro, 1732 m ISD (for around 0.7—4 GHz) Urban macro, 500 m ISD (for around 0.7—30 GHz) Dense urban, 200 m ISD (for around 4—30 GHz) Other scenarios are not precluded (companies to report) |
| Bandwidth | 20 MHz (baseline) 100 MHz (for 4—7 GHz) (optional) Other bandwidths are not precluded (companies to report) |
| Deployment | 7 x 3, single layer, hex grid (baseline) 19 x 3, single layer, hex grid (optional) |
| BS transmit power (for 20 MHz) | For around 0.7—7 GHz 49 dBm for Suburban macro, 1732 m 46 dBm for Urban macro, 500 m 44 dBm for Dense urban, 200 m Note: BS Tx power scales up with bandwidth proportionally under the limitation of the maximum BS Tx power is 56 dBm for outdoor and 33 dBm for indoor for the above carrier frequencies. For around 30 GHz 33 dBm for all scenarios Other BS transmit powers are not precluded (companies to report) |
| BS transmit power constraint | Total transmit power constraint (baseline) Per-TXRU transmit power constraint (optional) |
| BS antenna configuration | Around 0.7 GHz: 4 TXRUs, 32AEs, (M, N, P, Mg, Ng; Mp, Np) = (8, 2, 2, 1, 1; 1, 2), (dH, dV) = (0.5, 0.5), (“Baseline Configuration”) Around 2 GHz: 4 TXRUs, 32 AEs, (M, N, P, Mg, Ng; Mp, Np) = (8, 2, 2, 1, 1; 1, 2), (dH, dV) = (0.5, 0.5), (“Outdoor Combination 1”) 32 TXRUs, 128 AEs, (M, N, P, Mg, Ng; Mp, Np) = (8, 8, 2, 1, 1; 2, 8), (dH, dV) = (0.5, 0.5) 64 TXRUs, 192 AEs, (M, N, P, Mg, Ng; Mp, Np) = (12, 8, 2, 1, 1; 4, 8), (dH, dV) = (0.5, 0.5), (“Outdoor Combination 2”) Around 4 GHz: 4 TXRUs, 32 AEs, (M, N, P, Mg, Ng, Mp, Np) = (8, 2, 2, 1, 1; 1, 2), (dH, dV) = (0.5, 0.8), (“Outdoor Combination 0”) 32 TXRUs, 128 AEs, (M, N, P, Mg, Ng, Mp, Np) = (8, 8, 2, 1 ,1; 2, 8), (dH, dV) = (0.5, 0.8) , (“Indoor Combination 1”) 64 TXRUs, 192AEs, (M, N, P, Mg, Ng; Mp, Np) = (12, 8, 2, 1, 1, 4, 8). (dH, dV) = (0.5, 0.8), (“Outdoor Combination 1”) Around 7 GHz: Details follow corresponding agreements in Agenda 10.1 Around 30 GHz 4 TXRUs, 1024 AEs, (M, N, P, Mg, Ng, Mp, Np) = (16, 16, 2, 2, 1; 1, 1), (dH, dV) = (0.5, 0.5) , (“Outdoor Combination 3”) 16 TXRUs, 2048 AEs, (M, N, P, Mg, Ng, Mp, Np) = (16, 8, 2, 4, 2; 1, 1), (dH, dV) = (0.5, 0.5) , (“Outdoor Combination 1”) Other antenna configurations are not precluded (companies to report) |
| BS mechanical/electrical tilt | Mechanical tilt: 90° in GCS Electrical tilt: Company to report Other mechanical tilts are not precluded (companies to report) |
| UE antenna configuration (IoT) | Details follow corresponding agreements in Agenda 10.1 |
| UE antenna configuration (handheld) | Details follow corresponding agreements in Agenda 10.1 |
| CPE configuration | Details follow corresponding agreements in Agenda 10.1/10.5.2.3 |
| UE speed (handheld) | Urban macro and dense urban: 80% indoor in buildings (3 km/h), 20% outdoor in cars (30km/h) Suburban macro: 80% indoor in buildings (3 km/h), 20% outdoor in cars (40km/h) |
| Traffic model | NFB FTP model 1/3 with 500 kB packet size 20%, 50%, and 70% resource utilization FTP 3-extension 1 model can be optionally considered 10 or 30 UEs per cell for applicable models FB model can be optionally considered, for technical performance requirements (TPR) Other traffic models and packet sizes are not precluded (companies to report) |
| Scheduler | PF |
| MIMO scheme | Reported by companies |
| Receiver | MMSE-IRC (baseline) R-ML (Reported by companies) |
| DMRS channel estimation | Realistic |
| CSI-RS channel estimation | Realistic |
| Inter-cell interference estimation | Realistic |
| Inter-cell interference model | Explicit |
| CSI-RS periodicity | 10 ms (optional) 20 ms (baseline) |
| CSI delay | 4 ms |
| Phase errors for radios with uncalibrated antennas (for 4 TXRUs) | Wideband phase error between Tx antenna port 0 and Tx antenna port () can be modeled as follows: Independent random phase offset uniformly distributed between 0 and 2π between any two Tx antenna ports. |
| Backhaul assumption | Ideal backhaul (baseline) Non-ideal backhaul (optional) |
| Performance metric | Throughput Other performance metrics are not precluded (companies to report) |
| Multi-TRP (e.g., CJT) scenario | For evaluation of multi-TRP under single layer deployment, consider multi-TRP Scenario 1, 2, and 3, with Same antenna configuration and Tx power is assumed across TRPs. Note: other multi-TRP scenarios are not precluded Note: TRP assumption for HST scenarios will be treated separately |
| Multi-TRP Scenario 1: Intra-cell scenario, with 4 TRPs/RRHs per multi-TRP set | Multi-TRP Scenario 2: Intra-site, inter-cell, with 3 TRPs per cooperative set (as baseline) | Multi-TRP Scenario 3: Inter/intra-site, inter-cell with TRPs per cooperative set |
| --- | --- | --- |
|  |  | Companies report the setting when N>1 |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.2-a014`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
For LLS EVM for non-HST scenario:
Revise the RAN1#124 agreement as follows:
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.2-a015`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
Study PDSCH and RS for PDSCH based on the following LLS EVM assumptions
Note: Additional EVM assumptions for AI/ML based DMRS overhead reduction can be further discussed.
| Parameter | Value |
| --- | --- |
| Carrier frequency and duplex | Around 0.7 GHz, FDD Around 2 GHz, FDD Around 4 GHz, TDD Around 7 GHz, TDD Around 30 GHz, TDD |
| Subcarrier spacing | 15 kHz for 0.7 and 2 GHz 30 kHz for 4 GHz and 7 GHz 120 kHz for 30 GHz |
| Waveform | CP-OFDM |
| Channel model | CDL-A/C/D in TR 38.901 |
| System bandwidth | 20 MHz 100 MHz Other bandwidths are not precluded (companies to report) |
| PRG size | 2 RBs, 4 RBs and wideband as start point for evaluation Other values are not precluded, and reported by companies |
| Delay spread | 30 ns, 100 ns, 300 ns, 1000 ns (optional) |
| UE speed | 3 km/h, 30 km/h, 120 km/h, 350 km/h, 500 km/h |
| BS antenna configuration | Align with SLS |
| UE antenna configuration | Align with SLS |
| Receiver | MMSE-IRC (baseline) R-ML (Reported by companies) Other receivers are not precluded (companies to report) |
| Channel estimation | Realistic |
| Channel parameter estimation | Practical channel parameter estimation (baseline) Companies to report channel parameter estimation, e.g., delay spread, Doppler spread, delay, SNR, etc. (optional) |
| MIMO scheme | Reported by companies |
| MU-MIMO interference model | The assumption of MU-MIMO interference in NR Rel-18 DMRS enhancement can be reused (companies to report which Alt) |
| Link adaptation and HARQ | AMC or fixed MCS |
| Phase errors for radios with uncalibrated antennas (for 4 TXRUs) Note: Only for radios with uncalibrated antennas | Wideband phase error between Tx antenna port 0 and Tx antenna port () can be modeled as follows: Independent random phase offset uniformly distributed between 0 and 2π between any two Tx antenna ports. |
| Performance metric | BLER, SE, Throughput Other performance metrics are not precluded (companies to report) |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.2-a016`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
Study codeword-to-layer mapping for PDSCH:
Consider the following aspects
The number of codewords for each rank
The maximum number of codewords
The maximum rank per codeword
The modulation order per layer(s)
Including identifying and evaluating important aspects affecting performance and complexity that are impacted by codeword-to-layer mapping
NR spatial first, frequency second, time third mapping as baseline for evaluation
NR codeword-to-layer mapping as baseline for evaluation
Further study whether/how to map one or more transport block(s) to time/frequency resources and its impact on codeword-to-layer mapping
Further study aspects related to modulation order and code rate and its impact on codeword-to-layer mapping
Final summary in R1-2603459.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.2-a017`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.3 Uplink transmission scheme(s) for uplink channels

```text
For 6GR PUSCH transmission,
The supported number of UE antenna ports are {1, 2, 3, 4, 8}
FFS: Other number of UE antenna ports
The maximum number of SU-MIMO layers is assumed same as the given number of UE antenna ports for CP-OFDM.
Separate discussion on the number of antenna ports of UE device(s).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.3-a001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.3 Uplink transmission scheme(s) for uplink channels

```text
For frequency domain resource allocation for a PUSCH,
Support physically contiguous allocation in a single physical carrier.
Study frequency domain resource allocation granularity/unit(s).
FFS physically non-contiguous allocation in a single physical carrier.
Note: Scheduling across multiple physical carriers is subject to agreements in other agenda items.
Note: Frequency hopping, interleaving, UL muting, potential impact of SBFD are separately discussed.
R1-2602189	FL Summary #2 on Uplink transmission scheme(s) for uplink channels	Moderator (NTT DOCOMO), Moderator (Samsung)
From Tuesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.3-a002`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.3 Uplink transmission scheme(s) for uplink channels

```text
Support the following table as the assumption of LLS for evaluation of PUSCH and DMRS.
Parameters
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.3-a003`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.3 Uplink transmission scheme(s) for uplink channels

```text
For time domain resource allocation for a PUSCH within a slot, consider at least the following aspects:
Support flexible starting symbol
Study which symbol(s) can be the starting symbol.
Study number of symbols
Granularity is 1 symbol.
Study time offset from the scheduling PDCCH, considering UE processing capabilities.
Note: Time domain DMRS position is separately discussed.
R1-2602190	FL Summary #3 on Uplink transmission scheme(s) for uplink channels	Moderator (NTT DOCOMO), Moderator (Samsung)
Presented in Wednesday session.
R1-2602191	FL Summary #4 on Uplink transmission scheme(s) for uplink channels	Moderator (NTT DOCOMO), Moderator (Samsung)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.3-a004`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.3 Uplink transmission scheme(s) for uplink channels

```text
In addition to the agreement on the basic assumption of SLS for evaluation of PUSCH transmission scheme in RAN1#124, for traffic model, support the followings
FTP Model 1/3, 0.5 Mbyte packet size
FTP 3-extension 1 (optional)
Resource Utilization (RU)
20%
50%
70%
Full buffer traffic model (optional, for 6G TPR evaluation)
10 or 30 UEs per cell, other values are not precluded (companies to report)
Other traffic models and packet sizes are not precluded (companies to report)
Note: This is also applicable to assumption of SLS for evaluation of PUSCH DMRS
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.3-a005`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.3 Uplink transmission scheme(s) for uplink channels

```text
In addition to the agreement on the basic assumption of SLS for evaluation of PUSCH transmission scheme in RAN1#124, for SLS assumption for PUSCH DMRS, support the followings
Deployment: other deployment is not precluded, and can be reported by company.
Link adaptation & HARQ retransmission are modelled
Number of HARQ retransmissions is reported by company
Note: this is also applicable to assumption of SLS for evaluation of PUSCH transmission scheme.
DMRS specific assumptions: reuse the assumption of LLS for evaluation of PUSCH and DMRS
Reported by company, if additionally needed
This is also applicable with HST scenario.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.3-a006`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.3 Uplink transmission scheme(s) for uplink channels

```text
For PUSCH transmission scheme and PUSCH DMRS in HST scenario, in addition to the agreement on the basic assumption of SLS for evaluation of PUSCH transmission scheme in RAN1#124, support the followings.
| #1 Frequency range | Around 4 GHz, TDD Around 7 GHz, TDD Around 30 GHz, TDD |
| --- | --- |
| #3 Numerology | 30 kHz for TDD and around 4—7 GHz 120 kHz for TDD and around 30 GHz |
| #4 Scenario | Around 4 GHz or Around 7 GHz: ISD 500 m or 1732 m between RRH sites, two TRxPs per RRH site, one or more RRH sites connected to a BBU. Around 30GHz: 1732 m between BBU sites, 3 RRH sites connected to 1 BBU, one TRxP per RRH site, inter RRH site distance (580 m, 580 m, 572 m) as in Figure 2 below. |
| #4-1 Deployment | Macro-layer only: Around 4 GHz or 7 GHz: Dedicated linear deployment along the railway line as in Figure 1 below. - RRH site to railway track distance: 100 m Figure 1 Around 30 GHz: Dedicated linear deployment along the railway line as in Figure 2. - RRH site to railway track distance: 5 m. Figure 2 |
| #5 Channel model | TR 38.901 with spatial consistency (optional) |
| #13 UE speed | 350km/h, 500km/h |
| UE distributions | - Train length: 400m - 300 (for non-full-buffer) (assuming 1000 passengers per high-speed train and at least 30% activity ratio) - 100% of users in train |
| Multi-TRP scenario | Maximum number of coordinated TRPs is 2, 4, 8 or 16 Other number of coordinated TRPs are not precluded |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.3-a007`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.3 Uplink transmission scheme(s) for uplink channels

```text
Support codebook based PUSCH transmission for 6GR, and study at least the following aspects:
UL precoder is selected from an UL codebook, based on UL CSI acquisition in NW to schedule UE
As baseline, SRS is used for UL CSI acquisition
FFS: Which RS/method can be used to obtain UL CSI, other than SRS
UL codebook design, at least considering
Fixed codebook which is pre-defined in specification
Configurable codebook which can be configured by NW
Hybrid approach of fixed and configurable codebook
performance, resolution, overhead, codebook size comparing to 5G NR
Diverse UE coherency capabilities
Diverse UE Tx antenna structures
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.3-a008`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.3 Uplink transmission scheme(s) for uplink channels

```text
For the assumption of LLS for evaluation of AI based receiver for PUSCH DMRS overhead reduction,
Support to reuse the assumption of LLS for evaluation of PUSCH and DMRS in RAN1#124b.
In addition, in RAN1#125, the following template is used as starting point for collecting related parameter values.
Further discuss on detail of values
| Parameters | Value |
| --- | --- |
| #1 Receiver assumptions |  |
| #2 Model input | (Including model input dimension) |
| #3 Model output | (Including model output dimension) |
| #4 Label | (Labelling error model can be reported optionally) |
| #5 Training type |  |
| #6 Number of MIMO layers |  |
| #7 Number of FLOPs | (Number of FLOPs per RB/slot/layer can be reported optionally) |
| #8 Number of parameters of AI Model |  |
| #9 Benchmark | Receiver: non-AI based receiver with realistic assumption Other aspects (including DMRS patterns, etc) can be reported by company |
| #10 Aspects to consider for generalization and scalability performance |  |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.3-a009`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.3 Uplink transmission scheme(s) for uplink channels

```text
In addition to the agreement on the basic assumption of SLS for evaluation of PUSCH transmission scheme in RAN1#124, for CPE configuration, support the followings
Indoor and outdoor CPE pre-selection criterion or mechanism
Approach 0. Random selection between indoor/outdoor CPE, as baseline
(optional) Approach 1. A pre-selection criterion is applied to ensure that the CPE/FWA devices experience sufficiently good link quality and the fraction of the cell over which service is sufficiently good is reported.
(optional) Approach 2. The approach first assumes CPEs are indoors. Then according to the criteria, a number of worst performing households are either rejected or reassigned as outdoor CPEs. The number of outdoor CPEs is limited to some fraction (20% in the example of Profile 1), and the households with the worst performance that exceed the number of allowed outdoor CPEs are rejected.
In cases where CPEs are 100% indoor or outdoor, prequalification can be used, and a fraction of worst performing households are rejected.
The criteria can be e.g RSRP, minimum UL or DL data rate, etc.
Other approaches are not precluded and can be considered (reported by company if considered)
Note 1: This is only for Profile 1 (mixed deployment of indoor and outdoor CPE).
Note 2: This is also applicable for assumption of SLS for evaluation of PUSCH DMRS
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.3-a010`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.3 Uplink transmission scheme(s) for uplink channels

```text
In addition to the agreement on the basic assumption of SLS for evaluation of PUSCH transmission scheme in RAN1#124, for CPE antenna configuration, support the followings
Details follow corresponding agreements in Agenda 10.1.
Other antenna location/configuration are not precluded and can be considered (reported by company if considered), e.g.,
For Alt 1 in agreement of AI 10.1, Outdoor CPEs use horizontally directive antenna elements.
For Alt 1 and Alt 2 in agreement of AI 10.1, Single panel indoor and outdoor CPEs with horizontally directive antenna elements are oriented to point at the serving base station. Indoor CPEs whose antenna elements are omnidirectional in the horizontal plane are not constrained to be oriented to point at the serving base station.
Note: This is also applicable for assumption of SLS for evaluation of PUSCH DMRS.
Final summary in R1-2603466.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.3-a011`

### [6G/Rel-20 RAN1#124b] `proposal` 10.5.2.3 Uplink transmission scheme(s) for uplink channels

```text
#1 Carrier frequency
Around 0.7 GHz, FDD
Around 2 GHz, FDD
Around 4 GHz, TDD
Around 7 GHz, TDD
Around 30 GHz, TDD
#2 SCS
15 kHz for FDD
30 kHz for TDD and around 2 - 7 GHz
120 kHz for TDD and around 30 GHz
#3 Waveform
CP-OFDM, DFTS-OFDM
#4 System BW
20 MHz
100 MHz
Other bandwidths are not precluded (reported by company)
#4-1 RB allocation
Small: 4, 8 RBs
Medium: 24 RBs
Large: 48 RBs
Other values are not precluded (reported by company)
#5 Channel model
CDL-A/C/D in TR 38.901
TDL-A/C in TR 38.901 (optional)
Other channel models are not precluded (reported by company)
#5-1 MU-MIMO interference model
FFS: How to model MU-MIMO channel (e.g., can emulate low correlation among MU scheduled UEs)
FFS: same RB allocation among MU scheduled UEs
#6 Delay spread
30 ns
100 ns
300 ns
1000 ns (optional)
#7 UE speed
3 km/h, 30 km/h, 120 km/h, 350 km/h, 500 km/h
Additional assumption of 0.3 km/h for FWA
#8 UE antenna configuration
Align with SLS assumption for PUSCH
#8-1 CPE antenna configuration
Align with SLS assumption for PUSCH
#9 BS antenna configuration
Align with SLS assumption for PUSCH
#10 Precoding granularity
Reported by company, wideband precoding is baseline
#11 SRS configuration
Reported by company
#12 Link adaptation
AMC or fixed MCS
#12-1 HARQ
No HARQ as baseline
HARQ retransmission as optional
#13 Channel estimation
Realistic, Ideal (as the upper bound, optional)
Note: This also includes noise and interference estimation
#14 Receiver
Baseline: MMSE-IRC
Other can be reported by company
#15 DMRS specific assumptions
Rel-15 NR Type 1/2, Rel-18 NR eType 1/2 design as baseline used for comparison (reported by companies which type(s) is used)
For 6G PUSCH DMRS design, the following(s) can be reported by company, e.g., DMRS pattern used (including mapping in time and frequency), DMRS overhead, port allocation strategies, DMRS sequence, power boosting / multiplexing with data in FDM manner, etc
#16 MIMO scheme
Reported by company (e.g., SU/MU-MIMO, max rank, fixed rank/rank adaptation, UL codebook)
#17 Performance metric
BLER, throughput, PAPR
MSE (optional)
Net gain (optional, if applicable) which the definition is aligned based agreement in RAN1#122bis 6GR waveform agenda
#18 Impairments
Align with SLS assumption for PUSCH
#19 TB size determination
Reported by company how TB size is determined
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.3-p001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.4 Beam management for downlink and uplink

```text
Support the following table as the assumption of SLS for evaluation of 6GR beam management:
MCC: In below table, only the parts marked as green are assumed stable, the other proposed agreements are not yet finally confirmed.
| Parameter | Value |
| --- | --- |
| #1 Scenario (Carrier frequency) | Indoor hotspot, Urban macro, Dense urban (one-layer, and two-layer), High Speed Train, SMa, Urban grid, 4 GHz, TDD 7 GHz, TDD 30 GHz, TDD Other scenarios are not precluded (companies to report) |
| #2 Mode | DL/UL SU-MIMO/MU-MIMO |
| #3 System BW | 4GHz: 20MHz 7GHz: 100 MHz 30GHz: 100 MHz |
| #4 Subcarrier spacing for data | 4GHz/7GHz: 30KHz; 30GHz: 120 KHz |
| #5 Channel model | TR 38.901 with the following features, if needed: Spatial consistency, including Autocorrelation of shadow fading (Section 7.4.4 in TR 38.901) Correlation modeling for multi‑frequency simulations. Near-field characters Spatial non-stationarity |
| #6 BS Antenna Configuration | Reuse the agreed configuration(s) from 6GR air interface evaluation assumptions For 7GHz, the following can be further considered: 128 TXRUs, 2048AEs, (M, N, P, Mg, Ng; Mp, Np) = (64, 16, 2, 1, 1, 8, 8), (dH, dV) = (0.5, 0.5); For 30GHz, the following can be further considered: (M, N, P, Mg, Ng; Mp, Np) = (8, 16, 2, 1, 1; 1, 1), or (16, 32, 2, 1, 1; 1, 1)), (dH, dV) = (0.5, 0.5); |
| #7 BS array orientation | Mechanical tilt: 180° in GCS for indoor hotspot; 90° in GCS for Urban Macro, Dense Urban and High Speed Train Electrical tilt: Company to report Other mechanical tilts are not precluded (companies to report) |
| #8 TXRU mapping to antenna elements | A single TXRU is mapped per panel per subarray per polarization. Others are not precluded (companies to report). |
| #9 Beam-forming scheme | Companies explain the details, e.g., DFT-based or Eigen-based |
| #10 Procedure of beam sweeping | Companies explain the details |
| #11 Multi-TRP operation | Reuse the assumptions for multi-TRP scenarios of DL-based CSI (A.I. 10.5.3.1) with the following interpretation: The maximum number of coordinated TRP(s) = {1, 2, 3, 4}, and other larger value(s) are not precluded Backhaul: ideal (baseline) or non-ideal; sync: ideal (baseline) or non-ideal; FFS: Other update for high-speed train |
| #12 Criteria for selection for serving TRP(s) | Serving TRP selection with objective of maximizing RSRP is considered as baseline, and other criteria is not precluded and up to companies to report. For TRP switching, it is up to companies to report the TRP selection margin, if any. |
| #13 Criteria for beam selection for serving TRP(s) | Beam selection with objective of maximizing RSRP is considered as baseline, and other criteria is not precluded and up to companies to report. |
| #14 UE Antenna Configuration | 4GHz & 7GHz: Reuse the agreed configuration(s) from 6GR air interface evaluation assumptions; 30GHz: Reuse the agreed configuration(s) from 6GR air interface evaluation assumptions: [Config 0 (one panel) or Config 1 (two panels)]: (M, N, P, Mg, Ng; Mp, Np) = (4, 1, 2, 1, 1; 1, 1) is considered as a baseline |
| #15 UE array orientation | Ω‌UT,a uniformly distributed on [0, 360] deg, Ω‌UT,b = 0 deg, Ω‌UT,g = 0 deg is considered as a baseline. Others are not precluded (companies to report) |
| #16 Beam correspondence | Ideal (baseline) or non-ideal. Others are not precluded. |
| #17 Link adaptation | Based on CSI-RS (Adaptive Modulation and Coding, AMC) |
| #18 UE receiver type | MMSE-IRC as baseline; other advanced receivers are not precluded |
| #19 BS Tx Power | Reuse the configuration(s) from 6GR air interface evaluation assumptions |
| #20 Maximum UE Tx Power | Reuse the configuration(s) from 6GR air interface evaluation assumptions |
| #21 Inter site distance | Reuse the configuration(s) from 6GR air interface evaluation assumptions, besides for the following: High Speed Train: 1732 m ISD |
| #22 UE antenna element radiation pattern | Reuse the configuration(s) from 6GR air interface evaluation assumptions |
| #23 UE Speed and UE distribution | Reuse the configuration(s) from 6GR air interface evaluation assumptions, besides for the following: High Speed Train: 100% outdoor in train (up to 500km/h) |
| #24 UE rotation | No UE rotation (baseline). UE rotation is not precluded and the corresponding rotation speed is up to companies to report. |
| #25 BS Antenna height | Dense urban macro and Urban Macro: 25 m; Dense urban micro: 10 m; Indoor: 3m |
| #26 UE Antenna height | Section 7.2 in TR 38.901. Others are not precluded (companies to report). |
| #27 Car penetration Loss | TR 38.901, sec 7.4.3.2: μ = 9 dB, σp = 5 dB |
| #28 Building penetration loss (O2I) | Table 7.4.3-2 in TR 38.901 |
| #29 UE mobility feature (optional) |  |
| #30 Scheduling algorithm | PF scheduler |
| #31 MCS | Use NR MCS |
| #32 Traffic Model | FTP model 1/3 with packet size 0.5 Mbytes (other value is not precluded) Other traffic models are not precluded (companies to report). Full buffer (Optional) |
| #33 CSI Feedback | CSI periodicity: 10ms, 20ms (baseline), 40ms, 80ms, 160ms FFS: Other update for high-speed train |
| #34 Resource Utilization | 30%, 50%, 70% (optional) |
| #35 Prediction parameter |  |
| #36 UE number/cell | Reuse the configuration(s) from 6GR air interface evaluation assumptions |
| #37 Layout/deployment | Reuse the assumptions of uplink/downlink transmission schemes (10.5.2.2/3) 7 x 3, single layer, hex grid (baseline) 7 x 3 two layers, macro layer: hex grid; micro layer: locations of micro sites are reported by company (optional) 19 x 3, single layer, hex grid (optional) FFS: Other update for high-speed train |
| #38 Inter-cell interference model | Reuse the assumptions of DL-based CSI (10.5.3.1) Explicitly and realistically modelled |
| #39 Metric |  |
Multi-TRP Scenario 1: Intra-cell scenario, with 4 TRPs/RRHs per multi-TRP set
Multi-TRP Scenario 2: intra-site, inter-cell, with 3 TRPs per cooperative set
(as baseline)
Multi-TRP Scenario 3: Inter/intra-site, inter-cell with  TRPs per cooperative set
Companies report the setting when N>1
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.4-a001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.4 Beam management for downlink and uplink

```text
Support the following table as the basic assumption of LLS for evaluation of 6GR beam management:
MCC: In below table, only the parts marked as green are assumed stable, the other proposed agreements are not yet finally confirmed.
| Parameter | Value |
| --- | --- |
| #1 Carrier Frequency | 4GHz, 7GHz, 30GHz |
| #2 Duplex / Waveform | TDD/CP-OFDM |
| #3 Subcarrier Spacing | For 4GHz/7GHz: 30KHz; For 30GHz:120KHz |
| #4 Simulation Bandwidth | Reuse the assumptions of PDSCH EVM (10.5.2.2) 20 MHz, 100 MHz Other bandwidths are not precluded (companies to report) |
| #5 Channel Model | Reuse the assumptions of PDSCH EVM/CSI-others (10.5.2.2/10.5.3.3) CDL-A/B/C/D model in TR 38.901 The CDL table is translated so that the strongest cluster’s AoD and AoA occur at a random angle for both the antenna panels of TRP and UE in the local coordinate. The value of the random angle is selected to be uniformly distributed from +30 to -30 degree. The random value is chosen independently for both AoD and AoA. |
| #6 Delay Spread | Reuse the assumptions of PDSCH EVM (10.5.2.2) 30 ns, 100 ns, 300 ns, 1000 ns (optional) |
| #7 NW Antenna Config | Reuse the agreed configuration(s) from 6GR air interface evaluation assumptions For 7GHz, the following can be further considered: 128 TXRUs, 2048AEs, (M, N, P, Mg, Ng; Mp, Np) = (64, 16, 2, 1, 1, 8, 8), (dH, dV) = (0.5, 0.5); For 30GHz, the following can be further considered: (M, N, P, Mg, Ng; Mp, Np) = (8, 16, 2, 1, 1; 1, 1), or (16, 32, 2, 1, 1; 1, 1)), (dH, dV) = (0.5, 0.5); |
| #8 Multi-TRP operation | The maximum number of coordinated TRP(s) = {1 (baseline), 2, 3, 4}, and other larger value(s) are not precluded CDL channel model is generated per TRP independently; Backhaul: ideal (baseline) or non-ideal; Sync: ideal (baseline) or non-ideal; Companies explain the details, if any. |
| #9 TXRU mapping to antenna elements | A single TXRU is mapped per panel per subarray per polarization. Others are not precluded (companies to report). |
| #10 Beam-forming scheme | Companies explain the details, e.g., DFT-based or Eigen-based |
| #11 Procedure of beam sweeping | Companies explain the details |
| #12 Criteria for beam selection | To maximize RSRP (with/without a margin (baseline for margin: 3dB, companies to report)) as a baseline. Other criteria is not precluded and up to companies to report. |
| #13 UE Antenna Config | 4GHz & 7GHz: Reuse the agreed configuration(s) from 6GR air interface evaluation assumptions; 30GHz: Reuse the agreed configuration(s) from 6GR air interface evaluation assumptions: [Config 0 (one panel) or Config 1 (two panels)]: (M, N, P, Mg, Ng; Mp, Np) = (4, 1, 2, 1, 1; 1, 1) is considered as a baseline |
| #14 BS array orientation | Azimuth 0°, mechanic downtilt: 90° in GCS. |
| #15 UE array orientation | ΩUT,a uniformly distributed on [0, 360] degree, ΩUT,b = 0°, ΩUT,g = 0° |
| #16 UE antenna element radiation pattern | For 4 GHz/7GHz: Option-1: Omni-directional with 0dBi gain; Option-2: According to Table 7.3-2 in TR 38.901 (radiation power pattern for handheld UT) For 30 GHz: See Table A.2.1-8 in TR 38.802 |
| #17 UE Velocity | 3km/h, 30km/h, 120km/h (Optional), 350km/h(Optional), 500km/h (Optional) |
| #18 MIMO Scheme | SU-MIMO/MU-MIMO |
| #19 CW-to-layer mapping | Reuse the assumptions of CSI EVM (10.5.3.1) |
| #20 Channel coding | LDPC for DL/UL data channel, Polar for CSI |
| #21 SSB, CSI-RS configuration for BM | NR SSB, CSI-RS for BM as benchmark, and it is up to company to report other configuration, e.g., periodicity. |
| #22 SRS configuration for BM | NR SRS with usage set to BM as baseline, and it is up to company to report other configuration, e.g., periodicity |
| #23 Receiver Type | MMSE-IRC as baseline; R-ML (companies to report) |
| #24 Channel Estimation | Ideal or realistic |
| #25 MCS | NR MCS (fixed, or AMC) |
| #26 Performance Metric(s) |  |
R1-2602857	Moderator summary #2 on beam management for DL and UL	Moderators (ZTE, Apple)
From Tuesday session
Debate on the support of the following QCL definition for 6GR:
Alt.1: A first antenna port is said to be quasi co-located with a second antenna port if the large-scale properties of the channel over which a symbol on the first antenna port is conveyed can be inferred from the channel over which a symbol on the second antenna port is conveyed.
FFS: Whether/how to extend the QCL definition, if the large-scale properties are inferred from the combined channels corresponding to >1 second antenna ports.
Alt.2: A first antenna port is said to be quasi co-located with a second antenna port/antenna port group if the large-scale properties of the channel over which a symbol on the first antenna port is conveyed can be inferred from the channel over which a symbol on the second antenna port/antenna port group is conveyed.
TBC: Support antenna port group
MCC: RAN1 did not conclude.
R1-2602858	Moderator summary #3 on beam management for DL and UL	Moderators (ZTE, Apple)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.4-a002`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.4 Beam management for downlink and uplink

```text
Support the following table as the assumption of SLS for evaluation of 6GR beam management:
| #29 UE mobility feature (optional) | Baseline: Random direction straight-line trajectories (from 38.843, Option-3) - Initial UE location, moving direction and speed: UE is randomly dropped in a cell, and an initial moving direction is randomly selected, with a fixed speed. - The initial UE location should be randomly drop within the following blue area: where d1 is the minimum distance that UE should be away from the BS. Each sector is a cell and that the cell association is geometry based. Company to report whether inter-cell handover or switching is disabled during the simulation. Company to report whether the trajectory should be terminated (e.g., single-TRP) or be retained (e.g., multi-TRP), if the UE trajectory hits the site boundary (the hexagonal grid) Other UE mobility model(s), e.g., EVM for NR ICBM, linear trajectory model with random and smooth direction change (i.e., TR38.843, Option-2), are not precluded (companies to report). |
| --- | --- |
| #35 Prediction parameter | Company can report assumption for set-A and set-B, prediction window and any extension for intra-/inter-cell/multi-TRP measurement Set A: M*N M: {8, 16, 32, 64, 256,1024}. N: {1, 2, 3, 4}. Ratio of the size of Set-B to Set-A: {1, 1/2, 1/4, 1/8, 1/16, 1/32} For multi-TRP, Set-A and Set-B can contain beams across TRP(s). Other values for M, N and ratio are not precluded. Set A/Set B combinations: Alt1: Set B is different from Set A Alt2: Set B is a subset of Set A Alt3: Set B is the same as Set A Regarding temporal domain prediction, the following can be considered: Time gap between neighboring predicted time instances: {20ms, 40ms, 80ms, 120ms, 160ms, 200ms}. Predicted time instances: {1, 2, 4, 8}. Measured time instances: companies to report. Other values for the above are not precluded Other prediction mechanism is not precluded and up to companies’ report. |
| #39 Metric | Top-K/1 beam prediction accuracy (with or without L1-RSRP margin), average/5%-ile UPT/throughput, SINR/RSRP, L1-RSRP/SINR difference between Top-1 predicted beam and genie-aided beam, RS overhead reduction, beam management latency, and/or number of model-parameter(s)/model computational complexity. Companies can report other performance metrics Companies report the assumption of transmission scheme, if UPT/throughput is reported. |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.4-a003`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.4 Beam management for downlink and uplink

```text
Support the following table as the assumption of LLS for evaluation of 6GR beam management:
| #26 Performance Metric(s) | BLER and Spectrum Efficiency (SE) Companies can report other performance metrics |
| --- | --- |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.4-a004`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.4 Beam management for downlink and uplink

```text
For 6GR UE-initiated beam management (UEIBM), Study the following events for single-TRP as a starting point:
Event-1: The measured/predicted quality of the current/serving beam is worse than a threshold, including “beam failure”.
Event-2: The measured/predicted quality of at least one candidate beam becomes a threshold value better than the current/serving beam.
The candidate beam is associated with a same (i.e., intra-cell) or a different physical cell ID (i.e., inter-cell case) as the current/serving beam.
How to extend to m-TRP use case, including the feasibility.
R1-2602859	Moderator summary #4 on beam management for DL and UL	Moderators (ZTE, Apple)
R1-2603456	Moderator summary #5 on beam management for DL and UL	Moderators (ZTE, Apple)
From Friday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.4-a005`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.4 Beam management for downlink and uplink

```text
Study requirement/functionality of DL RS for beam measurement, e.g., number of RS ports, time/frequency-domain RS pattern, time-domain behaviour, etc.
Note: Sync-signal design is not considered herein
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.4-a006`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.4 Beam management for downlink and uplink

```text
For the study on spatial/temporal/frequency domain beam measurement/prediction (relevant to AI/ML or non-AI/advanced schemes), the following is considered:
Implementation complexity/overhead:
Model/computation complexity: FLOPs
Model size, if AI/ML is involved: Number of parameters
Note: The above complexity/overhead with the increase of TRP number should be clarified.
Benchmark:
Benchmark-1: based on the measurement of Set-A;
Benchmark-2: only based on the measurement of Set-B (non-prediction).
Other benchmarks are not precluded and up to companies report
Evaluation assumptions with the following clarifications
Spatial/Temporal domain DL Tx beam prediction and management, scenarios of both single-TRP and multi-TRP (intra/inter-cell) can be considered.
For multi-TRP (intra/inter-cell), companies report whether the predicted beam(s) (Set-A) are from the same set of cells/TRPs corresponding to the measured beam(s) (Set-B) or not.
Note (Sample and Hold): Regarding temporal domain prediction, reuse the result of the latest measurement.
Regarding frequency domain beam measurement/prediction (cross-frequency), the scenario of co-located and non-collocated, intra-frequency-range (inter-/intra-band) and inter-frequency-range can be considered.
Note: Regarding Cross frequency DL Tx beam prediction, Set-A includes beams in the predicted/target frequency, and Set-B is based on the measurement in the source frequency
Further clarification/extension on channel modeling (e.g., inter-frequency-range, non-collocated) can be studied.
Note: For collocated case, impact on performance using same/different placement and orientation on NW antenna(s) for source and target frequencies should be considered.
Note: the above assumptions can also apply for non-AI schemes, i.e., without training/inference/data collection, when applicable.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.4-a007`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.4 Beam management for downlink and uplink

```text
For network-initiated beam reporting in 6GR, support at least L1-RSRP as a measurement/report quantity for beam reporting, when applicable.
Note: L1-RSRP maybe measured or predicted by UE.
FFS: L1-SINR and others.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.4-a008`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.2.4 Beam management for downlink and uplink

```text
Regarding NW-initiated beam management, study DL beam measurement and report procedure on DL RS(s) for both single-TRP/cell/carrier and multi-TRP/cell/carrier scenario(s).
At least the following aspects can be studied:
Procedure of beam sweeping/tracking, e.g., intra-/inter-symbol, time-domain/frequency-domain sweeping
Measurement/prediction metrics
Time-domain behavior for report, e.g., aperiodic, semi-persistent, periodic
Report content
Note: Report container for study will be discussed under other agenda.
Note: RAN1 strives to support a unified framework for beam measurement and reporting for MIMO and mobility.
R1-2603475	Moderator summary #6 on beam management for DL and UL	Moderators (ZTE, Apple)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.2.4-a009`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For spatial domain CSI prediction, Baseline #2 is Linear interpolation, where the channel of an unmeasured port uses the channel of the nearest measured ports based on CSI-RS port indexing (for evaluation purpose, 5G NR port indexing is assumed) in the same polarization, without using assistance information derived from full-dimensional measurement.
Companies to report remaining details if any, including other baselines
R1-2602019	Feature lead summary #3 on DL-based CSI acquisition	Moderator (Samsung), Moderator (vivo)
R1-2602020	Feature lead summary #4 on DL-based CSI acquisition	Moderator (Samsung), Moderator (vivo)
From Tuesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.1-a001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For 6GR codebook design for CSI report, study considering the following to ensure better performance than 5G
SU-MIMO and MU-MIMO
Single TRP and multi-TRP including CJT
Other use scenarios, at least including High Doppler / High Speed Train (HST), Near-Field Propagation, spatial non-stationary (SNS)
Note: Companies to provide complexity analysis.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.1-a002`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
Starting from NR L1-based CSI reporting design, study whether/how the following aspects to be addressed in 6GR CSI reporting design taking into account of the comparison, at least including:
B1. Scheduling constraint relaxation
B2. Streamlined multiplexing complexity/collision handling rules, if applicable
B3. Streamlined CSI timeline including timeline relaxation
B4. Handling of varying CSI payload size
For comparison on CSI report in L1 and L2, considering at least the following aspects taking into account of B1~B4:
A1. Efficiency /overhead
A2. Latency
A3. Reliability
A4. Implementation processing complexity at UE considering cross layer complexity (if any)
A5. Implementation processing complexity at NW considering cross layer complexity (if any)
A6. Congestion
A7. Min/Max CSI payload
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.1-a003`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For CSI-RS for CSI acquisition in 6GR, study the maximum number of ports considering the following alternatives
Alt 1: The maximum number of CSI-RS ports is 128
Alt 2: The maximum number of CSI-RS ports is 256
Alt 3: The maximum number of CSI-RS ports is 512
The study includes evaluation of the performance and CSI-RS overhead
Note: relevant complexity can also be considered
FFS whether all the NR port numbers are supported
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.1-a004`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
6GR supports NZP CSI-RS as the channel measurement RS for DL based CSI acquisition
FFS other reference signals, e.g., DMRS
FFS Aspects related with non-precoded CSI-RS or precoded CSI-RS
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.1-a005`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
Consider CSI-IM as the baseline for interference measurement resource for DL CSI acquisition in 6GR
FFS other RS types, e.g., NZP CSI-RS, DMRS, etc
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.1-a006`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
On time-domain type of 6G CSI-RS for downlink based CSI acquisition, at least support periodic and aperiodic CSI-RS, and further study
Whether semi-persistent CSI-RS is additionally supported
Whether new time-domain behavior is beneficial
R1-2602021	Feature lead summary #5 on DL-based CSI acquisition	Moderator (Samsung), Moderator (vivo)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.1-a007`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
6GR CSI-RS pattern is defined as aggregation of CDM groups, for which study the following aspects
Whether CSI-RS pattern is defined on single or multiple slots/RBs in time/frequency domain
For CDM design, consider the following options
RE locations of CDM groups
Option 1-1: Localized CDM group similar to 5G NR, where one CDM group contains adjacent REs
Option 1-2: Comb-based CDM group, where subcarriers in one CDM group are distributed following comb pattern
CDM group size and type
Option 2-1: Reuse/Simplify NR, i.e., CDM 1, 2, 4, 8 with potential reduction of candidates,
Option 2-2: Larger CDM size, e.g., CDM 16
Option 2-3: New CDM type for NR CDM size (e.g., fd-CDM4 or cdm8-FD4-TD2)
At least following aspects to be considered for designing CSI-RS pattern
CSI-RS Overhead
CSI-RS coverage
CSI-RS sharing use cases
Channel estimation performance
NES
Coexistence with other signals/channels
Digital precoding/Hybrid precoding structures
MRSS
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.1-a008`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For the study of non-AI/AI based time domain CSI prediction at UE or NW side, consider
Intermediate metric: Subband-level per layer per predicted time instance eigenvector/precoder SGCS, NMSE calculated between predicted channel and ground-truth channel
To compare NW side prediction with UE side prediction, the impact of CSI reporting shall be considered
FFS WB SGCS/NMSE
System-level metric: UPT (mean, 5%tile), CSI reporting overhead
CSI-RS overhead is considered in UPT calculation
To evaluate CSI report overhead, companies to report how the PMI/channel of the predicted time instance(s) is reported
Link-level metric: BLER/SE/throughput
Complexity metrics: FLOPs/M
For AI based prediction: number of parameters/M
Baseline: Sample & Hold
Additional EVM assumption
Channel modelling: Spatial consistency with mobility procedure A
UE distribution: 100% outdoors with speed 10, 20, 30, 60, 120km/h
Other speeds are not precluded
UE Rx antenna phase discontinuity modelling: Companies to report the used model
Observation window (number/distance between adjacent CSI-RS occasions): e.g., 5/10ms, 5/20ms for periodic CSI-RS; and 12/2ms, 8/2ms, 4/2ms for aperiodic CSI-RS;
other values can be additionally submitted
Prediction window (number/length of each predicted instances/gap from the last observation instance to the 1st predicted instance):  e.g., 1/10ms/5ms, 4/10ms/5ms;
other values can be additionally submitted.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.1-a009`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For the study on JSCM-based CSI compression, at least considering the following aspects on top of previous agreement for AI-based CSI compression:
Performance of Projection-matrix-based compression (compress target CSI by multiplying with a projection matrix at UE) or encoder-based (e.g., transformer-based), and reconstruct the CSI at NW with a NW-sided model
Companies to report method for obtaining projection matrix/encoder
Companies to report non-AI/ML operations (if any) before/after multiplying with a projection matrix.
Study the potential RF related impact (e.g., PAPR) and potential solutions at least including
Map the output to certain discrete constellation with, at least considering
NR modulation constellations, e.g., 16QAM, 64QAM, 256QAM, 1024QAM
Other modulation constellations, e.g., 64APSK, other customized (fixed) constellations
Map/restrict the output, e.g., with restricted amplitude(s)
PAPR restriction during training as part of loss function
Note: the above operation is fixed/known by NW
Both precoding matrix and explicit H can be considered as the target CSI for inference
For performance evaluation related to error detection,
For benchmark of SSCC and eType II/Type I, when CSI error is detected, previous CSI is adopted to derive the precoder for downlink transmission
For JSCM, details of error detection, if any, companies report the assumption in the evaluation
Study on generalization and scalability performance
Study on LCM for JSCM-based CSI compression
Note: Companies to report how to multiplex JSCM-compressed precoding matrix/explicit H with other UCI, e.g., RI or CQI, and/or UL-SCH
Note: The related testability issue is up to RAN 4.
Note: LS to RAN 4 is to be considered for RAN 4 potential related impacts, e.g., EVM, ACLR, SEM, PAPR, testability, arbitrary constellation, when mature.
Note: Companies to report I/Q imbalance assumption, if any
R1-2603375	Feature lead summary #6 on DL-based CSI acquisition	Moderator (Samsung), Moderator (vivo)
R1-2603376	Feature lead summary #7 on DL-based CSI acquisition	Moderator (Samsung), Moderator (vivo)
R1-2603377	Feature lead summary #8 on DL-based CSI acquisition	Moderator (Samsung), Moderator (vivo)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.1-a010`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For 6GR CSI-RS for DL based CSI acquisition, study CSI-RS RE sharing considering the following use cases.
Use case 1: Sharing a common set or subset of REs among CSI-RS with different number of ports
Use case 2: Sharing a common set or subset of REs among CSI-RS with different frequency densities
Use case 3: Sharing a common set or subset of REs among CSI-RS with different periodicities/time domain types
Use case 4: Sharing a common set or subset of REs among 5G CSI-RS and 6G CSI-RS
Note: the combination of the above use cases can be considered.
Note: the above use cases are design principles at this stage. Whether there is specification impact subjects to further discussion.
Note: the scenarios for sharing of CSI-RS may need to consider CSI-RS channel estimation performance at cell-edge, precoded/non-precoded CSI-RS, AI/non-AI, NES enabled/disabled, UEs with different measurement capabilities, single-TRP/Panel or multi-TRP/Panel etc
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.1-a011`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For 6GR, on the study of non-AI or AI based frequency/spatial domain prediction in NW side or UE side, study necessary assistance information used to predict the full-dimension channel from the reduced-dimension measurement
Companies to provide details on the assistance information, including the content, how to derive it, how often it needs to be updated, etc.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.1-a012`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For AI based CSI prediction, evaluate generalization/scalability performances of prediction models at least across one or more of the following scenarios/configurations
Various deployment scenarios, e.g., UMa, InH
Various carrier frequencies
Various indoor/outdoor distributions
Various BS antenna configurations, e.g., antenna spacing, antenna virtualization/TxRU mapping, antenna port layouts, antenna port numbers
Various sampling ratios and/or sampling patterns
Various UE side parameters, e.g., UE speeds, SNR/SINR, UE channel estimation errors, UE antenna configurations
Various report resolution
Companies are encouraged to evaluate generalization/scalability performance across multiple scenario/configuration combinations.
The above is at least applicable to frequency/spatial/time domain prediction. FFS other sub-use case specific generalization aspects, if any.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.1-a013`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For the codebook design, study at least the following codebook structures
For low-resolution/ high-resolution CSI, considering ,  for evaluation
Note: Other codebook structure and enhancements of NR codebook structure(s), or other codebook are not precluded
Note: NR codebooks are used as benchmark for performance and complexity assessment
For evaluation on codebook design, companies report
the max rank assumption, and whether a single codebook structure across all ranks for low-/high-resolution CSI, if appliable
the assumption of SD/FD basis selection, if appliable
the codebook parameter assumptions
basis format assumption
assumption of target CSI and corresponding codebook structure, e.g., implicit/explicit CSI
complexity analysis
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.1-a014`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For the evaluation of scalability/generalization for AI-based CSI compression, the evaluation methodology in NR (as in TR 38.843) can be considered as the starting point. The set of configurations are considered focusing on one or more of the following aspects at a starting point:
Various DL channels for compression, for example, deployment scenarios (e.g., UMa, UMi, InH), outdoor/indoor UE distributions (e.g., 10:0, 8:2, 5:5, 2:8, 0:10), antenna virtualization (TxRU mapping)
Various uplink channel/interference for uplink transmission (e.g., AWGN, CDL, TDL, Uma channel, different uplink SNR range, different UL noise/interference patterns)
Various UL resource size, e.g., #of REs for CSI feedback
Various NW (Rx chain, channel estimation, equalization) and UE (Tx chain, and RF impairments) implementations
Various number of Tx/Rx ports/layers, if applicable
Various number of subbands
Companies report the training and testing assumptions
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.1-a015`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For the study on channel property information (CPI), at least the following is considered.
Potential use cases, e.g., assisting RS configuration; assisting CSI report configuration; assisting scheduling coordination at spatial domain; how to be used for event/condition definition for event-triggered CSI computation and reporting; determining CSI report; assisting CSI prediction
Note: examples are for the purpose of discussion. Other use cases are not excluded.
Note: assisting SRS based CSI acquisition is to be discussed in 10.5.3.3
For each potential use case, studying details of
Benchmark
KPI
Report quantities/updating occasion, and associated time domain computation assumptions, if applicable
measurement RS
UE computation complexity for CPI, and corresponding CSI feedback complexity, if applicable.
Note: Strive for common report quantities for use cases, if applicable.
Note: The related testability issue is up to RAN 4.
Note: LS to RAN 4 is to be considered for RAN 4 testability issues, when mature.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.1-a016`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
Study on whether/how to support CSI report for CJT calibration.
Final summary in R1-2603397.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.1-a017`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.2 Aspects of uplink-based CSI acquisition

```text
Study at least hierarchical structure of SRS resource set and SRS resource for 6GR.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.2-a001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.2 Aspects of uplink-based CSI acquisition

```text
Study how to support multiple usages using a same SRS transmission.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.2-a002`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.2 Aspects of uplink-based CSI acquisition

```text
Study SRS sequence design considering at least the following aspects:
Coverage, capacity and measurement performance, e.g., PAPR, size of sequence pool, cross-correlation/auto-correlation
Length candidates of SRS sequence
SRS resource element mapping
Flexible adaptation of SRS frequency domain parameters (if supported)
R1-2602506	Moderator summary#2 on uplink-based CSI acquisition	Moderator (CATT)
From Tuesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.2-a003`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.2 Aspects of uplink-based CSI acquisition

```text
ZC and CGS sequences in NR are the starting point for studying 6GR SRS design.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.2-a004`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.2 Aspects of uplink-based CSI acquisition

```text
{1, 2, 3, 4, 8} are supported as the numbers of SRS antenna ports
FFS: Other number of UE antenna ports
Note: Separate discussion on the number of antenna ports of UE device(s).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.2-a005`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.2 Aspects of uplink-based CSI acquisition

```text
Support P/AP-SRS as the baseline for 6GR. Further study:
Whether it is necessary to support SP-SRS.
Note: UE initiated SRS can be discussed separately.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.2-a006`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.2 Aspects of uplink-based CSI acquisition

```text
For 6GR SRS frequency hopping mechanism, study the following:
SRS frequency hopping pattern
Partial frequency sounding with/without intra-repetition hopping
R1-2602507	Moderator summary#3 on uplink-based CSI acquisition	Moderator (CATT)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.2-a007`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.2 Aspects of uplink-based CSI acquisition

```text
5G SRS pattern design per resource (in frequency domain) with regular comb values (comb values supported by NR), i.e., combs 2, 4 and 8 is taken as starting point for the 6GR SRS study, further study at least the following aspects.
Multiplexing of multiple SRS ports.
Sparse SRS patterns, such as larger comb values, non-uniform-based patterns.
Note 1: impact of SRS pattern design on at least complexity, coverage, capacity and performance is to be considered.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.2-a008`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.2 Aspects of uplink-based CSI acquisition

```text
For UL-based CSI acquisition, study the following aspects of SRS repetition
Number of repetitions
Cross-slot SRS transmission
Others
R1-2602508	Moderator summary#4 on uplink-based CSI acquisition	Moderator (CATT)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.2-a009`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.2 Aspects of uplink-based CSI acquisition

```text
For UL-based CSI acquisition, study at least the following mechanisms of SRS interference mitigation
Interference randomization based on hopping of group/base sequence, start RB index, comb offset, and cyclic shift for SRS
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.2-a010`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.2 Aspects of uplink-based CSI acquisition

```text
To support maximum SRS bandwidth beyond 272 PRBs within a carrier efficiently, study at least the following aspects:
Frequency hopping
Sparse SRS in frequency domain
Redefining or extending the existing SRS bandwidth configuration
SRS sequence design
Combinations of above schemes
Other approaches are not excluded
Note1: Sounding for larger DL CBW is a separate issue to be studied.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.2-a011`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.2 Aspects of uplink-based CSI acquisition

```text
At least from the perspectives of benefit, complexity, and overhead, study the feasibility and necessity of introducing more dynamic/flexible adaptation of the following SRS parameters than that supported by NR.
Frequency domain parameters, such as SRS bandwidth, starting position in frequency domain, hopping related parameters, resource element mapping
Time domain parameters, such as slot offset, starting position in time domain, number of consecutive OFDM symbols, periodicity
Code domain parameters, such as cyclic shift
Number of SRS ports
Combinations of above schemes, such as adaptive combination of comb offset and cyclic shift
Spatial domain parameters, such as SRS precoding
Other schemes are not excluded
Note 1: feasibility may be different for each of the parameters.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.2-a012`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.2 Aspects of uplink-based CSI acquisition

```text
For the inter-UE multiplexing of SRS and other uplink channels/signals (e.g., SRS/PUCCH/PUSCH), study at least the following aspects
Whether/how to introduce unified hopping between SRS and other UL channels (i.e., PUCCH, PUSCH)
PUSCH/PUCCH Rate matching for SRS.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.2-a013`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.2 Aspects of uplink-based CSI acquisition

```text
For UL-based CSI acquisition, study at least the following aspects of precoded SRS transmission.
How the precoder is determined
Whether it requires UE side reciprocity or not
Coherency assumption on antenna ports
Impact on PAPR
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.2-a014`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.3 Other aspects

```text
Study and evaluate the following parameters and candidate values to determine the frequency domain structure of RS for finer time/frequency tracking for both connected and idle modes
Minimum Bandwidth: candidate values {partial BW (please clarify) of the BWP, full BW of the BWP}.
Density: candidate values {x} REs/RB.
R1-2602750	FL summary #2 on other aspects of CSI acquisition and report	Moderator (Lenovo)
From Tuesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.3-a001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.3 Other aspects

```text
Study single-port and multi-port RS for finer time/frequency tracking.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.3-a002`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.3 Other aspects

```text
Study and evaluate the mismatch and impact on performance, if any, between QCL parameters of the RS for finer time/frequency tracking and the target RSs/Channels.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.3-a003`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.3 Other aspects

```text
Study and evaluate the following parameters and candidate values to determine the time domain factors of the RS for finer time/frequency tracking for both connected and idle modes
Time domain behaviour:
Candidate values: periodic, aperiodic, semi-persistent
Combination of them can be used for tracking
Periodicity for semi-persistent and periodic tracking RS, if supported
Candidate values: {Y} ms,
Number of symbols in a slot
Candidate values: {N}
Time interval between tracking RS symbols for finer time/frequency tracking
Candidate values: {Ssymb} symbols
Number of consecutive slots
Candidate values: {Sslot}
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.3-a004`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.3 Other aspects

```text
Regarding the frequency domain density for RS for finer time/frequency tracking for both connected and idle modes, at least the following candidate values are considered for study and evaluation
x∈{2,3,4,6,12}.
x is defined as number of REs/RBs/symbol/port
Other values are not precluded.
R1-2602751	FL summary #3 on other aspects of CSI acquisition and report	Moderator (Lenovo)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.3-a005`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.3 Other aspects

```text
At least study the following use case for joint DL/UL CSI acquisition
Use case 1: SRS based CSI acquisition assisted by DL based measurement and reporting
DL based measurement and reporting is reported by companies
Note: Both AI and non-AI solutions can be considered
Use case 2: MCS and rank selection for DL transmission with SRS based CSI acquisition assisted by other assistant information reporting
R1-2602752	FL summary #4 on other aspects of CSI acquisition and report	Moderator (Lenovo)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.3-a006`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.3 Other aspects

```text
For the purpose of performance evaluation of joint DL/UL based CSI acquisition, consider the following SRS error model:
SRS error model
is the estimated channel, is the channel response in frequency domain.  is the white complex Gaussian matrix with zero mean, and variance  is the scaling factor .
The details of calculation on should be provided by each company and additional factors (e.g., SRS interference, non-perfect open loop power control, UE TX antenna gain imbalance modelling) may be considered.
Examples on calculation of
SINR refers to the underlying SINR of the SRS as received at the aNB
for inter-cell SRS interference: UEs are randomly grouped to 4 groups in baseline cases, UEs in the same group (in different cells) would interfere with each other’s SRS
Use pathloss for interference calculation
Actual SRS transmission and estimation can be used instead of such modeling.
Other models can be used by companies.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.3-a007`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.3 Other aspects

```text
For the purpose of performance evaluation of joint DL/UL based CSI acquisition, consider the following antenna calibration error:
Antenna calibration error can be modeled as
represents the downlink channel obtained using channel reciprocity at aNB side and has a dimension .
is the uplink channel derived by SRS and has a dimension .
is the number of antenna ports of UE,  is the number antenna ports of aNB.
is the amplitude mismatch coefficient and could be modeled as subject to uniform or Gaussian distribution, e.g., Gaussian distribution with zero mean and variance X1=0.35 dB.
is the phase mismatch coefficient and could be modeled as subject to uniform or Gaussian distribution, e.g., Gaussian distribution with zero mean and variance Y1=5 degrees.
Other values on X1 and Y1 can be considered and reported by companies.
is the amplitude mismatch coefficient and could be modeled as subject to uniform or Gaussian distribution, e.g., Gaussian distribution with zero mean and variance X2 dB.
is the phase mismatch coefficient and could be modeled as subject to uniform or Gaussian distribution, e.g., Gaussian distribution with zero mean and variance Y2 degrees.
Values on X2 and Y2 are reported by companies.
The distribution of  and  can also be reported by companies.
Both or either of aNB or UE-side antenna calibration error can be used in the simulation and is reported by companies.
Note: For any scheme requiring UE DL/UL reciprocity, the feasibility of UE DL/UL reciprocity should be considered.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.3-a008`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.3.3 Other aspects

```text
For the purpose of performance evaluation of joint DL/UL based CSI acquisition, study whether and how to model the uplink and downlink insertion loss difference. Example on uplink and downlink insertion loss difference model:
The uplink and downlink insertion loss difference by using the model , where  is a diagonal matrix with diagonal coefficient  representing the power ratio of the -th antenna with respect to the antenna that has highest power in dB scale. is the uplink channel derived by SRS and has a dimension .  The generation of  is reported by companies.
R1-2603474	Final FL summary on other aspects of CSI acquisition and report	Moderator (Lenovo)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.3.3-a009`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.4.1 Downlink control channel, scheduling for downlink and uplink transmission

```text
For the study of the adaptation of PDCCH monitoring in 6GR in connected mode, study at least the time domain adaptation of PDCCH monitoring and the corresponding signalling mechanisms, considering at least techniques in NR as starting point.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.4.1-a001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.4.1 Downlink control channel, scheduling for downlink and uplink transmission

```text
Study whether/how to support the minimum DCI-to-PDSCH scheduling offset > 0 slot.
R1-2603348	FL summary#3 for downlink control and DL/UL scheduling	Moderator (CMCC, Apple)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.4.1-a002`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.4.1 Downlink control channel, scheduling for downlink and uplink transmission

```text
RAN1 to study how to determine various DCI sizes that the UE monitors.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.4.1-a003`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.4.1 Downlink control channel, scheduling for downlink and uplink transmission

```text
RAN1 to study for a given DCI, the methods to determine the functions carried by the DCI
e.g. single or multiple Header/Identifier field(s), RNTI, DCI size,…
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.4.1-a004`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.4.1 Downlink control channel, scheduling for downlink and uplink transmission

```text
For 6GR, a single PDCCH carrying the entire DCI information is the baseline at least for DCI transmitted for UEs in idle mode.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.4.1-a005`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.4.1 Downlink control channel, scheduling for downlink and uplink transmission

```text
For the study of two-stage DCI in 6GR, consider at least the following aspects:
The targeted scenarios and use cases
Functionalities of the two stages and the information carried in each stage
Physical [channel/signal] for each stage
Timing relationships between first-stage [DCI], second-stage [DCI] and scheduled PDSCH(s)/PUSCH(s)
Monitoring and blind decoding assumptions for each stage
Network/UE complexity
Impact on coverage
Impact on reliability
Impact on blocking probability
Resource efficiency/overhead
Impact on UE/network power consumption
Impact on DCI decoding latency, and data processing timeline
Impact on scheduling delay and user experience
Pros and cons compared to single-stage DCI
Note: companies are encouraged to provide their assumptions/designs used for studying above aspects.
R1-2603421	FL summary#4 for downlink control and DL/UL scheduling	Moderator (CMCC, Apple)
Presented in Thursday session.
No more stable proposals.
R1-2603422	Final FL summary for downlink control and DL/UL scheduling	Moderator (CMCC, Apple)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.4.1-a006`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.4.3 HARQ related Aspects

```text
In 6GR, study whether and how to support downlink HARQ-ACK feedback granularity smaller than TB-level, considering at least the following factors:
Feedback overhead
Retransmission efficiency
Implementation feasibility
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.4.3-a001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.4.3 HARQ related Aspects

```text
In 6GR, study whether and how to support HARQ-ACK bundling across multiple TBs.
R1-2603252	FL summary #2 for AI 10.5.4.3: 6GR HARQ related aspects	Moderator (OPPO)
Presented in Tuesday session
R1-2603253	FL summary #3 for AI 10.5.4.3: 6GR HARQ related aspects	Moderator (OPPO)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.4.3-a002`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.4.3 HARQ related Aspects

```text
Study HARQ-ACK codebook(s) and its operation for downlink HARQ operation in 6GR, considering at least the following aspects:
HARQ-ACK codebook generation
HARQ-ACK feedback granularity, e.g., TB-level, smaller than TB-level, bundling across multiple TBs, etc.
Feedback overhead
HARQ-ACK payload size and bits order misalignment between NW and UE due to DCI missing
Ambiguity between DTX of DL assignment and PDSCH decoding failure when network decodes a NACK in a HARQ-ACK codebook
Coordination between schedulers, e.g., between multiple carriers, between DL and UL, etc.
Feedback complexity
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.4.3-a003`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.4.3 HARQ related Aspects

```text
In 6GR, the minimum downlink HARQ-ACK payload size is 1 and the upper limit supported by 5G NR Polar coding can be reused (i.e., 1706 bits) at least for Mechanism 1 of HARQ feedback if supported.
Note1: this upper limit does not imply the max HARQ-ACK payload size would be 1706.
Note2: the exact value of the maximum size may be determined at a later stage if needed.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.4.3-a004`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.4.3 HARQ related Aspects

```text
In 6GR, study the details and pros and cons of the following methods to determine timing and resource for downlink HARQ-ACK feedback.
Method 1: Dynamic indication in DCI
Method 2: UE initiated HARQ-ACK feedback
Method 3: Next available/feasible time slot of semi-static configured resources that satisfy UE processing time/capability
Method 4: Only based on configuration via RRC
Note: combinations of above methods and other methods are not precluded.
R1-2603326	FL summary #4 for AI 10.5.4.3: 6GR HARQ related aspects	Moderator (OPPO)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.4.3-a005`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.4.3 HARQ related Aspects

```text
For 6GR UL: Study an explicit indication or implicit indication for a given HARQ process failure to trigger faster ARQ procedure in UL.
Note: Companies are encouraged to check RAN2 agreements and LS if any on fast ARQ in RAN2#133bis.
R1-2603254	FL summary for AI 10.5.4.3: 6GR HARQ related aspect (EOM)	Moderator (OPPO)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.4.3-a006`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.5 Other physical layer signals, channels and procedure

```text
Study the following mechanisms with NR 1-bit SR mechanism as the benchmark for study:
Study the mechanism of transmitting multiple (>1) bits in SR.
Study enhancements of resource allocation and L1-aspect of triggering for SR for 1-bit.
Note: This also applies to multiple bit SR study.
Study the L1-aspects of BS UL pre-scheduling mechanism.
Study the L1-aspects of contention-based BSR transmission.
Study the L1-aspects of BSR transmission in preconfigured PUSCH (contention free).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.5-a001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.5 Other physical layer signals, channels and procedure

```text
Study UE-to-UE CLI handling mechanisms for 6GR:
The studies of UE-to-UE CLI focus on deployment scenarios of dynamic TDD, semi-static SBFD, TDD- semi-static SBFD coexistence, and consider inter-subband, intra-subband and intra-band CLI, both intra-cell CLI and inter-cell CLI.
Study the following UE-to-UE CLI measurement and reporting mechanism, considering at least the following aspects:
Reference signals or/and channels for measuring CLI
Timing misalignment for measurement
Measurement metric
CLI reporting contents.
CLI reporting mechanisms.
Network-controlled reporting.
UE-initiated/Event-triggered CLI reporting.
Study the following UE-to-UE mitigation/suppression mechanisms:
Coordination of time/frequency resource allocation.
Uplink power control to reduce the CLI.
Spatial domain methods to suppress CLI.
Information exchange between BSs for example the configuration of CLI resources, TDD/SBFD configuration.
R1-2603040	FL Summary #3 for 10.5.5	Moderator (OPPO)
From Friday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.5-a002`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.5 Other physical layer signals, channels and procedure

```text
Study BS-to-BS CLI handling mechanisms for 6GR:
The study of BS-to-BS CLI focus on deployment scenarios of dynamic TDD, semi-static SBFD, TDD-semi-static SBFD coexistence. The BS-to-BS CLI can be inter-subband interference, intra-subband interference and co-channel intra-band interference, inter-cell interference.
Study the following BS-to-BS handling mechanisms:
Uplink resource muting mechanism to enable the BS to identify BS-to-BS CLI.
BS-to-BS CLI/channel measurement mechanisms/resources.
Coordinated scheduling
Information exchange between BSs including the configuration of measurement resource, TDD/SBFD configuration, DL beam information CLI measurement results and CLI mitigation request.
Note: this may or may not have RAN1 spec impact.
DL Power allocation-based mechanism.
Spatial domain solution, for example beam nulling, beam paring, restrict/preferred beam.
Note: For any of the above items, the study includes necessity.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.5-a003`

### [6G/Rel-20 RAN1#124b] `agreement` 10.5.5 Other physical layer signals, channels and procedure

```text
Study mechanisms for handling remote interference management (RIM) for 6GR:
The study should consider
Coexist of BSs with same or different TDD configurations for 6GR BS or for 6GR and NR BSs in the same band.
Scenarios with at least one BS configured with SBFD
The remote interference between NR BS and 6GR BS
Note: The upper mid-band operation (around 7GHz) is also considered in the study.
Study the potential workflow and framework for 6GR RIM
The wireless-based and backhaul-based RIM frameworks in NR are considered as the starting point for study.
Aim to minimize unnecessary complexity.
Study the reference signal design for 6GR RIM, at least consider the following aspects:
Take NR RIM RS as starting point or study.
The functions of RIM RS, including how many types of RIM-RS, information indicated and carried in RIM RS, and physical layer design of RIM RS.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.5.5-a004`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.0 General aspects and frameworks

```text
For the 6GR smallest maximum UE bandwidth for at least one lower-tier device, RAN1 to further study the following alternatives:
Alt 1: 20MHz RF and BB bandwidth for both UL and DL with 15kHz SCS for FDD, and with 30kHz SCS for TDD
Alt 2: 5MHz RF and BB bandwidth for FDD with 15kHz SCS for both UL and DL, 10 or 20 MHz RF and BB bandwidth for TDD with 30kHz SCS for both UL and DL
Alt 3: 20MHz RF bandwidth for both UL and DL with 15kHz SCS for FDD, and with 30kHz SCS for TDD
Narrower bandwidth for BB in UL, and/or Narrower bandwidth for BB in DL
R1-2601572	FL summary #2 of General aspects and frameworks	Moderator (Huawei, Xiaomi)
R1-2601573	FL summary #3 of General aspects and frameworks	Moderator (Huawei, Xiaomi)
From Tuesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.0-a001`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.0 General aspects and frameworks

```text
For the RAN1 study of “Re-use of existing 5G mid-band (~3.5 GHz) site grid for 6G deployments in at least around 7 GHz and targeting comparable to same coverage to 5G mid-band”,
For the link budget evaluation for coverage gap identification in around 7 GHz.
For initial access, Rel-15 NR signals/channels during initial access are used for identifying the gap of individual signal/channel compared to Rel-15 NR msg3 in 5G mid-band, respectively.
Note: The candidate coverage enhancement techniques will be separately discussed.
R1-2601574	FL summary #4 of General aspects and frameworks	Moderator (Huawei, Xiaomi)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.0-a002`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.0 General aspects and frameworks

```text
For 6GR spectrum aggregation operation, study the following methods and their associated application scenarios:
Method 1: Multiple physical carriers can be aggregated into single “Gothia cell”.
Note: the term ‘Gothia cell’ is for RAN1 discussion purposes, and whether/how to specify the feature / refer to the feature is separate RAN1 discussion.
Method 2: “Carrier aggregation” where multiple physical carriers can be aggregated into separate cells.
For both methods, study them under idle mode and connected mode, and study their pros and cons at both NW and UE side.
R1-2601715	FL summary #5 of General aspects and frameworks	Moderator (Huawei, Xiaomi)
From Friday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.0-a003`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.0 General aspects and frameworks

```text
For the RAN1 study of “Re-use of existing 5G mid-band (~3.5GHz) site grid for 6G deployments in at least around 7 GHz and targeting comparable coverage to 5G mid-band”, the following assumptions are assumed for link budget template candidates 1 for Msg3 PUSCH in 5G mid-band.
| System configuration |  |
| --- | --- |
| Channel for evaluation | Msg3 PUSCH (TBS 56bits with 10% BLER target) |
| Scenarios and Carrier frequency (GHz) | FFS |
| BS antenna heights (m) | 25m for Urban macro, 35m for sub-urban macro |
| UT antenna heights (m) | TR38.901 UMa Table 7.2-1, SMa Table 7.2-5 |
| Cell area reliability (%) | 90% |
| Lognormal shadow fading std deviation (dB) | 6 or 8 (Refer to the row of Uma/SMa NLOS in Table 7.4.1-1 of TR 38.901 |
| Tx Diversity |  |
| Number of SSB |  |
| Transmitter |  |
| (1) Number of transmit antenna elements | 1 |
| (2) Number of transmit TxRUs Note: this row is void (left empty) for uplink |  |
| (2a) Number of transmit chains modelled in LLS | 1 |
| (3) Total transmit power (dBm) Note: total transmit power for system bandwidth | 23 |
| 3a) System bandwidth for downlink, or occupied bandwidth for uplink (Hz) | 720000 |
| (3b) Power Spectrum Density = (3) - 10 log( (3a) / 1000000 ) (dBm/MHz) Note: no PSD constraint for uplink |  |
| (3c) Bandwidth used for the evaluated channel (Hz) Note: (3c) is identical to the number of PRBs assigned to the channel evaluated. For uplink, (3a) = (3c) |  |
| (3bis) Total transmit power for occupied bandwidth = (3b) + 10 log ((3c) /1000000) (dBm) |  |
| (4) Total antenna gain at antenna gain component 3 & antenna gain component 4 of transmitter = (4a) – (4b) (dB) | 0 |
| (4a) Antenna gain at antenna gain component 3 & antenna gain component 4 of transmitter = (4c) + 10 log ((1) / (2)) (dB) for downlink, and = (4c) + 10 log ((1) / (2a)) (dB) for uplink | 0 |
| (4b) Antenna gain correction factor at antenna gain component 3 & antenna gain component 4 of transmitter (dB) | 0 |
| (4c) Gain of antenna element (dBi) | 0 |
| (5) Total antenna gain at antenna gain component 2 of transmitter = (5a) - (5b) (dB) Note: zero for uplink | 0 |
| (5a) Antenna gain at antenna gain component 2 of transmitter = 10 log((2)/(2a)) (dB) Note: zero for uplink | 0 |
| (5b) Antenna gain correction factor at antenna gain component 2 of transmitter (dB) Note: zero for uplink | 0 |
| (8) Cable, connector, combiner, body losses, etc. (enumerate sources) (dB) (feeder loss must be included for and only for downlink) | 0 |
| (9) EIRP = (3bis) + (4) + (5) – (8) dBm |  |
| Receiver |  |
| (10) Number of receive antenna elements | 192 |
| (10a) Number of receive TxRUs Note: this row is void (empty) for downlink | 64 |
| (10b) Number of receive chains modelled in LLS | Reported by companies |
| (11) Total antenna gain at antenna gain component 3 & antenna gain component 4 of receiver = (11a) - (11b) (dB) |  |
| (11a) Antenna gain at antenna gain component 3 & antenna gain component 4 of receiver = (11c) + 10 log ((10)/(10a)) (dB) for uplink = (11c) + 10 log ((10)/(10b)) (dB) for downlink |  |
| (11b) Antenna gain correction factor at antenna gain component 3 & antenna gain component 4 of receiver (dB) | Reported by companies |
| (11c) Gain of antenna element (dBi) | 8 |
| (11bis) Total antenna gain at antenna gain component 2 of receiver = (11bis-a) - (11bis-b) (dB) Note: zero for downlink |  |
| (11bis-a) Antenna gain at antenna gain component 2 of receiver = 10 log((10a)/(10b)) (dB) Note: zero for downlink |  |
| (11bis-b) Antenna gain correction factor at antenna gain component 2 of receiver (dB) Note: zero for downlink | Reported by companies |
| (12) Cable, connector, combiner, body losses, etc. (enumerate sources) (dB) (feeder loss must be included for and only for uplink) | Reported by companies (same values used for NR midband and ~7GHz) |
| (13) Receiver noise figure (dB) | 5 |
| (14) Thermal noise density (dBm/Hz) | -174 |
| (15) Receiver interference density (dBm/Hz) | FFS |
| (16) Total noise plus interference density = 10 log (10^(( (13) + (14))/10) + 10^((15)/10)) (dBm/Hz) |  |
| (18) Effective noise power = (16) + 10 log ((3c)) (dBm) |  |
| (19) Required SNR (dB) |  |
| (20) Receiver implementation margin (dB) | 2 (same values used for NR midband and ~7GHz) |
| (21) H-ARQ gain (dB) Note: Only applicable if HARQ is not considered in LLS |  |
| (22) Receiver sensitivity = (18) + (19) + (20) – (21) (dBm) |  |
| (22bis) MCL = (3bis) – (22) + (5) + (11bis) (dB) |  |
| (23) Hardware link budget, a.k.a. MIL = (9) + (11) + (11bis) − (12) − (22) (dB) Note: MIL can also be derived by (22bis) + (4) – (8) + (11) − (12) |  |
| Calculation of available pathloss |  |
| (25) Shadow fading margin (function of the cell area reliability and lognormal shadow fading std deviation) (dB) | Calculated by companies with the aforementioned parameters |
| (26) BS selection/macro-diversity gain (dB) | Reported by companies (same values used for NR midband and ~7GHz) |
| (27) Penetration margin (dB) | Value based on High-loss Model [Table 7.4.3-2 in TR 38.901] for Uma Value based on Low-loss A Model [Table 7.4.3-2 in TR 38.901] for SMa |
| (28) Other gains (dB) (if any please specify) | 0 |
| (29) Available path loss = (23) – (25) + (26) – (27) + (28) (dB) |  |
| Range/coverage efficiency calculation |  |
| FFS: (30) Maximum range (based on (29) and according to the system configuration section of the link budget) (m) |  |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.0-a004`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.0 General aspects and frameworks

```text
For the RAN1 study of “Re-use of existing 5G mid-band (~3.5GHz) site grid for 6G deployments in at least around 7 GHz and targeting comparable coverage to 5G mid-band”, the following assumptions are assumed for link budget template candidates 1 for signals/channels in around 7GHz.
| System configuration |  |
| --- | --- |
| Channel for evaluation | Signals/channels during initial access assuming Rel-15 NR design |
| Scenarios and Carrier frequency (GHz) | FFS |
| BS antenna heights (m) | 25m for Urban macro, 35m for sub-urban macro |
| UT antenna heights (m) | TR38.901 UMa Table 7.2-1, SMa Table 7.2-5 |
| Cell area reliability (%) | 95% for control channel, SSB and SIB1, 90% for other data channel can be used as a starting point. |
| Lognormal shadow fading std deviation (dB) | 6/8 (Refer to the row of Uma/SMa NLOS in Table 7.4.1-1 of TR 38.901 |
| Tx Diversity | 0 |
| Number of SSB | 8 |
| Transmitter |  |
| (1) Number of transmit antenna elements | For BS: - Urban: - 768 antenna elements - 1024 antenna elements (optional) - Suburban: - 768 antenna elements - 1024 antenna elements (optional) For UE: - 1 |
| (2) Number of transmit TxRUs Note: this row is void (left empty) for uplink | BS: - 128 TxRUs (for 768 antenna elements) - 256 TxRUs (optional, for 1024 antenna elements) |
| (2a) Number of transmit chains modelled in LLS | Reported by companies |
| (3) Total transmit power (dBm) Note: total transmit power for system bandwidth | 46 dBm per 20 MHz for BS, with total transmit power no larger than 56 dBm (as agreed in RAN1#123 in AI 11.1) 23 dBm, 26dBm for UE |
| (3a) System bandwidth for downlink, or occupied bandwidth for uplink (Hz) | For downlink: System bandwidth: - 200 or 400 MHz For uplink: - Occupied bandwidth is reported by companies (same between NR midband and ~7GHz) |
| (3b) Power Spectrum Density = (3) - 10 log( (3a) / 1000000 ) (dBm/MHz) Note: no PSD constraint for uplink |  |
| (3c) Bandwidth used for the evaluated channel (Hz) Note: (3c) is identical to the number of PRBs assigned to the channel evaluated. For uplink, (3a) = (3c) |  |
| (3bis) Total transmit power for occupied bandwidth = (3b) + 10 log ((3c) /1000000) (dBm) |  |
| (4) Total antenna gain at antenna gain component 3 & antenna gain component 4 of transmitter = (4a) – (4b) (dB) |  |
| (4a) Antenna gain at antenna gain component 3 & antenna gain component 4 of transmitter = (4c) + 10 log ((1) / (2)) (dB) for downlink, and = (4c) + 10 log ((1) / (2a)) (dB) for uplink |  |
| (4b) Antenna gain correction factor at antenna gain component 3 & antenna gain component 4 of transmitter (dB) | Reported by companies |
| (4c) Gain of antenna element (dBi) | For BS: - 8 dBi For UE: - 0 dBi |
| (5) Total antenna gain at antenna gain component 2 of transmitter = (5a) - (5b) (dB) Note: zero for uplink |  |
| (5a) Antenna gain at antenna gain component 2 of transmitter = 10 log((2)/(2a)) (dB) Note: zero for uplink |  |
| (5b) Antenna gain correction factor at antenna gain component 2 of transmitter (dB) Note: zero for uplink | Reported by companies |
| (8) Cable, connector, combiner, body losses, etc. (enumerate sources) (dB) (feeder loss must be included for and only for downlink) | Reported by companies (same values used for NR midband and ~7GHz) |
| (9) EIRP = (3bis) + (4) + (5) – (8) dBm |  |
| Receiver |  |
| (10) Number of receive antenna elements | For BS: - Urban: - 768 antenna elements - 1024 antenna elements (optional) - Suburban: - 768 antenna elements - 1024 antenna elements (optional) For UE: - 4 |
| (10a) Number of receive TxRUs Note: this row is void (empty) for downlink | BS: - 128 TxRUs (for 768 antenna elements) - 256 TxRUs (optional, for 1024 antenna elements) |
| (10b) Number of receive chains modelled in LLS | Reported by companies (same between two carrier frequencies) |
| (11) Total antenna gain at antenna gain component 3 & antenna gain component 4 of receiver = (11a) - (11b) (dB) |  |
| (11a) Antenna gain at antenna gain component 3 & antenna gain component 4 of receiver = (11c) + 10 log ((10)/(10a)) (dB) for uplink = (11c) + 10 log ((10)/(10b)) (dB) for downlink |  |
| (11b) Antenna gain correction factor at antenna gain component 3 & antenna gain component 4 of receiver (dB) | Reported by companies |
| (11c) Gain of antenna element (dBi) | For BS: - 8 dBi For UE: - 0 dBi |
| (11bis) Total antenna gain at antenna gain component 2 of receiver = (11bis-a) - (11bis-b) (dB) Note: zero for downlink |  |
| (11bis-a) Antenna gain at antenna gain component 2 of receiver = 10 log((10a)/(10b)) (dB) Note: zero for downlink |  |
| (11bis-b) Antenna gain correction factor at antenna gain component 2 of receiver (dB) Note: zero for downlink | Reported by companies |
| (12) Cable, connector, combiner, body losses, etc. (enumerate sources) (dB) (feeder loss must be included for and only for uplink) | Reported by companies (same values used for NR midband and ~7GHz) |
| (13) Receiver noise figure (dB) | DL: 9, UL: 5 |
| (14) Thermal noise density (dBm/Hz) | -174 |
| (15) Receiver interference density (dBm/Hz) | FFS |
| (16) Total noise plus interference density = 10 log (10^(( (13) + (14))/10) + 10^((15)/10)) (dBm/Hz) |  |
| (18) Effective noise power = (16) + 10 log ((3c)) (dBm) |  |
| (19) Required SNR (dB) |  |
| (20) Receiver implementation margin (dB) | 2 (same values used for NR midband and ~7GHz) |
| (21) H-ARQ gain (dB) Note: Only applicable if HARQ is not considered in LLS |  |
| (22) Receiver sensitivity = (18) + (19) + (20) – (21) (dBm) |  |
| (22bis) MCL = (3bis) – (22) + (5) + (11bis) (dB) |  |
| (23) Hardware link budget, a.k.a. MIL = (9) + (11) + (11bis) − (12) − (22) (dB) Note: MIL can also be derived by (22bis) + (4) – (8) + (11) − (12) |  |
| Calculation of available pathloss |  |
| (25) Shadow fading margin (function of the cell area reliability and lognormal shadow fading std deviation) (dB) | calculated by companies with the aforementioned parameters |
| (26) BS selection/macro-diversity gain (dB) | Reported by companies (same values used for NR midband and ~7GHz) |
| (27) Penetration margin (dB) | Value based on High-loss Model [Table 7.4.3-2 in TR 38.901] Value based on Low-loss A Model [Table 7.4.3-2 in TR 38.901] for SMa |
| (28) Other gains (dB) (if any please specify) | Reported by companies |
| (29) Available path loss = (23) – (25) + (26) – (27) + (28) (dB) |  |
| Range/coverage efficiency calculation |  |
| FFS: (30) Maximum range (based on (29) and according to the system configuration section of the link budget) (m) |  |
Note: Companies to provide updated link budget results before April 3rd , to be triggered by email thread (March 30th ).
[Post-124-R20-General Aspects-Coverage] – Xinhua (Huawei)
Email discussion for collection of updated link budget results from Marth 30th until April 3rd.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.0-a005`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.0 General aspects and frameworks

```text
6GR shall at least be capable of configuring the same TDD slot configurations as TDD slot configurations deployed in 5G NR.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.0-a006`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.0 General aspects and frameworks

```text
Study link direction determination for dynamic TDD, considering at least
UE PDCCH monitoring efforts and power consumption
Signaling overhead
Scheduling flexibility
Avoid duplicated functionalities
Collision handling
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.0-a007`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.1.1 Synchronization acquisition and beam measurement

```text
For initial access and mobility in 6GR, study the following deployment scenarios
Single beam and multi-beam based deployments
Single TRP and multi-TRP based deployments
Single carrier and multi-carrier deployments
Other deployment scenarios
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.1.1-a001`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.1.1 Synchronization acquisition and beam measurement

```text
For 6GR paging transmission/reception, study at least the following aspects:
Study paging transmission scheme(s) to facilitate network energy savings
Study paging scheme(s) to facilitate UE energy savings
Study necessity of paging capacity enhancement
Study necessity of paging coverage enhancement
R1-2601577	FL summary #3 of Synchronization acquisition and beam measurement	Moderator (Huawei, Xiaomi)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.1.1-a002`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.1.1 Synchronization acquisition and beam measurement

```text
Study 6GR signals, channels and procedures for initial access and idle mobility, considering at least
Cell/Initial Cell search and cell ID identification
Time/frequency synchronization/tracking
Beam measurement
System information acquisition
Whether TRP is transparent/non-transparent to UE during above procedures
R1-2601578	FL summary #4 of Synchronization acquisition and beam measurement	Moderator (Huawei, Xiaomi)
From Friday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.1.1-a003`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.1.1 Synchronization acquisition and beam measurement

```text
For 6GR measurements in initial access and for mobility, study measurement resource, measurement quantity, measurement functionality and measurement procedure, at least including:
L1 measurements
Cell-level/[TRP-level] and beam-level measurement
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.1.1-a004`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.1.1 Synchronization acquisition and beam measurement

```text
Study beam operation during 6GR initial access, including:
Beam acquisition during initial access
Beam report/refinement during initial access
Feasibility and performance of spatial/temporal beam prediction during initial access
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.1.1-a005`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.1.1 Synchronization acquisition and beam measurement

```text
Basic 6GR sync signal structure is defined as 6GR SSB, which consists of primary synchronization signal(s), secondary synchronization signal(s) and physical broadcast channel(s)
FFS: Other types of 6GR sync signal/channel structure or reference signal and their structure
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.1.1-a006`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.1.2 PRACH and RACH procedure

```text
Study random access framework with the following aspects:
Enablement of energy efficient random access procedures (supporting SID objective 1b);
Including both network and UE power saving
Coverage improvement (supporting SID objective 1d);
Support of random access for diverse device types and capabilities (supporting SID objective 1g);
System performance improvement from overhead reduction, simplification of signaling/configurations (supporting SID objective 1k);
Additionally consider following aspects
random access latency;
capacity
detection reliability;
high speed mobility;
Note: Other aspects identified during future discussions are not excluded.
The following scenarios and assumptions beyond single carrier/TRP are considered for the study of above random access framework:
NTN
SBFD
multi-carrier
multi-TRP
Note: whether/how to support one or more of the scenarios/assumptions, including whether any special handling or functionality needs to be introduced in support of the scenarios/assumptions is part of the study.
R1-2601535	Summary #3 of discussion on Random Access and RA Procedures	Moderator (InterDigital, Inc.)
R1-2601536	Summary #4 of discussion on Random Access and RA Procedures	Moderator (InterDigital, Inc.)
From Friday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.1.2-a001`

### [6G/Rel-20 RAN1#124] `working_assumption` 10.5.1.2 PRACH and RACH procedure

```text
Adopt the following link level simulation assumption for random access evaluations:
Link Level Assumption Parameters for Random Access
| Assumptions | Value |
| --- | --- |
| Carrier frequency | Refer to AI 10.1 Select among the following candidates: 700 MHz, 2 GHz, 4 GHz, 7 GHz, 14 GHz, 30 GHz |
| Duplex | Select among the following candidates: FDD, TDD |
| System Bandwidth | 5 MHz, 10 MHz, 100 MHz |
| Numerology | 700 MHz carrier frequency: 15 kHz 2 GHz carrier frequency: 15 kHz [3.5/4] GHz carrier frequency: 30 kHz 7 GHz carrier frequency: [30] kHz [14/15] GHz carrier frequency: FFS 30 GHz carrier frequency: 120 kHz |
| Antenna Configuration at the TRP | Select among the following candidates: For TDL: - 1T1R, 2T2R, 4T4R, FFS: 16T16R, 64T64R For CDL: (M,N,P,Mg,Ng; Mp, Np) - FFS: - 30 GHz: (4,8,2,1,1; 1,2) (dH, dV) = (0.5, 0.5)λ |
| Antenna Configuration at the UE | For TDL: 1T2R, 2T2R, 2T4R For CDL: - FFS: 0.7, 2, [3.5/4], 7 GHz - handheld UT model with 1T2R, 2T2R, 2T4R - FFS: 14 GHz 30 GHz: (M,N,P,Mg,Ng; Mp, Np) = (2,4,2,1,2; 1,2) (dH, dV) = (0.5, 0.5)λ, (dg,H, dg,V) = (0, 0)λ, Θmg,ng = 90°; Ω0,1 = Ω0,0 + 180° - [Modeling of a polarized antenna shall follow Section 7.3.2 in TR 38.901] |
| Channel estimation | Realistic |
| Channel Model | Select among following DS candidates: 10, 30, 100, 300, 1000 ns FFS: other DS values |
| Mobility | Select among the following candidates: 3 km/h, 30km/h, 120 km/h, 500km/h, 1000 km/h |
| RF Impairment modeling | Phase noise (if modeled): Follow the models in R1-165685 Frequency offset (if modeled): - Non-initial acquisition - TRP: uniform distribution +/- 0.05 ppm - UE: uniform distribution +/- 0.1 ppm |
Note: additional parameter tables are evaluation parameters specific to the evaluation of PRACH or Msg 3 that would override the general link level assumption parameters for random access if fields were duplicate
Additional Parameters for PRACH Evaluations
| Carrier Frequency | 700 MHz | 2 GHz | [3.5/4] GHz | 7 GHz | [14/15] GHz | 30 GHz |
| --- | --- | --- | --- | --- | --- | --- |
| Channel Model (baseline, other model usage not precluded) | FFS: TDL-A - DS = 30 ns TDL-C - DS = 100, 300 ns FFS: other models | FFS | TDL-A - DS = 30 ns TDL-C - DS = 100, 300 ns FFS: CDL-C - DS = 100, 300 ns (see Note 1) FFS: other models | TDL-C - DS = 100, 300 ns FFS: CDL-C - DS = 100, 300ns (see Note 1) FFS: other models | FFS | FFS CDL-C - DS = [30] ns (see Note 1) FFS: other models |
| UE speed | 3, 120 km/h, 500 km/h (optional) 30, 1000km/h | FFS | 3 km/h (optional) other values |  |  |  |
| RF Impairments modeling | - TRP: uniform distribution +/- 0.05 ppm - UE: uniform distribution +/- 0.1 ppm |  |  |  |  |  |
| Initial timing Offset | Timing uncertainty derived from cell radius |  |  |  |  |  |
| RO assumption | Number of preambles per RO – 64, 256, 512, 1024 Number of UEs per RO – 1, 2, 4, 8 |  |  |  |  |  |
| PRACH Sequence & Format | Companies to provide detailed information on sequence used (e.g., sequence type, length, CP/GP lengths, SCS, cyclic shift values, repetition, etc). |  |  |  |  |  |
| Target Performance | 0.1% False Alarm 1% miss-detection |  |  |  |  |  |
| NOTE 1: The CDL table is translated so that the strongest cluster’s AoD and AoA occur at a random angle for both the antenna panels of TRP and UE in the local coordinate systems. ZoD and ZoA is assumed to be unchanged. The value of the random angle is selected to be uniformly distributed from +30 to -30 degree. The random value is chosen independently for both AoD and AoA. CDL angle scaling is based on Clause 7.7.5.1 of TR38.901 v19.1.0. |  |  |  |  |  |  |
Additional Parameters for PUSCH of Msg.3
| Parameter | Value |
| --- | --- |
| Frequency hopping | w/ or w/o frequency hopping |
| Number of UE transmit chains | 1, 2 |
| Number of DMRS symbol | w/o frequency hopping: 3, w/ frequency hopping: 2 for each hop |
| Waveform | Company to report |
| HARQ configuration | For eMBB, whether HARQ is adopted is reported by companies. For VoIP, w/ HARQ. The maximum number of HARQ transmission (limited by frame structure and latency requirements) is reported by companies. |
| Msg 3 Repetitions | FFS |
| PUSCH duration | 14 OS |
| Number of PRBs | [2] |
| TBS | [56] bits FFS: other values |
| Other parameters | Reported by companies |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.1.2-w001`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.1.3 Bandwidth operation

```text
For basic initial access procedures considering UEs with different bandwidth capabilities, study the determination of frequency location(s) and bandwidth(s) for UE to receive/monitor the downlink signals/channels during initial access and idle mode for at least the following:
System information
Random access procedure
Paging
FFS: Relation to frequency location of 6G synchronization signals
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.1.3-a001`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.1.3 Bandwidth operation

```text
For basic initial access procedures considering UEs with different bandwidth capabilities, study the determination of the frequency location(s) and bandwidth(s) for UE to transmit uplink signals/channels during initial access and idle mode:
FFS: Relation to the DL frequency location(s) and bandwidth(s) in TDD
FFS: Relation to frequency location of 6G synchronization signals
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.1.3-a002`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.2.1 Downlink transmission scheme(s) for downlink control channels

```text
6G PDCCH study will consider at least the following concepts:
CORESET
CCE
REG as the minimum resource unit
REG bundle
CCE to REG mapping
Search Space
PDCCH candidate and CCE aggregation levels
Blind decoding
DMRS for PDCCH
Hash function
FFS the details of the concepts above.
FFS the relation among CCE, REG, REG bundle, and PDCCH candidates.
R1-2601527	Feature Lead summary #4 on PDCCH Transmission Schemes	Moderator (Nokia)
From Friday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.2.1-a001`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.2.1 Downlink transmission scheme(s) for downlink control channels

```text
For 6G PDCCH study, consider at least the following aspects:
Controlchannel blocking
Coverage
UE energy consumption
UE complexity
Coexistence of different device types
Reliability of PDCCH transmission
NW complexity and scheduling
Resource efficiency and overhead
Latency
MRSS
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.2.1-a002`

### [6G/Rel-20 RAN1#124] `working_assumption` 10.5.2.1 Downlink transmission scheme(s) for downlink control channels

```text
REG consists of multiple REs.
CCE consists of a set of REGs.
PDCCH candidate corresponds to one or multiple CCE(s).
REG bundle consists of a set of REGs.
Final summary in R1-2601528.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.2.1-w001`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
Study the PT-RS for PDSCH including at least the following aspects
The necessity of PT-RS in different bands
R1-2601430	FL Summary #4 on Downlink Transmission Scheme for Downlink Shared Channel	Moderator (Ericsson), Moderator (Google)
R1-2600955	FL Summary #5 on Downlink Transmission Scheme for Downlink Shared Channel	Moderator (Google), Moderator (Ericsson)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.2.2-a001`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
Study PDSCH and RS for PDSCH based on the following SLS EVM assumptions
Note: Additional EVM assumptions for AI/ML based DMRS overhead reduction can be further discussed.
Note: EVM assumption for HST scenarios will be treated separately
| Parameter | Value |
| --- | --- |
| Carrier frequency and duplex | Around 0.7 GHz, FDD Around 2 GHz, FDD Around 4 GHz, TDD Around 7 GHz, TDD Around 30 GHz, TDD |
| Subcarrier spacing | 15 kHz for FDD 30 kHz for TDD and around 2—7 GHz 120 kHz for TDD and around 30 GHz |
| Waveform | CP-OFDM |
| Channel model | TR 38.901 (Rel-19) |
| Scenario | Suburban macro, 1732 m ISD (for around 0.7—4 GHz) Urban macro, 500 m ISD (for around 0.7—30 GHz) Dense urban, 200 m ISD (for around 4—30 GHz) Other scenarios are not precluded (companies to report) |
| Bandwidth | 20 MHz (baseline) 100 MHz (for 4—7 GHz) (optional) Other bandwidths are not precluded (companies to report) |
| Deployment | 7 x 3, single layer, hex grid (baseline) 19 x 3, single layer, hex grid (optional) |
| BS transmit power (for 20 MHz) | For around 0.7—7 GHz 49 dBm for Suburban macro, 1732 m 46 dBm for Urban macro, 500 m 44 dBm for Dense urban, 200 m Note: BS Tx power scales up with bandwidth proportionally under the limitation of the maximum BS Tx power is 56 dBm for outdoor and 33 dBm for indoor for the above carrier frequencies. For around 30 GHz 33 dBm for all scenarios Other BS transmit powers are not precluded (companies to report) |
| BS transmit power constraint | Total transmit power constraint (baseline) Per-TXRU transmit power constraint (optional) |
| BS antenna configuration | Around 0.7 GHz: 4 TXRUs, 32AEs, (M, N, P, Mg, Ng; Mp, Np) = (8, 2, 2, 1, 1; 1, 2), (dH, dV) = (0.5, 0.5), (“Baseline Configuration”) Around 2 GHz: 4 TXRUs, 32 AEs, (M, N, P, Mg, Ng; Mp, Np) = (8, 2, 2, 1, 1; 1, 2), (dH, dV) = (0.5, 0.5), (“Outdoor Combination 1”) 32 TXRUs, 128 AEs, (M, N, P, Mg, Ng; Mp, Np) = (8, 8, 2, 1, 1; 2, 8), (dH, dV) = (0.5, 0.5) 64 TXRUs, 192 AEs, (M, N, P, Mg, Ng; Mp, Np) = (12, 8, 2, 1, 1; 4, 8), (dH, dV) = (0.5, 0.5), (“Outdoor Combination 2”) Around 4 GHz: 4 TXRUs, 32 AEs, (M, N, P, Mg, Ng, Mp, Np) = (8, 2, 2, 1, 1; 1, 2), (dH, dV) = (0.5, 0.8), (“Outdoor Combination 0”) 32 TXRUs, 128 AEs, (M, N, P, Mg, Ng, Mp, Np) = (8, 8, 2, 1 ,1; 2, 8), (dH, dV) = (0.5, 0.8) , (“Indoor Combination 1”) 64 TXRUs, 192AEs, (M, N, P, Mg, Ng; Mp, Np) = (12, 8, 2, 1, 1, 4, 8). (dH, dV) = (0.5, 0.8), (“Outdoor Combination 1”) FFS: Around 7 GHz: 128 TXRUs, 768 AEs, (M, N, P, Mg, Ng, Mp, Np) = (24, 16, 2, 1, 1; 4, 16), (dH, dV) = (0.5, 0.8), (“Outdoor Combination 1”) 256 TXRUs, 1024 AEs, (M, N, P, Mg, Ng, Mp, Np) = (32, 16, 2, 1, 1; 8, 16), (dH, dV) = (0.5, 0.8), (“Outdoor Combination 2”) 512 TXRUs, 2048AEs, (M, N, P, Mg, Ng; Mp, Np) = (64, 16, 2, 1, 1, 16, 16), (dH, dV) = (0.5, 0.5), (“Outdoor Combination 5”) 256 TXRUs, 1536 AEs, (M, N, P, Mg, Ng; Mp, Np) = (48, 16, 2, 1, 1, 8, 16). (dH, dV) = (0.5, 0.8), (“Outdoor Combination 3”) 128 TXRUs, 2048AEs, (M, N, P, Mg, Ng; Mp, Np) = (64, 16, 2, 1, 1, 8, 8), (dH, dV) = (0.5, 0.5) Around 30 GHz 4 TXRUs, 1024 AEs, (M, N, P, Mg, Ng, Mp, Np) = (16, 16, 2, 2, 1; 1, 1), (dH, dV) = (0.5, 0.5) , (“Outdoor Combination 3”) 16 TXRUs, 2048 AEs, (M, N, P, Mg, Ng, Mp, Np) = (16, 8, 2, 4, 2; 1, 1), (dH, dV) = (0.5, 0.5) , (“Outdoor Combination 1”) Other antenna configurations are not precluded (companies to report) |
| BS mechanical/electrical tilt | Mechanical tilt: 90° in GCS Electrical tilt: Company to report Other mechanical tilts are not precluded (companies to report) |
| UE antenna configuration (IoT) | Details follow corresponding agreements in Agenda 10.1 |
| UE antenna configuration (handheld) | Details follow corresponding agreements in Agenda 10.1 |
| FFS: CPE configuration | Details follow corresponding agreements in Agenda 10.1 |
| UE speed (handheld) | Urban macro and dense urban: indoor (3 km/h), outdoor (30km/h) Suburban macro: indoor (3 km/h), outdoor (40km/h) |
| Traffic model | FFS: NFB, FTP 1, 500 kB FFS: NFB, FTP 3, 500 kB FFS: FB and EFTP Other traffic models and packet sizes are not precluded (companies to report) |
| Resource utilization | FFS: 20%, 50%, 70% |
| Number of UEs per cell | FFS: 10 or 30 (for FTP 3) |
| Scheduler | PF |
| MIMO scheme | Reported by companies |
| Receiver | MMSE-IRC (baseline) R-ML (Reported by companies) |
| DMRS channel estimation | Realistic |
| CSI-RS channel estimation | Realistic |
| Inter-cell interference estimation | Realistic |
| Inter-cell interference model | Explicit |
| CSI-RS periodicity | 10 ms (optional) 20 ms (baseline) |
| CSI delay | 4 ms |
| Phase errors for radios with uncalibrated antennas (for 4 TXRUs) | Wideband phase error between Tx antenna port 0 and Tx antenna port () can be modeled as follows: in following two ways: Case 1: Independent random phase offset uniformly distributed between 0 and 2π between any two Tx antenna ports. |
| Backhaul assumption | Ideal backhaul (baseline) Non-ideal backhaul (optional) |
| Performance metric | Throughput Other performance metrics are not precluded (companies to report) |
| Multi-TRP (e.g., CJT) scenario | Reuse AI 10.5.3.1 (DL CSI) as reference and consider potential more TRPs than 3 |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.2.2-a002`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
Study PDSCH and RS for PDSCH based on the following LLS EVM assumptions
Note: Additional EVM assumptions for AI/ML based DMRS overhead reduction can be further discussed.
| Parameter | Value |
| --- | --- |
| Carrier frequency and duplex | Around 0.7 GHz, FDD Around 2 GHz, FDD Around 4 GHz, TDD Around 7 GHz, TDD Around 30 GHz, TDD |
| Subcarrier spacing | 15 kHz for 0.7 and 2 GHz 30 kHz for 4 GHz and 7 GHz 120 kHz for 30 GHz |
| Waveform | CP-OFDM |
| Channel model | CDL-A/C/D in TR 38.901 |
| System bandwidth | 20 MHz 100 MHz Other bandwidths are not precluded (companies to report) |
| PRG size | 2 RBs, 4 RBs and wideband as start point for evaluation Other values are not precluded, and reported by companies |
| Delay spread | 30 ns, 100 ns, 300 ns, 1000 ns (optional) |
| UE speed | 3 km/h, 30 km/h, 120 km/h, 350 km/h, 500 km/h |
| BS antenna configuration | Align with SLS |
| UE antenna configuration | Align with SLS |
| Receiver | MMSE-IRC (baseline) R-ML (Reported by companies) Other receivers are not precluded (companies to report) |
| Channel estimation | Realistic |
| FFS: Channel parameter estimation | Companies to report channel parameter estimation, e.g., delay spread, Doppler spread, delay, SNR, etc. |
| MIMO scheme | Reported by companies |
| MU-MIMO interference model | The assumption of MU-MIMO interference in NR Rel-18 DMRS enhancement can be reused (companies to report which Alt |
| Link adaptation and HARQ | AMC or fixed MCS |
| Phase errors for radios with uncalibrated antennas (for 4 TXRUs) Note: Only for radios with uncalibrated antennas | Wideband phase error between Tx antenna port 0 and Tx antenna port () can be modeled as follows: Independent random phase offset uniformly distributed between 0 and 2π between any two Tx antenna ports. |
| Performance metric | BLER, SE, Throughput Other performance metrics are not precluded (companies to report) |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.2.2-a003`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.2.2 Downlink transmission scheme(s) for downlink shared channels

```text
Study the following options regarding the spec impact on the maximum number of orthogonal DMRS ports for PDSCH
Option 1: Up to 24 orthogonal DMRS ports
Option 2: Up to 32 orthogonal DMRS ports
Option 3: Up to 48 orthogonal DMRS ports
Option 4: Up to 64 orthogonal DMRS ports
Option 5: Up to 96 orthogonal DMRS ports
Study Non-orthogonal DMRS on top of the options above to achieve the target number of MIMO layers (from network side).
Note: To provide link/system level simulation results for this study.
Final summary in R1-2600956.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.2.2-a004`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.2.3 Uplink transmission scheme(s) for uplink channels

```text
If 6GR supports to define uplink control information (UCI) in Layer 1, study how to define the method(s) to convey the UCI over physical channel, at least (but not limited to) the following aspects:
Option 1: Define a UCI dedicated physical channel, i.e., Physical Uplink Control Channel (PUCCH)
Option 2: UCI carried on PUSCH
Option 3: Other method(s)
Note: Whether UCI is carried in L1 or L2 to be discussed in agenda item 10.5.3.1 and 10.5.4.3
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.2.3-a001`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.2.3 Uplink transmission scheme(s) for uplink channels

```text
Support following table as the basic assumption of SLS for evaluation of PUSCH transmission scheme.
Note: Additional EVM assumptions for AI/ML based evaluation can be further discussed.
Parameters
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.2.3-a002`

### [6G/Rel-20 RAN1#124] `proposal` 10.5.2.3 Uplink transmission scheme(s) for uplink channels

```text
#1 Frequency range
Around 0.7 GHz, FDD
Around 2 GHz, FDD
Around 4 GHz, TDD
Around 7 GHz, TDD
Around 30 GHz, TDD
#2 Multiple access
OFDMA
#2-1 waveform
CP-OFDM and DFTS-OFDM
#3 Numerology
15 kHz for FDD
30 kHz for TDD and around 2—7 GHz
120 kHz for TDD and around 30 GHz
#4 Scenario
Suburban macro, 1732 m ISD (for around 0.7—4 GHz)
Urban macro, 500 m ISD (for around 0.7—30 GHz)
Dense urban, 200 m ISD (for around 4—30 GHz)
Urban Macro (500m), one-layer deployment, two-layer deployment (Optional)
Dense urban (200m), one-layer deployment, two-layer deployment (Optional)
Urban Grid (Optional)
Other scenarios are not precluded (companies to report)
#4-1 Deployment
7 x 3, single layer, hex grid (baseline)
7 x 3 two layers, macro layer: hex grid; micro layer: locations of micro sites are reported by company (optional)
19 x 3, single layer, hex grid (optional)
#5 Channel model
TR 38.901
#6 System bandwidth
20 MHz (baseline)
100 MHz (for 4—7 GHz) (optional)
Other bandwidths are not precluded (companies to report)
#7 gNB RX antenna setup and port layouts
(𝑀,𝑁,𝑃,𝑀𝑔,𝑁𝑔,𝑀𝑝,𝑁𝑝)
Reuse SLS assumption for PDSCH (AI 10.5.2.2)
and additional assumption as follows:
Around 4 GHz:
4 TXRUs, 32 AEs, (M, N, P, Mg, Ng, Mp, Np) = (8, 2, 2, 1, 1; 1, 2), (dH, dV) = (0.5, 0.8) (optional)
#8 BS receiver noise figure
Around 7 GHz and below: 5dB
Around 15 GHz and above: 7dB
#9 BS receiver
Baseline: MMSE-IRC
Other can be reported
#10 BS scheduler
Proportional fair
#11 Modulation
Up to 256 QAM
Other can be reported
#12 MIMO scheme
Depending on PUSCH scheme
Reported by company (e.g., SU/MU-MIMO, max rank)
#13 UE speed
Urban macro and dense urban: indoor (3 km/h), outdoor (30km/h)
Suburban macro: indoor (3 km/h), outdoor (40km/h)
additional assumption of 0.3 km/h for FWA
#14 UE TX antenna configuration
Details follow corresponding agreements in Agenda 10.1.
Other antenna location/configuration are not precluded and can be considered.
FFS: CPE configuration
#15 Traffic model (FFS)
#16 Precoder granularity
Company can report
#17 Backhaul assumption
Ideal backhaul (baseline)
Non-ideal backhaul (optional)
#18 Power control
Company can report
#19 UE power class
23dBm, 26dBm[,29dBm]
#20 Metric
Throughput
Additional assumption of average UPT, 5%-tile UPT, 50%-tile UPT, 95%-tile UPT
#21 Impairments
Company can report (according to use case / scenario / scheme)
e.g., UE coherence modeling, Tx power imbalance, relative phase error, DL&UL reciprocity
Note: EVM assumption for HST scenarios will be treated separately
Final summary in R1-2601692.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.2.3-p001`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.2.4 Beam management for downlink and uplink

```text
Study TCI/QCL-related aspects, e.g., definition of QCL/TCI-state, QCL property/chain
On beam management for DL and UL of 6GR, at least the following aspects should be studied:
Beam measurement(prediction)/report/indication within a same TRP, i.e., single-TRP, in a cell/carrier;
Beam measurement(prediction)/report/indication among different TRPs, i.e., multi-TRP, in a cell/carrier;
Beam measurement(prediction)/report/indication among different cells/carrier, i.e., inter-cell/carrier
Note: Both AI/ML and non-AI/ML related mechanism(s) for the above can be further studied.
Note-1: Which multi-TRP transmission scheme for study will be discussed under other agenda.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.2.4-a001`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.2.4 Beam management for downlink and uplink

```text
Study of UE-initiated/event-driven beam management (UEIBM) mechanisms for 6GR, covering at least the following aspects:
Event definition and the corresponding target use case.
UL transmission, UE’s behavior, and procedure for a triggered event, including the necessity and design of the associated network’s response.
Note 1: Both AI/ML and non-AI/ML related mechanism(s) for the above can be further studied.
Note 2: UE-initiated/event-driven CSI reporting is not discussed in this agenda.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.2.4-a002`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.2.4 Beam management for downlink and uplink

```text
Regarding link-level evaluation of 6GR beam management, in RAN1#124b, to use the following template as starting point for collecting related parameters.
| Parameter | Value |
| --- | --- |
| Carrier Frequency |  |
| Duplex / Waveform |  |
| Subcarrier Spacing |  |
| Simulation Bandwidth |  |
| Channel Model |  |
| Delay Spread |  |
| NW Antenna Config |  |
| Multi-TRP operation |  |
| TXRU mapping to antenna elements |  |
| Beam-forming scheme |  |
| Procedure of beam sweeping |  |
| Criteria for beam selection |  |
| UE Antenna Config |  |
| BS array orientation |  |
| UE array orientation |  |
| UE antenna element radiation pattern |  |
| UE Velocity |  |
| MIMO Scheme |  |
| CW-to-layer mapping |  |
| Channel coding |  |
| SSB, CSI-RS configuration for BM |  |
| SRS configuration for BM |  |
| Receiver Type |  |
| Channel Estimation |  |
| MCS |  |
| Performance Metric(s) |  |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.2.4-a003`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.2.4 Beam management for downlink and uplink

```text
Regarding system-level evaluation of 6GR beam management, in RAN1#124b, , to use the following template as starting point for collecting related parameters.
| Parameter | Value |
| --- | --- |
| Scenario (Carrier frequency) |  |
| Mode |  |
| System BW |  |
| Subcarrier spacing for data |  |
| Channel model |  |
| BS Antenna Configuration |  |
| BS array orientation |  |
| TXRU mapping to antenna elements |  |
| Beam-forming scheme |  |
| Procedure of beam sweeping |  |
| Multi-TRP operation |  |
| Criteria for selection for serving TRP(s) |  |
| Criteria for beam selection for serving TRP(s) |  |
| UE Antenna Configuration |  |
| UE array orientation |  |
| Beam correspondence |  |
| Link adaptation |  |
| UE receiver type |  |
| BS Tx Power |  |
| Maximum UE Tx Power |  |
| Inter site distance |  |
| UE antenna element radiation pattern |  |
| UE Speed and UE distribution |  |
| UE rotation |  |
| BS Antenna height |  |
| UE Antenna height |  |
| Car penetration Loss |  |
| Building penetration loss (O2I) |  |
| UE mobility feature (optional) |  |
| Scheduling algorithm |  |
| MCS |  |
| Traffic Model |  |
| CSI Feedback |  |
| Resource Utilization |  |
| Prediction parameter |  |
| UE number/cell |  |
| Layout/deployment |  |
| Inter-cell interference model |  |
| Metric |  |
R1-2601744	Final summary on beam management for DL and UL	Moderators (ZTE, Apple)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.2.4-a004`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
Adopt the following table as the basic assumption of SLS for evaluation of DL-based CSI acquisition.
Table General Assumption
Parameters
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.3.1-a001`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
Adopt the following table as the assumptions for LLS for DL based CSI acquisition.
| Parameters | Value |
| --- | --- |
| #1 Carrier frequency | Around 700MHz (FDD) Around 2 GHz (FDD) Around 4 GHz (TDD) Around 7 GHz (TDD) |
| #2 RB allocation for PDSCH | 24RB, 48RB, others are not precluded |
| #2a Channel BW | Depend on carrier frequency. Companies to report the assumed channel BW. |
| #3 Waveform and numerology for DL | CP-OFDM, 15 kHz for FDD, 30 kHz for others |
| #4 Channel model | CDL-A/B/C/D/E in TR 38.901 Possible DS values = {10, 30, 100, 300, 1000} ns. ASA, ASD, ZSA, ZSD follow the values in sec 7.7.1 in TR 38.901 Companies to report how randomization is performed if considered For time domain CSI prediction, companies to report whether CDL or TDL is used. Note: it does not mean it is mandatory for companies to evaluate time domain CSI prediction in LLS If UL transmission is simulated, companies to report the assumption for UL channel model. |
| #5 UE speed | 3 km/h, 30 km/h, 120km/h, 350km/h, 500km/h |
| #6 PRG | 2 RBs, 4 RBs as start point for evaluation Other values are not precluded |
| #7 BS antenna configuration | Reuse the assumption under AI 10.5.2.2 when applicable, otherwise refer to AI 10.1 |
| #8 UE antenna configuration | Follow agreements in agenda 10.1 |
| #9 MIMO scheme | SU-MIMO, MU-MIMO. |
| #10 Receiver type | MMSE-IRC or rML for DL. MMSE-IRC for UL |
| #11 CW to layer mapping | NR CW to layer mapping (baseline) Other codeword-to-layer mapping options are not precluded |
| #12 Channel coding | LDPC for PDSCH, Polar for CSI (for evaluation benchmark), when applicable |
| #13 MCS | For PDSCH: QPSK (1/5, 1/3), 16QAM (2/5, 1/2, 3/4), 64QAM (1/2, 2/3, 5/6), 256QAM (2/3, 5/6) |
| #14 Channel estimation | Realistic as baseline Companies to report the detailed CSI-RS channel estimation. |
| #15 Link adaptation | AMC/fixed MCS |
| #16 KPIs | Intermediate KPIs: SGCS/NMSE BLER, SE/throughput |
| #17 Other CSI-RS parameters | Specified by proponent, e.g., CDM-group sizes, CDM group layout, PDSCH/CSI-RS multiplexing, etc. |
| #18 Maximum CSI-RS power boosting | 6dB (cf. R1-103331.FFS other values pending RAN4 feedback) |
| #19 CSI-RS periodicity | 10, 20 ms |
| #20 Scheduling delay | Minimum [4ms] from CSI measurement to CSI application Companies to report if other assumptions are used |
| #21 CSI reception | At least for the CSI feedback without channel coding, e.g. JSCM, JSCC related study: Simulate CSI receiver performance with realistic channel/interference+ noise estimation under realistic assumptions. Companies to report the detailed assumptions for UL channel/interference |
| #22 Phase errors for radios with uncalibrated antennas (for 4 TXRUs) | Wideband phase error between Tx antenna port 0 and Tx antenna port () can be modeled: Independent random phase offset uniformly distributed between 0 and 2π between any two Tx antenna ports. |
Note: additional necessary evaluation assumptions for CSI feedback without channel coding, e.g. JSCM, JSCC, are to be discussed separately.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.3.1-a002`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
To evaluate the performance of non-AI/AI based CSI prediction at UE side or NW side, consider
Intermediate metric: Subband/RB-level per layer eigenvector/precoder SGCS, NMSE calculated between predicted channel and ground-truth channel
To compare NW side prediction with UE side prediction, the impact of CSI reporting shall be considered
FFS: other intermediate KPI
System-level metric: UPT (mean, 5%tile), CSI reporting overhead
CSI-RS overhead is considered in UPT calculation
Companies to report how to calculate CSI report overhead and CSI report mechanism
Link-level metric: BLER/SE/throughput
Complexity metrics: FLOPs/M
For AI based prediction: number of parameters/M
Baseline:
Baseline#1: CSI measurement/report based on full CSI-RS ports/density
Baseline#2:
Sample & Hold for frequency domain, companies to report how Sample & Hold is performed
FFS for spatial domain
Other baselines are not precluded
Companies to report sampling ratio and sampling pattern
Definition of sampling ratio and sampling pattern subjects to detailed domain for reduction
FFS calibration error for BS antenna arrays other than 4TXRUs
Companies to report the assumptions for spatial consistency modelling, if applicable
The above is at least applicable to frequency/spatial domain prediction. Companies to report other sub-use case specific parameters, if applicable
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.3.1-a003`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For evaluation of multi-TRP under single layer deployment,
Same antenna configuration and Tx power is assumed across TRPs.
Note: other multi-TRP scenarios are not precluded
Note: TRP assumption for HST scenarios will be treated separately
Table Multi-TRP scenarios
| Multi-TRP Scenario 1: Intra-cell scenario, with 4 TRPs/RRHs per multi-TRP set | Multi-TRP Scenario 2: intra-site, inter-cell, with 3 TRPs per cooperative set (as baseline) | Multi-TRP Scenario 3: Inter/intra-site, inter-cell with TRPs per cooperative set |
| --- | --- | --- |
|  |  | Companies report the setting when N>1 |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.3.1-a004`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
For the study on AI-based CSI compression, the following is considered:
KPI: SGCS (Intermediate), PAPR (when applicable), throughput vs CSI feedback overhead, DL throughput/BLER vs SNR
CSI feedback overhead: the number of UL resource elements
Companies to report values
Note: the overhead of DMRS (if applicable) is reported by company
Model/computation complexity at UE side (when applicable): FLOPs/M
Model/computation complexity at NW side: FLOPs/M
Model size: Number of parameters/M
Overhead of downloadable basis/codebook/matrix for compression (when applicable): size of parameters (Mbytes) and updated frequency
Overhead/complexity/impact of inter-vendor collaboration (when applicable)
Benchmark:
Rel-20 NR SSCC approach with 2-sided model (companies report the inter-vender collaboration assumption) and/or NR eType II feedback and/or NR Type I feedback
Link adaptation is considered
Evaluation assumptions follow general EVM.
For uplink transmission (e.g., UL channel model, UL SNR range, UL channel estimation, UL noise + interference estimation) are reported by companies
Companies to report the considered non-ideal factors, if assumed, e.g., Tx PA nonlinearity & RF impairment, UL/DL channel estimation errors, uplink interference pattern
Companies to report the bitwidth/shape of the modulation constellation
Note: the above assumptions can also apply for non-AI schemes, i.e., without training/inference/data collection/projection, when applicable.
Note: RAN4 related impacts, e.g., EVM, ACLR, SEM, are to be considered
Final summary in R1-2601311.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.3.1-a005`

### [6G/Rel-20 RAN1#124] `proposal` 10.5.3.1 Aspects of downlink-based CSI acquisition

```text
#1
Carrier frequency
Around 700MHz (FDD)
Around 2 GHz (FDD)
Around 4 GHz (TDD)
Around 7 GHz (TDD)
Other carrier frequency is not precluded
#2
Simulation bandwidth
20MHz
100MHz (not applicable for 700MHz)
Other BW is not precluded
System/channel bandwidth assumption is reported by companies.
#3
Number of subbands and subbands size
Number of SBs
1 for WB
13 SB for 20MHz
TBD SB for 100MHz
Subband size:
4 or 8 PRBs for 20MHz
TBD PRBs for 100MHz
Note: Temporary, before subband size for 6GR is decided
Other number can be reported.
#4
Scenario
Note: Reuse SLS assumption for PDSCH
#5
UE number/cell
10, 30 for FTP3
Other numbers is not precluded.
#6
Layout/deployment
1-ring (7*3), 2-ring (19*3)
Other layout/deployment are not precluded.
#7 Channel model
Rel-19 TR 38.901
Note: spatial consistency could be considered, if applicable
#8 Numerology
OFDM, 15 kHz for FDD, 30 kHz for TDD
#9
Transmit power
(per 20MHz)
Dense urban: 44dBm
Urban macro: 46dBm
Suburban Marco:49dBm
Other values can be reported by companies.
Note: For evaluation purpose, BS Tx power scales up with bandwidth proportionally under the limitation of the maximum BS Tx power is 56dBm for outdoor and 33dBmfor indoor for the above carrier frequencies.
#10 BS antenna configuration
Reuse the assumption under AI 10.5.2.2 when applicable, otherwise refer to AI 10.1
#11 UE power class
23dBm, 26dBm[,29dBm]
#12
UE antenna configuration
Details follow corresponding agreements in Agenda 10.1
#13 UE Receiver
MMSE-IRC (baseline)
R-ML (Reported by companies)
#14
Traffic model
FTP Model 1/3 (0.5 Mbyte packet sizes)
Low RU about 30%
Medium RU about 50%
High RU about 70%
Other model is not precluded.
#15
Scheduling
PF
#16
Inter-cell interference model
Explicitly and realistically modelled
#17
Channel estimation assumption
Realistic as the baseline
Companies to report the detailed CSI-RS channel estimation
#18
CSI feedback
CSI periodicity: 10ms, 20ms
Scheduling delay: Minimum [4ms] from CSI measurement to CSI application
Companies to report if other assumptions are used
#19
MIMO scheme
SU-MIMO
MU-MIMO
with rank adaptation
NR CW-to-layer mapping is used and other mapping is not precluded.
#20
Feedback assumption
Companies report UCI reception assumption.
FFS: how to modeling
#21
Evaluation Metric
Throughput and CSI feedback overhead as baseline metrics, the CSI feedback overhead is the actual feedback overhead statistics per system level evaluation
Other KPI is not precluded.
#22
Baseline for performance evaluation
Rel-19 Type I Scheme A/B
Rel-19 eType II Codebook 
Ideal SVD for calibration
[NR AI-CSI compression, when applicable]
#23
Phase errors for radios with uncalibrated antennas (for 4 TXRUs)
Wideband phase error between Tx antenna port 0 and Tx antenna port  () can be modeled:
Independent random phase offset uniformly distributed between 0 and 2π between any two Tx antenna ports.
#24
Calibration error modeling for other antennas
FFS
Note: EVM assumption for HST scenarios will be treated separately
R1-2601310	Feature lead summary #3 on DL-based CSI acquisition	Moderator (Samsung), Moderator (vivo)
From Friday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.3.1-p001`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.3.2 Aspects of uplink-based CSI acquisition

```text
Study at least the following aspects of SRS for uplink and downlink CSI acquisition:
Efficient support of larger channel bandwidth
Capacity enhancements
Coverage enhancements
Efficient resource utilization
Dynamic/flexible adaptation of SRS parameters
mTRP transmission/reception, FWA, HST and other high mobility scenarios
Interference mitigation
Energy efficiency
R1-2601303	Moderator summary#2 on uplink-based CSI acquisition	Moderator (CATT)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.3.2-a001`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.3.2 Aspects of uplink-based CSI acquisition

```text
For UL-based CSI acquisition, study at least the following SRS usages:
CSI acquisition for UL transmission
CSI acquisition for DL transmission
Beam management
Other usages are not precluded
R1-2601304	Moderator summary#3 on uplink-based CSI acquisition	Moderator (CATT)
From Friday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.3.2-a002`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.3.2 Aspects of uplink-based CSI acquisition

```text
Adopt the assumptions in the following table as the basic assumption of SLS for evaluation of UL-based CSI acquisition.
Table: SLS assumption for DL CSI and UL CSI
| Parameters | Assumptions for DL CSI | Assumptions for UL CSI |
| --- | --- | --- |
| #1 Carrier frequency | Reuse SLS assumptions of DL-based CSI(10.5.3.1) Around 700MHz (FDD) Around 2 GHz (FDD) Around 4 GHz (TDD) Around 7 GHz (TDD) Other carrier frequency is not precluded | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Around 0.7 GHz, FDD Around 2 GHz, FDD Around 4 GHz, TDD Around 7 GHz, TDD Around 30 GHz, TDD |
| #2 Simulation bandwidth | Reuse SLS assumptions of DL-based CSI(10.5.3.1) 20MHz 100MHz (not applicable for 700MHz) Other BW is not precluded System/channel bandwidth assumption is reported by companies. | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) 20 MHz (baseline) 100 MHz (for 4—7 GHz) (optional) Other bandwidths are not precluded (companies to report) |
| #3 Precoding granularity | Company report the precoder granularity | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Company can report |
| #4 Scenario | Reuse SLS assumptions of DL-based CSI(10.5.3.1) Note: Reuse SLS assumption for PDSCH | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Suburban macro, 1732 m ISD (for around 0.7—4 GHz) Urban macro, 500 m ISD (for around 0.7—30 GHz) Dense urban, 200 m ISD (for around 4—30 GHz) Urban Macro (500m), one-layer deployment, two-layer deployment (Optional) Dense urban (200m), one-layer deployment, two-layer deployment (Optional) Urban Grid (Optional) Other scenarios are not precluded (companies to report) |
| #5 UE number/cell | Reuse SLS assumptions of DL-based CSI(10.5.3.1) Other numbers is not precluded. | Company to report |
| #6 Layout/deployment | Reuse SLS assumptions of DL-based CSI(10.5.3.1) 1-ring (7*3), 2-ring (19*3) Other layout/deployment are not precluded. | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) 7 x 3, single layer, hex grid (baseline) 7 x 3 two layers, macro layer: hex grid; micro layer: locations of micro sites are reported by company (optional) 19 x 3, single layer, hex grid (optional) |
| #7 Channel model | Reuse SLS assumptions of DL-based CSI(10.5.3.1) Rel-19 TR 38.901 Note: spatial consistency could be considered, if applicable | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) |
| #8 Numerology | Reuse SLS assumptions of DL-based CSI(10.5.3.1) OFDM, 15 kHz for FDD, 30 kHz for TDD | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) 15 kHz for FDD 30 kHz for TDD and around 2—7 GHz 120 kHz for TDD and around 30 GHz |
| #9 Transmit power (per 20MHz) | Reuse SLS assumptions of DL-based CSI(10.5.3.1) Dense urban: 44dBm Urban macro: 46dBm Suburban Marco:49dBm Other values can be reported by companies. Note: For evaluation purpose, BS Tx power scales up with bandwidth proportionally under the limitation of the maximum BS Tx power is 56dBm for outdoor and 33dBmfor indoor for the above carrier frequencies. | NA |
| #10 BS antenna configuration | Reuse the assumption under AI 10.5.3.1 when applicable, otherwise refer to AI 10.1 | Reuse the assumption under AI 10.5.2.3 when applicable, otherwise refer to AI 10.1 |
| #11 UE power class | Reuse SLS assumptions of DL-based CSI(10.5.3.1) 23dBm, 26dBm[,29dBm] | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) 23dBm, 26dBm[,29dBm] |
| #12 UE antenna configuration | Reuse SLS assumptions of DL-based CSI(10.5.3.1) Details follow corresponding agreements in Agenda 10.1 | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Details follow corresponding agreements in Agenda 10.1. Other antenna location/configuration are not precluded and can be considered. |
| #13 UE Receiver | Reuse SLS assumptions of DL-based CSI(10.5.3.1) MMSE-IRC (baseline) R-ML (Reported by companies) | NA |
| gNB receiver | NA | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Baseline: MMSE-IRC Other can be reported |
| #14 Traffic model | Reuse SLS assumptions of DL-based CSI(10.5.3.1) FTP Model 1/3 (0.5 Mbyte packet sizes) Low RU about 30% Medium RU about 50% High RU about 70% Other model is not precluded. | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) |
| #15 Scheduling | Reuse SLS assumptions of DL-based CSI(10.5.3.1) PF | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Proportional fair |
| #16 Inter-cell interference model | Reuse SLS assumptions of DL-based CSI(10.5.3.1) Explicitly and realistically modelled | Explicitly and realistically modelled |
| #17 Channel estimation assumption | Realistic as the baseline Companies to report the detailed SRS channel estimation error model | Realistic as the baseline Companies to report the detailed SRS channel estimation error model |
| #18 SRS periodicity | 5ms, 10ms, 20ms, 40ms, 80ms, 160ms Companies to state the simulated SRS periodicity if other values are used. Note: SRS triggering may be aperiodic Scheduling delay: Minimum [4ms] from CSI measurement to CSI application. | 5ms, 10ms, 20ms, 40ms, 80ms, 160ms Companies to state the simulated SRS periodicity if other values are used. Note: SRS triggering may be aperiodic Scheduling delay: Minimum [4ms] from CSI measurement to CSI application. |
| #19 MIMO scheme | Reuse SLS assumptions of DL-based CSI(10.5.3.1) SU-MIMO MU-MIMO with rank adaptation NR CW-to-layer mapping is used and other mapping is not precluded. | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Depending on PUSCH scheme Reported by company (e.g., SU/MU-MIMO, max rank) |
| #21 Evaluation Metric | DL throughput as baseline metrics Other KPI is not precluded. | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Throughput Additional assumption of average UPT, 5%-tile UPT, 50%-tile UPT, 95%-tile UPT |
| #24 Calibration error modeling for other antennas | Reuse SLS assumptions of DL-based CSI(10.5.3.1) FFS |  |
| #25gNB noise figure | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Around 7 GHz and below: 5dB Around 15 GHz and above: 7dB | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Around 7 GHz and below: 5dB Around 15 GHz and above: 7dB |
| #26UE noise figure | Reuse general assumption |  |
| #27 Impairments | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Company can report (according to use case / scenario / scheme) e.g., UE coherence modeling, Tx power imbalance, relative phase error, DL&UL reciprocity | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Company can report (according to use case / scenario / scheme) e.g., UE coherence modeling, Tx power imbalance, relative phase error, DL&UL reciprocity |
| #28 power control | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Company can report | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Company can report |
| #29 UE speed | Reuse SLS assumptions of downlink transmission schemes(10.5.2.2) | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Urban macro and dense urban: indoor (3 km/h), outdoor (30km/h) Suburban macro: indoor (3 km/h), outdoor (40km/h) additional assumption of 0.3 km/h for FWA |
Note: EVM assumption for HST scenarios will be treated separately
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.3.2-a003`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.3.2 Aspects of uplink-based CSI acquisition

```text
Adopt the assumptions in the following table as the basic assumption of LLS for evaluation of UL-based DL CSI acquisition.
| Parameters | Assumptions for DL CSI |
| --- | --- |
| #1 Carrier frequency | Reuse assumptions of DL-based CSI(10.5.3.1) Around 700MHz (FDD) Around 2 GHz (FDD) Around 4 GHz (TDD) Around 7 GHz (TDD) |
| #2 RB allocation for PDSCH | Reuse assumptions of DL-based CSI(10.5.3.1) 24RB, 48RB, others are not precluded |
| #2a Channel BW | Reuse assumptions of DL-based CSI(10.5.3.1) Depend on carrier frequency. Companies to report the assumed channel BW. |
| #3 Waveform and numerology for DL | Reuse assumptions of DL-based CSI(10.5.3.1) CP-OFDM, 15 kHz for FDD, 30 kHz for others |
| #4 Channel model | Reuse assumptions of DL-based CSI(10.5.3.1) CDL-A/B/C/D/E in TR 38.901 Possible DS values = {10, 30, 100, 300, 1000} ns. ASA, ASD, ZSA, ZSD follow the values in sec 7.7.1 in TR 38.901 Companies to report how randomization is performed if considered |
| #5 UE speed | Reuse assumptions of DL-based CSI(10.5.3.1) 3 km/h, 30 km/h, 120km/h, 350km/h, 500km/h |
| #6 PRG | Reuse assumptions of DL-based CSI(10.5.3.1) 2 RBs, 4 RBs as start point for evaluation Other values are not precluded |
| #7 BS antenna configuration | Reuse assumptions of DL-based CSI(10.5.3.1) |
| #8 UE antenna configuration | Reuse assumptions of DL-based CSI(10.5.3.1) Follow agreements in agenda 10.1 |
| #9 MIMO scheme | Reuse assumptions of DL-based CSI(10.5.3.1) SU-MIMO, MU-MIMO. |
| #10 Receiver type | Reuse assumptions of DL-based CSI(10.5.3.1) MMSE-IRC or RML for DL |
| #11 CW to layer mapping | Reuse assumptions of DL-based CSI(10.5.3.1) NR CW to layer mapping (baseline) Other codeword-to-layer mapping options are not precluded |
| #12 Channel coding | Reuse assumptions of DL-based CSI(10.5.3.1) LDPC for PDSCH, Polar for CSI (for evaluation benchmark), when applicable |
| #13 MCS | Reuse assumptions of DL-based CSI(10.5.3.1) For PDSCH: QPSK (1/5, 1/3), 16QAM (2/5, 1/2, 3/4), 64QAM (1/2, 2/3, 5/6), 256QAM (2/3, 5/6) |
| #14 Channel estimation | Reuse assumptions of DL-based CSI(10.5.3.1) Realistic as baseline Companies to report the detailed SRS channel estimation. |
| #15 Link adaptation | Reuse assumptions of DL-based CSI(10.5.3.1) AMC/fixed MCS |
| #16 KPIs | Reuse assumptions of DL-based CSI(10.5.3.1) Intermediate KPIs: SGCS/NMSE BLER, SE/throughput |
| #19 SRS periodicity | 5ms, 10ms, 20 ms, 40ms, 80ms, 160ms Company to report if other assumptions are used |
| #20 Scheduling delay | Reuse assumptions of DL-based CSI(10.5.3.1) Minimum [4ms] from CSI measurement to CSI application Companies to report if other assumptions are used |
| #23 SNR difference between DL and UL | Company to report the value of SNRDL-SNRUL |
| #24 SRS transmission parameters | Company to report the SRS parameters such as comb, sequence, etc |
| #25 Impairments | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Company can report (according to use case / scenario / scheme) e.g., UE coherence modeling, Tx power imbalance, relative phase error, DL&UL reciprocity |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.3.2-a004`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.3.2 Aspects of uplink-based CSI acquisition

```text
For LLS for UL-based UL CSI acquisition, reuse the LLS assumption for uplink transmission schemes under AI 10.5.2.3.
Final summary in R1-2601729.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.3.2-a005`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.3.3 Other aspects

```text
Adopt the following simulation assumptions for tracking RS evaluation
Table 1: LLS assumptions for T/F tracking
| Parameter | Value |
| --- | --- |
| Duplex, Waveform | FDD and TDD, CP-OFDM |
| Carrier Frequency/SCS | 700MHz/15kHz, 4GHz/30kHz, 7GHz/30kHz, 30GHz/120kHz |
| Number of TRPs | NTRP=1, 2, 4 Companies should report the transmission assumptions for the RS transmission for tracking in case of more than 1 TRP. |
| Bandwidth for PDSCH | 5MHz, 20MHz, 100MHz, bandwidth for tracking RS can be reported by companies |
| MIMO scheme | SU-MIMO, Rank 1,2,3,4 |
| Modulation | QPSK, 16QAM, 64QAM, 256QAM and 1024QAM |
| Precoding granularity | PRG = wideband, other value(TBD) |
| Channel Model | CDL channel in TR38.901 For CDL-C for 4, 7 and 30 GHz - with combination of ASA and ASD scaling values in sec. 7.7.5.1 in TR 38.901, for above 6 GHz cases - ZSA = 5°, ZSD = 1° The CDL table is translated so that the strongest cluster’s AoD and AoA occur at a random angle for both the antenna panels of TRP and UE in the local coordinate. The value of the random angle is selected to be uniformly distributed from +30 to -30 degree. The random value is chosen independently for both AoD and AoA. In mTRP cases, the channel is generated per TRP. |
| Delay spread | 30ns, 100ns, 300ns, 1000ns |
| UE speed | 3km/h, 10km/h, 120km/h, 350km/h 500km/h |
| Initial time offset (TO) | 1/X CP, X= 8 Other values can be reported by companies. |
| CFO | Initial acquisition TRP: uniform distribution +/- 0.05 ppm UE: uniform distribution +/- 5, 10, 20ppm (each company to choose one) Non-initial acquisition Per TRP: uniform distribution +/- 0.05 ppm UE: uniform distribution [+/- 0.1] ppm Note 1: Those parameters are used for simulation assumptions for synchronization signals/channels in NR (TR38.802). Note 2: Other values can be reported by companies. |
| Drift rate | 0.2 ppm/sec Other values can be reported by companies. |
| BS antenna configuration | Around 700MHz carrier frequency 4TXRUs/32AEs: (M,N,P,Mg,Ng; Mp, Np)= (8, 2, 2, 1, 1, 1, 2), (dH,dV) = (0.5, 0.5)λ Around 4GHz carrier frequency 32TXRUs/128AEs: (M, N, P, Mg, Ng; Mp, Np) = (8,8,2,1,1,2,8). (dH, dV) = (0.5, 0.5)λ Around 7GHz carrier frequency 128 TXRUs/728AEs: (M, N, P, Mg, Ng, Mp, Np) = (24,16,2, 1, 1, 4,16). (dH,dV) = (0.5,0.8)λ Around 30GHz carrier frequency 8TXRUs / 512AEs: (M, N, P, Mg, Ng, Mp, Np) = (8, 8, 2, 2, 2; 1, 1), (dH,dV) = (0.5, 0.5)λ |
| UE antenna configuration | Follow the agreement in 10.1. |
| Channel estimation | Realistic channel estimation. Companies can report the CE methods. |
| Performance metric | Estimation error (e.g., CFO/Dopler rmse), BLER, Throughput |
R1-2601465	FL summary #3 on other aspects of CSI acquisition and report	Moderator (Lenovo)
From Friday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.3.3-a001`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.3.3 Other aspects

```text
For joint DL and UL based DL CSI acquisition, reuse the evaluation methodology for LLS and SLS agreed in DL CSI / UL CSI agendas.
Note: Specific necessary aspects on joint operation will be discussed.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.3.3-a002`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.3.3 Other aspects

```text
Study joint DL and UL based CSI acquisition in TDD system.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.3.3-a003`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.3.3 Other aspects

```text
Study and evaluate at least the following aspects on RS for finer time/frequency tracking for both connected and idle modes
Frequency domain factors
Bandwidth
Frequency domain density
Time domain factors
Time domain behavior: e.g., periodic, semi-persistent, aperiodic, on-demand
Time domain density: e.g., periodicity, number of slots, number of symbols and interval between symbols in a slot, etc.
Spatial domain factors
FFS: Details
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.3.3-a004`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.3.3 Other aspects

```text
Considering at least the following aspects for the tracking RS design for finer time/frequency tracking
Set 1 (KPI):
Tracking performance
Overhead
Energy efficiency for NW&UE
UE-side complexity
Accuracy of QCL parameter(s) estimation
R1-2601736	Final summary on other aspects of CSI acquisition and report	Moderator (Lenovo)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.3.3-a005`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.4.1 Downlink control channel, scheduling for downlink and uplink transmission

```text
RAN1 to study what functions are indicated by DCI for 6GR.
RAN1 to study how functions are indicated by DCI for 6GR.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.4.1-a001`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.4.1 Downlink control channel, scheduling for downlink and uplink transmission

```text
Study the adaptation of PDCCH monitoring in 6GR for UE energy efficiency purpose, considering at least:
Impact on network energy efficiency, as well as complexity and performance
UE energy saving gain
Note: 6GR DL WUS related discussions are handled in AI 10.6.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.4.1-a002`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.4.1 Downlink control channel, scheduling for downlink and uplink transmission

```text
Study single-stage and two-stage DCI.
R1-2601584	FL summary#3 for downlink control and DL/UL scheduling	Moderator (CMCC, Apple)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.4.1-a003`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.4.1 Downlink control channel, scheduling for downlink and uplink transmission

```text
RAN1 to study L1 signalling framework for time-domain scheduling/resource allocation for downlink and uplink transmission by considering, e.g., within a slot or across the slot boundary, PXSCH repetitions, and other necessary aspects if any.
Note1: PXSCH corresponds to PDSCH or PUSCH.
Note2: It doesn’t mean those examples are confirmed.
Note3: The descriptions/figures for scheduling options in [R1-2601584, FL summary] is an example for information.
R1-2601727	FL final summary for downlink control and DL/UL scheduling	Moderator (CMCC, Apple)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.4.1-a004`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.4.3 HARQ related Aspects

```text
In 6GR, DL and UL HARQ operation designs considers at least the following aspects:
latency
reliability
coverage
power saving (NW and UE)
NW complexity
UE complexity
diverse services/applications/traffics
R1-2601542	FL summary #3 for AI 10.5.4.3: 6GR HARQ related aspects	Moderator (OPPO)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.4.3-a001`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.4.3 HARQ related Aspects

```text
In 6GR, DL and UL HARQ operation designs considers at least the following aspects:
latency
reliability
coverage
power saving (NW and UE)
NW complexity
UE complexity
diverse services/applications/traffics
system efficiency/system throughput/user throughput
feedback efficiency/UL and DL overhead
Note: the design of DL and UL HARQ does not necessarily be the same.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.4.3-a002`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.4.3 HARQ related Aspects

```text
For DL HARQ in 6GR, study both following HARQ-ACK feedback mechanisms
Mechanism 1: HARQ-ACK information bits are transmitted via L1 signalling
Mechanism 2: HARQ-ACK information bits are transmitted via higher layer signalling (e.g., MAC CE)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.4.3-a003`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.4.3 HARQ related Aspects

```text
For discussion purposes,
Asynchronous HARQ refers to that retransmission(s) occurs in a non pre-determined occasion once the corresponding initial transmission is scheduled.
Adaptive HARQ refers that the transmission parameters and resources for the retransmission can be adaptively adjusted.
For DL and UL in 6GR, support asynchronous and adaptive HARQ operation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.4.3-a004`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.4.3 HARQ related Aspects

```text
Study possible HARQ-ACK payload size range.
R1-2601716	FL summary #4 for AI 10.5.4.3: 6GR HARQ related aspects	Moderator (OPPO)
From Friday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.4.3-a005`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.4.3 HARQ related Aspects

```text
In 6GR, support at least TB level granularity for HARQ-ACK feedback.
R1-2601543	FL summary for AI 10.5.4.3: 6GR HARQ related aspect (EOM)	Moderator (OPPO)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.4.3-a006`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.5 Other physical layer signals, channels and procedure

```text
Study the UE-to-UE cross-link interference for 6GR:
Study and identify the applicable scenarios of UE-to-UE cross-link interference.
Study the characteristics of UE-to-UE cross-link interference, for example what is the potential interference signal level, what is the potential impact on system operation.
Study the mechanisms and techniques for handling UE-to-UE cross-link interference, including UE-to-UE cross-link interference measurement and reporting
For each candidate mechanism, evaluate and analyze the performance benefit, impact to the system and complexity at BS/UE.
Study the candidate resource or signals/channels for measuring UE-to-UE cross-link interference.
Study and identify the candidate measurement quantities.
Study the reporting mechanisms
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.5-a001`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.5 Other physical layer signals, channels and procedure

```text
Study BS-to-BS cross-link interference for 6GR:
Study and identify the applicable scenarios of BS-to-BS cross-link interference.
Study the characteristics of BS-to-BS cross-link interference, for example what is the potential interference signal level, what is the potential impact to the system operation.
Study the mechanisms and techniques that can handle the BS-to-BS cross-link interference, including the mechanisms for measuring and identifying the BS-to-BS cross-link interference:
For each considered mechanism, evaluate the performance benefit, impact to the system operation, and complexity at BS/UE.
The candidate resource for measuring BS-to-BS cross-link interference.
The measurement quantities at least for evaluation purpose.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.5-a002`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.5 Other physical layer signals, channels and procedure

```text
For handling remote interference in 6GR:
Study the applicable scenarios for remote interference between remote cells due to atmospheric ducting;
Study the impact of remote interference to the system, including the impact to the uplink reception.
Study the characteristics of the remote interference.
Study the candidate mechanisms for measuring/detecting/identifying remote interference, mechanisms to mitigate remote interference.
For each candidate mechanism, evaluate the benefits and impact to the system.
Note: UE reporting to request uplink resource scheduling is to be discussed under this agenda.
R1-2601448	FL Summary #2 for 10.5.5	Moderator (OPPO)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.5-a003`

### [6G/Rel-20 RAN1#124] `agreement` 10.5.5 Other physical layer signals, channels and procedure

```text
Study the UE reporting mechanism for requesting uplink resource with considering at least the following aspects:
Applicable use cases, at least including requesting resource for UL data transmission
UL transmission latency
Signalling overhead
UL resource efficiency
System capacity
Network/UE complexity
Other aspects are not precluded
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.5.5-a004`

