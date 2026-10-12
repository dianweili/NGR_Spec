# 6GR 数据与模型传输

**当前进展** · 阶段：收敛中

RAN2 已从 AI/ML、感知、SON/MDT、QoE 等用例着手建立数据类型、端点、数据量、上报间隔和 QoS 的研究基线，并推动面向多类数据的统一框架。讨论逐步聚焦于端点与消费者、可见性和可解码性的区分、避免重复采集，以及按用例配置优先级和 QoS；对 UE-RAN 传输也提出优先研究非 IP、新数据平面和新无线承载等方向。模型传输方面，MNO 的知情与控制需求已被提出，但 UE 侧模型传输范围及网络侧模型传输仍涉及其他工作组协调。若干方案和定义仍处于提议、待协调或未处理状态，尚未形成完整定稿。

**未决问题**

- 标准化 UE 侧数据收集应由 RAN、CN 还是 OAM 终止，以及 RAN 是否可复用和解码数据，仍有不同意见并需与 SA2 等协调。
- 数据传输框架及承载方案尚未定案，包括增强 CP、增强 UP、新数据平面和新无线承载；UE-RAN 与 UE-CN 的协议选择也待进一步研究。
- 数据消费者、终止点、可见性、可解码性及标准化与厂商特定数据的适用边界仍需明确。
- 数据传输框架的用例范围和 QoS 分类仍在讨论；感知数据指标与特征待 RAN1 输入，部分连续学习、Immediate MDT、QoE 和性能监测用例是否纳入也有分歧。
- 移动性期间的传输连续性与无损要求虽已被提出为需考虑方面，但早期提议曾标记为未处理，具体机制尚未说明。
- UE 侧模型交付要求、RAN 生成模型向 UE 传输的支持需求，以及网络侧模型交付的职责划分仍待确认或跨工作组协调。

## 6GR 演进

### [6G/Rel-20 RAN2#134] `agreement` 9.3.3.1 Data transfer

UE-side data collection 中，RAN 不解码或解释数据内容，但应了解传输数据的类型以支持 controllability 和 forwarding；standardized data 的 decodability 将在 CN 或 OAM，具体位置待定。拟于 August meeting 发送 LS，RAN awareness 的实现方案仍待研究。

```text
1	For UE side data collection, RAN shall not decode and interpret the content of the data.  RAN shall have awareness on the type of data being transferred for controllability and forwarding purposes.   The decodability for standarized data will in the CN or OAM. FFS if it is in the CN or OAM.    FFS on solutions that provide awareness to the RAN
2	Send the LS in August meeting
Decodability of collected data
R2-2603271	Visibility & decodability of UE-side data in 6G data transfer	Apple, Xiaomi, Qualcomm, LG Electronics	discussion	Rel-20	FS_6G_Radio
Proposal 1	For UE-side data collection, the Termination Point in MNO does not have bit-by-bit decodabilty of data. RAN2 further discuss the characteristics of data (e.g., data types, QoS) to be exposed to MNO at Termination Point w/o access to the actual data content.
R2-2603759	Data Transfer Framework for 6G RAN	AT&T	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-a001`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

RAN2 将明确 visibility 与 decodability 是不同概念：decodability 指解码并解释数据内容的能力，visibility 指判断收到的数据应如何处理的能力。

```text
RAN2 to clarify that visibility and decodability are not equivalent concepts
- Decodability refers to the capability to decode and interpret the content of the data
- Visibility refers to the capability to determine how the received data should be handled
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p001`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

条目提出 termination point 应具备 full visibility，以决定路由、处理或本地终止数据，并以此为基线研究至少适用于 AI/ML 的 standardized data collection framework。要求还涉及数据安全与隐私、MNO 对传输过程的控制、可扩展性，以及降低对 UE 和用户流量的影响；术语说明 full visibility 包含 decodability 和 controllability，并将在 MNO。

```text
RAN2 to consider that a termination point should have full visibility (e.g., can determine whether to route/process/consume data). Based on the visibility, the termination point can perform the following operation:
- Decide whether the data needs to be routed to another NW entity;
- Decide whether the data is to be terminated locally,
- Perform the necessary processing based on the data characteristic related information (e.g., data type/QoS).
Study the standardized data collection framework with these requirements as a baseline at least for AI/ML
The data collected is secured and data integrity and confidentiality for that data is ensured.
User data privacy, anonymity and user consent is respected.
The MNO has full control of the standardized data collection transfer process and can manage data transfer to the server for UE side data collection, without the need of Service Level Agreement (SLA) for this purpose
This includes initiating, terminating, and fully managing data transfer.
MNO has full visibility for standardized data.
The design is future-proof and extendable.
The UE data collection should minimize impact to the UE battery, UE processing and memory utilization.
UE data collection should minimize impact to user traffic transmission and power saving features
These requirements can apply to both UE and NW sided data collection.  FFS if some don’t apply to both.
----
For terminology purposes – it is not implying a change of requirements
- Decodability refers to the capability to decode and interpret the content of the data
- Controllability refers to the capability to determine how the received data should be transferred (e.g. enable awareness for routing/controllability purposes, etc).
- Full visibility includes both decodability and controllability and will be in the MNO.
Termination point for UE-side data collection
R2-2604025	Discussion on data collection and transfer framework	CMCC, NTT DOCOMO, CATT, OPPO, ZTE, Ericsson, vivo, China Unicom, China Telecom	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p002`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

standardized UE-side data collection 指 UE 侧数据收集的数据类型/格式和数据传输过程均实现标准化。

```text
It is clarified that standardized UE-side data collection means that both the data type/format and data transfer procedure for UE-side data collection are standardized.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p003`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

认为网络复用 UE 侧数据采集的数据进行网络侧模型训练是合理的。Qualcomm 提出，UE 实现可能导致数据粒度不同，并询问这是否限制 UE 能力。

```text
Based on observation 5~7, it makes sense for network to reuse the data from UE side data collection for NW-sided model training.
-	Qualcomm thinks that we may have different granularity in the data according to UE implementation.  Is this now limiting what the UE can do?
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p004`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

原文认为，若在 RAN 终止 UE 侧数据采集，基于 5G-A 用例中的标准化测量结果（如 L1/L3 measurement results 或 CSI channel information）不存在安全或隐私风险，也没有将这些数据在 CN 终止的必要或益处。会议记录同时指出，对所有用例是否可复用数据尚未达成结论，并提出了标准化与厂商特定数据范围及商业化价值方面的关注。

```text
Based on observation 8~11, there is no security/privacy risk when the termination of UE side data collection is in RAN since the standardized data for UE side data collection are measurement results such as L1/L3 measurement results or CSI channel information according to 5G-A use cases. And there is no necessity and no benefit to terminate these data in CN.
-	Apple points out that we haven’t concluded on all the use case before determining whether we can reuse the data.
-	Qualcomm is concerned that there a lot of things exposed.
-	Mediatek asks this rules out vendor specific data.   CMCC thinks that this only covers standardized data.   Mediatek asks if we will have a standardized and non-standarized data collection.   Just using standardized data comes with a lot of a problems, which means that first we have to agree what data to be collected before we can collect and we have no ways to enhance the performance beyond what 3GPP has looked at.  There are other data than standardized data that can be useful.    We need to specify what the market needs as if we got this way it is not useful.   Qualcomm agrees we should do commercializable things.
Noted
R2-2602966	Discussion on 6G UE-side data collection	Xiaomi, Apple, Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p005`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

提出标准化 AI/ML UE-side data collection 的终止点不在 RAN，终止点由 SA2 决定。Huawei 询问是否支持标准化和非标准化数据；Qualcomm 与 MediaTek 认为传输非标准化数据也很重要。

```text
RAN is not the termination point for standardized AI/ML UE-side data collection. It is up to SA2 on termination
-	Huawei ask whether we will have standardized and non-standardized data.  Qualcomm and mediatek think that this is important to also have non-standardized data transferred.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p006`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

决定向 SA2 和 SA5（抄送 RAN3、SA3）发送 LS，说明 RAN 不是 AI/ML UE-side data collection 的终止点，即 6G 不支持 UE 经 gNB、OAM 到 server 的 Option 3。关于非标准化数据，讨论涉及数据验证责任、数据类型可见性，以及标准化数据应可解码的意见。

```text
Send LS to SA2 and SA5 (cc RAN3, SA3) on RAN2 decision on ‘RAN is not the termination point of AI/ML UE-side data collection’, i.e., Option 3 (UE -> gNB -> OAM -> server for data collection for UE-side model training/OTT server) of AI/ML UE-side data collection is not supported in 6G.
Noted
Discussion on standarized and non-standarized data
-	Oppo asks who is going to do the verification of the data.  Xiaomi explains that the non-standarized data doesn’t include any private data.    SA2 studied that and hasn’t concluded the verification.   Xiaomi thikns that the network can verify what is the UE and the data type.  But it doesn’t have to decode what is reported.   Mediatek thinks that the verification happens between the UE and the consumer and if the data is non-standarized we can provide some visibility on the type of data and some data can be used by MNO and some cannot.
-	Ericsson doesn’t think that we can prevent non-standarized data but at least the standarized data should be decodable.
R2-2602955	Considerations on RAN2 Data Transfer in 6G	vivo, CAICT, NTT DOCOMO INC., CMCC	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p007`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

提出 UE-side data collection 的终止点可依数据是否供 RAN 使用而定：供 RAN 复用时由 RAN 终止并可查看数据，否则由 CN 终止且 RAN 不可查看；基线考虑 RAN 为终止点，涉及 CN 的情况需 RAN2 与 SA2 进一步协调。讨论中对单一采集方案、RAN 与 CN 终止点及数据复用等问题存在不同意见。

```text
For UE-side data collection, the termination points include the following cases:
If the data can be reused by RAN (e.g., for network-side AI model training), RAN is the termination point with visibility on the data;
Otherwise (if the data is not expected to be utilized by RAN), CN is the termination point, and RAN has no visibility on the data.
As a baseline, RAN2 should consider the RAN as the termination point; cases involving the CN as the termination point are subject to further coordination between RAN2 and SA2.
Noted
Discussion on termination point RAN vs. CN for standarized data with assumption we don’t exclude non-standarized data (to be discussed later)
-	LG agrees with Xiaomi, as we should discussed UE side and NW data.
-	Lenovo thinks that UE shouldn’t share data with the RAN, but it can share it with the operator in CN and they can determine how to handle it.
-	Interdigital asks what is the technical reason to have in the RAN, if the requirements are satisfied by MNO if the data is in the CN.
-	CMCC thinks that the motivation is to re-use the data for both network sided and UE sided.   Interdigital thinks that there is already a mechanism for data collection for the network.
-	Tmobile agrees that we should be able to reuse, but there are things that vendors can do outside the RAN and that’s why we have thing a bit bigger and we should terminate CN.
-	ATT agrees with CMCC and we should have the ability to decode for some use case, but we can make it configurable.  Contrallability should always be in the RAN.
-	Xiaomi thinks we should have a simple and single solution to collect the data from the UE side, as if we have for some cases sending to RAN and some cases for CN this increases complexity.  Apple agrees with Xiaomi.
-	Verizon thinks that we can get the data to OAM and we can combine with other data as well.
-	Samsung also agrees that we should have a simple way of doing it and we can’t exclude one of the termination point so we should study both.
-	ZTE also thinks that we should RAN as a termination point.
-	ZTE thikns that this data can also be re-used by SON and MDT as a lot of this measurement data.
-	China Telecom and CATT also would like to re-use the data.   CATT and ZTE thinks that this will reduce the UE memory too.
-	Ericsson agrees we should have a single solution with nw and UE sided.  The controllabity should be in the RAN and decodability can be in RAN or OAM.
-	MEdiatek thinks that if we support very big file we should support some stop and start functionality and mobility, like we can support protocol like TCP/IP.  This are long files that can be stored somewhere and we don’t need to specify it.  Anyone can access this server and decode.
-	Nokia thinks that OAM can be a good point from data re-usability perspective.   We should support mobility and a UP like solution is an easy way to support transfer of long file.
-	Kyocera would like to clarify the principle if it is used by the network then we can support termination point in the RAN.
-	ATT would like to ensure that we don’t use UP for the protocol.   Nokia thinks that the agreement doesn’t preclude this discussion.  Ericsson would also like to preclude having a UP solution.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p008`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

提出 RAN 侧 decodability 可按用例配置；所有类型的采集数据都必须在 RAN 具备 identifiability，以便 MNO 控制高效数据传输。另提议向 RAN3 通报 RAN2 关于 SON、MDT 和 AI/ML 数据采集用例的数据消费者与终止点的讨论或协议。

```text
Decodability at the RAN is a configurable parameter depending on the use case. Identifiability at the RAN is a mandatory requirement for all types of collected data, as it enables the MNO to exercise control over efficient data transfer.
Coordination with other WGs (if time allows)
R2-2603835	Discussion on data transfer in 6G	Verizon, Ericsson	discussion	FS_6G_Radio
Proposal 6	Send an LS to RAN3 to inform them about discussions/agreements in RAN2 about data consumers and termination points for SON, MDT and AI/ML data collection use cases, ask them to involve SA WGs in the discussion whenever they deem it is needed.
Transport of collected data [30 min]
Transport methods
R2-2602955	Considerations on RAN2 Data Transfer in 6G	vivo, CAICT, NTT DOCOMO INC., CMCC	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p009`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

UE 与 RAN 间数据传输优先考虑 non-IP 方案，理由是开销较低且不需要 IP routing。潜在方向包括增强型 CP 方案或新 data plane；原文认为 UP-based solution 不适用于 UE-RAN 数据传输。

```text
For the data transfer between UE and RAN, a non-IP solution is preferred due to its lower overhead and the lack of IP routing requirements. Potential directions include:
- Enhanced CP-based solution;
- New data plane (e.g., new protocol layer and new RB type).
- Note: UP-based solution is considered unsuitable for UE-RAN data transfer.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p010`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

UE 与 CN 间数据传输方面，RAN2 应聚焦由 SA2 架构进展触发的 Uu 传输协议，并区分用例特定的 UE-CN 高层协议与低层传输协议。传输协议候选包括 CP、UP 和 new plane；IP 或 non-IP 取决于 SA2 架构。

```text
For the data transfer between UE and CN, RAN2 should focus on the air interface (Uu) transport protocols triggered by the architectural progress in SA2. Specifically, RAN2 should differentiate between the use-case-specific UE-CN protocol (higher layer) and the transport protocols (lower layers), noting that:
- CP, UP, and a new plane are potential candidates for the transport protocols;
- IP or non-IP depends on the SA2 architecture (e.g., IP for UP compatibility; non-IP for non-UP solutions).
R2-2603759	Data Transfer Framework for 6G RAN	AT&T	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p011`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

提出 RAN2 不应采用基于 NR UP 和 NR CP 的数据传输框架，理由是这两种方案均存在已识别的根本性限制。

```text
RAN2 should not adopt a data transfer framework based on NR UP and NR CP, given the fundamental limitations identified for each approach.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p012`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

提出 RAN2 应研究一种新型 radio bearer，支持可配置的 decodability、所有用例下 RAN 侧的 identifiability，以及 QoS differentiation。QoS differentiation 用于支持具有不同数据量和时延要求的数据传输。

```text
RAN2 should study a new type of radio bearer. Such a bearer should:
- support configurable decodability,
- provide identifiability at the RAN for all use cases, and
- support QoS differentiation to enable data transfer with varying volume and latency requirements.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p013`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

RAN2 应研究支持新 radio bearer 所需的机制，例如 logical channels 和 scheduling framework。

```text
RAN2 should study the mechanisms necessary to support the new radio bearer (e.g., logical channels, scheduling framework.
R2-2603210	Considerations on 6G data transfer	CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p014`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

RAN2 研究 DP，以尽量减少对 legacy CP 和 UP 的影响，并支持多种 QoS requirements、灵活的数据交付端点以及大数据量传输。

```text
RAN2 study DP to minimize impacts on legacy CP and UP, and enable the support of various QoS requirements, flexible data delivery endpoints and huge data size for data transfer.
Non-standardized data (if time allows)
R2-2603068	Discussion on data transfer	OPPO	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p015`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

对于 UE-side data collection 的 non-standardized data/vendor specific data，无需在 3GPP system 内引入标准化 data transfer solution。此类数据的传输问题由 UE implementation 解决。

```text
For non-standardized data/vendor specific data for UE-side data collection, there is no need to introduce a standardized data transfer solution within 3GPP system, i.e. it’s up to UE implementation to solve the data transfer issue for non-standardized data/vendor specific data for UE-side data collection.
R2-2603801	Data transfer and Data collection	MediaTek Beijing Inc.	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p016`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

UE-side purpose 的 data collection 要求 fully support vendor-specific data。

```text
Requirement For data collection from the UE for UE-side purpose: collection of vendor-specific data need to be fully supported.
Data transfer framework principles and requirements (if time allows)
R2-2604025	Discussion on data collection and transfer framework	CMCC, NTT DOCOMO, CATT, OPPO, ZTE, Ericsson, vivo, China Unicom, China Telecom	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p017`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

考虑在 Uu interface 上进行 6G data collection 时，应尽可能避免 duplicated data collection and reporting；原文列出数据被多个 consumers 使用及用于不同 use cases 的情形。

```text
The following principle should be considered for 6G data collection over Uu interface:
- The duplicated data collection and reporting should be avoided as much as possible,
- For the data used by multiple consumers
- For the data used for different use cases
R2-2604143	Data Transfer Terminating in RAN for NW-side Data Collection	Nokia	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p018`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

Data transfer solution 应支持根据 use case 相对于其他类型流量（例如 control 和 user traffic）的不同 priority levels。

```text
Add as a requirement that the data transfer solution supports different priority levels depending on use case with respect to other types of traffic, e.g., control and user traffic.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p019`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

Data transfer solution 应支持为每个 data transfer use case 配置不同的 QoS parameters。

```text
Add as a requirement that the data transfer solution supports different QoS parameters for each data transfer use case.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p020`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

研究 RAN2 中 data transfer use cases 应定义哪些 QoS parameters。

```text
Study which QoS parameters should be defined for data transfer use cases in RAN2.
R2-2602955	Considerations on RAN2 Data Transfer in 6G	vivo, CAICT, NTT DOCOMO INC., CMCC	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p021`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

将 UE 与 network 间 data transfer 在 mobility 期间的 continuity 和 lossless transfer 作为必要方面考虑：handover 期间应连续传输且无需重新启动 data transfer procedure，并且不得丢失数据。另提出针对不同 6G use cases 的统一 data collection framework，并在讨论中考虑 duplicated data transfer 问题。

```text
Consider continuity and lossless transfer during mobility for data transfer between UE and network as a necessary aspect:
- Continuity: Ensuring continuous data transfer during handover without re-initiating data transfer procedure;
- Lossless:  no data is lost during handover procedure.
R2-2603044	Discussion on Data Transfer	NEC	discussion	Rel-20	FS_6G_Radio
Proposal-2: RAN2 should aim for a unified data collection framework for different 6G use cases and take duplicated data transfer issue into account during such discussion.
Not treated
R2-2603230	Discussion on data transfer	NTT DOCOMO	discussion
R2-2603288	Discussion on 6G data transfer framework	Futurewei Technologies	discussion	Rel-20
R2-2603308	Data framework in 6G	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2603324	Discussion on data transfer	ZTE  Corporation, Sanechips	discussion	FS_6G_Radio
R2-2603334	Discussion on data transfer for 6G	China Telecom	discussion	Rel-20	FS_6G_Radio
R2-2603366	Discussion on transfer of diverse types of data	1Finity	discussion	Rel-20	FS_6G_Radio
R2-2603397	Considerations for 6G data transfer	Samsung	discussion	Rel-20	FS_6G_Radio
R2-2603403	Discussions on UE Data Collection for Network Use Cases 	Qualcomm Incorporated	discussion	Rel-20
R2-2603415	SK Telecom's views on 6G MDT including lessons learned from 5G	SK Telecom	discussion
R2-2603421	Framework for the transfer of operational data	InterDigital, Inc.	discussion	Rel-20	FS_6G_Radio
R2-2603428	Discussion on Data Transfer Framework for AI/ML in 6G	KT Corp.	discussion	Rel-20	FS_6G_Radio
R2-2603446	Discussion on 6G data transfer	China Unicom	discussion	Late
R2-2603488	Considerations on delivery-relevant information for AI/ML-related data transfer	Hanbat National University	discussion
R2-2603575	Discussion on data transfer framework	Lenovo	discussion
R2-2603624	Discussions on AI/ML Data Transfer Framework	Sony	discussion	Rel-20	FS_6G_Radio
R2-2603737	Discussion on Data Transfer in 6G	CAICT.	discussion	Late
R2-2603891	Discussion on data transfer	Spreadtrum, UNISOC	discussion	Rel-20
R2-2603937	Analysis of Data Transfer	Kyocera	discussion
R2-2603961	Discussion on data transfer	Sharp	discussion	Rel-20
R2-2603982	Discussion on data transfer for 6G	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2604012	Discussion on data transfer for diverse types of data	Transsion Holdings	discussion	Rel-20
R2-2604052	Discussion on 6G data collection and transfer	Google Korea LLC	discussion
R2-2604068	Discussion on data collection and transfer	ETRI	discussion	Rel-20
R2-2604117	Discussion on data transfer in 6G	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p022`

### [6G/Rel-20 RAN2#133bis] `agreement` 9.3.3.1 Data transfer

感知用例的讨论延期；待感知议题在数据特征、终止点等基础方面取得进一步进展后，可重新讨论其对 data transfer framework 的影响。

```text
Postpone discussion on sensing use case. Impact on data transfer framework can be revisited after further progress on fundamental aspects (e.g., data characteristics, termination point(s) etc.) in sensing session.
Size + Latency categories
R2-2601915	Discussion on data transfer in 6G	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.1-a001`

### [6G/Rel-20 RAN2#133bis] `agreement` 9.3.3.1 Data transfer

目前不将 performance monitoring and inference 视为 data transfer。Immediate MDT 暂不属于 data transfer，当前假设其属于 measurement reporting framework。

```text
Performance monitoring and inference is not considered data transfer for now.
Immediate MDT is not part of data transfer as it is assumed to be part of measurement reporting framework for now.
Data consumer, termination point, and decodability
Termination points
R2-2601454	Requirements Analysis and Use Cases of UE as a Consumer	vivo, CAICT, CMCC	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.1-a002`

### [6G/Rel-20 RAN2#133bis] `agreement` 9.3.3.1 Data transfer

至少考虑以下终止点：RAN 侧的 SON、NW-side data collection 和 logged MDT；OAM 侧终止点留空。标准化 UE-side data collection 将在 MNO 设置一个用于可见性的终止点，但具体位置仍待确定；各公司下次会议应说明终止点设在 RAN 的理由。

```text
1	At least the following termination points are considered
RAN – SON,  NW-side data collection, logged MDT
OAM –
2	For standardized UE-side data collection there will be a termination point in the MNO for visibility purposes (according to the requirement).   FFS where termination point is.  Companies next meeting should provide justifications for reason why termination is in the RAN.
Not treated
RAN decodability
R2-2602437	Discussion on data collection and transfer framework	CMCC, China Unicom, NTT DOCOMO, vivo, OPPO	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.1-a003`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.1 Data transfer

Measurement Data transfer framework 应支持总数据量较小或较大、且时延要求较宽松（数十毫秒至数秒）的用例，包括 immediate MDT、continuous learning 的 NW-side data collection 和 sensing。讨论中对 continuous learning、immediate MDT、QoE 及 performance monitoring 是否属于该框架范围存在不同意见。

```text
Measurement Data transfer framework should also support the use cases with the following requirements:
1) small total data size with less relaxed latency (e.g., several tens of msecs to a few seconds), such as: immediate MDT, NW side data collection for continuous learning, sensing.
2) large total data size with less relaxed latency (e.g., several tens of msecs to a few seconds), such as: NW side data collection for continuous learning, sensing.
Noted
R2-2601905	Discussion on data transfer	ZTE  Corporation, Sanechips	discussion	FS_6G_Radio
Proposal 4  The data transfer framework should support the small total data size with less relaxed latency requirement cases (e.g. immediate MDT and the RAN visible measurement report of QoE).
Noted
Discussion
-	Qualcomm thinks data collection for continuous learning is not in scope so we should discuss also why do we need to consider immediate MDT for this framework as we report anything for immediate MDT with L3 measurements.   Samsung has the same understanding and then we’d have to wonder if now we are also including RRM measurements.
-	Oppo, Lenovo and Mediatek thinks Immediate MDT is relaxed as it is triggered by OAM.   Mediatek also thinks QoE is relaxed.
-	LG would like to consider performance monitoring data.   Interdigital thinks that we don’t know how performance monitoring works.  Nokia further points out that performance monitoring and inference are not data transfer.   It is offline training and SON/MDT.   ATT thinks that we can use performance monitoring for re-training.   Qualcomm explains that re-training is data training it is not performance monitoring.  CATT thinks that re-training data is the same as continuous learning.
-	Huawei thinks that the framework should account for less relaxed latency yet.  Xiaomi thinks that we started with the view of understanding the use cases, these doesn’t preclude transferring things with less relaxed requirements in the future.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.1-p001`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.1 Data transfer

对于 NW-side data collection 和 SON/MDT 用例，当 RAN 是 data consumer 时，RAN node 作为 termination point 并解码数据。

```text
For NW-side data collection and SON/MDT use cases, when the RAN is the data consumer, the RAN node acts as the termination point and decodes the data.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.1-p002`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.1 Data transfer

当 OAM 是数据消费者时，应逐跳标识终止点：UE-RAN 数据传输由 RAN 终止，RAN-OAM 数据传输由 OAM 终止。RAN 可以解码数据。

```text
For use cases (e.g., NW-sided data collection, SON, MDT) where the OAM is the data consumer, the termination point should be identified on a hop-by-hop basis (e.g., UE-to-RAN and RAN-to-OAM).
-	RAN is the termination point for UE-RAN data transfer.
-	OAM is the termination point for RAN-OAM data transfer.
-	RAN can decode the data.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.1-p003`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.1 Data transfer

UE-side data collection 由 UE server 消费时，端到端方案需要与 SA WGs 协调；UE-CN_NF 数据传输的终止点至少包括 CN NF，具体 NF 尚未确定，且 CN NF 可解码数据以核验或匹配请求数据与上报数据。经 OAM 转发的 UE-RAN 数据传输可由 RAN 终止；RAN 是否作为可解码节点应根据传输数据特征确定。

```text
For UE-side data collection where the UE server is the data consumer, coordination with SA WGs (e.g., SA2, SA5) on the E2E solution is required. The requirements of data transfer include:
-	The termination point at least includes the CN NF (specific NF is FFS) for UE-CN_NF data transfer.
	The radio bearer terminates in the RAN, and RAN provides data forwarding functions.
	The CN NF can decode data to verify or match the requested data against the reported data.
-	The termination point can be RAN for UE-RAN data transfer, when the UE-side data collection is transferred via OAM.
-	Whether the RAN node acts as a decodable node should be determined on the characteristics of the transferred data.
-	Qualcomm wonders why the RAN needs to have visibility on UE sided data.
Noted
R2-2601511	Service-based Data Transfer Framework	Xiaomi, Apple, InterDigital	discussion	Rel-20	FS_6G_Radio
Proposal 1b: As least the following termination points (i.e., the entity with service-specific protocol(s)) can be supported:
•	SON/MDT: RAN (SON) /OAM (logged MDT)
•	AI/ML: RAN/OAM for NW-side data collection, UE server (if within MNO) for UE-side data collection (FFS other entity in CN or outside of RAN)
•	Sensing: termination point and data consumer postponed until further progress in sensing agenda.
Proposal 1c: The entity with service-specific protocol(s) has the visibility of the data.
Noted
R2-2601875	Discussions on 6G Data Collection 	Qualcomm Incorporated	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.1-p004`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.1 Data transfer

对于网络用途的 UE data collection，仅当报告对 Uu 操作和 RAN 优化至关重要时，才将 RAN 视为终止实体，例如 immediate MDT、RVQoE 和 SON reports。此做法也有助于降低 UE AS 的数据收集内存需求，同时提供有意义的报告。

```text
For UE data collection for network use cases, the RAN is considered the termination entity only if
-	A report is critical for Uu operations and RAN optimizations (e.g., immediate MDT, RVQoE, SON reports)
This also helps in reducing UE AS memory requirements for data collection while providing meaningful reports
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.1-p005`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.1 Data transfer

条目按 SON、Logged MDT、Immediate MDT、QoE、RVQoE 和 NW-side data collection 分别列出了 consumer、termination entity 和 decodability；其中 Logged MDT 与 QoE 的终止实体为 OAM domain 中的 DCF，RVQoE 的终止实体为 RAN。讨论记录了关于数据是否应在 RAN 或 OAM 终止、解码负担、可见性与可解码性的关系及安全性的不同意见。

```text
For different data types for the network use cases, consider the consumers, termination entity, and decodability as follows:
-	SON reports: consumer: RAN, OAM; termination entity: RAN (if SON optimization is agreed to be supported by RAN nodes in 6G) or DCF (in OAM domain) [if SON optimizations are performed by OAM in 6G]; decodability: RAN, OAM
-	Logged MDT report: consumer: OAM; termination entity: DCF (in OAM domain); decodability: OAM
-	Immediate MDT reports: consumer: RAN, OAM; termination entity: RAN; decodability: RAN, OAM
-	QoE: consumer: OAM; termination entity: DCF (in OAM domain); decodability: OAM
-	RVQoE: consumer: RAN; termination entity: RAN; decodability: RAN
-	NW-side data collection: consumer: RAN, OAM; termination entity: DCF (in OAM domain); decodability: RAN, OAM.
Noted
Discussion
-	ATT thinks that RAN3 didn’t agreed that it can be stored in OAM.   Xiaomi explains that RAN3 is only dealing with
-	Nokia thinks that if the NW-side data collection ends in the RAN there is the burden to decode.   Huawei thinks that we have gNB centric and the RAN should received it.  Qualcomm thinks it should go to OAM and if the RAN wants it can get it back.   ZTE doesn’t agree, it should be RAN if the RAN needs it.   Also logged MDT should be in the RAN.  Samsung agrees logged MDT should be in the RAN.
-	Xiaomi thinks that there is no protocol between the UE and OAM so RAN is a termination point.
-	Qualcomm thinks that we want to simplify and not have to use AS memory.
-	Nokia is concerned that the aNB needs to decode everything.  Huawei explains that they are just visible it is up to network implementation to decode or just forward transparently.
-	Mediatek thinks that the RAN does UE selection.
-	Huawei asks if we should provide the path.
-	Xiaomi, Apple, Lenovo, Qulacomm, has very strong concern about RAN being a termination point for security reasons.
-	CMCC thinks that for RAN based use cases we would like to share the UE sided data for training for NW-sided training.   ZTE agrees and the measurement based information doesn’t need to be secure but other information can be re-considered.   Ericsson also has the same view on the benefit.   Xiaomi doesn’t agree as from reporting point of view it will be quite different, as for UE sided collection the actual collection of data is up to UE implementation and for nw sided it is configured by the network.   And there are concerned that if the data is sent to RAN they can be shared with other UEs.
-	MEdiatek sees some benefit for the control part of RAN involvement but no strong reason for re-usability.   And for standardized data don’t see a big problem with security aspects.  It would be beneficial to have similar things with some commonality.
-	Nokia agrees that RAN should have the controllability.   It’s ok to be outside the RAN, the OAM can use the data for NW sided use cases.
-	Xiaomi thinks we need to clarify whether visibility and decodability are the same.
-	Qualcomm explains that the RAN selects the UE but for UE sided the UE decides.  Also for NW sided we need to meet the RAN4 requirements, but for UE sided we don’t need to and can be more relaxed.
-	Verizon asks what is outside of RAN.   Xiaomi explains it could a new server within MNO, OAM, and data repository (RAN3 is discussing this options).
-	Nokia thinks it would be helpful to see actual solutions on how it would look like if terminated in RAN, CN, OAM.   Qualcomm agrees that we can start looking at the solutions.    Also look at the pain points.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.1-p006`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.1 Data transfer

在 RAN 作为消费者的用例中，数据应对 RAN node 可见且可解码，包括模型训练位于 RAN 的 NW-side data collection、SON、Immediate MDT 和 RAN visible QoE。

```text
For the following use cases where RAN as consumer, the data should be visible and decodable by RAN node.
- NW side data collection where model training resides at RAN (e.g. Beam management, CSI prediction, CSI compression, AI Mob)
- SON (e.g. MRO, RACH Optimization)
- Immediate MDT (e.g. measurement results)
- RAN visible QoE (e.g. Buffer level, playout delay for media start-up)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.1-p007`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.1 Data transfer

在 OAM 作为消费者的用例中，数据也可以对 RAN 可见且可解码，包括模型训练位于 OAM 的 NW-side data collection、SON、Logged MDT 和 Immediate MDT。

```text
For the following use cases where OAM as consumer, the data can also be visible and decodable by RAN.
- NW side data collection where model training resides at OAM (e.g. Beam management, CSI prediction, CSI compression, AI Mob)
- SON (e.g. MRO, RACH Optimization)
- Logged MDT (e.g. cell measurements)
- Immediate MDT (e.g. L1/L3 measurement results)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.1-p008`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.1 Data transfer

对于 OTT server 作为消费者的 UE-side data collection，由于同一数据也用于 RAN 中的 NW-side model training，数据可以对 RAN node 可见且可解码，并可经 CN/OAM 从 RAN node 共享给 UE-side OTT server。另有提议指出，终止点不是消费者时通常不可解码，但 OAM 消费 SON/MDT 且复用 RRC 是例外。

```text
For UE side data collection where OTT server as consumer, the data can be visible and decodable by RAN node, since the same data is also used for NW-side model training in RAN. The data can be shared to UE-side OTT server via CN/OAM from RAN node.
R2-2601839	Views on 6G Data Transfer	Apple	discussion	Rel-20	FS_6G_Radio
Proposal 1 From RAN2 perspective, when the termination point is not the data consumer, the data transfer is generally not decodable at the termination point, with the following exception:
- RRC is reused for SON/MDT data transfer with OAM as consumer
Not treated
Data transfer
Transport protocols
R2-2601511	Service-based Data Transfer Framework	Xiaomi, Apple, InterDigital	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.1-p009`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.1 Data transfer

各服务支持的传输方式应考虑服务特定数据特征，例如 latency 和 total data size；RAN2 讨论服务特定协议下方的子层选项，包括 CP-based、UP-based 和必要时的 new plane-based。另有提议主张为不同 6G 用例采用统一的数据收集框架。

```text
The supported transport for each service shall consider the service-specific data characteristics (e.g., latency and total data size). RAN2 to discuss the sublayer options underneath service-specific protocol(s) for different types of data:
- Option 1. CP-based: PHY/MAC/RLC/PDCP(/RRC);
- Option 2. UP based: PHY/MAC/RLC/PDCP(/SDAP);
- Option 3. New plane based (if needed): PHY/MAC/RLC/PDCP(/SDAP)/new sublayer (e.g., IP/non-IP either in RAN or CN);
- NOTE: The need of SDAP is up to user plane discussion.
Unified vs. service specific protocol (if time allows)
R2-2601593	Discussion on Data Transfer	NEC	discussion	Rel-20	FS_6G_Radio
Proposal-2: RAN2 should aim for a unified data collection framework for different 6G use cases which require data collection.
R2-2602283	Discussion on data transfer in 6G	Verizon, Ericsson	discussion	Rel-20	FS_6G_Radio
Proposal 1	A common framework is used for data collection over the air interface for network-side and UE-side AI/ML data collection and for monitoring of network performance (e.g. logged MDT and SON).
R2-2601511	Service-based Data Transfer Framework	Xiaomi, Apple, InterDigital	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.1-p010`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.1 Data transfer

AI/ML、sensing 和 SON/MDT 使用 service-specific protocols；服务的数据处理和控制信令分别在对应的 service-specific protocol 中定义。

```text
Service-specific protocols are used to define AI/ML, sensing and SON/MDT, e.g., Data processing  and control signalling of a service are defined independently in the corresponding service-specific protocol.
Not treated
Data Transfer Requirements (if time allows)
R2-2602437	Discussion on data collection and transfer framework	CMCC, China Unicom, NTT DOCOMO, vivo, OPPO	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.1-p011`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.1 Data transfer

6G data collection over Uu interface 应考虑避免重复的数据收集和上报，并涵盖数据被多个消费者使用或用于不同用例的情况。

```text
The following principle should be considered for 6G data collection over Uu interface:
- The duplicated data collection and reporting should be avoided as much as possible,
- For the data used by multiple consumers
- For the data used for different use cases
R2-2602293	Data transfer terminology and use of the user plane	Nokia, T-Mobile USA	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.1-p012`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.1 Data transfer

将 data collection and transfer 的 controllability 定义为 MNO 能够启动、停止或调节 data transfer traffic 流量，并启用或禁用 data collection measurement resources（例如 reference signals）的能力。

```text
Define controllability of data collection and transfer as the ability for the MNO to start, stop or modulate the flow of data transfer traffic and to enable or disable data collection measurement resources such as reference signals.
R2-2601454	Requirements Analysis and Use Cases of UE as a Consumer	vivo, CAICT, CMCC	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.1-p013`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.1 Data transfer

提议将 UE 与 network 间 data transfer 在 mobility 期间的 continuity 和 lossless transfer 作为额外方面：continuity 指 handover 期间无需重新发起 data transfer procedure 即可持续传输，lossless 指传输过程中不丢失数据。该提议标记为 Not treated。

```text
Consider continuity and lossless transfer during mobility for data transfer between UE and network as an additional aspect:
-	Continuity: Ensuring continuous data transfer during handover without re-initiating data transfer procedure;
-	Lossless:  no data is lost during data transfer procedure.
Not treated
R2-2601568	Dicussion on data transfer framework	DOCOMO Beijing Labs	discussion
R2-2601647	Considerations for 6G data transfer	Samsung	discussion	Rel-20	FS_6G_Radio
R2-2601676	Considerations on 6G data transfer	CATT	discussion	Rel-20	FS_6G_Radio
R2-2601690	Discussion on Data transfer	LG Electronics Finland	discussion	Rel-20	FS_6G_Radio
R2-2601719	Discussion on transfer of diverse type of data	1Finity	discussion	Rel-20	FS_6G_Radio
R2-2601730	Discussion on data transfer in 6G	CAICT.	discussion
R2-2601749	6GR Data framework	Lenovo	discussion
R2-2601754	Discussion on data transfer	OPPO	discussion	Rel-20
R2-2601819	Data transfer	Futurewei Technologies	discussion	Rel-20
R2-2601864	Data transfer in 6G	Ofinno	discussion
R2-2601983	Discussion on data transfer for 6G	China Telecom	discussion	Rel-20	FS_6G_Radio
R2-2601996	Framework for the transfer of operational data	InterDigital	discussion	Rel-20	FS_6G_Radio
R2-2602055	Consideration on RAN decodability for AI/ML related data	Hanbat National University	discussion	Rel-20
R2-2602077	Discussion on data transfer and data collection for 6G	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2602103	Discussion on data transfer	Spreadtrum, UNISOC	discussion	Rel-20
R2-2602165	Discussions on AI/ML Data Transfer Framework	Sony	discussion	Rel-20	FS_6G_Radio
R2-2602239	Discussion on AI/ML related data transfer	Transsion Holdings	discussion	Rel-20
R2-2602349	Discussion on AI-ML, ISAC, SON/MDT, QoE data transfer	Rakuten Symphony	discussion	Rel-20
R2-2602373	Considerations for a Data Transfer Framework for 6G RAN	AT&T	discussion	FS_6G_Radio
R2-2602497	Analysis of Data Transfer	Kyocera	discussion
R2-2602528	Discussion on 6G data collection and transfer	Google Korea LLC	discussion
R2-2602555	Discussion on data transfer	ETRI	discussion	Rel-20
R2-2602571	Discussion on data transfer	Sharp	discussion	Rel-20
R2-2602585	Data transfer and Data collection	MediaTek USA	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.1-p014`

### [6G/Rel-20 RAN2#133] `agreement` 10.3.3.1 Data transfer and model transfer

数据传输框架应至少支持两类用例：总数据量大且时延要求宽松，以及总数据量小且时延要求宽松。总数据量按 UE 累积存储的数据与最小 UE AS buffer 比较，区分为 Large 和 Small。

```text
Definitions/categories when we talk about use cases
Latency:
	relaxed (e.g., minutes, hours, days, or no latency requirement) (e.g. UE and NW sided data collection)
 	less relaxed (e.g., several tens of msecs to a few seconds)
Total data size per UE (accumulated data that the UE has to store):
-  Large: Larger than minimum UE AS buffer
-  Small: Smaller than minimum UE AS buffer
Data transfer framework should support at least the use cases with the following requirements:
-	large total data size with relaxed (e.g., minutes, hours, days, or no latency requirement) latency requirements (e.g. UE and NW sided data collection, logged MDT)
-	small total data size with relaxed (e.g., minutes, hours, days, or no latency requirement) latency requirement (e.g. MDT/SON, NW sided data collection)
Consumer/end points
R2-2600616	Discussions on data transfer and model transfer	NTT DOCOMO, INC.	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-a001`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

提议 RAN2 认可两个定义：‘termination point’ 是 UE 与 NW entity 间 E2E data transfer transport protocol stack 的端实体；‘data consumer’ 是可处理所收集数据的实体，可位于 MNO 内部或外部。数据应仅由 data consumer 解码和处理。

```text
RAN2 to endorse the below definition of ‘termination point’ and ‘data consumer’:
-	‘Termination point’ is the end-entity of E2E data transfer transport protocol stack between UE and NW entity.
-	‘Data consumer’ is the entity (either inside or outside of MNO) that can process the collected data. Data should only be decoded and processed by data consumer.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p001`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

QoS 特征分析区分 ‘Non-real time’ 与 ‘Real-time’：前者允许先累积数据再上报，后者要求立即向网络上报。数据量分为 UE 可累积的 ‘Accumulated data size’，以及考虑数据相关性、需在同一报告中一起上报的最小 ‘One-shot report data size’。

```text
The analysis of QoS characteristics considers the following aspects with clarification:
-	‘Non-real time’ means the collected data can be ‘accumulated and then report’ to network;
-	‘Real-time’ means the collected data needs to be reported to network immediately;
-	Data volume considers the following two types:
	Accumulated data size: The data size that can be accumulated by UE.
	One-shot report data size: The minimum data size that needs to be reported together in the same report, considering correlation among the collected data.
Noted
R2-2600084	Discussion on data transfer and model transfer	vivo, NTT DOCOMO INC., CAICT	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p002`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

提出进一步明确时延类别、termination points 和 RAN 对标准化数据内容的可见性，并将移动性期间的连续性与无损传输作为数据传输的附加方面；相关定义包括切换期间不重新启动传输过程，以及传输过程中不丢失任何数据位。该条目记录为 Not treated。

```text
For the requirements of data transfer:
-	Further clarify the definitions of latency requirement includes:
	Relaxed latency (or non-real-time): minutes, hours, days, or no specific latency requirement;
	Near-real-time: several tens of msecs to a few seconds.
-	Further clarify the termination points refer to the sending and receiving nodes within 3GPP scope and with full visibility of the data.
-	Further clarify that decodable by RAN refers to full visibility for standardized data content.
-	Consider continuity and lossless transfer during mobility for data transfer between UE and network as an additional aspect:
	Continuity: Ensuring continuous data transfer during handover without re-initiating data transfer procedure;
	Lossless:  not a single bit of data is lost during data transfer procedure.
-	Data transfer requirements should be updated as relevant use cases advance in other working groups.
Noted
Discussion on data consumer
-	‘Data consumer’ is the entity (either inside or outside of MNO) that can process the collected data. Data should can be decoded and processed by data consumer.
-	ATT and CMCC thinks that we can have multiple consumers for example we can have the same data to make the same decision.   CMCC explains L3 measurements can be use for different purposes.   Use the consumer that consumes not process.   Also data can be be decoded by other entity.
Discussion on terminations
-	‘Termination point’ is the end-entity of E2E data transfer transport protocol stack between UE and NW entity.
-	Further clarify the termination points refer to the sending and receiving nodes within 3GPP scope and with full visibility of the data.
-	Apple thinks it is an intermediate node.   Samsung thinks that there are cases where the intermediate node doesn’t have visibility like QoE for example.
-	ZTE thinks that we can have several termination points.   The entity that forwards the data is not a termination point.
-	Interdigital thinks that intermediate node can be a data consumer if it needs visibility.
-	Nokia thinks what really matters here is whether the gNB can decode the data or not and where the data needs to go.    The data will always initially terminate in gNB.
-	Vivo emphasizes that the termination point is where the data is visible.     For the node transparently forwarding the data are not termination point.
-	Huawei thinks that if the consumer is the UE server then there is value to discuss about termination point.
-	Oppo thinks that first termination point
Not treated
Requirements (e.g., controllability, visibility, security etc.) (if time allows)
R2-2601128	6GR Data framework and model transfer	Lenovo	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p003`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

提出适用于 AIML、sensing、SON/MDT 和 QoE 等应用及 UE-side、NW-side 数据收集的基线要求，包括保障数据安全、完整性和机密性，尊重用户隐私、匿名性与同意，并由 MNO 全面控制标准化数据收集传输过程且具备标准化数据的完全可见性。还要求设计可扩展，并尽量减少对 UE 电池、处理、内存、用户流量传输及省电功能的影响。

```text
The following baseline requirements apply to all applications (AIML, sensing, SON/MDT, QoE), including data collected at the UE-side and the NW-side.
-	The data collected is secured and data integrity and confidentiality for that data is ensured.
-	User data privacy, anonymity and user consent is respected.
-	The MNO has full control of the standardized data collection transfer process and can manage data transfer to the server for data collection, without the need of Service Level Agreement (SLA) for this purpose (This includes initiating, terminating, and fully managing data transfer).
-	MNO has full visibility for standardized data.
-	The design is future-proof and extendable.
-	The data collection should minimize impact to the UE battery, UE processing and memory utilization.
-	The data collection should minimize impact to user traffic transmission and power saving features
Design principles (if time allows)
R2-2600084	Discussion on data transfer and model transfer	vivo, NTT DOCOMO INC., CAICT	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p004`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

RAN2 研究数据传输方案时，应避免重复收集可由 RAN 利用的数据，并使其可由 RAN nodes 解码。方案还应支持单次或多次报告中从 tens of Kbits 到 several Gbits 的数据量、从 msecs 到 days（或无时延要求）的时延范围，并提升数据传输效率。

```text
RAN2 studies data transfer solutions based on at least the following principles:
-	Avoid duplicated data collection, the data can be utilized by RAN (e.g., MDT, NW-side data collection, etc.)  should be decodable by RAN nodes.
-	Supporting various data sizes, data volume could range from tens of Kbits to several Gbits in a single or multiple report
-	Supporting various latency requirements, latency ranging from msecs to days (or no latency requirement), starts with relaxed or near-real-time latency.
-	Improve data transfer efficiency, to eliminate unnecessary protocol functions and improve data transmission efficiency.
R2-2601020	Unified, Flexible and Intelligent Data Transfer Framework and Architecture for 6G Various Data Services	LG Electronics Inc.	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p005`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

RAN2 旨在设计统一框架和架构，以管理 6G 中 AI/ML、Sensing、SON/MDT、QoE 及未来新兴服务的各种数据类型。

```text
RAN2 aims to design a unified framework and architecture that can manage 6G various types of data such as AI/ML, Sensing, SON/MDT, QoE and future emerging services.
Data Transfer framework
QoS characteristics
R2-2600538	Discussion on data transfer and model transfer in 6G	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p006`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

提议按每报告的数据大小和时延定义数据特征类别：large 为大于 9 kB，small 为不大于 9 kB；时延类别为 relaxed（分钟、小时、天或无时延要求）和 near-real-time（数十毫秒至数秒）。该条目记录为 Noted。

```text
RAN2 to define some categories for data characteristics, such as:
- Typical message size:
	large. It refers to data size per report>9 kB
	small. It refers to data size per report<=9 kB
-	Huawei explains that this is a PDCP size limitation.  Qualcomm thinks that this size only matters for CP not UP.   Oppo thinks L2 PDU size limitation.
- Latency:
	relaxed (e.g., minutes, hours, days, or no latency requirement)
	near-real-time (e.g., several tens of msecs to a few seconds)
Noted
R2-2601018	Framework for the transfer of operational data	InterDigital	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p007`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

数据传输框架应支持高数据量（例如最高 hundreds of MB）与宽松时延（例如分钟至小时），至少以 RAN 和 UE-side server 为端点。

```text
Data transfer framework shall support high volume (e.g., up to hundreds of MB) with relaxed latency (e.g., minutes to hours). At least RAN and UE-side server are end points.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p008`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

数据传输框架应支持低数据量（例如最高 several hundred kB）与较低时延（例如 100ms 至数秒），至少以 RAN 和 OAM 为端点。该条目记录为 Noted。

```text
Data transfer framework shall support low volume (e.g., up to several hundred kB) with lower latency (e.g., 100ms to seconds). At least RAN and OAM as end points.
Noted
Discussion
-	Vivo thinks that discussion on relaxed are important.
-	Qualcomm thinks that total size should also be taken into account and that should be defined on total UE buffer.   Less than UE buffer and large if it is more than UE buffer.
-	Lenovo asks what is the purpose of the large data size – Qualcomm explains that it is just to understand whether there would be segmentation or not.
-	Xiaomi thinks that we have one shot data for example data sample for beam management. That defines if the data needs to be segmented or not.  Then we have accumulated data and that is use to determine whether the UE can store all the accumulated data.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p009`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

RAN2 采纳 Table 1 用于 data transfer 分析。

```text
RAN2 to adopt Table 1 for data transfer analysis.
Noted
R2-2600839	Discussions on Data Collections in 6G	Qualcomm Incorporated	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p010`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

请求 RAN2 考虑 Table 1，用于分析 AI/ML Data 数据收集的不同方面，包括 QoS requirements、termination entities、consumers 和 RAN decodability。

```text
RAN2 is requested to consider Table 1 for different aspects of data collection (e.g., QoS requirements, termination entities, consumers, decodability at the RAN) for AI/ML Data.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p011`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

请求 RAN2 考虑 Table 2，用于分析 SON、MDT 和 QoE Data 数据收集的不同方面，包括 QoS requirements、termination entities、consumers 和 RAN decodability。

```text
RAN2 is requested to consider Table 2 for different aspects of data collection (e.g., QoS requirements, termination entities, consumers, and decodability at the RAN) for SON, MDT, and QoE Data.
Noted
R2-2600500	Views on data transfer and model transfer	ZTE  Corporation, Sanechips	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p012`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

对于给定的数据源和数据消费者，可能存在多个 termination point 组合；数据传输路径上不透明转发数据的中间节点（例如处理或重新格式化数据）也可视为 termination node。RAN2 暂定将 data consumer 定义为可消费、解码和处理所收集数据的实体，将 termination point 定义为 UE 与 NW 之间端到端数据传输协议栈中、可按需解码数据以供查看的网络实体。

```text
For a given data source and data consumer, there may be multiple termination point combinations. In addition to the data source and data consumer, the intermediate node on the data transfer path which is not transparently forwarding the data (e.g. process or reformat the data) can be regarded as termination node.
Noted
| Terminology and guidance Terminology to consider to use for now from RAN2 point of view - ‘Data consumer’ is an entity (either inside or outside of MNO) that can consume the collected data. Data can be decoded and processed by data consumer. NOTE: assumptions is that there can be more than one data consumer. - ‘Termination point’ is the network entity of E2E data transfer transport protocol stack between UE and NW. This termination point is within the 3GPP scope and can decode the data for visibility purposes (when needed). The decodability can be discussed on a case by case basis. For next meeting companies, for different use cases can determine the data consumer and termination point or which node needs to decode the data. The data transfer framework will support at least the following data consumers - FFS termination points (including where visibility is required) RAN: NW-sided data collection, SON, immediate MDT OAM: NW-sided data collection, SON/MDT UE server: UE sided data collection |
| --- |
Not treated
RAN decodability
R2-2601128	6GR Data framework and model transfer	Lenovo	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p013`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

通过 data transfer framework 收集的数据不一定需要由 RAN 解码；当 RAN 是数据消费者时例外。

```text
Data collected as part of the data transfer framework is not necessarily required to be decodable by RAN, except for the cases in which RAN is the consumer of the data.
R2-2600893	On Decodability of AI/ML Data in 6G RAN	AT&T	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p014`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

6G RAN 节点可以配置为解码收集后以其他实体为终止点的数据。

```text
6G RAN nodes can be configured to decode data collected for termination at other entities.
Enhancements for data transfer (if time allows)
R2-2600268	Discussion on Data Collection	NEC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p015`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

RAN2 应研究采用哪种 data transfer 方案：增强 control plane、增强 user plane，或新方案（例如 new data plane、new entity/protocol layer 或 new RB）。

```text
RAN2 should study which solution to be adopted for data transfer:
- enhanced control plane
- enhanced user plane
- new solution (e.g., new data plane, new entity/protocol layer, new RB)
Not treated
Model transfer
R2-2600616	Discussions on data transfer and model transfer	NTT DOCOMO, INC.	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p016`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

6G 中的 model transfer 应满足 awareness 和 controllability 要求：MNO 可获知模型存在，并能控制模型传输/交付流程，包括启动、暂停、恢复和停止。

```text
In 6G, the model transfer should follow requirements:
•	Awareness: MNO can be aware of the existence of model.
•	Controllability: MNO can control the model transfer/delivery procedure (initiate, suspend, resume, stop etc.).
R2-2600780	Discussion on data transfer and model transfer in 6G	Verizon, Ericsson	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p017`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

网络应能够控制从 UE-side training server 到 UE 的模型传输/交付。RAN2 应与其他 WGs 协调，研究实现方式。

```text
It should be possible for the network to control the model transfer/delivery from the UE-side training server to the UE. RAN2 to study ways to achieve this in coordination with other WGs
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p018`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

RAN2 应识别数据收集和模型传输中属于其他工作组范围的方面，并在 6G 研究早期与相关工作组协调。

```text
RAN2 to identify which data collection and model transfer aspects pertain to the scope of other working groups and coordinate with the relevant groups at an early stage of the 6G study.
R2-2600839	Discussions on Data Collections in 6G	Qualcomm Incorporated	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p019`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

认为无需定义 model transfer/delivery 的要求，现有 UE 软件更新方式可复用于向 UE 传输或交付供 UE inference 使用的模型。

```text
No need to define requirements for model transfer/delivery, as existing means to update the “UE” software can be reused for model transfer/delivery to the UE for UE inference.
R2-2600125	Consideration on data transfer and model transfer	Xiaomi	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p020`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

UE-side OTT server 向 UE device 传输已训练的 UE-side model 不属于 3GPP 范围。RAN2 等待 RAN1 对 6G AI/ML use cases 的研究，以确认是否需要支持将 RAN-generated model（如 constellation diagram/precoding matrix）从 RAN 传到 UE。

```text
Model transfer of trained UE-side model from UE-side OTT server to UE device is out of 3GPP scope. RAN2 waits for RAN1 6G AI/ML use cases study on the need of supporting transferring RAN-generated ‘model’ (e.g., constellation diagram/precoding matrix) from RAN to UE.
Not treated
R2-2600065	Discussion on data and model transfer	OPPO	discussion	Rel-20
R2-2600114	Consideration on 6GR data transfer and AI/ML framework	Xiaomi	discussion	Rel-20	FS_6G_Radio	Withdrawn
R2-2600115	Unnecessary standardized model transfer and delivery	Xiaomi	discussion	Rel-20	FS_6G_Radio	Withdrawn
R2-2600194	Considerations on 6G data transfer	CATT	discussion	Rel-20	FS_6G_Radio
R2-2600267	Discussion on Data Transfer for 6G RAN	TCL	discussion	Rel-20	FS_6G_Radio
R2-2600353	Discussion on AI/ML Data transfer and model transfer	Fujitsu	discussion	Rel-20	FS_6G_Radio
R2-2600359	Considerations for 6G data and model transfer	Samsung	discussion	Rel-20	FS_6G_Radio
R2-2600369	6GR Data framework and model transfer	Lenovo	discussion
=> Revised in R2-2601128
R2-2600407	Consideration on RAN decodability for AI/ML data and model transfer	Hanbat National University	discussion
R2-2600467	Views on 6G data transfer and model transfer	Apple	discussion	Rel-20	FS_6G_Radio
R2-2600489	Discussion on data transfer for 6G	China Telecom	discussion	Rel-20	FS_6G_Radio
R2-2600500	Views on data transfer and model transfer	ZTE  Corporation, Sanechips	discussion	FS_6G_Radio
R2-2600505	Discussion on data transfer and data collection for 6G	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2600617	Discussion on data transfer and model transfer	Sharp	discussion	Rel-20
R2-2600662	Discussion on data transfer and model transfer	Spreadtrum, UNISOC	discussion	Rel-20
R2-2600863	Data framework in 6G	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2600886	On training data collection and model transfer	Nokia	discussion	Rel-20	FS_6G_Radio
R2-2600891	On QoS Differentiation Framework for AI/ML Data in 6G RAN	AT&T	discussion	FS_6G_Radio
R2-2600906	Data transfer and model transfer	MediaTek USA	discussion	FS_6G_Radio
R2-2600917	Model Transfer and Feedback Procedure for 6G AIML Framework	Jio Platforms	discussion	Rel-20	FS_6G_Radio	R2-2508775
R2-2600952	Discussion on data collection and transfer framework	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2600967	Analysis of Data Transfer and Model Transfer	Kyocera	discussion
R2-2600968	Discussion on data transfer and model transfer	Futurewei Technologies	discussion	Rel-20
R2-2600990	Discussion on AI-ML, ISAC, SON/MDT, QoE data transfer	Rakuten Mobile, Inc	discussion	Rel-20
R2-2601015	Discussion on connectivity for data transfer	ETRI	discussion	Rel-20
R2-2601021	Discussion on 6G data collection	Google Korea LLC	discussion
R2-2601051	Considerations on 6GR Model Transfer	CAICT	discussion	Late
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p021`

### [6G/Rel-20 RAN2#132] `agreement` 10.3.3.1 Data transfer, model transfer, and AIML

作为起点，研究非实时数据类型，包括用于 offline training 的 AI/ML data collection、SON/MDT、QoE 和 sensing，并讨论 QoS 类别及数据传输端点。还需了解数据消费者及数据是否必须由 RAN 解码；部分 QoS 细节取决于其他 WGs。

```text
Study the follow aspects as a starting point:
Data types (non-real time)
-	AI/ML (data collection for offline training)
-	SON/MDT, QoE - (details on what is included in 6G depends on RANP)
-	Sensing (the detailed characteristics (including what cases are real time or not) will be discussed in later phase, after some RAN1 and RAN2 discussions in the sensing session)
QoS (e.g. data volume and latency)
-	Define some categories we want to base our discussion on.   Details of QoS for some cases may depend on other WGs.
Termination points (impacted group)
-	UE to RAN
-	UE to CN
-	UE to OAM
-	UE to UE server
Understand the consumer (may be different than the termination) of the data and whether data has to be decodable by RAN.
Data transfer framework [40 min]
Requirements/principles for data transfer framework
R2-2508335	6GR Data transfer and AIML framework	Lenovo	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-a001`

### [6G/Rel-20 RAN2#132] `observation` 10.3.3.1 Data transfer, model transfer, and AIML

5G 基于 CP 的 data transfer framework 不适合支持大数据量，并存在降低现有 essential CP signaling 性能的风险。

```text
5G data transfer over CP-based framework is not suitable to support large volume of data and has the risk of degrading the existing essential CP signaling.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-o001`

### [6G/Rel-20 RAN2#132] `observation` 10.3.3.1 Data transfer, model transfer, and AIML

5G 基于 UP 的 data transfer framework 会不必要地经过 UPF，且在需要时 gNB 无法参与数据传输和管理。此外，UP 上的数据传输终止于不受 3GPP 控制的 application layers。

```text
5G data transfer over UP-based framework has to go through UPF unnecessarily and gNB cannot be involved for data transfer and management (when needed). Besides, the data transfer over UP is terminated in application layers which are not in control of 3GPP.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-o002`

### [6G/Rel-20 RAN2#132] `observation` 10.3.3.1 Data transfer, model transfer, and AIML

5G 数据传输最终引入了多种框架，以支持不同数据类型。

```text
5G data transfer ended up introducing diverse frameworks to support various data types.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-o003`

### [6G/Rel-20 RAN2#132] `observation` 10.3.3.1 Data transfer, model transfer, and AIML

针对可能需要 RAN2 评估的 6GR 新 AI/ML 用例，方法应定义一致的指标，以相对于 6GR non-AI/ML baselines 量化 AI/ML 功能的复杂度和能耗。

```text
For the study of new AI/ML use cases for 6GR that may require evaluation by RAN2, the methodology should define consistent metrics to quantify the complexity and energy consumption of AI/ML features against 6GR non-AI/ML baselines
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-o004`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.1 Data transfer, model transfer, and AIML

以 5GNR 中 AI/ML 数据的 size、latency 和 frequency 假设作为 6GR AI/ML 数据传输的 baseline，并将 Table 1 作为数据类型研究起点。NW-side training、inference 和 monitoring 数据分别参考 data collection framework、measurement/CSI framework 等基线，具体特征和适用框架依数据类型或用例讨论。

```text
For AI/ML data, assumption on data size/latency/frequency used in 5GNR can be considered as baseline for 6GR AI/ML data transfer. RAN2 considers Table 1 as starting point for AI/ML data types study, including:
-	For NW-side training data collection and transfer, data collection framework is considered as baseline and consider the following characteristics:
o	For logging data: low priority, delay tolerant/relaxed latency, low PER, large MDBV;
o	For non-logging data: medium priority, medium delay/near-real-time, low PER, medium MDBV;
-	For inference data collection and transfer, at least for AI/ML based BM/CSI/Mobility, measurement framework and/or CSI framework is considered as baseline. New use cases need to be discussed case by case;
-	For monitoring data collection and transfer, whether measurement framework/CSI framework or data collection framework needs to be discussed case by case and consider the following characteristics:
o	Medium priority, medium delay/near-real-time, low PER, medium MDBV.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-p001`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.1 Data transfer, model transfer, and AIML

Sensing data 的 metrics、size 和 reporting frequency 等待 RAN1 对 measurement metrics 的进一步输入；Table 2 和 Table 3 分别作为 sensing data collection/transfer 及不同 sensing 服务用例 QoS 特性的研究起点。Sensing data producer 为 UE，处理或结果计算实体为 SF（位于 RAN 或 CN）。

```text
For Sensing Data:
-	Data metrics, data size, and reporting frequency, RAN2 needs to wait for further input from RAN1 evaluation on measurement metrics;
-	RAN2 considers Table 2 as starting point for sensing data collection and transfer study, and focuses on the data transfer framework where sensing data producer is UE, entity for sensing data processing/result calculation is SF (either in RAN or in CN);
-	RAN2 considers QoS characteristics in Table 3 as starting point for different sensing service use cases/categories, which are defined based on sensing performance requirements captured in Table 6.2.-1 TS 22.137.
-	Nokia asks how many ms are low, medium, high latency.    Xiaomi thinks that we can further discuss what they are mapped to but this is from 5G.
-	Oppo asks why SON/MDT and QoE is not addressed.  Some of those QoS parameters are very SA2 related and we should find a more generic requirement.   Xiaomi explains that all QoS parameters are inputs from other WGs but from RAN2 point of view we can also focus on the termination.
[3 min]
Noted
R2-2508285	Views on data transfer and AI/ML framework	ZTE  Corporation, Sanechips	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-p002`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.1 Data transfer, model transfer, and AIML

RAN2 将在 TR 中记录各类用例（如 AI/ML、sensing、MDT、QoE）的 data type、endpoint pairs、data size、transmission interval 和 QoS requirement，作为后续 unified data transfer study 的 baseline。

```text
RAN2 to capture the comparison on data type, endpoint pairs, data size, transmission interval and QoS requirement (summarized in Table 1) of various use cases (e.g. AI/ML, sensing, MDT, QoE) to the TR as baseline for further unified data transfer study.
-	LG asks how the reliability can be measured.   ZTE thinks that RAN1 will be further discussed
-	Samsung asks why we don’t add inference and monitoring.
[2 min]
Noted
R2-2508576	Discussion on data transfer and AI/ML framework in 6G	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-p003`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.1 Data transfer, model transfer, and AIML

RAN2 将在 TR 中记录 6GR 不同类型待收集数据的特性和需求，并以 Table 2 为研究起点。讨论指出研究重点包括 5G 中讨论的 AI 训练和 monitoring，也可研究 inference；MDT 可采用 relaxed requirements。

```text
RAN2 to capture characteristics and requirements of different types of data that needs to be collected in 6GR in the TR. Table 2 can be used as a starting point.
-	Tmobile asks what types of data are we refereeing to, is it for inference, is it for training.    And depending on the type the characteristic are quire different.  Defining end points might be difficult.   Huawei explains that we are focusing on AI use cases we discussed in 5G, mainly training and monitoring.  We can study inference too.
-	Mediatek asks why immediate MDT is considered real time, as there are no real time requirement.  Huawei thinks that for MDT we can have relaxed requirements.
[2 min]
Noted
R2-2509054	AI/ML Framework and Data Transfer Design	MediaTek USA	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-p004`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.1 Data transfer, model transfer, and AIML

记录 Table 1 中的数据收集和数据传输用例及其 termination points。讨论提到研究 Uu 用例，UE-to-UE 用例可用于 on-device training 信息共享，sensing 数据接近实时但并非严格实时。

```text
Capture the Data collection and Data transfer cases including termination points as in Table 1.
-	MEdiatek explains that the assumptions is that we will look at Uu Cases.
-	Xiaomi asks about UE to UE use case, what is it.  Mediatek thinks it can be so sharing of information for on-device training.
-	Vivo asks what is interactive data.  Mediatek explains that for sensing cases they are more almost real time but not exactly real time.
[2 min]
Noted
R2-2508360	Discussions on 6G AI/ML	Qualcomm Incorporated	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-p005`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.1 Data transfer, model transfer, and AIML

对于 6G 网络用例中获支持的数据类型，预期至少以下方面与 5G 保持一致：数据收集的 use case/purpose、data producers 和 consumers，以及收集数据的 size 和 reporting frequency（例如由网络配置）。

```text
In 6G, for a type of data (e.g., L1, L2, L3 measurements, AI/ML data, SON/MDT, QoE, etc.) (if agreed to be supported) for network use case (e.g., regular network operations, AI/ML model training at network side, coverage and capacity optimization (CCO), Mobility Robust Optimization (MRO), RACH optimization), at least the following are expected to remain the same as 5G (as illustrated in Table 1):
-	Use case (or purpose) of the data collection,
-	Producers and consumers of the data, and
-	Size and frequency of the reporting of the collected data (e.g., configurable by network).
-	Oppo asks if we are only considering standardized data.  Qualcomm explains that we should focus on data collection for the network.
[2 min]
Noted
R2-2508578	Discussion on data transfer and model transfer in 6G	Ericsson	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-p006`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.1 Data transfer, model transfer, and AIML

提议将 Table 1 的数据假设用于 6G 数据传输和数据收集研究。讨论中出现的意见包括以 training data 或 offline training 为 baseline、聚焦 UE 参与且供网络使用的数据，并进一步研究 termination points、QoS 特性及数据传输协议；相关范围仍有待讨论。

```text
Consider data assumptions in Table 1 for study of data transfer and data collection in 6G.
-	CMCC thinks that months/weeks seems very long as the UE can only store the data for 24 hours.
[2 min]
Noted
Discussion
-	Nokia thinks we should try to define the requirements for example on latency (e.g. low means x-y ms).    Also termination points are difficult to discuss, what we need to discuss whether the data is decodable or not.
-	Oppo thinks we should start from what we have for 5G and for sensing we can postpone.
-	Apple thinks that we need inputs from other WGs and RAN2 should focus on termination points first and UE involved ones, UE to RAN and UE to CN.
-	ZTE thinks that all companies thinks that monitoring and inference should be considered but the measurement framework can be used like today, and they should be excluded.   We should focus on data training.
-	Mediatek thinks that we should focus on the cases where the UE is one of the end-points and make some assumptions on what could be the other end points.   We should discuss the type of data like SRB1, those should stay in the measurement framework.
-	Ericsson thinks that we should understand what is gNB involvement and the termination points are outside of the scope.   We should clarify the terminology we are using.
-	Lenovo thinks that we should not consider real-time data and some of the CSI etc we shouldn’t consider here.
-	CMCC thinks that we should start with training data and we shouldn’t consider data for downloading models.
-	Qualcomm thinks that we should focus on the data generated by UE and used by the network.   We should also understand the consumer of the data and only for the network use cases.
-	Xiaomi thinks we should identify the termination point, e.g. RAN, CN, OAM, and study the transport protocol.
-	Huawei agrees with training data as baseline but we should also study the monitoring data.    We can focus on data volume and latency for QoS requirements and define categories.
-	Samsung also thinks that offline training should be baseline.    Spreadtrum thinks that we should not focus only on network side.
-	Interdigital thinks that from RAN2 perspective what will impact us is the QoS characteristics.
-	Apple doesn’t think all these use case belong to do the data framework
-	MEdiatek thinks that we should add DL which includes model delivery and the delivery has several characteristics that can be similar)
-	ZTE and Xiaomi thinks that monitoring can be FFS depending on other WG discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-p007`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.1 Data transfer, model transfer, and AIML

提出适用于 AI/ML、sensing、SON/MDT 和 QoE 应用及 UE-side、NW-side 数据收集的 baseline requirements，包括保障数据安全、完整性和机密性，尊重用户隐私、匿名性及同意，并由 MNO 完全控制和查看 standardized data 的传输过程。设计还应可扩展，并尽量减少 UE 数据收集对电池、处理、内存、用户流量传输和省电功能的影响。

```text
The following baseline requirements apply to all applications (AIML, sensing, SON/MDT, QoE), including data collected at the UE-side and the NW-side.
-	The data collected is secured and data integrity and confidentiality for that data is ensured.
-	User data privacy, anonymity and user consent is respected.
-	The MNO has full control of the standardized data collection transfer process and can manage data transfer to the server for UE side data collection, without the need of Service Level Agreement (SLA) for this purpose (This includes initiating, terminating, and fully managing data transfer).
-	MNO has full visibility for standardized data.
-	The design is future-proof and extendable.
-	The UE data collection should minimize impact to the UE battery, UE processing and memory utilization.
-	UE data collection should minimize impact to user traffic transmission and power saving features
[2 min]
Noted
(Not treated) Candidate architectures
R2-2509012	Considerations for 6G data transfer	Samsung	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-p008`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.1 Data transfer, model transfer, and AIML

目标是形成适用于多种 6G 数据类型（例如 AI/ML、sensing）的通用框架。

```text
Aim to a generic framework for various types of 6G data (e.g., AI/ML, sensing).
[2 min]
R2-2508293	Discussion on Data Collection and AI/ML framework	NEC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-p009`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.1 Data transfer, model transfer, and AIML

RAN2 应研究数据传输采用哪种方案：增强 control plane、增强 user plane，或新方案（例如 new data plane、new entity/protocol layer、new RB）。传输协议的研究视时间允许而定。

```text
RAN2 should study which solution to be adopted for data transfer:
- enhanced control plane
- enhanced user plane
- new solution (e.g., new data plane, new entity/protocol layer, new RB)
[2 min]
(Not treated) Transfer protocols (if time allows)
R2-2508082	Consideration on 6GR data transfer and AI/ML framework	Xiaomi	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-p010`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.1 Data transfer, model transfer, and AIML

RAN2 将研究 UE 生成、由 CN/AF 消费的数据传输协议选项（Over NAS 或 Over IP/non-IP and UP-L2），以及 UE 生成、由 RAN 消费的数据传输协议选项（Reuse RRC、Over RRC、Over CP-L2、Over UP-L2、Over IP and UP-L2、Over non-IP and UP-L2）。对于 RAN 生成、由 CN/OAM/AF 消费的数据，传输层协议没有 RAN2 影响；协议选项将依据前向兼容性、QoS/priority 区分能力、空口协议复用和规范工作量等方面分析优缺点。

```text
Transport layer protocol used for data transfer supports the following options:
-	For ‘data produced by UE and consumed by CN/AF’, RAN2 to study two data transfer transport layer protocol options as shown in Table 4: Option 1) Over NAS, Option 2) Over IP/non-IP and UP-L2;
-	For ‘data produced by RAN and consumed by CN/OAM/AF’, no RAN2 impact on transport layer protocol;
-	For ‘data produced by UE and consumed by RAN’, RAN2 to study six data transfer transport layer protocol options as shown in Table 5: Option 1) Reuse RRC, Option 2) Over RRC, Option 3) Over CP-L2, Option 4) Over UP-L2, Option 5) Over IP and UP-L2, Option 6) Over non-IP and UP-L2;
-	RAN2 to analysis pros/cons of transport layer protocol options based on the following aspects:
o	Forward compatibility to support various data sizes;
o	Whether support differentiation across different QoS/priority requirement for different data types;
o	Whether can maximize reuse of air interface radio protocols between traffic transfer and data transfer;
o	Whether can maximize reuse of air interface radio protocols between UE<->CN and UE<->RAN;
o	Specification effort.
[3 min]
Model Transfer [30 mins]
R2-2509068	Guidelines for AI_ML model delivery options	BT Plc, Orange, T-Mobile USA, Deutsche Telekom, Turkcell, Verizon, KDDI, Vodafone, TIM, Nokia, Ericsson	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-p011`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.1 Data transfer, model transfer, and AIML

AI model transfer 需考虑模型参数传输的多种大小（具体模型大小待定）、UE mobility 期间的服务连续性，以及由 NW 决定是否及何时通过空口传输。其 latency 要求宽松，更新不频繁。

```text
The AI model transfer solution shall consider at least the below requirements:
•	Size: from RAN2 point of view, aim to support various sizes of the model parameter transfer (FFS on model size);
•	Continuity: service continuity of model transfer during UE mobility needs to be supported;
•	Controllability: NW decides on if and when to transfer over the air interface;
•	Latency: relaxed latency requirement and infrequent update;
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-p012`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.1 Data transfer, model transfer, and AIML

AI model transfer/delivery 研究应考虑将其流量设为不同于用户流量的优先级，并与其他用户流量区分。还应考虑安全、NW-aware 的传输保障，以及模型可寻址性，以便 UE 请求特定模型和/或版本。

```text
RAN2 needs to perform the study based on at least the following principles for the AI model transfer:
•	Model transfer/delivery: traffic should be transferred at a different priority, e.g., lower than user traffic.
•	Differentiability: model transfer/delivery traffic should be differentiated from other user traffic.
•	Security: there should be a guarantee that models are transferred securely, in a NW-aware manner, such that untrusted models or models from untrested AI model servers cannot be downloaded.
•	Addressability: Models need to be addressable such that the UE can request the transfer of a specific one and/or versions of models
[3 min]
Noted
R2-2508083	Unnecessary standardized model transfer and delivery	Xiaomi, Apple, Samsung, Qualcomm, Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-p013`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.1 Data transfer, model transfer, and AIML

对于 two-sided model，从 NW 到 UE-side OTT server 的 dataset/model parameter transfer 被视为 AI/ML training data collection，而非 model transfer/delivery。该模型的 transfer/delivery 指从 UE-side OTT server 下载经训练的 UE-part two-sided model 到 UE，用于 model inference。

```text
Dataset/model parameter transfer for two-sided model from NW to UE-side OTT server is considered as AI/ML training data collection, instead of model transfer/delivery. Model transfer/delivery for two-sided model is model download trained UE-part two-sided model from UE-side OTT server to UE for model inference.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-p014`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.1 Data transfer, model transfer, and AIML

NW-side model 是否以及如何支持标准化的 model transfer/delivery（例如 CN -> RAN、OAM -> RAN），属于 RAN3/SA2/SA5 的职责范围。NW-side model transfer/delivery 应对 UE 透明。

```text
For NW-side model, whether and how to support a standardized solution on model transfer/delivery (e.g., CN -> RAN, OAM -> RAN) is within remit of RAN3/SA2/SA5. NW-side model transfer/delivery should be transparent to UE.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-p015`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.1 Data transfer, model transfer, and AIML

6G 中 UE-side/UE-part two-sided model transfer/delivery（例如模型传输、内容、版本）对 3GPP 透明，可通过 non-3GPP 方案或经 UP 透明传输，因此无需定义相关要求。原文讨论记录对模型大小、WiFi、可控性和安全等问题存在不同看法。

```text
In 6G, UE-side/UE-part two-sided model transfer/delivery (e.g., model transfer, model content, model version, etc) is transparent to 3GPP (either via non-3GPP solutions or via UP transparently). No need to define requirement for UE-side/UE-part two-sided model transfer/delivery.
[3 min]
Noted
Discussion
-	BT thinks that Xiaomi is assuming everything is the same for 5G.  Xiaomi thinks that there is a big different with 5G and there isn’t a use case that requires a large model size and we can use WiFi etc like software update.
-	ZTE agrees with BT and we can’t assume the same as 5G.    We also have 2 sided model that may require model transfer.  Waiting for the UE to download from WiFi will take too long and it may have to download another model when it moves the cell.
-	Tmobile asks if chipset vendors want to story GB of models.  We just want to control and know when it is occurring.   Qualcomm thinks that the models are in the kB range for now.   Even if the size is kB, but we have few hundred thousand models that need to be transferred.
-	Apple reminds everyone that we are talking only about 3GPP model transfers.   What is untrusted AI model?
-	Mediatek also doesn’t think that security is an issue.   We need to understand how many models we have and also do we have site specific models.   If we switch models there may be a need to transfer data and maybe give ability to RAN control the transfer.
-	Nokia thinks that if UE vendors are saying that it is only few kBs can we can then commit that the models will be small.
-	Vivo also doesn’t thinks that we can rely on WiFi and we can’t conclude as RAN1 has introduced a new requirement as well and we can’t assume it is transparent.
-	Oppo thinks that it related to where the model is stored, if it is in OTT and model is small it can be transferred as app, but if it is large then we may need to consider some controllability.
-	Xiaomi thinks that we are just talking about transfer from server to UE.
AIML [10 min]
AIML use case evaluation
R2-2508285	Views on data transfer and AI/ML framework	ZTE  Corporation, Sanechips	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-p016`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.1 Data transfer, model transfer, and AIML

RAN2 将逐案研究 6GR AI/ML use cases；提案方需提供用例描述及动机/依据、性能增益及其评估方法，以及包括各 LCM 组件评估在内的规范影响。讨论中还提出明确评估基准、单侧或双侧模型，以及各用例的输入和输出。

```text
RAN 2 to conduct a case by case study on 6GR AI/ML use cases and the use case proponent shall provide the following aspects for the use case discussion: 1) Use case description, including the motivation, justification; 2) Performance gain, including the methodology for the gain evaluation; 3) Specification impact, including the evaluations based on each component of the LCM.
-	Apple thinks that we should also clarify what is the benchmark for the evaluation.  Also wether it is one sided/two sided.   Xiaomi also suggests what is input and out for each use case.
Noted
R2-2508644	Framework for AI/ML and Transfer of Various Data Types	InterDigital	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-p017`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.1 Data transfer, model transfer, and AIML

优先评估不存在传统替代方案，或 AI/ML 能显著提升系统性能的用例。

```text
Prioritize evaluation of use cases where no conventional alternative exists or AIML offers significant improvements to system performance.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-p018`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.1 Data transfer, model transfer, and AIML

已注意到为 AI/ML 评估建立复杂度指标集合的建议，包括 normalized FLOPs、space complexity 和 derived energy consumption profiles。下次会议提交 use case 时可考虑提供用例描述、性能增益及评估方法、复杂度评估、benchmark 和输入/输出；LCM aspects 未讨论。

```text
Establish a set of complexity metrics for AI/ML evaluation, including normalized FLOPs, space complexity, and derived energy consumption profiles.
Noted
Recommendation for next meeting, when bringing a use case can consider the following 1) Use case description, including the motivation, justification; 2) Performance gain (if available), explanation of the methodology needed for gain evaluation; 3) complexity evaluation (e.g. flops, memory, specification etc), 4) benchmark for evaluation, 5) input/output for each use case.
Not treated
LCM aspects (if time allows)
R2-2508099	Considerations on 6G data transfer and AI framework	CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-p019`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.1 Data transfer, model transfer, and AIML

RAN2 将研究适用于 6G AI/ML 不同 use cases 的统一 LCM procedure。

```text
RAN2 to study one unified LCM procedure across different use cases for AI/ML in 6G.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-p020`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.1 Data transfer, model transfer, and AIML

同意将 5G 中面向 UE-sided model 的 LCM procedure 作为起点。该流程包括网络查询能力、UE 指示能力、网络指示 inference configuration、UE 判断并报告 functionality applicability，以及网络/UE 功能激活或去激活。

```text
The LCM procedure agreed in 5G for UE-sided model can be agreed as starting point which consists of the following steps:
-	Step 1: NW enquiry for capability;
-	Step 2: UE indicating capability;
-	Step 3: NW indicating inference configuration;
-	Step 4: UE determines functionality applicability;
-	Step 5: UE reporting functionality applicability;
-	Step 6: NW/UE functionality (de-)activation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-p021`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.1 Data transfer, model transfer, and AIML

RAN2 将研究 6G Day1 中 two-sided model 的 LCM 影响；待 R20 AI-PHY WI 取得充分进展后再开始详细讨论。该议题未讨论。

```text
RAN2 to study the LCM impact of two-sided model in 6G Day1, and the detailed discussion can be started after sufficient progress made in R20 AI-PHY WI.
[3 min]
Not treated
R2-2508043	Discussion on data transfer and AIML	OPPO	discussion	Rel-20
R2-2508053	6GR Data transfer model transfer and AIML	vivo	discussion	Rel-20
R2-2508184	Discussion on 6GR AIML	Transsion Holdings	discussion
R2-2508185	Considerations on Data Transfer and LCM Framework for 6G AI/ML, Sensing and Other Services	LG Electronics Inc.	discussion	Rel-20
R2-2508258	Discussion on data transfer, model transfer, and AIML	Sharp	discussion	Rel-20	Withdrawn
R2-2508292	Discussion on Data transfer, Model Transfer, and AI/ML	Sharp	discussion
R2-2508355	On Management and Model Transfer for AI/ML, and Data Collection	Nokia	discussion	Rel-20	FS_6G_Radio
R2-2508375	Discussion on 6G data collection and data transfer	Apple	discussion	Rel-20	FS_6G_Radio	Withdrawn
R2-2508376	Discussion on 6G AI/ML general framework	Apple	discussion	Rel-20	FS_6G_Radio	Withdrawn
R2-2508454	Discussion on 6G data collection and data transfer	Apple	discussion	Rel-20	FS_6G_Radio
R2-2508455	Discussion on 6G AI/ML general framework	Apple	discussion	Rel-20	FS_6G_Radio
R2-2508463	Discussion on data/model transfer	Fujitsu	discussion	Rel-20	FS_6G_Radio
R2-2508470	Support for Location Dependent Data Collection	Fraunhofer IIS, Fraunhofer HHI	discussion	R2-2506974
R2-2508498	Initial consideration on AI/ML for 6GR	China Telecom	discussion	Rel-20	FS_6G_Radio
R2-2508503	Discussion on data transfer design to support various type of data	KT Corp.	discussion
R2-2508547	Views on 6GR data transfer and AIML	Sony	discussion	Rel-20	FS_6G_Radio
R2-2508581	Discussions on data collection and data transfer	NTT DOCOMO, INC.	discussion
R2-2508583	Discussion on Data transfer, model transfer, and AIML	Hanbat National University	discussion	Rel-20
R2-2508589	Discussion on Data transfer requirements for 6GR	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2508598	Consideration on radio protocols for 6G system data	HONOR	discussion	Rel-20	FS_6G_Radio
R2-2508633	Data Framework in 6G	Ofinno	discussion	Rel-20
R2-2508676	Views on data framework and AI	Fainity Innovation	discussion
R2-2508766	Discussion on AI-ML, ISAC, SON/MDT, QoE data transfer	Rakuten Mobile, Inc	discussion	Rel-20
R2-2508775	Model Transfer and Feedback Procedure for 6G AIML Framework	Jio Platforms	discussion	Rel-20	FS_6G_Radio
R2-2508843	Discussion on data collection and transfer framework	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2508880	Considerations for 6G Data Framework	AT&T	discussion	Rel-20
R2-2508884	Considerations on AI/ML framework	LG Uplus	discussion	Rel-20	Late
R2-2508905	Discussion on Data Transfer for 6G RAN	TCL	discussion	Rel-20	FS_6G_Radio
R2-2508918	Discussion on data transfer, model transfer, and AI/ML framework	Futurewei Technologies	discussion
R2-2508936	Discussion on data transfer and AIML framework	Spreadtrum, UNISOC	discussion	Rel-20
R2-2508960	Discussion on 6G AIML framework	ASUSTeK	discussion	Rel-20
R2-2508988	Discussion on data transfer and AI/ML framework	ETRI	discussion	Rel-20
R2-2509000	Discussion on 6G general AI/ML framework	TCL	discussion
R2-2509005	AI-ML model transfer based on location	LG Uplus	discussion	Late
R2-2509037	Discussion on UE data collection and transfer	Google Korea LLC	discussion
R2-2509070	Analysis of Data Flow Requirements for AI/ML and ISAC	Kyocera	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-p022`

