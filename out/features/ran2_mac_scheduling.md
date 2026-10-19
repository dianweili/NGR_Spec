# 6GR MAC 与调度

**当前进展** · 阶段：收敛中

RAN2#132 至 #134 已形成 6GR MAC 与调度的若干基线：支持 dedicated SR、buffer/delay status reporting、基于序列号的 L2 ARQ recovery，并以 legacy per-LCG reporting 和 NR 4-step/2-step RA 等作为起点。工作重点包括评估 CB-PUSCH 对低时延和资源效率的收益、增强 CG 的灵活配置与资源回收，以及改进 scheduling information reporting 和 LCP，以适配突发、时延敏感及具备不同 QoS 的业务。部分方向已有共识或评估假设，例如 4-step 与 2-step RA 均受支持、UE 可配置多个 CG，以及 CB-PUSCH 评估从共享资源传输 BSR 开始。整体仍处于收敛阶段，关键机制的适用范围、细节及与物理层设计的协同尚未全部确定。

**未决问题**

- CB-PUSCH 是用于一般上行目的还是限于 BSR，以及其相对 SR/其他方案在碰撞、时延和资源效率上的表现仍待评估；评估还依赖 UE population、traffic models 和 RAN1 物理层输入。
- 统一的 BSR/DSR 或上行状态报告机制仍待明确，包括报告内容与粒度、触发条件、格式，以及是否包含 data importance、anticipated arrival 等信息。
- LCP 与 UL grant 的增强粒度、动态参数调整方式，以及如何权衡 DCI 开销、QoS 适配和多种性能目标仍待研究。
- CG 的配置更新、动态激活与资源回收机制，以及其相对 dynamic grant 的适用性仍待进一步明确。
- 2-step/4-step RA 的统一方式、CB-PUSCH 与 RACH 的关系、fallback 条件、RACH partitioning 及动态资源分配细节仍有待解决。

## 跨会议演进脉络（6G）

2025年11月至2026年5月，6GR MAC 与调度从研究方向逐步推进到评估假设和基本协议行为的确定：CB-PUSCH 明确了 BSR 评估起点，调度信息逐步形成 reporting 与 triggering 基线，RA 和 CG 明确了支持范围及部分操作规则。更细粒度调度、LCP、资源效率增强及跨 RAN1/RAN2 的设计仍待研究，材料未表明整体方案已定型。

### 关键进展

- CB UL 从以 normal SR/BSR 为比较基线的探索，推进到 RAN2 牵头评估，并在 RAN2-133bis 明确从 TN scenario 下共享资源承载多 UE BSR 开始；KPI 覆盖 UL PRB utilization、data burst latency 和/或 BSR latency，并考虑 collision ratio。评估假设 payload 包含 UE ID，timer 内收到 positive NW response 表示 contention resolution 成功，失败重试采用 HARQ new transmission。（依据：RAN2-132、RAN2-133、RAN2-133bis）
- 调度信息从研究 buffer status 与 delay status 的统一 framework，推进到明确支持两类信息、采用 legacy per-LCG reporting 基线；RAN2-134 进一步以 NR BSR/DSR triggering events 作为 unified uplink data status procedure 的触发基线，支持 data importance reporting，并至少将 PHR reporting 与 BSR/DSR 分开。（依据：RAN2-132、RAN2-133、RAN2-133bis、RAN2-134）
- RAN2-132 确立 DL SPS 基线并继续研究 UL CG like mechanisms；RAN2-133bis 明确 CG 研究涵盖立即激活、动态激活/去激活及资源调整。RAN2-134 进一步支持一个或多个 CG configurations，通过 RRC 和/或 DCI 激活或去激活，允许多个 CG 同时激活，但每个 cell 同一时刻 UE 仅在一个 CG 上发送，并批准向 RAN1 发送相关 L1 scheduling 需求 LS。（依据：RAN2-132、RAN2-133bis、RAN2-134）
- RA 从 RAN2-133bis 支持 CBRA/CFRA、限定 Msg1/Msg3 indication 适用范围并研究流程统一，推进到 RAN2-134 明确支持 2-step/4-step RA、要求 4-step RA 可独立工作，并支持在 preamble 解码成功但 msgA-PUSCH payload 解码失败时 fallback 到 4-step RA 的 msg3 transmission。MAC 共性设计仍在推进。（依据：RAN2-133bis、RAN2-134）
- LCP 研究从动态参数以及 delay、importance、跨 flow/packet correlation，扩展到新 LCP design、多种 performance objectives、application context awareness 和 dynamic QoS，并结合 per-LCG/per-LCH UL grant 探索更细粒度调度；截至 RAN2-134 尚未形成具体增强设计。（依据：RAN2-132、RAN2-133、RAN2-133bis、RAN2-134）
- RAN2-132 明确支持 sequence number-based L2 recovery 和基于 STATUS reporting 的 ARQ retransmission，保留 ARQ 独立于 HARQ、实现最高 100% reliability 的要求，并研究利用 HARQ process status 加快重传。后续材料未给出该机制定型或要求变更的证据。（依据：RAN2-132）

### 待决问题

- CB-PUSCH 用于 general purposes 还是仅用于 BSR 尚未确定；共享资源 blind decoding complexity、碰撞时 UE 区分与 payload 解码能力及 DMRS/RNTI 假设仍需 RAN1 输入。基于 CG 的增强、复用 RACH framework，以及 valid TA 下仅发送 MSGA payload 的机制仍待研究。（依据：RAN2-133bis、RAN2-134）
- 调度信息的统一格式、粒度和新增触发条件仍待明确；early reporting 的内容、触发与约束未见后续定论。data importance 粒度、BSR 指示待处理 MAC CE 及其大小、更细粒度 SR 和 SR resources 效率增强仍待研究；PHR 细节需等待 CA framework 与 RAN1 MIMO 要求更明确。（依据：RAN2-133、RAN2-133bis、RAN2-134）
- LCP 动态参数、信道选择、优先级灵活性及 delay、importance、QoS flow/packet dependency 的处理尚待设计；更细粒度 UL allocation/grant 的场景、粒度、DCI 开销及对 LCP/BSR 的影响仍不明确。（依据：RAN2-133、RAN2-133bis、RAN2-134）
- RA 统一的参数、MAC PDU、恢复机制和窗口长度仍待确定；RACH partitioning、2-step RA preamble/PUSCH 对应关系、负载管理和节能设计需与 RAN1 协调。UL CCCH segmentation 的可行性及 preamble partition 方案仍需结合大小需求、复杂度和 contention resolution delay 评估。（依据：RAN2-133bis、RAN2-134）
- CG 资源使用/未使用指示、UE 发起的 advance indication 及资源效率机制仍待研究；是否以 NR UTO-UCI 为基线存在不同意见，多 CG 操作细节可在 stage 3 继续讨论。此前提出的 CG recycling 和 UE 请求更新 CG configuration 未见明确结论。（依据：RAN2-133bis、RAN2-134）
- 显式 UL HARQ process status 及利用 HARQ status、feedback 或 network indications 加快 ARQ/RLC 重传的细节仍缺乏定论；更细粒度 HARQ、通过不同 HARQ processes 调度不同 logical channels 的提议也未见后续处理结果。（依据：RAN2-132、RAN2-133）

### 会议时间线

- **RAN2#132**（2025-11-17 至 2025-11-21）：RAN2#132 明确了 6GR MAC 与调度的研究方向，重点是降低 scheduling 时延并提升 UL resource efficiency，基线支持 DL SPS，UL 继续研究 CG like mechanisms。会议明确研究至少包含 buffer status reporting 和 delay status reporting 的 scheduling information 机制，并在详细功能取得进展后争取统一 framework。L2 recovery 支持 sequence number-based ARQ，并研究利用 HARQ process status 加快重传；CB UL、CG、报告机制及 LCP 的具体增强设计仍需后续讨论。
- **RAN2#133**（2026-02-09 至 2026-02-13）：RAN2#133 推进了 6GR MAC 与调度中 contention-based UL 方案的评估，并明确将支持 buffer status 和 delay status information、研究用于 UL scheduling 的 early reporting。RAN2 继续牵头 CB based schemes 评估，Dedicated SR mechanism 在 RAN1 已定义的前提下被假定为请求 UL resource 的基线。上述进展明确了评估方向和调度信息支持范围，但 CB 的协议机制、报告细节以及 HARQ、LCP 增强仍需后续研究。
- **RAN2#133bis**（2026-04-13 至 2026-04-17）：本会议明确了 CB-PUSCH 承载 BSR 的评估起点、指标及 contention resolution 假设，并以 legacy per-LCG scheduling information reporting 为调度信息上报基线。随机接入方面，明确了 Msg1/Msg3 indication 的适用原则，支持 CBRA 和 CFRA，并继续研究 2-step/4-step RA 的统一与简化。会议还推进了更细粒度 UL grant、新 LCP design 和动态 CG 的研究，但具体协议设计及部分物理层可行性仍待后续确定。
- **RAN2#134**（2026-05-18 至 2026-05-22）：本会议推进了 6GR MAC 与调度的基线确定，明确了 scheduling information reporting、随机接入和 configured grant 的若干基本行为，并继续研究面向多样化业务的 LCP 与 UL 资源分配增强。协议层面保留 legacy per-LCG reporting 和 NR BSR/DSR 触发事件作为基线，支持报告 data importance，并推动 2-step RA 与 4-step RA 的 MAC 共性设计。更细粒度调度、低时延状态报告及资源效率增强仍需进一步明确机制和跨 RAN1/RAN2 的接口要求。

## 6GR 演进

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.3.1 Scheduling

由于 XR 和 IC 等实时流量出现增多，legacy LCP procedure 可能不足以支持 6G 中更多样的流量。

```text
The legacy LCP procedure may not be sufficient in supporting more diverse traffic in 6G, due to increased presence of real time traffic such as XR and IC.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-o001`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.3.1 Scheduling

6G 的新用例和流量特征要求更具适应性的 LCP。

```text
New use cases and traffic characteristics in 6G call for more adaptive LCP.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-o002`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.3.1 Scheduling

现有 LCP framework 可通过为每个 QoS flow 配置专用 DRB/LCH 实现 QoS adaptation，但受 DRB/LCH 数量有限、配置开销以及半静态 priority、PBR 和 BSD 限制，缺乏可扩展性和动态性。

```text
Existing LCP framework can achieve QoS adaptation by configuring dedicated DRB/LCH per QoS flow. However, it is not scalable and dynamic due to the limited number of DRBs/LCHs, configuration overhead, and semi-static priority, PBR and BSD.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-o003`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.3.1 Scheduling

5G NR 的 LCP procedure 在 MAC entity 中所有已选 logical channel 之间执行，导致 XR service 和 mobile AI 的各 traffic stream uplink grant 调度缺乏灵活性。

```text
LCP procedure in 5G NR is performed among all the selected logical channels in the MAC entity, causing inflexibility to schedule the uplink grant for each traffic streams in XR service and mobile AI.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-o004`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.3.1 Scheduling

NR 中为 XR traffics 设计的 refined buffer status granularity 仍会在大数据量下产生 quantization errors。

```text
In NR, refined buffer status granularity was intended for XR traffics. Therefore, quantization errors would still occur for large data volumes.
SR enhancements
R2-2603343	Scheduling Aspects for 6GR	Sharp	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-o005`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.3.1 Scheduling

6G 中需要更高效地使用 SR resources，以便为小区内尽可能多的 UEs 提供低时延 UL access。

```text
SR resources need to be used more efficiently in 6G, to provide low latency UL access to as many UEs as possible in a cell.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-o006`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.3.1 Scheduling

Short BSR 的 maximum reportable size 对应的 UL grant 无法传完剩余 UL data 时，UE 必须等待 periodicBSRTimer 到期后才能再次发送 BSR，因此会增加时延。

```text
The UE must wait for the expiration of the periodicBSRTimer to be triggered to send another BSR for the remaining UL data that could not be transmitted using the UL grant corresponding to the maximum reportable size of a Short BSR.　This leads to additional delay.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-o007`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

研究新的 LCP 设计，在一个统一流程中支持具有不同性能目标的多样化业务，例如最大化吞吐量或保证时延。

```text
Study new LCP designs that can support diverse traffic with distinct performance objectives (e.g. maximize throughput vs guarantee delay) in one unified procedure.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p001`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

研究自适应 LCP 设计，以更好支持 6G 用例，包括动态参数适配，以及提高 UE 在信道选择和优先级设置方面的灵活性。该提案已记录（Noted）。

```text
Study adaptive LCP designs that can better support 6G use cases, e.g. dynamic parameter adaptation, increased UE flexibility in channel selection and prioritization.
Noted
R2-2602948	Discussion on 6GR scheduling	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p002`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

RAN2 将进一步研究面向 6GR 的 LCP 增强，并考虑时延、重要性及 QoS flow/packet 间依赖等业务特征。相关意见指出，需识别现有设计的不足，并考虑为多样化数据重新审视 LCP。

```text
RAN2 to further study LCP enhancements considering various traffic characteristics, e.g., delay, importance, inter-QoS flow/packet dependency for 6GR.
Noted
Discussion
-	Qualcomm thinks that the NR design is not sufficient especially for real time.
-	Mediatek thinks that we should agree on what we want to identify.
-	Huawei thinks that the only scenario for LCP is dynamic QoS, what other requirements are there to justify the shortcomings.   Qualcomm thinks that the static priority is fine for MBB but not for the diverse type of data, and the dynamic priority in R19 was just a patch work so we can reconsider LCP in a more integrated.
-	Nokia would like to understand more what we are missing for LCP other than the already agreed dynamic priority.   Interdigital agrees with Qualcomm and we should make sure that LCP is designed well from the beginning.
Finer granularity LCP
R2-2604156	Views on UL scheduling	NTT DOCOMO INC..	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p003`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

研究 UL 资源分配框架，使其能以比 LCH 级更细的粒度进行动态控制，以支持 QoS adaptation 并缓解 inter DRB HoL blocking。该提案已记录（Noted），讨论中有人询问 finer granularity 的含义。

```text
Study the framework for allocating UL resources to UL data that allow dynamic control at a finer granularity than the LCH level to enable QoS adaptation and to mitigate inter DRB HoL blocking.
-	Lenovo asks what is meant by finer granularity
Noted
R2-2603353	Consideration on Scheduling and uplink scheduling information in 6G	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p004`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

研究更细粒度的 UL grant 增强，例如 per-LCG 或 per-LCH UL grant；提案还提出 RAN2 与 RAN1 共同研究 UL grant 粒度改进。讨论涉及 DCI signaling 开销、对 LCP 和 BSR 的影响，以及需要明确问题与场景；该议题已记录（Noted）。

```text
Study UL grant enhancement with finer granularity, e.g., per-LCG UL grant, per-LCH UL grant.
-	Samsung asks if this requires putting the information in DCI and if so RAN1 needs to be involved.  LG confirms.
-	Apple asks what happens if there is no more data for that logical channel can something else go in it.
Noted
Moved from 9.3.1.3.2
R2-2603455	Configured grant and random access procedure	Ericsson, Bell Mobility	discussion
Proposal 3	To improve resource allocation in 6G, RAN2 together with RAN1, should study how to improve the granularity of the UL grants, e.g. per LCH indications.
Noted
Discussion
-	Mediatek asks if this removes the need for prioritized bit rates.  If so it simplifies UE behavior otherwise it just means more restrictions.
-	ZTE supports this direction in general but we have to be a bit careful about overhead in DCI signaling so one option is to do at LCG level.   We will need LCP with PBR as baseline, but this can help on top.
-	Lenovo thinks that this decision will impact quite a few things, as it will impact LCP, BSR, and have some concern on impact on DCI.  We can try to see if we can optimize the existing framework first before deciding such a thing.
-	Vivo would like to clarify the intention rather than the solution.    We can resolve how the UE uses the grant issue by doing LCP.
-	Huawei thikns that in 5G we can provide priority and based on that we can filter out the LCH with that priority.   ZTE thinks that we can go one level lower of granularity, LCH for example to ensure that you treat the LCH that has delay problems.
-	Xiaomi thinks that we need to ask RAN1 first.
-	Oppo and Samsung is fine to study this and the granularity should be aligned with granularity of reporting.
-	Qualcomm thinks that this proposal seems to provide more flexibility in scheduling, but this works only if the network has a more accurate buffer status and not sure we need to go into that granularity.   Maybe we can consider only a small group of logical channels that can do this type of scheduling and that would give enough flexibility.
-	Apple is not sure why the network needs this level of control, the UE is one that is most aware and has better knowledge on how LCP needs to be done to deliver the best user experience.
-	Interdigital thinks that this is a way for the scheduler to indicate to the UE to skip the normal multiplexing, but we can think more.
-	Nokia thinks that with current LCP the UE is already utilizing the grant the best way.  Wants to understand what the scenario is.   Ericsson thinks that even from 5G we knew that LCP was not sufficient.
-	CMCC thinks that this would allow some ability for the network guarantee the service for some LCHs.
Study LCP procedure and scheduling granularity to support the various types of 6G traffic.   Identify problem and scenario to solve.
Scheduling information
Reported Information
R2-2602948	Discussion on 6GR scheduling	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p005`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

RAN2 将支持在 scheduling information 中报告 data importance information，其粒度仍待确定（FFS）。

```text
RAN2 to support data importance information reporting as part of scheduling information. FFS the granularity of the importance information.
R2-2603115	Uplink scheduling in 6G	Samsung	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p006`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

RAN2 将考虑在 6G 中使用 BSR 指示待处理的 MAC CE 及其潜在大小。

```text
RAN2 to consider using BSR to indicate the pending MAC CE(s) and their potential size in 6G.
R2-2603466	UP Scheduling aspects	Nokia	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p007`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

支持在 6G 中至少将 PHR reporting 与 BSR/DSR 分开。PHR mechanism 的细节可待 CA framework 和 RAN1 对 MIMO 的要求更明确后再讨论。

```text
At least separate PHR reporting from BSR/DSR is supported for 6G. The details on the PHR mechanism could be discussed later after the CA framework as well as the RAN1 requirement on MIMO become clearer.
Reporting granularity
R2-2603038	Discussion on scheduling	Xiaomi	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p008`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

RAN2 以 legacy per-LCG scheduling information reporting 作为基线。

```text
RAN2 to reuse the legacy per-LCG scheduling information reporting as the baseline.
R2-2603907	Discussion on MAC scheduling enhancements	1Finity	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p009`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

RAN2 研究更细粒度的 SR，以支持无需单独发送 BSR 即可直接分配 UL 资源。

```text
RAN2 to study finer granularity of SR to enable direct UL resource allocation without separate BSR transmission.
R2-2603263	Views on 6G User Plane: Scheduling	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p010`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

为降低 SR/BSR latency，可考虑用 SR configuration ID 表示与 buffer status 相关的信息，例如 buffer size 或是否存在 delay-critical data。这样网络可在没有 BSR 的情况下及时分配更合适的 UL 资源。

```text
To reduce SR/BSR latency, RAN2 can consider using SR configuration ID to represent certain information related to the buffer status (e.g. buffer size, or presence of delay-critical data), such that network can timely allocate more appropriate UL resource even without BSR.
R2-2602940	Discussion on scheduling procedures	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p011`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

研究提高 SR resources 使用效率的方法，例如与 PDCCH 联合调整、动态 de-/activation SR resources，以及避免 resource partitioning。

```text
Study methods to achieve more efficient use of SR resources, e.g. joint adaptation with PDCCH, dynamic de-/activation of SR resources, avoid resource partitioning, etc.
BSR/DSR triggers
R2-2603603	Further Discussion on Uplink Scheduling	Lenovo	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p012`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

对于 6G unified uplink data status procedure 的触发条件，RAN2 同意将 5G NR 规定的 BSR 和 DSR triggering events 作为基线。

```text
RAN2 to agree that for the triggering conditions for the unified uplink data status procedure in 6G, BSR and DSR triggering events specified for 5G NR are considered as a baseline.
R2-2603475	Scheduling, Scheduling Information Reporting and LCP	CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p013`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

unified scheduling information reporting 可由事件触发，也可周期性进行。触发事件至少应考虑 data arrival、padding 和 remaining time。

```text
The unified scheduling information reporting can be event-triggered and periodical. The trigger events should at least consider data arrival, padding and remaining time.
R2-2604156	Views on UL scheduling	NTT DOCOMO INC..	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p014`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

研究新的 triggering conditions，以支持 6G 中及时、准确地报告 buffer information。

```text
Study new triggering conditions to enable timely and accurate buffer information reporting in 6G.
CB-PUSCH
R2-2603263	Views on 6G User Plane: Scheduling	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p015`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

RAN2 应确认 CB-PUSCH 是用于所有 general purposes，还是仅用于 BSR。

```text
RAN2 should confirm whether we aim to use CB-PUSCH for all general purposes, or only for BSR.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p016`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

CB based PUSCH mechanism 以 CG based transmission mechanism 为起点，进一步增强仍待讨论（FFS）。

```text
CB based PUSCH mechanism takes CG based transmission mechanism as the starting points, FFS on the further enhancement.
Noted
Moved from 9.3.1.3.2
R2-2603051	Framework for RACH and CB-PUSCH	ZTE Corporation, Sanechips, Samsung, China Telecom, Sony, ESA, DLR, Sateliot	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p017`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

6G 应复用 RACH framework 作为启用 CB-PUSCH 的基线，以避免 RACH 与 CB-PUSCH 功能重复，并尽量减少 CB-PUSCH 的规范工作。

```text
6G should avoid duplicate functionality between RACH and CB-PUSCH and minimize the specification work for CB-PUSCH by reusing RACH framework as the baseline for enabling CB-PUSCH
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p018`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.1 Scheduling

对于 CB-PUSCH，除常规 2-step RACH mode（preamble + PUSCH）外，RAN2 应研究 UE 在具有 valid TA 时能否不发送 preamble 而传输 MSGA payload part。条目记录了 simulation assumptions 已在 R2-2604388 中达成一致。

```text
For CB-PUSCH, in addition to the normal 2-step RACH mode (i.e. preamble + PUSCH), RAN2 should study whether the UE can transmit the MSGA payload part without the preamble when the UE has a valid TA
Noted
Discussion
-	Mediatek thinks that we should try to find the commonality and what is different.
After CB
-	Oppo indicates that RAN1 has made progress and companies should take these assumptions into account.   Ericsson indicates DMRS separation is supported in the evaluation and they will evaluate L1 transmission delay.
-	MEdiatek thinks that one think missing is what is the periodicity of the SR request.   Companies should indicate what they used.
-	Qualcomm thinks that we should have one common data point so we can calibrate and compare.
[POST134][018][6G UP] Simulation assumption (Mediatek)
Intended outcome: Align on any new/other remaining possible assumptions and try to converge on at least one set of parameters that everyone should try to evaluate and then allow other ranges for companies, taking RAN1 information into account.
Deadline:  2 weeks
=> Noted in R2-2604388 (Simulation assumptions in this document are agreed).
R2-2604394	CB-PUSCH progress	OPPO	discussion	Rel-20	FS_6G_Radio
Withdrawn
R2-2603050	Scheduling enhancements	ZTE Corporation, Sanechips	discussion
R2-2603090	Discussion on scheduling in 6G	Transsion Holdings	discussion	Rel-20
R2-2603164	Latency reduction techniques for 6G	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
R2-2603254	On the support for CB-PUSCH	Google	discussion	Rel-20	FS_6G_Radio
R2-2603305	6G CB-PUSCH and Scheduling information reporting	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2603329	Discussion on scheduling	China Telecom	discussion	Rel-20	FS_6G_Radio
R2-2603418	L2 scheduling framework for 6GR	InterDigital, Inc.	discussion	Rel-20	FS_6G_Radio
R2-2603454	System simulation for contention based BSR	Ericsson, T-Mobile USA, OPPO, Kyocera, WILUS Inc., LG Electronics Inc.,Turkcell, Sharp	discussion
R2-2603484	6G scheduling	NEC	discussion	Rel-20	FS_6G_Radio
R2-2603746	Latency-aware contention-based UL access and load-aware grant expectation for CB-PUSCH	Jio Platforms	discussion	Rel-20	FS_6G_Radio
R2-2603747	Predictive CB-CG resource control and latency-aware retransmission gating	Jio Platforms	discussion	Rel-20	FS_6G_Radio
R2-2603856	Consideration on 6GR Scheduling	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2604021	Contention-based BSR reporting	MediaTek Inc.	discussion	Rel-20
R2-2604120	Discussion on UL scheduling in 6G	III	discussion	Rel-20	FS_6G_Radio	R2-2601700
R2-2604162	Discussion on L2 Scheduling for 6G AI-driven Services	III, National Taiwan University	discussion	Rel-20	FS_6G_Radio
R2-2604169	MAC handling assumptions for uplink scheduling information	Rakuten Mobile, Inc	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.1-p019`

### [6G/Rel-20 RAN2#134] `agreement` 9.3.1.3.2 Other MAC functionalities

支持 2-step RA 和 4-step RA，并寻找 MAC commonalities 以期统一；设计应确保 4-step RA 无需 2-step RA 即可工作。向 RAN1 通知该决定并询问能否在不进行 RACH partitioning 的情况下支持两者，同时研究用于 RA load management 和 energy saving 的 RACH designs。

```text
1	Support 2-step RA and 4-step RA.   Find commonalities in MAC with the aim to unify (if possible) but the design should ensure that 4 step RA can work without the need for 2-step RA
2	Indicate to RAN1 our decision to support 2-step and 4-step and take into account.  Explain that RAN2 discussed whether it is possible to do 2-step and 4-step without RACH partitioning and ask whether it is possible.
3	Study RACH designs that enable more efficient use of resources for RA load management and energy saving purposes
[AT134][010][6G UP] Random Access (Huawei)
Intended outcome: Discuss RA procedure steps for 2 and 4 step (try to understand commonalities for unified procedure) and identify any possible questions to RAN1 that we can already send and any/whether any email discussions over the summer would be helpful.
Deadline:  Thursday
R2-2604396	Summary of [AT134][010][6G UP] Random Access (Huawei)	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-a001`

### [6G/Rel-20 RAN2#134] `agreement` 9.3.1.3.2 Other MAC functionalities

将所列 2-step 与 4-step CBRA/CFRA procedures 作为 6G 讨论基线，并支持在网络解码 preamble 但未解码 msgA-PUSCH payload 时从 2-step RA fallback 到 4-step RA 的 msg3 transmission。两种 RA 均支持的决定及关于 RACH partitioning 和 2-step RA 中 preamble 与 PUSCH 对应关系的问题将发送给 RAN1；窗口长度统一等事项仍为 FFS。

```text
RA procedure for 2-step and 4-step RA
1	Take the following procedure for 2-step RA and 4-step RA as the baseline for the discussion in 6G from RAN2 point of view
4-step CBRA: Where the UE transmits the RACH preamble and waits for the network response (i.e. RAR) which schedules transmission of MSG3 in the UL
2-step CBRA: Where UE transmits RACH preamble along with the PUSCH and waits for the network response which provides RACH response as well as contention resolution
4-step CFRA: Where UE transmits dedicated RACH preamble assigned by the gNB and terminates the RA procedure upon reception of NW response
2-step CFRA: Where UE transmits dedicated RACH preamble assigned by the gNB and its corresponding PUSCH resource and terminates the RA procedure upon reception of NW response.
2	Support fallback from 2-step RA to 4-step RA to msg3 transmission when the network decodes the preamble but not the msgA-PUSCH payload. FFS RACH type switching
Unification of 2-step and 4-step RA
3	Aim to have the same length of the two windows when both 2-step and 4-step RA are configured, i.e., same as 4-step RA. FFS the start of the window for the unification.   FFS other aspects of unification after some further progress on basic procedure (e.g. format,etc).
LS to RAN1
4	Send an LS to RAN1 about the agreements above and indicate:
(a) the agreement that both 2-step and 4-step RA are supported from RAN2 point of view in 6G;
(b) asking whether it is possible to support 2-step and 4-step RA without RACH partitioning;
(c) asking about the correspondence between preamble and PUSCH in 2-step RA
[POST134][017][6G UP]  RACH (Huawei)
Intended outcome:
(a) LS to RAN1; and
(b) discuss the FFSs for 2-step and 4-step RA procedure (not dependent on RAN1 progress) keeping in mind potential unification for cases.   Understand details of possible agreed RA enhancement.
Deadline:
LS to RAN1 (one week)
The remaining discussion (long)
R2-2604385	LS on Random Access in 6G	RAN2	LS out	Rel-20	FS_6G_Radio	To:RAN1
=> Approved
Scope of the post email discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-a002`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.3.2 Other MAC functionalities

在 NR 中，RACH resources 难以适应接入负载的短期变化，常导致高争用和接入失败。

```text
In NR, RACH resources do not adapt well to short-term variations in access load, often resulting in high level of contention and access failures.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-o001`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.3.2 Other MAC functionalities

允许 CCCH channel segmentation 可使 MSG3 payload size 更灵活，同时不损害 coverage，并避免通过 preamble partitioning 指示 MSG3/MSGA payload size。它还可让可延后至 MSG3 的功能（如 early UE type、slice indication）使用基于 MSG3 而非 MSG1 的指示。

```text
Allowing segmentation for CCCH channel can enable the following:
o	Make the MSG3 payload size flexible without compromising the coverage whilst avoiding the need for preamble partitioning for MSG3/MSGA payload size indication
o	Enable more features that can wait till MSG3 (e.g. early UE type, slice indication etc) to use MSG3 based indication instead of MSG1 based indication.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-o002`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.3.2 Other MAC functionalities

CCCH segmentation 需要多轮 Msg2 reception 和 segment transmission，会增加 UE implementation complexity，并增加 contention resolution delay。

```text
CCCH segmentation requires multiple-round Msg2 reception and segment transmission, which introduces complexity on UE implementation as well as additional delay for contention resolution.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-o003`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.3.2 Other MAC functionalities

CCCH segmentation 需要在 Msg3 中增加指示，以说明是否还有后续 segment，和/或指示每个 segment 的 sequence number。

```text
CCCH segmentation requires additional indication in Msg3 to indicate if there is more segment or not and/or the sequence number of each segment.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-o004`

### [6G/Rel-20 RAN2#134] `observation` 9.3.1.3.2 Other MAC functionalities

如果 CG 用于 bursty traffic，可利用 UTO-UCI 和 early report 来提高 radio efficiency。

```text
If CG is to be used for bursty traffic, to improve radio efficiency, UTO-UCI and early report can be utilized.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-o005`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

6G 的 RACH framework 应支持 4-step RA、2-step RA，以及在网络解码 preamble 但未解码 RACH payload 时从 2-step RA fallback 到 4-step RA。Qualcomm 认为，在无法解码 payload 时应使用 failure indication，而非 fallback。

```text
The RACH framework in 6G should support:
-	4-step RA: Where the UE transmits the RACH preamble and waits for the network response (i.e. RAR) which schedules transmission of MSG3 in the UL
-	2-step RA: Where the UE transmits RACH preamble along with the associated PUSCH transmission and waits for the network response which provides RACH response as well as contention resolution
-	Fallback from 2-step RA to 4-step RA: when the network decodes the preamble but not the RACH payload
-	Qualcomm thinks that it should be failure indication to decode the payload instead of fallback
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p001`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

RACH 的 RAR format 应支持 TA、backoff、contention resolution 和 UL grant（用于 4-step RA）的指示，并支持从 2-step RA fallback 到 4-step RA；RAR format 的最终设计可留到 stage-3。讨论中提出研究 unified RACH framework，包括 common RACH pool、由 UE 根据网络指示和/或预配置条件选择 Msg1 resources，以及用 unified RAR 响应不同 UL transmissions。

```text
RAR format for RACH should support indication of TA, backoff, contention resolution, UL grant (for 4-step RA) and should enable fallback from 2-step to 4-step RA. Final design of RAR format can be left for stage-3.
Noted
R2-2603112	Discussion on RACH and configured grant	OPPO	discussion	Rel-20	FS_6G_Radio
Proposal 1	For 6G RACH, RAN2 to study a unified RACH framework including:
	A common RACH pool (i.e. for Msg1) including PRACH and/or PUSCH is configured to support different UL transmission types.
	The UE selects the resources (i.e. preamble, or preamble and payload, or payload) for Msg1 based on NW indication and/or preconfigured conditions.
	A unified RAR is design to respond the UEs performing different UL transmissions.
-	ZTE asks how can we avoid partitioning.    Oppo thinks we don’t need to differentiate.  Huawei thinks that we need to think about aNB as we would have to do blind decoding and for 4step we don’t need to as it is just a preamble.   Oppo thinks that the network can detect whether there was a preamble or a preamble and PUSCH.      ZTE thinks that this was discussed in RAN1 so we would need to ask input.
-	Interdigital thinks that we made the decisions because of legacy as well but we should study if there is a way with RAN1 input.   Nokia also thinks RAN1 needs to discuss.
Noted
Discussion
-	Ericsson thinks we should have 2-step RA only for the scenarios needed, like NTN.  ZTE thinks that the 2-step RA is useful for other cases and not just for synchronous.
-	Qualcomm thinks that the UE should have the option to implement it or not and the design should be done in a way that it doesn’t implement features it doesn’t supports.    Huawei has the same view.
-	Nokia thinks 4-step as a baseline.
-	ZTE thinks that we should wish for having the same window.  Interdigital thinks that the window length requirements come from RAN2.
R2-2602949	Considerations on 6GR Random Access and Configured Grant	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p002`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

在 6GR 中，以 NR 4-step RA procedure 为基线，4-step RA procedure 包括 RACH request、RACH response、Msg3 payload 和 Contention resolution 四步。

```text
In 6GR, taking the NR 4-step RA procedure as baseline, the 4-step RA procedure includes the following steps:
1) RACH request;
2) RACH response;
3) Msg3 payload;
4) Contention resolution.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p003`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

在 6GR 中，以 NR 2-step RA procedure 为基线，2-step RA procedure 包括两步：RACH request 与 MsgA payload，以及 RACH response 与 Contention resolution。

```text
In 6GR, taking the NR 2-step RA procedure as baseline, the 2-step RA procedure includes the following steps:
1) RACH request and MsgA payload;
2) RACH response and Contention resolution.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p004`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

为统一 4-step 和 2-step RA，考虑共用 RA configuration parameter structure、Contention resolution determination、recovery mechanism 和统一的 MAC PDU format。还考虑共用 backoff mechanism、power ramping accumulation and reset，以及 maximum access attempt。

```text
For the commonization of 4-step and 2-step RA, at least the following aspects are considered:
1) Common RA configuration parameter structure;
2) Common contention resolution determination, recovery mechanism, as well as a unified MAC PDU format;
3) Common backoff mechanism, power ramping accumulation and reset, and maximum access attempt.
RACH Resource Adaptation
R2-2602941	Discussion on other MAC functionalities	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p005`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

研究提升资源使用效率的 RACH designs，例如 dynamic 或 on-demand allocation of RACH resources、beam-specific RACH configurations。还提出研究可与中间睡眠机会捆绑的 RO configuration framework，以及缓解 RA overload 的方法，包括动态切换 Random Access resource set 和调整 PRACH、MsgA PUSCH resources。

```text
Study RACH designs that enable more efficient use of resources, e.g. dynamic or on-demand allocation of RACH resources, beam-specific RACH configurations, etc.
Noted
R2-2603455	Configured grant and random access procedure	Ericsson, Bell Mobility	discussion
Proposal 6	Study how to design a configuration framework for ROs such that it would be possible to bundle with sleeping opportunities in between.
Noted
R2-2603913	Discussion on other MAC functionalities	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
Proposal 1	Study methods to mitigate RA overload situation, e.g.,:
-	Dynamic indication to switch the Random Access resource set,
-	Adaptation of PRACH and MsgA PUSCH resources
Noted
R2-2603016	Random Access in 6G	Samsung	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p006`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

为高效利用多个 random access resource sets 配置的资源，UE 发起 random access procedure 时，可以先指示将使用的 random access resource set，再使用所选集合执行该过程。

```text
For efficient utilization of resources configured by multiple random access resource sets, when the UE initiates random access procedure, UE can first indicate the random access resource set UE is going to use and then perform random access procedure using the selected random access resource set.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p007`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

6G 支持在 random access procedure 期间，在一组稀疏配置的 random access occasions 与一组密集配置的 random access occasions 之间动态切换。

```text
Dynamic switch between a set of sparsely configured random access occasions and a set of densely configured random access occasions during the random access procedure is supported in 6G.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p008`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

当网络进入 network energy saving mode 时，对于该模式期间发起的 random access procedure，多个 RACH configurations 中仅考虑一个处于 active 状态。讨论意见提到 idle mode 下设计需谨慎；对于是否需要动态握手以及是否应避免 RACH partitioning，意见存在分歧。

```text
When the network enters network energy saving mode, only one of the multiple RACH configurations is considered active for the random access procedure initiated during the network energy saving mode.
Noted
-	Mediatek thinks that we need to be careful when designing this especially for idle mode, like dynamic handshaking between NW and UE.   Xiaomi thiks we should avoid RACH partitioning.
-	Apple thinks we need to be very careful for idle mode as it will be something supported and mandatory from day 1.
-	ZTE thinks we should discuss here for energy saving and we don’t need handshake for idle mode.   Ericsson explains that there is no intention to switch things dynamically and there are ways of providing things
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p009`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

讨论了 2-step RA 中 UE 已有 TA 时是否仍需发送 preamble；相关公司确认可在讨论 2-step procedures 时研究。还提出先明确仅发送 PUSCH 而不发送 preamble 的适用场景，并指出这可能改变 gNB behavior，且 preamble 可能有利于 fallback 和可靠性。

```text
-	Ericsson ask whether to transmit preamble when transmit preamble when UE has TA for 2 step RA is still in scope.  Companies confirm that it can be discussed when we discuss 2step procedures.  ZTE thinks that we should include the question to RAN1.   Huawei thinks that we first discuss under what scenario we should not transmit preamble but only PUSCH, the question is not clear.    Lenovo agrees haven’t really discussed this as it would change gNB behavior.   Interdigital asks what is the benefit of just transmitting PUSCH, transmitting the preamble may be beneficial for fallback and it is more reliable.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p010`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

邮件讨论范围包括向 RAN1 发送 LS，以及讨论 2-step 和 4-step RA procedure 的新问题、待定事项和两种过程潜在的统一。

```text
Scope of the email disc: (a) LS to RAN1; and (b) discuss on the new issues and the FFSs for 2-step and 4-step RA procedure and potential unification of the two procedures.
CCCH segmentation
Moved from 9.3.1.1
R2-2603049	Functionality for upper user plane	ZTE Corporation, Sanechips	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p011`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

研究通过支持 UL CCCH channel segmentation，在不影响覆盖的情况下支持更大的 UL CCCH message size。提出研究 UL CCCH message segmentation 的可行性；原文指出，分段传输 MSG3 中的 CCCH payload 可避免过度依赖 GroupA/GroupB preamble partitioning，并支持在初始接入过程中携带多个 early indications。

```text
Study solutions to enable larger UL CCCH message size without impacting coverage, by supporting segmentation for UL CCCH channel
Noted
R2-2604066	Views on Random Access and Configured grants	1Finity	discussion	Rel-20
Observation#3: GroupA/GroupB preamble partitioning can be avoided if the CCCH payload in MSG3 can be transmitted in parts (i.e. segmented). For SDT the small data payload in MSG3 it can be transmitted in parts so Group/GroupB preamble partitioning can be avoided.
Observation#8: UL CCCH SDU included in MSG3 if segmented, then the excessive need for preamble partitioning can be avoided and early indications can be included in MSG3 segments.
Proposal#3: RAN2 to study the feasibility of UL CCCH message segmentation as it not only avoids excessive need for preamble partitioning but also provides flexibility in conveying multiple early indications as part of initial access procedure.
Noted
R2-2603039	Discussion on other MAC functionalities	Xiaomi	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p012`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

为支持灵活的 Msg3/MsgA 大小，采用与 NR 相同的 preamble partition，而非 CCCH segmentation。CCCH 大小需求将在 6G 工作后期明确前，暂不讨论此项。

```text
To support flexible Msg3/MsgA size (e.g., 56bits and 72bits), preamble partition as in NR is used instead of CCCH segmentation.
Noted
Discussion
-	Nokia doesn’t support the segmentation as it complicated everything, but if we want to increase the size we can discuss with RAN1.   Oppo agrees with Nokia and then we need to consider retransmission.  Huawei has same view and there is no requirement for larger CCCH.
Will not discuss this until we understand the CCCH size requirement much later in the 6G work
Configured Grants
Adjustment of resource allocation
R2-2603455	Configured grant and random access procedure	Ericsson, Bell Mobility	discussion
Proposal 1	Support unified CG framework with dynamic activation/deactivation/adjustment using DCI and immediate activation using RRC.
Noted
R2-2603620	Other MAC functionalities: CG and Random-access	Sony	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p013`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

达成一致：UE 可配置一个或多个 CG configurations；每个配置至少可通过 RRC 和/或 DCI signaling 进行激活/去激活。可以同时激活多个 CG，但每个 cell 同一时刻 UE 仅在一个 CG 上发送，更多细节可在 stage 3 讨论。

```text
From RAN2 perspective, support a single CG resource that can adapt/adjust parameters (e.g. MCS, TBS) for data variability, channel variability and data reliability, and can handle different traffic types/services.
-	Mediatek asks if this would be done with DCI.
-	Panasonic asks if it is per UE or per BWP.
Noted
Discussion
-	ZTE thinks we can agrees there will be some RRC configuration and some DCI and what we put there we can leave it to stage 3.   Ericsson thinks that we can agree for same CG configuration we support both RRC signaling and DCI signaling.
-	Vivo thinks we should wait for RAN1 response.
-	Ericsson thinks that we don’t know if we need multiple CG configurations.   Huawei thinks that we have a very good motivation to have it as we support diverse and immersive communication since the beginning.   Apple thinks that we have diverse traffic types and we agreed we need to support.
-	Mediatek doesn’t see a motivation to use multiple configured.   Qualcomm also thinks this is needed and it brings a lot of benefits without much additional cost.    Also 6G design should support bursty traffic, and we should support something similar to multi-PUSCH.     Lenovo agrees with QC, it was introduced in Rel-18.
-	Samsung thinks we should be careful to ensure that low cost devices don’t need to support DCI.
-	ZTE and Interdigital thinks that the MAC needs to work for cases where there are multiple.
Agreements on CG
1	UE can be configured with one or multiple CG configurations.  For each configuration we can allow RRC and/or DCI signaling at least for activation/deactivation.   Understanding is that more than one CG can be active at a time, but the UE transmits only on one at time per cell. Further details can be discussed in stage 3.
Higher resource efficiency
R2-2603464	Other MAC functionalities	Nokia	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p014`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

RAN2 将研究 UE 如何指示已使用或未使用的 CG PUSCH resources，以提高 spectral efficiency。6G 不需要采用与 5G NR 相同格式的 UTO-UCI。

```text
RAN2 to study ways for UE to indicate used/unused CG PUSCH resources for the purpose of increased spectral efficiency. UTO-UCI in the same format as 5G NR is not needed in 6G.
Noted
R2-2602949	Considerations on 6GR Random Access and Configured Grant	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p015`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

为提高 resource efficiency，RAN2 将研究由 UE 发起 advance indication，通知 aNB 即将发生的 CG utilization。

```text
For the sake of higher resource efficiency, RAN2 to study UE initiating the advance indication to inform aNB about the upcoming CG utilization.
Noted
R2-2603039	Discussion on other MAC functionalities	Xiaomi	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p016`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.1.3.2 Other MAC functionalities

关于以 NR UTO-UCI 作为提升 resource efficiency 的基线，讨论中存在不同意见；记录指出 RAN2 不预期在这些方面提交贡献。已批准向 RAN1 发送 LS，要求其考虑 RAN2 协议，并研究支持 dynamic grant、configured grant、CG 资源立即激活、动态激活/去激活、资源分配动态调整及更高资源效率的 L1 scheduling。

```text
6G CG supports NR UTO-UCI (unused transmission occasion) to improve resource efficiency as a baseline.
Noted
Discussion
-	QC thinks that this is not a useful feature and understand the desire to improve the efficiency but they can observe the utilization and dynamically adapt the CG to make it.  Lenovo has same view as Qualcomm and we are discussing predictive reporting which is similar in terms of what it is trying to achieve.  Interdigital has the same view and also the UE has no incentive to do it.   Mediatek would like to minimize the time we spend on WI and focus on things that really matter.  Apple has same understanding, even the UE sends it not sure the network can use it.  If we want to improve resource efficiency we allow the UE to use the resource for something else like retransmission.
-	Fraunhoufer thinks that we can at least capture the intention of recovering unused resources.
-	Xiaomi thinks we can provide the information and details are FFS
-	ZTE also thinks it is useful but we can wait for RAN1.
-	Huawei thinks that the proponents can propose this in RAN1.
-	Oppo thinks that there may be some benefitis but the current UTO-UCI is not very useful as it is.
-	Samsung also thinks that the CG resource efficiency should be good.
-	Ericsson does’nt think that the reporting is useful at all, by the time the NW gets it, it doesn’t have enough time to re-cycle the resource.  The predictive reporting we are doing in RAN2 should be enough to help the network.
-	Vivo thinks we should report before the CG is used.
-	CMCC thinks that we can notify whether the resource will be used.
-	Docomo agrees that there is no incentive but from network perspective it can be useful.
No contributions expected on these aspects in RAN2
LS to RAN1
R2-2603419	Other MAC functionality	InterDigital, Inc.	discussion	Rel-20	FS_6G_Radio
Send an LS to RAN1 to inform them about the following agreements and ask them to study L1 scheduling to support them:
-	Support at least the following scheduling schemes: dynamic grant and configured grant.
-	study CG like mechanisms to address different types of traffic, including voice, bursty traffic, other periodic traffic etc.
-	Study 6G CG, which can support at least the following from RAN2 perspective:
o	CG resource immediately activated (e.g. for delay critical service) after configuration;
o	Dynamic activation/deactivation;
o	Dynamic adjustment of resource allocation (e.g. MCS, TBS and start time);
o	Higher resource efficiency
-	Add SPS
-	Add new agreements from this meeting
Action: take the RAN2 agreement into account for the L1 design
Noted
[AT134][11][6G UP] CG LS to RAN1  (Interdigital)
-	Intended outcome: Agree to LS to RAN1
-	Deadline:  Friday
R2-2604210	LS on 6G Grant Types	RAN2	LS out	Rel-20	FS_6G_Radio	To:RAN1
The LS is approved in R2-2604399
R2-2602988	Discussion on RACH and CG	NEC	discussion	Rel-21	FS_6G_Radio
R2-2603012	Discussion on MAC functionalities in 6G	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
R2-2603021	MAC processing for high data rates	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
R2-2603154	6GR MAC Functionalities	Sharp	discussion	Rel-20	FS_6G_Radio
R2-2603264	Views on 6G User Plane: Miscellaneous MAC Mechanisms	Apple	discussion	Rel-20	FS_6G_Radio
R2-2603306	6G Random Access and Configured Grant	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2603349	On random access procedure aspects	NTT DOCOMO	discussion	Rel-20	FS_6G_Radio
R2-2603476	Random Access and Configured Grant	CATT	discussion	Rel-20	FS_6G_Radio
R2-2603551	Discussion on other MAC functions	Philips International B.V.	discussion	Rel-20	FS_6G_Radio
R2-2603570	Discussion of other MAC functionalities	Lenovo	discussion	Rel-20
R2-2603857	Consideration on 6GR Random Access and CG	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2603886	Discussion on MAC functionalities in 6G	Spreadtrum, UNISOC	discussion	Rel-20
R2-2603976	Discussion on Random Access procedure	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2603977	Discussion on Configured Grant	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2604003	Discussion on 6G configured uplink grant	ASUSTeK	discussion	Rel-20
R2-2604031	Further discussion on unified RACH procedure	Google Korea LLC	discussion	FS_6G_Radio
R2-2604066	Views on Random Access and Configured grants	1Finity	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.1.3.2-p017`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.1 Scheduling

资源效率 KPI 至少包括 UL PRB utilization。

```text
The KPI for resource efficiency at least includes UL PRB utilization.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.1-p001`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.1 Scheduling

Latency KPI 包括 data burst latency 和/或 BSR latency。

```text
The KPIs for latency include data burst latency and/or BSR latency.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.1-p002`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.1 Scheduling

评估中应考虑 collision ratio。

```text
Collision ratio should be considered in the evaluation.
Scenario
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.1-p003`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.1 Scheduling

TN scenario 被视为评估的起始场景。

```text
The TN scenario is considered as the starting point for evaluation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.1-p004`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.1 Scheduling

评估的 traffic models 不受限制，例如 FTP3、XR 和 bursty eMBB。

```text
No restriction on the traffic models (e.g. FTP3, XR and bursty eMBB) for the evaluation.
CB-PUSCH assumption
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.1-p005`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.1 Scheduling

为与 legacy SR-BSR 比较，CB-PUSCH 评估从 CB-PUSCH 用于传输 BSR 的用例开始。

```text
To compared with the legacy SR-BSR, the evaluation for the CB-PUSCH starts from the use case that CB-PUSCH is used for the transmission of BSR.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.1-p006`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.1 Scheduling

RAN2 认为，aNB 共享资源的 blind decoding complexity（例如 DMRS 和 scrambling sequence）应由 RAN1 分析。

```text
RAN2 considers that the blind decoding complexity (e.g. DMRS and scrambling sequence) for the shared resource at the aNB should be analyzed by RAN1.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.1-p007`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.1 Scheduling

对于 CB-PUSCH BSR 的 RAN2 评估，配置假设包括 dedicated 或 shared DMRS、C-RNTI 或 common RNTI，以及典型 Msg3 配置（1 或 2 PRBs、QPSK）；beam information 的使用不受限制，且 CB-PUSCH payload 包含 UE ID。若 CB-UL transmission 后 timer 内收到 positive NW response，则 contention resolution 视为成功；失败时 UE 重试 CB-UL，且不使用 HARQ retransmission，而是在 contention resolution failure 后使用 HARQ new transmission。

```text
For the RAN2 evaluation purpose for CB PUSCH of BSR, the followings are assumed for the CB PUSCH configuration:
1) Either dedicated or shared DMRS can be used.
2) Either C-RNTI or common RNTI can be used.
3) The typical Msg3 configuration (i.e. 1 or 2 PRBs and QPSK) is used
4) No restriction on how beam information (i.e. no beam or NW-indicated or UE-selected) is used for CB-PUSCH.
5) UE ID (e.g. C-RNTI MAC CE) is included in CB-PUSCH payload.
6) If a positive NW response is received within a timer after CB-UL transmission, the contention resolution is considered as successful.
7) The UE re-attempts CB-UL transmission when contention resolution fails.
8) HARQ retransmission is not used, i.e. the UE uses HARQ new transmission after contention resolution failure.
Question for RAN1
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.1-p008`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.1 Scheduling

提出向 RAN1 询问如何在相同 time-frequency resources 上复用多个 UE 的 PUSCH，包括采用 UE-dedicated 或 shared DMRS、UE-dedicated RNTI 或 common RNTI，以及其他评估假设。

```text
Provide the following question to RAN1:
Regarding how to multiplex the PUSCHs from multiple UEs on the same time-frequency resources:
o	Whether to use UE-dedicated or shared DMRS
o	Whether to use UE-dedicated RNTI or common RNTI
Other evaluation assumption
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.1-p009`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.1 Scheduling

RAN2 评估不要求 False positive SR。已同意以 CB-PUSCH 共享资源承载多个 UE 的 BSR 作为评估起点，并规定相关评估假设；同时将评估假设作为参考发送给 RAN1，并询问发生时频资源碰撞时网络能否区分 UE 并解码 payload。

```text
False positive SR is not mandated in the RAN2 evaluation.
Noted
R2-2602024	System simulation for contention based BSR	Ericsson, LG Electronics Inc, OPPO, T-Mobile USA, Turkcell, Kyocera, Verizon, Sharp, WILUS Inc.	discussion
Observation 1	There is a need for a low complexity and scalable solution where several hundreds of connected UEs are enabled to request fine grained UL resources every slot.
Observation 4	A pure DMRS based solution is not scalable and introduce high complexity that increases with number of UEs.
Observation 6	Randomization of DMRS selection at each CB attempt results in a better contention resolution
Observation 7	Limiting the number of DMRS and including the UE identity in the payload keeps the number of blind-decoding attempts to minimum
Observation 8	The number of transmissions per CB occasion—and consequently the collision rate—remains low because usage is limited to BSRs and only when no dedicated ULSCH resources are available.
Proposal 2	RAN2 to discuss the evaluation results of various scheduling solutions including CB BSR and the SR/BSR functionality and capture them in the TR.
R2-2602801	Report of [AT133bis][006][6G UP] CB-BSR assumption (Oppo)	OPPO	discussion	Rel-20	FS_6G_Radio
=> Revised in R2-2602810
R2-2602810	Report of [AT133bis][006][6G UP] CB-BSR assumption (Oppo)	OPPO	discussion	Rel-20	FS_6G_Radio
Discussion
-	Samsung doesn’t think that we need to ask RAN1, they are studying it anyways.
-	Vivo thinks that we anyways we have our assumptions, why are we asking.  Oppo explains that is are just RAN2 initial assumptions.
-	Nokia doesn’t understand why we are discussing this again after so many discussion.
-	Huawei thinks that it is clear that if things are not separated then it is CB-PUSCH, so dedicated DMRS is not CB-PUSCH.   ZTE thinks that the main point is what happens where there is a collision.  So when time frequency resources collide can the network differentiate using scrambling code or DMRS.  RAN1 can say that even if the DMRS are different there will still be problem.
-	Ericsson thinks that reduction of aNB blind decoding complexity would be beneficial.   Qualcomm doesn’t think it is an worry if you have small number of UEs.
Noted
| Agreements on assumptions for evaluation as the starting point in RAN2: KPI For resource efficiency evaluation: UL PRB utilization (e.g. resource efficiency as defined in TR 36.881). For latency evaluation: data burst latency or/and successful-BSR latency. Collision ratio for CB based schemes Scenario TN Bursty traffic (e.g. FTP3). Transport layer protocol (e.g. TCP) can be considered. CB-PUSCH assumption CB PUSCH resources are shared by multiple UEs for the BSR transmission Blind decoding complexity (e.g. DMRS and scrambling sequence) and DMRS miss detection probability for the shared resource at the aNB can be decided by RAN1 CB PUSCH procedure: a. Either dedicated or shared DMRS can be used. b. Either C-RNTI or common RNTI can be used. c. The typical Msg3 configuration (i.e. 1 or 2 PRBs and QPSK) is used d. No restriction on how beam information (i.e. no beam or NW-indicated or UE-selected) is used for CB-PUSCH. e. UE ID (e.g. C-RNTI MAC CE) may be included in CB-PUSCH payload in the shared DMRS case. f. If a positive NW response is received within a timer after CB-UL transmission, the contention resolution is considered as successful. g. The UE re-attempts CB-UL transmission when contention resolution fails. h. HARQ retransmission is not used, i.e. the UE uses HARQ new transmission after contention resolution failure. i. A collision occurs when more than one UEs choose the same time/frequency resource and the same DMRS sequence, and all colliding PUSCHs will fail when collision occurs. Send agreements on simulation assumptions to RAN1 as a reference Ask RAN1 for following: 1 When there is a collision in time and frequency resource, is there a way for the network to differentiate the UE and decode the payload. RAN2 discussed for evaluation purposes, DMRS, scrambling code, UE ID, but would like to ask RAN1 their view and to understand probability of differentiating the UE and decoding. 2 Kindly provide any feedback |
| --- |
R2-2602808	[Draft] LS on uplink scheduling enhancements	OPPO	LS out	Rel-20	FS_6G_Radio	To:RAN1
[POST133bis][006][6G UP] CB-BSR assumption (Oppo)
Intended outcome:  Agree to LS to RAN1
Deadline:  Wednesday, April 22nd
=> Approved in R2-2602815.
R2-2602815	LS on evaluation assumptions for contention based PUSCH transmission	RAN2	LS out	Rel-20	FS_6G_Radio	To:RAN1
=> Approved
Not treated
Finer L2 scheduling – if time allows, dependent on QoS progress-
R2-2601856	6G CB-PUSCH and scheduling information reporting	Ofinno	discussion
Proposal 4	RAN2 to study finer granularity for scheduling information reporting in 6G compared to the LCG-level granularity in 5G.
R2-2601501	Discussion on scheduling	Xiaomi	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.1-p010`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.1 Scheduling

RAN2 将沿用 legacy per-LCG scheduling information reporting 作为基线。

```text
RAN2 to reuse the legacy per-LCG scheduling information reporting as the baseline.
R2-2601660	Uplink scheduling in 6G	Samsung	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.1-p011`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.1 Scheduling

RAN2 将考虑在 6G 中使用 BSR 指示待发送的 MAC CE(s) 及其潜在大小。

```text
RAN2 to consider using BSR to indicate the pending MAC CE(s) and their potential size in 6G.
R2-2601804	Consideration on Scheduling and uplink scheduling information in 6G	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.1-p012`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.1 Scheduling

研究具有更细粒度的 UL grant 增强，例如 per-LCG UL grant 和 per-LCH UL grant。

```text
Study UL grant enhancement with finer granularity, e.g., per-LCG UL grant, per-LCH UL grant.
R2-2601972	Discussion on 6G scheduling	China Telecom	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.1-p013`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.1 Scheduling

RAN2 将研究支持动态调整 LCP parameters 的新 LCP design。

```text
RAN2 to study the new LCP design that supports dynamic adjustment of LCP parameters.
R2-2601465	Discussion on scheduling procedures	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.1-p014`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.1 Scheduling

研究新的 LCP designs，使其能够以统一方式支持多个 performance objectives（例如 throughput 与 delay）。这些设计还应比 NR 更具适应性，以支持 application context awareness 和 dynamic QoS 等新用例。

```text
Study new LCP designs that
-	can support multiple performance objectives (e.g. throughput vs delay) in a cohesive way;
-	are more adaptive than NR in supporting new use cases such as application context awareness and dynamic QoS.
R2-2601446	Discussion on 6GR scheduling	vivo	discussion	Rel-20
R2-2601559	Discussion on scheduling information reporting	OPPO	discussion	Rel-20	FS_6G_Radio
R2-2601662	Scheduling Aspects for 6GR	SHARP Corporation	discussion
R2-2601700	Discussion on UL scheduling in 6G	III	discussion	Rel-20	FS_6G_Radio	R2-2601049
R2-2601717	UP Scheduling aspects	Nokia	discussion	FS_6G_Radio
R2-2601721	Discussion on Unified Scheduling Information Reporting	Pengcheng Laboratory	discussion
R2-2601777	Scheduling enhancements	ZTE Corporation, Sanechips	discussion
R2-2601831	Views on 6G User Plane: Scheduling	Apple	discussion	Rel-20	FS_6G_Radio
R2-2601851	6G scheduling	NEC	discussion	Rel-20	FS_6G_Radio
R2-2601908	Scheduling and Scheduling Information Reporting	CATT	discussion	Rel-20	FS_6G_Radio
R2-2601937	Discussion on Contention based UL resource	ASUSTeK	discussion	Rel-20
R2-2601953	On Dynamic QoS Requirements and L2 Scheduling Enhancements for AI-driven Services in 6G RAN	III, National Taiwan University	discussion	Rel-20
R2-2601988	Discussion on MAC scheduling enhancements	1Finity	discussion	Rel-20	FS_6G_Radio
R2-2601993	L2 scheduling framework for 6GR	InterDigital	discussion	Rel-20	FS_6G_Radio
R2-2602044	Further Discussion on Uplink Scheduling	Lenovo	discussion	Rel-20	FS_6G_Radio
R2-2602050	Discussion on scheduling in 6G	Transsion Holdings	discussion	Rel-20
R2-2602053	Latency reduction techniques for 6G	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20
R2-2602070	Discussion on Scheduling	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2602235	Discussion on scheduling enhancements for 6G	Panasonic	discussion	Rel-20
R2-2602276	Discussion on Scheduling enhancements	AUMOVIO	discussion
R2-2602397	Efficiently handling small UL packets	Fraunhofer IIS,  Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
R2-2602413	Considerations on scheduling for 6GR UP	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2602511	Further discussions on scheduling	Futurewei	discussion	Rel-20	FS_6G_Radio
R2-2602577	Contention-based BSR reporting	MediaTek Inc.	discussion	Rel-20
R2-2602607	Views on BSR trigger	NTT DOCOMO INC..	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.1-p015`

### [6G/Rel-20 RAN2#133bis] `agreement` 9.3.1.3.2 Other MAC functionalities

RAN2 采用两项原则：Msg1 indication 仅用于影响 msg1 transmission、RAR、Msg3 scheduling 或相关流程的用例；Msg3 early indication 仅用于影响 Msg4 scheduling 或相关流程的用例。哪些情况需要 msg1 indication 仍待根据 RAN1/RAN2 设计进展进一步研究。

```text
From RAN2 point of view, at least the following principles are used:
1	The Msg1 indication is only applied to use cases which affect msg1 transmission/RAR/Msg3 scheduling and/or related procedures.
2	The Msg3 early indication is only applied to use cases which affect Msg4 scheduling and/or related procedures.
FFS what cases need msg1 indication after further progress on RAN1/RAN2 design
R2-2601502	Discussion on other MAC functionalities	Xiaomi	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-a001`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

RA design 需要考虑基本的 NR RA-triggering events，包括 connection management、UL synchronization、resource request、cell switch、system information request 和 BFR。

```text
The RA design needs to consider basic NR RA-triggering events (e.g., connection management, UL synchronization, resource request, cell switch, system information request, BFR).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o001`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

2-step RA 在快速接入和 UE energy efficiency 方面有优势；4-step RA 则提供更广覆盖和更高可靠性。

```text
2-step RA offers benefits in fast access and UE energy efficiency, while 4-step RA provides wider coverage and higher reliability.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o002`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

CBRA 支持高效率的大规模接入；CFRA 用于避免碰撞，面向低时延和高可靠场景。

```text
CBRA supports massive access with high efficiency, while CFRA avoids collisions for latency-sensitive and high-reliability scenarios.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o003`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

MsgA/Msg3 可承载初始 RRC signaling 和 uplink data。Proposal 1 提议研究 6G Day 1 的多种 RACH 触发事件、2-step/4-step RACH、CBRA/CFRA，以及经 MsgA/Msg3 承载 RRC signaling 和 uplink data；该提议标记为 Noted。

```text
MsgA/Msg3 in random access can carry initial RRC signaling and uplink data.
Proposal 1：Study RACH procedure considering at least the following aspects:
Various RACH triggering events from 6G Day 1
Both 2-step RACH and 4-step RACH
Both CBRA and CFRA
Carrying both RRC signaling and uplink data via MsgA/Msg3
Noted
R2-2601624	Discussion on other MAC  functionalities	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o004`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

NR 为 4-step RACH 的 RAR 和 2-step RACH 的 MsgB 定义了不同的 DL response，并使用不同 RNTI 调度，以区分两种 RACH 类型。这样会降低 multiplexing flexibility，并增加 RNTI spaces 的消耗。

```text
In NR, separate DL responses are defined for 4-step RACH (RAR) and 2-step RACH (MsgB). Although RAR and MsgB (e.g., fallbackRAR in MsgB) share similarities, they must be separately scheduled using different RNTIs. This ensures UE differentiation between the two RACH types but at a cost of reduced multiplexing flexibility and increased consumption of RNTI spaces.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o005`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

NR UE 仅在达到配置的失败次数后执行 RACH fallback，并严格遵循预定义顺序。该机制忽略 UE 侧 radio link quality 的动态变化，可能增加 fallback latency，并阻止 UE 选择更合适的 RACH resources。

```text
In NR, the UE performs RACH fallback only after a configured number of failed attempts and strictly follows a predefined order. The mechanism disregards dynamic change of radio link quality at UE side, which may increase fallback latency and prevents the UE from selecting more suitable RACH resources.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o006`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

NR RACH 在初始化时选择 UL carrier 和 BWP，之后保持不变，因此无法适应小区内动态负载变化。

```text
In NR RACH, the UL carrier and BWP are selected during RACH initialization and remain unchanged thereafter, which cannot adapt to dynamic intra-cell load variations.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o007`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

通过灵活传输 preamble 和 MSG3/MSGA payload parts，6G 可采用统一框架支持 4-step RACH、2-step RACH 和 CB-PUSCH。

```text
By enabling flexible transmission of the preamble, MSG3/MSGA payload parts, 6G can support 4-step RACH, 2-step RACH and CB-PUSCH using a unified framework for all these features
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o008`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

NR 中 RedCap、eRedCap、SDT 和 network slicing 的 RACH partitioning 不要求采用根本不同的 RA response message 或 Msg3 format。因此，只要网络能在随机接入期间或之前通过其他机制识别 UE feature，6G 就不必为这些特性专门进行 RACH partitioning。

```text
In NR, RACH partitioning for RedCap, eRedCap, SDT, and network slicing does not impose requirements on a fundamentally different RA response message or Msg3 format. Therefore, dedicated RACH partitioning for these features is not an absolute requirement in 6G, provided that the network can identify the UE's feature through alternative mechanisms at or prior to the random access procedure.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o009`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

只有在 response handling 存在根本差异的特性（如 OD-SIB1）中，才需要在 PRACH detection 阶段提前识别；缺少指示会导致错误的 monitoring 或 response procedures。对于 SBFD、IAB-MT、preamble Group A/B 和 OD-SIs 等功能兼容 common configuration 的特性，单独的 RACH resource partitioning 并非严格必需，额外机制仅用于优化。

```text
Early identification at PRACH detection is required only for features with fundamental differences in response handling (e.g., OD-SIB1), where lack of such indication leads to incorrect monitoring or response procedures. For other features (e.g., SBFD, IAB-MT, preamble Group A/B, OD-SIs), separate RACH resource partitioning is not strictly required as the procedures remain functionally compatible with a common configuration, with any additional mechanisms providing optimization rather than necessity.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o010`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

NR 支持的特性中，有些必须通过 Msg1 指示，有些可以等到 Msg3，还有一些需要 RAN1 讨论。

```text
Among all these features supported by NR, some are necessary to be indicated via Msg1, some can wait for Msg3 and some require RAN1 discussion.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o011`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

NR 中支持特性及其组合会显著增加 RACH resource set selection procedure 的复杂度，尤其是在多个资源仅支持触发该 RACH procedure 的部分特性时。

```text
In NR, support of feature/feature combinations introduces significant complexity on RACH resource set selection procedure, especially when there are multiple resources supporting a subset of all features triggering this RACH procedure.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o012`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

在 NR 中，RACH resources 难以适应接入负载的短期变化，常导致高争用和接入失败。

```text
In NR, RACH resources do not adapt well to short-term variations in access load, often resulting in high level of contention and access failures.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o013`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

原文指出，NR 中的 RACH resource allocation mechanism and procedure 效率不高。

```text
RACH resource allocation mechanism and procedure in NR are not efficient.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o014`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

原文提出允许 CCCH channel segmentation，以灵活调整 MSG3 payload size、避免为 MSG3/MSGA payload size indication 进行 preamble partitioning。此举还可让可延迟到 MSG3 的功能（如 early UE type、slice indication）改用 MSG3 based indication，而非 MSG1 based indication。

```text
Allowing segmentation for CCCH channel can enable the following:
Make the MSG3 payload size flexible without compromising the coverage whilst avoiding the need for preamble partitioning for MSG3/MSGA payload size indication
Enable more features that can wait till MSG3 (e.g. early UE type, slice indication etc) to use MSG3 based indication instead of MSG1 based indication.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o015`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

原文预计 6G 中的 MAC CEs 将用于发送更多样的消息，其中一些可能要求更高的 reliability。

```text
MAC CEs in 6G are expected to be used to send more diverse types of messages, some of which may demand higher reliability.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o016`

### [6G/Rel-20 RAN2#133bis] `observation` 9.3.1.3.2 Other MAC functionalities

6G 中的 MAC CEs 可以采用更结构化的设计，以实现高效处理并满足预期更严格的 6G timing requirements。

```text
MAC CEs in 6G can be designed in a more structured way to enable efficient processing and meet the stricter timing requirements expected in 6G.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-o017`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

记录的内容为：4-step contention-based Random-Access procedure 作为 baseline 得到支持。

```text
4-step contention-based Random-Access procedure is supported as the baseline.
Noted
R2-2601502	Discussion on other MAC functionalities	Xiaomi	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p001`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

记录的内容为：6G baseline 应支持 4-step RACH 和 2-step RACH。

```text
In 6G, both 4-step RACH and 2-step RACH should be supported as a baseline.
Noted
R2-2601560	Discussion on RACH and configured grant	OPPO	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p002`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

记录的内容为：RAN2 研究 6G RACH 是否以及如何解决 5G RACH 中识别的问题，包括不同 RA types 的 RA responses 复用受限、fallback 未考虑动态 radio link quality change，以及动态 load distribution 灵活性不足。

```text
For 6G RACH, RAN2 to study whether and how to solve the following problems identified from 5G RACH:
Limitation in multiplexing the RA responses across different RA types, e.g., RAR and MsgB share similarities but cannot be multiplexed into the same DL signalling.
Lack of consideration for dynamic radio link quality change in RACH fallback, e.g., RACH fallback relies solely on attempt number and follows a predefined fallback order.
Less-flexibility in dynamic load distribution, e.g., fixed UL carrier/BWP to perform RACH after initial selection.
Noted
R2-2601778	Random Access and other MAC enhancements	ZTE Corporation, Sanechips	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p003`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

记录的提议为：6GR 支持 unified RACH framework，允许 UE 仅发送 preamble 并等待 RAR 后在 MSG3 发送 payload、同时发送 preamble 与 payload，或在 valid TA 时仅通过 contention based PUSCH transmission 发送 RACH payload。

```text
6GR should support a unified framework for RACH where the UE may transmit:
Only preamble and wait for RAR before transmitting the payload part in MSG3 (similar to 4-step RACH in NR)
Preamble + payload parts together (without waiting for RAR) – similar to 2-step RACH in NR
Only RACH payload part without preamble when the UE has valid TA – contention based PUSCH transmission
Noted
R2-2602128	Discussion of other MAC functionalities	Lenovo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p004`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

记录的协议事项为：研究 “2step” 和 “4step” RA，了解其功能后进一步研究随机接入流程能否以及如何 unified/simplified；CB-PUSCH 是否纳入 unification discussion 留待进一步进展后讨论。另记录 CBRA 和 CFRA random access procedures 均获支持。

```text
RAN2 to study a unified Random-Access procedure incorporating 2-step RACH and 4-step RACH types at least for contention-based RA procedure, e.g., Common RACH resource configuration for 2-step RACH and 4-step RACH is applied.
Noted
Discussions on 2-step/4-step RACH
-	Oppo thinks that for 6G we can use a different concept than 2 step RA
-	Qualcomm thinks that 4step is sufficient.  2step RA is low access latency and low access latency is not a key KPI for idle mode and for connected if we have CB-PUSCH then we don’t need it.  Also there is implementation complexity.  Xiaomi thinks that there are cases where the UE cannot send CB-PUSCH.
-	Ericsson thinks that we should study if we need a faster way from preamble to resource allocation.
-	Lenovo thinks that faster access is an important KPI.  We should design it so from gNB perspective it is seen a single procedure so we shouldn’t rule it out yet.
-	ZTE highlights that one important use case for 2step RA is NTN, which has very long RTT, and this is essential.    On the unification, we needed different RAR formats as 2step was added in later release and now we don’t have that problem as if we design from day one we can use one format and think that 2 step RA is the baseline.   Mediatek agrees and we shouldn’t add this in later release.
-	Samsung also see the benefits and there is no reason to exclude it from study, including how to address some of the identified issues.
-	LG agrees with ZTE and Xioami about latency benefit.
-	Sharp doesn’t think it is very essential as it can only be used when the signal condition are good.
-	CMCC thinks we can study whether to unify the PRACH and address such issues.
-	Huawei thinks that if NTN is the main reason then NTN folks need to support this.   ZTE thinks that NTN is one reason but we have other reasons including CP latency reduction.
-	Nokia supports 4 steps as a baseline and if we do 2step we can’t avoid partitioning.
-	Ofinno thinks that from functional point of view we can look at a unified design.
-	Apple also thinks it is too early to exclude anything
-	DLR also thinks unification is important for CB-PUSCH and RA
-	Mediatek reminds everyone that unification just means strive to find commonalities.
Agreements on random access
1	Study “2step” and “4step” RA.  After understanding the functionality, further study how and if the random access procedure can be unified/simplified.  FFS if and whether we can include CB-PUSCH in unification discussion only after some further progress on CB-PUSCH.
2	Both CBRA and CFRA random access procedures are supported
RA Early indications
R2-2601735	Other MAC Functionalities		Nokia 	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p005`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

记录的提议为：6G 的 RACH partitioning 应限于需要在 PRACH detection 时 early identification 以确保 procedure 正确执行的功能（如 OD-SIB1）。对于 RedCap、eRedCap、SDT、network slicing、SBFD、IAB-MT、OD-SIs 和 preamble Group A/B，应支持 common RACH configuration，因为这些功能不需要不同的 RA response 或 Msg3 formats。

```text
In 6G, RACH partitioning should be limited to features that require early identification at PRACH detection to ensure correct procedure execution (e.g., OD-SIB1). For other features such as RedCap, eRedCap, SDT, network slicing, SBFD, IAB-MT, OD-SIs and preamble Group A/B, a common RACH configuration should be supported, as they do not require distinct RA response or Msg3 formats.
Noted
R2-2601994	Other MAC functions	InterDigital	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p006`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

记录的规则为：Msg1 indication 仅适用于会影响 RAR/Msg3 scheduling 和/或相关 procedures 的 use cases。关于其是否也可用于 msg1 retransmission，原文记录了相关提问及回应：此情形未被排除，因为它会影响 RAR。

```text
The Msg1 indication is only applied to use cases which affect RAR/Msg3 scheduling and/or related procedures.
-	Vivo can this also be used for msg1 retransmission.   Interidigtal explains it is not excluded as anyways it impacts RAR.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p007`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

Msg3 indication 仅适用于影响 Msg4 scheduling 和/或相关 procedures 的用例。相关原则已 noted。

```text
The Msg3 indication is only applied to use cases which affect Msg4 scheduling and/or related procedures.
-	Samsung thinks that these are good principles and then we can wait for RAN1 design to decide what is needed based on the principle.
-	Huawei asks what is msg3 indication.  Interdigital explains that is redcap or msg4 PUSCH repetetition requests etc.
Noted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p008`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

RAN2 将推迟讨论哪些 feature 必须使用 msg1 indication、哪些可等待 msg3，直到明确支持哪些 feature 且 RAN1 确定相关 physical layer design。该提议已 noted。

```text
RAN2 to postpone the discussion on what feature absolutely needs msg1 indication and what can wait for msg3, until it is clear about which feature will be supported as well as physical layer design related to the features are determined in RAN1.
Noted
Not treated
R2-2601624	Discussion on other MAC  functionalities	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
Observation 2-1:	Additional RACH resource could be introduced in addition to RACH resource for initial access in 6G day1 and forward compatibility issues for RACH configuration should be considered.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p009`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

确认从 RAN2 角度，RACH partitioning 可避免不同 features 的 RACH configuration 参数重复，并便于 features 组合的共同配置，例如 SDT+ RedCap。

```text
Confirm the following benefits of using RACH partitioning for RACH configuration from RAN2 point of view:
Avoid duplicated parameters of RACH configuration for different features
Ease of co-configuration for features combination (e.g., SDT+ RedCap)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p010`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

若 6G day1 的 system information 除 initial access 外还需要为多个 features 配置 RACH resources，则支持通过 RACH partitioning 配置 RACH。

```text
If RACH resources for multiple features are needed in system information in addition to RACH resource for initial access in 6G day1, support RACH configuration by RACH partitioning.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p011`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

若 6G Day1 支持 RACH partition configuration，则研究简化 RACH resource set selection 的方法，例如简化 CBRA 的 priority-based fallback。

```text
If RACH partition configuration is supported in 6G Day1, study how to simplify the procedure of RACH resource set selection, e.g., by simplifying the priority-based fallback for CBRA.
Not treated
Adaptive/dynamic RACH resources
R2-2601466	Discussion on other MAC functionalities	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p012`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

研究提升资源使用效率的 RACH designs，例如 dynamic 或 on-demand allocation of RACH resources，以及 beam-specific RACH configurations。

```text
Study RACH designs that enable more efficient use of resources, e.g. dynamic or on-demand allocation of RACH resources, beam-specific RACH configurations, etc.
R2-2601518	Random Access in 6G	Samsung	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p013`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

为高效利用多个 random access resource sets 配置的资源，UE 发起 random access procedure 时可先指示将使用的 resource set，再使用所选集合执行该过程。

```text
For efficient utilization of resources configured by multiple random access resource sets, when the UE initiates random access procedure, UE can first indicate the random access resource set UE is going to use and then perform random access procedure using the selected random access resource set.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p014`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

6G 支持在 random access procedure 期间，在一组 sparsely configured random access occasions 与一组 densely configured random access occasions 之间 dynamic switch。

```text
Dynamic switch between a set of sparsely configured random access occasions and a set of densely configured random access occasions during the random access procedure is supported in 6G.
R2-2602092	Discussion on MAC functionalities in 6G	Spreadtrum, UNISOC	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p015`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

RAN2 将研究 dynamic 或 hybrid RACH resource allocation mechanism 和 procedure。

```text
RAN2 to study dynamic or hybrid RACH resource allocation mechanism and procedure.
Not treated
CCCH segmentation
R2-2601778	Random Access and other MAC enhancements	ZTE Corporation, Sanechips	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p016`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

研究 CCCH channel segmentation 的两种选项：Hard segmentation 要求网络收到所有 segments 后才能解码 Msg3；Soft segmentation 将 Msg3 定义为携带不同自包含信息片段、可独立解码的多条消息。

```text
Study the following options for segmentation of CCCH channel.
Hard segmentation: Network can only decode Msg3 after all the segments are received.
Soft segmentation: Msg3 is defined as multiple messages carrying different self-contained pieces of information that can be decoded independently.
Configured grants – adaptation and NR limitations
R2-2602025	Configured grant and random access procedure	Ericsson	discussion
Observation 1	Configured allocation is not adaptive to channel conditions or traffic changes.
Observation 2	Skip uplink leads to indeterministic receiver behaviour.
Observation 3	CG’s non-adaptive and skip uplink behaviour leads to resource inefficiency.
Observation 4	NR has multiple configured grant frameworks (Type 1 and 2) which leads to complex implementations.
Proposal 1	RAN2 to discuss and agree on below issues faced in NR CG
-	Indeterministic receiver behaviour and resource wastage due to skip uplink,
-	Complexity posed by multiple CG frameworks.
-	In-adaptive to traffic and channel variations,
-	Uplink reporting unable to address resource deficiency,
-	CG retransmissions via grants handled separately from dynamic grants,
-	Restrictions on retransmissions over CG.
Noted
R2-2601502	Discussion on other MAC functionalities	Xiaomi	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p017`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

6G CG 配置应支持可立即用于 delay critical service 的 CG resource、动态激活/去激活、动态调整 CG size、适应 jitter，以及灵活的资源共享/回收。该提议被记为 Noted。

```text
6G CG configuration should be able to allow:
- CG resource immediately usable for delay critical service;
- Dynamical activation/deactivation;
- Dynamical adjustment of CG size;
- Adaptation to jitter;
- Flexible Resource sharing/recycling.
Noted
R2-2601994	Other MAC functions	InterDigital	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p018`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

协议记录了研究 6G CG 的共识，至少支持配置后立即激活 CG resource、动态激活/去激活、动态调整 resource allocation，以及支持不同 traffic types 和更高 resource efficiency。另有意见提出应将这些 dynamic CG 选项与 dynamic grant 进行 benchmark；该意见标记为 Not treated。

```text
Configured Grants for 6GR support:
-	Semi-static configuration of resources;
-	Dynamic activation/deactivation of configured resources (e.g. by DCI);
-	Dynamic adaptation of a resource allocation and timing parameter without requiring RRC reconfiguration (e.g. indication of a start offset by DCI).
Noted
-	Mediatek thinks that we should at least benchmark all these dynamic CG options with dynamic grant.
| Agreements on configured grants 1 Study 6G CG, which can support at least the following from RAN2 perspective: - CG resource immediately activated (e.g. for delay critical service) after configuration; - Dynamic activation/deactivation; - Dynamic adjustment of resource allocation (e.g. MCS, TBS and start time); - Support different traffic types - Higher resource efficiency (e.g. unused resource indication, etc). 2 Inform RAN1 about our agreements and any further agreements in May meeting |
| --- |
Not treated
Configured grants - UE indication
R2-2601447	Considerations on 6GR CG and Random Access	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p019`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

提出研究 CG recycling mechanism：由 UE 发起 advance indication，通知 aNB 即将使用 CG。

```text
RAN2 to study CG recycling mechanism on UE initiating the advance indication to inform aNB about the upcoming CG utilization.
R2-2601832	Views on 6G User Plane: Miscellaneous MAC Mechanisms	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p020`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

为提高 CG resource efficiency，UE 可在进行 CG PUSCH transmission 前，先指示其使用特定 CG resources 的意图。

```text
To improve resource efficiency of CG, the UE may first indicate its intention to use particular CG resources, before performing CG PUSCH transmission.
R2-2601807	Discussion on Configured Grants	Philips International B.V.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p021`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

提出由 RAN2 研究如何动态更新 CG configuration。

```text
RAN2 to study how to perform dynamic updates of the CG configuration.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p022`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

提出由 RAN2 研究 UE 请求网络更改 CG configuration 的流程。材料还指出，固定长度 MAC CE 的 MAC subheader 不含 L field 只节省少量 bit overhead，却显著增加处理和实现复杂度；5G LCID design 缺乏 forward scalability，导致后续修补增加 overhead 和复杂度。

```text
RAN2 to study procedures for the UE to request a change of CG configuration to the network.
MAC PDU format and MAC CEs  (if time allows)
R2-2601624	Discussion on other MAC  functionalities	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
Observation 6-1:	Not including the L field in the MAC subheader for the fixed-sized MAC CE saves only a small bit overhead but significantly increases the processing and implementation complexity.
Observation 6-2:	The 5G LCID design lacked forward scalability, forcing incremental fixes (e.g., eLCID field or LX field) that increased overhead and complexity.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p023`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

提出由 RAN2 研究 MAC PDU format 的潜在增强，例如 L field 和 LCID design。

```text
RAN2 to study the potential enhancements for MAC PDU format, e.g., for the L field and LCID design.
R2-2601466	Discussion on other MAC functionalities	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p024`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.1.3.2 Other MAC functionalities

提出将 MAC CEs 设计为适用于多种用途的 versatile format，同时易于处理和组装。

```text
Design MAC CEs to have a versatile format suitable for multiple purposes, while easy to process and assemble.
R2-2601474	Discussion on RACH and CG	NEC	discussion	Rel-21	FS_6G_Radio
R2-2601576	Discussion on 6GR MAC Functionalities	Sharp	discussion	Rel-20	FS_6G_Radio
R2-2601857	6G Random Access and Configured Grant	Ofinno	discussion
R2-2601909	Random Access and Configured Grant	CATT	discussion	Rel-20	FS_6G_Radio
R2-2601946	Discussion on RACH partitioning for 6GR	TCL	discussion
R2-2602040	Discussion on other MAC functionalities	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
R2-2602160	Other MAC functionalities: CG and Random-access	Sony	discussion	Rel-20	FS_6G_Radio
R2-2602266	Discussion on RA procedure and CG	NTT DOCOMO	discussion	Rel-20	FS_6G_Radio
R2-2602377	Discussion on early indication in 6G RA 	ETRI	discussion	Rel-20
R2-2602414	Considerations on other MAC functionalities for 6GR UP	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2602471	Discussion on random access procedure	Google Korea LLC	discussion	FS_6G_Radio
R2-2602544	Some Views on Random Access	1Finity	discussion	Rel-20
R2-2602596	MAC processing for high data rates	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.1.3.2-p025`

### [6G/Rel-20 RAN2#133] `agreement` 10.3.1.3 Scheduling

RAN2 继续研究并牵头评估 CB based schemes，确定高层评估假设并识别所需的 RAN1 输入；评估需考虑 LTE 和 NTN simulations，并与 RAN1、RAN2 方案进行比较。Dedicated SR mechanism 被假定为请求 UL resource 的基线机制（若 RAN1 已定义），其他待比较方案仍待讨论。

```text
RAN2 continues study.  RAN2 will lead the evaluation of the CB based schemes.   Determine some high level evaluation assumptions.  Identify the inputs needed from RAN1.      NOTE: check and consider LTE simulations and NTN simulations to determine what will need to be simulated.   NTN should also be taken into account.
Intention is to compare and take into account solutions with RAN1 and RAN2 solutions.   FFS which other solutions we will continue evaluating for comparison purposes (still to discuss in this meeting…)
Assumption is that dedicated SR mechanism to request UL resource is considered as a baseline mechanism, as discussed and defined in RAN1 (if defined).
[POST133][013][6G UP] Assumptions (Oppo)
Intended outcome:
Discuss questions that need to be asked to RAN1
Discuss high level simulation assumptions to be used for evaluation in RAN2
Deadline:  Long to submission deadline
Not treated
Evaluation assumptions [20 mins –offline]
Scope of use
R2-2600377	On scheduling and latency reduction	Nokia	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-a001`

### [6G/Rel-20 RAN2#133] `agreement` 10.3.1.3 Scheduling

将支持 buffer status 和 delay status information；是否支持其他信息仍待确定。信息细节及其格式统一方式可在整体功能取得进展后讨论。

```text
Buffer status and delay status information will be supported.   FFS any other information
Details of buffer status and delay status information and how they are formatted/unified can be discussed after some progress on overall functionality.
Early Reporting
R2-2600077	Discussion on 6GR scheduling	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-a002`

### [6G/Rel-20 RAN2#133] `agreement` 10.3.1.3 Scheduling

研究用于 UL scheduling 的信息 early reporting，具体信息仍待确定。

```text
Study early reporting of information useful for UL scheduling purposes. FFS details of the information.
Not treated
Granularity of scheduling (if time allows)
R2-2600289	Scheduling Aspects for 6GR	SHARP Corporation	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-a003`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.3 Scheduling

Contention-based UL transmission 的 upper-layer design 有若干方面取决于 physical layer designs。

```text
Several aspects in the upper-layer design for contention-based UL transmission depend on physical layer designs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-o001`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.3 Scheduling

缺少 CB PUSCH 专用统计信息（如 average collision ratio）时，难以准确评估其性能或配置最优性。

```text
Without CB PUSCH-specific statistics like average collision ratio, it is challenging to accurately evaluate its performance or configuration optimality.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-o002`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.3 Scheduling

不同 traffic models 对 CB PUSCH collision rates 的影响不同，因此模拟需要采用多种模型。

```text
Traffic models will affect CB PUSCH collision rates differently, reinforcing the need for diverse models in simulations.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-o003`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.3 Scheduling

UE 数量与 CB-PUSCH resource pool 大小共同直接影响 CB-PUSCH 资源上的碰撞率。

```text
The number of UEs, together with the CB-PUSCH resource pool size, directly affects the collision ratio on CB-PUSCH resources.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-o004`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.3 Scheduling

单个 UL data burst 中，UE 可发送多次 SR 和 BSR 报告以指示 data SDU 到达；这会增加 signaling overhead 和 scheduling delay。

```text
The UE can transmit multiple SR and BSR reports to indicate data SDU arrivals within a single UL data burst, resulting in increased signaling overhead and scheduling delay.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-o005`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.3 Scheduling

具有不同 service requirements 的 flows 可通过不同的 HARQ transmission parameters 获得更好的服务，例如 MCS 和重传次数。

```text
Flows with different service requirements can be better served with different HARQ transmission parameters (e.g. MCS, number of retransmissions)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-o006`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.3 Scheduling

由于 XR 和 mobile AI 等 delay sensitive traffic 增多，NR 中的 LCP procedure 可能不足以支持 6G 中更多样化的 traffic。

```text
The LCP procedure in NR may not be sufficient in supporting more diverse traffic in 6G, due to increased presence of delay sensitive traffic such as XR and mobile AI.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-o007`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.3 Scheduling

application context awareness 和 adaptive QoS 等新的 6G use cases 要求 LCP 比 NR 更具适应性。

```text
New 6G use cases such as application context awareness and adaptive QoS require LCP to be more adaptive than NR.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-o008`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.3 Scheduling

5G 的“two-phase” LCP process 具有明确结构：第一阶段确保 mandatory 和 deterministic QoS，第二阶段处理 best-effort resource optimization。

```text
The 5G "two-phase" LCP process provides a clear structure: the first phase ensures mandatory and deterministic QoS, and the second phase handles best-effort resource optimization.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-o009`

### [6G/Rel-20 RAN2#133] `observation` 10.3.1.3 Scheduling

依赖 static priority 和 PBR configurations 的 legacy LCP mechanism，在处理动态 traffic profiles 和 context-aware QoS requirements 时不够灵活。

```text
The legacy LCP mechanism, relying on static priority and PBR configurations, leads to inflexibility in handling dynamic traffic profiles and context-aware QoS requirements.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-o010`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

提议向 RAN1 征询 contention-based UL transmission 的物理层问题，包括冲突时 UE 的识别、冲突后的重传处理及 payload size 范围。讨论中对仿真范围和职责有不同意见，并提及资源效率、blind decoding complexity、端到端时延以及 SR 作为评估基线或回退机制等事项。

```text
Ask input from RAN1 on the following physical-layer aspects of contention-based UL transmission:
-	how UEs are identified when there is a contention;
-	how retransmission after a contention is handled;
-	Range of payload size.
[3 mins]
Noted
Discussion
-	Qualcomm is concerned to have RAN2 run a full blown simulation.  It is common sense the contention based has the benefits and drawback.    ZTE agrees with Qualcomm and we should cooperate with RAN1 as early as possible, payload size.   IT would be good to have some comparison.  Ericsson thinks that we need to consider resource efficiency and blind decoding complexity.   RAN2 should do this analysis especially for end-to-end latency.   We can just agree to some high level assumptions.
-	ESA explains that we introduced CB for msg3 in IoT NTN.   We did a simulation in RAN2 but we can coordinate a bit with RAN1.
-	Nokia thinks that we have some simulation activities and the traffic model would impact and not sure whether we have the expertise.   Interdigital thinks RAN1 should be involved for some aspects but it doesn’t mean they are the only group.
-	Xiaomi thinks that RAN2 can’t do such simulations.    Ericsson doesn’t think they can model protocol aspects and end-to-end considerations.
-	Apple thinks that full scale simulation may not be needed but RAN1 should be involved.
-	Vivo thinks that even the methodology needs to be done by RAN1.
-	LG thinks that the simulations should be in RAN2 as it is related to QoS but RAN1 input is needed.
-	Mediatek thinks that the drawback can be controlled by the network.   RAN1 can provide some input but only what RAN2 determines needs.
-	Samsung thinks that there are other ways like finer granularity CG.   Sharp thinks we can start the simulation to at least check if CB has clear benefits and consider the other schemes.   Vivo thinks that RAN1 is discussing other SR based solutions.
-	ZTE thinks that the one thing missing in LTE is NTN which has long RTT times.
-	Qualcomm thinks that if we use both SR like and CB based scheme, there is no point of doing evaluation.
-	ZTE thinks that we’d have to understand what things we’d need to do to make it more efficient
-	Ericsson thinks that we shouldn’t have two solutions.  Mediatek agrees.
-	Apple thinks that CB may be beneficial in some scenarios but SR is proven to work in all scenarios.   ATT thinks that SR needs to be a fallback mechanism.    Fraunhoufer agrees with Apple, the issue is that we have many problems and we should try to find the minimum set.  Xiaomi thinks that CB-PUSCH only work when collision rate is low, so we will always need SR.
-	Docomo thinks that we don’t want duplication and SR like mechanisms will always work, so it should be assumed.
-	Samsung thinks that the network has to meet the enforced QoS requirements which is the SR mechanism.
-	Ericsson understands that we haven’t agreed to have SR mechanisms but it is used as baseline for evaluation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p001`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

初始 CB-PUSCH 研究范围限定为 RRC connected mode，以及 BSR/DSR messages。

```text
Focus the initial study of CB-PUSCH exclusively on RRC connected mode and BSR/DSR messages.
R2-2600289	Scheduling Aspects for 6GR	SHARP Corporation	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p002`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

RAN2 将研究供 BSR 和 small data transmissions 共享的 contention-based UL resources。评估假设包括每次传输由 BSR 触发、禁用 HARQ、未在规定时间内收到响应时重试 BSR；传输包含用于 contention resolution 的 UE ID，并与 DMRS sequence 复用，部分细节仍待研究。

```text
RAN2 to study contention-based UL resources shared for both BSR and small data transmissions.
R2-2600429	Evaluation assumptions for contention based BSR	Ericsson, LG Electronics Inc., OPPO, MediaTek Inc., Sharp, NTT Docomo, Verizon, AT&T, Turkcell	discussion	Rel-20
Observation 9 Allowing UE to use CB resources to transmit data will increase the frequency of CB resource usage.
Observation 10 It is feasible and can be discussed later whether to include data using the leftover resources after the BSR is included.
Observation 11 Using HARQ for CB resources for BSRs causes problems without providing any benefits.
Observation 12 It is reasonable to allow a UE to reattempt the CB transmission if the UE didn’t receive a grant within a time after the previous transmission
Proposal 3	For transmissions using CB resources, RAN2 agrees to the following evaluation assumptions:
c.	Each transmission is triggered by BSR.
d.	Each transmission is based on HARQ disabled mode.
e.	if a response was not received within a time after the previous transmission, the BSR is reattempted. FFS whether the response is an explicit (e.g., CB MAC CE) or implicit (e.g., uplink grant addressed to C-RNTI).
UE Identification
R2-2600429	Evaluation assumptions for contention based BSR	Ericsson, LG Electronics Inc., OPPO, MediaTek Inc., Sharp, NTT Docomo, Verizon, AT&T, Turkcell	discussion	Rel-20
Observation 7 Including the UE ID in the transmission is a natural solution for contention resolution.
Observation 8 DMRS sequences is needed in transmission to provide code division multiplexing to allow multiple UEs to conduct transmissions using the same resources without interference.
Proposal 3	For transmissions using CB resources, RAN2 agrees to the following evaluation assumptions:
a.	Each transmission includes a UE ID for contention resolution.
b.	Each transmission is multiplexed with a DMRS sequence. FFS the DMRS sequence is dedicated
R2-2600773	Discussion on scheduling enhancements for 6G	Panasonic	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p003`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

对于 contention-based uplink resources 上的 contention resolution，UE 不必显式向网络指示 UE-ID。

```text
For contention resolution with contention-based uplink resources, the UE need not explicitly indicate UE-ID to the network.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p004`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

RAN2 将考虑基于 DMRS detection 的反馈方案，包括 Dedicated DMRS、Shared DMRS，以及在两者之间进行 Network Configuration。

```text
RAN2 to consider feedback based on DMRS detection with the following options:
-	Dedicated DMRS
-	Shared DMRS
-	Network Configuration between dedicated and shared
R2-2600620	Discussion on 6G scheduling	NTT DOCOMO INC..	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p005`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

RAN2 应与 RAN1 协调研究 UE identification。相关议题包括 Contention resolution。

```text
RAN2 should study UE identification in coordination with RAN1.
Contention resolution
R2-2600377	On scheduling and latency reduction	Nokia	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p006`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

仿真结果应包含平均碰撞比等统计数据，并说明 UE multiplexing、CB PUSCH resource size 和 traffic models 的假设。

```text
Simulation results should include statistics, such as the average collision ratio, alongside assumptions for UE multiplexing, CB PUSCH resource size, and traffic models.
R2-2600620	Discussion on 6G scheduling	NTT DOCOMO INC.	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p007`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

对于 CB-PUSCH 的 contention resolution，基线考虑 UE 在网络分配 UL grant 时判定成功，在 timer 到期时判定失败。

```text
On contention resolution for CB-PUSCH, the followings are considered as a baseline.
	A UE can consider the contention resolution successful when the UL grant is allocated by the network.
	A UE can consider the contention resolution failure when a timer expires.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p008`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

RAN2 将从 collision tolerance、coverage、latency 和 resource efficiency 方面评估 CB scheme。原文指出，CB-PUSCH 在 UE 数量较少时 latency 较低；UE 数量增长时，SR 的 latency 更低且更稳定，并提议进一步研究 UE population 对 CB-PUSCH 与 SR 的 latency 和 resource usage 表现的影响。

```text
RAN2 to evaluate CB scheme from collision tolerance and coverage aspects as well as latency and resource efficiency.
R2-2600961	Considerations on scheduling for 6GR UP	CMCC	discussion	Rel-20	FS_6G_Radio
Observation 1d: CB-PUSCH has less latency with a small group of UEs, however, when the UE population grows, SR has less and stable latency compared to CB-PUSCH
Proposal 1b: RAN2 should further study the evaluation assumptions with UE population which has impact on the latency and resource usage performance for both CB-PUSCH and SR.
R2-2600245	Discussion on Scheduling	CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p009`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

UL latency reduction solutions 可从 PUSCH resource configuration、collision probability 和 contention resolution 角度进行比较。

```text
The UL latency reduction solutions can be compared from the following perspectives: PUSCH resource configuration, collision probability and contention resolution.
Other
R2-2600403	Contention-based BSR reporting	MediaTek Inc.	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p010`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

RAN2 将研究 contention-based uplink resource pool 的配置或向 UE(s) 指示的机制。

```text
RAN2 to study the mechanism that how the contention-based uplink resource pool is configured or indicated to UE(s).
R2-2600059	Scheduling in 6G	Samsung	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p011`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

支持使用周期性 UL grants（即 configured grants）进行快速 BSR delivery。

```text
Periodic UL grants (i.e. configured grants) for fast BSR delivery is supported.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p012`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

可选配置 PUCCH resource，用于指示 UL grants 是否用于 BSR。

```text
PUCCH resource to indicate usage of UL grants for BSR can be optionally configured.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p013`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

对于 contention based BSR，将配置专用于 BSR 的 2 step RACH configuration，并由多个 UE 共享。可选择为共享该配置的 UE 分别分配 preambles。

```text
For contention based BSR, 2 step RACH configuration dedicated for BSR purpose is configured. The 2 step RACH configuration is shared with multiple UEs. Preambles can be optionally assigned separately to UEs sharing the 2 step RACH configuration.
Not treated
Scheduling request
R2-2600377	On scheduling and latency reduction	Nokia	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p014`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

支持在 6G 中使用 Dedicated SR 请求 UL resource，无论是否引入 CB-PUSCH。

```text
Dedicated SR to request UL resource is to be supported for 6G, regardless of whether CB-PUSCH would be introduced.
[2 mins]
R2-2600289	Scheduling Aspects for 6GR	SHARP Corporation	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p015`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

RAN2 将研究更细粒度的 SR，以支持无需单独发送 BSR 即可直接分配 UL resource。

```text
RAN2 to study finer granularity of SR to enable direct UL resource allocation without separate BSR transmission.
[2 mins]
R2-2600449	Views on 6G User Plane: Scheduling	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p016`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

为降低 SR/BSR latency，可考虑用 SR configuration ID 表示部分 buffer status 信息，例如 buffer size 或是否存在 delay-critical data。这样即使没有 BSR，网络也能及时分配更合适的 UL resource。

```text
To reduce SR/BSR latency, RAN2 can consider using SR configuration ID to represent certain information related to the buffer status (e.g. buffer size, or presence of delay-critical data), such that network can timely allocate more appropriate UL resource even without BSR.
[2 mins]
Scheduling Information Reporting
Unified BSR/DSR
R2-2600077	Discussion on 6GR scheduling	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p017`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

RAN2 应研究统一 BSR 和 DSR framework，包括基于 data arrival 和/或 remaining time 的协调触发机制，以及同时包含 delay status 和 buffer status 的集成报告格式。该提议标记为 Noted。

```text
For a unified BSR and DSR framework in 6GR, RAN2 should study the following aspects:
-	Harmonized triggering mechanisms based on joint consideration of data arrival and/or remaining time;
-	Integrated reporting formats comprising both delay status and buffer status.
Noted
R2-2600427	Discussion on UL scheduling aspects in 6G	Lenovo	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p018`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

RAN2 将研究统一的 UL data-related status reporting procedure，报告 data/buffer status、data 的 delay status 及潜在的其他信息（例如 data importance）。讨论中对 DSR 是否总是包含、触发条件是否相同，以及分别定义 BSR、DSR 和两者组合等问题提出了不同观点。

```text
RAN2 to study a unified UL data-related status reporting procedure in 6G which includes information on the data/buffer status as well as the delay status of the data and potential further information, e.g. importance of the data.
[2 mins]
Noted
Discussion
-	Ericsson thinks that the unification shouldn’t impact the frequency of the BSR reporting and we should design it such that DSR is not always included.
-	Lenovo thinks that if we trigger BSR why not include DRS.  The triggers can be same.
-	Apple thinks that if we have data arrival but not delayed data, there is no reason to report DRS.   Having an integrated BSR/DSR is fine but we should consider defining just BSR and just DSR and one that includes boths.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p019`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

6GR 将研究基于预计 burst arrival 信息（例如 burst arrival time、burst size）并具备 service-awareness 的 early uplink radio resource request triggering mechanism。该提议标记为 Noted。

```text
6GR to study early uplink radio resource request triggering mechanism based on the estimated burst arrival information (e.g., burst arrival time, burst size) with service-awareness.
[3 mins]
Noted
R2-2600737	L2 scheduling framework for 6GR	InterDigital	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p020`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

支持报告 UL data burst 的 anticipated data arrival，并可报告 burst delay、data packet units 数量和 packet size；报告须遵守 data burst 和 network configuration 设定的约束。该提议标记为 Noted。

```text
Reporting anticipated data arrival for an UL data burst is supported (burst metrics: burst delay, number of data packet units, packet size), within the constraints set by the data burst and network configuration.
[2 mins]
Noted
R2-2600151	Discussion on scheduling and scheduling information reporting	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p021`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

RAN2 将研究通过在数据到达 AS buffer 前提前触发 SR 来降低 dynamic scheduling 的 UL resource request latency。讨论涉及提前报告 SR 和 BSR、traffic characteristics 以及 burst characteristics。

```text
RAN2 to study latency reduction of UL resource request for the dynamic scheduling by the early triggering of SR before data arriving at the AS buffer.
[2 mins]
Noted
Discussion
-	Qualcomm supports early reporting for both SR and BSR and how the UE determines it its UE implementation.
-	Fraunhoufer indicates that we should be able to also provide some traffic characteristics.
-	Interdigital thinks that we also touched upon burst characteristics so those would be useful to report to the scheduler.  Mediatek asks if we report BSR and DSR don’t we provide enough information.  Interdigital explains that we’d provide burst information not the BSR per logical channel.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p022`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

Buffer status 按 LCG 指示。

```text
The buffer status is indicated per LCG.
R2-2600523	Consideration on Scheduling and uplink scheduling information in 6G	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p023`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

将研究 6G BDR scheduling information 的增强，包括更细粒度的信息（例如 per-QoS flow、per-LCH 或 per-importance level），以及 pending MAC CE 的 expected size。

```text
Study following enhancements for scheduling information in 6G BDR:
-	Scheduling information with finer granularity, e.g. per-QoS flow, per-LCH, or per importance level
-	Expected size of pending MAC CE
R2-2600141	Discussion on scheduling procedures	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p024`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

支持更细粒度的 HARQ，并允许网络通过不同 HARQ processes 调度不同 logical channels。

```text
Support finer granularity for HARQ and allow network to schedule different logical channels by separate HARQ processes.
Data/Logical Channel Prioritization (if time allows)
R2-2600484	Discussion on scheduling in 6GR	China Telecom	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p025`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

RAN2 研究支持动态调整 LCP 参数的新设计。

```text
RAN2 to study the new LCP design that supports dynamic adjustment of LCP parameters.
R2-2600077	Discussion on 6GR scheduling	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p026`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

RAN2 进一步研究 LCP 增强，考虑流量特性变化，包括 delay、importance 以及 inter-QoS flow/packet dependency。

```text
RAN2 to further study LCP enhancements considering the varying traffic characteristics, e.g., delay, importance, inter-QoS flow/packet dependency.
R2-2600141	Discussion on scheduling procedures	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p027`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

研究新的 LCP 设计，以统一支持多种性能目标、直接处理拥塞，并更灵活地支持 application context awareness 和 adaptive QoS 等新用例。

```text
Study new LCP designs that
-	can support multiple performance objectives (e.g. throughput vs delay) in a cohesive way;
-	are more direct in handling congestion (e.g. UL grant for a specific LCH);
-	are more adaptive than NR in supporting new use cases such as application context awareness and adaptive QoS.
R2-2600099	Consideration on 6G UP Scheduling and retransmission	Xiaomi	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p028`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.1.3 Scheduling

建议研究面向 6G 的增强 LCP framework，保留并澄清定义明确的 two-phase LCP process。该框架包括动态调整 LCP 参数，例如 logical channel priority、Prioritized Bit Rate (PBR) 和 token bucket state (Bj)。

```text
RAN2 is recommended to study an enhanced LCP framework for 6G, which includes:
-	Retention and clarification of a well-defined "two-phase" LCP process;
-	Support for the dynamic adjustment of LCP parameters, including but not limited to:
	Logical channel priority (extending beyond delay based boosting);
	Prioritized Bit Rate (PBR) and token bucket state (Bj).
R2-2600095	Discussion on 6GR scheduling	WILUS Inc.	discussion	FS_6G_Radio
R2-2600100	Discussion on DSR enhancement	Xiaomi, BYD, Ofinno, Meta, Huawei, HiSilicon, Toyota ITC	discussion	Rel-20
R2-2600166	Contention based UL channel for 6G	ZTE Corporation, Sanechips, Sony	discussion
R2-2600209	Discussion on scheduling improvements	OPPO	discussion	Rel-20	FS_6G_Radio
R2-2600211	Considerations for signaling design for contention-based scheduling	Tejas Network Limited	discussion	Rel-20
R2-2600350	Discussion on scheduling enhancements for 6G	Fujitsu	discussion	Rel-20	FS_6G_Radio
R2-2600386	On the improvements for the 6G BSR	Google	discussion	Rel-20	FS_6G_Radio
R2-2600400	Latency reduction for 6GR	Fraunhofer IIS, Fraunhofer HHI	discussion
R2-2600519	Discussion on Scheduling	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2600579	Discussion on Contention based UL resource	ASUSTeK	discussion	Rel-20
R2-2600628	Discussion on scheduling in 6G	Transsion Holdings	discussion	Rel-20
R2-2600655	6G UL scheduling	NEC	discussion	Rel-20	FS_6G_Radio
R2-2600721	Improving resource efficiency for small UL packets	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
R2-2600856	6G Scheduling and information reporting	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2600897	Discussions on scheduling enhancements	Futurewei	discussion	Rel-20	FS_6G_Radio
R2-2600973	Discussion on scheduling in 6G	DENSO CORPORATION	discussion	Rel-20
R2-2601043	Scheduling enhancements for 6GR	CEWiT	discussion	Rel-20	FS_6G_Radio
R2-2601049	Discussion on UL scheduling in 6G	III	discussion	Rel-20	FS_6G_Radio
R2-2601108	Discussion on 6GR Scheduling 	Rakuten Mobile, Inc	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.1.3-p029`

### [6G/Rel-20 RAN2#132] `agreement` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

RAN2 将研究提升 scheduling（包括 contention based schemes）时延和 UL resource efficiency 的方案。CB UL 研究以至少现有 normal SR/BSR functionality 为比较基线，并可说明方案与 5G 机制的异同；进一步假设取决于已识别方案，仍待讨论。

```text
1	RAN2 will study solutions on how to improve latency and UL resource efficiency of scheduling (including contention based schemes).
2	RAN2 study on CB UL will assume the following:
-	Baseline for comparison is at least the normal SR/BSR functionality we have today
-	Companies can highlight the similarities and differences between the proposed solutions with what we have today for 5G (e.g. shared CG resources with or without retransmissions, 2-step RACH like scheme without preamble etc).
-	Discussion on further assumptions is FFS based on the solutions identified.
Scheduling requests
R2-2508310	UP functionalities and requirements	Nokia, Nokia Shanghai Bell	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-a001`

### [6G/Rel-20 RAN2#132] `agreement` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

为支持 voice 等周期性业务，基线支持 DL SPS。UL 继续研究 CG like mechanisms，以适配 voice、bursty traffic 和其他周期性业务。

```text
To support periodic traffic like voice, as a baseline support DL SPS
For UL, continue to study CG like mechanisms to address different types of traffic, including voice, bursty traffic, other periodic traffic etc.
BSR
R2-2508408	Scheduling and Retransmission Aspects	SHARP Corporation	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-a002`

### [6G/Rel-20 RAN2#132] `agreement` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

研究提供 scheduling information 的机制，至少包括 buffer status reporting 和 delay status reporting；是否需要其他信息取决于 traffic/services，仍待确定。详细功能取得进展后，目标是在可能时统一 framework。

```text
Study mechanisms to provide scheduling information (including at least buffer status reporting, delay status reporting).   FFS other scheduling information needed depending on traffic/services.   Aim to unify the framework if possible, after some progress on the detailed functionalities.
(Not treated) (If time allows)
LCP
R2-2508034	Discussion on scheduling in 6G	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-a003`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

依赖 HARQ coordination 可能加快 RLC recovery loop。RLC Sequence Number-window based mechanism 可保证最终纠正所有 HARQ errors，且使 NW 能在 latency、spectral efficiency、power、overhead 和 processing 等 design KPIs 之间权衡。

```text
Reliance on HARQ coordination may speed up the RLC recovery loop. However, the RLC Sequence Number-window based mechanism guarantees that eventually all HARQ errors are corrected independent of HARQ degradation, and gives NW flexibility to trade off different design KPIs (latency, spectral efficiency, power, overhead, processing, etc.)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-o001`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

如果 UE 获得 UL transmissions 的 HARQ feedback，UL data 就可以可靠传输。

```text
UL data can be reliably transmitted if the UE gets HARQ feedback for UL transmissions.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-o002`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

在 NR 中，发送 BSR/DSR MAC CE 前需通过 SR 或 RACH 经历多个步骤和信令交互以获取 UL grant。这会增加 UL transmission latency。

```text
In NR, several steps/signalling interactions are required to acquire the UL grant for BSR/DSR MAC CE transmission, i.e., via SR or RACH, which increases UL transmission latency.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-o003`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

Contention-based UL transmissions 不应成为发送 SR/BSR 的唯一选项，因为其时延不确定，并可能取决于 transmission occasions 的周期性、contention levels 等因素。

```text
Contention-based UL transmissions should not be the only option for sending SR/BSR, as its latency is not deterministic and can depend on several factors, such as periodicity of transmissions occasions, contention levels, etc.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-o004`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

BSR 和 DSR 存在重复，导致 signalling overhead，甚至造成 inefficiency。

```text
BSR and DSR have duplication which results in signalling overhead or even inefficiency.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-o005`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

application context awareness 和 adaptive QoS 等新的 6G use cases 要求 LCP 比 NR 更具适应性。

```text
New 6G use cases such as application context awareness and adaptive QoS require LCP to be more adaptive than NR.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-o006`

### [6G/Rel-20 RAN2#132] `observation` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

legacy LCP procedure 会导致 LCH starvation、resource inefficiency，以及处理动态 traffic requirements 时缺乏灵活性，尤其影响 delay-sensitive applications。

```text
The legacy LCP procedure leads to LCH starvation, resource inefficiency, and inflexibility in handling dynamic traffic requirements—particularly for delay-sensitive applications.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-o007`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

Sequence number-based L2 recovery mechanism 是 ARQ 的基线；ARQ 保留独立于 HARQ、实现最高 100% reliability 的要求。讨论指出，即使禁用 HARQ，ARQ 仍可启动。

```text
Sequence number-based L2 recovery mechanism is the baseline for ARQ. ARQ to retain the requirement to achieve up to 100% reliability independent of HARQ.
-	Vivo asks what happens if HARQ is disabled.  Qualcomm explains that ARQ can still kick in.
Noted
R2-2508107	Discussion on 6G scheduling and (re-)transmission schemes	OPPO	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p001`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

支持基于 STATUS reporting 的 ARQ retransmission。

```text
ARQ retransmission based on STATUS reporting is supported.
Noted
R2-2508567	Discussion UL scheduling and Retransmission protocols	Lenovo	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p002`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

RAN2 将研究由 HARQ status 和 feedback 在 transmitter side 本地触发 ARQ retransmissions 的机制。

```text
RAN2 to study mechanisms for locally triggered ARQ retransmissions at the transmitter side based on HARQ status and feedback.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p003`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

RAN2 将研究基于 HARQ status 或 feedback 触发更快 RLC retransmission 的机制，包括 transmitter side 本地触发 ARQ retransmissions，以及由 network indications 显式启动本地 NACK procedures。

```text
RAN2 to study mechanisms enabling faster RLC retransmission triggered based on HARQ status or feedback, including locally triggered ARQ retransmissions at the transmitter side and explicit network indications to initiate local NACK procedures.
Noted
---
R2-2508319	Scheduling and retransmission enhancements for 6G	ZTE Corporation, Sanechips	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p004`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

建议 RAN2 研究 UL fast ARQ mechanism，由 lower layer signalling（例如 DCI）触发，使 upper layers 能立即进行类似 ARQ 的 retransmission。并建议通知 RAN1 支持 DCI signalling。

```text
RAN2 should study a fast ARQ mechanism for UL where the ARQ is triggered by lower layer signalling (e.g. in DCI) to enable an immediate ARQ like retransmission from upper layers – inform RAN1 to enable the DCI signalling for this
Noted
R2-2508126	On latency reduction mechanisms for 6G eMBB traffic	MediaTek UK	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p005`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

UE 获得显式 HARQ feedback，以指示 UL transmissions 的 decoding result。

```text
The UE is provided with explicit HARQ feedback that indicates the decoding result of UL transmissions.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p006`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

一致认为 ARQ 支持 sequence number-based L2 recovery，并研究基于 HARQ process status、由 transmitter side 更快触发 ARQ retransmissions 的机制，先从 UL 开始，也可考虑 DL。RAN2 认为 gNB 提供显式 UL HARQ process status 有益，其具体细节待进一步研究。

```text
Send an LS to RAN1 to take the following design requirements into consideration:
2.	HARQ feedback designed to be robust to misinterpretation
3.	HARQ feedback made available to the UE for UL transmissions
Noted
Discussion
-	LG asks why we need SN if we have HARQ feedback.   Interdigital explains that there are cases where this is needed, including NTN where there may be no HARQ.
-	Samsung thinks that this should be an optional feature.   Sharp thinks we should only support one mechanism.
-	Lenovo agrees that explicit HARQ status is beneficial.   Interdigital agree and for configured grant there is no explicit feedback.  Qualcomm agrees that we may need the status but we need to first discuss and then if we agree then we can tell RAN1.
-	Oppo explains that the UE only know if the packet has to be retransmitted but not if it was successful.  Apple agrees.  We should tell RAN1 that this is beneficial for RAN2 so please implement it.
-	Nokia also thinks that it makes sense to tell the UE why the packet is dropped.   Vivo wonders why we need to bother RAN1 as MAC CE.
-	Sony thinks that feedback would create overhead
-	Huawei thinks that RAN1 has introduced explicit feedback for CG
-	Ericsson thinks that L1 signaling should be used and we should bother RAN1.
-	LG agrees that we should be careful because for CG we would be increasing resource inefficiencies.
Agreements on HARQ - ARQ
1	Assume that sequence number-based L2 recovery mechanism is supported for ARQ
2	Study mechanisms for faster ARQ retransmissions at the transmitter side based on HARQ process status (e.g. whether the TB was successful or not).   Start with UL and can consider DL.
3	From RAN2 perspective, it is beneficial to have explicit UL HARQ process status from gNB for this purposes.  FFS on the details of explicit UL HARQ process status.
UL contention-based resources
R2-2508107	Discussion on 6G scheduling and (re-)transmission schemes	OPPO	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p007`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

为降低 UL latency，RAN2 将支持 contention-based CG resources，至少用于直接传输 BSR/DSR MAC CE。

```text
To reduce UL latency, RAN2 to support contention-based CG resources at least for direct BSR/DSR MAC CE transmission.
-	Xiaomi would like to understand the difference between the current shared resource and DMRS based resolution and this proposal.   Oppo considers that the 6G solution can perform more, as NR is NW implementation.   LG explains that in legacy the UE doesn’t know if it is shared or not so doesn’t need to be involved in contention resolution phase.
-	Fraunhaufer asks whether the proposal is limited to CG.  Oppo explains that it is an example.
-	Samsung asks what is the use case we are targeting as it doesn’t work for URLLC.  Oppo thinks that this to address the resource efficiency.  Samsung thinks that this will then increase latency in the cases of contention.
Noted
R2-2508034	Discussion on scheduling in 6G	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p008`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

SR/BSR 使用哪类 UL resources（例如 CBUL、CG 或 PUCCH）可由 network configuration 决定。将研究降低不同 UL resources 上 SR transmission latency 的技术。

```text
Which type of UL resources (e.g. CBUL vs CG vs PUCCH) should be used to for transmitting SR/BSR can be left to network configuration. Study techniques that can reduce transmission latency of SR over different types of UL resources.
Noted
R2-2508126	On latency reduction mechanisms for 6G eMBB traffic	MediaTek UK	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p009`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

建议将 contention-based UL PUSCH resource 用于 early BSR reporting，并通知 RAN1 考虑该设计要求；讨论支持研究和比较方案，同时指出需评估相对现有方案的收益及碰撞概率。讨论还提出 UE ID、DMRS 是否专用或共享，以及 CB 是否仅限 BSR 等待研究的问题。

```text
Send an LS to RAN1 to take the following design requirements into consideration:
1.	Contention-based UL PUSCH resource designed for early BSR reporting
Noted
Discussion
-	LG thinks it is important to study such types of schemes.
-	Xiaomi doubts the real motivation of this compared to real CG
-	Lenovo agrees to study but we should compare it to other schemes and see if it provides real gains.
-	Apple, Nokia thinks we can study but it is important to evaluate how much additional benefits we get when compared to what we have already.   Also RAN1 should be involved for study the collision probability etc.  ZTE thinks RAN2 can evaluate too.
-	Vivo also thinks that we need to compare all the solutions, but we can study.  Offino also thinks we can study.
-	Mediatek thinks we should study mechanism to reduce latency.  Ericsson and Sony thinks that it is both resource efficiency and latency.
-	Sony thinks we should consider other schemes as well.
-	Nokia thinks that no matter what we design it is important to have network control on what scheme being.
-	Ericsson thinks that we should study performance evaluation as well and encourages companies to also evaluate and should highlight the benefits.
-	Interdigital thinks that in the case there is no contention the benefit is latency but if there is contention then latency is a function of collision.   The network should have the tools to configure the needed scheme.
-	Huawei explains that one use case is the bursty type of data.  Huawei asks what is the benchmark and we need to discuss simulation assumptions.
-	ZTE views this also a channel for any bursty data, so the UE doesn’t have to send BSR.  So it should be generic and we need to study how much data can be sent on this.  Lenovo that one issue is that if more data is transmitted on these resources the collision probability will be increased, so let’s start with BSR and then determine if we can transmit any higher layer data.
-	Fraunhaufer thinks we need to understand the type of traffic we are trying to address it is difficult to evaluate
-	Samsung is concerned that we haven’t agreed about the current BSR so it is too early to evaluate.   Ericsson thinks that we know how the current protocols work and when we have bursty UL traffic we save quite a lot.    We looked at UL data and the issue is that it increased collision.
-	Ericsson thinks that we don’t need to go into tiny details of simulation assumption alignment.
-	Qualcomm thinks that some of these aspects depend on the PHY characteristics, so we should wait for some understanding how it works.  LG doesn’t thinks that the RAN1 progress is so important and also UL traffic is also not so important.    All we want to do is evaluate is comparison between legacy procedure and skipping the SR.   ZTE agrees with LG.   One thing we need to understand the contention resolution (e.g. whether we put an ID in the channel or if RAN1 has a way to differentiate the UE).
-	Huawei asks whether this is a RAN1 and/or RAN2 solution.  If we discuss in RAN2 we should only discuss RAN2 related aspects.
-	Xiaowei thinks we should compare with shared CG and not with SR.
-	Vivo thinks that this RAN2 solution and it should be started in RAN2, and we can use 5G baseline design for evaluation.
After offline the following were brought up
1. 	Whether UE ID is needed to address contention resolution
2.	Whether DMRS is dedicated or shared
3.	Whether to limit CB to BSR or also include data.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p010`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

6G 应支持 dedicated SR，用于请求 UL resource，并支持类似 BSR/DSR 的机制报告 buffer status 和 delay information；无论是否引入 CB-PUSCH。

```text
For scheduling information, dedicated SR to request UL resource as well as BSR/DSR like mechanism to report buffer status and delay information are to be supported for 6G, regardless of whether CB-PUSCH would be introduced.
From 10.3.1.1
Noted
R2-2508138	Discussion on scheduling, retransmissions and uplink scheduling information in 6G	Huawei, HiSilicon	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p011`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

当 UE 没有可用于向 RAN 发送 scheduling information 的 UL-SCH resource 时，UE 向 RAN 发送 scheduling request，以请求用于发送该信息的 UL-SCH resource。

```text
When there is no UL-SCH resource for the UE to send the scheduling information to RAN, UE sends scheduling request to the RAN for UL-SCH resource for sending such scheduling information.
Noted
Discussion
-	Xiaomi and Samsung think that it is very important to keep the dedicated SR as it is too risky in high system load scenarios.
Configured grants
R2-2508049	Discussion on 6GR scheduling and retransmission	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p012`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

以 5G 中 Type 1/2 configured grant 为起点，进一步研究 6GR 的 resource efficiency enhancements，用于低时延上行资源分配。

```text
Both Type 1/2 configured grant in 5G are supported as the starting point, and 6GR further study the related resource efficiency enhancements, for low latency uplink resource allocation.
Noted
R2-2508848	Considerations on scheduling and retransmisson for 6GR UP	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p013`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

RAN2 应研究 CG 的 radio resource configuration 和 adjustment enhancement，以支持突发流量业务。

```text
RAN2 should study radio resource configuration and adjustment enhancement for CG to adopt service with bursty traffic.
Not treated
R2-2508127	On scheduling, retransmissions and uplink scheduling information	Nokia, Nokia Shanghai Bell	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p014`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

提出研究统一的 CG framework，至少满足 RRC-based configuration、Flexible CG activation，以及使用 DCI 进行 Flexible modification。讨论中对是否统一 Type 1/2 CG、采用何种基线及如何适配 bursty traffic 存在不同意见。

```text
Study a unified CG framework that satisfies at least the following requirements: 1) RRC-based configuration, 2) Flexible CG activation, 3) Flexible modification using DCI
Noted
Discussions
-	CATT thinks that CG type 1 is for delay sensitive services and type 2 is for overhead so it is very hard to unify.    Nokia agrees that those are for two for different requirements but it doesn’t mean we can’t try to find a way in 6G to unify.
-	Lenovo asks what is the difference between 2 and 3.
-	Oppo likes the idea to unify
-	sony thinks the 3rd bullet flexible modification of transmission parameters  using DCI/UCI
-	Ericsson thinks that first we must agree on the issues and then we can determine whether any enhancements are needed.
-	Apple asks what is the baseline R15 or R16 CG as baseline, they think R16 should be the baseline.
-	Interdigital thinks that the multiple CG and trying to predict the traffic, wasn’t the most useful way.   In 6G we are discussing bursty traffic so predictability is difficult so we should look at how to adapt the CG more dynamically for these types of traffic.
-	LG think that both functionalities are needed.   But current solutions are too static so we should consider something similar to what Nokia is proposing so we can unify and be more dynamic.
-	Huawei thinks that if we have bursty data we shouldn’t have CG in the first place.  So each CG enhancment has to have a reason.   We can take legacy type 1 and type 2 from the beginning as we will still have voice and urllc.
-	Samsung thinks we should first wait for what type of traffic characteristic we have then we can discuss.
-	Mediatek thinks that these discussions can be discussed together with the resource efficiency discussion.   We shouldn’t use a baseline from NR.
-	Qualcomm thinks that we should have CG in 6G and we can study enhancements but we don’t need to unify as there is no commonality between the two.  They were designed for two different reasons and have different PHY procedures.
-	Ofinno thinks we should have Rl15 as baseline.
-	ZTE indicates that we have to at least support voice and therefore we need something periodic like DL SPS. For UL we can discuss how to address repeating traffic, including voice and other types of traffic including bursty.   Lenovo agrees that we should support some form of semi-persistent schedule.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p015`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

RAN2 应研究统一的 buffer status reporting，报告 total buffered data volume 和 buffered data 的 delay status。

```text
RAN2 to study a unified buffer status reporting including total buffered data volume and delay status of the buffered data.
Noted
R2-2508127	On scheduling, retransmissions and uplink scheduling information	Nokia, Nokia Shanghai Bell	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p016`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

提出为 6G 定义统一的 buffer status 和 delay status reporting procedure，并覆盖新类型数据的报告。讨论涉及是否采用统一 DSR/BSR、统一 signaling 或 procedure，以及报告内容、触发条件和格式。

```text
For scheduling information report, we aim at defining unified procedure for buffer status and delay status reporting, covering also the report of new types of data for 6G.
Noted
Discussion
-	Apple thinks that before we talk about unified DSR, we should first discuss whether we have DSR.
-	Qualcomm thinks we should have a unified DSR/BSR and what we include.
-	Lenovo thinks we should have a unified scheduling procedure and not just limit to DSR/BSR
-	CATT supports but asks what is the understanding on the solution.
-	Docomo thinks that we should separate whether we unify singaling or procedures. And signaling we should be careful as BSR is small so we should not impact performance.   Nokia thinks we should consider both, including triggers.  We can consider to indicate what we are reporting but the MAC CE format can be unified.   Also we can also discuss the format as we have different BSR for grant sizes.
-	Vivo asks about the triggers, if we unify do we have to report both.  Nokia thinks we can discuss.
-	Ericsson thinks we should have unified buffer related information and not limit it only to MAC CE.
-	MEdiatek asks for eMBB I don’t care about latency so do we need to report DSR.    Nokia think we can configure whether DSR I reported.
-	Huawei doesn’t think it matters at this point,we should discuss what needs to be reported, buffer status and delay.  ZTE agrees.
-	Interdigital thinks that we are going into stage 3 details, but the intention is that buffer status reporting and DSR are not separately transmitted when both pending.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p017`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

提出研究新的 LCP designs，以 cohesive 方式支持多个 performance objectives（如 throughput 与 delay），并增强对 application context awareness 和 adaptive QoS 等新用例的适应性。

```text
Study new LCP designs that can support multiple performance objectives (e.g. throughput vs delay) in a cohesive way and be more adaptive than NR to support new use cases such as application context awareness and adaptive QoS.
R2-2508094	Consideration on 6G UP Scheduling and retransmission	Xiaomi	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p018`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

提出研究增强型 LCP mechanism，使 LCP parameters 能够动态调整。

```text
Study enhanced LCP mechanism allowing dynamic adjusting of LCP parameters.
R2-2508049	Discussion on 6GR scheduling and retransmission	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p019`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.1.3 Scheduling, retransmissions and uplink scheduling information

以 5G 的 LCP design 为起点，RAN2 进一步研究 LCP enhancements，并考虑 delay、importance 及 inter-QoS flow/packet correlation 等 traffic characteristics。

```text
LCP design in 5G is taken as a starting point, RAN2 further study LCP enhancements considering the traffic characteristics, e.g. delay, importance, inter-QoS flow/packet correlation.
R2-2508060	Addressing the SR/BSR User Plane Latency: Round-Trip Grants	Fraunhofer IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
R2-2508146	Cross-layer coordination between ARQ and HARQ for 6G user plane	KT Corp.	discussion	Rel-20	FS_6G_Radio
R2-2508225	Discussion on L2 re-transmission in 6G	Transsion Holdings	discussion	Rel-20
R2-2508235	Discussion on L2 Retransmission and Scheduling	CATT	discussion	Rel-20	FS_6G_Radio
R2-2508270	Discussion on scheduling enhancements for 6G	Fujitsu	discussion	Rel-20	FS_6G_Radio
R2-2508316	Retransmissions and scheduling aspects for 6G	Samsung	discussion	Rel-20
R2-2508344	Scheduling and retransmissions	Ericsson	discussion	Rel-20
R2-2508383	Views on 6G User Plane: HARQ and Scheduling	Apple	discussion	Rel-20	FS_6G_Radio
R2-2508439	Consideration on Scheduling, retransmissions and uplink scheduling information in 6G	LG Electronics Inc.	discussion	Rel-19	FS_6G_Radio
R2-2508523	Discussion on 6GR User plane	KDDI Corporation (TTC)	discussion	Rel-20
R2-2508544	Scheduling enhancement to address latency – initial simulation results	Sony	discussion	Rel-20	FS_6G_Radio
R2-2508596	Discussion on Scheduling and Retransmission	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2508615	UL HARQ- and CSI feedback in 6G	Ericsson	discussion	Rel-20	FS_6G_Radio
R2-2508629	6G Scheduling and (re-)transmission	Ofinno	discussion	Rel-20
R2-2508643	L2 scheduling framework for 6GR	InterDigital	discussion	Rel-20	FS_6G_Radio
R2-2508650	Discussion on UL Scheduling in 6G	Tejas Network Limited	discussion
R2-2508670	Discussion on UL scheduling improvements	NEC	discussion	Rel-20	FS_6G_Radio
R2-2508798	On scheduling and retransmission for 6G	NTT DOCOMO INC.	discussion	Rel-20	FS_6G_Radio
R2-2508904	Discussion on Re-transmissions for 6G RAN	TCL	discussion	Rel-20	FS_6G_Radio
R2-2508989	Discussion on retransmission and uplink scheduling	ETRI	discussion	Rel-20
R2-2509028	Retransmission enhancements for 6GR	CEWiT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.1.3-p020`

