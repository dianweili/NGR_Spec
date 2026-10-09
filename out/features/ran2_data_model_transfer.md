# 6GR 数据与模型传输

**当前进展** · 阶段：—

_尚无综述_

## 6GR 演进

### [6G/Rel-20 RAN2#134] `agreement` 9.3.3.1 Data transfer

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

```text
RAN2 to clarify that visibility and decodability are not equivalent concepts
- Decodability refers to the capability to decode and interpret the content of the data
- Visibility refers to the capability to determine how the received data should be handled
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p001`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

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

```text
It is clarified that standardized UE-side data collection means that both the data type/format and data transfer procedure for UE-side data collection are standardized.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p003`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

```text
Based on observation 5~7, it makes sense for network to reuse the data from UE side data collection for NW-sided model training.
-	Qualcomm thinks that we may have different granularity in the data according to UE implementation.  Is this now limiting what the UE can do?
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p004`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

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

```text
RAN is not the termination point for standardized AI/ML UE-side data collection. It is up to SA2 on termination
-	Huawei ask whether we will have standardized and non-standardized data.  Qualcomm and mediatek think that this is important to also have non-standardized data transferred.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p006`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

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

```text
For the data transfer between UE and RAN, a non-IP solution is preferred due to its lower overhead and the lack of IP routing requirements. Potential directions include:
- Enhanced CP-based solution;
- New data plane (e.g., new protocol layer and new RB type).
- Note: UP-based solution is considered unsuitable for UE-RAN data transfer.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p010`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

```text
For the data transfer between UE and CN, RAN2 should focus on the air interface (Uu) transport protocols triggered by the architectural progress in SA2. Specifically, RAN2 should differentiate between the use-case-specific UE-CN protocol (higher layer) and the transport protocols (lower layers), noting that:
- CP, UP, and a new plane are potential candidates for the transport protocols;
- IP or non-IP depends on the SA2 architecture (e.g., IP for UP compatibility; non-IP for non-UP solutions).
R2-2603759	Data Transfer Framework for 6G RAN	AT&T	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p011`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

```text
RAN2 should not adopt a data transfer framework based on NR UP and NR CP, given the fundamental limitations identified for each approach.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p012`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

```text
RAN2 should study a new type of radio bearer. Such a bearer should:
- support configurable decodability,
- provide identifiability at the RAN for all use cases, and
- support QoS differentiation to enable data transfer with varying volume and latency requirements.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p013`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

```text
RAN2 should study the mechanisms necessary to support the new radio bearer (e.g., logical channels, scheduling framework.
R2-2603210	Considerations on 6G data transfer	CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p014`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

```text
RAN2 study DP to minimize impacts on legacy CP and UP, and enable the support of various QoS requirements, flexible data delivery endpoints and huge data size for data transfer.
Non-standardized data (if time allows)
R2-2603068	Discussion on data transfer	OPPO	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p015`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

```text
For non-standardized data/vendor specific data for UE-side data collection, there is no need to introduce a standardized data transfer solution within 3GPP system, i.e. it’s up to UE implementation to solve the data transfer issue for non-standardized data/vendor specific data for UE-side data collection.
R2-2603801	Data transfer and Data collection	MediaTek Beijing Inc.	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p016`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

```text
Requirement For data collection from the UE for UE-side purpose: collection of vendor-specific data need to be fully supported.
Data transfer framework principles and requirements (if time allows)
R2-2604025	Discussion on data collection and transfer framework	CMCC, NTT DOCOMO, CATT, OPPO, ZTE, Ericsson, vivo, China Unicom, China Telecom	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p017`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

```text
The following principle should be considered for 6G data collection over Uu interface:
- The duplicated data collection and reporting should be avoided as much as possible,
- For the data used by multiple consumers
- For the data used for different use cases
R2-2604143	Data Transfer Terminating in RAN for NW-side Data Collection	Nokia	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p018`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

```text
Add as a requirement that the data transfer solution supports different priority levels depending on use case with respect to other types of traffic, e.g., control and user traffic.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p019`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

```text
Add as a requirement that the data transfer solution supports different QoS parameters for each data transfer use case.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p020`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

```text
Study which QoS parameters should be defined for data transfer use cases in RAN2.
R2-2602955	Considerations on RAN2 Data Transfer in 6G	vivo, CAICT, NTT DOCOMO INC., CMCC	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.3.3.1-p021`

### [6G/Rel-20 RAN2#134] `proposal` 9.3.3.1 Data transfer

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

```text
Postpone discussion on sensing use case. Impact on data transfer framework can be revisited after further progress on fundamental aspects (e.g., data characteristics, termination point(s) etc.) in sensing session.
Size + Latency categories
R2-2601915	Discussion on data transfer in 6G	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.1-a001`

### [6G/Rel-20 RAN2#133bis] `agreement` 9.3.3.1 Data transfer

```text
Performance monitoring and inference is not considered data transfer for now.
Immediate MDT is not part of data transfer as it is assumed to be part of measurement reporting framework for now.
Data consumer, termination point, and decodability
Termination points
R2-2601454	Requirements Analysis and Use Cases of UE as a Consumer	vivo, CAICT, CMCC	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.1-a002`

### [6G/Rel-20 RAN2#133bis] `agreement` 9.3.3.1 Data transfer

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

```text
For NW-side data collection and SON/MDT use cases, when the RAN is the data consumer, the RAN node acts as the termination point and decodes the data.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.1-p002`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.1 Data transfer

```text
For use cases (e.g., NW-sided data collection, SON, MDT) where the OAM is the data consumer, the termination point should be identified on a hop-by-hop basis (e.g., UE-to-RAN and RAN-to-OAM).
-	RAN is the termination point for UE-RAN data transfer.
-	OAM is the termination point for RAN-OAM data transfer.
-	RAN can decode the data.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.1-p003`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.1 Data transfer

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

```text
For UE data collection for network use cases, the RAN is considered the termination entity only if
-	A report is critical for Uu operations and RAN optimizations (e.g., immediate MDT, RVQoE, SON reports)
This also helps in reducing UE AS memory requirements for data collection while providing meaningful reports
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.1-p005`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.1 Data transfer

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

```text
For the following use cases where RAN as consumer, the data should be visible and decodable by RAN node.
- NW side data collection where model training resides at RAN (e.g. Beam management, CSI prediction, CSI compression, AI Mob)
- SON (e.g. MRO, RACH Optimization)
- Immediate MDT (e.g. measurement results)
- RAN visible QoE (e.g. Buffer level, playout delay for media start-up)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.1-p007`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.1 Data transfer

```text
For the following use cases where OAM as consumer, the data can also be visible and decodable by RAN.
- NW side data collection where model training resides at OAM (e.g. Beam management, CSI prediction, CSI compression, AI Mob)
- SON (e.g. MRO, RACH Optimization)
- Logged MDT (e.g. cell measurements)
- Immediate MDT (e.g. L1/L3 measurement results)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.1-p008`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.1 Data transfer

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

```text
Service-specific protocols are used to define AI/ML, sensing and SON/MDT, e.g., Data processing  and control signalling of a service are defined independently in the corresponding service-specific protocol.
Not treated
Data Transfer Requirements (if time allows)
R2-2602437	Discussion on data collection and transfer framework	CMCC, China Unicom, NTT DOCOMO, vivo, OPPO	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.1-p011`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.1 Data transfer

```text
The following principle should be considered for 6G data collection over Uu interface:
- The duplicated data collection and reporting should be avoided as much as possible,
- For the data used by multiple consumers
- For the data used for different use cases
R2-2602293	Data transfer terminology and use of the user plane	Nokia, T-Mobile USA	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.1-p012`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.1 Data transfer

```text
Define controllability of data collection and transfer as the ability for the MNO to start, stop or modulate the flow of data transfer traffic and to enable or disable data collection measurement resources such as reference signals.
R2-2601454	Requirements Analysis and Use Cases of UE as a Consumer	vivo, CAICT, CMCC	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.3.3.1-p013`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.3.3.1 Data transfer

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

```text
RAN2 to endorse the below definition of ‘termination point’ and ‘data consumer’:
-	‘Termination point’ is the end-entity of E2E data transfer transport protocol stack between UE and NW entity.
-	‘Data consumer’ is the entity (either inside or outside of MNO) that can process the collected data. Data should only be decoded and processed by data consumer.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p001`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

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

```text
RAN2 aims to design a unified framework and architecture that can manage 6G various types of data such as AI/ML, Sensing, SON/MDT, QoE and future emerging services.
Data Transfer framework
QoS characteristics
R2-2600538	Discussion on data transfer and model transfer in 6G	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p006`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

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

```text
Data transfer framework shall support high volume (e.g., up to hundreds of MB) with relaxed latency (e.g., minutes to hours). At least RAN and UE-side server are end points.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p008`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

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

```text
RAN2 to adopt Table 1 for data transfer analysis.
Noted
R2-2600839	Discussions on Data Collections in 6G	Qualcomm Incorporated	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p010`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

```text
RAN2 is requested to consider Table 1 for different aspects of data collection (e.g., QoS requirements, termination entities, consumers, decodability at the RAN) for AI/ML Data.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p011`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

```text
RAN2 is requested to consider Table 2 for different aspects of data collection (e.g., QoS requirements, termination entities, consumers, and decodability at the RAN) for SON, MDT, and QoE Data.
Noted
R2-2600500	Views on data transfer and model transfer	ZTE  Corporation, Sanechips	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p012`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

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

```text
Data collected as part of the data transfer framework is not necessarily required to be decodable by RAN, except for the cases in which RAN is the consumer of the data.
R2-2600893	On Decodability of AI/ML Data in 6G RAN	AT&T	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p014`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

```text
6G RAN nodes can be configured to decode data collected for termination at other entities.
Enhancements for data transfer (if time allows)
R2-2600268	Discussion on Data Collection	NEC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p015`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

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

```text
In 6G, the model transfer should follow requirements:
•	Awareness: MNO can be aware of the existence of model.
•	Controllability: MNO can control the model transfer/delivery procedure (initiate, suspend, resume, stop etc.).
R2-2600780	Discussion on data transfer and model transfer in 6G	Verizon, Ericsson	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p017`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

```text
It should be possible for the network to control the model transfer/delivery from the UE-side training server to the UE. RAN2 to study ways to achieve this in coordination with other WGs
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p018`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

```text
RAN2 to identify which data collection and model transfer aspects pertain to the scope of other working groups and coordinate with the relevant groups at an early stage of the 6G study.
R2-2600839	Discussions on Data Collections in 6G	Qualcomm Incorporated	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p019`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

```text
No need to define requirements for model transfer/delivery, as existing means to update the “UE” software can be reused for model transfer/delivery to the UE for UE inference.
R2-2600125	Consideration on data transfer and model transfer	Xiaomi	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.3.3.1-p020`

### [6G/Rel-20 RAN2#133] `proposal` 10.3.3.1 Data transfer and model transfer

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

```text
5G data transfer over CP-based framework is not suitable to support large volume of data and has the risk of degrading the existing essential CP signaling.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-o001`

### [6G/Rel-20 RAN2#132] `observation` 10.3.3.1 Data transfer, model transfer, and AIML

```text
5G data transfer over UP-based framework has to go through UPF unnecessarily and gNB cannot be involved for data transfer and management (when needed). Besides, the data transfer over UP is terminated in application layers which are not in control of 3GPP.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-o002`

### [6G/Rel-20 RAN2#132] `observation` 10.3.3.1 Data transfer, model transfer, and AIML

```text
5G data transfer ended up introducing diverse frameworks to support various data types.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-o003`

### [6G/Rel-20 RAN2#132] `observation` 10.3.3.1 Data transfer, model transfer, and AIML

```text
For the study of new AI/ML use cases for 6GR that may require evaluation by RAN2, the methodology should define consistent metrics to quantify the complexity and energy consumption of AI/ML features against 6GR non-AI/ML baselines
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-o004`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.1 Data transfer, model transfer, and AIML

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

```text
Aim to a generic framework for various types of 6G data (e.g., AI/ML, sensing).
[2 min]
R2-2508293	Discussion on Data Collection and AI/ML framework	NEC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-p009`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.1 Data transfer, model transfer, and AIML

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

```text
The AI model transfer solution shall consider at least the below requirements:
•	Size: from RAN2 point of view, aim to support various sizes of the model parameter transfer (FFS on model size);
•	Continuity: service continuity of model transfer during UE mobility needs to be supported;
•	Controllability: NW decides on if and when to transfer over the air interface;
•	Latency: relaxed latency requirement and infrequent update;
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-p012`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.1 Data transfer, model transfer, and AIML

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

```text
Dataset/model parameter transfer for two-sided model from NW to UE-side OTT server is considered as AI/ML training data collection, instead of model transfer/delivery. Model transfer/delivery for two-sided model is model download trained UE-part two-sided model from UE-side OTT server to UE for model inference.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-p014`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.1 Data transfer, model transfer, and AIML

```text
For NW-side model, whether and how to support a standardized solution on model transfer/delivery (e.g., CN -> RAN, OAM -> RAN) is within remit of RAN3/SA2/SA5. NW-side model transfer/delivery should be transparent to UE.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-p015`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.1 Data transfer, model transfer, and AIML

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

```text
RAN 2 to conduct a case by case study on 6GR AI/ML use cases and the use case proponent shall provide the following aspects for the use case discussion: 1) Use case description, including the motivation, justification; 2) Performance gain, including the methodology for the gain evaluation; 3) Specification impact, including the evaluations based on each component of the LCM.
-	Apple thinks that we should also clarify what is the benchmark for the evaluation.  Also wether it is one sided/two sided.   Xiaomi also suggests what is input and out for each use case.
Noted
R2-2508644	Framework for AI/ML and Transfer of Various Data Types	InterDigital	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-p017`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.1 Data transfer, model transfer, and AIML

```text
Prioritize evaluation of use cases where no conventional alternative exists or AIML offers significant improvements to system performance.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-p018`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.1 Data transfer, model transfer, and AIML

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

```text
RAN2 to study one unified LCM procedure across different use cases for AI/ML in 6G.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.3.3.1-p020`

### [6G/Rel-20 RAN2#132] `proposal` 10.3.3.1 Data transfer, model transfer, and AIML

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

