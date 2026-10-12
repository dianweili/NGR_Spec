# 6GR 波形与帧结构

**当前进展** · 阶段：收敛中

6GR 波形研究以 NR 的 CP-OFDM、DFT-s-OFDM 及 normal CP 为基础，已明确上行与下行的主要研究方向，并建立了较细致的评估假设、指标和提案信息模板。上行低 PAPR 和多层 DFT-s-OFDM 研究持续推进，已汇总多种方案及评估结果；低 PAPR 技术正按频谱处理方式和调制方式进一步筛选。下行 DFT-s-OFDM 不再纳入 AI 10.2.1 的讨论，但相关下行信号仍可在各自议题中研究。SCS、部分带宽选项及若干方案适用条件仍未确定，现有材料尚未形成完整的波形与帧结构定稿。

**未决问题**

- 其他 SCS 选项是否纳入讨论、是否需要 normal CP 以外的 CP，以及 sensing numerology 如何确定。
- FR2-1 网络侧 400 MHz 与 800 MHz 信道带宽的最终选择，以及 UE 侧是否支持相应带宽；400 MHz UE 实现选项及其性能、能效、成本和复杂度仍待研究。
- UL low-PAPR 方案的适用 SE 范围、频谱扩展或截断条件、透明性与调制方式仍待筛选。
- 应用频谱扩展或截断前的 DFT size 选项 2（X=4）是否支持、RB 数量上限及相关评估结果仍待确定。
- 各波形方案的最终评估指标、适用场景与信号、兼容性及规范影响仍需进一步收敛。

## 6GR 演进

### [6G/Rel-20 RAN1#126] `agreement` 10.2.1 Waveform

同意采用 R1-2606804 第 4.5 节中嵌入的 UL PAPR reduction scheme 结果收集模板。鼓励有评估结果的公司填写模板，并于 8 月 27 日 EOD 前上传至 FL 指定的 draft folder。

```text
Agree on the embedded template for UL PAPR reduction scheme results collection in section 4.5 of R1-2606804.
Companies having evaluation results are encouraged to fill the template and upload it into the draft folder indicated by FL by 27th August EOD.
R1-2606804	Feature Lead summary #3 on 6G waveform	Moderator (Nokia)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.2.1-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.2.1 Waveform

认可 R1-2606804 第 3.5 节中更新后的 observations。

```text
Endorse the updated observations in section 3.5 in R1-2606804
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.2.1-a002`

### [6G/Rel-20 RAN1#126] `agreement` 10.2.1 Waveform

列出供后续筛选的 UL PAPR reduction 技术：FDSS 不扩展或截断频谱、扩展频谱、截断频谱三种选项，并给出各自的调制方式。适用 SE 范围及最终应用条件仍为 FFS；目标是在 RAN1#126bis 筛选透明性和调制方式。

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

DFT size 在应用 SE/ST 之前至少支持选项 1，即 12 * 2^x3^y5^z 个子载波；选项 2（X * 2^x3^y5^z，X=4）是否支持将在 RAN1#127 决定。选项 2 适用 RB 数量上限仍为 FFS，并安排收集额外评估结果。

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

在通过 DFT-s-OFDM 的 low UL PAPR enhancement 改善 UL coverage 的 RAN1 研究中，优先考虑所列 FDSS cases，包括 π/2 BPSK、QPSK、16QAM，以及 spectral extension 和 spectral truncation 变体。各类 FDSS 均考虑 transparent filter（由 RAN4 通过 transmitter requirement 等定义）或 non-transparent filter（由 RAN1 指定 filter coefficients）；公司也被鼓励报告是否使用 transparent CFR。

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

记录了所列 waveform 提案的研究情况。除非 RAN#112 或之后的 RAN 会议下达任务，否则 RAN1 的 waveform 议题下不计划进一步讨论这些提案。

```text
The study on the following listed proposals is noted. Further discussion on these is not planned under the waveform agenda item in RAN1 unless tasked by RAN at or after RAN#112.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.2.1-c001`

### [6G/Rel-20 RAN1#124b] `observation` 10.2.1 Waveform

材料汇总了 UL DFT-s-OFDM 的 max-rank、接收天线数、功率受限时的 Tx power gain，以及不同 codebook 和 Dynamic waveform switching 设置下的评估结果；系统级增益或损失随场景和评估设置而异。RAN1#124 同意，面向 waveform evaluation 的 2Tx UE DFT-s-OFDM 研究聚焦于 non-coherent CB，但层数少于 Tx 天线数的情况除外。

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

列出了各公司评估的 waveform 提案及其是否建议考虑纳入 6GR TR；所列反馈均为 YES。

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

扩展 RAN1#123 认可的表格，以描述各 waveform 提案作为潜在 RAN1 observation 的特征，并涵盖对 transmitter 和 receiver processing operation 的影响。表格字段包括提案动机、适用链路方向、目标信道与调制、KPI、规范影响、MRSS 兼容性、复用共存、多用户复用、MIMO 兼容性及收发处理影响。

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

评估 UL low-PAPR 方案的 spectrum extension 和 spectrum truncation 时，扩展或截断前的子载波数 A 设有两个选项：12 × 2ˣ3ʸ5ᶻ 或 2ˣ3ʸ5ᶻ。A 是否需要最大值仍为 FFS；占用带宽 B 以 RB 数表示。

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

评估 UL low-PAPR 提案增益时，应使用 NR Rel-15 DFT-s-OFDM 作为基线参考。

```text
NR Rel-15 DFT-s-OFDM should be used as the baseline reference when evaluating the gains of UL low-PAPR proposals.
R1-2600788	Feature Lead summary #3 on 6G waveform	Nokia
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.2.1-a003`

### [6G/Rel-20 RAN1#124] `agreement` 10.2.1 Waveform

多层 UL DFT-s-OFDM 和 CP-OFDM 研究的 SLS 评估采用 User perceived throughput (UPT) 指标，包括 90% 高百分位、均值、中位数及 5/10 百分位小区边缘值；full buffer traffic 下的小区平均吞吐量为可选指标。还鼓励报告所有 UE 的瞬时 UL TX power CDF，以及 UL TX rank 和所用 MCS 的统计数据。

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

多层 UL DFT-s-OFDM 和 CP-OFDM 研究采用 BLER curves（覆盖整个 NR MCS 范围的子集、禁用 HARQ 重传）和 Netgain 作为 LLS 评估指标。Companies 可基于 BLER curves 推导 Link-level throughput vs SNR。

```text
Following metrics are used for LLS evaluation for multi-layer UL DFT-s-OFDM and CP-OFDM studies.
BLER curves (for a subset of NR MCS (covering whole range with spanning), HARQ re-transmissions disabled) for same transmission rank, for same resource allocation and same transmission power for DFT-s-OFDM and CP-OFDM
Companies may derive Link-level throughput vs SNR based on BLER curves
Netgain
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.2.1-a005`

### [6G/Rel-20 RAN1#124] `agreement` 10.2.1 Waveform

针对 2-layer/2Tx UL DFT-s-OFDM 和 CP-OFDM 研究，分别考虑仅支持 non-coherent precoder 和支持 fully-coherent precoder 的 UE。对于 rank-2 transmission，前者的两种 waveform 均仅允许 non-coherent precoder；后者的 CP-OFDM 允许所有 NR precoder options，而 DFT-s-OFDM 仅允许 non-coherent precoder。

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

多层 UL DFT-s-OFDM 和 CP-OFDM 研究中的 NR reference，应假设启用 Release 16 full power mode 1。

```text
For the multi-layer UL DFT-s-OFDM and CP-OFDM studies, the NR reference should be evaluated assuming the Release 16 full power mode 1 to be enabled.
R1-2600789	Feature Lead summary #4 on 6G waveform	Nokia
From Friday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.2.1-a007`

### [6G/Rel-20 RAN1#124] `agreement` 10.2.1 Waveform

列出了供进一步考虑的 DFT-s-OFDM UL low-PAPR proposals，包括 Non-AI-ML-based 和 AI-ML-based 方案。条目明确说明，提案中列出的 tdoc 编号仅提供进一步考虑的提案信息，不代表这些 tdoc 支持该提案。

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

6GR Downlink 的 DFT-s-OFDM waveform 及相关增强不再作为 AI 10.2.1 的讨论内容。DL signal（例如 SS、WUS、sensing）仍可能在相应 AI 中单独讨论。

```text
DFT-s-OFDM waveform including related enhancements for 6GR Downlink will be no further discussed as part of AI 10.2.1.
Note: for DL signal (e.g., SS, WUS, sensing), it may or may not be separately discussed in corresponding AI.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.2.1-c001`

### [6G/Rel-20 RAN1#124] `conclusion` 10.2.1 Waveform

通过 DFT-s-OFDM 的 low UL PAPR enhancement 改善 UL coverage 的研究，在 AI 10.2.1 中按高优先级处理。

```text
Studies on UL coverage improvements through low UL PAPR enhancement for DFT-s-OFDM are to be handled with high priority in AI 10.2.1.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.2.1-c002`

### [6G/Rel-20 RAN1#124] `conclusion` 10.2.1 Waveform

DFT-s-OFDM 多 rank UL MIMO 研究，在 AI 10.2.1 中按高优先级处理。

```text
Studies on DFT-s-OFDM for multi-rank UL MIMO are to be handled with high priority in AI 10.2.1.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.2.1-c003`

### [6G/Rel-20 RAN1#124] `conclusion` 10.2.1 Waveform

评估 DFT-s-OFDM UL low-PAPR proposals 时，公司应披露接收端处理 waveform 所需的知识，例如 filter coefficients 和 extension scheme。

```text
Further clarifications on evaluations of UL low-PAPR proposals for DFT-s-OFDM:
In the evaluation assumptions, companies should disclose the necessary knowledge (e.g., filter coefficients, extension scheme, …) of the waveform at the receiver to process if any.
R1-2601696	Feature Lead summary #5 on 6G waveform	Moderator (Nokia)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.2.1-c004`

### [6G/Rel-20 RAN1#123] `agreement` frame-structure-ecea07cd Frame structure

RAN1 假设 FR2-1 网络侧最大信道带宽为 800MHz 或 400MHz，具体值将在未来择一确定。UE 侧是否采用 800MHz 或 400MHz 仍为 FFS。

```text
RAN1 assumes maximum channel bandwidth 800MHz or 400MHz at network side for FR2-1.
800MHz or 400MHz, to be down-selected in the future
FFS: 800MHz or 400MHz at UE side.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-frame-structure-ecea07cd-a001`

### [6G/Rel-20 RAN1#123] `agreement` frame-structure-ecea07cd Frame structure

研究网络支持 400 MHz CBW 时使 UE 支持 400 MHz 带宽的选项，包括假设 single FFT 和 2 RF chain 的 Option 5。还需研究 BB processor 的分离或并行方式、各选项的规范影响及性能、能效、成本和复杂度，并将信息告知 RAN4。

```text
For how to enable UE to support 400MHz bandwidth when a network supports 400 MHz Channel Bandwidth (CBW), the following options 1/2/3/4/5 are considered from RAN1 understanding for studying
Option 5: Variance of Option 3 by assuming single FFT and 2 RF chain.
FFS which aspects of the BB processor in option 3 and 4 should be separated/parallelled.
Note: DL and UL design options may be considered independently.
To provide potential specification impact of each option.
To provide investigations on performance/energy efficiency/cost/complexity for the above options.
Inform RAN4 about the above information.
R1-2509577	Draft LS on 400MHz maximum bandwidth around 7GHz	CMCC
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-frame-structure-ecea07cd-a002`

### [6G/Rel-20 RAN1#123] `agreement` frame-structure-ecea07cd Frame structure

Draft LS R1-2509577 原则上获认可，最终 LS R1-2509578 获批准。

```text
Draft LS R1-2509577 is endorsed in principle. Final LS is approved in R1-2509578.
R1-2509625	FL summary for Frame Structure (Final)	Moderator (CMCC)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-frame-structure-ecea07cd-a003`

### [6G/Rel-20 RAN1#123] `conclusion` frame-structure-ecea07cd Frame structure

TN communication 的 Extended CP 不再继续研究。

```text
Extended CP will not be further studied for TN communication.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-frame-structure-ecea07cd-c001`

### [6G/Rel-20 RAN1#123] `agreement` waveform-6eae1e79 Waveform

在 RAN1#122b 已有协议基础上，为 UL PAPR reduction 增加评估指标：在 spectral efficiency 相近且 occupied bandwidth 相同条件下的 Net gain@10% BLER，以及 ACLR、EVM 和 IBE。

```text
Add the following metrics for UL PAPR reduction to the existing agreement (made in RAN1#122b)
Net gain@10% BLER assuming similar spectral efficiency and same occupied bandwidth for each compared method
ACLR, EVM, IBE
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-waveform-6eae1e79-a001`

### [6G/Rel-20 RAN1#123] `agreement` waveform-6eae1e79 Waveform

为 UL low-PAPR proposals 设定通用评估假设，包括 4GHz 载频、Urban 场景至少 100MHz Channel BW、30 kHz SCS 和 TDL-C 300ns 信道模型。还规定 UE speed 为 3km/h、TDL 信道下 1 个 Tx 天线和 1 或 4 个 Rx 天线、每 slot 2 个 DMRS 与 12 个 PUSCH 数据符号，并采用无重传 HARQ、禁用 frequency hopping。

```text
General evaluation assumptions for UL low-PAPR proposals
|  | 3GPP 6GR |
| --- | --- |
| Carrier frequency and scenario | 4GHz |
| Channel BW | At least 100MHz for Urban (4GHz) |
| Occupied BW | To be discussed with detailed simulation assumptions |
| SCS | 30 kHz for 4GHz |
| Channel model | TDL-C 300ns for 4GHz |
| UE speed | 3km/h |
| Number of Tx antennas for TDL channel | 1 |
| Number of Rx antennas for TDL channel | 1 and 4 for 4GHz |
| Number of DMRS symbols/slot (location as defined in NR) | 2 |
| Number of PUSCH data symbols/slot | 12 |
| HARQ configuration | No retransmissions |
| Frequency hopping | Disabled |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-waveform-6eae1e79-a002`

### [6G/Rel-20 RAN1#123] `agreement` waveform-6eae1e79 Waveform

规定 UL low-PAPR proposals 在 single user 评估中，针对 spectrum extension 和 spectrum truncation 分别使用 MCS 与子载波数量报告假设，并列出扩展或截断前后的子载波数及 occupied bandwidth。其他 extension 或 truncation 数值不受排除。

```text
For single user evaluation assumption for MCS and subcarriers UL low-PAPR proposals with spectrum extension
| No Spectrum Extension | With Spectrum Extension |  |  |  |
| --- | --- | --- | --- | --- |
| MCS | #subcarriers | #SCs before extension ) | Occupied BW: #SCs after extension () | Spectrum extension Extension: |
| NR MCS |  |  |  |  |
For single user evaluation assumption for MCS and subcarriers UL low-PAPR proposals with spectrum truncation
| No Spectrum Truncation | With Spectrum Truncation |  |  |  |
| --- | --- | --- | --- | --- |
| MCS | #subcarriers | #SCs before truncation ) | Occupied BW: #SCs after truncation () | Spectrum truncation factor Truncation: |
| NR MCS |  |  | 𝐵 |  |
Note: other values for extension or truncation are not precluded.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-waveform-6eae1e79-a003`

### [6G/Rel-20 RAN1#123] `agreement` waveform-6eae1e79 Waveform

对 CP-OFDM 和 DFT-S-OFDM 的 tone reservation UL low-PAPR proposals，规定 single user 评估需报告 MCS、occupied bandwidth 中的子载波数、保留 tone 数量（inband/sideband）及保留比例。

```text
For both CP-OFDM and DFT-S-OFDM, for single user evaluation assumption for MCS and subcarriers UL low-PAPR proposals with tone reservation.
| MCS | Occupied BW: #subcarriers | #reserved tones (inband/sideband) | Ratio of reserve |
| --- | --- | --- | --- |
| NR MCS |  |  | A/𝐵 |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-waveform-6eae1e79-a004`

### [6G/Rel-20 RAN1#123] `agreement` waveform-6eae1e79 Waveform

通过用表格表征各 waveform proposal，作为潜在的 RAN1 observation。表格涵盖提案动机、适用链路方向、波形增强、目标信道或信号、KPI、规范影响及兼容性等项目。

```text
Table is endorsed to characterize each proposal as a potential RAN1 observation.
Characterization of each waveform proposal
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
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-waveform-6eae1e79-a005`

### [6G/Rel-20 RAN1#123] `agreement` waveform-6eae1e79 Waveform

UL PAPR reduction 评估采用 occupied BW B 对应的 PRB 数值：2、4、8、16、24、30、32、64、128、240、256；其他 PRB allocation 也允许考虑。还应考虑 TS 38.101 定义的 edge、outer 和 inner PRB allocations。

```text
For UL PAPR reduction, values for occupied BW B:
{2, 4, 8, 16, 24, 30, 32, 64, 128, 240, 256} PRBs.
Other PRB allocations are not precluded.
Edge, outer and inner PRB allocations as defined in TS 38.101 should be considered.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-waveform-6eae1e79-a006`

### [6G/Rel-20 RAN1#123] `agreement` waveform-6eae1e79 Waveform

Performance benefit 需通过 link level 和 system level simulation 评估，metrics 仍待确定。条目给出了 multi-layer UL waveform link level study 的参数，包括 4 GHz、30 kHz、CP-OFDM/DFT-s-OFDM、2 或 4 layers、10% BLER target 等。

```text
Performance benefit to be evaluated using both link level and system level simulation.
FFS: metrics
Link level configuration for multi-layer UL waveforms study.
| Parameters | Values |
| --- | --- |
| Carrier frequency​​ | 4 GHz |
| Subcarrier spacing​​ | 30 kHz​​ |
| UE antenna ports | 2, 4 |
| BS antenna ports | 64, port reduction is not precluded |
| FDRA | 4, 8, 16, 32, 64​​ |
| Waveform​​s | CP-OFDM DFT-s-OFDM​​ |
| MCS/modulation​​ | NR UL MCS table with 256 QAM |
| Number of layers​ | 2 layers​​, 4 layers |
| Channel model​​ | CDL-A30​​, TDL-C300, CDL-C300, |
| UE speed​​ | 3km/h​​, 30 km/h |
| Channel est.​​ | Practical​ |
| SRS periodicity | To be reported by the company |
| Receiver | LMMSE |
| HARQ retransmission​ | Disabled |
| DMRS configuration | Configuration type 1 2 DMRS symbols per slot |
| Number of PUSCH data | 12 symbols |
| Waveform and MIMO configuration | 5G codebook, to be reported by the company |
| BLER target | 10% |
| Frequency hopping | Disabled |
| Power class and power mode | Option 1: PC2, total power limited to 26 dBm. MaxRank 2: Each PA is limited to 23 dBm MaxRank 4: Each PA is limited to 20 dBm Option2: PC3, total power limited to 23 dBm. MaxRank 2: Each PA is limited to 20 dBm MaxRank 4: Each PA is limited to 17 dBm |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-waveform-6eae1e79-a007`

### [6G/Rel-20 RAN1#123] `agreement` waveform-6eae1e79 Waveform

规定了 multi-layer UL CP-OFDM/DFT-s-OFDM system level study 的配置，包括 UMa 21 cells、每小区 10/30/50 UEs、至少 100 MHz 带宽和 30 kHz 子载波间隔等。UL low-PAPR proposals 的 link level multi-user evaluation 假设为 2 users，并列出 RB overlap、baseline scheme、MCS 对齐方式及由提案方报告 receiver 类型。

```text
Table: System level configuration for multi-layer UL CP-OFDM/DFT-s-OFDM study:
| Parameters | Values |
| --- | --- |
| System configuration | UMa, 21 cells, 10, 30 or 50 UEs/cell Detailed parameters not listed in this table according to UMa as defined in AI 11.2 |
| Traffic model | FTP model 3, 0.5 Mbyte packet sizes Network load up to companies to report Full buffer (optional, for calibration) |
| Carrier frequency | 4 GHz |
| Channel bandwidth/Subcarrier spacing | At least 100 MHz, 30KHz |
| Frame structure | TDD (DDDSU), S-slot D:G:U as 10:2:2 |
| UE antenna ports | Same as link level |
| BS antenna ports | Outdoor Combination 2 for UMa as agreed in 11.2 |
| UE antenna model | The UE handheld model as agreed in AI 11.2, companies to report the used model. |
| ISD | 500 m |
| Maximum Number of layers (maxRank) per UE | Adaptive rank, maxRank 2 or 4 SU-MIMO |
| Receiver | Same as link level, port reduction mapping to be reported |
| Waveform and MIMO configuration | Same as link level |
| Power class and power mode | Same as link level |
| UL Maximum power | MPR based Pcmax according to modulation/FDRA/waveform/coherency/etc. Option 1: 38.101-1 section 6.2D definition Option 2: Based on a realistic PA model |
| UL Power Control Settings | P0 and Alpha to be reported by the company |
| SRS periodicity | To be reported by the company |
Table: Link level multi-user evaluation assumption for UL low-PAPR proposals
| Parameters | Values |
| --- | --- |
| User # | 2 users |
| RB allocation | X RBs per UE, with Y RB overlap. I.e. 2X-Y RBs as the total occupied BW |
| Per user configuration | As in the single user sim assumptions agreed earlier. |
| Multi-user overlap RBs | Reported by companies |
| Baseline scheme | No spectrum extension/truncation. (2X-Y)/2 RB as the occupied BW for each simulated UE. |
| Per UE MCS | Chosen to align with the spectral efficiency |
| Receiver type | The receiver type/algorithm to be reported by the proponent |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/) · `RAN1-123-waveform-6eae1e79-a008`

### [6G/Rel-20 RAN1#122] `agreement` frame-structure-ecea07cd Frame structure

6GR 将除 PRACH 外的所有信号和信道的 SCS 作为讨论起点。低于 6 GHz 时至少支持 FDD 15kHz、TDD 30kHz；约 7 GHz 可研究 30/60kHz，24.25–52.6 GHz 支持 120kHz，其他列出的 SCS 选项是否讨论仍待 RANP 决定或保持 FFS。

```text
6GR takes the following SCS as start point for discussion for all the signals/channels except PRACH.
For sub 6GHz
The following subcarrier spacing is at least supported
15kHz SCS for FDD, 30kHz SCS for TDD
FFS: 30kHz SCS for FDD for around e.g., 1-2.5GHz
FFS: 7.5kHz SCS for sub1GHz (FDD)
Whether to discuss the FFS will be subject to RANP decision.
For around 7GHz
The following subcarrier spacing options can be studied
30kHz, 60kHz
FFS: For around 15GHz
The following subcarrier spacing options can be studied
30kHz, 60kHz, 120kHz
Whether to discuss it will be subject to RANP decision
For between 24.25GHz - 52.6GHz
Subcarrier spacing 120kHz is supported
FFS whether to allow using additional subcarrier spacing for SSB
FFS subcarrier spacing for PRACH and up to initial access discussion.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-frame-structure-ecea07cd-a001`

### [6G/Rel-20 RAN1#122] `agreement` frame-structure-ecea07cd Frame structure

6GR 支持 normal cyclic prefix，即与 NR 定义的 normal CP 相同。是否需要其他 CP 仍为 FFS。

```text
6GR supports normal cyclic prefix, i.e., same as the normal CP defined in NR.
FFS potential need for other CP.
Final summary in R1-2506604.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-frame-structure-ecea07cd-a002`

### [6G/Rel-20 RAN1#122] `conclusion` frame-structure-ecea07cd Frame structure

sensing 的 numerologies 由 sensing 议题讨论决定。

```text
Numerologies for sensing is up to sensing agenda discussion.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-frame-structure-ecea07cd-c001`

### [6G/Rel-20 RAN1#122] `agreement` waveform-6eae1e79 Waveform

6GR 上行以 5G NR 定义的 CP-OFDM 和 DFT-s-OFDM 波形为基础。对两种波形的增强或修改将作为潜在补充进行研究，且不排除其他基于 OFDM 的波形。

```text
CP-OFDM and DFT-s-OFDM waveforms as defined in 5G NR are supported as the basis for 6GR for uplink
Enhancements/modifications on CP-OFDM/DFT-s-OFDM will be studied as potential additions
Other OFDM based waveforms are not precluded.
R1-2506595	Feature Lead summary #2 on 6GR waveform	Moderator (Nokia)
From Friday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-waveform-6eae1e79-a001`

### [6G/Rel-20 RAN1#122] `agreement` waveform-6eae1e79 Waveform

6GR 下行以 5G NR 定义的 CP-OFDM 波形为基础，其增强或修改将作为潜在补充进行研究；DFT-s-OFDM 或其他基于 OFDM 的波形也将作为潜在下行补充波形研究。提案者需说明目标用例、信号/信道及与 CP-OFDM（包括 MRSS）的复用方式等，并提供相关性能、兼容性和复杂度信息。

```text
CP-OFDM waveform as defined in 5G NR is supported as the basis for 6GR for downlink
Enhancements/modifications on CP-OFDM will be studied as potential additions
DFT-s-OFDM or any other OFDM-based waveform will be studied as a potential additional waveform for downlink
Note: proponents to identify at least the target use cases, signals/channels to use the waveform, and how the proposal is intended (if applicable) to support multiplexing with CP-OFDM, including MRSS, and how multi-user multiplexing is supported, etc.
Note:
Proponents are encouraged to provide more detailed information on their proposals for the next meeting, e.g.:
Proponents to characterize the main motivation for modification/additional waveform proposals:
Targeted link direction, i.e. DL, UL or both
Targeted use case (e.g. NTN, specific frequency range, etc.), if any
Potential motivations metrics used, and quantified gains for a proposal, e.g.
Coverage
Network energy efficiency
UE energy efficiency
Spectral efficiency
High speed tolerance
Scheduling flexibility
Integration with ISAC
Proponents provide information on the following aspects, if applicable
MRSS compatibility
Target channels/signals, e.g. all channels, PxSCH only, etc.
MIMO (SU and MU-MIMO) compatibility
Target modulations, and impact to other modulations, if applicable
Multi-user multiplexing/scheduling flexibility
Multiplexing/coexistence with baseline waveforms
Impact on synchronization and initial access
Expected specification impact
Transmitter/receiver complexity and impact to power consumption.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/) · `RAN1-122-waveform-6eae1e79-a002`

