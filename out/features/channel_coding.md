# 6GR 信道编码与调制

**当前进展** · 阶段：收敛中

6GR 已明确以 NR 等概率均匀 QAM 为至少支持基础，并进一步限定了 DL、UL 及 DFT-s-OFDM 的调制范围。超出 NR 范围的 LDPC 扩展已收窄部分码块、基图和矩阵结构选项，但若干参数及设计仍待确定；大载荷 Polar 码与小载荷 UCI 编码也在评估中。PS/GS 的性能、复杂度和存储权衡已有评估要求与部分结果，但是否支持 constellation shaping 尚无共识。FWA 场景的 DL 4K QAM 和 UL 1K QAM 获得了 SLS 评估，结果因场景与条件而异；RAN1 建议 UL 1K QAM，对 DL 4K QAM 尚未达成共识。

**未决问题**

- LDPC 扩展的最终 BG 结构、lifting size 及若干矩阵参数仍待选择或确定。
- 是否需要超出 NR 范围的 UCI 载荷，以及大载荷 Polar segmentation 设计仍待确认。
- 3~11 bits 小载荷 UCI 的编码方案尚待比较，5G RM code 的适用性存在不同意见。
- 是否支持 constellation shaping，以及若支持时选择 PS 还是 GS，尚无共识；计划在 Q3 决定。
- DL 4K QAM 是否采用尚无共识；UL 1K QAM 的 SLS 收益受场景、EVM、MPR、负载和 rank 等因素影响。
- PS/GS 的复杂度、存储、时延与性能权衡，以及规范和功能链影响仍需进一步评估。

## 6GR 演进

### [6G/Rel-20 RAN1#126] `agreement` 10.3.1 Channel coding

BG3 的子矩阵 E 支持选项 E2：下三角矩阵中，度数大于 1 的列数少于 I。I 的取值仍为 FFS，且 E 不能是单位矩阵（选项 E1）。

```text
For the sub-matrix E of BG3, support the following option
Option E2 (from agreement in RAN1#124bis): A lower triangular matrix, wherein the number of columns with degree larger than 1 is less than I.
FFS: the value of I.
E can not be the identity matrix (i.e. Option E1).
R1-2606774	FL summary#4 for 6G channel coding	Moderator (ZTE)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.3.1-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.3.1 Channel coding

除 UE 在其支持的任何频段中最大 UL channel bandwidth 不超过 20MHz 外，支持 BG3 in UL 对 UE 为强制要求，并需进行 capability signaling。对上述 UE，BG3 in UL 为可选；是否需要其他例外由 RAN plenary 决定。

```text
With respect to the decision for capability of BG3 in UL tasked by RANP, the following is supported:
supporting BG3 in UL is mandatory with capability signaling for UEs except for UEs with up to 20MHz maximum UL channel bandwidth in any band supported by UE, i.e., BG3 in UL is optional for UEs with up to 20MHz maximum UL channel bandwidth in any band supported by UE.
Note: Whether any additional exception to the above is needed is up to RAN plenary decision.
R1-2606775	FL summary#5 for 6G channel coding	Moderator (ZTE)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.3.1-a002`

### [6G/Rel-20 RAN1#126] `agreement` 10.3.1 Channel coding

针对 payload size 为 3~11 bits 的 small UCI 编码候选评估，采用 AWGN channel，并报告目标 BLER 下的 SNR、BER，以及收发机复杂度和时延影响。候选包括 5G RM code、Enhanced RM code、Enhanced PC-Polar code、Golay-based code、Vertical and horizontal code、CRC polynomial code；公司可选择一个或多个候选并与 5G RM code 比较。

```text
For the evaluation of coding based candidates for small UCI with payload size of 3~11 bits, refer to the evaluation assumptions in PUCCH/PUSCH, with the following update
Use AWGN channel
Note: Companies can provide results for other channels
Info. block length (bits w/o CRC): 3:1:11
Metrics: SNR at target BLER, BER
Other metrics agreed in PUCCH agenda can be also reported by companies
Companies to report the details of PUSCH/PUCCH including DM-RS configuration, PUCCH format, if any
Companies to report impact on receiver complexity/latency and transmitter complexity/latency, if any.
| The channel coding based candidates for evaluation are as below |
| --- |
5G RM code (baseline)
Enhanced RM code
Enhanced PC-Polar code
Golay-based code
Vertical and horizontal code
CRC polynomial code
Note: Companies to report the details of coding based candidates
Note: Companies to provide comparison with 5G RM code.
Note: Companies can choose one or more candidates above for evaluation
R1-2606915 	FL summary#6 for 6G channel coding	Moderator (ZTE)
Final post-meeting summary for this agenda item.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.3.1-a003`

### [6G/Rel-20 RAN1#126] `observation` 10.3.1 Channel coding

公司贡献指出，5G RM code 在高码率下可能出现 rank deficiency、error floor 或性能下降；同时有意见认为 small UCI 通常采用低码率，且 5G RM code 可复用。贡献还提出 Enhanced RM code、Enhanced PC-Polar code、Vertical and horizontal code、CRC polynomial code、Golay-based code 等提升候选。

```text
For the study of 5G RM code for small UCI with 3~11 bits, the following are observed based on companies’ contributions:
11 sources (R1-2605455, R1-2605560, R1-2605655, R1-2605714, R1-2605783, R1-2606019, R1-2606283, R1-2606307, R1-2606308, R1-2606371, R1-2606638) observed that 5G RM code suffers from error floor and performance degradation at high code rates (e.g., R>=1/2) due to rank deficiency or limited minimum Hamming distance
On the other hand, the following are also observed:
2 sources (R1-2605288, R1-2606793) observed small UCI with 3~11 bits is generally scheduled with low code rates.
1 source (R1-2605821) observed that the rank-deficiency cases occur in approximately 6.7% of all the valid (E, K) configurations and have negligible impact on system performance.
5 sources (R1-2605288, R1-2605455, R1-2605560, R1-2605714, R1-2605783) observed that the mother code length of 5G RM code is limited to 32. Furthermore, 4 sources (R1-2605288, R1-2605455, R1-2605560, R1-2605783) observed repetition is needed at low code rates, thus the performance and coverage is degraded.  1 source (R1-2605288) observed small UCI with 3~11 bits is generally scheduled with low code rates.
4 sources (R1-2605455, R1-2605560, R1-2606308, R1-2606371) observed the BLER performance loss of 5G RM code due to DMRS overhead at least for PUCCH.
2 sources (R1-2605455, R1-2605560) observed the performance loss of 5G RM code due to high PAPR at least for PUCCH.
3 sources (R1-2605455, R1-2605560, R1-2605909) observed 5G RM code cannot support DMRS-less transmission at least for PUCCH due to the all-one vector in the first column.
In addition, the following are also observed:
4 sources (R1-2605821, R1-2606793, R1-2606769, R1-2605379) observed that RM code was used in 5G NR, and 6G does not have new requirements for this region to justify re-design.
1 source (R1-2605379) observed that 5G RM code is optimized for good minimum distance and can be decoded via FHT-based ML decoding with low complexity.
The potential solutions (coding based only) to enhance performance for small UCI with 3~11 bits are summarized as below
12 sources (R1-2605560, R1-2605655, R1-2605714, R1-2605783, R1-2605909, R1-2606793, R1-2606283, R1-2606307, R1-2606308, R1-2606371, R1-2606638, R1-2606019) discussed the potential solutions to improve the performance for short block code.
Enhanced RM code
8 sources (R1-2605560, R1-2605655, R1-2605714, R1-2605783, R1-2606793, R1-2606371, R1-2606638, R1-2606019) observed enhanced RM code with optimized basis sequence selection and/or rate matching can resolve the rank deficiency and error floor issue of RM code at high code rates.
1 source (R1-2605783) observed enhanced RM code can provide 0.7dB and 1.4dB performance gain under the case of K=3 and 4 at medium code rate respectively, resolve error floor or provide 0.7~1.2dB performance gain under the case of K=6~8 and 11 at higher code rate.
1 source (R1-2605714) observed that enhanced RM code by introducing row permutation in the basis RM sequence selection can resolve error floor under the cases of K=6~9 and 11 at higher code rate, and provide 0.52~0.57 dB performance gain under the cases of {E=12, K=6, 7} and {E=14, K=7}.
1 source (R1-2606371) observed applying an interleaver before rate matching for 5G RM code can fix the rank deficiency problem, and provide 0.1~0.9dB, 0.1~0.4dB and 0.1~0.2dB performance gain for K = 3~11, E = 12, 16 and 24, respectively.
1 source (R1-2606019) observed Kerdock code, which contains the first-order RM code, can provide 0.11dB mean performance gain, 2.62dB maximum performance gain across all combinations of (K, E).
1 source (R1-2606793) observed extension of RM code (n*32, K), n=2 or 4 can provide up to 0.6 dB performance gain in AWGN for n=4 over 5G RM code (32, K) with repetition.
1 source (R1-2605909) observed that RM (32,13) code agreed in RAN1 #52bis can provide 11 base sequences, excluding the base sequence of all-1’s.
Enhanced PC-Polar code
5 sources (R1-2605288, R1-2605560, R1-2605714, R1-2605783, R1-2605909) observed that enhanced PC-Polar code can resolve the rank deficiency and error floor issue of 5G RM code at high code rates, and improve the performance at low code rates
1 source (R1-2605909) observed about 0.7dB gain from enhanced PC-Polar code for K=8 bits and E=256 bits.
1 source (R1-2605288) observed enhanced PC-Polar code can improve the BLER performance by [0.6~0.9] dB and increase coverage by >10% over 5G RM code at low code rates, and also observed enhanced PC-Polar code can provide the benefits of error detection via parity check bits and unequal error protection for important bits.
vertical and horizontal code
1 source (R1-2606308) observed vertical and horizontal code can provide about 0.4 dB performance gain for K=8, E=12, and about 2 dB performance gain for K=8, E=26.
New code derived from linear block codes or orthogonal subspaces
1 source (R1-2606283) observed by constructing the short block length codes using sequences or using generator polynomial, the minimum hamming distance can be increased.
CRC polynomial code
1 source (R1-2606307) observed CRC polynomial code can provide better BLER performance than 5G RM code for K=6, E=8, and K=7, E=10.
Golay-based code
1 source (R1-2606371) observed Golay-based code can provide 0.1~1.0dB, 0.2~0.6dB, 0.1~0.4dB, 0.1~0.4dB and 0.2~0.3dB performance gain for K = 3~11, E= 12, 16, 20, 24 and 32, respectively.
On the other hand, 5 sources (R1-2605379, R1-2605821, R1-2606793, R1-2606769, R1-2606494) suggested reusing 5G RM code for small UCI with 3~11 bits, e.g., to avoid optimization for high coding rates that are atypical for normal usage.
2 sources (R1-2605821, R1-2605379) observed that the rank-deficiency (E, K) issue can be resolved by the scheduler through allocating a marginally larger number of coded bits without specification change.
R1-2606773	FL summary#3 for 6G channel coding	Moderator (ZTE)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.3.1-o001`

### [6G/Rel-20 RAN1#126] `conclusion` 10.3.2 Modulation, Joint channel coding and modulation

RAN1 将继续研究 GS（1D-NUC）及 PS（ESS-based PS、ECC-based PS），并在 Q3 决定是否支持 constellation shaping；如支持，将在 PS（含 1-bit 或 2-bits）与 GS 之间选择。DL 与 UL 不支持采用不同的 constellation shaping scheme；若 Q3/26 未达成共识，相关研究将停止。

```text
RAN1 to continue the study on GS (i.e. 1D-NUC) and PS (ESS based PS and ECC based PS in Q3/26
decide by Q3 whether or not to support constellation shaping and if supported, between PS (including whether it is 1-bit or 2-bits PS scheme) and GS
support of different constellation shaping schemes for DL and UL is precluded (e.g. PS for DL, GS for UL)
If there is no consensus on the support of constellation shaping in Q3/26 the study on constellation shaping will be stopped
Summary of companies’ preferences:
GS (1D-NUC with equal probability and Gray mapping) — support for both DL and UL
Support shaping AND support this scheme (11): Ericsson, NTT DOCOMO, LG Electronics, SJTU, ETRI, ZTE, Vivo, CATT, OPPO, Verizon, Lenovo
Do NOT support shaping but support this scheme (0): none
Support shaping but do NOT support this scheme (13): IDC, MTK, Intel, Samsung, Qualcomm, HFCL, Jio Platforms, IIT Kanpur, IIT Madras, CEWiT, Lekha Wireless, Charter, CableLabs
PS (ESS based PS) – 1 bit — support for both DL and UL
Support shaping AND support this scheme (18): Tejas, IDC, MTK, Intel, Samsung, OPPO, Verizon, Qualcomm, HFCL, Jio Platforms, IIT Kanpur, IIT Madras, CEWiT, Lekha Wireless, Charter, CableLabs, T-Mob USA, DeepSig
Do NOT support shaping but support this scheme (0): none
Support shaping but do NOT support this scheme (7): Ericsson, NTT DOCOMO, LG Electronics, SJTU, ETRI, ZTE, CATT
PS (ECC based PS) – 1 bit — support for both DL and UL
Support shaping AND support this scheme (11): IDC, MTK, Samsung, Verizon, Qualcomm, HFCL, Jio Platforms, Charter, CableLabs, T-Mob USA, DeepSig
Do NOT support shaping but support this scheme (0): none
Support shaping but do NOT support this scheme (13): Ericsson, NTT DOCOMO, LG Electronics, SJTU, Intel, ETRI, ZTE, CATT, OPPO, IIT Kanpur, IIT Madras, CEWiT, Lekha Wireless
PS (ESS based PS) – 2 bits — support for both DL and UL
Support shaping AND support this scheme (15): Tejas, IDC, MTK, OPPO, Qualcomm, HFCL, Jio Platforms, IIT Kanpur, IIT Madras, CEWiT, Lekha Wireless, Charter, CableLabs, T-Mob USA, DeepSig
Do NOT support shaping but support this scheme (0): none
Support shaping but do NOT support this scheme (10): Ericsson, NTT DOCOMO, LG Electronics, SJTU, Intel, ETRI, ZTE, Samsung, CATT, Verizon
PS (ECC based PS) – 2 bits — support for both DL and UL
Support shaping AND support this scheme (9): IDC, MTK, Qualcomm, HFCL, Jio Platforms, Charter, CableLabs, T-Mob USA, DeepSig
Do NOT support shaping but support this scheme (0): none
Support shaping but do NOT support this scheme (15): Ericsson, NTT DOCOMO, LG Electronics, SJTU, Intel, ETRI, ZTE, Samsung, CATT, OPPO, Verizon, IIT Kanpur, IIT Madras, CEWiT, Lekha Wireless
GS (1D-NUC with equal probability and Gray mapping) — support for only for UL
Support shaping AND support this scheme (12): Ericsson, NTT DOCOMO, LG Electronics, SJTU, Intel, ETRI, ZTE, Vivo, CATT, OPPO, Verizon, Lenovo
Do NOT support shaping but support this scheme (0): none
Support shaping but do NOT support this scheme (9): IDC, MTK, Samsung, HFCL, Jio Platforms, IIT Kanpur, IIT Madras, CEWiT, Lekha Wireless
PS (ESS based PS) – 1 bit — support for only for UL
Support shaping AND support this scheme (17): Tejas, IDC, MTK, Intel, OPPO, Verizon, Qualcomm, HFCL, Jio Platforms, IIT Kanpur, IIT Madras, CEWiT, Lekha Wireless, Charter, CableLabs, T-Mob USA, DeepSig
Do NOT support shaping but support this scheme (0): none
Support shaping but do NOT support this scheme (8): Ericsson, NTT DOCOMO, LG Electronics, SJTU, ETRI, ZTE, Samsung, CATT
PS (ECC based PS) – 1 bit — support for only for UL
Support shaping AND support this scheme (9): IDC, MTK, Qualcomm, HFCL, Jio Platforms, Charter, CableLabs, T-Mob USA, DeepSig
Do NOT support shaping but support this scheme (0): none
Support shaping but do NOT support this scheme (15): Ericsson, NTT DOCOMO, LG Electronics, SJTU, Intel, ETRI, ZTE, Samsung, CATT, OPPO, Verizon, IIT Kanpur, IIT Madras, CEWiT, Lekha Wireless
PS (ESS based PS) – 2 bits — support for only for UL
Support shaping AND support this scheme (15): Tejas, IDC, MTK, OPPO, Qualcomm, HFCL, Jio Platforms, IIT Kanpur, IIT Madras, CEWiT, Lekha Wireless, Charter, CableLabs, T-Mob USA, DeepSig
Do NOT support shaping but support this scheme (0): none
Support shaping but do NOT support this scheme (10): Ericsson, NTT DOCOMO, LG Electronics, SJTU, Intel, ETRI, ZTE, Samsung, CATT, Verizon
PS (ECC based PS) – 2 bits — support for only for UL
Support shaping AND support this scheme (9): IDC, MTK, Qualcomm, HFCL, Jio Platforms, Charter, CableLabs, T-Mob USA, DeepSig
Do NOT support shaping but support this scheme (0): none
Support shaping but do NOT support this scheme (15): Ericsson, NTT DOCOMO, LG Electronics, SJTU, Intel, ETRI, ZTE, Samsung, CATT, OPPO, Verizon, IIT Kanpur, IIT Madras, CEWiT, Lekha Wireless
GS (1D-NUC with equal probability and Gray mapping) — support for only for DL
Support shaping AND support this scheme (6): NTT DOCOMO, LG Electronics, ETRI, ZTE, CATT, Lenovo
Do NOT support shaping but support this scheme (1): Nokia
Support shaping but do NOT support this scheme (15): IDC, Ericsson, MTK, SJTU, Intel, Samsung, OPPO, Verizon, Qualcomm, HFCL, Jio Platforms, IIT Kanpur, IIT Madras, CEWiT, Lekha Wireless
PS (ESS based PS) – 1 bit — support for only for DL
Support shaping AND support this scheme (18): Tejas, IDC, MTK, Intel, Samsung, OPPO, Verizon, Qualcomm, HFCL, Jio Platforms, IIT Kanpur, IIT Madras, CEWiT, Lekha Wireless, Charter, CableLabs, T-Mob USA, DeepSig
Do NOT support shaping but support this scheme (0): none
Support shaping but do NOT support this scheme (7): Ericsson, NTT DOCOMO, LG Electronics, SJTU, ETRI, ZTE, CATT
PS (ECC based PS) – 1 bit — support for only for DL
Support shaping AND support this scheme (10): IDC, MTK, Samsung, Qualcomm, HFCL, Jio Platforms, Charter, CableLabs, T-Mob USA, DeepSig
Do NOT support shaping but support this scheme (0): none
Support shaping but do NOT support this scheme (14): Ericsson, NTT DOCOMO, LG Electronics, SJTU, Intel, ETRI, ZTE, CATT, OPPO, Verizon, IIT Kanpur, IIT Madras, CEWiT, Lekha Wireless
PS (ESS based PS) – 2 bits — support for only for DL
Support shaping AND support this scheme (15): Tejas, IDC, MTK, OPPO, Qualcomm, HFCL, Jio Platforms, IIT Kanpur, IIT Madras, CEWiT, Lekha Wireless, Charter, CableLabs, T-Mob USA, DeepSig
Do NOT support shaping but support this scheme (0): none
Support shaping but do NOT support this scheme (10): Ericsson, NTT DOCOMO, LG Electronics, SJTU, Intel, ETRI, ZTE, Samsung, CATT, Verizon
PS (ECC based PS) – 2 bits — support for only for DL
Support shaping AND support this scheme (9): IDC, MTK, Qualcomm, HFCL, Jio Platforms, Charter, CableLabs, T-Mob USA, DeepSig
Do NOT support shaping but support this scheme (0): none
Support shaping but do NOT support this scheme (15): Ericsson, NTT DOCOMO, LG Electronics, SJTU, Intel, ETRI, ZTE, Samsung, CATT, OPPO, Verizon, IIT Kanpur, IIT Madras, CEWiT, Lekha Wireless
Do not support constellation shaping (23): Nokia, Apple, China Telecom, Xiaomi, Panasonic, Vodafone, Deutsche Telekom, Orange, Telecom Italia, Bouygues Telecom, Spreadtrum, HONOR, Huawei, HiSilicon, Ericsson, BT, CU, Futurewei, PCL, NTT DOCOMO, ZTE, 1Finity, NERCDTV
R1-2606732	FL summary #4 on AI 10.3.2 modulation, joint channel coding and modulation, Moderator (Qualcomm)	Qualcomm Incorporated
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.3.2-c001`

### [6G/Rel-20 RAN1#126] `conclusion` 10.3.2 Modulation, Joint channel coding and modulation

该条目指出 RANP 要求 RAN1 就 constellation shaping 的支持作出结论，未包含进一步的结论内容。

```text
With respect to RANP task to RAN1 (copied below) to conclude the support for constellation shaping in RAN1:
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.3.2-c002`

### [6G/Rel-20 RAN1#126] `conclusion` 10.3.2 Modulation, Joint channel coding and modulation

RAN1 对 DL 或 UL 支持任何 constellation shaping scheme 均未达成共识。部分方案的支持者表示愿意撤回相应方案。

```text
RAN1 to continue the study on GS (i.e. 1D-NUC) and PS (ESS based PS and ECC based PS in Q3/26
decide by Q3 whether or not to support constellation shaping and if supported, between PS (including whether it is 1-bit or 2-bits PS scheme) and GS
support of different constellation shaping schemes for DL and UL is precluded (e.g. PS for DL, GS for UL)
If there is no consensus on the support of constellation shaping in Q3/26 the study on constellation shaping will be stopped
RAN1 concludes the following:
There is no consensus in RAN1 to support any constellation shaping schemes for either DL or UL.
Summary of companies’ preferences is in R1-2606762.
Some proponents of some constellation shaping schemes stated that they would agree to withdraw that scheme.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.3.2-c003`

### [6G/Rel-20 RAN1#126] `conclusion` 10.3.2 Modulation, Joint channel coding and modulation

若在 6GR 中支持 DL 4K QAM 和 UL 1K QAM，其适用范围限于 FWA use case，不适用于 eMBB，且该限制须在规范中落实。RAN1 建议采用 UL 1K QAM；对 DL 4K QAM 是否采用未达成共识。

```text
With respect to RANP guidance to RAN1 (copied below) for support of higher order modulation:
| RAN Chair guidance (RAN#112) For 1K QAM on UL and 4K QAM on DL: RAN1/RAN4 to continue study and make decision in Q3/26. |
| --- |
From RAN1 perspective, for DL 4K QAM, and UL 1K QAM in 6GR, if supported, is restricted to FWA use case only and not for eMBB use case
The restriction to FWA use case shall be enforced in the spec
FFS: How to reflect this restriction in the spec
Other restrictions on DL 4K QAM and UL 1K QAM can be identified
Multiple sources performed SLS to evaluate DL 4K QAM and UL 1K QAM under agreed evaluation methodology for FWA use case. The detailed assumptions and results are captured in the tables provided in R1-2606762.
From RAN1 perspective,
RAN1 recommends to adopt 1k QAM for UL.
No consensus in RAN1 to recommend adopting 4K QAM for DL
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.3.2-c004`

### [6G/Rel-20 RAN1#126] `observation` 10.3.2 Modulation, Joint channel coding and modulation

原文仅引出相对于 RAN#112 结论的观察，未提供具体观察或决定。

```text
With respect to the conclusion from RAN#112 (copied below), the following observations are made:
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.3.2-o001`

### [6G/Rel-20 RAN1#126] `observation` 10.3.2 Modulation, Joint channel coding and modulation

提供了 UL 1K QAM 的 SLS 评估结果，其中部分结果符合 RAN4 推荐的 EVM/MPR，部分不符合。结果显示不同场景和配置下的 UPT 增益不一；多项评估指出，在户外 CPE 等情形可见增益，而 MPR、EVM、负载及 rank 会影响收益。

```text
For UL 1K QAM SLS performance summary, the following evaluation results are provided:
Evaluations comply with RAN4 recommended EVM/MPR
| Company | Config / Scheme | UE Profile | Carrier / BW / SCS | Antenna config (BS / UE), UE Tx power & max rank | Traffic model / load (RU) | EVM (Tx+Rx) | MPR assumed (1024QAM / 256QAM baseline) | Mean / Avg. UPT Gain | Other reported gain metrics | Beneficial UE Ratio | Key Observation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Qualcomm | UMa, FWA outdoor, max rank-2, 3.5 GHz, CP-OFDM | 100% outdoor CPE | 3.5 GHz / 20 MHz / 30 kHz | BS 32 TxRU; UE 4 ports, 28 dBm (alpha = 0.9); max rank 2 | FTP3, target ~20% RU | 2.5%+2.5% | 7.5 / 6.5 dB (CP-OFDM); delta 1.0 dB | Mean UPT: +17% | 95%-tile +25.4%; mean 133.60 -> 156.30 Mbps, 95%-tile 181.78 -> 228.06 Mbps | High (outdoor CPEs) | Gains driven by outdoor CPEs with LoS |
| Qualcomm | UMa, FWA outdoor, max rank-4, 3.5 GHz, CP-OFDM | 100% outdoor CPE | 3.5 GHz / 20 MHz / 30 kHz | BS 32 TxRU; UE 4 ports, 28 dBm (alpha = 0.9); max rank 4 | FTP3, target ~20% RU | 2.5%+2.5% | 7.5 / 6.5 dB (CP-OFDM); delta 1.0 dB | Mean UPT: +5% | 95%-tile +6.5%; mean 169.78 -> 178.31 Mbps, 95%-tile 260.17 -> 277.13 Mbps | Moderate | Rank-4 reduces per-stream SNR |
| Qualcomm | UMa, FWA outdoor, max rank-2, 3.5 GHz, CP-OFDM; UE 2Tx, UE Tx power sweep | 100% outdoor CPE | 3.5 GHz / 20 MHz / 30 kHz | BS 32 TxRU; UE 2 ports, 28 / 26 / 24 / 22 dBm (alpha = 0.9); max rank 2; SVD precoding, SU-MIMO / PF | FTP3, target ~20% RU | 2.5%+2.5% (1024QAM); 3.5%+2.5% (256QAM baseline) | 7.5 / 6.5 dB (CP-OFDM); delta 1.0 dB | Mean UPT: +9.8 / +9.2 / +8.4 / +7.6% at 28 / 26 / 24 / 22 dBm | 95%-tile +17.9 / +17.3 / +16.6 / +15.7% at 28 / 26 / 24 / 22 dBm; at 28 dBm mean 131.59 -> 144.54 Mbps, 95%-tile 180.98 -> 213.52 Mbps [note 6] | High (outdoor CPEs) | Gain is retained down to 22 dBm UE Tx power; 2Tx gain is smaller than 4Tx because of the reduced beamforming gain |
|  |  |  |  |  |  |  |  |  |  |  |  |
| Ericsson | Dense Urban (UMi), 8T UE, maxRank 2 SU-MIMO; 1024QAM vs. 256QAM MCS table | 100% outdoor UEs | 4 GHz / 20 MHz (51 RB) / 30 kHz | BS 64 ports, 44 dBm/20 MHz; UE 8 ports, 31 dBm; maxRank 2 SU-MIMO | FTP model 1; Dense Urban, 21 cells, 200 UEs, ISD 200 m | 2.5%+2.5% | Yes, value n/s [note 1] | Mean UPT: +11.5% / +5.82% / −6.77% at RU = 20 / 50 / 70% (Dense Urban) | RU 20/50/70%: 5%-tile +6.14 / -3.77 / -17.5%; 50%-tile +6.4 / +7.63 / -11.39%; 95%-tile +18.6 / +12.8 / +4.41% (peak gain retained at all loads). Same config w/o EVM: mean +27.7 / +34.0 / +44.9% | ~10–30% outdoor UEs | Higher EVM can degrade at high load |
| MediaTek | UMa, FR1 (4 GHz) / FR3 (7 GHz), SU-MIMO up to rank 4 | Mixed indoor/outdoor and 100% outdoor CPE | 4 GHz and 7 GHz / 100 MHz / 30 kHz | BS 64 TXRU @4 GHz / 256 TXRU @7 GHz, 51 dBm/100 MHz; UE 4Tx/8Rx, 31 dBm (mixed) / 31 or 35 dBm (100% OD); SU-MIMO up to 4 layers | FTP3 with RU = 30%; 10 UEs/sector, ISD 500 m | 2.5%+2.5% | 9 dB @31 dBm / 10 dB @35 dBm (CP-OFDM); 256QAM n/s [note 3] | −0.47% to −2.21% (negative avg. gain) | Beneficial UE only: up to +4% (vs. system average -0.47 to -1.16%); beneficial UE ratio up to 5%; 31 -> 35 dBm gives negligible improvement (interference-limited); rank-4 >75% of scheduling | Up to 5% | MPR severely limits gain; avg. system gain negative |
| MediaTek | UMi, FR1 (4 GHz) / FR3 (7 GHz), SU-MIMO up to rank 4 | Mixed indoor/outdoor and 100% outdoor CPE | 4 GHz and 7 GHz / 100 MHz / 30 kHz | BS 64 TXRU @4 GHz / 256 TXRU @7 GHz, 51 dBm/100 MHz; UE 4Tx/8Rx, 31 dBm (mixed) / 31 or 35 dBm (100% OD); SU-MIMO up to 4 layers | FTP3 with RU = 30%; 10 UEs/sector, ISD 200 m | 2.5%+2.5% | 9 dB @31 dBm / 10 dB @35 dBm (CP-OFDM); 256QAM n/s [note 3] | −2.21% (negative avg. gain) | Beneficial UE only: up to +3% @4 GHz, +4.3% @7 GHz (vs. system average -0.36 to -2.21%); beneficial UE ratio up to 2.4% @4 GHz / 14.3% @7 GHz; 31 -> 35 dBm raises ratio only 11% -> 12% | Up to 2.4% (4GHz), 14% (7GHz UMi) | 7GHz UMi shows higher beneficial UE ratio but still negative avg. |
| Apple | UMa, FWA (UL config not provided) [note 5] | Mixed indoor / outdoor CPE | Not provided for UL [note 5] | Not provided for UL [note 5] | Not provided for UL [note 5] | 2.5%+2.5% | None (no UL SLS) [note 5] | Positive for outdoor CPE; 1024QAM rarely used by indoor UE [note 5] | Not reported for UL [note 5] | Low (indoor), moderate (outdoor) | Rank-2 preferred over rank-4 for 1024QAM |
| vivo | UMa and Dense Urban, FWA, max rank-2, 4 GHz, CP-OFDM and DFT-s-OFDM, MU-MIMO | Mixed indoor / outdoor CPE | 4 GHz / 20 MHz / 30 kHz | BS 64 TxRU; UE 2T, 31 dBm; max rank 2; MU-MIMO | FTP3, low / medium / high load | 2.5%+2%;2.5%+2.5%;3%+2.3% | 5 dB DFT-s / 8 dB CP-OFDM; 256QAM 4.5 / 6.5 dB; delta 0.5 / 1.5 dB [note 4] | Positive: +5.38%~+11.92% for DFT-s-OFDM, +3.48%~+11.49% for CP-OFDM | Annex (RAN1#125-endorsed, with EVM without MPR): UMa 4 GHz rank-2 +19.89 / +14.12 / +12.66% (low / med / high load); Dense Urban +20.33 / +18.87 / +14.32% | Moderate | DFT-s-OFDM gains higher than CP-OFDM due to lower MPR |
| vivo | UMa and Dense Urban, FWA, max rank-2, 7 GHz, CP-OFDM and DFT-s-OFDM, MU-MIMO | Mixed indoor / outdoor CPE | 7 GHz / 100 MHz / 30 kHz | BS 256 TxRU; UE 2T, 31 dBm; max rank 2; MU-MIMO | FTP3, low / medium / high load | 2.8% + 2.3; 2.8%+2.8%; 3% + 2.5% | 5 dB DFT-s / 8 dB CP-OFDM; 256QAM 4.5 / 6.5 dB; delta 0.5 / 1.5 dB [note 4] | Negative or near-zero: -3.1%~+1.75% for DFT-s-OFDM, -5.08%~-1.14% for CP-OFDM | Annex (RAN1#125-endorsed, with EVM without MPR): UMa 7 GHz rank-2 +4.31 / +7.65 / +1.43% (low / med / high load); Dense Urban +3.75 / +1.00 / +2.10% | Low | 4GHz gains larger than 7GHz due to same UL power with different bandwidth |
| vivo | UMa and Dense Urban, FWA, max rank-4, CP-OFDM, 4 GHz and 7 GHz, MU-MIMO | Mixed indoor / outdoor CPE | 4 GHz / 20 MHz and 7 GHz / 100 MHz / 30 kHz | BS 64 TxRU @4 GHz / 256 TxRU @7 GHz; UE 4T, 31 dBm; max rank 4 | FTP3, low / medium / high load | 2.8% + 2.3; 2.8%+2.8%; 3% + 2.5% for 7GHz, 2.5%+2%;2.5%+2.5%;3%+2.3% for 4GHz | 8 dB CP-OFDM; 256QAM 6.5 dB; delta 1.5 dB [note 4] | Negative or near-zero: -2.32~+1.53% for 4GHz; -3.49%~+0.27% for 7GHz | Annex (RAN1#125-endorsed, with EVM without MPR): UMa 4 GHz rank-4 -5.22 / -8.09 / -1.32% (low / med / high load); Dense Urban -1.88 / -1.93 / -1.62%; UMa 7 GHz rank-4 +2.99 / -2.36 / +3.91% (low / med / high load); Dense Urban +3.50 / -2.86 / -4.94% | Very low | CP-OFDM MPR (8 dB) eliminates most gain, max Rank4 shows less gain than max Rank2 |
| Huawei, HiSilicon | Dense Urban (3D-UMa), TDD, MU-MIMO; 1024QAM vs. 256QAM MCS table | Profile 1: 80% indoor / 20% outdoor CPE | 4 GHz / 100 MHz / SCS30kHz | BS 64 TxRU @25 m, MMSE-IRC; UE 2 ports, 31 dBm; MU-MIMO; max rank 4 | Burst buffer, PF, 10 UE/sector; RU 30% | 2.5%+2.5% (1024QAM); 3.5%+2.5% (256QAM baseline) | Yes, Align with RAN4 LS | Mean UPT: -0.98% | 1024QAM scheduling prob. 0.17%; loss attributed to removal of low-SE MCS entries when the 1024QAM entries are added (coarser SE granularity at lower modulation orders) | scheduling prob. 0.17% | Obs 4: average UPT loss (0.98%) in Profile 1, scheduling prob. small. Prop 3: do not consider UL 1024QAM in 6GR (R1-2605289 / R1-2606786) |
| Huawei, HiSilicon | Dense Urban (3D-UMa), TDD, MU-MIMO; 1024QAM vs. 256QAM MCS table | Profile 3: 100% outdoor CPE | 4 GHz / 100 MHz / SCS30kHz | BS 64 TxRU @25 m, MMSE-IRC; UE 2 ports, 31 dBm; MU-MIMO; max rank 4 | Burst buffer, PF, 10 UE/sector; RU 30% | 2.5%+2.5% (1024QAM); 3.5%+2.5% (256QAM baseline) | Yes, Align with RAN4 LS | Mean UPT: +2.56% | 1024QAM scheduling prob. only 6% even in the 100%-outdoor case | scheduling prob. only 6% | Obs 5: only +2.56% in the 100%-outdoor case, which Huawei regards as an idealised assumption (R1-2605289 / R1-2606786) |
| ZTE/Sanechips | UMa, maxRank 4 SU-MIMO; 1024QAM vs. 256QAM MCS table | 80% indoor / 20% outdoor | 4 GHz / 100 MHz / 30 kHz | BS 64 TxRU, 49 dBm; UE 8 ports, 23 dBm; maxRank 4 SU-MIMO | FTP3, 0.5 MB; 21 cells, 5-20 UE/cell, ISD 500 m; RU n/s | 2.5% + 2.5% | 6.8 dB | +35 Mbps / +16% avg. gain (1024QAM MCS table vs. 256QAM MCS table) | ~+35 Mbps (~+16%); 1024QAM scheduling prob. ~20% for indoor UE; rank-4 scheduling reduced ~5% for indoor UE | ~20% (indoor UEs) | Scheduling probability of 1024QAM ~20% even for indoor UEs |
Evaluations not comply with RAN4 recommended EVM/MPR
| Qualcomm | UMa, FWA outdoor, max rank-2, 3.5 GHz, CP-OFDM | 100% outdoor CPE | 3.5 GHz / 20 MHz / 30 kHz | BS 32 TxRU; UE 4 ports, 28 dBm (alpha = 0.9); max rank 2 | FTP3, target ~20% RU | 0%+0% (Ideal: no EVM/MPR) | No (no MPR, no EVM) | Mean UPT: +28% | 95%-tile +30.5%; mean 136.07 -> 174.50 Mbps, 95%-tile 182.51 -> 238.22 Mbps | High | Upper bound without impairments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Qualcomm | UMa, FWA outdoor, max rank-4, 3.5 GHz, CP-OFDM | 100% outdoor CPE | 3.5 GHz / 20 MHz / 30 kHz | BS 32 TxRU; UE 4 ports, 28 dBm (alpha = 0.9); max rank 4 | FTP3, target ~20% RU | 0%+0% (Ideal: no EVM/MPR) | No (no MPR, no EVM) | Mean UPT: +8.5% | 95%-tile +12.7%; mean 180.00 -> 195.42 Mbps, 95%-tile 270.19 -> 304.58 Mbps | Moderate |  |
| Qualcomm | UMa, FWA outdoor, max rank-2, 3.5 GHz, CP-OFDM; UE 2Tx, UE Tx power sweep | 100% outdoor CPE | 3.5 GHz / 20 MHz / 30 kHz | BS 32 TxRU; UE 2 ports, 28 / 26 / 24 / 22 dBm (alpha = 0.9); max rank 2; SVD precoding, SU-MIMO / PF | FTP3, target ~20% RU | 0%+0% (no EVM/MPR) | No (no MPR, no EVM) | Mean UPT: +26.6 / +25.4 / +23.9 / +22.1% at 28 / 26 / 24 / 22 dBm | 95%-tile +30.0 / +29.7 / +29.1 / +28.5% at 28 / 26 / 24 / 22 dBm; at 28 dBm mean 135.76 -> 171.89 Mbps, 95%-tile 182.45 -> 237.26 Mbps [note 6] | High | Upper bound without impairments; the 95%-tile gain stays ~28-30% across all four UE Tx power levels |
| Ericsson | Dense Urban (UMi), 8T UE, maxRank 2 SU-MIMO; 1024QAM vs. 256QAM MCS table | 100% outdoor UEs | 4 GHz / 20 MHz (51 RB) / 30 kHz | BS 64 ports, 44 dBm/20 MHz; UE 8 ports, 31 dBm; maxRank 2 SU-MIMO | FTP model 1; Dense Urban, 21 cells, 200 UEs, ISD 200 m | 2.5%+1.0% | Yes, value n/s [note 1] | Mean UPT: +14.0% / +11.6% / +6.29% at RU = 20 / 50 / 70% (Dense Urban) | RU 20/50/70%: 5%-tile +11.0 / +6.19 / +5.51%; 50%-tile +11.6 / +12.4 / +4.97%; 95%-tile +18.62 / +15.54 / +10.6%. Same config w/o EVM: mean +27.7 / +34.0 / +44.9%. 1024QAM selected 10-30% of outdoor UE (~30% UMi, ~10% UMa), >90% of those at rank 2 | ~10–30% outdoor UEs | 1024QAM rarely selected for indoor UEs |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.3.2-o002`

### [6G/Rel-20 RAN1#126] `observation` 10.3.2 Modulation, Joint channel coding and modulation

提供了 DL 4K QAM 的 SLS 评估结果，分别报告符合和不符合 RAN4 推荐 EVM 的评估。结果显示增益依场景、负载、rank 和 impairment model 而异；多项评估报告平均增益很小或为负，也有评估在 FWA 户外 CPE 或特定条件下报告正增益。

```text
For DL 4K QAM SLS performance summary, the following evaluation results are provided:
Evaluations comply with RAN4 recommended EVM (R4-2607375: txEVM + rxEVM for DL 4096QAM = 1.5% + 1.5% or 1.8% + 1.8% for 4 GHz; 1.5% + 1.5%, 1.8% + 1.8% or 2% + 2% for 7 GHz)
| Company | Config / Scheme | UE Profile | Carrier / BW / SCS | Antenna config (BS / UE), BS Tx power & max rank | Traffic model / load (RU) | EVM (Tx+Rx) (4096QAM / 1024QAM baseline aligned with NR minimum requirement unless otherwise stated) | Impairment / power back-off model | Mean / Avg. throughput (UPT) gain | Other reported gain metrics | 4096QAM scheduling prob. / beneficial UE ratio | Key Observation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ericsson | UMa FWA, max rank 4, SU-MIMO; experimental 4096QAM MCS table vs. NR 1024QAM MCS table | Indoor CPE and outdoor CPE (LOS / NLOS), reported separately and jointly | 4 GHz / BW not stated / 30 kHz | BS 64T (64T8R), MMSE-based channel estimation and practical sync; UE 8R; max rank 4 | Results reported vs. load; gains only visible at low load | 1.5% + 1.5% (4096QAM); 1024QAM baseline n/s | Flat additive EVM applied as independent AWGN per antenna element | Almost no gain over NR 1024QAM for most CPEs; slight degradation of average throughput for some outdoor CPEs | Figures only, no numeric values (Fig. 11-13): scheduler frequently selects higher rank; 4096QAM selected more often only for LOS outdoor CPE | LOS outdoor CPEs only (no numeric ratio given) | Obs 8: DL 4096-QAM offers system level gains primarily for LOS outdoor CPEs, not for macro deployments in general (R1-2606808) |
| Ericsson | UMa FWA, max rank 2 (same setup, rank restricted); 4096QAM MCS table vs. NR 1024QAM MCS table | Indoor CPE and outdoor CPE (LOS / NLOS) | 4 GHz / BW not stated / 30 kHz | BS 64T (64T8R); UE 8R; max rank 2 | Low load emphasised (gain disappears at higher load) | 1.5% + 1.5% (4096QAM); 1024QAM baseline n/s | Flat additive EVM per antenna element | Positive but limited gain, mainly at low load and for outdoor CPEs (Fig. 14; values not stated numerically) | Rank restriction to 2 increases 4096QAM opportunities vs. max rank 4 (less inter-layer interference) | LOS outdoor CPEs | Supports Proposal 3: support uniform 4096QAM in DL as optional feature for at least FWA |
| Ericsson | UMa FWA, max rank 2, impairment-model comparison (4 configurations) | Indoor CPE and outdoor CPE (LOS / NLOS) | 4 GHz / BW not stated / 30 kHz | BS 64T (64T8R); UE 8R; max rank 2 | Same as above | (1) no impairment; (2) 1.5% + 1.5% additive; (3) phase noise with equivalent e2e EVM 1.57%; (4) PA non-linearity with 14.8 dB backoff (~1.5% Tx EVM) + 1.5% Rx EVM | Additive EVM / phase noise / PA non-linearity (signal-dependent) | Gain strongly reduced under PA non-linearity compared with additive EVM or phase-noise models (Fig. 15; values not stated numerically) | Spatial processing partly suppresses additive EVM and phase noise; signal-aligned PA distortion is not suppressed | n/a | Obs 9: impairment impact depends on spatial characteristics, not only on the EVM value |
| ZTE / Sanechips | Dense Urban and UMa, adaptive rank up to maxRank 8 SU-MIMO (no MU-MIMO); candidate 4096QAM MCS table vs. NR 1024QAM MCS table | Profile 1 (mixed): 80% indoor CPE / 20% outdoor rooftop CPE | 4 GHz / 100 MHz system BW / 30 kHz | BS 64 TxRU [16,8,2,1,1;4,8], 49 dBm, 10 deg tilt; UE 8 ports [1,4,2,1,1;1,4]; NR Type I precoding; LMMSE; max rank 8 (adaptive) | FTP3, packet size 0.5 MB; 21 cells, 500 m ISD, 5-20 UEs/cell; RU not stated | 4096QAM: 1.5% + 1.5%, 1.8% + 1.8%, 2% + 2%; 1024QAM baseline: 2.5% + 2.5% (4 GHz) | EVM only (no power back-off modelled) | +3.45% (+10 Mbps) average DL throughput of 4096QAM MCS table over 1024QAM MCS table | UPT with the 4096QAM MCS table is lower than with the 1024QAM MCS table over ~97% of the CDF range; rank-4 scheduling probability reduced by ~5% for indoor UEs; indoor UEs dominate DL throughput | 4096QAM scheduling probability only 4% for indoor UEs | Obs 9/10 + Proposal 2: applicable scenarios limited (high SNR and stringent EVM); do not support DL 4096QAM (R1-2606856) |
| MediaTek | R19 UMa, SU-MIMO up to 4 layers, FR1 (4 GHz) and FR3 (7 GHz); up-to-4096QAM vs. up-to-1024QAM baseline | Mixed CPE (80% indoor / 20% outdoor) and 100% outdoor CPE | 4 GHz and 7 GHz / 100 MHz / 30 kHz | BS 64 TXRU @4 GHz (256 elements) / 256 TXRU @7 GHz (1024 elements), 51 dBm per 100 MHz; UE 4Tx / 8Rx; DL Type II precoder; MMSE-IRC; SU-MIMO up to 4 layers | FTP3 with RU = 30%; 10 UEs per sector; ISD 500 m; TDD DDDSU | 1.8% + 1.8% (BS Tx / UE Rx) for DL 4K QAM | EVM only for DL (MPR modelled for UL only) | Negative: -0.53% to -1.02% across all evaluated cases (FR1/FR3, mixed / 100% OD CPE) | Average gain of beneficial UEs only up to +0.6%; rank 4 dominates (95-100% of scheduling); 7 GHz gives higher beneficial UE ratio than 4 GHz due to larger antenna count | Beneficial UE ratio up to 6.8% | Obs 1-3 + Proposal 1: even with the tight 1.8% EVM budget the system gain is negative; required SNR > 35 dB is the fundamental limit (R1-2606857) |
| MediaTek | R19 UMi, SU-MIMO up to 4 layers, FR1 (4 GHz) and FR3 (7 GHz); up-to-4096QAM vs. up-to-1024QAM baseline | Mixed CPE (80% indoor / 20% outdoor) and 100% outdoor CPE | 4 GHz and 7 GHz / 100 MHz / 30 kHz | BS 64 TXRU @4 GHz / 256 TXRU @7 GHz, 51 dBm per 100 MHz; UE 4Tx / 8Rx; MMSE-IRC; SU-MIMO up to 4 layers | FTP3 with RU = 30%; 10 UEs per sector; ISD 200 m; TDD DDDSU | 1.8% + 1.8% | EVM only | Negative: -1.06% | Average gain of beneficial UEs only up to +0.6%; rank 4 dominates (99-100%) | Beneficial UE ratio up to 3.49% | Obs 4: consistent with UMa - DL 4K QAM is not beneficial in either UMa or UMi |
| Apple | FWA per agreed SLS assumptions, max rank 4 per CPE UE; 4KQAM MCS table (MCS 27-30 are 4096QAM) | Profile 1 (mixed): 80% indoor CPE / 20% outdoor rooftop CPE | 4 GHz / BW not restated in SLS text (100 MHz or 20 MHz per agreement) / 30 kHz | Per agreed assumptions (BS Outdoor Combination 2, 44 dBm/20 MHz; UE antenna Combination 3 Alt 1); realistic channel estimation; max rank 4 | FTP3, target RU = 0.5 (~50%) | Not restated in the SLS section (Table 2.2-2 of this FL summary captured 1.8% + 1.8%) | EVM only | No gain vs. 1024QAM reported; absolute UPT reported instead: indoor mean/median 93.4/100.5 Mbps vs. outdoor 76.6/78.9 Mbps (all UEs 90.0/98.0 Mbps) | Indoor UEs get higher throughput than outdoor UEs despite 4x less 4096QAM usage, because of higher mean rank (2.82 vs. 2.14); MCS distribution bimodal, 12.0% of outdoor UEs at MCS 0 | 4096QAM scheduled 1.8% of the time overall (indoor 1.12% / outdoor 4.08%) | Obs 18/19: 4096QAM scheduled 1.8% of the time in Profile 1; when scheduled, 26.4% of cases are combined with rank 2 (R1-2606833) |
| Apple | FWA per agreed SLS assumptions, max rank 4 per CPE UE; 4KQAM MCS table | Profile 3: 100% outdoor rooftop-mounted CPE | 4 GHz / as above / 30 kHz | As above; max rank 4 | FTP3, target RU = 0.5 | Not restated in the SLS section (1.8% + 1.8% per Table 2.2-2) | EVM only | No gain vs. 1024QAM reported; absolute UPT: mean/median 77.7/82.8 Mbps (slightly above the outdoor split of Profile 1) | Mean rank only 1.89 (vs. 2.14 for the Profile 1 outdoor split) but higher mean MCS (12.31 vs. 11.01), i.e. higher modulation order compensates the lower rank | 4096QAM scheduled 6.5% of the time | Obs 18/19: 6.5% scheduling probability in Profile 3; 45.4% of the 4096QAM cases combined with rank 2 |
| vivo | UMa, CP-OFDM DL, MU-MIMO, max rank 2 and 4; NR 1024QAM table + 4 additional 4096QAM entries (829.5, 869, 908.5, 948) vs. NR 1024QAM table | Mixed deployment: 80% indoor CPE / 20% outdoor rooftop CPE | 4 GHz / 20 MHz and 7 GHz / 100 MHz | BS Outdoor Comb. 2: (16,8,2,1,1;4,8) @4 GHz, (32,16,2,1,1;8,16) @7 GHz, 44 dBm/20 MHz @4 GHz and 43 dBm/20 MHz @7 GHz; UE DL (1,4,2,1,1;1,4) = 8 ports; MU-MIMO; max rank 2 and 4 | FTP3, low / medium / high load | 4096QAM: 1.5% + 1.5% and 1.8% + 1.8%; 1024QAM baseline: 2.5% + 2.5% @4 GHz, 2.8% + 2.8% @7 GHz | EVM only for DL (MPR modelled for UL only) | Max rank 2: +0.51 / +0.34 / +0.40% @4 GHz and +3.55 / +2.93 / +1.29% @7 GHz (low / med / high load). Max rank 4: +0.42 / -3.39 / +3.17% @4 GHz and +0.32 / -0.23 / +1.19% @7 GHz | Overall DL 4K QAM gain < 4%, i.e. much smaller than their UL 1K QAM gain; 7 GHz > 4 GHz because DL power scales with bandwidth; max rank 2 > max rank 4 | Not reported | Obs 37/39: gain for UMa is 0.34-0.51% @4 GHz max rank 2 and 1.29-3.55% @7 GHz max rank 2 (R1-2605456) |
| vivo | Dense Urban, CP-OFDM DL, MU-MIMO, max rank 2 and 4; same MCS tables as above | Mixed deployment: 80% indoor CPE / 20% outdoor rooftop CPE | 4 GHz / 20 MHz and 7 GHz / 100 MHz | Same as UMa row; MU-MIMO; max rank 2 and 4 | FTP3, low / medium / high load | 4096QAM: 1.5% + 1.5% and 1.8% + 1.8%; 1024QAM baseline: 2.5% + 2.5% @4 GHz, 2.8% + 2.8% @7 GHz | EVM only | Max rank 2: +0.51 / +0.66 / -0.58% @4 GHz and +3.80 / +3.03 / +1.88% @7 GHz (low / med / high load). Max rank 4: +0.80 / +0.13 / +1.06% @4 GHz and +0.01 / -0.48 / -1.00% @7 GHz | Same trends as UMa (7 GHz > 4 GHz, max rank 2 > max rank 4) | Not reported | Obs 38: gain is -0.58 to +0.66% @4 GHz max rank 2 and 1.88-3.8% @7 GHz max rank 2 |
| Huawei, HiSilicon | Dense Urban (3D-UMa), TDD, MU-MIMO; MCS table up to 4096QAM vs. up to 1024QAM | Profile 1: 80% indoor CPE / 20% outdoor CPE | 4 GHz / 20 MHz / 30 kHz | BS 64 TxRU (16,8,2,1,1;4,8) @25 m, 44 dBm/20 MHz; UE 8 ports (1,4,2,1,1;1,4), MMSE, UE NF 7 dB; MU-MIMO, 10 UEs/sector, PF, IR-HARQ up to 3 retx, realistic channel estimation | Burst buffer traffic; 7 sites / 3 sectors, 500 m ISD | 1.8% + 1.8% (RAN4 agreed value for 4 GHz) | EVM only | Not quantified (no average UPT gain reported for DL) | Rank and modulation-order distributions provided (Fig. 1); the EVM requirement restricts the achievable SINR in the system | 4096QAM scheduling probability extremely small: 0.01% | Obs 1/3 + Proposal 2: 4096QAM cannot outperform lower-order MCSs at any SNR (companion RAN4 paper); do not study 4096QAM further in 6GR (R1-2606786) |
Evaluations not comply with RAN4 recommended EVM
| Company | Config / Scheme | UE Profile | Carrier / BW / SCS | Antenna config (BS / UE), BS Tx power & max rank | Traffic model / load (RU) | EVM (Tx+Rx) (4096QAM / 1024QAM baseline) | Impairment / power back-off model | Mean / Avg. throughput (UPT) gain | Other reported gain metrics | 4096QAM scheduling prob. / beneficial UE ratio | Key Observation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Qualcomm | UMa, outdoor FWA, max rank 2, CP-OFDM; 4KQAM-enabled vs. 1KQAM-only | 100% outdoor (rooftop-mounted) FWA CPE | 4 GHz / 20 MHz / SCS not stated | BS 64 TxRU (16,8,2,1,1;4,8), 44 dBm; UE 8 ports (1,4,2,1,1;1,4); LMMSE; realistic SRS (16 ms); SVD precoding, PF SU-MIMO; max rank 2 | FTP, packet size 4 Mb, mean inter-arrival 600 ms (target ~20% RU); 21 cells, 500 m ISD, 10 UE drops/cell; UE 3 km/h, uniformly in floors 4-8 | Tx EVM 1% (4096QAM) / 2.5% (1024QAM) - tighter than the RAN4 recommended 1.5% + 1.5%; Rx EVM not stated | EVM only (no BS power back-off) | +21.2% (259.59 -> 314.73 Mbps); the text calls this a median gain while Table 2 labels the metric as mean UPT | 95%-tile UPT +18.9% (318.85 -> 379.38 Mbps) | High (cell-centre LOS outdoor CPEs); not quantified | Obs 2: FWA could be one potential case for higher-order QAM extension; Proposal 1: support DL 4K-QAM (R1-2606862) |
| Qualcomm | UMa, outdoor FWA, max rank 4, CP-OFDM; 4KQAM-enabled vs. 1KQAM-only | 100% outdoor FWA CPE | 4 GHz / 20 MHz / SCS not stated | Same as above; max rank 4 | FTP, ~20% RU target | Tx EVM 1% (4096QAM) / 2.5% (1024QAM) - tighter than RAN4 recommendation | EVM only | +9.4% (394.87 -> 432.29 Mbps) | 95%-tile UPT +17.1% (603.98 -> 707.71 Mbps) | Moderate; not quantified | Rank-4 reduces per-stream SNR and therefore the 4096QAM benefit |
| Qualcomm | Appendix A: real-world-like network and UE drops, U6GHz band, several deployment scenarios | FWA | U6GHz / n/s | Not stated in text (Fig. 58 gives the assumptions) | Not stated in text | Not stated | MPR back-off derived from Wi-Fi 7; Qualcomm notes this relative back-off is pessimistic for cellular | Figures only (Fig. 57): 4K-QAM is still achieved a non-trivial fraction of the time, especially in near-cell conditions | Fig. 59 gives link performance and the Wi-Fi 7-based MPR back-off | Not quantified | Presented as a conservative additional data point; closer-to-cellular back-off to be provided in a future meeting |
| Nokia | UMa 500 m ISD and UMi 200 m ISD, SU-MIMO and MU-MIMO (MU = 2/4/8), max rank 1 / 2 / 4; HOM (1024QAM and 4096QAM) vs. 256QAM baseline | UMa: 20% outdoor CPE; UMi: 100% outdoor CPE | 3.5 GHz / 20 MHz (44 dBm/20 MHz, i.e. 51 dBm/100 MHz) | Full digital BS array; 10 UEs/cell on average, 21-cell network; max rank 1, 2, 4 | FTP and full buffer; RU sweep 16 / 37 / 78 / 100% | Modelled as limits rather than RAN4 EVM pairs: BS Tx max SNR 22 dB and UE max Rx SINR 28 dB; ideal (unlimited) EVM also evaluated | EVM modelled as Tx SNR / Rx SINR ceilings for a full digital array (per-port noise does not scale with antenna count) | Max rank 4: no significant gain for UMa 20% OD; at most +5% for UMi 100% OD - both with realistic and with ideal EVM | Notable gains only for max rank 1, SU-MIMO and FTP with RU below ~40-50%; gains diminish rapidly with higher rank, higher RU, full buffer, and increasing MU-MIMO order (crosstalk limits SINR more than EVM) | 4096QAM usage in the MCS PDF drops rapidly as RU increases (Fig. 2) | Obs 1: very low EVM, particularly at 7 GHz, is required for DL 4096QAM to be meaningful; questionable whether DL 4K-QAM would be scheduled often enough to be statistically relevant (R1-2605380) |
| OPPO | No UPT-based SLS: link-level evaluation (2T4R / 4T4R / 8T8R, 1/2/4 layers) plus a large-scale-fading system-level study (Table A-2) | n/a | 4 GHz and 7 GHz | 2T4R, 4T4R, 8T8R; random Type-I codebook for BS precoding | n/a | 1.5% + 1.5% and 1.8% + 1.8% for 4096QAM (LLS) | EVM only | Not reported (no UPT gain) | Multi-layer 4096QAM transmission essentially infeasible; 1-layer needs SNR ~32-42 dB | Very limited fraction of UEs can support 4096QAM | Marginal system gains expected; OPPO does not support DL 4096QAM (R1-2605910) |
R1-2606883	FL summary #5 on AI 10.3.2 modulation, joint channel coding and modulation, Moderator (Qualcomm)	Qualcomm Incorporated
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.3.2-o003`

### [6G/Rel-20 RAN1#124b] `agreement` 10.3.1 Channel coding

对于超出 NR 范围的 LDPC extension 研究，假设最大 code block size 为 8448，并进一步研究两种方案：BG 中 44 个 information columns、maximum lifting size 为 192，或 22 个 information columns、maximum lifting size 为 384。原文提出在本周内决定两者之一。

```text
For the study of LDPC extension beyond NR range, the maximum code block size of 8448 is assumed for further study with the following two options:
Option 1: 44 information columns in BG and a maximum lifting size of 192
Option 2: 22 information columns in BG and a maximum lifting size of 384
Note: Aim to decide between option 1 and option 2 during this week.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.3.1-a001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.3.1 Channel coding

对于超出 NR 范围的 LDPC extension 研究，进一步研究时假设母码率约为 2/3。该约定仅适用于 new BG 研究。

```text
For the study of LDPC extension beyond NR range, the mother code rate of approximately 2/3 is assumed for further study.
The above agreement is only applicable for study of the new BG.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.3.1-a002`

### [6G/Rel-20 RAN1#124b] `agreement` 10.3.1 Channel coding

对于最大信息块大小为 8448 bits 的 LDPC extension 研究，new BG 的 lifted parity check matrix 在母码率下的 1 总数不超过 N；N 由 BG1 在码率 X 下的 lifted parity check matrix 的 1 总数确定。X 不低于 1/2，具体值仍待确定。

```text
For the study of LDPC extension beyond NR range, for the maximum information block size of 8448 bits, the total number of ones in the lifted parity check matrix under mother code rate is no larger than N, where N is determined by the total number of ones in the lifted parity check matrix of BG1 under the code rate of X.
X is not lower than 1/2.
FFS: Value of X.
R1-2603339	FL summary#2 for 6G channel coding	Moderator(ZTE)
Presented in Tuesday session.
R1-2603340	FL summary#3 for 6G channel coding	Moderator(ZTE)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.3.1-a003`

### [6G/Rel-20 RAN1#124b] `agreement` 10.3.1 Channel coding

对于 new BG 研究，进一步假设 encoder 的 parity check matrix 由五个子矩阵 A、B、C、D、E 组成，并列出各子矩阵结构要求。sub-matrix B 的 B1、B2 方案及 sub-matrix E 的 identity matrix、lower triangular matrix 方案将继续研究，并力争在 RAN1#125 下选。

```text
For the study of LDPC extension beyond NR range, for the study of new BG, assume the parity check matrix for encoder consists of five sub-matrices (A, B, C, D, E) for further study, wherein
Sub-matrix A contains columns that correspond to information bits.
Sub-matrix C is a zero matrix
Sub-matrix D: the number of columns of sub-matrix D equals to (the number of columns of Sub-matrix A) + (the number of columns of Sub-matrix B)
Sub-matrix B contains columns that correspond to core parity check bits
For sub-matrix B, consider the following options for further study, and strive for down-selection in RAN1#125
Option B1: A weight-3 column with corresponding shifting values of [0, X, 0] or [X, 0, X], followed by a dual-diagonal structure with corresponding shifting values of [0,0]
Option B2: At most 2 weight-3 columns and dual-diagonal structure(s) with comparable number of XOR and cyclic shift operations with Option B1, e.g.,
Option B2-1: Sub-matrix B has a weight-3 column with corresponding shifting values of [a, b, c], followed by a dual-diagonal structure
Option B2-2: Sub-matrix B can be decomposed into two sets: set 1 and set 2. Each set follows Option B1/ Option B2-1, with additional pair-wise orthogonality across sets, e.g.,
For sub-matrix E, the following options are identified for further study, and strive for down-selection in RAN1#125
Option E1: An identity matrix
Option E2: A lower triangular matrix
R1-2603411	FL summary#4 for 6G channel coding	Moderator (ZTE)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.3.1-a004`

### [6G/Rel-20 RAN1#124b] `agreement` 10.3.1 Channel coding

对于 new BG，进一步研究采用 44 个 information columns、maximum lifting size 为 192 的 single edge BG，并列出 row splitting、转换为 22 个 information columns 与 maximum lifting size 为 384 的 BG，以及 quasi-row orthogonality 等方案。上述方案可组合，且其他 single edge BG 方案未被排除；目标是在 RAN1#125 下选。

```text
For the study of LDPC extension beyond NR range, for study of the new BG, consider a single edge BG with 44 information columns and a maximum lifting size of 192, with the following options identified for further study, and strive for down-selection among the options in RAN1#125
Option 1: Row splitting, wherein one or more rows outside the core matrix (i.e., sub matrix A and sub matrix B) are split from at least some rows inside the core matrix, and the core column indices of the non-zero entries of the original row are a superset of those of the corresponding split row,
The core matrix contains Y1 rows, and all elements of Y2 rows in sub-matrix A are ones.
Y1= 3 or 4
Y1Y21
Sub-option 1-1: With at least the first row in sub-matrix A included in the Y2 rows
Sub-option 1-2: The first row in sub-matrix A is not included in the Y2 rows.
No puncturing before rate matching
Option 2: The single edge BG with 44 information columns and a maximum lifting size of 192 can be convertible to a BG with 22 information columns and a maximum lifting size of 384. More specifically, each 2x2 submatrix at column 2j, 2j+1, and row 2k, 2k+1 of the BG can only take one of the following forms:
, , , .
No puncturing or puncturing one or two columns before rate matching, wherein the puncturing (if any) is applied within the first two information columns and/or any core parity columns
Option 3: Quasi-row orthogonality in core matrix (i.e., sub matrix A and sub matrix B) and/or sub matrix D, i.e., in which except for certain columns, the row 2k, 2k+1 do not share non-zero entries in the same column in the sub-matrix A and/or sub-matrix D
No puncturing or puncturing one or two columns before rate matching, wherein the puncturing (if any) is applied within the first two information columns and/or any core parity columns
The options above are not mutually exclusive and can be combined.
Other options that have a single edge BG with 44 information columns and a maximum lifting size of 192 are not precluded.
Final summary in R1-2603412.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.3.1-a005`

### [6G/Rel-20 RAN1#124b] `agreement` 10.3.2 Modulation, Joint channel coding and modulation

6G 至少支持 5G NR equal probability uniform QAM constellation：CP-OFDM 数据信道的 DL 支持 QPSK 至 1024QAM，UL 支持 QPSK 至 256QAM；DFT-s-OFDM 数据信道的 UL 支持 pi/2 BPSK 及 QPSK 至 256QAM。其他调制方案或阶数可另行讨论并在有依据时增加支持，低 PAPR 增强和 waveform 相关影响仍待讨论或决定。

```text
At least support 5G NR equal probability uniform QAM constellation for 6G:
For 6GR DL, 5G NR equal probability uniform QPSK, 16QAM, 64QAM, 256QAM and 1024QAM are supported for CP-OFDM for data channel
For 6GR UL, 5G NR equal probability uniform QPSK, 16QAM, 64QAM, and 256QAM are supported for CP-OFDM for data channel
For 6GR UL, 5G NR pi/2 BPSK, equal probability uniform QPSK, 16QAM, 64QAM, and 256QAM are supported for DFT-s-OFDM for data channel
Note: Further enhancements for low PAPR are being discussed in waveform agenda, and will be decided there
Note: The support of equal probability uniform QAM does not have any implication to the study and potential inclusion of shaping based schemes and the study of waveform discussions.
Note: Other equal probability uniform modulation schemes and modulation orders, including but not limited to DL 4kQAM and UL 1k QAM, can be separately discussed and can be additionally supported if justified.
FFS: Impact on modulation if the waveform agenda item concludes on any waveform enhancements.
R1-2603304	FL summary #2 on modulation, joint channel coding and modulation	Moderator (Qualcomm)
Presented in Tuesday session.
R1-2603305	FL summary #3 on modulation, joint channel coding and modulation	Moderator (Qualcomm)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.3.2-a001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.3.2 Modulation, Joint channel coding and modulation

对于 fading channel 下 PS/GS 方案的评估，优先鼓励公司提供指定场景的结果，包括 SIMO 1x4、多种 CDL/TDL 信道，至少 200 Hz Doppler 的高移动速度 UE open-loop MIMO，以及 rank 4 closed-loop precoding。还列出了 MIMO 4x4 和 32x4 在 CDL-A、CDL-B、CDL-C 下的评估场景及 delay spread。

```text
For the evaluation of PS/GS schemes under fading channel, prioritize companies are encouraged to provide evaluation results for the following
SIMO 1x4: CDL-A 100ns, CDL-B 30ns, CDL-C 300ns, TDL-C 100ns
MIMO: Open loop for high speed UE with identity precoding, at least 200 Hz Doppler
MIMO: Closed loop precoding, Rank 4
MIMO 4x4 CDL-A 100ns, MIMO 4x4 CDL-B 30ns,  MIMO 4x4 CDL-C 300ns,
MIMO 32x4 CDL-A 100ns, MIMO 32x4 CDL-B 30ns,  MIMO 32x4 CDL-C 300ns
R1-2603306	FL summary #4 on modulation, joint channel coding and modulation	Moderator (Qualcomm)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.3.2-a002`

### [6G/Rel-20 RAN1#124b] `agreement` 10.3.2 Modulation, Joint channel coding and modulation

针对 FWA 场景 CPE 的 DL 4K uniform QAM 和 UL 1K uniform QAM SLS 研究，确定 Dense Urban 与 Urban Macro 的参数子集，包括布局、频段、天线模型、功率、流量、UE 分布与速度、天线面板、UE 功率等级、带宽、最大 rank、信道估计和 MU-MIMO 假设。结果报告还需包含按室内、室外 LOS 和室外 non-LOS 分类及联合统计的 rank 分布与 MCS 分布，并单独报告选择 DL 4KQAM 和 UL 1KQAM 时的 rank 分布；EVM 和 MPR 假设需 RAN4 输入。

```text
For SLS study for DL 4K uniform QAM without shaping and UL 1K uniform QAM without shaping for CPE in FWA scenario, focus on the following subset of parameters for Dense Urban and Urban Macro:
Layout: Single layer
Frequency: Around 4GHz and/or Around 7GHz
BS antenna model: Outdoor Combination 2 for around 4GHz and Outdoor Combination 2 for around 7GHz
BS power: 44dBm/20MHz for around 4GHz, and 43dBm/20MHz for around 7GHz
O2I penetration loss: Option 2: 50% low loss, 50% high loss
Traffic model: FTP3
UE distribution and UE speed:
Profile 1 (mixed deployment): 80% Indoor CPE: (0, 0.3] km/h; 20% Outdoor rooftop mounted CPE: (0, 0.3]km/h.
Profile 3 (Outdoor mounted CPE only): Roof-top mounted, 100% outdoor (0,0.3] km/h
For outdoor rooftop mounted CPE, consider uniform distributed in 4-8 floors for building height.
UE antenna panel: Combination 3 Alt 1 for around 4GHz, combination 4 for around 7GHz
Tx configuration of UE antenna panel for UL 1024QAM
Companies to report antenna orientation
UE power class: 31dBm, 35dBm (Other values can be reported by companies)
Simulation BW: 100MHz, 20MHz
Maximum rank per CPE UE: 2, 4, 8 (optional)
Channel estimation: Realistic channel estimation
Assume MU-MIMO capability is available at gNB
MCS table including the additional MCS entries for DL 4K QAM and UL 1K QAM provided by company
Other parameter setting not precluded and company can report
For SLS result reporting, also include
Rank distribution (for indoor CPE and outdoor LOS CPE and outdoor non-LOS CPE separately and jointly)
Rank distribution when 4KQAM DL and 1KQAM UL is selected.
Modulation order (MCS) distribution (for indoor CPE and outdoor LOS CPE and outdoor non-LOS CPE separately and jointly)
Note: RAN4 input is needed for the following parameters:
EVM assumption and modelling
MPR assumption
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.3.2-a003`

### [6G/Rel-20 RAN1#124b] `observation` 10.3.2 Modulation, Joint channel coding and modulation

观察到，使用 MMSE receiver 时，1D-NUC 的 demodulation/demapper complexity 相对 uniform QAM 为 1 至 1.6 倍（量化位宽为每 I/Q 6 至 10 bit），另有 14 bit 情形为 6.45 倍；2D-NUC（QAM-CS 除外）为 20 至 947 倍，NP-NUC 使用与 uniform QAM 相同的 demodulation/demapper。需为 RAN plenary checkpoint 补充 GS 与 uniform QAM 的复杂度、存储需求比较，以及性能增益/损失与复杂度/存储的关联观察。

```text
For GS schemes, at least the following are observed:
For 1D-NUC, if MMSE receiver is used, the demodulation/demapper complexity is [1 to 1.6] times that of uniform QAM assuming [6 to 10] quantization bit-width per I/Q for 1D-NUC.
Further observations will be worked on demodulation/demapper complexity of 1D-NUC with rML receiver
For 1D-NUC, if MMSE receiver is used, the demodulation/demapper complexity is [6.45] times that of uniform QAM assuming [14] quantization bit-width per I/Q for 1D-NUC.
Further observations will be worked on demodulation/demapper complexity of 1D-NUC with rML receiver
For 2D-NUC (except for QAM-CS), if MMSE receiver is used, the demodulation/demapper complexity is [20 to 947] times that of uniform QAM.
Further observations will be worked on demodulation/demapper complexity of QAM-CS based 2D-NUC
Further observations will be worked on demodulation/demapper complexity of 2D-NUC with rML receiver
For NP-NUC, the same demodulation/demapper as uniform QAM is used
Further observations are required to be provided for RAN plenary checkpoint to compare the complexity and storage requirements for GS with respect to uniform QAM.
Further observations of linkage between performance gain/loss under agreed fading channels with the complexity/storage are required for RAN plenary checkpoint.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.3.2-o001`

### [6G/Rel-20 RAN1#124b] `observation` 10.3.2 Modulation, Joint channel coding and modulation

对于 ESS based PS，存储需求随 DM block length 增长约呈二次增加，随每个 I/Q symbol 的 shaped bits 数量增长呈指数增加，processing delay 随 DM block length 线性增加；对于 CCDM based PS，processing delay 随 DM block length 线性增加。需为 RAN plenary checkpoint 补充不同 DM 算法/参数相对 uniform QAM 的复杂度与存储需求比较，以及性能增益/损失与复杂度/存储的关联观察。

```text
For PS schemes, at least the following are observed:
For ESS based PS, the storage requirement increases approximately quadratically with increasing DM block length, the storage requirement increases exponentially with increasing number of shaped bits per I/Q symbol, and processing delay increases linearly with increasing DM block length
For CCDM based PS, the processing delay increases linearly as DM block length increases.
Further observations are required to be provided for RAN plenary checkpoint to compare the complexity and storage requirements of different DM algorithm/parameters for PS with respect to uniform QAM.
Further observations of linkage between performance gain/loss under agreed fading channels with the complexity/storage are required for RAN plenary checkpoint.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.3.2-o002`

### [6G/Rel-20 RAN1#124] `agreement` 10.3.1 Channel coding

针对超出 NR 范围的 LDPC extension，RAN1#124 确定 maximum code block size 的两个进一步研究选项：8448 和 8448*2。

```text
For the study of LDPC extension beyond NR range, the following options of the maximum code block size are identified in RAN1#124 for further study
Option 1: 8448
Option 2: 8448*2
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.3.1-a001`

### [6G/Rel-20 RAN1#124] `agreement` 10.3.1 Channel coding

针对超出 NR 范围的 LDPC extension，RAN1#124 确定 BG 中 information columns 数量的三个进一步研究选项：22、44 和 33。

```text
For the study of LDPC extension beyond NR range, the following options of the number of information columns in BG are identified in RAN1#124 for further study
Option 1: 22
Option 2: 44
Option 3: 33
R1-2601568	FL summary#2 for 6G channel coding	Moderator(ZTE)
From Tuesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.3.1-a002`

### [6G/Rel-20 RAN1#124] `agreement` 10.3.1 Channel coding

针对 LDPC extension beyond NR range，确定进一步研究 rate matching 前 puncturing 的三种选项：不 puncture、puncture 1 column、puncture 2 columns。

```text
For the study of LDPC extension beyond NR range, the following options of puncturing before rate matching are identified in RAN1#124 for further study
Option 1: no puncturing
Option 2: puncture 1 column
Option 3: puncture 2 columns
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.3.1-a003`

### [6G/Rel-20 RAN1#124] `agreement` 10.3.1 Channel coding

为评估 payload size 超过 NR 范围且大于 1706 bits 的 L1 uplink control information 的 Polar code segmentation enhancement，列出了评估假设，包括 AWGN、QPSK、多个 code rate、CRC-aided SCL decoding 和 BLER 目标。每段使用 11 bits CRC，rate matching、channel interleaver 和 code-block concatenation 沿用 NR；其他评估取值由公司报告。

```text
For performance evaluation purposes, the corresponding evaluation assumptions for study the Polar code segmentation enhancement used for L1 uplink control information with payload size beyond NR range and larger than 1706 bits, following evaluation assumptions are considered.
| Channel | AWGN |
| --- | --- |
| Modulation | QPSK other modulation orders can be reported by companies |
| UL | Code rate: 1/8, 1/6, 1/5, 1/4, 1/3, 1/2, 2/3, 3/4 Information bit length (bits w/o CRC) A: 1706+S: S: X Coded bit length X is up to companies to report. S: 16 |
| Decoding algorithm for Polar code | CRC-aided SCL decoding Companies to report the list sizes either 8 or 16. |
| Target BLER of UCI payload | 10-2, 10-3 |
Note: 11 bits CRC per segment, rate matching, channel interleaver and code-block concatenation follow NR.
Note: Companies to report other values that are used in their evaluations.
R1-2601569	FL summary#3 for 6G channel coding	Moderator(ZTE)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.3.1-a004`

### [6G/Rel-20 RAN1#124] `agreement` 10.3.1 Channel coding

LDPC extension beyond NR range 的 maximum lifting size 不大于 384；其确切取值仍待研究。

```text
For the study of LDPC extension beyond NR range, the maximum lifting size is not larger than 384
FFS: the exact value of the maximum lifting size
R1-2601666	FL summary#4 for 6G channel coding	Moderator (ZTE)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.3.1-a005`

### [6G/Rel-20 RAN1#124] `agreement` 10.3.1 Channel coding

LDPC extension beyond NR range 进一步研究采用 quasi-cyclic LDPC codes，其 parity check matrix 由 circularly shifted matrices 或 zero matrices 组成，且循环移位矩阵的 row weight 不超过 2。mb、nb、z 的取值以及循环移位矩阵的 row weight 配置仍待研究。

```text
For the base graph of LDPC extension beyond NR range, the following is identified in RAN1#124 for further study
The LDPC extension is quasi-cyclic LDPC codes, the parity check matrix of quasi-cyclic LDPC Codes is defined at least by a matrix H of size (mb×z)×(nb×z), which consists of sub-block matrices of size z×z, where each sub-block matrix is composed by circularly shifted matrices or zero matrices. Wherein, mb, nb and z are integers larger than 1.
The values of mb, nb and z are FFS.
The row weight of circularly shifted matrices is less than or equal to 2.
FFS: Whether row weight of all circularly shifted matrices is 1, or the row weight of some circularly shifted matrices is 1 and the row weight of some circularly shifted matrices is 2.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.3.1-a006`

### [6G/Rel-20 RAN1#124] `agreement` 10.3.1 Channel coding

LDPC extension beyond NR range 的 BG1 与公司提出的 BG(s)/PCM(s) 性能比较，至少考虑在相同 BLER 下的 computational complexity 差异，以及相同计算复杂度下的 SNR 性能差异。BG1 的 reference maximum number of iterations 为 5、7、10、15，公司也可报告其他值及平均迭代次数差异。

```text
For study of LDPC extension beyond NR range, at least the following metrics are considered for the performance comparison among BG1 and BG(s)/PCM(s) proposed by companies
Computational complexity difference to achieve the same BLER performance as BG1 under the reference maximum number of iterations of BG1.
SNR performance difference with the same computation complexity as BG1 under the reference maximum number of iterations of BG1.
The reference maximum number of iterations is 5, 7, 10, 15 based on BG1.
Other values can be also reported by companies
Note: Companies can report the average number of iterations difference to achieve the same performance as BG1 under the reference maximum number of iterations of BG1.
Final summary in R1-2601667.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.3.1-a007`

### [6G/Rel-20 RAN1#124] `agreement` 10.3.2 Modulation, Joint channel coding and modulation

列出了影响 PS 与 GS 复杂度、存储、时延、BLER 和 throughput 权衡的参数，并要求提交评估所用参数及性能结果。鼓励公司评估不同参数组合，以研究不同权衡并提供可行性评估。

```text
Parameters affect the PS complexity/storage/latency and BLER and throughput performance trade-off are at least:
DM output length in unit of I/Q symbol,
# of bits shaped per I/Q,
# of shaping parameters
# of DM blocks needed to support the target throughput of 6GR
DM algorithm and bit-width of variables in the DM algorithm
Impact of mismatch on the quantization bitwidth between DM and DDM.
Parameters affect the GS complexity/storage/latency and BLER and throughput performance trade-off are at least:
1D-NUC or 2D-NUC
Constellations and  # of constellations
Bitwidth for describing the constellation
Bits to constellation mapping
The values of these parameters used in evaluations shall be submitted together with performance results.
Companies are encouraged to provide evaluations for different combination parameters to study different performance and complexity/storage/latency trade-offs to provide proper assessment including feasibility .
R1-2601549	FL summary #2 on modulation, joint channel coding and modulation	Moderator (Qualcomm)
Presented in Tuesday session,
R1-2601550	FL summary #3 on modulation, joint channel coding and modulation	Moderator (Qualcomm)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.3.2-a001`

### [6G/Rel-20 RAN1#124] `agreement` 10.3.2 Modulation, Joint channel coding and modulation

DL 4K uniform QAM 和 UL 1K uniform QAM 的研究聚焦 FWA 室外及室内部署场景，in-door hot-spot 仍待研究。相关 CPE SLS 假设采用 Dense Urban 和 UMA layout，其他 SLS 参数仍待研究。

```text
For the study of introducing DL 4K uniform QAM and UL 1K uniform QAM, focus on the following use cases:
FWA deployed outdoor
FWA deployed indoor
FFS: In-door hot-spot.
For SLS of DL 4K uniform QAM and UL 1K uniform QAM for CPE under FWA scenarios, assume the following:
For layout
Dense Urban
UMA
FFS: Other SLS parameters
R1-2601551	FL summary #4 on modulation, joint channel coding and modulation	Moderator (Qualcomm)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.3.2-a002`

### [6G/Rel-20 RAN1#124] `agreement` 10.3.2 Modulation, Joint channel coding and modulation

决定向 RAN4 发 LS，请其提供不带 shaping 的 DL 4K uniform QAM 和 UL 1K uniform QAM 的 EVM 与 MPR 数值。

```text
Send LS to RAN4 to kindly provide the EVM and MPR values for DL 4K uniform QAM without shaping and UL 1K uniform QAM without shaping.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.3.2-a003`

### [6G/Rel-20 RAN1#124] `agreement` 10.3.2 Modulation, Joint channel coding and modulation

针对 PS，列出了 TX/RX chain functionality blocks 的潜在影响，包括新增 DM 功能，以及 TBS calculation、CB segmentation、interleaving、scrambling 和 modulation 等功能的修改；RX 侧还涉及 DDM、demodulation 和 CB concatenation。鼓励公司提供相关功能修改的设计细节，并说明未受影响功能块的原因。

```text
For PS, potential impact to the TX/RX chain functionality blocks are identified as follows:
TX chain
(Modified) TBS calculation
(Modified) CB segmentation
(New) DM functionalities
Bit splitting: Split to shaped bits and unshaped bits
DM
Bit concatenation/multiplexing: Concatenate/multiplex DM output and unshaped bits
(Modified) Bit interleaver and Bit selection
(Modified) Scrambling: shaped bits should not be scrambled to keep the target distribution
(Modified) Modulation: Power normalization needed for shaped constellation
RX chain
(Modified) TBS calculation
(New) DM functionalities
Bit splitting: Split to shaped bits and unshaped bits
DDM
Bit concatenation/demultiplexing: Concatenate/demultiplex DDM output with unshaped bits
(Modified) Bit de-interleaver and Bit selection
(Modified) Descrambling:
(Modified) Demodulation: Prior probability used in demodulation
(Modified) CB concatenation
Companies are encouraged to provide design details for the modification needed for above functionalities.
Companies are encouraged to explain the reason if a functionality block is not impacted.
R1-2601662	FL summary #5 on modulation, joint channel coding and modulation	Moderator (Qualcomm)
From Thursday session
R1-2601663	Draft LS to RAN4 for 4K QAM and 1K QAM EVM and MPR	Qualcomm
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.3.2-a004`

### [6G/Rel-20 RAN1#124] `agreement` 10.3.2 Modulation, Joint channel coding and modulation

R1-2601663 中的 draft LS 获得认可，最终 LS 在 R1-2601664 中获批。

```text
The draft LS in R1-2601663 is endorsed. The final LS is approved in R1-2601664.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.3.2-a005`

### [6G/Rel-20 RAN1#124] `agreement` 10.3.2 Modulation, Joint channel coding and modulation

已识别 GS 相比 NR 对 TX/RX chain 功能块的潜在影响，包括映射、调制符号生成、接收符号解调和解映射。鼓励公司在同时支持 NUC 和 uniform QAM 时说明影响、所需设计修改及未受影响功能块的原因。

```text
For GS, potential impact to the TX/RX chain functionality blocks compared to NR are identified as follows:
TX chain
Mapper
Bit to constellation symbol mapping
Modulation symbol generation
RX chain
Demodulation of received symbols
Demapper
Companies are encouraged to identify potential impact on TX, RX chains if both NUC and uniform QAM are supported.
Companies are encouraged to provide design details for the modification needed for above functionalities.
Companies are encouraged to explain the reason if a functionality block is not impacted.
R1-2601699	FL summary #6 on modulation, joint channel coding and modulation	Moderator (Qualcomm)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.3.2-a006`

### [6G/Rel-20 RAN1#123] `agreement` channel-coding-0cf828bf Channel coding

对于载荷大于 NR 范围（即超过 1706 bits）的 UCI Polar code 设计，至少将 more than 2 segments 作为进一步研究选项。是否需要超出 NR 范围的 UCI 载荷，需由其他议题确认。

```text
For Polar code design for UCI with payload size larger than NR range (i.e., larger than 1706 bits), at least the following option is identified for further study
More than 2 segments
Note: The necessity of UCI payload size larger than NR range needs to be confirmed by other agenda(s)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-channel-coding-0cf828bf-a001`

### [6G/Rel-20 RAN1#123] `agreement` channel-coding-0cf828bf Channel coding

针对超出 NR 范围数据速率的 LDPC 扩展研究，需在 RAN1#124 前提供初版 LDPC BG(s) 和 PCM(s)，并给出目标 BLER 所需 SNR、复杂度及译码算法评估假设。复杂度定义将进一步讨论，其他指标仍为 FFS。

```text
For the study of LDPC extension for data rate beyond NR range with acceptable performance-complexity tradeoff,
To provide the initial version of LDPC BG(s) and PCM(s) in the excel spreadsheet by RAN1#124
To provide the required SNR and complexity for target BLER, and the evaluation assumptions of the decoding algorithm
The definition of complexity will be further discussed
FFS: other metrics
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-channel-coding-0cf828bf-a002`

### [6G/Rel-20 RAN1#123] `agreement` channel-coding-0cf828bf Channel coding

针对 3~11 bits 小载荷 UCI 的信道编码研究，至少考虑 5G RM code。若 5G RM code 存在可论证的缺点，应识别并研究潜在解决方案。

```text
For the study of channel coding for small UCI with payload size of 3~11bits, at least considering:
5G RM code
Identify the justifiable drawbacks of 5G RM code, if exists, study potential solution(s).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-channel-coding-0cf828bf-a003`

### [6G/Rel-20 RAN1#123] `agreement` channel-coding-0cf828bf Channel coding

LDPC 扩展的 BG(s) 和 PCM(s) 评估将考虑给定的 AWGN 信道、调制与码率、交织器、码块大小、目标 BLER 及译码算法假设，这些假设仅用于仿真，不影响最终设计。候选方案需同时比较性能和复杂度，且 BLER 性能比较须在相同计算复杂度下进行，计算复杂度按所需 BLER 的迭代次数与提升后校验矩阵中 1 的数量之积除以 CB size 定义。

```text
For the study of BG(s) and PCM(s) for LDPC extension for data rate beyond NR range, at least the following evaluation assumptions will be considered.
| Parameters | Values or assumptions |
| --- | --- |
| Channel | AWGN |
| Modulation and code rate | Uniform QAM modulations and corresponding code rates (i.e., (8,682.5/1024), (8, 797/1024), (8, 885/1024), (8, 948/1024)) in NR MCS Table 5.1.3.1-4 as starting point. Other modulation order, if used, can be reported. |
| Interleaver | Same as 5G NR. Other interleaver scheme (intra-CB level), if used, can be reported. |
| Code block size (bits with CRC) | CB size: same as 5G NR (8448 as baseline, other values less than 8448 can be reported). CB size: other value(s) larger than 8448 and no larger than 8448*2, e.g.,16k. Company to report the TBS. |
| Target CB BLER | BLER=10-2, 10-4 |
| Decoding algorithm of LDPC | Layered BP or min-sum(offset, normalized or adjusted min-sum) Company to report the details of offset, normalized or adjusted min-sum decoding algorithm, if used. Max number of iteration times: 5:1:20 Other iteration times can be reported. Decoding order: reversed order Other decoding order, if used, can be reported. |
| Demodulation algorithm | Max-log-map |
Note: For any comparison among 5G BG and BG(s)/PCM(s) proposed by companies, the BLER performance is compared at least under the same CB size.
Note: all evaluation assumptions above are for simulation only and have no implication on the final design of BG(s)/PCM(s).
For candidate comparison, both performance and complexity should be considered.
The comparison of BLER performance is under the same computation complexity,
Computation complexity is defined as (the number of iteration times for required BLER) *(the number of ones in the lifted parity check matrix)/ (CB size)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-channel-coding-0cf828bf-a004`

### [6G/Rel-20 RAN1#123] `conclusion` channel-coding-0cf828bf Channel coding

对于载荷处于 NR 范围内且大于 11 bits 的 Polar code 设计潜在扩展或增强，其动机尚无共识。

```text
No consensus on motivation(s) for potential extension/enhancement for Polar code design with payload size within NR range (larger than 11bits).
R1-2509582	FL summary#6 for 6G channel coding	Moderator (ZTE, Apple)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-channel-coding-0cf828bf-c001`

### [6G/Rel-20 RAN1#123] `agreement` modulation-joint-channel-coding-and-modu-ff7518f4 Modulation, joint channel coding and modulation

对 PS/GS 固定 MCS 的性能报告，采用以 10% BLER 为目标的表格格式作为仿真结果报告起点；NR 参考需提供 modulation order 与 coding rate，而不只提供 MCS index。表格包含各 SE 点参数、均匀 QAM 基线 SNR、相对 NR baseline 的增益或损失及方案假设；其他指标（至少 complexity）可在细节达成一致后并入。

```text
For PS/GS fixed MCS performance reporting for 10% BLER (other target x% BLER can also be reported), adopt the following format for simulation as a starting point for result reporting.
| NR reference | Scheme A (e.g, PS, 1D-NUC, 2D-NUC etc) |  |  |  |
| --- | --- | --- | --- | --- |
| SE | (Mod order, coding rate) | SE point specific parameters | Baseline (uniform QAM) SNR to reach target BLER | Gain/loss in dB wrt NR baseline at target BLER x% |
| SE x | (modOrder, coding rate) | … |  |  |
| SE y | (modOrder, coding rate) | … |  |  |
| SE z | (modOrder, coding rate) | … |  |  |
| SE point independent assumptions | Common assumptions for the scheme simulated, including channel type (AWGN, SISO, SIMO, MIMO) and antenna configuration, number of spatial layers, number of RB allocated, TB size, shaping algorithm used (including block length), freq domain interleaver applied or not, receiver assumption, precoding assumption, realistic channel estimation, etc |  |  |  |
Note: For NR MCS reference, since NR has multiple MCS tables, it is not enough to provide the MCS index. Instead, need to provide the (modulation order, coding rate) pair for the simulated SE
Note: For SE point specific parameters:
For GS, this can be a pointer to the constellation used for this SE point
For PS, this can be a constellation size, coding rate and shaping parameter used for this SE point
Note: Other metrics (at least complexity) will be merged into the same table with other columns, if details of the metrics are agreeable.
Note: For AMC study, if possible, we can use the same table format
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-modulation-joint-channel-coding-and-modu-ff7518f4-a001`

### [6G/Rel-20 RAN1#123] `agreement` modulation-joint-channel-coding-and-modu-ff7518f4 Modulation, joint channel coding and modulation

为比较 PS/GS 与 uniform QAM，规定复杂度、存储、处理时延及并行性/串行性的报告项目；复杂度按 information bits 归一化，并以比较、加减、乘除运算数表示。复杂度和存储按其是否依赖 SE 点分别加入既有性能报告表的列或行，规范影响另行评估。

```text
On how to evaluate complexity, storage requirement, delay and parallelism/serialism for PS and GS compared with uniform QAM.
For PS
The demapper complexity is compared with uniform QAM demapper complexity
Can report the demapper complexity with PS and the demapper complexity of NR MCS with the same spectrum efficiency, and the ratio of the complexities
Also report the number of spatial layers, dm-algorithm used and the receiver type (e.g., LMMSE or rML), and fixed point assumed or floating point assumed.
The Distribution Matcher (DM)/Distribution De-Matcher (DDM) complexity and/or storage requirement as a function of the DM algorithm used (ESS, CCDM, etc), precision of fixed point implementation, block length, and the number of bit levels shaped per symbol
For complexity, can report the complexity normalized by the number of information bits
As a reference, can also report the computation complexity of LDPC decoding with 10 iterations.
For storage requirement, can report the overall storage needed for DM/DDM for supporting all MCS in the MCS table and all shaping related parameters
DM and DDM complexity and storage will be counted separately
The DM/DDM processing delay, parallelism/serialism, as a function of DM design and block length, and their impact to throughput
For GS,
The demapper complexity is compared with uniform QAM demapper complexity
Can report the ratio of GS demapper complexity over the uniform QAM demapper complexity
Also report if 1D-NUC or 2D-NUC is used, # of spatial layers, and the receiver type (e.g., LMMSE or rML)
Also need to report the assumption on complexity counting, e.g, fixed point assumed or floating point assumed
The storage requirement for storing all the constellations corresponding to the MCS indices in the MCS table, as a function of precision of constellation point storage
Processing delay and parallelism/serialism, if applicable, and their impact to throughput
Note: the complexity is represented by the numbers of comparison, addition/subtraction, and multiplication/division operations, normalized by the number of information bits.
Note: For complexity as a function of SE point, will add a column in the already agreed performance reporting table.
Note: For complexity/storage not as a function of SE point, will add a row in the already agreed performance reporting table.
Note: Spec impact will be separately evaluated, include BICM, scrambling, etc
Note:
For 4K uniform QAM DL and 1K uniform QAM UL link level performance study, the following format can be used for performance reporting.
| (modOrder, coding rate*1024, SE) | Assumed TX/RX EVM | Channel 1 | Channel 2 | Channel 3 |
| --- | --- | --- | --- | --- |
|  |  | SNR to achieve target BLER | SNR to achieve target BLER | SNR to achieve target BLER |
| (10, 900.5, 8.7939) for DL evaluation (8, 916.5, 7.1602) for UL evaluation | Legacy EVM for 1K QAM for DL and 256QAM for UL respectively |  |  |  |
| (10, 948, 9.2578) for DL evaluation (8, 948, 7.4063) for UL evaluation | Legacy EVM for 1K QAM for DL and 256 QAM for UL respectively |  |  |  |
| SE1 |  |  |  |  |
| SE2 |  |  |  |  |
| SE3 |  |  |  |  |
| Other parameters |  |  |  |  |
For assumed TX/RX EVM, before we receive any concrete numbers from RAN4, companies can provide their assumptions. One example can be 6dB tighter than the EVM of 1K QAM for DL and 256QAM for UL.
Other parameters include: Channel estimation assumption (genie or realistic), channel configurations (AWGN, SISO, SIMO, MIMO and TX/RX antenna configurations, channel types, number of spatial layers,), assumed residual freq offset range, number of allocated RBs, etc
Two highest MCS points in DL 1K QAM and UL 256QAM in NR added in the table for comparison.
This is preliminary result and not intended for TR
Note: For high order uniform QAM for DL 4K QAM and UL 1K QAM, to provide the UPT with the high order QAM (DL 4K QAM and UL 1K QAM) over the UPT without the high order QAM under the assumed deployment scenario.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-modulation-joint-channel-coding-and-modu-ff7518f4-a002`

### [6G/Rel-20 RAN1#123] `agreement` modulation-joint-channel-coding-and-modu-ff7518f4 Modulation, joint channel coding and modulation

对 PS/GS 固定 MCS 的性能报告，采用以 10% BLER 为目标的表格格式作为仿真结果报告起点；NR 参考需提供 modulation order 与 coding rate，而不只提供 MCS index。表格包含各 SE 点参数、均匀 QAM 基线 SNR、相对 NR baseline 的增益或损失及方案假设；其他指标（至少 complexity）可在细节达成一致后并入。

```text
For PS/GS fixed MCS performance reporting for 10% BLER (other target x% BLER can also be reported), adopt the following format for simulation as a starting point for result reporting.
| NR reference | Scheme A (e.g, PS, 1D-NUC, 2D-NUC etc) |  |  |  |
| --- | --- | --- | --- | --- |
| SE | (Mod order, coding rate) | SE point specific parameters | Baseline (uniform QAM) SNR to reach target BLER | Gain/loss in dB wrt NR baseline at target BLER x% |
| SE x | (modOrder, coding rate) | … |  |  |
| SE y | (modOrder, coding rate) | … |  |  |
| SE z | (modOrder, coding rate) | … |  |  |
| SE point independent assumptions | Common assumptions for the scheme simulated, including channel type (AWGN, SISO, SIMO, MIMO) and antenna configuration, number of spatial layers, number of RB allocated, TB size, shaping algorithm used (including block length), freq domain interleaver applied or not, receiver assumption, precoding assumption, realistic channel estimation, etc |  |  |  |
Note: For NR MCS reference, since NR has multiple MCS tables, it is not enough to provide the MCS index. Instead, need to provide the (modulation order, coding rate) pair for the simulated SE
Note: For SE point specific parameters:
For GS, this can be a pointer to the constellation used for this SE point
For PS, this can be a constellation size, coding rate and shaping parameter used for this SE point
Note: Other metrics (at least complexity) will be merged into the same table with other columns, if details of the metrics are agreeable.
Note: For AMC study, if possible, we can use the same table format
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-modulation-joint-channel-coding-and-modu-ff7518f4-a003`

### [6G/Rel-20 RAN1#123] `agreement` modulation-joint-channel-coding-and-modu-ff7518f4 Modulation, joint channel coding and modulation

研究允许一个 spectrum efficiency point 对应多个 MCS entries 的方案，并要求报告 MCS table 设计与预期大小、不同映射方式下的性能，以及不同信道和 rank 假设下的收益。性能基线包括最高至 256 QAM 的 legacy MCS table；另需说明同一 SE 对应多个 MCS 时的选择机制及可能需要的 UE feedback。

```text
To evaluate the proposal to allow a single spectrum efficiency point to be supported by multiple MCS entries (with different modulation order and coding rate combinations with uniform QAM or with different shaping parameters, coding rate, and constellation size combinations for PS and different coding rate and constellation combinations for GS).
When providing results, to provide the following information
Details on the design of MCS table with overlapping MCS entries and expected size of MCS table, including performance comparison of designs with the same expected size of MCS table
Performance benefit under different channel and rank assumptions
As baseline, provide performance with legacy MCS table up to 256 QAM
Can additionally provide performance with legacy MCS table up to 1K QAM
For PS/GS, provide performance allowing each SE point to be mapped to one or more MCS entries
For PS/GS, provide performance allowing each SE point to be mapped to only one MCS entry (from the set of one or more MCS entries)
For uniform QAM, provide performance allowing each SE point to be mapped to one or more MCS entries
MCS selection mechanism across multiple MCS corresponding to the same spectrum efficiency.
If UE feedback is needed for gNB to select between multiple MCS entries corresponding to the same SE, provide details on what is to be fed back
FFS: How different MPR for different modulation order is captured in the simulation for uplink
FFS: How different EVM for different modulation order is captured in the simulation
For the purpose of this study, the same set of SE points as in legacy uniform QAM table will be used as starting point.
When reporting performance, also report other assumptions, including channel type (AWGN, SISO, SIMO, MIMO) and antenna configuration, number of spatial layers, number of RB allocated, TB size, shaping algorithm used (including block length), freq domain interleaver applied or not, receiver assumption, precoding assumption, realistic channel estimation, etc
To propose how to align shaping parameters or how to align coding rate for facilitating comparison.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-modulation-joint-channel-coding-and-modu-ff7518f4-a004`

### [6G/Rel-20 RAN1#123] `agreement` modulation-joint-channel-coding-and-modu-ff7518f4 Modulation, joint channel coding and modulation

针对 DFT-s-OFDM，进一步研究 PS/GS 是否以及如何能够相较 uniform QAM 实现 Net Gain。

```text
For DFT-s-OFDM, further study how/whether Net Gain over uniform QAM can be achieved by PS/GS.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-modulation-joint-channel-coding-and-modu-ff7518f4-a005`

### [6G/Rel-20 RAN1#122] `agreement` modulation-joint-channel-coding-and-modu-ff7518f4 Modulation, joint channel coding and modulation

6GR DL 数据信道将 5G NR uniform QPSK、16QAM、64QAM、256QAM 和 1024QAM 作为支持基础进行研究。UL 数据信道方面，CP-OFDM 以 QPSK 至 256QAM 为基础，DFT-s-OFDM 另包括 pi/2 BPSK；增强和其他调制方案仍为 FFS。

```text
For 6GR DL, 5G NR uniform QPSK, 16QAM, 64QAM, 256QAM and 1024QAM are supported as basis for study for data channel
FFS: Enhancements and other modulation schemes
For 6GR UL, 5G NR uniform QPSK, 16QAM, 64QAM, and 256QAM are supported as basis for study for CP-OFDM for data channel
FFS: Enhancements and other modulation schemes
For 6GR UL, 5G NR pi/2 BPSK, uniform QPSK, 16QAM, 64QAM, and 256QAM are supported as basis for study for DFT-s-OFDM for data channel
FFS: Enhancements and other modulation schemes
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-modulation-joint-channel-coding-and-modu-ff7518f4-a001`

