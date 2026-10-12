# 6GR 空口评估假设

**当前进展** · 阶段：收敛中

RAN1#124 已为 6GR 评估规定多类载频下的 UE、CPE 与 BS 天线配置及辐射假设，并更新了功率、UE 分布和速度等系统级仿真条件。FTP3 extension 和 Massive Communication (IoT) 的业务负载假设也已给出，包括多包大小模型及可选的较大 L2 PDU。整体评估框架已较为具体，但若干配置仍需公司报告或在评估阶段进一步确定。

**未决问题**

- FWA 场景的适用性仍为 FFS。
- 约 30 GHz 场景的具体仿真功率由公司报告；低于 30 GHz 的 EIRP limit 也可进一步考虑。
- 室内与室外 CPE 的预选标准或机制可在评估阶段讨论。
- 其他 UE 天线配置及 FTP3 Alt2 相关取值仍可由公司报告或在评估阶段决定。
- TR38.914 中 RAN1 尚未讨论的场景仍属于候选评估场景。

## 6GR 演进

### [6G/Rel-20 RAN1#124] `agreement` 10.1 Evaluation assumptions for 6GR air interface

为低于 30 GHz 的 6GR evaluation 规定 UE antenna modelling 组合，覆盖 1、2、4、8、16 个 antenna elements，并列出对应 TXRU、Alt 1/Alt 2 配置及适用载频。Alt 1 和 Alt 2 中的天线位置作为性能校准示例；TR 38.901 section 7.3 的其他天线阵列结构或位置也可用于评估。

```text
For 6GR evaluation, RAN1 to model the UE antenna as follows for below 30GHz carrier frequency,
Note: Each of other topics could further decide to use which combination(s) for the evaluations. Other combinations are not precluded for evaluations, e.g., 2T6R, 3T6R, 6T6R, 6T8R.
Note: The antenna locations in Alt1 and Alt 2 in the following table are considered as examples and used for performance calibration. Any antenna array structures and/or antenna locations in section 7.3 in TR38.901 is possible for evaluations and up to companies to report.
Note: The antenna locations in Alt 2 not included in section 7.3 in TR38.901 are up to companies to report.
Note: The antenna element-wise power variation at the UE in TR 38.901 section 7.6.14.2 can be optionally considered for Alt2 for handheld devices.
Note: The radiation power pattern of a single antenna element in Table 7.3-2 TR38.901 is assumed for Alt2. The isotropic radiation power pattern is assumed for Alt1 at least for handheld devices.
Note: The antenna element/location of T is a subset of the element/locations for R.
Note: The mapping between the combination and the device types might be separately discussed.
| UE antenna modelling for RAN1 evaluations | Total number of antenna elements | Total number of TXRU | Alt 1: (M,N,P,Mg,Ng; Mp,Np), (dH,dV), (dg,H,dg,V) if any, or Alt 2: UT device antenna model using candidate antenna locations as described in section 7.3 in TR38.901 | Applicable carrier frequency |
| --- | --- | --- | --- | --- |
| Combination0 NOTE1 | 1 | 1T1R, | Alt 1: 1T: (M, N, P, Mg, Ng; Mp, Np)=(1, 1, 1, 1, 1; 1, 1) 1R: (M, N, P, Mg, Ng; Mp, Np)=(1, 1, 1, 1, 1; 1, 1) Alt 2: 1T 1R | 700MHz, 2GHz |
| Combination1 | 2 | 1T2R, | Alt 1: 2R: (M, N, P, Mg, Ng; Mp, Np)=(1, 2, 1, 1, 1; 1, 2) for single polarization or (1, 1, 2, 1, 1; 1, 1) for dual polarization, (dH,dV)= (0.5, 0.5)λ Alt 2: 2R: [(1, 5), or (4, 8)] as described in section 7.3 in TR 38.901. | 700MHz, 2GHz, 4GHz |
| Combination2 | 4 | 1T4R, 2T4R, 4T4R | Alt 1: 4R: (M, N, P, Mg, Ng; Mp, Np)=(1, 2, 2, 1, 1; 1, 2) for dual polarization or (2, 2, 1, 1, 1; 2, 2) for single polarization, (dH,dV)= (0.5, 0.5)λ Alt 2: 4R: [(2, 4, 6, 8), or (1, 3, 5, 7)] as described in section 7.3 in TR 38.901 | 700MHz, 2GHz, 4GHz, 7GHz, 15GHz NOTE3 |
| Combination3 | 8 | 1T8R, 2T8R, 4T8R, 8T8R | Alt 1: (M, N, P, Mg, Ng; Mp, Np)= (1, 4, 2, 1, 1; 1, 4), or (2, 2, 2, 1, 1; 2, 2) for dual polarization or (2, 4, 1, 1, 1; 2, 4) for single polarization , (dH,dV)= (0.5, 0.5)λ Alt 2: (1, 2, 3, 4, 5, 6, 7, 8) as described in section 7.3 in TR38.901 | 2GHz, 4GHz, 7GHz, 15GHz NOTE3 |
| Combination4 NOTE2 | 16 | 4T16R 8T16R, | Alt 1: 16R: (M, N, P, Mg, Ng; Mp, Np)= (2, 4, 2, 1, 1; 2,4) , (dH,dV)= (0.5, 0.5)λ Alt2: Company to report the antenna placement, directional pattern orientation of the CPE panel. | 7GHz, 15GHz |
| NOTE1: This combination is for IoT UE only. NOTE2: This combination is for CPE UE only. NOTE3: If number of TXRU and frequency combination is applicable. |  |  |  |  |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.1-a001`

### [6G/Rel-20 RAN1#124] `agreement` 10.1 Evaluation assumptions for 6GR air interface

为约 30 GHz 载频的 6GR evaluation 规定 UE antenna configuration 遵循 Table 1，UE antenna radiation pattern 遵循 Table 2。其他天线配置也可考虑，并由公司报告。

```text
For 6GR evaluation, RAN1 to model the UE antenna as follows for around 30GHz carrier frequency,
UE antenna configuration follows Table 1 below.
UE antenna radiation pattern follows Table 2 below.
Other antenna configuration can be considered and up to companies to report.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.1-a002`

### [6G/Rel-20 RAN1#124] `agreement` 10.1 Evaluation assumptions for 6GR air interface

给出了约 30 GHz UE 天线配置：每个 panel 为 8 个 antenna elements，Config 0、1、2 分别采用 1、2、4 个 panels，并规定每 panel 的 TXRU 配置。天线单元最大方向增益 GE,max 为 5 dBi。

```text
Table 1: UE antenna configuration for around 30GHz
| UE antenna configuration | Values |
| --- | --- |
| # of antenna elements per panel | 8 elements per panel (M, N, P) = (2, 2, 2) for Config 1 and Config 2. (M, N, P, Mg, Ng; Mp, Np) = (4, 1, 2, 1, 1; 1, 1) for Config 0. (M, N, P, Mg, Ng; Mp, Np) = (4, 4, 2, 1, 1; 1, 1) for CPE only for Config 0. |
| # of panels | Config 0: 1 panel. Config 1: 2 panels on front and back; Config 2: 4 panels on 4 edges. |
| # of TXRUs | 2T2R per panel - The antenna elements of the same polarization of the same panel is virtualized into one TXRU |
25
,
90
,
,
90
12
min
)
(
0
3
2
3
0
,
=
=
ú
ú
û
ù
ê
ê
ë
é
÷
÷
ø
ö
ç
ç
è
æ
-
¢
¢
-
=
¢
¢
V
dB
V
dB
V
E
SLA
SLA
A
q
q
q
q
Table 2: UE antenna radiation pattern for around 30GHz [see Table A.2.1-8 TR38.802]
| Parameter | Values |
| --- | --- |
| Antenna element radiation pattern in dim (dB) |  |
| Antenna element radiation pattern in dim (dB) |  |
| Combining method for 3D antenna element pattern (dB) |  |
| Maximum directional gain of an antenna element GE,max | 5dBi |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.1-a003`

### [6G/Rel-20 RAN1#124] `agreement` 10.1 Evaluation assumptions for 6GR air interface

规定 6GR evaluation 的 FWA/CPE 单天线单元辐射方向图候选包括 Isotropic、具有不同 half power beamwidth 和 maximum directional gains 的 Directional，以及 Omnidirectional。CPE 可配备 1 至 3 个天线面板，且面板方向可优化。

```text
For 6GR evaluation, RAN1 to model the radiation pattern of a single antenna element for FWA/CPE including,
Candidate1: Isotropic,
Candidate2: Directional with different half power beamwidth and maximum directional gains as described in Table 1 below,
CPE can be equipped with 1 to 3 antenna panels, each following Alt 1 ((M,N,P,Mg,Ng; Mp,Np), (dH,dV)) configuration.
Candidate3: Omnidirectional as described in Table 2 below.
Note: The orientation of the CPE panel can be optimized.
Table 1: Directional radiation power pattern of a single antenna element for CPE
| Parameter | Values |
| --- | --- |
| Vertical cut of the radiation power pattern (dB) |  |
| Horizontal cut of the radiation power pattern (dB) |  |
| 3D radiation power pattern (dB) |  |
| Maximum directional gain of an antenna element | GE,max dBi |
| Company reports, e.g., |  |
Table 2: Omnidirectional radiation power pattern of a single antenna element for CPE
| Parameter | Values |
| --- | --- |
| Vertical cut of the radiation power pattern (dB) |  |
| 3D radiation power pattern (dB) | for any |
| Maximum directional gain of an antenna element, GE,max | 5 dBi |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.1-a004`

### [6G/Rel-20 RAN1#124] `agreement` 10.1 Evaluation assumptions for 6GR air interface

定义约 4 GHz 载频下的 4 TXRU outdoor BS antenna configuration：32 个 antenna elements、4 个 TXRU，阵列参数为 (8, 2, 2, 1, 1; 1, 2)，(dH,dV)=(0.5, 0.8)λ。该组合标为 Optional。

```text
Define a 4 TXRU outdoor BS antenna configuration for about 4GHz carrier frequency as below.
| Outdoor |  |  |  |  |
| --- | --- | --- | --- | --- |
| BS antenna modelling | Total number of antenna elements | Total number of TXRU | (M, N, P, Mg , Ng; Mp, Np) | (dH,dV) |
| Combination 0 (Optional) | 32 | 4 | (8, 2, 2, 1, 1; 1, 2) | (0.5, 0.8)λ |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.1-a005`

### [6G/Rel-20 RAN1#124] `agreement` 10.1 Evaluation assumptions for 6GR air interface

系统级仿真中，低于 30 GHz 时仅 CPE 假设 UE transmission power 为 35 dBm，并注明可考虑 EIRP limit。约 30 GHz 的各场景表格规定 peak EIRP 下限 23 dBm、上限 43 dBm；仅 CPE 的范围为 35 至 55 dBm，具体仿真功率由公司报告。

```text
Regarding the agreement on UE transmission power assumptions in system-level simulation, the further update is highlighted as follows in red:
Transmission power of 35dBm is assumed for CPE only for below 30GHz.
Note: EIRP limit could be considered
| UE power class | Indoor Hotspot | Dense Urban | Rural | Urban Macro | Sub-urban macro |
| --- | --- | --- | --- | --- | --- |
| Around 30GHz | Minimum peak EIRP: 23dBm. EIRP should not exceed 43dBm. For CPE only (NOTE1): 35dBm<=peak EIRP<=55dBm. | Minimum peak EIRP: 23dBm. EIRP should not exceed 43dBm. For CPE only (NOTE1): 35dBm<=peak EIRP<=55dBm. | NA | Minimum peak EIRP: 23dBm. EIRP should not exceed 43dBm. For CPE only (NOTE1): 35dBm<=peak EIRP<=55dBm. | Minimum peak EIRP: 23dBm. EIRP should not exceed 43dBm. For CPE only (NOTE1): 35dBm<=peak EIRP<=55dBm. |
|  | NOTE1: It is up to company to report the simulated transmission power confined within the defined peak EIRP range. |  |  |  |  |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.1-a006`

### [6G/Rel-20 RAN1#124] `agreement` 10.1 Evaluation assumptions for 6GR air interface

评估中，BS Tx power 随带宽按比例增加，并受最大功率限制：室外为 56dBm、室内为 33dBm。option1 的值引用 Report ITU-R M. [IMT-2030. EVAL]；option2 的值按模拟带宽比例缩放，并受最大 BS Tx power 56dBm 限制。

```text
Regarding the gNB transmission power assumptions in the evaluations, update the second note of the agreement as follows:
| Note: For evaluation purpose, BS Tx power scales up with bandwidth proportionally under the limitation of the maximum BS Tx power is 56dBm for outdoor and 33dBm for indoor for the above carrier frequencies. Note: The values defined in option1 refer to the Report ITU-R M. [IMT-2030. EVAL]. The values defined in option2 is calculated based on the proportional scaling with simulation bandwidth under the limitation of the maximum BS Tx power of 56dBm. |
| --- |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.1-a007`

### [6G/Rel-20 RAN1#124] `agreement` 10.1 Evaluation assumptions for 6GR air interface

系统级模拟的 UE 分布和速度表进一步更新，涵盖 Indoor Hotspot、Dense Urban、Rural、Urban Macro 和 Suburban Macro 场景，并列出各场景的 UE 数量、室内外比例及速度选项。FWA 的适用性仍为 FFS；每个 micro TRxP 假设的 UE 数量不大于对应 macro TRxP。

```text
The agreed table for UE distribution and UE speed for system-level simulation, the further update is highlighted in cyan as follows:
| Parameters | Indoor Hotspot | Dense Urban | Rural | Urban Macro | Suburban Macro |
| --- | --- | --- | --- | --- | --- |
| UE distribution and UE speed | 10 users per TRxP. Opt1: 100% Indoor, 3km/h | Single layer: Uniform/macro TRxP Two layers: Uniform/macro TRxP + Clustered/micro TRxP UE number per TRxP is [10, 30, 50] NOTE1. Opt1: 80% indoor (3km/h); 20% outdoor in cars (30km/h). Opt2: 40% indoor (3km/h) 40% outdoor (3km/h) 20% outdoor in cars (30km/h). | Single layer: Uniform/macro TRxP UE number per TRxP is [10, 30, 50]. Opt1: 50% indoor (3km/h); 50% outdoor in cars (120km/h). Opt2: 20% indoor (3km/h) 40% outdoor (60km/h) in cars 40% outdoor in cars (120km/h). | Single layer: Uniform/macro TRxP Two layers: Uniform/macro TRxP + Clustered/micro TRxP UE number per TRxP is [10, 30, 50] NOTE1. Opt1: 80% indoor (3km/h); 20% outdoor in cars (30km/h). Opt2: 40% indoor (3km/h) 40% outdoor (3km/h) 20% outdoor in cars (30km/h). | Single layer: Uniform/macro TRxP UE number per TRxP is [10, 30, 50]. Opt1: 10% Outdoor pedestrian: 3km/h; 10% Outdoor in cars: 40km/h; 80% Indoor in houses: 3km/h. Opt2: 20% outdoor in cars: 40km/h 80% indoor in houses: 3km/h |
| FFS: Applicability for FWA NOTE1: Regarding the number of UEs per TRxP, a smaller or the same number of UEs is assumed for each micro TRxPs compared to each macro TRxPs. |  |  |  |  |  |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.1-a008`

### [6G/Rel-20 RAN1#124] `agreement` 10.1 Evaluation assumptions for 6GR air interface

RAN1 将在 6GR 评估中采用表列的 CPE antenna height、UE distribution 和 UE speed 假设，覆盖 Rural、Urban Macro 和 Suburban Macro。室内与室外 CPE 的预选标准或机制可在评估阶段进一步讨论。

```text
RAN1 to assume the UE antenna height and UE distribution for CPE for 6GR evaluations as follows:
Note: Indoor and outdoor CPE pre-selection criterion or mechanism could be further discussed in the evaluation phase.
| Parameters | Rural | Urban Macro | Suburban Macro |
| --- | --- | --- | --- |
| Antenna height for CPE only | Indoor CPEs: follow the heights in 38.901 for RMa. Outdoor CPEs: 1m above rooftop. Building heights modeled as 3m or 6m, equally likely. | Indoor CPEs: follow the heights in 38.901 for UMa. Outdoor CPEs: 1m above building height in 38.901 for UMa | Indoor CPEs: follow the heights in 38.901 for SMa. Outdoor CPEs: 1m above building height in 38.901 for SMa |
| UE distribution and UE speed for CPE only | Profile 1 (mixed deployment): 80% Indoor CPE: (0, 0.3] km/h; 20% Outdoor rooftop mounted CPE: (0, 0.3]km/h. Profile 2 (Indoor CPE only): 100% Indoor: (0, 0.3]km/h. Profile 3 (Outdoor mounted CPE only): Rooftop mounted; 100% Outdoor: (0, 0.3] km/h. |  |  |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.1-a009`

### [6G/Rel-20 RAN1#124] `agreement` 10.1 Evaluation assumptions for 6GR air interface

FTP3 extension 的多包大小配置设定为 X=2，各包大小的到达服从 Poisson distribution，且 λ₁=K·λ₂、K≥1，并假设 S₁<S₂。Alt1 为每个 UE 模拟一种包大小，UE 数量比为 G；Alt2 为每个 UE 以独立 Poisson Process 模拟两种包大小，相关取值可在评估阶段决定。

```text
Regarding FTP3 extension with multiple packet sizes:
The number of packet sizes X = 2;
For each packet size S_i, the packets arrive according to Poisson distribution (as FTP 3) with mean inter-arrival time T_i  (or arrival rate λ_i where T_i = 1/ λ_i);
For Alt1: Y=1 packet size is simulated for each UE
For FTP3-extension with X=2, K is the ratio between arrival rates of the packet sizes, i.e., λ_1= K·λ_2, with K>=1, assuming S_1<S_2,
G>=1 is the ratio between the number of UEs with packet size S_1 and S_2, respectively.
Values of S_i, λ_i, i=1, 2, and G can be decided in evaluation phase.
Note: The following table is an illustration of the traffic configurations.
|  | Example 1 | Example 2 | Example 3 |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Packet Type | Small size, i=1 | Large size, i=2 | Small size, i=1 | Large size, i=2 | Small size, i=1 | Large size, i=2 |
| S_i | 10KB | 500KB | 4KB | 400KB | 10KB | 100KB |
| λ_i | λ_1= K·λ_2, e.g., K=[3, 5, 8, 10] |  |  |  |  |  |
| G | N_1= G·N_2, e.g., G=[2, 4, 9] |  |  |  |  |  |
|  | N_1 is the number of UEs with small packet size S_1; N_2 is the number of UEs with large packet size S_2. |  |  |  |  |  |
For Alt2: Y=X=2 packet sizes are simulated for each UE
The packet of each size is generated following the independent Poisson Process (S_i, λ_i) with i=1,2.
K is the ratio between arrival rates of the packet sizes, i.e., λ_1= K·λ_2, with K>=1, assuming S_1<S_2.
Values of (S_i, λ_i) with i=1,2 can be decided in evaluation phase.
Note: The following table is an illustration of the traffic configurations.
|  | Example 1 | Example 2 | Example 3 |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Packet Type | Small size, i=1 | Large size, i=2 | Small size, i=1 | Large size, i=2 | Small size, i=1 | Large size, i=2 |
| S_i | 10[4]KB | 400[800]KB | 100KB | 500KB | 10KB | 100KB |
| λ_i | λ_1= K·λ_2, e.g., K=[3, 5, 8, 10] |  |  |  |  |  |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.1-a010`

### [6G/Rel-20 RAN1#124] `agreement` 10.1 Evaluation assumptions for 6GR air interface

针对 Massive Communication (IoT) 的 6GR 评估，除 IMT-2030 L2 PDU 的 32 bytes 消息大小外，也可评估更高业务负载，例如采用 320 bytes 的较大 L2 PDU 消息大小。

```text
For 6GR evaluations related to Massive Communication (IoT),
In addition to the IMT-2030 L2 PDU message size of [32] bytes, evaluation of higher traffic loads can be used, e.g., evaluation with a larger L2 PDU message size of [320] bytes.
R1-2601697	Collection of agreements for R20 6GR evaluation assumptions	Moderator (Huawei)
Final summary in R1-2601416.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.1-a011`

### [6G/Rel-20 RAN1#124] `conclusion` 10.1 Evaluation assumptions for 6GR air interface

TR38.914 中已涵盖但 RAN1 尚未讨论的场景，也属于 RAN1 进行 6GR 评估的候选场景。

```text
The scenarios captured in TR38.914 but are not discussed in RAN1 are also candidate scenarios for RAN1 evaluations for 6GR.
R1-2601415	FLS#2 on evaluation assumptions for 6GR air interface	Moderator (Huawei)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.1-c001`

