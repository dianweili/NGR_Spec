# 6GR 移动性

**当前进展** · 阶段：收敛中

6GR 移动性已形成以 NR cell reselection 为基线、面向各类切换方案建立统一框架的方向，并明确无预配置移动性为 TN 基线，同时研究可选的候选配置与快速 RRC 处理。RAN2 已推进统一测量框架、按切换场景定义处理时延、缩减切换命令、早期上下行同步及资源共享或动态分配等工作，但多项方案仍在研究或等待 RAN1、RAN4、RAN3 和 SA2 协调。NTN 方面已纳入 TN–NTN 与 NTN–NTN 移动性、多轨道、位置或时间触发及 GNSS-free 操作等研究，并将低中断、低信令开销和减少 GNSS 依赖列为目标。整体方向已有若干基线和研究共识，但方案取舍、适用条件和具体程序尚未定稿。

**未决问题**

- 统一移动性框架如何整合 L3 HO、CHO、LTM 及网络触发和 UE 触发流程，仍有信令与程序设计分歧。
- 统一测量框架的具体范围、报告机制及 L1/L3、cell/beam 测量支持细节仍待推进。
- 候选配置、条件移动性及后续移动性的资源预留效率和具体支持方式仍未解决。
- 早期上下行同步、早期下行同步及早期 CSI 的可行性、触发方式和复杂度或功耗权衡仍待研究。
- 切换命令处理、目标配置应用、数据转发和 path switch 对整体时延的影响，以及不同切换场景的时延要求仍待协调。
- NTN 的多轨道与 TN–NTN 移动性、GNSS-free 操作及不同网络集成模式下的具体机制仍待研究。

## 6GR 演进

### [6G/Rel-20 RAN2#134] `agreement` 9.4 Mobility

除 CFRA baseline 外，RAN2 研究 UE 使用预配置 preamble 的 CBRA-based early UL synchronization 的可行性；支持 NW-triggered early UL synchronization，并进一步研究 UE-triggered 的潜在收益和可行性。NW-triggered baseline procedure 包括 source cell 向 UE 发命令、UE 向 target cell 发 RACH preamble、target cell 计算并传送 TA 给 source cell、source cell 将 TA 交付 UE，之后 UE 使用有效 TA 执行 RACH-less mobility；还考虑 network-triggered mobility 中 target cell initial access resources 在 cell switch command 前提供或随命令提供的两种情形。

```text
1	In addition to CFRA baseline for early UL synchronization in 6G mobility, RAN2 studies also the feasibility of UE using CBRA based early UL synchronization.  For CBRA-based the assumption is that the UE still is configured with a preamble to use for this purpose.
2	NW-triggered early UL synchronization is supported. Study further the potential benefits and feasibility of UE-triggered early UL synchronization
3	For NW-triggered early UL synchronization RAN2 considers the following steps to be a part of baseline procedure (FFS if any other enhancements are needed):
a.	Source cell initiates the procedure by transmitting a command to the UE
b.	UE transmits a RACH preamble to the indicated target cell
c.	Target cell is responsible to calculate the TA value and transmits it to the source cell
d.	Source cell is responsible to deliver the TA value to the UE
e.	With a valid TA value, UE performs a RACH-less mobility procedure
4	In mobility with pre-configuration, for network-triggered mobility, the resources for initial access to the target cell (e.g. CFRA, CG, SR): the following two cases are considered
-	Can be provided before cell switch command but be used upon cell switch command
-	Can be provided with cell switch command and be used.
Resource reservation issue of pre-configuration
R2-2603672	6GR mobility designs	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.4-a001`

### [6G/Rel-20 RAN2#134] `observation` 9.4 Mobility

UE 处理时间（Tprocessing，RAN4 定义）主要取决于 UE 收到 HO command 后需要执行的实际操作。它与 HO 期间变更的 IE/参数数量或 HO command 的大小没有直接相关性。

```text
The factor which contributes majorly to the UE processing time (i.e., Tprocessing defined by RAN4), depends on the actual actions UE need to take after receiving the HO command and is not directly correlated to the number of IEs/parameters that change during HO or the "size of the HO command”.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.4-o001`

### [6G/Rel-20 RAN2#134] `observation` 9.4 Mobility

RAN2 认可，在某些痛点场景中，legacy handover mechanisms 可能有较高概率发生非预期事件。例如，快速 RSRP 下降时 measurement event 未能正确触发。

```text
RAN2 recognize that legacy handover mechanisms might show high probability of unintended events (e.g., measurement event is not properly triggered when fast RSRP degradation) in some pain point scenario (e.g., some trajectory in urban grid scenario defined in TR 38.914).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.4-o002`

### [6G/Rel-20 RAN2#134] `observation` 9.4 Mobility

UL-based mobility measurement 可在网络侧执行：UE 向潜在目标小区发送上行信号（如 PRACH preamble/SRS），目标小区再基于这些信号进行测量。

```text
UL-based measurement for mobility can be performed at the network side where the UE transmits uplink signals (e.g., PRACH preamble/SRS) to the potential target cells, and then these target cells perform measurements based on the uplink signals.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.4-o003`

### [6G/Rel-20 RAN2#134] `observation` 9.4 Mobility

降低 interruption time 是 mobility 的 KPI 之一。因此，UL-based mobility 可与 candidate configurations、DL sync、UL signal transmission 和 RACH-less HO 等预配置技术集成。

```text
One of the KPIs of mobility is to reduce interruption time, therefore UL-based mobility can be integrated with pre-configured techniques such as candidate configurations, DL sync, UL signal transmission and RACH-less HO.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.4-o004`

### [6G/Rel-20 RAN2#134] `observation` 9.4 Mobility

UL-based mobility 可减少访问目标小区的资源消耗：只有接受 UE 的候选小区才指示资源分配（如 CG、CB-PUSCH）。它也可改善上行服务质量，例如 uplink-heavy interactive AI applications。

```text
Other advantages of UL-based mobility are: to minimize resource consumption for accessing the target cells as only the candidate cell that accepts the UE provides the indication of resource allocation (e.g., CG, CB-PUSCH), and to improve UL service quality such as uplink-heavy interactive AI applications.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.4-o005`

### [6G/Rel-20 RAN2#134] `proposal` 9.4 Mobility

应用目标小区参数时的关键时延包括：Physical layer configuration 的 RF retuning 和 BWP switching，MAC configuration 的 MAC reset，RLC configuration 的 RLC entity re-establishment，以及 PDCP configuration 的 PDCP entity re-establishment 和 security update。

```text
The key delays incurred by applying target cell parameters are as follows:
•	Physical layer configuration: delay incurred by RF retuning and BWP switching
•	MAC configuration: delay incurred by MAC reset
•	RLC configuration: delay incurred by RLC entity re-establishment
•	PDCP configuration: delay incurred by PDCP entity re-establishment and security update
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.4-p001`

### [6G/Rel-20 RAN2#134] `proposal` 9.4 Mobility

不同 handover 场景中持续变化的配置范围不同：Intra-DU/Intra-CU 涉及 physical layer configuration；Inter-DU/Intra-CU 涉及 physical layer、MAC 和 RLC configuration；Inter-CU 还涉及 PDCP configuration 和 security。条目还提出请 RAN4 研究两类场景是否可定义更低的 interruption requirements：无 RF 和 baseband change configuration update 的同频 mobility，以及基于 multi-carrier configuration 的异频 mobility。

```text
The always changing parameters in each handover scenario are as follows:
•	Intra-DU/Intra-CU: physical layer configuration: e.g., SSB frequency, PCI, SCS, carrier bandwidth, BWP configuration, TDD configuration, etc.
•	Inter-DU/Intra-CU: physical layer configuration, MAC configuration, RLC configuration
•	Inter-CU: physical layer configuration, MAC configuration, RLC configuration, PDCP configuration, security
Noted
R2-2603645	Considerations on 6G Mobility	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
Proposal 1 Ask RAN4 to study the feasibility of defining separate and lower interruption requirements (e.g. TRRC-processing and Tprocessing) for the following scenarios (consider the draft LS in Annex as a baseline):
Scenario 1: Intra-frequency mobility without RF and baseband change configuration update:
Most likely changed parameters include: PCI, C-RNTI, PUCCH resource config, SR resource, SRS resource, PRACH root sequence index.
May changed parameters include: CSI-Meas config, RRM measurement config.
Note: no change on other parameters that are not listed above.
Scenario 2: Inter-frequency mobility based on multi-carrier configuration (e.g. PCell and SCell role change).
Noted
R2-2603084	Views on Mobility for 6G	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.4-p002`

### [6G/Rel-20 RAN2#134] `proposal` 9.4 Mobility

RAN2 应由 RAN4 为不同 HO 场景定义适当的 UE processing time（Tprocessing）要求，不应按 HO 期间配置变更的多少区分要求。会议同意向 RAN4 发 LS，说明已识别的无 RF 和 baseband configuration change 的同频 mobility 场景，并询问该场景是否可降低 UE processing delay。

```text
RAN2 should leave it upto RAN4 to define appropriate UE processing time (Tprocessing) requirements for different HO scenarios and not request to define different requirements based on “how much” the configuration changes during a HO.
Noted
Discussion
-	Qualcomm thinks that there are other things that we can do something related with HO timeline.   ZTE thinks that even if we have the QC solution RAN4 still has to define a maximum value.
-	Ericsson, Interdigital and Xioami think that ZTE’s proposal makes sense and we should provide the scenario with and without RF re-tuning.
-	Vivo explains that RAN4 is discussing how to shorten the processing time.   ZTE explains that RAN4 will discuss how to minimize the Tprocessing but they will still consider the worst case scenario and will not discuss the RAN2 scenario.
-	Qualcomm thinks that if we send an LS to RAN4 we should explain the scenario where this happens.
-	Apple and Qualcomm don’t see the cases where this happens.  Apple suggest to ask RAN4 if there is a case where the mobility can happen without RF and baseband configuration change.
Send LS to RAN4 to indicate that RAN2 has identified a mobility scenario, intra-frequency mobility without RF and baseband configuration change.  Ask RAN4 if they agree that in this scenario there is no RF and baseband configuration and if it is possible to reduce the UE processing delay.   Explain that we’d just like an assessment if this direction is possible.
[AT134][014][6G Mobility] LS to RAN4 on processing delay (ZTE)
Intended outcome:  Agree to an LS to RAN4
Deadline:  Friday
R2-2604395	[DRAFT] LS on mobility interruption time	ZTE Corporation	LS out	Rel-20	FS_6G_Radio	To:RAN4
The LS is approved in R2-2604406
R2-2603312	Key considerations for mobility in 6G	Ofinno	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.4-p003`

### [6G/Rel-20 RAN2#134] `proposal` 9.4 Mobility

RAN2 将研究一种 small-size HO command 方案，该命令仅包含源小区与目标小区之间发生变化的参数。该方案主要适用于 RF/BB-impacting parameters 不变的场景。

```text
RAN2 to study an option for a small-size HO command that includes only the parameters that change between source and target cells. This option is primarily applicable in scenarios where the RF/BB-impacting parameters do not change.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.4-p004`

### [6G/Rel-20 RAN2#134] `proposal` 9.4 Mobility

RAN2 将向 RAN4 发送 LS，询问对于 RF/BB-impacting parameters 不变的 HO 场景，能否定义更低的 RRC procedure delay（T_RRC）和 UE processing time（T_processing）要求。

```text
RAN2 to send an LS to RAN4 asking whether reduced RRC procedure delay (T_RRC) and UE processing time (T_processing) requirements can be defined for HO scenarios where no RF/BB-impacting parameters change.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.4-p005`

### [6G/Rel-20 RAN2#134] `proposal` 9.4 Mobility

RAN2 将研究减少 HO command 处理时间和数据中断的机制，包括 RF/BB 参数不变时使用 small-size HO command、在 target configuration 应用前继续与 source cell 通信，以及结合使用 pre-configuration 和 fast RRC processing。该议题先在线下会议讨论。

```text
RAN2 to study mechanisms to reduce HO command processing time and data interruption, including: a) small-size HO command for scenarios where RF/BB parameters do not change (per Proposal 1); b) continued source cell communication until a time at which the target configuration is applied, distinct from NR DAPS; and c) combined use of pre-configuration with fast RRC processing.
To be discussed first face to face offline
R2-2604208	Report from [AT134][008] Early UL Synchronization and Resource Reservation for 6G Mobility (Nokia)	Nokia	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.4-p006`

### [6G/Rel-20 RAN2#134] `proposal` 9.4 Mobility

支持 NW-triggered early UL synchronization；进一步研究 UE-triggered early UL synchronization 和 UE-based TA acquisition 的潜在收益与可行性。

```text
NW-triggered early UL synchronization is supported. Study further the potential benefits and feasibility of UE-triggered early UL synchronization and UE-based TA acquisition.
-	Ericsson, ZTE and Nokia points out the UE-based TA acquisition is purely a RAN4.  Vivo thinks that we studied in RAN2 but many think that RAN4.
Noted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.4-p007`

### [6G/Rel-20 RAN2#134] `proposal` 9.4 Mobility

在采用 pre-configuration 的 mobility 中，source cell 可在 cell switch command 中指示 initial access 资源，例如 CFRA、CG 或用于 RACH-less 的 SR，前提是已与 target cell 协调。协调可在 cell switch 前进行，也可更早进行，由 source cell 决定。

```text
For mobility with pre-configuration:
the source cell can indicate the resources for initial access (e.g., CFRA, CG or SR for RACH-less) in the cell switch command (i.e., when triggering the switching), after coordination with the target cell.
It is up to the source cell whether to perform such coordination just before the cell switch or earlier (e.g., depending on inter-node delay).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.4-p008`

### [6G/Rel-20 RAN2#134] `proposal` 9.4 Mobility

在采用 pre-configuration 的 mobility 中，source cell 与 target cell 协调 initial access 资源时，target cell 可为 UE 提供新配置，而不使用预存配置；source cell 可触发 normal L3 handover。

```text
For mobility with pre-configuration, when the source cell coordinates with the target cell for resources for initial access, the target cell can provide a new configuration for the UE (i.e., not using the pre-stored configuration) and the source cell can trigger a normal L3 handover.
R2-2603142	Discussion on 6G Mobility	OPPO	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.4-p009`

### [6G/Rel-20 RAN2#134] `proposal` 9.4 Mobility

为提高 6G mobility 的 resource reservation efficiency，可使用 shared resource pool 避免为 UE 预留专用资源，例如 contention based PUSCH transmission 或 shared CFRA/SR resource pool。

```text
To improve the resource reservation efficiency for 6G mobility, shared resource pool can be used to avoid UE dedicated resource reservation, e.g., contention based PUSCH transmission, shared CFRA/SR resource pool.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.4-p010`

### [6G/Rel-20 RAN2#134] `proposal` 9.4 Mobility

为提高 6G mobility 的 resource reservation efficiency，采用 dynamic resource allocation/activation 以避免长期资源预留；例如基于 NW coordination 或 UE assistance info 分配/激活 CG、CFRA 或 SR 资源。该议题先在线下会议讨论。

```text
To improve the resource reservation efficiency for 6G mobility, dynamic resource allocation/activation is used to avoid long term resource reservation, e.g., NW coordination-based CG/CFRA/SR resource allocation/activation, or UE assistance info-based CG/CFRA/SR resource allocation/activation.
To be discussed first face to face offline
Early UL sync
R2-2604175	Solutions for mobility shortcomings	Ericsson, T-Mobile USA, Deutsche Telekom	discussion	Rel-20	FS_6G_Radio	R2-2603523
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.4-p011`

### [6G/Rel-20 RAN2#134] `proposal` 9.4 Mobility

6G Early UL synchronization 的基线为 network-controlled：网络向 UE 发送命令，UE 向指示的 target cell 发送 RACH preamble，target cell 计算 TA 并发送给 source cell，再由 source cell 将 TA 交付 UE。获得有效 TA 后，UE 执行 RACH-less mobility procedure。

```text
The Early UL synchronization procedure in 6G is network-controlled as baseline and comprises the following baseline steps (FFS on additional enhancements):
a.	Network initiates the procedure by transmitting a command to the UE
b.	UE transmits a RACH preamble to the indicated target cell
c.	Target cell is responsible to calculate the TA value and transmits it to the source cell
d.	Source cell is responsible to deliver the TA value to the UE
e.	With a valid TA value, UE performs a RACH-less mobility procedure
R2-2603984	Discussion on Mobility management for 6GR	HONOR	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.4-p012`

### [6G/Rel-20 RAN2#134] `proposal` 9.4 Mobility

RAN2 将同时考虑 NW-triggered 和 UE-triggered early UL synchronization。

```text
RAN2 to consider both NW-triggered and UE-triggered early UL synchronization.
R2-2604072	Discussion on 6G mobility	NTT DOCOMO	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.4-p013`

### [6G/Rel-20 RAN2#134] `proposal` 9.4 Mobility

对于 early UL sync，RAN2 将研究使用 CFRA resource 和 CBRA resource。

```text
For early UL sync, RAN2 to study not only using CFRA resource but also CBRA resource.
R2-2603086	Considerations on 6G mobility	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.4-p014`

### [6G/Rel-20 RAN2#134] `proposal` 9.4 Mobility

Early UL synchronization 将研究两种方向：对 RA-based early UL sync，通过优化 early measurement reporting 的 event configurations（例如 MR 的 event thresholds）减少不必要的同步；对 UE-based TA measurement，研究将其扩展到 asynchronous network 场景，包括向 UE 提供 source/target cell 的 reference timing difference 或可用于计算 target cell propagation delay 的 assistance information。另有提案考虑 UE 在 RRC_CONNECTED 且无数据期间基于预配置自行切换小区、不报告测量结果或通知网络，并在离开预配置 cell-list 时通知网络；该提案被 noted。

```text
Study the following approaches for early UL synchronization:
For RA-based early UL sync: Focus on minimizing the frequency of unnecessary early UL sync by optimizing the event configurations for early measurement reporting (e.g., defining appropriate event thresholds for a MR).
For UE-based TA measurement: Expand the applicability of UE-based TA estimation to asynchronous network scenarios. Specifically, study mechanisms to provide the UE with:
the reference timing difference between the source and target cells; or
Assistance information enabling the UE to calculate the propagation delay to the target cell.
UE power saving considerations
R2-2604139	Discussion on UE-based mobility for UE power saving	Turkcell, China Unicom, OPPO, Huawei, HiSilicon, Kyocera, NEC, Ofinno, Sony,  CEWIT, BYD, Wistron	discussion	Rel-20	FS_6G_Radio
Proposal 1	For mobility in the RRC_CONNECTED state, the following UE-based mobility behaviours can be considered for UE power saving:
Within the pre-configured cell-list: during the no-data period, the UE does NOT report measurement results, performs conditional cell switching itself per configuration, and does NOT notify the network for cell switching; Upon data arrival, the pre-configured identification(s) for each cell are used to identify the UE.
Upon the UE moving outside the pre-configured cell-list, the UE notifies the network with the necessary identification(s).
Noted
R2-2604175	Solutions for mobility shortcomings	Ericsson, T-Mobile USA, Deutsche Telekom	discussion	Rel-20	FS_6G_Radio	R2-2603523
Observation 6	Relying only on conditional mobility solutions for energy efficient operation in RRC Connected mode would result in wastage of a large amount of conditional resources assigned to the UE. Such a solution would not be scalable.
Observation 7	The UE still needs to perform RA in the new cell to obtain timing advance.
Observation 8	Transmitting a measurement report before the mobility execution would not introduce a significant cost in terms of the UE energy consumption.
Proposal 7	There is no special mobility handling needed for performing mobility while the UE is in energy efficient operation of RRC Connected mode i.e., the UE transmits measurement reports as per the measurement configuration associated to the mobility in the RRC Connected mode and performs the mobility procedures.
Noted
Discussion
-	Ericson is concerned that if the UE doesn’t report when it changes the NW doesn’t know where the UE is and we have to reserve resources and we would have to do sub-sequent mobility and that was agreed that it was complex.  Huawei explains that the UE will not apply the configuration until it has data and if does apply it, it will notify the network.  So there is no need for subsequent mobility as the UE is not applying the configuration as it is moving.
-	Ericsson thinks that one way to save power is to have some form measurement relaxation.
-	Vivo and Offino thinks that it would be good to save power for the UE and we should study.
-	Oppo thinks that we should analyze the benefits and the complexity.   Oppo explains that the UE will stay in RRC connected and that is power consuming and it also helps the system as a whole.  For complexity part, we should look at restrictions on how to reduce the complexity, like for example limit for intra.
-	Lenovo agrees with Ericsson and also it is not clear what UE ID would be used.
-	Samsung thinks that the network is responsible for the UE in connected mode and has to reserve resource including resources for reaching the UE in the other cells, so it is not good from network.
-	ZTE also agree with Ericsson.   It is difficult to know when to release the resources.   We should split the discussion into separate features, RRM and PDCCH monitoring.   We can look at RRM relaxation and also consider new triggers related to data activity.
-	CATT also agrees with Ericsson and ZTE.  Wonders if there is a target scenario and the UE has to apply the RACH procedure and that will cause delay.   Huawei thinks that to remove the delay you need to reserve.
-	Mediatek thinks that there may be some gains so we can study but it should be something simple.  How does the UE determine when to be in this mode.    Huawei explains that this would controlled by the network.
-	Apple thinks that a UE in connected mode should follow the same procedures as connected mode, from UE perspective don’t want to support different procedures.   Apple asks how the UE gets the measuremetns.  Huawei explains that the UE performs the measurements like in idle mode.
-	Sony thinks that this is beneficial if the UE knows when it will trigger UL data and you have longer periodicity.
-	Interdigital thinks that there may be some scenario like intra-CU/DU but we don’t know yet if we have HLS, so we can focus on measurement relaxation.
-	Nokia is concerned with the complexity we are adding in RRC connected as we are trying to replicate the mobility/functionality we have in idle mode.   The RNA configuration now it’s like in a pre-configuration form.
-	Rakuten thinks this is not efficient from resource reservation perspective and the network does’nt know when the UE left.
-	ZTE thinks that even for DL you still need to find the UE and you will send WUS, so it’s similar to paging.
R2-2603870	Discussion on 6G mobility	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.4-p015`

### [6G/Rel-20 RAN2#134] `proposal` 9.4 Mobility

为降低 RRC connected mode 下 delay-sensitive、bursty traffic 的功耗，研究两项彼此独立且不捆绑的功能：基于 DL/UL (LP)WUS 的 wake-up mechanism，以及以 CLTM/CHO-like pre-configuration 为基线的 UE-based mobility，并进一步研究 measurement relaxation 和 measurement reporting reduction。

```text
For further power saving in RRC connected mode for delay-sensitive and bursty traffic, the energy-saving gains are provided by two independent functionalities, which are studied separately and are not bundled:
•	DL/UL (LP)WUS based wake-up mechanism;
•	UE-based mobility, taking CLTM/CHO-like pre-configuration as baseline, with further study on measurement relaxation and reduction of measurement reporting.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.4-p016`

### [6G/Rel-20 RAN2#134] `proposal` 9.4 Mobility

UE 应在每次 cell switch 后通知 network，以便 network 维护 UE 的 cell-level location。这样可避免在所有 candidate cells 预留 UE-dedicated resources，以及向所有 candidate cells 发送 UE-dedicated WUS 所带来的 signaling overhead。

```text
The UE should notify the network after each cell switch, so that the network maintains cell-level location of the UE. This avoids:
The capacity impact of reserving UE-dedicated resources across the full set of candidate cells; and
The signalling overhead of transmitting UE-dedicated WUS across the full set of candidate cells.
R2-2603086	Considerations on 6G mobility	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.4-p017`

### [6G/Rel-20 RAN2#134] `proposal` 9.4 Mobility

针对 delay-sensitive、bursty traffic，UE 应在每次 cell change 后通知 network，以维护有效的 TA 和 beam，并确保 UE context 已准备好，从而快速恢复 data transmission。

```text
For delay-sensitive and bursty traffic, UE should notify the network upon every cell change to maintain a valid TA and beam, and to ensure UE context readiness for fast data transmission resumption.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.4-p018`

### [6G/Rel-20 RAN2#134] `proposal` 9.4 Mobility

针对 RRC connected state 下与 mobility 和 connection management 相关的 UE power saving，重点研究降低 5G measurement 和 reporting overhead 的增强方案，包括 S-measure、dynamic measurement and report configuration Act/Deact、RLM/BFD relaxation，以及目前仅允许 RedCap 使用的 RRM relaxation。

```text
For UE power saving related to mobility and connection management in RRC connected state, focus on studying enhancements of 5G measurement and reporting overhead reduction schemes e.g., S-measure, dynamic measurement and report configuration Act/Deact (being introduced in Rel-20 for LTM), RLM/BFD relaxation, and RRM relaxation currently allowed only for RedCap.
Early DL sync
R2-2603645	Considerations on 6G Mobility	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.4-p019`

### [6G/Rel-20 RAN2#134] `proposal` 9.4 Mobility

支持 network-triggered early DL sync，并以 5G 中由 source cell 触发 candidate cell 的 TCI-state activation 机制为基线；进一步研究 UE-triggered early DL sync 的可行性。对于无 pre-configuration 的 mobility，支持仅预配置 DL RS 和 candidate cell(s) 的 TCI-state configuration，以触发 early DL sync。

```text
Support network-triggered early DL sync in 6G, the 5G mechanism (i.e. source cell triggers TCI-state activation of candidate cell) is taken as a baseline, and
To further study the feasibility of UE-triggered early DL sync.
In case of mobility without pre-configuration, support pre-configuration of only DL RS, TCI-state configuration of candidate cell(s) for triggering early DL sync.
R2-2602970	Discussion on 6G mobility	Xiaomi	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.4-p020`

### [6G/Rel-20 RAN2#134] `proposal` 9.4 Mobility

Early DL sync（TCI state activation）有益且可以支持；其可行性由 RAN1 负责。RAN2 角度关于简化方案的进一步讨论，可在 RAN1 取得更多进展后进行。

```text
Early DL sync (TCI state activation) is beneficial and can be supported. Feasibility is up to RAN1 and any further discussions on simplifications from RAN2 perspective can be discussed after further RAN1 progress.
Others
R2-2602960	Discussion on 6GR Mobility enhancement for pain point scenarios	vivo, NTT DOCOMO, Ericsson, MediaTek Inc., ZTE Corporation, Huawei, HiSilicon, China Telecom, China Unicom, CMCC, Verizon, Qualcomm Incorporated, Apple, Nokia, CATT, CAICT, Lenovo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.4-p021`

### [6G/Rel-20 RAN2#134] `proposal` 9.4 Mobility

RAN2 将研究 mobility enhancements，以解决真实网络部署特定“pain point”场景中已知的 mobility issues，例如 ping-pongs、unnecessary HOs 和 RLFs；场景示例包括 TR 38.914 定义的 urban grid scenario。

```text
RAN2 to study mobility enhancements to address mobility issues (e.g., ping-pongs, unnecessary HOs, RLFs) known from specific “pain point” areas in real network deployments, such as urban grid scenario as defined in TR 38.914.
R2-2603042	Consideration of Uplink-based Mobility for 6GR	Sony, KDDI, Turkcell, Charter Communications, Fraunhofer-IIS, Fraunhofer HHI	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.4-p022`

### [6G/Rel-20 RAN2#134] `proposal` 9.4 Mobility

RAN2 应研究 connected mode UE 的 UL-based mobility，以减少 UE 执行 DL measurements 和 reporting 的负担及功耗，并降低访问 target cells 的资源消耗：仅接受 UE 的 candidate cell 提供资源分配指示，例如 CG、CB-PUSCH。该研究还旨在改善 uplink-heavy interactive AI applications 等场景的 UL service quality。

```text
RAN2 should study UL-based mobility for connected mode UEs to
minimize the burden on the UE for performing DL measurements and reporting (i.e., reducing power consumption),
minimize resource consumption for accessing the target cells as only the candidate cell that accepts the UE provides the indication of resource allocation (e.g., CG, CB-PUSCH), and
improve UL service quality such as uplink-heavy interactive AI applications.
R2-2602959	Discussion on 6GR Mobility	vivo	discussion	Rel-20
R2-2603003	Evaluation and Impact Analysis on UE-based-Mobility	OPPO	discussion	Rel-20	FS_6G_Radio
R2-2603180	Discussion on 6GR Mobility	1Finity	discussion	Rel-20	FS_6G_Radio
R2-2603235	Discussion on Idle Mode Mobility	Google Korea LLC	discussion
R2-2603256	Considerations for Mobility in 6GR	Charter Communications, Inc	discussion
R2-2603289	Reducing data interruption for 6G mobility	Qualcomm Incorporated, MediaTek Inc., Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2603292	6G Mobility	Nokia	discussion	Rel-20	FS_6G_Radio
R2-2603336	Discussion on mobility in 6GR	China Telecom	discussion	Rel-20	FS_6G_Radio
R2-2603347	On mobility control for pre-configured NTN mobility in 6GR	Wistron Corporation	discussion
R2-2603390	Discussion on Mobility in 6G systems	Tejas Networks Limited	discussion	Rel-20	FS_6G_Radio
R2-2603471	Discussion on 6G mobility	NEC	discussion	Rel-20	FS_6G_Radio
R2-2603506	Discussion on 6GR Mobility	Sharp	discussion	Rel-20	FS_6G_Radio
R2-2603528	Discussion on mobility configuration	ITRI	discussion	FS_6G_Radio
R2-2603571	Discussion on 6G Mobility	Lenovo	discussion	Rel-20
R2-2603627	6GR mobility aspects: issues and solutions	Sony	discussion	Rel-20	FS_6G_Radio
R2-2603660	Discussion on UE-based mobility in sub-state	NEC	discussion	Rel-20	FS_6G_Radio
R2-2603669	Discussion on 6G Mobility	InterDigital, Inc.	discussion	Rel-20	FS_6G_Radio
R2-2603697	UE based mobility for power saving in 6G connected mode	Panasonic	discussion	Rel-20
R2-2603709	UE power saving mobility in connected mode	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
R2-2603734	Views on 6G mobility	Apple	discussion	Rel-20	FS_6G_Radio
R2-2603740	On 6GR Mobility	Fraunhofer HHI, Fraunhofer IIS	discussion
R2-2603750	Resource Reservation Enhancements for 6G Mobility	Jio Platforms	discussion	Rel-20	FS_6G_Radio
R2-2603758	Considerations on pre-configured mobility in 6G	AT&T	discussion	FS_6G_Radio
R2-2603793	Discussions on 6G Mobility	Futurewei	discussion	Rel-20	FS_6G_Radio
R2-2603850	Discussion on 6G mobility	ETRI	discussion	Rel-20
R2-2603895	Consideration on mobility for 6GR	Spreadtrum, UNISOC	discussion	Rel-20
R2-2603918	Discussion on essential issues for 6G mobility 	Kyocera 	discussion	Rel-20
R2-2603942	Resource reservation in 6G mobility	TCL	discussion	Rel-20	FS_6G_Radio
R2-2603943	Discussion on measurement gap framework for 6G	TCL	discussion	Rel-20	FS_6G_Radio
R2-2603945	Study on 6G Mobility Framework	Samsung	discussion	Rel-20
R2-2603995	Mobility for 6GR	MediaTek Inc.	discussion	R2-2602521
R2-2604026	Resource reservation for pre-configuration based mobility	Rakuten Symphony	discussion	Rel-20
R2-2604027	Discussion on 6G mobility framework	Rakuten Symphony	discussion	Rel-20
R2-2604083	Discussion on 6G Mobility	CEWiT	discussion	Rel-20	FS_6G_Radio
R2-2604098	Discussion on Mobility for 6GR	KDDI Corporation	discussion
R2-2604099	Assumptions on the 6G Mobility Framework	1Finity, Huawei, HiSilicon, Xiaomi	discussion	Rel-20
R2-2604133	Discussion on mobility in 6G	Transsion Holdings	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.4-p023`

### [6G/Rel-20 RAN2#133bis] `agreement` 9.4 Mobility

6G 可支持 candidate RRC configuration 的预配置，具体细节及如何解决资源效率问题仍待研究。若已向 UE 预配置 candidate RRC configuration，6G mobility procedure 应支持 fast RRC processing；该功能为可选，并非所有 UE 都需要支持。

```text
Pre-configuration of candidate RRC configuration can be supported in 6G.   FFS details and how to address the resource efficiency identified issue.
The concept of fast RRC processing should be supported in 6G mobility procedure if candidate RRC configuration is pre-configured to the UE.   Assumption is that the feature is optional (not all UEs need to support).
R2-2601531	Views on Mobility for 6G	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-a001`

### [6G/Rel-20 RAN2#133bis] `agreement` 9.4 Mobility

研究基于位置和定时器的测量报告/触发及 UE 触发移动性条件，并考虑连接态与空闲/非激活态移动性。研究至少考虑 6G TN–5G NTN 的 inter-RAT 移动性，并研究 NTN 小区中的 TN 测量跳过/放宽、多轨道移动性和 GNSS-free/GNSS-less 操作对 NTN 设计的 RAN2 影响。

```text
1	Study location-based conditions (at least for cases where UE have location information) and timer based conditions for measurement report/triggers and UE triggered mobility (e.g., cell switch and cell reselection) (with or without radio conditions).  Study can consider aspects of both connected and idle/inactive mode mobility.
2	Study should consider at least inter-RAT 6G TN – 5G NTN mobility support.   Companies are encouraged to only bring contributions if something specific for NTN would need to be considered when we discuss overall 6G inter-RAT framework.
3	TN measurement skipping/relaxation in an NTN cell is beneficial.
4	At least the solution that 6G should be able to provide some form of TN coverage related information in the NTN cell as well as to provide NTN assistance information in TN e.g. ephemeris in TN cell is considered.     Further discussion on how to better provide coverage related information can be discussed in WI phase.
5	For multi-orbit mobility,  study aspects related to cell selection/reselection and understand what and if anything additional needs to be introduced for NTN.  An understanding of the problems that needs to be addressed should also be provided next meeting.
6	Study the RAN2 impacts of GNSS-free/GNSS-less operation on overall NTN design (e.g. mobility, measurements, UP impacts, etc).   Aspects still depending on RAN1 progess (e.g. initial access, pre-compensation, etc) will not be discussed next meeting.  Companies should provide an understanding of whether UE location information is available.
NTN: GNSS-Degraded/Free operation
R2-2602615	Discussion on prioritizing GNSS-free NTN operation for 6G	THALES, Ericsson, Novamint, ESA, Airbus, Sateliot, Eutelsat, TNO, ST Engineering iDirect, Viasat, Iridium, DSIT	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-a002`

### [6G/Rel-20 RAN2#133bis] `observation` 9.4 Mobility

即使大幅缩短空口切换中断时间，整体数据转发时延仍会影响 L2 数据传输。

```text
Even if the handover interruption time over air interface can be reduced greatly, the L2 data transmission will still be affected by the overall data forwarding latency.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-o001`

### [6G/Rel-20 RAN2#133bis] `observation` 9.4 Mobility

Path switch 仍是端到端 UP DL 新数据传输时延中不可忽略的组成部分。当前流程设计基于基本的 L3 handover 机制。

```text
The path switch remains a non-negligible component for the end-to-end UP DL new data transmission latency, and the current procedure design is based on the fundamental L3 handover mechanism.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-o002`

### [6G/Rel-20 RAN2#133bis] `observation` 9.4 Mobility

UE 应用目标小区配置的时间是空口时延的关键方面。5G LTM 支持快速 UE 处理，但仅适用于预配置 HO CMD 的场景，且 UE 收到 HO execution indication 后才应用完整配置，因此无法将该时间缩短至 0 ms。

```text
The time for UE applying the target cell configuration is a crucial aspect of air interface latency. 5G LTM supports fast UE processing, but it only applies to the scenarios where HO CMD is pre-configured and it cannot be reduced to 0ms because the UE only applies the full set of configuration after receiving HO execution indication.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-o003`

### [6G/Rel-20 RAN2#133bis] `observation` 9.4 Mobility

通过 advanced delta configuration 缩减 HO command 大小的工作已在“RRC Structure and (re)configuration”议题中进行。RAN2 应避免在 mobility 议题下重复讨论，并等待该议题的结果。

```text
Since HO command size reduction via advanced delta configuration is already being addressed in the "RRC Structure and (re)configuration" agenda item, RAN2 should avoid duplicating the discussion under the mobility agenda item and instead wait for its outcome.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-o004`

### [6G/Rel-20 RAN2#133bis] `observation` 9.4 Mobility

若 gNB 未有选择性或智能地进行 early CSI configuration，UE 可能需要测量多个“不必要”的候选小区/波束的 CSI-RS。这样会增加 UE 处理能力和测量模块的负担。

```text
If early CSI configuration is not selectively/intelligently done by the gNB, UE might need to measure the CSI-RS of several “unnecessary” candidate cells/beams, adding burden to UE’s processing capability and measurement modules.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-o005`

### [6G/Rel-20 RAN2#133bis] `observation` 9.4 Mobility

TN-NTN 网络集成的商业部署模式可能不同，联合部署可为 inter-PLMN 或 intra PLMN，也可能由同一或不同运营商提供。这会直接影响 handover latency 等移动性性能指标，进而影响最终用户体验。

```text
The commercial rollout model of TN-NTN network integration may vary. The resulting TN – NTN joint deployment of inter-PLMN or intra PLMN, could be of the same operator or different operator. This will directly impact on the mobility performance metrics, such as handover latency, and subsequently define the quality of the end-user experience.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-o006`

### [6G/Rel-20 RAN2#133bis] `observation` 9.4 Mobility

5G NTN 与 5G TN 商业部署进度可能分化，使 5G NTN 部署在首个 6G TN 商用网络可用时达到峰值。在这种情况下，稳定的 6G TN–5G NTN 移动性支持标准规范比 6G TN–6G NTN 移动性支持更重要。

```text
Diverge trajectory of 5G NTN and 5G TN commercial roll-out will potentially create a situation where 5G NTN commercial rollout is at its peak when the first 6G TN commercial network is available. In this case stable standard specification for 6G TN – 5G NTN mobility support is more important compared to 6G TN – 6G NTN mobility support.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-o007`

### [6G/Rel-20 RAN2#133bis] `observation` 9.4 Mobility

TN-to-NTN 移动性挑战包括：使用准确的卫星辅助信息和适当的预补偿测量 NTN 小区，以及及时提供切换配置。

```text
TN-to-NTN mobility challenges include the need to measure NTN cells with accurate satellite assistance information and proper pre-compensation as well as timely handover configuration.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-o008`

### [6G/Rel-20 RAN2#133bis] `observation` 9.4 Mobility

NTN-to-TN 移动性挑战包括避免在特定区域进行不必要的测量，以及避免 pingpong。

```text
NTN-to-TN challenges include preventing unnecessary measurements in specific areas and pingpong avoidance.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-o009`

### [6G/Rel-20 RAN2#133bis] `observation` 9.4 Mobility

在 multi-orbit 场景中，UE 驻留于 GSO cells，并切换到不同 orbits 以满足不同 QoS requirements。该方式可帮助 UE 和 network 节能，UE 可避免频繁 cell reselection，network 可在无服务需求时关闭 NGSO beams。

```text
For multi-orbit scenario, UEs camp on GSO cells and switch to different orbits to perform service with different QoS requirements, which can facilitate energy saving for both UE and the network, as UEs can avoid frequent cell reselection and the network can switch off NGSO beams when there is no service requirement.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-o010`

### [6G/Rel-20 RAN2#133bis] `observation` 9.4 Mobility

仅依赖 UE-based switching approaches（例如 priority-based cell reselection mechanism）可能导致 access congestion 和 load imbalance。此类方式还可能使 network 无法按需调度 beams。

```text
Regarding switching mechanisms between orbits, relying solely on UE-based approaches (e.g., priority-based cell reselection mechanism) may result in access congestion and load imbalance, and make it impossible for the network to schedule beams on demand.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-o011`

### [6G/Rel-20 RAN2#133bis] `observation` 9.4 Mobility

Multi-orbit mobility 自 Release 17 起已支持于 5G NTN。

```text
Multi-orbit mobility has been supported for 5G NTN since Release 17.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-o012`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

记录了 6G mobility latency 的计时范围：从 UE 收到 cell switch command 开始，到 RACH-based mobility 发送 PRAMBLE 或 RACH-less mobility 发送首个 uplink data 为止，并列出 command 处理、ASN.1 解码、目标小区参数应用、时间跟踪、SSB 处理及首个 UL 资源获取不确定性等组成部分。讨论指出可使用更一般的 mobility 术语，且 6G 中各组成部分的功能、术语及并行处理方式可能不同；该议题已 Noted。

```text
The 6G mobility latency is counted from the time that UE receives cell switch command and ends at the time of UE starts to send PRAMBLE for RACH-based mobility or to send first uplink data for RACH-less mobility, including the following components:
-	The time to receive cell switch command and processing the command;
-	The time for ASN.1 decoding and validity/compliance check;
-	The time for UE processing, consisting of applying the target cell parameters and related change;
-	The time for fine time tracking and acquiring full timing information of the target cell;
-	The time for SSB processing;
-	The interruption uncertainty in acquiring the first UL transmission resource , which related to UE’s cell switch type, i.e., RACH-based or RACH-less cell switch.
-	Ericsson thinks this are find but we can have more general terms, like instead of cell switch command, mobility.
-	Qualcomm thinks that the components in 5G may not do the same things in 6G and it may not be the same terminology and doing some things in parallel.
Figure 1: Components of Mobility Latency for LTM
Figure 2: Mobility Latency for RACH-based LTM
Figure 3: Mobility Latency for RACH-less LTM
Noted
R2-2602514	Discussions on 6G Mobility	Futurewei	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p001`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

记录了 6GR overall mobility latency 各组成部分的负责工作组：TRRC、TRRC-target、TRAR 由 RAN2 负责；TCSC、TDL-sync、TRA、Tfirst-data 由 RAN2 和 RAN1 负责。该事项已 Noted。

```text
The responsible WGs for different components of overall mobility latency for 6GR are as follows:
TRRC : RAN2
TCSC : RAN2 and RAN1 (e.g., considering acknowledgement of CSC or the CSC is physical layer signaling)
TRRC-target : RAN2
TDL-sync :  RAN2 and RAN1
TRA : RAN2 and RAN1
TRAR  : RAN2
Tfirst-data  : RAN2 and RAN1
Noted
R2-2602002	Considerations on 6G Mobility	ZTE Corporation, Sanechips	discussion	Rel-20	NR_cov_Ph3
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p002`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

RAN2 将与 RAN3 和 SA2 协调，研究如何降低 mobility 期间由 data forwarding 和 path switch 引起的 end-to-end UP data transmission latency，例子包括有无 pre-configuration 的 mobility。该事项已 Noted。

```text
RAN2 coordinates with RAN3 and SA2 to study how to reduce the end-to-end UP data transmission latency during mobility caused by data forwarding and path switch, e.g. considering both mobility with pre-configuration and mobility without pre-configuration.
-	Ericsson thinks that we send an LS to RAN3 if we need some help but we can avoid topics that have heavy RAN3 impact.
Noted
HO command size/delta signalling:
R2-2602002	Considerations on 6G Mobility	ZTE Corporation, Sanechips	discussion	Rel-20	NR_cov_Ph3
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p003`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

提出定义一种 HO CMD，使 network 在 mobility 期间仅更改最少配置（例如 PCI、SR、SRS），并与 RAN4 协作制定较低的 TRRC-processing 和 TProcessing latency requirements；讨论目前主要针对 L3 HO。下次会议可提交始终变化的参数、适用场景及其延迟影响，以判断是否向 RAN4 询问未更改 RF parameters 时能否采用不同 requirements。

```text
Define the HO CMD which allows the network to change only a minimum set of configurations (e.g. PCI, SR, SRS) during mobility, collaborate with RAN4 to define lower latency requirements (i.e. TRRC-processing and TProcessing) for this scenario.
-	Oppo asks if this means that we limit the HO scenarios, meaning that this applicable only to some scenarios.   ZTE thinks that this includes two parts, separate requirement with lower delay and second RAN2 part on how to do it, e.g. separate message or discussed as modular design.  Open for both but difficult to do it with modular as that is not the main goal of modular RRC
-	Rakutens asks if this for L2 HO also.   Now mainly for L3 now.
-	Mediatek thinks that we first need to study if this is really possible.   ZTE thinks that we first need to study the minimum set needed.
-	Qualcomm thinks that even if we decided the minimum set the actual requirement would need to be defined by RAN4 and it is difficult to know what happens when we have just some IEs.  ZTE agrees and what matters is what parameter is included, for example if we are modifying frequency, BWP.   The ones we have identified don’t impact baseband and RF.
-	Apple thinks that RAN2 cannot discuss as it is a RAN4 domain.
-	CMCC thinks that 80% of reconfiguration within the same are is the same.  So there are opportunities to reduce the HO command.   UE and NW vendors have been gap in requirements in RAN4.
-	Ericsson doesn’t thinks that this a new HO command, but starting to identify the minimum set of parameters can be difficult, we can at least ask them if it is possible to have different requirements when we change the RF and when don’t RF parameters.   Huawei agrees with Ericsson.
-	Lenovo asks if this is a problem that is real in the field.   ZTE confirms it is real in the field.
-	Docomo thinks we can discuss for each scenario what type of parameters are different.
-	Rakuten agrees with this exercise and we have some early processing and others so we can do this exercise after.
-	CATT thinks that we should first determine if we have one minimum set or multiple minimum sets.
-	Ericsson strongly encourages that if companies point to parameters they should explain what type of delays the parameters.
For next meeting, can bring contributions on what parameters that are always changing, and scenarios,  and what type of delays those parameters bring.  Next meeting we can determine if we ask RAN4 if new requirements are possible in the case where no RF parameters are changed.
R2-2602243	Further Views on 6G TN and NTN Mobility	Nokia	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p004`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

RAN2 将研究降低 handover command size 的方法，包括带 immediate execution command 的 pre-configuration、postponed handover execution，以及 enhanced delta-configuration for mobility。该事项已 Noted。

```text
RAN2 to investigate approaches that may reduce the handover command size. The areas to study include pre-configuration with immediate execution command of smaller size, postponed handover execution or enhanced delta-configuration for mobility.
Noted
R2-2601965	Discussion on mobility enhancements for 6G	LG Electronics Inc.	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p005`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

HO command size reduction 中的 advanced delta configuration 将依赖 “RRC Structure and (re)configuration” 议程项的结果；其他方法（例如 CA-based handover）的必要性将在该结果可用后评估。

```text
Rely on the outcome of the "RRC Structure and (re)configuration" agenda item for HO command size reduction via advanced delta configuration, and evaluate the necessity of other methods (e.g., CA-based handover) only after the outcome is available.
Noted
Discussion
-	Samsung doesn’t think this significantly change the processing delay.  Xiaomi thinks that this related to the previous discussion.
fast/early RRC processing
R2-2602521	Mobility for 6GR	MediaTek Inc.	discussion	R2-2600645
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p006`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

如果向 UE 提供 candidate RRC configuration，6G mobility procedure 应支持 fast RRC processing。讨论意见认为该功能不应是 mandatory；该事项已 Noted。

```text
The concept of fast RRC processing should be supported in 6G mobility procedure if candidate RRC configuration is provided to the UE.
-	Qualcomm is fine but it shouldn’t be mandatory.  Mediatek also thinks that it shouldn’t be mandatory.
Noted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p007`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

研究减少中断时间时，RAN2同意由RAN4为不同HO场景定义合适的UE处理时间（Tprocessing）。RAN2应先研究HO command的内容及发送方式（例如RRC或MAC），再讨论“HO command processing”导致的中断。

```text
For the study on reducing interruption time, RAN2 agrees to the following principles:
a.	RAN2 should leave it upto RAN4 to define appropriate UE processing time (Tprocessing) requirements for different HO scenarios.
b.	RAN2 should study the contents of the HO command and how the HO command is sent (e.g., via RRC or MAC) before discussing interruption due to “HO command processing”
Noted
early UL sync/RACH-less HO:
R2-2602600	Discussion on 6G Mobility	Turkcell, Deutsche Telekom, Ericsson, NTT Docomo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p008`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

RAN2应建立涵盖所有部署类型的6G mobility framework，纳入early UL synchronization，以实现无缝、低时延移动性且不增加cell overhead。

```text
RAN2 should establish a 6G mobility framework that encompasses early UL synchronization across all deployment types to ensure seamless, low-latency mobility without increasing cell overhead
Noted
R2-2601984	Discussion on mobility in 6GR	China Telecom	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p009`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

对于6G HO的early UL synchronization，可在RAN2研究network triggered early TA acquisition和UE-based TA measurement。已同意研究支持连接态移动性的early UL/DL synchronization，适用于有或没有candidate cell预配置的情形，也适用于spectrum aggregation scenarios。

```text
Regarding early UL synchronization for HO in 6G, both network triggered early TA acquisition and UE-based TA measurement could be studied in RAN2.
-	Ericsson thinks that this UE-based TA measurement was not useful for 5G and this is mainly RAN4 work.
Noted
Discussion
-	Ericsson points out that the intention
-	Apple thinks that this is very critical that it is not mandatory as we have different device types.   Companies think that it can be optional but UE capabilities will be discussed in the future and it also depends on the solution.
-	LG assumes that this agreements includes carrier aggregation.  Confirmed
Agreements on early UL/DL synchronization
Study support early UL/DL synchronization for 6G connected mode mobility for both with and without pre-configuration of candidate cells.   This is applicable to spectrum aggregation scenarios.   FFS how to address some of short comings
Early CSI acquisition
R2-2602600	Discussion on 6G Mobility	Turkcell, Deutsche Telekom, Ericsson, NTT Docomo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p010`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

RAN2应研究缓解移动性期间throughput degradation的方法，利用Release 19的early CSI acquisition并探索6G新进展，同时不增加UE complexity。

```text
RAN2 should research methods to mitigate throughput degradation during mobility, leveraging early CSI acquisition in Release 19 and exploring new 6G advancements without increasing UE complexity.
-	Ericsson points out that we can try to find a way to make it simpler for the UE.
Noted
R2-2602134	Discussion on 6G Mobility for TN and NTN	Lenovo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p011`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

可支持early TCI state和early CSI acquisition，以避免移动性导致的throughput degradation。

```text
Both early TCI state and early CSI acquisition can be supported for avoiding throughput degradation due to mobility.
Noted
R2-2601531	Views on Mobility for 6G	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p012`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

RAN2同意early CSI acquisition有益且可支持，其可行性由RAN1负责。RAN2可在RAN1进一步推进后讨论简化方案，并将该共识告知RAN1、请其研究。

```text
To address the 5G shortcomings of early CSI on “UE measurement complexity” and “unnecessary early CSI acqusition”, RAN2 should study mechanisms to enable the UE to perform CSI acquistion on the most appropriate candidate cells, considering UE preference/assistance into account.
Noted
Discussion
-	Apple thinks that this should be a RAN1 topic anyways.   Qualcomm thinks that before we decide to support it we should study how to make it simpler by considering UE preference. ZTE thinks that we can support it but details can be discussed after we have a RAN1 design.
Agreements on early CSI acquisition
Early CSI acquisition is beneficial and can be supported.  Feasibility is up to RAN1 and any further discussions on simplifications from RAN2 perspective can be discussed after further RAN1 progress.
Inform RAN1 of this agreement and ask them to study it.  LS can be written in later meeting once we have some more agreements on mobility.
pre-configuration and resource reservation:
R2-2602200	Connected Mode Mobility for 6GR	InterDigital, Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p013`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

提出支持dynamic conditional mobility framework：预配置时不必为所有目标完整配置或预留资源，可先配置执行HO所需的关键部分，再在HO触发时、执行时或之后提供额外配置和资源。会议记录了将配置拆分为执行HO关键部分并延后提供资源的方向。

```text
Support dynamic conditional mobility framework that does not rely on complete configuration/resource reservation for/at all the targets on pre-configuration (e.g., activation of static/essential configuration/resources to access target on pre-configuration, and dynamic configuration/activation during/after CHO triggering).
-	Huawei asks why only for conditional.  Interdigital clarifies it can be for anything.
-	ZTE asks if the intention is that the additional configuration can be send after the UE switches.
-	Oppo asks what resources.  Interdigital explains that we should only provide the parameters that are needed to execute the handover and the rest you can provide.
-	Nokia likes in general this approach and not mention CHO.   The general approach to divide the configuration in some parts that are critical to execute HO and then provide resources later is a good direction.   Rakuten agrees
-	Xiaomi thinks that even today it is already feasible so asks what is new compared to existing way.   Samsung has similar understanding.
-	Ericsson thinks that the resource reservation problem is the grant and preamble and we should allow to provide the resources when the mobility triggering.
-	Huawei thinks that this wouldn’t address the problem of robustness for LTM.
Ways to allow the network to provide some information in the pre-configuration of candidate cells and then allow the network to provide additional configuration at time of HO execution or later?.
Ways to identify the configuration in some parts that are critical to execute HO and then provide resources later/at the time it is triggered
Noted
R2-2602168	6GR mobility aspects: issues and solutions	Sony	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p014`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

针对preconfigured mobility schemes的resource reservation问题，至少聚焦于导致预留问题的关键资源：HO执行及early RACH的CFRA resource、HO执行的Configured grant和SR resources。

```text
For the resource reservation issues of the Preconfigured mobility schemes, consider the following solutions:
1)	Dynamic indication of contention-free PUSCH (CF-PUSCH) within shared resource during HO execution (e.g., LTM).
2)	Contention-Based PUSCH (CB-PUSCH) within shared resource during HO execution (e.g., LTM, C-LTM).
3)	Indication and Activation of CG resource from the target cell (e.g., LTM).
Noted
Discussion
-	Docomo thinks that we need ensure that whatever we do doesn’t impact the latency of HO.
-	Huawei thinks that we need to take to into account NW complexity, as the network  handle the configuration of UEs on other cells and add complexity.
-	Samsung and Ericsson thinks that SRS resource can be provided after HO.  ZTE thinks that it should be considered as if it is provided after it triggers new configuration.   Ericsson thinks it is not essential.   When you preconfigure you don’t need to include SRS resource.
-	Huawei and Samsung don’t think this is a pain point.  ZTE thinks that if we have a clash we’d need to reconfigure and it depends on the value range.   Samsung and Ericsson didn’t see the clash.    Huawei thinks that it is up to network implementation to avoid it.
| Agreements on resource reservation issue 1 Focus at least on the following essential resources that cause resource reservation problems - CFRA resource for HO execution and for early RACH - Configured grant for HO execution - SR resources NOTE: after we design a solution other parameters can be considered if the same solution can be used. |
| --- |
R2-2602284	6GR mobility designs	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p015`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

对于candidate target cell中预存UE配置的移动性，采用与任何RRC reconfiguration相同的delta-signalling procedure，且不针对后续移动性进行优化。该项未处理。

```text
For mobility with pre-stored UE configuration in the candidate target cell, the same delta-signalling procedure like for any RRC reconfiguration is used, without any optimization for subsequent mobility.
Noted
Not treated
Addressing standalone mechanisms & duplicated Configs:
R2-2601458	Discussion on 6GR Mobility	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p016`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

RAN2考虑支持所有cell switch类型（L3 HO、CHO、LTM）使用预配置的candidate configuration进行cell switch。为处理不同cell switch间相似或重复的配置，将使用一份适用于所有类型且可用于后续cell switch的common pre-configured candidate configuration。

```text
For pre-configuration, RAN2 considers to support cell switch with pre-configured candidate configuration for all cell switch types (i.e. L3 HO, CHO, LTM).
In order to address the shortcoming of similar or duplicated configuration for separate cell switch, one common pre-configured candidate configuration is shared/applicable for all cell switch types, and can be used for subsequent cell switch.
R2-2601599	Discussion on 6GR Mobility	Sharp	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p017`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

RAN2 应支持用于带预配置 mobility schemes 的 common candidate RRC configuration。

```text
RAN2 should support a common candidate RRC configuration for mobility schemes with pre-configuration.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p018`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

不带预配置的 mobility schemes 使用独立于 common candidate RRC configuration 的 RRC configuration。

```text
The RRC configuration for mobility schemes without pre-configuration is separate from the common candidate RRC configuration.
R2-2601543	Discussion on 6G Mobility	CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p019`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

RAN2 将研究设计适用于 6G Day1 所支持所有 handover schemes 的 6GR mobility framework，以解决 5G mobility 的 shortcomings a/b/c。该框架包含可选的 Pre-configuration 和 Early processing，以及 Cell switch triggering 和 Cell switch execution。

```text
To address shortcomings a/b/c of mobility in 5G,RAN2 study to design a 6GR mobility framework applicable for all the supported handover schemes in 6G Day1. 6GR mobility framework is structured into the following steps:
Pre-configuration(optional)
Early processing(optional)
Cell switch triggering
Cell switch execution
NTN: General
R2-2602080	Discussion on measurement and mobility framework for NTN	HONOR	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p020`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

对于 NTN，RAN2 将考虑用于 measurement report 和 UE triggered mobility（例如 cell switch 和 cell reselection）的 location-based conditions。

```text
For NTN, RAN2 will consider location-based conditions for measurement report and UE triggered mobility (e.g., cell switch and cell reselection).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p021`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

对于 NTN，RAN2 将考虑用于 measurement report 和 UE triggered mobility（例如 cell switch 和 cell reselection）的 time-based conditions。

```text
For NTN, RAN2 will consider time-based conditions for measurement report and UE triggered mobility (e.g., cell switch and cell reselection).
Noted
R2-2602282	Discussion on 6G NTN mobility and multi-orbit coordination	Google	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p022`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

RAN2 将研究并支持 RACH-less handover 在 6G NTN 中的适用性，包括其与 CHO mechanisms 的潜在组合，以尽量减少 service interruption time 和 signalling overhead。

```text
RAN2 to study and support the applicability of RACH-less handover in 6G NTN, including its potential combination with CHO mechanisms, to minimize service interruption time and signalling overhead.
Noted
R2-2601531	Views on Mobility for 6G	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p023`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

RAN2 应以 signalling efficiency、measurement 和 reporting procedures 的 energy efficiency 与 low complexity、减少 satellite switching interruption 和 signalling overhead，以及降低对 GNSS 的依赖为目标，支持 6G 中的 NTN 和 TN-NTN mobility/measurements。原文鼓励各公司牢记这些目标。

```text
RAN2 should aim to support NTN and TN-NTN related mobility/measurements in 6G with the following design goals:
a.	signalling efficiency (e.g., to signal neighbour satellite information and multiple SMTCs)
b.	energy efficiency and low complexity in measurement and reporting procedures  (e.g., measurements of multiple satellites or procedure for using and updating of multiple SMTCs)
c.	reducing satellite switching interruption and signalling overhead (such as ealry sync, considering RACH-less HO and satellite switch with resynchronization)
d.	reducing dependency on GNSS.
Companies are encouraged to keep in mind these goals
Noted
NTN: TN-NTN interworking
R2-2602365	Requirements for TN and NTN joint deployment: mobility and throughput enhancements  	Boost Mobile Network	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p024`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

应支持 Intra-RAT（Intra-6G）NTN-TN 和 TN-NTN 在 IDLE、INACTIVE、CONNECTED 状态下的 mobility，且与 5G 中定义的能力相当。

```text
Intra-RAT(Intra-6G) NTN-TN, TN-NTN mobility in IDLE, INACTIVE and CONNECTED – comparable to what was defined in 5G - shall be supported.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p025`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

6G NTN mobility study 应研究不同的 NTN-TN network integration models（例如 inter/intra PLMN、同一或不同运营商）对 handover latency 等方面的影响。

```text
6G NTN mobility study shall address different models of NTN-TN network integration, e.g. inter/intra PLMN (same/different operator) impact to e.g., handover latency.
-	Ericsson asks what are the impact to RAN2 for this topic
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p026`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

应支持 6G TN 与 5G NTN 之间的 Inter-RAT mobility。6G NTN mobility study 应研究 TN 与 NTN 间 Inter-RAT mobility 的潜在问题（例如 handover latency）及解决方案。

```text
Inter-RAT 6G TN – 5G NTN mobility support shall be supported. 6G NTN mobility study shall address potential issues (e.g. handover latency) and solution for inter-RAT mobility between TN and NTN.
-	Thales thinks that this is higher priority than 6G to 6G NTN.
Noted
R2-2602243	Further Views on 6G TN and NTN Mobility	Nokia	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p027`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

讨论在 6G 中提供 NTN cell 的 TN coverage information，以及 TN cell 中的 NTN assistance information（例如 ephemeris）。对 TN coverage signalling，讨论改进 NR 中以 reference point 和 radius 表示覆盖范围的方式；该条目记为 Noted、Not treated。

```text
6G should be able to provide TN coverage related information in the NTN cell as well as to provide NTN assistance information in TN e.g. ephemeris in TN cell. For TN coverage signalling, RAN2 discusses the improvements to NR way of representing these (i.e. reference point and the radius).
-	Samsung and Huawei are not sure this is useful.   Ericsson thinks that we can provide mechanisms for TN measurement relaxation in NTN cells.   Mediatek thinks that we can provide some rough coverage.
Noted
Not treated
R2-2601510	Discussion on 6G mobility	Xiaomi	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p028`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

提出研究 TN 与 NTN 间 mobility 的 handover，包括结合 NTN location 或 timing information 与 TN signal quality 的方案，以及 UE 在 TN 网络驻留时何时启用 GNSS 获取位置以执行向 NTN 的 handover。还提出研究 NTN multi-orbit scenarios。

```text
The following aspects should be studied for the mobility between TN and NTN.
Handover:
Hand over mechanism, a handover scheme that combines NTN’s location or timing information with TN’s signal quality
When the UE should activate GNSS to acquire its location while camping on the TN network to perform handover to NTN
NTN: multi-orbit scenarios
R2-2601543	Discussion on 6G Mobility	CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p029`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

提出研究基于不同 service requirements 在不同 orbit 间高效切换，以及 network assisted/controlled switching mechanisms。另提出研究 Multi-Orbit solution 对 cell selection、cell re-selection 和 handover 的影响、VSAT 的 network assistance information、邻区数量、cell prioritization criteria，以及高效提供 LEO/MEO/GEO ephemeris 的方式。

```text
For multi-orbit scenario, suggest RAN2 to study:
•	Efficient switching between orbits based on different service requirements, e.g., UE camps on GSO cell and switches to different orbits to perform service with different QoS requirements.
•	Efficient network assisted/controlled switching mechanisms.
-	Nokia asks if this is both connected and idle and also how does it differ from NR.  CATT thinks that this can be connected mode and it can be more efficient like for example paging.
-	Qualcomm asks if there will be any mobility restrictions.   CATT thinks it is up to network control.
-	CMCC and Apple thinks that this is only from idle to connected mode, it is like a virtual carrier. Apple agrees but thinks that this is a bit more complex than TN.
Noted
R2-2601523	Multi-Orbit Requirements	SES, CSCN, SKY Perfect JSAT, Kratos	discussion
For the 6G Mobility study, in addition to issues highlighted in section 9, we propose to study the following:
Investigate the impact of cell selection, cell re-selection and handover procedures for a Multi-Orbit solution.
Network assistance information for the VSAT for efficient switch between different orbits
Inline interference problem and mitigation options
Investigate number of neighboring cells
Investigate additional cell prioritization criteria that not only provides signal strength and signal quality but also service level and interference levels
To evaluates how to efficiently provide the ephemeris information for LEO/MEO/GEO (e.g. new system information block)
-	Oppo thinks that the first one is the most important.
Noted
R2-2602488	Study on 6G Mobility Framework	Samsung	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p030`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

讨论指出，6G NTN 的 multi-orbit mobility 可在没有特定增强的情况下支持；同时提出研究多轨场景下的 cell selection/reselection、UE 与网络功耗、pingpong、mobility restrictions 和 assistance information。该条目记为 Noted。

```text
Multi-orbit NTN mobility can be considered to be supported for 6G NTN without any specific enhancements.
-	CATT thinks that we can do something more efficiently to save UE and NW power. Google thinks that if the UE camps in GEO and then LEO comes along for a few second, it would be desirable to avoid switching to LEO and this case is not supported. Samsung thinks that we have other ways in idle mode to prevent the UE from camping in other cells.
-	SES explains that this happens very often where MEO/LEO/GEO are aligned and to avoid pingpong and only the network know and ideally it could move the UE to right orbit.   There is also something called exclusion zone.
-	Nokia thinks that we are now designing 6G cell selection/reselection and we should look at how to accommodate the multi-orbit scenario.
-	Huawei is also supportive to study this, to guide the UE to perform mobility without having to go to an intermediary orbit and we may need some assistance information to accommodate.
-	Qualcomm thinks that we need to consider mobility and measurement restrictions.
-	Ericsson
Noted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p031`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

将 GNSS-free NTN operation 相关方面的讨论列为 6G study 的优先事项。

```text
Discussions on aspects of GNSS-free NTN operation are prioritized in the 6G study.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p032`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

RAN2 研究 GNSS-free NTN operation 的 UP procedure timings 和 measurement timings 处理方式。

```text
RAN2 studies how to handle UP procedure timings and measurement timings for GNSS-free NTN operation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p033`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

RAN2 研究 GNSS-free NTN operation 下，如何支持 (quasi-)Earth-fixed cells 和 Earth-moving cells 的 mobility。该条目记为 Noted。

```text
RAN2 studies how to support mobility for (quasi-)Earth-fixed cells and Earth-moving   cells for GNSS-free NTN operation.
Noted
R2-2601672	Mobility Aspects for 6G NTN	MediaTek Inc.	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p034`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

提出按 RAN1 术语研究不同 GNSS availability levels（GNSS-based、GNSS-degraded、GNSS-free/GNSS-less）的 NTN mobility procedures。GNSS-degraded operation 的 UE position fix 和 accuracy 等待 RAN1 结论；GNSS-free/GNSS-less 则设计不依赖 GNSS UE location information 的 mobility procedures。

```text
RAN2 should study NTN mobility procedures for different levels of GNSS availability, following RAN1’s terminology (i.e., GNSS-based, GNSS-degraded, and GNSS-free/GNSS-less).
For GNSS-degraded operation, RAN2 wait for RAN1 conclusion about obtaining UE position fix and the accuracy. Then we will discuss if time-based and location-based mobility procedures are still applicable.
To support GNSS-free/GNSS-less operation, RAN2 design NTN mobility procedures that do not rely on UE location information from GNSS.
Noted
R2-2601630	Discussion on 6G Mobility	OPPO	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p035`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.4 Mobility

针对 6G NTN 的 RRC CONNECTED mode mobility，提出 GNSS-based 情况复用 5G NTN 的多项机制，并研究 TN>NTN mobility 的 UE location based event trigger 和 PDD report。还提出以 GNSS-based operation 为基线研究 GNSS-degraded/GNSS-free 的 rough UE position 可行性，以及对所有 GNSS availability types 研究基于 QoS 的 handover 或 cell switch。

```text
For RRC CONNECTED mode mobility in 6G NTN:
a)	For GNSS-based, reuse the following mechanisms from 5G NTN: Location based event trigger for NTN>NTN mobility, time based event trigger, multiple SMTC/MG, PDD report for NTN>NTN mobility, closest reference location report.
b)	For GNSS-based, study UE location based event trigger and PDD report for TN>NTN mobility.
c)	For GNSSdegraded and GNSSfree, take GNSS-based operation as baseline, and study the feasibility of using a rough UE position estimated from the reference location used for openloop TA/frequency pre-compensation and closedloop TA/frequency adjustments, subject to accuracy evaluation by RAN1.
d)	For multiorbit mobility and NTN-TN mobility, study QoSbased handover or cell switch for all GNSS availability types.
Noted
Discussion
-	Thales thinks that for mobility we are less dependent on RAN1 for GNSS free.
-	Interdigital thinks that we can at least look at areas that RAN2 will be impacted already.   LG thinks that we don’t need to wait for RAN1.
-	Mediatek thinks that for GNSS degraded we need to wait for RAN1, but for GNSS-free/GNSS-less we can progress.  Oppo thinks for mobility we can start.
-	ESA thinks we can already start now.
Not treated
R2-2601485	Consideration of Uplink-based Mobility for 6GR	Sony, KDDI	discussion	Rel-20	FS_6G_Radio
R2-2601525	Decouple Static Information from SIB messages for TN_NTN Mobility	T-Mobile USA Inc.	discussion
R2-2601616	Discussion on 6GR Mobility	Charter Communications, Inc	discussion
R2-2601666	6GR NTN Mobility	Sharp	discussion	Rel-20	FS_6G_Radio
R2-2601728	Considerations for 6G mobility	Panasonic	discussion	Rel-20
R2-2601773	Discussion on 6GR Mobility	1Finity	discussion	Rel-20	FS_6G_Radio
R2-2601852	Measurement and Mobility for NTN	NEC	discussion	Rel-20	FS_6G_Radio
R2-2601868	Key considerations for mobility in 6G	Ofinno	discussion
R2-2601941	Discussion on 6G mobility for NTN	ASUSTeK	discussion	Rel-20
R2-2601942	Discussion on 6G Mobility design	ASUSTeK	discussion	Rel-20
R2-2602006	Discussion on the 6G mobility of NTN	CSCN	discussion	Rel-20	FS_6G_Radio
R2-2602036	Discussion on 6G mobility	NEC	discussion	Rel-20	FS_6G_Radio
R2-2602057	Discussion on the shortcomings from 5G mobility	ITRI	discussion	FS_6G_Radio
R2-2602058	Discussion on the information to support mobility between TN and NTN	ITRI, Acer Incorporated	discussion	FS_6G_Radio
R2-2602079	Discussion on mobility management for 6GR	HONOR	discussion	Rel-20	FS_6G_Radio
=> Revised in R2-2602618
R2-2602618	Discussion on mobility management for 6GR	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2602088	Discussion on Mobility in 6G systems	Tejas Network Limited	discussion	Rel-20	FS_6G_Radio
R2-2602090	Discussion on mobility in 6G	Transsion Holdings	discussion
R2-2602110	Consideration on mobility for 6GR	Spreadtrum, UNISOC	discussion	Rel-20
R2-2602233	Views on 6G Mobility	Apple	discussion	Rel-20	FS_6G_Radio
R2-2602275	Solutions for mobility shortcomings	Ericsson	discussion	Rel-20	FS_6G_Radio
R2-2602280	On 6GR Mobility	Fraunhofer HHI, Fraunhofer IIS	discussion
R2-2602328	Alignment of NTN Mobility Terminology between RAN1 and RAN2	Toyota ITC	discussion	Rel-20
R2-2602350	Resource reservation for pre-configuration based mobility	Rakuten Symphony, Jio Platforms	discussion	Rel-20
R2-2602361	Discussion on 6G mobility framework	Rakuten Symphony	discussion	Rel-20
R2-2602368	Considerations on pre-configured mobility in 6G	AT&T	discussion	FS_6G_Radio
R2-2602391	Discussion on resource management for UE-triggered mobility	ETRI	discussion	Rel-20
R2-2602392	Discussion on 6G mobility	NTT DOCOMO	discussion	Rel-20
R2-2602395	Root Cause of Early CSI-Acquisition Shortcomings and Potential Enhancements	Jio Platforms	discussion	Rel-20	FS_6G_Radio
R2-2602401	Resource-Efficiency Shortcomings in Mobility and Potential Enhancements	Jio Platforms	discussion	Rel-20	FS_6G_Radio
R2-2602451	Prioritization of essential issues for 6G mobility framework 	Kyocera 	discussion	Rel-20
R2-2602503	Overview of 6GR NTN mobility	Amazon Web Services	discussion
R2-2602506	Discussion on Mobility for 6GR	KDDI Corporation	discussion
R2-2602525	Minimizing Interruption Time in 6G Mobility	Google Korea LLC	discussion
R2-2602556	Resource reservation in 6G mobility	TCL	discussion	Rel-20	FS_6G_Radio
R2-2602558	Shortcomings in 5G mobility and possible solutions for 6G	Indian Institute of Tech (M)	discussion	Rel-20
R2-2602568	Discussion on 6G Mobility	CEWiT	discussion	Rel-20	FS_6G_Radio
R2-2602579	Discussion on 6G Mobility	Turkcell, Deutsche Telekom, Ericsson	discussion	Rel-20
R2-2602580	IMU Views on 6GR Mobility and Measurements	IMU	discussion
=> Revised in R2-2602591
R2-2602591	IMU Views on 6GR Mobility and Measurements	IMU	discussion	R2-2602580
R2-2602590	Discussion on mobility framework for NTN including multi-orbit scenarios and (intra-RAT) mobility between TN and NTN	Turkcell	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.4-p036`

### [6G/Rel-20 RAN2#133] `agreement` 10.4 Mobility

研究如何降低与 HO command processing 相关的中断时间及 HO 的数据中断时间。识别整体 HO delay timeline 的组成部分，并确定各部分由哪个 WG 负责。

```text
Study how to reduce interruption time related to HO command processing
Study how to reduce data interruption time related to HO.
Identify the components that contribute to the overall HO delay timeline and identify which WG is responsible for those components.
Measurements:
R2-2600374	Considerations on 6G Mobility	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-a001`

### [6G/Rel-20 RAN2#133] `agreement` 10.4 Mobility

研究基于 pre-configuration 的 mobility，以协调 RAN3 解决上述 resource reservation 问题。

```text
Pre-configuration based mobility is studied with the aim to address the resource reservation issues described above in coordination with RAN3
R2-2600645	Mobility for 6GR	MediaTek Inc.	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-a002`

### [6G/Rel-20 RAN2#133] `observation` 10.4 Mobility

Early DL synchronization 可帮助 UE 为候选小区获取下行定时参考，从而减少 mobility 期间的中断。精细时间同步与 UE power consumption 之间存在权衡。

```text
Early DL synchronization can help to reduce interruption during mobility by allowing UEs to derive downlink timing references for candidate cells, but the trade-off between fine time synchronization and UE power consumption is delicate.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-o001`

### [6G/Rel-20 RAN2#133] `observation` 10.4 Mobility

Early UL synchronization 可能减少 mobility 期间的中断，但会增加 UE complexity、可能增加 UE power consumption，并增加 network complexity。

```text
Early UL synchronization may help to reduce interruption during mobility but it increases the UE complexity (special DCI), may increase the UE power consumption (early RA to cells the UE may not go to) and increases the network complexity (inter-node coordination).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-o002`

### [6G/Rel-20 RAN2#133] `observation` 10.4 Mobility

Early CSI acquisition 可帮助减少 mobility 期间的 throughput degradation，但会增加网络和 UE 的 power consumption；额外处理还可能引入更多 latency 或 interruption。

```text
Early CSI acquisition can help to minimize throughput degradation during mobility, but it is a high-cost operation for the network and the UE in terms of power consumption and the additional processing effort may introduce further latency/interruption.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-o003`

### [6G/Rel-20 RAN2#133] `observation` 10.4 Mobility

5G mobility（如 L3 HO、LTM）即使只有最小变更也依赖传输完整的 RRCReconfiguration message，导致显著处理延迟；LTM 的 fast RRC processing 可缓解该问题，但效果受 UE capability 和缺乏 network control 限制。

```text
5G mobility (e.g. L3 HO, LTM) relies on transmitting the full RRCReconfiguration message even for minimal changes, leads to significant processing delays (20ms per RAN4, sometimes 40ms in practice). While LTM's fast RRC processing feature mitigates this, but its effectiveness is limited by UE capability, and lack of network control.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-o004`

### [6G/Rel-20 RAN2#133] `observation` 10.4 Mobility

5G signaling design 为 L1 和 L3 measurements 定义了完全不同的 signaling frameworks，没有考虑两者功能的相似性。原文将此主要归因于相关讨论在不同 WGs 中进行。

```text
The 5G signaling design defines completely different signaling frameworks for L1 and L3 measurements, without taking into account the similarities between these functions. This is mainly because the discussions are taking place in different WGs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-o005`

### [6G/Rel-20 RAN2#133] `observation` 10.4 Mobility

Unified signaling design 是 6G design 的预期目标之一，但不是唯一目标。设计不应仅为追求统一而放弃功能设计本身的合理性。

```text
Unified signaling design is an expectation of 6G design, but not the only goal. We should not abandon the rationality of the functional design itself simply in pursuit of unification.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-o006`

### [6G/Rel-20 RAN2#133] `observation` 10.4 Mobility

CHO 的 resource reservation 周期最长可达 3.7 秒，并且依据典型 CHO preparation thresholds，可能需要为超过 3 个候选小区准备资源。

```text
The period of resource reservation for CHO can be as large as 3.7 seconds and the resources might need to be prepared for more than 3 candidate cells, based on the typical CHO preparation thresholds.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-o007`

### [6G/Rel-20 RAN2#133] `observation` 10.4 Mobility

CHO 的 resource inefficiency 随小区内 UE 数量、每个 UE 的候选小区数量及资源预留时长增加。大多数预留资源最终未被使用，因为 UE 只对一个已准备的候选小区执行 CHO，或完全不执行 CHO。

```text
Resource inefficiency in CHO scales with the number of UEs in the cell, number of candidate cells per UE and the time those resources are reserved. Furthermore, most of these resources are eventually not used as the UE executes a CHO just to one of the prepared candidate cells or does not execute CHO at all.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-o008`

### [6G/Rel-20 RAN2#133] `observation` 10.4 Mobility

为 conditional mobility 预留候选无线资源的网络负担，以及网络无法完全控制 UE mobility，是 CHO 商业化的障碍。

```text
Network burden to reserve candidate radio resources for conditional mobility and network’s inability to fully control UE mobility are obstacles to CHO commercialization.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-o009`

### [6G/Rel-20 RAN2#133] `observation` 10.4 Mobility

在 Legacy L3 handover 或 CHO 中，UE 只应用 HO command 并执行常规 delta reconfiguration；而在 LTM 中，UE 必须先执行新的、复杂的 LTM-specific configuration management（clause 5.3.5.18.6），该步骤主要用于支持后续 mobility。无论网络是否实际应用后续 mobility，UE 都需要实现这一步。

```text
In Legacy L3 handover or CHO, the UE just applies HO command and performs normal delta reconfiguration. But in LTM, the UE has to perform a new and complex LTM-specific configuration management (clause 5.3.5.18.6) first, which is largely specified to enable subsequent mobility. The UE needs to implement this complex step regardless whether the network actually applies subsequent mobility or not.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-o010`

### [6G/Rel-20 RAN2#133] `observation` 10.4 Mobility

Multi-Orbit NTN solution 将有助于实现 ubiquitous 和 robust connectivity。

```text
Multi-Orbit NTN solution would contribute to a ubiquitous and robust connectivity.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-o011`

### [6G/Rel-20 RAN2#133] `observation` 10.4 Mobility

Multi-Orbit NTN solution 需要考虑新的 mobility 和 handover 场景，并寻求相应解决方案。

```text
For the Multi-Orbit NTN solution, new mobility and handover scenarios need to be considered, and solution sought.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-o012`

### [6G/Rel-20 RAN2#133] `observation` 10.4 Mobility

Multi-Orbit NTN solution 需要考虑额外的 handover triggering mechanism。

```text
With the Multi-Orbit NTN solution, additional handover triggering mechanism would need to be considered.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-o013`

### [6G/Rel-20 RAN2#133] `observation` 10.4 Mobility

Multi-Orbit NTN solution 下，VSAT 的 neighbouring list 中将包含大量 satellite cells。

```text
with the Multi-Orbit NTN solution, large number of satellite cells would be in VSAT’s neighbouring list.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-o014`

### [6G/Rel-20 RAN2#133] `observation` 10.4 Mobility

Multi-Orbit NTN solution 需要考虑 Non-Terrestrial Service Anchor。

```text
A Non-Terrestrial Service Anchor need to be considered for a Multi-Orbit NTN solution.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-o015`

### [6G/Rel-20 RAN2#133] `observation` 10.4 Mobility

Multiple SMTCs configuration 配合 UE 在 idle/inactive mode 下自适应调整，以及 connected mode 下由 NW 控制的 SMTCs 调整方案，对 6G NTN 很重要。

```text
Multiple SMTCs configuration with UE adaptive adjustment solutions in idle/inactive mode and with NW-controlled adjustment of SMTCs solutions in connected mode are important for 6G NTN.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-o016`

### [6G/Rel-20 RAN2#133] `observation` 10.4 Mobility

为支持至少 beam hopping，6G NTN 需要在 idle/inactive mode 下采用 location-based SMTC selection，并在 connected mode 下采用 UE assisted SMTC configuration。

```text
Location-based SMTC selection solution in idle/inactive and UE assisted SMTC configuration in connected mode are necessary for 6G NTN at least to support ‌beam hopping.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-o017`

### [6G/Rel-20 RAN2#133] `observation` 10.4 Mobility

在 NTN cell 中广播 TN coverage information，以及在 TN cell 中提供 NTN assistance information，有利于节能，并需要支持 6G NTN-TN reselection。

```text
TN coverage information broadcast in NTN cell and NTN assistance information provided in TN cell are beneficial for energy saving and needs to support for 6G NTN-TN reselection.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-o018`

### [6G/Rel-20 RAN2#133] `proposal` 10.4 Mobility

RAN2 将在 6G 讨论中考虑 5G mobility 的不足，并记录 early DL sync、early UL sync 和 early CSI acquisition 的具体短板，包括信令复杂度、UE 功耗、资源开销及不必要的提前操作。

```text
Capture the advantages and drawbacks (possibly using as starting point the tables in this contribution) of the following technical components:
Early DL synchronization: can help to reduce interruption during mobility, but the trade-off between fine-time synchronization and UE power consumption/complexity is delicate.
Early UL synchronization: can help to reduce interruption during mobility but puts higher complexity on the network and the UE and may cause interruption at source cell.
Early CSI acquisition: can help to minimize throughput degradation during mobility but is a high-cost operation for the network and the UE in terms of power consumption.
-	Qualcomm thinks that we should capture shortcoming and what can 6G do.
Noted
| Agreements on mobility 1 RAN2 to take into account in 6G discussions the following shortcomings of mobility in 5G. These shortcomings are not used a strict guidelines for our solutions, but rather as observations to keep in mind in our discussions: a. Mobility procedures defined as standalone mechanisms, each with its own configuration and signalling. b. Some mobility aspects handled across multiple protocol layers (RRC, MAC, L1) with overlapping responsibilities c. Similar or duplicated configurations defined at different levels of the RRC specification. d. Complex UE/Network signalling and signalling overhead (e.g. subsequent LTM) e. Mobility mechanisms targeting resilience (e.g., RLF avoidance) have limited scope. f. Use of reserved resources (e.g., only use configured grant, CFRA preamble allocations) leading to complex and inefficient resource usage. 2 RAN2 to take into account the following shortcomings . This list doesn’t imply that we will solve all of these shortcoming and some of the issues may not happen in all cases. Shortcomings of early DL sync: - complex UE/network signalling (pre-configuration of TCI states, short-lived) - UE power consumption and measurement complexity (many RS to measure) - RS overhead (when using TRS) - unnecessary early DL sync (e.g., if the UE does not go soon to the cell) Shortcomings of early UL sync using RA: - complex UE/network signalling (RA to neighbour cell) - UE power consumption - RA resource usage (e.g., CFRA) - interruption for inter-frequency - unnecessary early UL sync (e.g., if the UE does not go soon to the cell) Shortcoming of early UL sync using UE-determined TA: - only works when source and target are synchronized - unnecessary early UL sync (to cells the UE does not go) Shortcoming of early CSI acquisition: - UE power consumption and measurement complexity - RS overhead (CSI-RS) - interruption for inter-frequency - unnecessary early CSI acquisition (e.g., if the UE does not go soon to the cell) - does not consider UL throughput |
| --- |
R2-2601348	Shortcomings of early DL/UL synch, and early CSI acquisition	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
Noted
Network triggered mobility without pre-configuration:
R2-2600374	Considerations on 6G Mobility	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-p001`

### [6G/Rel-20 RAN2#133] `proposal` 10.4 Mobility

研究降低 6G mobility 中 Tprocessing delay 的方法，包括仅在 mobility 时更新最少配置以实现简单快速切换，以及增强 5G fast RRC processing，例如 NW-controlled fast RRC processing。

```text
Study on the followings for reducing Tprocessing delay in 6G mobility:
Study methods to further reduce Tprocessing time, e.g. enable simple and fast handover by only updating a minimum set of configurations during mobility.
Study enhancement on 5G fast RRC processing method, e.g. NW-controlled fast RRC processing.
Noted
R2-2600127	Discussion on 6G mobility	Xiaomi	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-p002`

### [6G/Rel-20 RAN2#133] `proposal` 10.4 Mobility

为尽量减少 service interruption，RRC configuration 按不同部分组织，mobility 时仅重新配置发生变化的部分。RAN4 的 interruption time 要求根据发生变化的配置部分定义。

```text
To minimize service interruption, RRC configuration is structured into different parts and only changed parts are reconfigured during mobility. RAN4 requirements for interruption time are defined according to the changed configuration parts.
Noted
R2-2600805	Mobility 5G shortcomings and how to address them in 6G	Ericsson	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-p003`

### [6G/Rel-20 RAN2#133] `proposal` 10.4 Mobility

研究为 mobility 定义特定的 RRC message，并研究 UE 如何根据消息内容采用不同的 RRC processing delay 要求。必要时，此类消息可以较小。

```text
Define specific RRC message(s) for mobility (which may have a rather small size if needed) and study how the UE may apply different RRC processing delay requirements depending on the content of such RRC message.
Noted
R2-2600472	Selected topics on 6G Mobility	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-p004`

### [6G/Rel-20 RAN2#133] `proposal` 10.4 Mobility

RAN2 将研究使用低开销、类似 MAC 的 Layer-2，承载 mobility 相关的“critical and short”控制配置交换和 measurement reporting，以实现快速、高效且稳健的 mobility。讨论还涉及减少 HO processing 和 data path interruption，以及配置大小与处理时间的关系。

```text
For fast, efficient yet robust mobility, RAN2 to study on using low overhead (MAC like)  Layer-2 for all mobility related “critical and short” control configuration exchange and for measurement reporting.
Noted
Discussions
-	Apple thinks that this not only Tprocessing it is also reduction in data path interruption.
-	Jio thinks that we need to understand how RAN4 defined the Tprocessing time and they didn’t take into account the configuration size.   ZTE agrees that in RAN4 they didn’t care about the amount of parameters included in the HO command, but we do need to cooperate with RAN4.
-	Nokia agrees but instead of RRC we should refer to HO, we should study means to reduce the HO processing and understand the different components.
-	Qualcomm doesn’t think we should tie to RRC, just having a small RRC doesn’t mean we will have lower processing.   How to have minimal configuration during mobility and how to reduce data interruption during mobility.   ZTE observed something else in the field.  The bigger the message the bigger the interruption time.    Qualcomm observed that the larger messages take longer but that is more linked to RF processing and not RRC.   Mediatek agrees with Qualcomm.
-	Ericsson thinks that the processing should be tied to the size of the RRC message.
-	Apple thinks that for the HO command we should define something short and it can be a MAC message.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-p005`

### [6G/Rel-20 RAN2#133] `proposal` 10.4 Mobility

RAN2 先研究 6G measurements 的需求和方案，再分析配置或流程能否统一。首阶段将关注测量类型、被测 RS、报告方式及 measurement report 内容。

```text
RAN2 first studies the requirements and solutions for 6G measurements, and then analyse whether any configuration or procedure can be unified. For the first step, RAN2 to focus on the following aspects:
Measurement types: L1 or L3? beam-level or cell-level? Periodical or event-based?
Measured RS: SSB, CSI-RS? from serving or non-serving cells?
How to send the report: RRC, MAC CE, UCI?
Content of measurement report.
Noted
R2-2600279	Mobility and Measurements for 6G	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-p006`

### [6G/Rel-20 RAN2#133] `proposal` 10.4 Mobility

6G Measurement framework 支持 serving 和 non-serving cells、不同 RS 类型及不同测量目的，并涵盖频率和 RAT 范围、gap-assisted 与 non-gap-assisted 测量，以及周期和事件触发报告。Cell level 和 beam level measurements 列为支持项。

```text
6G Measurement framework should support the following:
a.	Cell level and beam level measurements
b.	Measurements for serving and non-serving cells
c.	Measurements using different RS types (e.g,. wide/narrow beams)
d.	Measurements for different purposes (e.g., mobility, RLM, BM)
e.	Intra-F/Inter-F, Intra-RAT/inter-RAT measurements
f.	Gap-assisted/non-gap-assisted measurements
g.	Periodic and event triggered measurement reporting
Noted
R2-2600127	Discussion on 6G mobility	Xiaomi	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-p007`

### [6G/Rel-20 RAN2#133] `proposal` 10.4 Mobility

RAN2 假设 6G Measurement framework 至少支持 serving 和 non-serving cells、不同 RS 类型（若 RAN1 同意）、不同测量目的、不同频率及 RAT 范围、gap-assisted 与 non-gap-assisted 测量，以及周期和事件触发报告。Cell level、beam level、L1 和 L3 measurements 仍标为 FFS；RAN2 至少等到 RAN2#134 再继续讨论。

```text
For measurement and measurement gap related study, RAN2 can postpone the discussion and wait for RAN1 and RAN4’s progress.
Noted
Discussion
-	ZTE thinks that form network perspective we would need both L1 and L3 and beam and cell level measurements as they are used for different reasons.   Qualcomm explains that we just can agree that we have cell and beam levels but how they are derived can be discussed after.
-	CATT thinks that we should at least start with the measurements for mobility and what HO mobility types to suupose.
-	LG thinks that we can at least start by agreeing that we need the beam and cell level.   Huawei thinks that the UE can send beam level results and the nw can derive the cell level results and would like to understand what are the issues.   If the intention is to not make 6G very fat we should consider if there are a few things that we don’t absolutely needed.   ZTE understands that the network can consolidate but this is already related to filtering so this would require the UE to send measurements more frequently so we can consolidate and filter.   Mediatek also is not sure whether we need it.   Xiaomi agrees with ZTE.
-	Mediatek thinks that if we remove bullet a and the (eg) the list makes sense.
| Agreements on measurements RAN2 assumes for 6G Measurement framework at least the following are supported: a. FFS Cell level and beam level measurements b. Measurements for serving and non-serving cells c. Measurements using different RS types (if agreed by RAN1) d. Measurements for different purposes e. Intra-F/Inter-F, Intra-RAT/inter-RAT measurements f. Gap-assisted/non-gap-assisted measurements g. Periodic and event triggered measurement reporting h. FFS L1 and L3 measurements NOTE: RAN2 will wait at least until RAN2#134 to resume this discussion |
| --- |
Pre-configuration/Conditional mobility:
R2-2600783	Various Aspects of 6G TN and NTN Mobility and Measurements	Nokia	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-p008`

### [6G/Rel-20 RAN2#133] `proposal` 10.4 Mobility

Mobility without pre-configuration 被视为 6G TN 的 baseline。研究 pre-configuration based mobility，目标是解决前述资源预留问题。

```text
Mobility without pre-configuration is considered as a baseline for 6G TN. Pre-configuration based mobility is studied with the aim to address the resource reservation issues described above.
Noted
R2-2600444	Consideration on mobility aspects for 6G	LG Electronics Inc.	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-p009`

### [6G/Rel-20 RAN2#133] `proposal` 10.4 Mobility

研究如何减少 conditional mobility 的候选无线资源预留造成的资源浪费，例如共享 mobility radio resources（如 CB-PUSCH）、动态启停执行条件评估，以及执行 conditional mobility 时的 hello/bye indication。讨论提出研究增强有无 pre-configuration 的 mobility。

```text
Study how to minimize radio resource waste due to candidate radio resource reservation for conditional mobility, e.g., shared radio resources for mobility (e.g., CB-PUSCH), dynamic activation/deactivation of evaluation of execution condition, and hello/bye indication upon conditional mobility execution.
Noted
Discussion
-	Nokia explains that for LTM the problem is a little lighter than CHO.
-	Rakuten doesn’t want to limit the baseline without pre-configuration.
-	Ericsson thinks we should study how to enhance both without and with pre-configuration.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-p010`

### [6G/Rel-20 RAN2#133] `proposal` 10.4 Mobility

6G不应支持NR LTM中的subsequent mobility和reference configuration。RAN2将研究是否支持subsequent mobility，以及是否能以更简单的方式支持。

```text
The subsequent mobility and reference configuration as in NR LTM should NOT be supported in 6G. RAN2 to study whether to support subsequent mobility, and if yes, how to support it in a simpler way.
NTN (General):
R2-2600177	6G Mobility aspects for NTN	THALES, TNO, ESA, Novamint, LG Uplus	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-p011`

### [6G/Rel-20 RAN2#133] `proposal` 10.4 Mobility

研究6G中NTN mobility的支持，包括idle和connected modes下的NTN/NTN及NTN/TN mobility，并考虑GNSS free运行。讨论还涉及GNSS resilient、不同程度的location information，以及RAN2视角的mobility影响。

```text
Study the support of mobility with NTN in 6G (e.g. NTN/NTN, NTN/TN) in both idle and connected modes with GNSS free 6GR operation.
-	Lenovo asks about GNSS free and whether it includes GNSS resilient.   Thales explains that it includes GNSS free and resilient.
-	Oppo asks if the intention is to remove some solutions related to relocated.   Thales assumes that the GNSS based should remain and on top of that they’d like to consider new GNSS free mechanism.  Oppo asks that for GNSS free we won’t have location information so the solutions won’t depend on location.
-	ESA explains that we have to study cases where the terminal has no location information.
-	Mediatek thinks that we can generalize to say that we will study mobility with various degrees of location information.
-	Qualcomm agrees but the question is what and where we should study it as RAN1 is already studying.
-	Huawei thinks that even rAN1 is study their main focus in on initial access so we should study from RAN2 perspective what is the mobility impact and take thinks like elevation angle and other metrics.   Xiaomi agrees and RAN1 will not discuss mobility.
-	Apple thinks that proposal is harmonizing the design.   We should start focusing by GNSS based as a starting point and wait for RAN1 to progress first.
-	Interdigital thinks we should study enhancements to mobility to support GNSS free and just focus on RAN2 aspects and whether we continue with location based for CHO and cell selection/reselection and pre-comp and RA.
-	Jio thinks we should study and we can speed up the market adoption of NTN in 6G.
-	ZTE thinks that we should study these aspects in all RRC states including inactive and we need to wait  for RAN1 to complete synchronization and pre-compensation aspects.
-	Samsung thinks that GNSS reliant might come for free at the end so we should start by looking at GNSS free.
-	ZTE asks if GNSS free means that we can’t use any other ways of obtaining positioning information.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-p012`

### [6G/Rel-20 RAN2#133] `proposal` 10.4 Mobility

Connected mode mobility with NTN应以zero packet loss和minimal interruption time为目标。该目标涵盖NTN/NTN及TN/NTN mobility。

```text
Connected mode mobility with NTN shall aim at zero packet loss and minimal interruption time
-	LG asks if this include TN to NTN mobility.  Thales explains that it includes both NTN/NTN And TN/NTN
-	Xiaomi thinks that we don’t even have this requirement for TN but we know that this is challenging.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-p013`

### [6G/Rel-20 RAN2#133] `proposal` 10.4 Mobility

研究TN与NTN之间的mobility支持，并研究相关高效信令，包括在NTN cells广播TN coverage information、在TN cells广播NTN assistance information，以及TN cells与NTN cells之间的ANR机制。

```text
Study the support of mobility between TN and NTN. This requires efficient signaling for   the:
Broadcasting TN coverage information in NTN cells for NTN to TN mobility.
Broadcasting NTN assistance information in TN cells for TN to NTN mobility.
ANR mechanism specified for between TN cells and NTN cells.
-	CMCC thinks that this third one is a new requirement.
-	Mediatek asks how the NTN knows the coverage of TN.  Huawei thinks this looks like a solution so we should capture our intention. For second bullet not sure if we will have the same NTN assistance information.
-	Samsung htinks that the second bullet is absolutely essentation and we should do to it for both intra- and inter-RAT.  Also not sure if the first bullet is crucial.
-	Oppo thinks that this assumes that GNSS is there.
-	Ericsson thinks that ANR seems to be more of a RAN3 focused things.
-	ZTE thinks that the first one is important for energy savings.
-	Jio thinks that unification of broad
-	Qualcomm thinks we need to have a common understanding whether 6G TN and NTN are considered same RAT or different RAT and this understanding should be common across groups.
Noted
R2-2600277	Multi-Orbit NTN Solution for 6G	SES, MITRE, JSAT, Thales, Lockheed Martin, Gatehouse, Gilat, Airbus	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-p014`

### [6G/Rel-20 RAN2#133] `proposal` 10.4 Mobility

RAN2假设所有状态下GNSS-based mobility以5G GNSS-based mobility mechanism为baseline，并进一步研究GNSS-based mobility及GNSS free和resilient mobility。对于6G TN与6G NTN间mobility，研究在TN cells提供NTN assistance information、是否及如何在NTN cells提供TN coverage information，并考虑inter-RAT mobility和同一运营商下的multi-orbit场景；范围为single connectivity。

```text
RAN2 to consider “Multi-Orbit” NTN solution in the study of mobility procedures as part of the 6G Study item.
-	Huawei asks if the expected impact is providing assistance information.   Assistance information is needed everywhere regardless of whether it is TN or NT.
-	Samsung is still confused what it means, as in 5G we provide the information so not sure what is not working.   Also what is the service anchor.   Does this means some form of dual connectivity.    SES doesn’t thinks this was linked to DC, this was for single connectivity and support mobility between these layers.
-	NTN session chair in 5G these aspects are supported even if multi-orbit is not mentioned in the specs.   What is not supported is mobility between Geo and Leo as you end up staying on the layer.
-	Qualcomm sees this a redirection between different orbits.
-	Mediatek thinks that for multi-orbit we need to understand whether this includes orbits of different operators or same.  SES explains that for now we should consider just within same operators.   Mediatek thinks that multi-operator multi-orbit should also be discussed in the plenary.    Mediatek would like to understand the scenario.
Noted
| Agreements on NTN - RAN2 assumes that (all states) for GNSS based mobility, the 5G GNSS based mobility mechanism is considered as baseline. Study further aspects of GNSS based mobility - Study mobility aspects for GNSS free and resilient, including how to support TN and NTN mobility. - For GNSS based, to support mobility between 6G TN and 6G NTN study at least the following: - providing NTN assistance information in TN cells - if and how to provide TN coverage information in NTN cells - Study should also consider inter-RAT mobility (between 5G and 6G), but this discussion can take place later. - The mobility study should take into account multi-orbit scenario (e.g. targeting efficient switch between different orbits). Study assumes same operator for now. NOTE: this is for single connectivity only. |
| --- |
NTN (Mobility/measurements):
R2-2600509	Discussion on Measurement and mobility framework for NTN	HONOR	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-p015`

### [6G/Rel-20 RAN2#133] `proposal` 10.4 Mobility

对于NTN，RAN2将考虑以location-based和time-based条件用于measurement report及UE triggered mobility，例如cell switch和cell reselection。

```text
For NTN, RAN2 will consider location-based and time-based conditions for measurement report and UE triggered mobility (e.g., cell switch and cell reselection).
R2-2600951	Discussion on 6G mobility	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-p016`

### [6G/Rel-20 RAN2#133] `proposal` 10.4 Mobility

6G NTN measurement可考虑idle/inactive mode下以time-based和location-based条件启动neighbour cell measurements，并在connected mode下进行location-based triggered measurement reporting。还可考虑多种SMTC配置与调整方案，以及为6G NTN-TN reselection提供TN coverage information和NTN assistance information。

```text
For 6G NTN measurement, the following enhancements could be considered:
Time-based and location-based neighbour cells measurements initiation in idle/inactive mode
Location-based triggered measurement reporting in connected mode
Multiple SMTCs configuration with UE adaptive adjustment solutions in idle/inactive mode and with NW-controlled adjustment of SMTCs solutions in connected mode
Location-based SMTC selection solution in idle/inactive and UE assisted SMTC configuration in connected mode
TN coverage information broadcast in NTN cell and NTN assistance information provided in TN cell for 6G NTN-TN reselection.
R2-2600765	Discussion on 6GR mobility aspects	Sony	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-p017`

### [6G/Rel-20 RAN2#133] `proposal` 10.4 Mobility

Time-based和location-based conditional handover是6G NTN的baseline。6G NTN需要处理因NTN cells移动导致的handover signalling storm问题。

```text
Time-based and location-based conditional handover is the baseline for 6G NTN. 6G NTN needs to address the signalling storm issue during handover due to the movement of the NTN cells.
R2-2600087	Discussion on 6GR Mobility	vivo	discussion	Rel-20
R2-2600090	Discussion on 6G Mobility	CATT	discussion	Rel-20	FS_6G_Radio
R2-2600179	Idle mode mobility consideration on 6G TN_NTN Mobility	T-Mobile USA Inc.	discussion
R2-2600202	Considerations for NTN Mobility in 6G	MediaTek Inc.	discussion
R2-2600251	IMU Views on 6GR Mobility and Measurements	IMU	discussion
R2-2600262	Discussion on Mobility in 6G systems	Tejas Network Limited	discussion	Rel-20
R2-2600316	Discussion on 6GR Mobility	Sharp	discussion	Rel-20	FS_6G_Radio
R2-2600355	Discussion on 6GR Mobility	Fujitsu	discussion	Rel-20	FS_6G_Radio
R2-2600367	Discussion on 6G Mobility	OPPO	discussion	Rel-20	FS_6G_Radio
=> Revised in R2-2601091
R2-2601091	Discussion on 6G Mobility	OPPO	discussion	Rel-20	FS_6G_Radio	R2-2600367
R2-2600423	Connected mobility for 6GR	InterDigital, Inc.	discussion	Rel-20	FS_6G_Radio
R2-2600492	Discussion on mobility aspects in 6GR	China Telecom	discussion	Rel-20	FS_6G_Radio
R2-2600507	Discussion on Mobility management for 6GR	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2600508	Discussion on measurement for 6GR	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2600582	Discussion on 6G Mobility design	ASUSTeK	discussion	Rel-20
R2-2600604	Discussion on 6G mobility	NEC	discussion	Rel-20	FS_6G_Radio
R2-2600614	Consideration on 6G mobility	ITRI	discussion	FS_6G_Radio
R2-2600643	Views on 6GR Mobility	Fainity Innovation	discussion
R2-2600668	General considerations on mobility for 6GR	Spreadtrum, UNISOC	discussion	Rel-20
R2-2600678	Discussion on mobility in 6G	Transsion Holdings	discussion	Withdrawn
R2-2600679	Discussion on mobility in 6G	Transsion Holdings	discussion
R2-2600689	Discussion on 6G mobility	NTT DOCOMO, INC.	discussion	Rel-20
R2-2600706	On 6GR Mobility	Fraunhofer HHI, Fraunhofer IIS	discussion
R2-2600749	Discussion on 6G Mobility and measurement	Lenovo	discussion	Rel-20
R2-2600779	Considerations for 6G mobility and measurements	Panasonic	discussion
R2-2600808	6G measurements	Ericsson	discussion	Rel-20	FS_6G_Radio
R2-2600821	Mobility in 6GR	TOYOTA ITC	discussion	FS_6G_Radio
R2-2600866	Key considerations for mobility in 6G	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2600900	Discussions on 6G Mobility	Futurewei	discussion	Rel-20	FS_6G_Radio
R2-2600907	Interruption Time Reduction Techniques for 6G Mobility	Jio Platforms	discussion	Rel-20	FS_6G_Radio
R2-2600908	Considerations on Split Handover Configuration for Resource-Efficient Mobility in 6G	Jio Platforms	discussion	Rel-20	FS_6G_Radio
R2-2600909	Resource-Efficient Mobility Preparation and Activation for 6G	Jio Platforms	discussion	Rel-20	FS_6G_Radio
R2-2600910	Unified RRC Configuration Framework for 6G Mobility	Jio Platforms	discussion	Rel-20	FS_6G_Radio
R2-2600916	Cell-Pair Specific Inter-RAT Mobility Configuration	Jio Platforms	discussion	Rel-20	FS_6G_Radio	R2-2508769
R2-2600920	Discussion on UE-triggered mobility	ETRI	discussion	Rel-20
R2-2600935	Consideration for 6G connected mode mobility	Kyocera	discussion	Rel-20
R2-2600984	Discussion on mobility aspects of 6GR	Rakuten Mobile, Inc	discussion	Rel-20
R2-2600986	Study on 6G Mobility Framework	Samsung	discussion	Rel-20
R2-2601013	Overview of 6GR NTN mobility	Amazon Web Services	discussion
R2-2601035	Discussion on the 6G mobility of NTN	CSCN	discussion	Rel-20	FS_6G_Radio
R2-2601036	Discussion on 6G Mobility and Interruption Time	Google Korea LLC	discussion
R2-2601037	Views on Mobility for 6GR	KDDI Corporation	discussion	Rel-20
R2-2601047	6G Mobility and unification of procedures	CEWiT	discussion	Rel-20	FS_6G_Radio
R2-2601053	Discussion on 6G Mobility	Turkcell	discussion	Rel-20
R2-2601102	6G mobility and measurements	TCL	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.4-p018`

### [6G/Rel-20 RAN2#132] `agreement` 10.4 Mobility

NR cell (re)selection framework（包括 best cell principle、cell ranking 和 inter-freq/RAT prioritization 等）作为 6G cell reselection framework 的基线。后续研究 6G 相关方面对 cell selection/reselection 的影响，并待其他 WGs 在 cells、reference signals 和 measurement framework/requirements 等方面取得进展后继续讨论。

```text
NR cell (re) selection framework (e.g best cell principle, cell ranking, inter-freq/RAT prioritization, etc)  is the baseline of 6G cell reselection framework.
Understand the issues we want to address in 6G. Study further how other 6G related aspects with energy saving, spectrum aggregation, service awareness, features, deployment type (e.g. TN, NTN), slicing, speed dependent etc impact cell selection/reselection, etc.
These discussions will resume once we have some progress/understanding from other WGs on cells, reference signals, measurement framework/requirements etc.
Inter-RAT mobility:
R2-2508832	Discussion on 6G mobility	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.4-a001`

### [6G/Rel-20 RAN2#132] `agreement` 10.4 Mobility

对于 5G 与 6G 的 inter-RAT mobility，起步方案支持 RRC_CONNECTED 状态下的 handover 和 re-direction，并可向 UE 提供 inter-RAT cell reselection information。进一步增强需求待 intra-RAT 方案的后续讨论后再评估，并考虑 MRSS。

```text
1	For inter-RAT mobility (5G and 6G), the following is supported as a starting point:
­	For RRC_CONNECTED state, both handover and re-direction can be supported for inter-RAT mobility
­	Inter-RAT cell reselection information can be provided to UE.
2	Wait for further mobility discussions on the intra-RAT solutions, before coming back to look at the need for further enhancements.  Consider MRSS.
Not treated
R2-2508085	Discussion on 6G mobility	Xiaomi	discussion	Rel-20	FS_6G_Radio
R2-2508178	Discussion on Intra-RAT Connected Mobility for 6GR	TCL	discussion
R2-2508192	On 6GR Mobility	Fraunhofer HHI, Fraunhofer IIS	discussion
R2-2508271	Discussion on 6GR Mobility	Fujitsu	discussion	Rel-20	FS_6G_Radio
R2-2508354	Views on Mobility and RRM for 6G	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
R2-2508363	On the Unified, Reliable and Interruption-free 6G Mobility	Nokia, Turkcell	discussion	Rel-20	FS_6G_Radio
R2-2508384	6G Mobility Discussion	Apple	discussion	Rel-20	FS_6G_Radio
R2-2508392	Consideration on mobility aspects for 6G	LG Electronics Inc.	discussion	Rel-20
R2-2508394	Discussion on mobility in 6G	Transsion Holdings	discussion	Rel-20	Withdrawn
R2-2508407	Consideration on 6G mobility	ZTE Corporation, Sanechips	discussion	FS_6G_Radio
R2-2508419	Discussion on Mobility in 6G systems	Tejas Network Limited	discussion
R2-2508438	Views on Mobility for 6GR	KDDI Corporation	discussion	Rel-20
R2-2508442	Discussion on mobility procedures in 6G	NEC	discussion	Rel-20	FS_6G_Radio
R2-2508465	Discussion on mobility in 6G	Transsion Holdings	discussion
R2-2508550	Discussions on the RLM/RLF for 6G mobility	ITRI, Acer Incorporated	discussion	FS_6G_Radio
R2-2508584	Multi-Orbit NTN Solution for 6G	SES S.A.	discussion	Late
R2-2508592	Discussion on Mobility management for 6GR	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2508636	Key considerations for mobility in 6G	Ofinno	discussion	Rel-20
R2-2508657	Discussion on 6G Mobility and measurement	Lenovo	discussion	Rel-20
R2-2508695	Discussion on 6GR Mobility	IMU	discussion
R2-2508769	Cell-Pair Specific Inter-RAT Mobility Configuration	Jio Platforms	discussion	Rel-20	FS_6G_Radio	R2-2507365
R2-2508776	Discussion on mobility aspects of 6G	Rakuten Mobile, Inc	discussion	Rel-20
R2-2508778	Necessity of DAPS Support in 6G Mobility	Jio Platforms	discussion	Rel-20	FS_6G_Radio
R2-2508779	Resource Efficient Mobility Procedures in 6G	Jio Platforms	discussion	Rel-20	FS_6G_Radio	Withdrawn
R2-2508784	Considerations for 6G mobility design	Panasonic	discussion
R2-2508787	6G Mobility Procedures with Efficient Resource Reservation	Jio Platforms	discussion	Rel-20	FS_6G_Radio
R2-2508795	Mobility	Turkcell, Nokia	discussion	Rel-20
R2-2508820	Consideration of cell reselection scheme for 6GR 	Kyocera 	discussion	Rel-20
R2-2508828	Discussions on 6G Mobility	Futurewei	discussion	Rel-20	FS_6G_Radio
R2-2508832	Discussion on 6G mobility	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2508859	Discussion on 6GR mobility	ETRI	discussion	Rel-20	FS_6G_Radio
R2-2508934	General considerations on mobility for 6GR	Spreadtrum, UNISOC	discussion	Rel-20
R2-2508961	Discussion on 6G Mobility design	ASUSTeK	discussion	Rel-20
R2-2508971	Views on 6GR Mobility Framework	Indian Institute of Tech (M)	discussion	Rel-20
R2-2509031	6G Mobility Framework	CEWiT	discussion	Rel-20	FS_6G_Radio
R2-2509038	Discussion on 6G Mobility	Google Korea LLC	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.4-a002`

### [6G/Rel-20 RAN2#132] `observation` 10.4 Mobility

5G mobility 设计的关键经验包括：不同 3GPP releases 中存在针对不同 handover types 的冗余设计；提升 HO performance 的方案往往仅适用于特定 handover types。

```text
Key lessons learned from 5G mobility design: Redundant design across 3GPP releases (for different handover types), and Solutions to improve HO performance are often limited to specific handover types.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.4-o001`

### [6G/Rel-20 RAN2#132] `observation` 10.4 Mobility

NR mobility 存在碎片化和复杂性，且与服务无关。6G 应面向多样化服务和设备，目标是建立单一、稳健、低时延且可扩展的框架。

```text
NR mobility suffers from fragmentation and complexity, and it is service agnostic. 6G should aim for a single, robust, low-latency and scalable framework adaptable to diverse services and devices.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.4-o002`

### [6G/Rel-20 RAN2#132] `observation` 10.4 Mobility

5G NR 中，L1 和 L3 measurement 使用分开且重复的 RS configurations。

```text
In 5G NR, separate and duplicate RS configurations exist for L1 and L3 measurement.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.4-o003`

### [6G/Rel-20 RAN2#132] `observation` 10.4 Mobility

在 5G NR 中，UE 应先执行 L3 measurement，以确保目标小区是已知小区，然后再执行 L1 measurement。

```text
In 5G NR, the UE should perform L3 measurement to ensure the target cell is a known cell before performing L1 measurement.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.4-o004`

### [6G/Rel-20 RAN2#132] `observation` 10.4 Mobility

在 5G NR 中，L1 measurement results 作为 L3 measurement results 的中间输入。

```text
In 5G NR, L1 measurement results serve as intermediate inputs for L3 measurement results.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.4-o005`

### [6G/Rel-20 RAN2#132] `observation` 10.4 Mobility

网络可利用 L1 measurement results，有效推导 cell/beam-level measurements 和 L3-filtered measurements。

```text
The network can use L1 measurement results to derive cell/beam-level measurements and L3-filtered measurements effectively.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.4-o006`

### [6G/Rel-20 RAN2#132] `observation` 10.4 Mobility

5G 的一个痛点是多个额外的 MG 相关功能（如 NeedforGap Pre-MG、Con-MG、NCSG）未纳入 5G Day-1，增加了支持不同功能的复杂性。6G Day-1 应支持简单且灵活的 MG signaling procedure。

```text
One of the pain points of 5G is that multiple additional MG-related features, e.g., NeedforGap Pre-MG, Con-MG, NCSG, was not included in 5G Day-1, which increase the complexity to support different features. A simple and flexible MG signaling procedure should be supported in 6G Day-1.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.4-o007`

### [6G/Rel-20 RAN2#132] `proposal` 10.4 Mobility

提出为所有支持的 handover types 设计统一的 6GR mobility framework，目标包括采用相同的 configuration signaling structure，并尽可能复用同一组 building blocks（functions/procedure steps）。该提议被记录（Noted）。

```text
RAN2 design a unified 6GR mobility framework, aiming at the following for all supported handover types,
‐	Same signaling structure for configuration
-	Oppo asks if this is only for DL or also for UL report.     CATT thinks it is related to all singaling.
‐	Maximizing the reuse of same set of building blocks, i.e., functions/procedure steps
-	Xiaomi asks what requirements we are assuming.  CATT explains that according to plenary SID there is a similar requirement between 5G and 6G.
-	Ofinno asks what is a building blocks.  CATT explains it can some procedures.
[2min]
Noted
R2-2508706	Connected mobility for 6GR	InterDigital Pennsylvania	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.4-p001`

### [6G/Rel-20 RAN2#132] `proposal` 10.4 Mobility

提出将 L3 HO 和 LTM 整合为单一 mobility framework，支持基于 L3/L1 measurements 和 L3/L2/L1 signalling 的 network-triggered 与 conditional mobility。

```text
Consolidate L3 HO and LTM into a single mobility framework that supports both network-triggered and conditional mobility based on L3/L1 measurements and L3/L2/L1 signalling.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.4-p002`

### [6G/Rel-20 RAN2#132] `proposal` 10.4 Mobility

提出统一 L3 HO 和 LTM（包括 network-triggered 和 conditionally triggered）的 signalling 与 procedural framework，同时允许分别配置各自的 triggering 和 reporting conditions/parameters。讨论认为可整合共同部分，但记录中对统一信令类型、保留 L3 与较低层信令等仍有不同意见；提议被记录（Noted）。

```text
Unify the signalling and procedural framework for L3 HO and LTM (both for network triggered and conditionally triggered), while enabling the possibility to configure the triggering and reporting conditions/parameters separately for each.
[2min]
-	LG asks what is meant by consolidation as the L3 and LTM are quite different.  Interdigital acknowledges that there are differences but we can consolidate the common part.
-	Qualcomm thinks that we shouldn’t have three types of singaling and shouldn’t we try to aim for one type of handover command.  Interdigital thinks that the different types of HO cover different needs and we need to keep L3 and lower layer signaling.
-	ZTE asks whether we want to add L1 signaling now.  If we keep both L3 and L1 we will need to keep two different procedures as they are sent to different entities.  We should keep L3 as baseline.
Noted
R2-2508477	Discussion on 6G mobility	NTT DOCOMO, INC.	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.4-p003`

### [6G/Rel-20 RAN2#132] `proposal` 10.4 Mobility

提出 6G unified mobility mechanism 应覆盖两类流程：网络不经预配置而配置并触发 mobility、UE 随即执行；以及网络向 UE 预配置候选配置后，由 NW/UE 触发 mobility。原文还指出 NW-triggered mobility 和 UE-initiated mobility 适用于不同目的和场景；提议被记录（Noted）。

```text
For balanced efficient resource management and mobility performance, “unified mobility mechanism” in 6G should cover following 2 types of mobility procedure.
NW configures and triggers the mobility without pre-configuration, and UE performs it immediately (i.e., legacy L3 HO-like mobility)
Candidate configurations are pre-configured by NW to UE, and after that NW/UE triggers the mobility (i.e., (C)LTM/CHO-like mobility)
[2min]
Noted
R2-2508162	Initial considerations on 6G Mobility	OPPO	discussion	Rel-20	FS_6G_Radio
Observation 5	NW-triggered mobility and UE-initiated mobility are applicable for different purposes and scenarios.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.4-p004`

### [6G/Rel-20 RAN2#132] `proposal` 10.4 Mobility

提出 6G unified mobility 支持基于 L1 和 L3 measurement 的 mobility、NW-triggered 和 UE-initiated mobility，以及 immediate 和 subsequent cell switch。还提出支持 RACH-less、early UL/DL sync、early CSI 和 early RRC processing；提议被记录（Noted）。

```text
The 6G unified mobility supports 1) both L1 measurement based mobility and L3 measurement based mobility; 2) both NW-triggered mobility and UE-initiated mobility; 3) Immediate and subsequent cell switch; 4) RACH-less, early UL/DL sync, early CSI and early RRC processing.
[2min]
Noted
R2-2508548	Discussion on 6GR Rel-20 mobility aspects	Sony	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.4-p005`

### [6G/Rel-20 RAN2#132] `proposal` 10.4 Mobility

一项意见提出以 Rel-19 LTM 作为 6G handover 工作的基线，并支持 L3 HO。记录的 agreement 是研究至少列出的 mobility schemes，包括无预配置的网络触发流程、预配置方案及 UE 触发流程，以及 CFRA、RACH-less、early UL/DL sync 和 early CSI；方案需考虑中断、鲁棒性、吞吐量下降、UE/NW 复杂度和资源效率，并先研究 5G 的不足及方案如何应对 6G 需求。该 study item 不考虑 NR 中的 DAPS。

```text
Rel-19 LTM should be the baseline for any HO work in 6G as LTM exhibited short interruption time and simple design. In addition,
L3 HO has been around for many generations, and it works well in the field [3], in our view, L3 HO should be supported.
[2min]
Noted
Discussion
Nw triggered and conditional UE triggered HO
-	Lenovo would like all companies to consider the following procedures:  RRC configuration after mobility, measurement framework, evaluation of the measurements, execution and signaling for that.
-	Sony supports docomo
-	Apple thinks that measurement reporting and actions based on measurement reporting are important.  We should set goals on faster measurement reporting and faster reaction time.   Qualcomm thinks that we can say beam level based and cell level based mobility.  And fine with supporting all other.  Ericsson thinks that we should just say measurements based mobility and further study beam/cell/L1/L3.
-	Ericsson likes docomo’s proposal.  Mediatek agrees and of course with beam level.   Also would support interdigital proposal, from device perspective it’s a pitty that we have different procedures for this, so we should aim to simplify.
-	Vivo is also fine with the direction, but we should unify and beam level should be considered since the beginning and it is related to how to change the beam the cell.
-	Nokia agrees that NW configured/triggered should be the baseline.  We can further study CHO, LTM, etc we should study them more.   A lot of those mobility procedures were never implemented but companies want to blend.  So we should start by understanding what we will have and what to unify.   For L1/L3 measurements we also don’t know from other groups, so too early to decide.
-	Xiaomi thinks that we need consider interruption time and robustness.   For interruption we have early synch, preconfig, etc.   But we should first have an understanding of what type of interruption we want to achieve, but with LTM with can achieve very close to 20ms.   From service level we don’t need to achieve the 0ms and even when we don’t have HO the network doesn’t have to schedule you in every slot.
-	Huawei agrees with Nokia that we don’t need to take all the procedures.    The application is not effected most of the time with HO so it work well already.   For pre-configuration there is a resource reservation issue and it should be considered as otherwise it is not usable, so we should be careful.  Jio agrees with the problem with preconfiguration, but there are some cases where we can use it, but for wide adoption we should look at more resource friendly procedure.   We should also consider some mandatory LTM aspect so we have interruption reduction.
-	Nokia explains that there are several aspects, number of cells, how early, which aspects of the configuration etc.  before we decide on the pre-config.
-	ZTE prefers to consider both pre-configuration otherwise a lot of the other procedures are gone.  LTM has some big drawbacks so we should study pre-configuration and further understand the different scheme.
-	Oppo thinks that for preconfiguration there are two cases, network triggered and UE triggered.
-	CMCC indicates that 80% of configurations are the same across several cells so we can consider preconfiguring the aspects that are the same.
-	Samsung thinks that LTM covers all features, so it should be the baseline.  And then further study unified framework.
-	LG agrees with apple on faster and more robust mobility, especially important for the higher band.
-	Ericsson thinks that we can try to understand if we can come up with a single solution.   Lenovo thinks it is a great goal, but it may be more complicated.   But we can start excluding a few things.    Oppo is not sure how we can come up with one solution.  Jio
Discussion on RACH-less, early UL/DL sync, early CSI and early RRC processing
-	Qualcomm is fine to support RACH-less and early UL/DL sync but would like to make it more efficient and consider UE complexity.   Nokia agrees
-	ZTE this that early CSI is for throughput improvement.
-	CATT thinks network triggered early UL/DL synch should be baseline
-	Docomo would like to add L2 partial reset.
-	Apple thinksk that we should study all this schemes for inter-RAT.  Xiaomi, ZTE agrees.   Mediatek thinks that this is for intra 6G.
-	Ericsson points out that we should really have a list on the problems we want to address.   For example, we list resource reservation problem.
Agreements on mobility
1.	Study at least the following mobility schemes
NW configures and triggers the mobility without pre-configuration, and UE performs it immediately
Pre-configured solutions and early UE configuration processing
UE triggered mobility based on some pre-configuration
CFRA, RACH-less, early UL/DL sync, early CSI.
Schemes should consider the lower interruption, robustness requirements and throughput degradation while considering UE and NW complexity and resource efficiency.
As first step, understand shortcomings/problems from 5G and how the schemes/solutions proposed can address the issues/requirements for 6G.   Aim to reduce the number of schemes required for 6G and consider how to unify after some initial discussions on the solutions
2.	DAPS as in NR is not considered in this study item
(Not treated) Measurement Framework:
R2-2508056	Discussion on 6GR mobility	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.4-p006`

### [6G/Rel-20 RAN2#132] `proposal` 10.4 Mobility

RAN2 将研究统一测量，例如为 L1 和 L3 measurement 使用 common RS configuration。并与 RAN4 协调 common beam level 和 cell level measurement，以及 common L1 和 L3 measurement。

```text
RAN2 to study the unified measurement, e.g. common RS configuration for L1 and L3 measurement. Coordination with RAN4 on common beam level and cell level measurement, common L1 and L3 measurement.
[2min]
R2-2508221	Discussion on 6GR Mobility	Sharp	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.4-p007`

### [6G/Rel-20 RAN2#132] `proposal` 10.4 Mobility

6GR 支持统一 measurement framework，至少包括适用于 L1 和 L3 measurements 的 single reference signal configuration，以及取代现有 RRC、MAC CE 和 UCI 多种机制的 unified reporting mechanism。原文指出，通过不同 uplink channels 发送相同或相似类型的 measurement reports 会造成不必要的 signalling complexity。

```text
6GR support unified measurement framework with at least the following aspects.
A single reference signal configuration applicable across L1 measurements and L3 measurements.
A unified reporting mechanism that replaces the multiple existing reporting mechanisms (RRC, MAC CE, and UCI).
[2min]
R2-2508721	Aspects on 6G mobility and measurements	Ericsson	discussion	Rel-20	FS_6G_Radio
Observation 2	NR defines means for sending the same or similar type of measurement reports using different uplink channels which causes unnecessary signalling complexity.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.4-p008`

### [6G/Rel-20 RAN2#132] `proposal` 10.4 Mobility

6GR measurements 应按统一 measurement framework 配置和上报：分别由 measurement configuration 定义 UE 测量的 reference signals，由 measurement reporting configuration 定义上报时机和内容。L1 和 L3 measurement 特性（如 L3 filter）作为配置属性；UE 根据 reliability、latency 或 error cases 等要求选择适当信道上报。

```text
Measurements in 6GR shall be configured and reported according to a unified measurement framework which has the following characteristics:
a.	A measurement configuration which defines reference signals to be measured by the UE.
b.	A measurement reporting configuration which defines when a UE shall transmit a measurement report to the network and what information to include in it.
c.	Characteristics related to current L1 and L3 measurements (e.g., L3 filter) are defined as attributes (of the measurement configuration and measurement reporting configuration).
d.	UE should use appropriate channels on where to report measurement reports based on requirements (e.g., reliability, latency, or error cases).
[2min]
R2-2508577	Discussion on 6GR mobility designs	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.4-p009`

### [6G/Rel-20 RAN2#132] `proposal` 10.4 Mobility

RAN2 应与 RAN1 密切合作，为 6GR mobility 开发适用于 L1 和 L3 measurements 的统一 measurement 和 configuration 方案。原文强调应尽早纳入 RAN1，以确保充分理解这一原则。

```text
RAN2 should collaborate closely with RAN1 to develop a unified solution for measurement and configuration that is suitable for L1 and L3 measurements for 6GR mobility. It is important to involve RAN1 early to ensure a thorough understanding of this principle.
[2min]
R2-2508985	Mobility for 6GR	MediaTek Inc.	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.4-p010`

### [6G/Rel-20 RAN2#132] `proposal` 10.4 Mobility

针对 6G measurement gap，RAN2 可从 procedure 和 signalling 设计着手。RAN4 可确定 MG periodicity、length、pattern 及相应 requirement。

```text
For 6G measurement gap, RAN2 can start from the design of procedure and signalling. RAN4 can determine the MG periodicity, length, pattern, and corresponding requirement.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.4-p011`

### [6G/Rel-20 RAN2#132] `proposal` 10.4 Mobility

RAN2 的目标是设计 measurement gap signaling framework，使 UE 能根据当前 UE configuration 和 status 动态请求 measurement gap。

```text
RAN2 aim to design a measurement gap signaling framework that allows UE to request measurement gap dynamically based on current UE configuration and status.
[2min]
IDLE/INACTIVE mobility:
R2-2508875	Study on 6G Mobility Framework	Samsung	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.4-p012`

### [6G/Rel-20 RAN2#132] `proposal` 10.4 Mobility

NR cell reselection framework 是 6G cell reselection framework 的基线。原文提出 6GR cell reselection 应支持 IDLE UEs 在多载波间高效分配负载，并考虑 services 和/或 device types、3D mobility 与 velocity。

```text
NR cell reselection framework is the baseline of 6G cell reselection framework.
[2min]
Noted
R2-2508820	Consideration of cell reselection scheme for 6GR 	Kyocera 	discussion	Rel-20
Observation 1	The multi-carrier deployments are expected to become more prevalent in 6GR deployment scenarios, according to the current TR38.914.
Observation 4	Especially for cell reselection, the functions supported in the initial release are quite important as it defines 6GR’s efficiency of load balancing and power/energy saving for a decade, given it’s difficult to deploy IDLE mode functions introduced in later releases.
Observation 6	The cell reselection priority broadcasted via SIB doesn’t achieve the load balancing since the same priority is applied to all the IDLE UEs.
Proposal 1	RAN2 should agree that the 6GR cell reselection supports the efficient load distribution of IDLE UEs, 1) among multiple carriers, 2) with awareness of services and/or device types, and 3) depending on 3D mobility and velocity.
[3min]
Noted
R2-2508502	Discussion on mobility aspects in 6GR	China Telecom	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.4-p013`

### [6G/Rel-20 RAN2#132] `proposal` 10.4 Mobility

6GR 对处于 Idle/Inactive（if supported）模式 UE 的 mobility management，应在一般 cell selection/reselection procedure 设计中考虑 network energy saving enhancements 和 multi-carrier enhancements。讨论中提及 slicing、idle mode multicarrier framework，以及测量框架和 requirements 对相关问题推进的影响。

```text
Regarding 6GR Mobility management for UE in Idle/Inactive (if supported) mode, take network energy saving enhancements and multi-carrier enhancements into account for the general cell selection/reselection procedure design in 6GR.
[2min]
Not treated
Discussions
-	Lenovo asks if slicing is included. Kyocera confirms.
-	LG is fine to study idle mode multicarrier framework.
-	Ericsson has identified an issue in the field and would like to progress those discussion.   Samsung agrees with the issue but that depends on the measurement framework from RAN4 and requirements.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.4-p014`

### [6G/Rel-20 RAN2#132] `proposal` 10.4 Mobility

5G 和 6G 支持 RRC_CONNECTED 与 RRC_IDLE UE 的 inter-RAT mobility。RRC_CONNECTED 下可支持 handover 和 re-direction，并考虑 L1 based 与 L3 based handover/cell switch；RRC_IDLE 下可向 UE 提供 inter-RAT cell reselection information。

```text
5G and 6G inter-RAT mobility is supported for both RRC_CONNECTED and RRC_IDLE state UE:
­	For RRC_CONNECTED state, both handover and re-direction can be supported for inter-RAT mobility, and both L1 based and L3 based handover/cell switch are considered;
­	For RRC_IDLE state, inter-RAT cell reselection information can be provided to UE.
[2min]
Noted
R2-2508384	6G Mobility Discussion	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.4-p015`

### [6G/Rel-20 RAN2#132] `proposal` 10.4 Mobility

为提高 IRAT mobility 效率，RAN2 应评估将 IRAT RACH-less handover、IRAT early DL/UL synchronization 和 IRAT early CSI acquisition 作为 UE optional features，并就可行性咨询 RAN1 和 RAN4。讨论中对方案可行性、复杂度、中断、L3 mechanism 基线及 mobility 简化等方面存在不同意见。

```text
For efficient IRAT mobility, RAN2 should evaluate on 6G UE performing IRAT RACH-less handover, IRAT early DL/UL synchronization and IRAT early CSI acquisition as optional features at the UE. Consult RAN1 and RAN4 for feasibility of this.
Noted
Discussion
-	Ericsson thinks that we should first look at the possible solution like for example, whether we have Xn or CN.   Then we can discuss further solutions.
-	Qualcomm thinks at least we should evaluate if there are better ways on achieving things.
-	Huawei explains that if it is inter-RAT it is likely inter-frequency so it is less attractive as you will have interruption on the source.    The first think we should look at is the flushing of data as that causes the interruption .
-	CATT thinks that L3 mechanism should be the baseline and we see some complexity to do this.
-	Tmobile thinks that for voice a smooth handover is very important.
-	Ericsson thinks that we should keep in mind that we have MRSS and hence inter-RAT mobility will happen very rarely.  We should aim for simplicity.   ZTE doesn’t agree.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.4-p016`

