# 6GR UE 能力框架

**当前进展** · 阶段：—

_尚无综述_

## 6GR 演进

### [6G/Rel-20 RAN2#134] `agreement` 9.2.1 UE capability framework

```text
-	UE capability change message is sent to the network in RRC connected mode and this information is expected to be forwarded to the target aNB in case of mobility.   FFS what happens when the UE goes to Idle/Inactive and if it is expected that the latest information is stored.
For next meeting, companies are encouraged to work offline to have an overall view on how the procedures work and co-sourced contributions only are expected.
Network response
R2-2603344	Views on dynamic capability change	NTT DOCOMO	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-a001`

### [6G/Rel-20 RAN2#134] `observation` 9.2.1 UE capability framework

```text
There may exist network implementations or operational policies that do not consider capability change requests for use cases that are not considered by the network and/or for use cases where the impact of the capability change is not significant.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-o001`

### [6G/Rel-20 RAN2#134] `observation` 9.2.1 UE capability framework

```text
A network that receives an indication of UE capability change has the opportunity to influence how the UE behaves in response to a problematic situation; a network that does not receive such an indication has no choice but to face the effects of the UE’s autonomous recovery behaviours, whatever they are.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-o002`

### [6G/Rel-20 RAN2#134] `observation` 9.2.1 UE capability framework

```text
The harmful impact to network KPIs related to capability updates comes primarily from UEs forced to rely on autonomous solutions when the network does not or cannot update the configuration.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-o003`

### [6G/Rel-20 RAN2#134] `observation` 9.2.1 UE capability framework

```text
By the time of capability change, the UE already has a problem that must be solved, and the network cannot at this stage prevent the problem from occurring; it can only refuse to notice.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-o004`

### [6G/Rel-20 RAN2#134] `observation` 9.2.1 UE capability framework

```text
Reporting the entire capability container for capability update prevents the network from performing delta configuration and necessitates full configuration, which causes service interruption and defeats the purpose of introducing capability update in RRC_CONNECTED.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-o005`

### [6G/Rel-20 RAN2#134] `observation` 9.2.1 UE capability framework

```text
Reporting the entire capability container for capability updates introduces unnecessary large signaling overhead and degrades resource efficiency, thus discouraging operators from deploying the feature.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-o006`

### [6G/Rel-20 RAN2#134] `observation` 9.2.1 UE capability framework

```text
Response from network can essentially be L12 setting and/or RRC Reconfiguration
Proposal 2	Upon expiry of a timer started upon the transmission of capability change request, UE perform capability change, and evaluate whether the latest L12 setting and RRC (re)configuration can comply with its request. If not, UE applies default/SIB1 configuration, and report to network on the event.
R2-2602944	Further discussion on dynamic UE capability change	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-o007`

### [6G/Rel-20 RAN2#134] `observation` 9.2.1 UE capability framework

```text
There is no need to discuss further on RACS ID (i.e. CN based ID, same as 5G, ID is defined to represent full set of UE capabilities) in RAN2, which has obvious coordination challenges and network maintenance burden (i.e., storage issue) and is up to SA2 to further discuss.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-o008`

### [6G/Rel-20 RAN2#134] `observation` 9.2.1 UE capability framework

```text
In 5G, UE capabilities were signalled using tightly coupled and deeply nested structures (e.g. per-band, per-band-combination capabilities), which limited reuse of common capability information and caused repeated signalling of identical values across bands and combinations.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-o009`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.1 UE capability framework

```text
The mechanism that allows reporting of capability updates without prior network reconfiguration shall be applied only to use cases that are independent of network implementation and have a significant impact on performance.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-p001`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.1 UE capability framework

```text
The UE is allowed to report capability updates without prior network
configuration when the cause is overheating and/or power saving.
Noted
R2-2603257	Capability update mechanism	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-p002`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.1 UE capability framework

```text
Further discuss the possibility of the UE updating a capability field that the network does not support, with an aim to understand how such a problem can be avoided.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-p003`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.1 UE capability framework

```text
Confirm that if the network controls whether the UE can invoke the capability update mechanism, the UE will necessarily apply autonomous fallback mechanisms without any indication when a problem occurs and the update is not permitted.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-p004`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.1 UE capability framework

```text
Allow the UE to indicate a capability update without prior network permission (i.e., without the equivalent of OtherConfig in 5G) for all use cases.  Network configuration of related parameters such as timers can be discussed.
Noted
Discussion
-	Vivo and Xiaomi thinks that it is important that the UE can always update.  Xiaomi thinks that we can discuss for which capability is allowed or not to be updated without network control.   Huawei thinks that this would make it mandatory for the network.    Xiaomi thinks that it depends on the network response.
-	Vodafone thinks that the frequency of the updates is an important issue, so we should be careful.   Mediatek asks that if you have these cases then is the preference to have a UE that detaches all the times or that sends many UE capability updates.  Nokia thinks that the UE should assume the worst capability if it moving back and forth between overheating and not overheating.  Qualcomm reminds everyone that it is not in UEs benefit to downgrade capabilities so it won’t do it for no reason.
-	Apple thinks that we can’t predict the future capabilities/features.
-	Docomo explains that we can’t treat all the cases the same, for example IDC shouldn’t be treated the same as overheating as the priority is licenced band.    Xiaomi thinks that there is to be a trust on UE implementation, as it is not possible to know why some of these capabilities are changing.    Also there is no way to test the use case.
Capability reporting
R2-2603402	Dynamic UE capability change in connected mode	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-p005`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.1 UE capability framework

```text
RAN2 to agree on the baseline solution where the UE reports the entire UE radio capability for dynamic UE capability change in connected mode
Noted
R2-2604146	Consideration on the Dynamic Capability Update	ZTE Corporation, Sanechips, CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-p006`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.1 UE capability framework

```text
For dynamic capability reporting, the UE shall be allowed to report different capabilities for different cases:
	For each case, the UE should report only the critical parameters rather than the full set of capabilities.
	For the power saving and overheating case, the envelope capability reporting mechanism should be retained.
Noted
R2-2603769	UE capability framework for 6G	Samsung	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-p007`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.1 UE capability framework

```text
RAN2 agree that only relevant UE capabilities will be considered for dynamic UE capability reporting.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-p008`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.1 UE capability framework

```text
RAN2 further study both different capability container and same capability container with delta signaling, evaluating them based on signaling overhead and future extensibility.
Noted
R2-2604157	Discussion on UE capability update	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-p009`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.1 UE capability framework

```text
The capability parameters which can be updated are defined in standards for each use case. The parameters defined in 5G are reused in 6G capability update study.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-p010`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.1 UE capability framework

```text
To clearly indicate the changed capability information for network to perform delta reconfiguration, and to reduce signalling overhead for capability update, only the changed capability parameters are reported.
Noted
Discussion
-	Qualcomm is fine with reporting just some capabilities but don’t want to end up in a discussion that if a parameter changes then it is not supported etc.
-	Xiaomi thinks that a container is also helpful from a context retrieval point of view.    Mediatek also thinks it is important for HO, etc.
-	Vivo thinks that the most important part is the delta.
-	Ericsson thinks that we shouldn’t look at every parameter whether it is allowed or not, but rather some general capabilities.
-	Oppo thinks that the reporting should be in a general manner (use case agnostic) and what parameter to be included, number of RF chain, bw, MIMO, they are critical parameters.
-	CMCC thinks that we should consider CN as well.
-	Apple has a request that we should carefully look at the parameters and not just base them on NR, for example for MUSIM there are some parameters missing.
-	Offino thinks we need to understand the requirements, long term or short term in connected.
-	Mediatek thinks that we can’t limit this to RRC connected.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-p011`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.1 UE capability framework

```text
The aNB, upon receiving a capability update request, shall send either an RRC reconfiguration message or a reject message including the reject cause to the UE.
R2-2603002	Discussion on 6G Dynamic Capability Update	OPPO	discussion	Rel-20	FS_6G_Radio
Observation 1	Response message opens the possibility for network to reject the request, meaning the request message will be meaningless in such case, and thus it motivates the 6G UE to adopt implementation methods. Eventually, it makes the standardized method (and the specification effort for it) becomes meaningless.
Proposal 1	Network may respond UE capability change request in various manners, including DCI, MAC-CE and RRC Reconfiguration (and combination of them). R2 puts no restriction on that, and not pursue defining a specific message as the response message for capability update request.
R2-2603257	Capability update mechanism	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-p012`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.1 UE capability framework

```text
The network response message does not provide an option for the network to reject the capability update.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-p013`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.1 UE capability framework

```text
A supervisory timer governs when the UE can expect a network response to a capability update.  Further discuss if the timer is network-configured.
UE behaviour when no response is received
R2-2603340	Discussion on dynamic capability update	LG Electronics France	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-p014`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.1 UE capability framework

```text
Upon the fallback timer expiry, the UE performs the RRC re-establishment procedure as a baseline.
R2-2603002	Discussion on 6G Dynamic Capability Update	OPPO	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-p015`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.1 UE capability framework

```text
Regarding how to handle the mismatch between the updated capability and the RRC configuration after the wait timer expires, RAN2 to discuss the following two options:
- Option 1: Referring to the existing solution for MUSIM, i.e., how to apply the RRC configuration is left to UE implementation;
- Option 2: Referring to the potential solution for the RRC reconfiguration failure, i.e., wait for the conclusion of the solution for the RRC reconfiguration failure handling, and consider reusing that solution if feasible.
R2-2603728	Dynamic UE capability update in 6G	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-p016`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.1 UE capability framework

```text
The UE behavior should be unified for the following cases:
•	The network does not provide a response message within a defined timeline
•	The network provides a NACK response message
•	The network provides an ACK response, but fails to provide appropriate handling within a defined timeline
Additional use-case
R2-2603287	Discussion on UE Capability Framework	Futurewei Technologies	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-p017`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.1 UE capability framework

```text
RAN2 to include UE internal resource availability (including computational power/APU, memory, and storage) as a use case for the dynamic capability update study
R2-2603617	Discussion on 6GR UE capability	Sony	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-p018`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.1 UE capability framework

```text
RAN2 to study dynamic capability to cater for wider use cases including UE battery level.
Other – if time allows
R2-2603873 Considerations on UE capability framework for 6GR CMCC discussion Rel-20 FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-p019`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.1 UE capability framework

```text
It is proposed to study modular UE Capability signaling to reduce signaling size.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-p020`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.1 UE capability framework

```text
For RAN based ID, pre-defining some basic/mandatory UE capability sets including static RAN related capability parameters (e.g. band/radio related parameters) could be considered.
R2-2603663	Design of 6GR UE capabilities	InterDigital, Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-p021`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.1 UE capability framework

```text
Support module-based capability reporting and configuration procedures using delta and reference profiles, enabling capability IDs to represent reusable partial capability sets (aligned with Direction 2).
R2-2603325	Discussion on 6GR capability framework	Nokia	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-p022`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.1 UE capability framework

```text
The study on the RAN-centric capability ID procedure can focus on identifier assignment and how identifiers may be used by the UE and network to reference capability sets.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-p023`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.1 UE capability framework

```text
Study scalable design for UE capability signalling with the objective of ensuring the UE capability container is unsegmented.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-p024`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.1 UE capability framework

```text
Study the use of progressive or iterative capability enquiries that enable the UE capability information to be reported across multiple self-decodable UL RRC messages.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-p025`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.1 UE capability framework

```text
Study how to capture all capability aspects in one technical specification to simplify specification, maintenance, and implementation of the 6GR UE capabilities.
Other – Early implementation
R2-2604166	Discussion on Early Implementations	MediaTek Inc., Ericsson, Nokia	discussion	Rel-20
Proposal 1	RAN2 to clarify the Early Implementation tables, if still needed in 6G, are just a bookkeeping of 3GPP endorsed features, and do not prevent the other features from being early implemented.
Proposal 2	Send an LS OUT to inform RAN5 of the RAN2 conclusion.
R2-2602964	Discussion on capability update	Xiaomi	discussion	Rel-20	FS_6G_Radio
R2-2603296	UE capability framework in 6G	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2603426	Discussion on Dynamic UE Capability Update in 6G	KT Corp.	discussion	Rel-20	FS_6G_Radio
R2-2603657	Discussion on dynamic UE capability change	NEC	discussion	Rel-20	FS_6G_Radio
R2-2603703	Improvements for UE capabilities	Ericsson	discussion	Rel-20	FS_6G_Radio
R2-2603748	On Dynamic UE Capability Update and Response from the Network	Jio Platforms	discussion	FS_6G_Radio
R2-2603771	Discussion on Dynamic UE Capability Change	Turkcell, CATT	discussion	Rel-20	FS_6G_Radio
R2-2603831	6GR UE Capability Framework	Sharp	discussion
R2-2603884	Discussion on dynamic UE capability in 6G	1Finity	discussion	Rel-20	FS_6G_Radio
R2-2604010	Discussion on UE autonomous behaviour for 6G UE dynamic capability 	ETRI	discussion	Rel-20
R2-2604157	Discussion on UE capability update	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
R2-2604166	Discussion on Early Implementations	MediaTek Inc., Ericsson, Nokia	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.1-p026`

### [6G/Rel-20 RAN2#133bis] `agreement` 9.2.1 UE capability framework

```text
1   For Size of FeatureSet ID and FSC List capture the following two solutions as candidate options in TR, the details will be decided in WI stage-3. No further discussion on this topic in RAN2 SI phase:
Solution 1. Reduce the size of FeatureSetDownlink/UplinkID
Solution 2. Variable FeatureSetDownlink/UplinkID length (short/long)
2	Wait for RAN4 progress on whether UE reports capabilities per RF chain instead of per band/BC.
3	RAN2 to study the benefit of compression solution (i.e., Category 6) later after some progress on the outcome of capability signalling design of Category 1-3/8.
4	RAN2 agrees to take category 1/3/8 and corresponding solutions as starting point to further compare gains/limitations of each solution based on real life NR capability container (including clarification on solutions if needed).
CATEGORY 1: Common capability reporting for a group of bands/band combinations/carriers that have the same capabilities [Study Area: 1, 2, 3] (12/12 companies)
Solution 1: Group signalling for the same capability set(s) without changing capability granularity level
-	For ‘per BC’ capability
	Example capabilities: repeated per BC capabilities
-	For ‘per band’ capability
	Example capabilities: repeated per band capabilities
Solution 2: Feature Set at band combination level
-	For ‘per BC’ capability
	Example capabilities: repeated baseband per BC capabilities
-	For ‘per band and per BC’ capability
	Example capabilities: MIMO codebook capabilities
Solution 4: Coarse granularity
Solution 4-1: Move to Coarse capability granularity level
-	From ‘per BC’ granularity to ‘per UE’ granularity for some UE envelop capabilities
	Example capabilities: e.g., csi-RS-IM-ReceptionForFeedbackPerBandComb, simultaneousCSI-ReportsAllCC
-	From ‘per band pair per BC’/ ‘per BC’ to ‘per UE’ granularity
	Example capabilities: e.g., switching period, including srs-SwitchingTimesListNR, uplinkTxSwitchingPeriod, switchingPeriodForFDD-SDL
Solution 4-2: Use envelop signalling for the following capabilities
-	For ‘per FSPC’ capability
	Example capabilities: e.g., maxNumberMIMO-LayersCB-PUSCH, maxNumberSRS-ResourcePerSet, maxNumberMIMO-LayersNonCB-PUSCH, supportedModulationOrderUL, maxNumberMIMO-LayersPDSCH, etc
-	For ‘per FS’ capability
	Example capabilities: e.g., DMRS parameters (oneFL-DMRS-TwoAdditionalDMRS-DL, additionalDMRS-DL-Alt, twoFL-DMRS-TwoAdditionalDMRS-DL, oneFL-DMRS-ThreeAdditionalDMRS-DL), supportedSRS-Resources
Solution 5: Band combination signaling optimization, e.g., including remove redundant BC for BW classes (assuming signalling of BW class is still needed), etc.
CATEGORY 3: Increase the reusability of FeatureSetCombination and UL/DL decoupling [Study Area: 3] (7/12 companies)
Solution 1.	Use separate FeatureSetCombinations for UL and DL for each BC
Solution 2.	Keep FeatureSetCombination for both UL and DL, while allowing indicate once for FS DL and a list of FS UL
Solution 3.	Create a mapping structure indicating valid UL-DL capability combination supported by a UE
Solution 4.	Remove FeatureSetCombination ID completely. Use FSC directly in BC.
CATEGORY 8: ‘Same-as-previous’
Solution 1: Use ‘same-as-previous’ method
-	For ‘per band’ capability
-	For ‘per FS’ capability
-	For repeated FeatureSet ID within FSC.
6	Inform RAN4 after some further progress on UE capabilities about the RAN2 identified redundant capability signalling caused by BC definition capabilities and hope RAN4 could take RAN2 study outcome (either consider BCS4/5 as baseline or use UE envelop limitation for supportedBandwidth) into consideration when discussing BC definition.
7	RAN2 has no consensus on whether RACS ID (i.e. CN based ID, same as 5G, ID is defined to represent full set of UE capabilities) will be still used in 6G considering coordination challenges and network maintenance burden (i.e., storage issue).  It is up to SA2 to further discuss this.
8	RAN2 can further consider/study RAN based ID, how it works, and what information is represented by this ID.
9	Companies to report the following information to compare gains/complexity of each solution:
-	Baseline UE capability log of eMBB UE used for gain analysis
-	Capability container size
-	Total number of BC
-	Total number of band
-	Number of bands with repeated capabilities in bits for each redundant group (detailed examples are welcomed)
-	Number of BCs with repeated capabilities in bits for each redundant group (detailed examples are welcomed)
-	Number of featureSet and FeatureSetCombination (including FeatureSetUL/DL)
-	Gains relative to capability container of each solution (in numbers)
-	Network and UE Complexity/Flexibility (including implementation complexity, implementation restriction, reporting flexibility)
10	UE capability discussions will continue until August over email and no contributions on UE capabilities signaling in scope of this email are expected in May meeting.
[POST133bis][003][6G] UE capabilities (Xiaomi)
Intended outcome: Gains and complexity analysis of candidate solutions.
Phase 1: Consolidate on high level signalling example for each solution (evaluate need for need for offline in the May meeting).
Phase 2: Practice on gains of all solutions. Compare gains and complexity of all solutions.
Deadline:  14th Aug
R2-2602809	Report of [AT133bis][003][6G] UE capabilities (Xiaomi)	Xiaomi	report	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.2.1-a001`

### [6G/Rel-20 RAN2#133bis] `agreement` 9.2.1 UE capability framework

```text
Capture the following Solution 4 and 5 in the TR
Solution 4: Coarse granularity
Description: Some companies in RAN2 observe the following capabilities are repeatedly signalled.
‘per BC’ granularity
Example capabilities: e.g., csi-RS-IM-ReceptionForFeedbackPerBandComb, simultaneousCSI-ReportsAllCC
‘per band pair per BC’/ ‘per BC’
Example capabilities: e.g., switching period, including srs-SwitchingTimesListNR, uplinkTxSwitchingPeriod, switchingPeriodForFDD-SDL
‘per FSPC’ capability
Example capabilities: e.g., maxNumberMIMO-LayersCB-PUSCH, maxNumberSRS-ResourcePerSet, maxNumberMIMO-LayersNonCB-PUSCH, supportedModulationOrderUL, maxNumberMIMO-LayersPDSCH, etc
‘per FS’ capability
Example capabilities: e.g., DMRS parameters (oneFL-DMRS-TwoAdditionalDMRS-DL, additionalDMRS-DL-Alt, twoFL-DMRS-TwoAdditionalDMRS-DL, oneFL-DMRS-ThreeAdditionalDMRS-DL), supportedSRS-Resources
Solution 5: Band combination signalling optimization, e.g., including remove redundant BC for BW classes (assuming signalling of BW class is still needed), etc.
R2-2601881	Summary of discussion [POST133][005][6G] Dynamic capability reporting (MediaTek)	MediaTek Inc.	report	Rel-20	FS_6G_Radio
Noted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.2.1-a002`

### [6G/Rel-20 RAN2#133bis] `agreement` 9.2.1 UE capability framework

```text
Do not capture a distinction between “families” of capability change use cases for now.
Confirm for all use cases the at least the following pain points of the existing UAI mechanism in NR:
The network may not support the UAI functionality and/or may not enable it for the UE.
There is no direct response from the network and no certainty that the network will address the UE’s request for a change.  Because of network and overall system considerations, the network may need flexibility to address the problem differently from what the UE requested, which makes it difficult for the UE to know what the outcome of the request was.
The network is unaware of unspecified UE autonomous behaviours (fallback, etc), resulting in KPI degradation and connection failures, and making it difficult for the network to identify the root cause of the problem.
Aim for a solution where the UE is allowed for some use cases to invoke the capability update mechanism without prior network configuration.  This proposal does not imply what the network will do with the update.   FFS what features/use cases and what circumstance/conditions.
Study how to send the UE capability update, including the complete capability container or specific UE dynamic capability container/parameter.   FFS if we have different behaviour/parameters affected for different use cases.
A response message to the capability update is defined for all use cases.  FFS what message is used and what information is provided to the UE.
Study timeline within which the UE expects a response to the capability update.  FFS what is the UE behaviour when no response is received.
Power saving, foldable phones and IDC are considered as additional use cases for capability update study.    Additional use cases can be discussed in the future as their requirements become clear, and the capability change framework should strive for forward compatibility for such use cases.
Not treated
R2-2601443	Further discussion on dynamic UE capability change	vivo	discussion	Rel-20
R2-2601462	Further considerations on UE capability signalling  and framework	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
R2-2601479	Discussion on 6G UE Capability	OPPO	discussion	Rel-20	FS_6G_Radio
R2-2601657	UE capability framework for 6G	Samsung	discussion	Rel-20
R2-2601673	Discussion on UE Capability Compression	CATT	discussion	Rel-20	FS_6G_Radio
R2-2601739	Further discussion on 6GR capability signaling design	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
R2-2601805	Discussion on 6G UE capability	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
R2-2601821	Discussion on UE Capability Framework	Futurewei Technologies	discussion	Rel-20
R2-2601853	UE capability framework in 6G	Ofinno	discussion
R2-2601987	Discussion on UE capability aspects in 6G	1Finity	discussion	Rel-20	FS_6G_Radio
R2-2602010	Discussion on 6G UE capability signalling	KT Corp.	discussion	Rel-20	FS_6G_Radio
R2-2602113	Consideration on the Dynamic Capability Update	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
R2-2602156	Discussion on 6GR UE capability	Sony	discussion	Rel-20	FS_6G_Radio
R2-2602194	Design of 6GR UE capabilities	InterDigital, Inc.	discussion	Rel-20	FS_6G_Radio
R2-2602228	Considerations on UE capability framework in 6G	Apple	discussion	Rel-20	FS_6G_Radio
R2-2602263	Improvements for UE capabilities	Ericsson	discussion
R2-2602277	Further discussion on UE capability change framework	NEC	discussion	Rel-20	FS_6G_Radio
R2-2602310	Discussion on 6GR capability framework	Nokia	discussion	Rel-20	FS_6G_Radio
R2-2602311	6GR UE Capability Framework	Sharp Laboratories of America	discussion
R2-2602432	Considerations on UE capability framework for 6GR	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2602516	Discussion on 6G dynamic UE capability update	DENSO CORPORATION	discussion
R2-2602536	Discussion on requirements for dynamic UE capability reporting	ETRI	discussion	Rel-20
R2-2602550	Discussion on capability update mechanism	LG Electronics France	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.2.1-a003`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.2.1 UE capability framework

```text
RAN2 to study the benefit of compression solution (i.e., Category 6) based on outcome of capability signalling design of Category 1-3/8.
CATEGORY 6: Compression
Solution 1.	Compress UE capability message, for example, Deflate, etc.
-	Apple indicates that they provided an analysis already and wonders if the analysis would need to be done again.  Xiaomi thinks that we should wait and use the agreed formats to do an analysis, as if we do analysis based on current signalling it would show a lot of benefits but if we do things better the gains may be different.
-	Ericsson wonders if this actually means that we would only do this in WI phase after we have some ASN.1 structure.  Xioami confirms as by the time we get all the structure done it will be in WI phase.
-	Oppo thinks that it is very useful to look into the method as some of the gains are up to 50% which is a lot more than any other solutions.   Qualcomm has similar understanding as Oppo, and we should at least capture the gains that show it is promising.
-	CMCC also thinks we should discuss after the structure is decided, as compression gains will depend on that.
-	Xiaomi thinks that the compression is more general for RRC rather than just UE capabilities.  Oppo thinks it would be meaningful to focus with UE capability and we can study if it can be extended to other capabilities.
Noted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.2.1-p001`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.2.1 UE capability framework

```text
Capture Solution 4/5 and impacted capabilities in the TR and revisit in WI phase the need of considering the coarse granularity based on RAN1/4 feature list in 6G.
Noted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.2.1-p002`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.2.1 UE capability framework

```text
Aim for a unified signalling procedure for change of UE capabilities that can accommodate indications of both a change in UE envelope capabilities and a change in specific RF- or hardware-related capabilities.  This does not imply that all use cases will affect the same capability fields.
-	Huawei thinks it is not clear what is unified and we shouldn’t rush.   Xiaomi explains that this is just for reporting and UE behaviour.   Ericsson is also not clear what is the gain for this unified behaviour.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.2.1-p003`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.2.1 UE capability framework

```text
Confirm for all use cases the following pain points of the existing UAI mechanism in NR:
The network may not support the UAI functionality and/or may not enable it for the UE.
There is no direct response from the network and no certainty that the network will address the UE’s request for a change.  Because of network and overall system considerations, the network may need flexibility to address the problem differently from what the UE requested, which makes it difficult for the UE to know what the outcome of the request was.
-	ZTE thinks that are NW side pain points that are not listed, like the autonomous fallback.  When the network doesn’t address the UE concern a pain point is that the UE will do something unpredictable.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.2.1-p004`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.2.1 UE capability framework

```text
The UE is allowed for all use cases to invoke the capability update mechanism without prior network configuration.  This proposal does not imply what the network will do with the update (see P8).
-	CMCC doesn’t agree that it should be done without network configuration as it will impact network performance.
-	Huawei thinks that one option is to make it mandatory for both the network and the UE, but we don’t discuss now, but it will also depend on the use case.
-	Docomo is concerned that there are cases where the UE may update capability but the network doesn’t even support.  In these cases it is a complete overhead.    But some optimization can be considered.
-	Qualcomm thinks that we need to support this proposal otherwise we need to accept UE autonomous behaviour which is a pain point.   Do you think it is better to not know what the UE is doing.
-	Ofinno thinks that we can at least consider this just for some capability and not all use cases.    Xiaomi also supports and it doesn’t mean this is mandatory.   This principle has been agreed for positioning already and it works.
-	Mediatek doesn’t think this is a discussion on optional or mandatory.
-	Samsung thinks that we need to solve the 5G problem and this is the first step.  Otherwise we have the same situation.
-	Ericsson thinks that this can be considered for some cases and it is too soon to make such decisions.   Nokia agrees.
-	ZTE thinks that we need to add restrictions that the UE is not allowed to do autonomous fallback and the network should at least be able to configure timers if there are timers.
-	Tmobile also thinks that the network needs to control the behavior.
-	LG thinks that a network response should be expected by the UE and this way we can avoid autonomous fallback.
-	Lenovo thinks that proposal 4 makes sense but we do be careful with the issue from Docomo and we should also do it along with P8. And the network should have some intention to rectrify the situation.
-	Mediatek thinks that if we have a configuration of capability change then we will have autonomous fallback.
-	ZTE would really hope that the UE won’t do any autonomous UE behaviour before sending this indication.    Xiaomi thinks that we didn’t consider it in RRC configuration failure that the UE will not do autonomous fallback before capability change.    Mediatek thinks that we can’t yet decide as we need to understand how the full solution works as they don’t want the UE to explode.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.2.1-p005`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.2.1 UE capability framework

```text
Discuss whether sending an updated version of the complete capability container is an agreeable approach to indicating the need for a capability update.
-	Qualcomm and LG agrees with this approach.
-	Docomo has two concerns, 1) reporting whole capability impacts capacity and it is a lot of overhead and also wonders if the UE has to do the full configuration or just delta.   CMCC and CATT has similar concerns.
-	CATT thinks that the UE can also provide preferred configuration.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.2.1-p006`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.2.1 UE capability framework

```text
A response message to the capability update is defined for all use cases.  FFS what message is used.
-	Lenovo thinks that this is important
-	ZTE thinks that sometimes the UE capability is for the future so the network may not need to give a response as it is impacting a future configuration and it should be up to the network how to react.
-	Ericsson thinks that even for proactive case the network can reply and it is just indicating whether the network will address it or not.
-	Huawei also thinks that this is a good start, but we don’t need to discuss the details for example this will be addressed or it won’t because of other consideration.    And if there is a reject then this may give the UE the ability to do a fallback.  Samsung thinks that it is not a reject it is just allowing the UE to fallback.
-	Samsung and Oppo would like to avoid reject.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.2.1-p007`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.2.1 UE capability framework

```text
Power saving is considered as an additional use case for capability update.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.2.1-p008`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.2.1 UE capability framework

```text
IDC is considered as an additional use case for capability update.
-	Huawei asks why IDC as implementation specific solution is already used and 3GPP is not impacted.  Samsung thinks that we can now use a standardized solution that works for IDC.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.2.1-p009`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.2.1 UE capability framework

```text
Further discuss whether capability update is needed for proper handling of foldable phones.
-	Samsung thinks that this should be handled similar to the other use cases.
-	Oppo thinks that this is an instantaneous change and it can be handled as a MIMO change.   Xiaomi thinks that it would be good for the network to know that this is because of UE capability change.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.2.1-p010`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.2.1 UE capability framework

```text
Additional use cases can be discussed in the future as their requirements become clear, and the capability change framework should strive for forward compatibility for such use cases.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.2.1-p011`

### [6G/Rel-20 RAN2#133] `observation` 10.2.1 UE capability framework

```text
Dynamic capability 1) will not increase overhead caused by re-generation of the supported BC list, 2) can reach mutual interests of both UEs and networks by reporting state-of-fact UE capability, the configuration(s) can be up to network implementation by respecting to the change of UE capability, 3) can consider to indicate the root cause of capability change together with the changed capability.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.1-o001`

### [6G/Rel-20 RAN2#133] `observation` 10.2.1 UE capability framework

```text
Spreading capabilities across multiple specifications has shown to be laborious and resulted in discrepancies that led to incorrect product implementations.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.1-o002`

### [6G/Rel-20 RAN2#133] `observation` 10.2.1 UE capability framework

```text
UE radio capabilities can be very large and can exceed the allowable size of a single UL RRC message size.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.1-o003`

### [6G/Rel-20 RAN2#133] `observation` 10.2.1 UE capability framework

```text
In 5G, UE capabilities were reported as a largely flat and comprehensive set, without a clearly defined minimum baseline shared by all devices, leading to market fragmentation and excessive IoT testing.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.1-o004`

### [6G/Rel-20 RAN2#133] `observation` 10.2.1 UE capability framework

```text
In 5G, UE capability signalling reports the full capability information, even though a large number of features are commonly supported in most devices.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.1-o005`

### [6G/Rel-20 RAN2#133] `observation` 10.2.1 UE capability framework

```text
In 5G, UE capabilities were signalled using tightly coupled and deeply nested structures (e.g. per-band, per-band-combination capabilities), which limited reuse of common capability information and caused repeated signalling of identical values across bands and combinations.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.1-o006`

### [6G/Rel-20 RAN2#133] `proposal` 10.2.1 UE capability framework

```text
RAN2 agrees the following problems identified that can cause signalling overhead and complexity:
-	Problem 1: Significant capability signalling size
-	Problem 2: Inefficient network filtering
-	Problem 3: Impractical RACS
-	Problem 4: Massive optional features that are not deployed/commercialized
Problem 1
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.1-p001`

### [6G/Rel-20 RAN2#133] `proposal` 10.2.1 UE capability framework

```text
RAN2 agrees the following root causes identified for Problem 1 ‘significant capability signalling size’:
-	Problem 1: Significant capability signalling size
	(19/19) Root cause 1: With the understanding that finer granularity cannot be avoidable according to different UE implementation for some features, Duplicated/redundant signalling was reported due to the same capability value shared across different bands and/or band combinations (e.g., due to inefficient BC structure (e.g., multiple bandwidth classes, fallback groups, etc), some band/BC sharing the same capability, improper use of finer granularity, etc);
	(19/19) Root cause 2: Complexity and overhead of UL Tx switching capability reporting (e.g., duplicate band combination list and BC capabilities between normal CA BC and UL Tx Switching, ambiguity of fallback rules, introduction of LBCA in later release, etc);
	(17/17) Root cause 3: Infrequent-reused FeatureSetCombination (e.g., due to loss of flexibility to reuse small sets of FeatureSet, etc).
-	Oppo thinks that BC should be decided by RAN4.  Xiaomi agrees but from a signalling point of view that is a root cause, so we need to discuss how to address it.
-	ZTE thinks that root cause 1 combines everything together, but we should prioritize the issue and maybe better to divide in two parts.
-	Nokia also thinks that we should prioritize and what to focus on first.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.1-p002`

### [6G/Rel-20 RAN2#133] `proposal` 10.2.1 UE capability framework

```text
For Problem 1, RAN2 agrees the following study areas in RAN2:
	(19/19) With the understanding that finer granularity cannot be avoidable according to different UE implementation for some features, study methods/principles and signalling reduction gain to 1) simplify reporting of capabilities with same value across bands/band combinations, 2) avoid using finer granularity for UE envelop limitation and 3) avoid overclassified capability. The basic concept of band/band combination (including BW class, FBG, etc), feature design, RF requirement, UE capability granularity of RAN1/4 features are up to RAN1/4, RAN2 to focus on signalling structure design;
	(19/19) Study how to reduce redundant capability reporting for capabilities with xDD/FRx difference, depending on whether feature(s) with xDD/FRx will be introduced in 6G by RAN1/2/4;
	(19/19) Study a unified spectrum aggregation capability framework (e.g., for CA, UL Tx switching, LBCA with switching, etc). The feasibility of unified framework of spectrum aggregation is up to RAN1/4.
	Study methods to reuse reporting of capabilities if the same capability applies for both normal CA BC and UL Tx switching.
	(17/17) Study an efficient structure that can be extensively reused by multiple bands/band combinations whenever needed, where this structure represents a group of repeated FeatureSet: RAN2.
	RAN2 postpone the discussion on DL/UL Decoupling from capability signalling point of view, due to no consensus on whether spectrum aggregation (DL/UL decoupling) has any impact to flexible pairing of DL/UL within a FSC or not.
-	Huawei points out that we are not talking about doing the feature but rather the signaling design.  Xiaomi explains that there is a camp that we can decouple from RAN2 signaling anyways and it is not related to the feature, but there is another camp that feels it would impact the actual design.
-	Oppo and Vivo think that there are RAN1/RAN4 depedencies.  Xiaomi explains that we are just agreeing to study and not necessarily who and when it will be done.  Ericsson doesn’t think that this is RAN4/RAN1.  It is related to signaling and we need to look into it, otherwise no one else will look at it.  Once we have found out the details and which previous decisions led to capability size increase.
-	ZTE agrees with Ericssons point and we need to agree to 5G pain points and what we can do for 6G.  ZTE also thinks that we need to focus on what is most critical. Qualcomm thinks that we can leave it open for companies to bring results/gains for other non prioritized topics.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.1-p003`

### [6G/Rel-20 RAN2#133] `proposal` 10.2.1 UE capability framework

```text
RAN2 to study the benefit and whether to support RACS in 6G Day 1 considering the followings:
-	Design principle in 6G (if supported):
	RACS-ID should be flexible to be reused and avoid covering all capabilities of a UE;
	RACS-like solution should reduce coordination challenges and maintenance burden;
-	Study areas (if supported):
	Proper granularity of RACS ID
	Retrieval framework of RACS-based capability
-	Coordination with SA2 if needed.
-	CATT thinks we can study but whether to support it should be an SA2 issue.  CMCC, ZTE, thinks that we may not depend on SA2 and it may be managed by RAN.
Problem 4
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.1-p004`

### [6G/Rel-20 RAN2#133] `proposal` 10.2.1 UE capability framework

```text
RAN2 agrees the following root causes identified for Problem 4 ‘Massive optional features that are not deployed/commercialized’:
	Root cause: Multiple options are introduced to the same functionality and too many optional components defined for single feature/function.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.1-p005`

### [6G/Rel-20 RAN2#133] `proposal` 10.2.1 UE capability framework

```text
To solve problem 4, RAN1/RAN2/RAN4 should strictly follow ‘minimizing the adoption of multiple options for the same functionality’ as in 6G SID.
Problem 5
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.1-p006`

### [6G/Rel-20 RAN2#133] `proposal` 10.2.1 UE capability framework

```text
RAN2 to down-selects from the following way-forwards for commercialization challenges:
Way-forward 1: RAN2 sends LS to RAN on the progress of commercialization challenges:
-	RAN2 confirms the agreeable root causes are commercialization challenges.
	Agreeable Root cause 2 (11/19 agree, 4/19 plenary discussion without agree/disagree, 2/19 with comment, 2/19 disagree but should be discussed in plenary):
	Mandatory feature is only mandating user equipment to implement, but not for the network, and further leads to losing tracking of ecosystem supported features in 3GPP. This makes difficult to guarantee the degree of forward compatibility.
-	CMCC doesn’t agree with this problem as we can specify ourself which one is mandatory or not.   ZTE agrees and explains it depends on regional requirement.  The problem that this is not done in 3GPP and this gives the wrong impression that this is a 3GPP problem.
-	Nokia thinks that we should at least capture something in the TR.
-	ATT thinks that majority think this is an issue so we should capture it.
-	Qualcomm thinks that we can discuss in plenary but doesn’t want the plenary discussion to stall because RAN2 didn’t agree.
-	Tmobile has internal requirements on what is requirement so not sure this is a problem.
	How to resolve the above root cause should be discussed in RAN.
-	RAN2 also confirms the dis-agreeable root causes are not considered as commercialization challenges.
	Not considered Root cause
	(17/18) (root cause 1) No differentiation between non-trivial feature(s) and other feature(s). This further leads to under-reporting/finer granularity UE capability reporting used in 5G for the purpose of addressing individual deployment and infra vendors, but increases signalling overhead (as discussed in Problem 1)
	(13/18) (root cause 4) Interoperability issue even after IoDT test is done, due to incompatibility to specification, insufficient tests covering the problematic case(s), lack of IoDT between vendors, etc.
-	RAN2 also discussed below root cause, but there’s no consensus in RAN2.
	No consensus Root cause
	Root cause 3 (7 consider, 10 not consider) Late deployment to wait for ‘slowest’ network vendor before activating a capability in operator’s network, due to no differentiation treatment of different vendors;
	RAN2 thinks whether to consider root cause 3 as commercialization challenges and how to resolve the identified root causes should be discussed in RAN.
Way-forward 2: RAN2 will not continue the discussion on commercialization challenges.
-	Continue discussion in RAN:
	Root cause 2: (11/19 agree, 4/19 plenary discussion without agree/disagree, 2/19 with comment, 2/19 disagree but should be discussed in plenary) Mandatory feature is only mandating user equipment to implement, but not for the network, and further leads to losing tracking of ecosystem supported features in 3GPP. This makes difficult to guarantee the degree of forward compatibility.
	Root cause 3: (7 consider, 10 not consider) Late deployment to wait for ‘slowest’ network vendor before activating a capability in operator’s network, due to no differentiation treatment of different vendors;
-	Not considered Root cause
	(17/18) (root cause 1) No differentiation between non-trivial feature(s) and other feature(s). This further leads to under-reporting/finer granularity UE capability reporting used in 5G for the purpose of addressing individual deployment and infra vendors, but increases signalling overhead (as discussed in Problem 1)
	(13/18) (root cause 4) Interoperability issue even after IoDT test is done, due to incompatibility to specification, insufficient tests covering the problematic case(s), lack of IoDT between vendors, etc.
R2-2601306	Report of [AT133][004][6G] UE capability	Xiaomi	discussion	Rel-20	FS_6G_Radio
Noted
Agreements on UE capability framework
1.   RAN2 agrees the following problems identified that can cause signalling overhead and complexity:
-	Problem 1: Significant capability signalling size
-	Problem 2: Inefficient network filtering
-	Problem 3: Impractical RACS
-	Problem 4: Massive optional features that are not deployed/commercialized
2. 	Problem 1: Significant capability signalling size
-	Root cause 1: With the understanding that finer granularity cannot be avoidable according to different UE implementation for some features, Duplicated/redundant signalling was reported due to the same capability value shared across different bands and/or band combinations (e.g., due to inefficient BC structure (e.g., multiple bandwidth classes, fallback groups, etc), some band/BC sharing the same capability, improper use of finer granularity, etc);
-	Root cause 2: Complexity and overhead of UL Tx switching capability reporting (e.g., duplicate band combination list and BC capabilities between normal CA BC and UL Tx Switching, ambiguity of fallback rules, introduction of LBCA in later release, etc);
-	Root cause 3: Infrequent-reused FeatureSetCombination (e.g., due to loss of flexibility to reuse small sets of FeatureSet, etc).
3.	For Problem 1, RAN2 agrees the following study areas in RAN2:
-	With the understanding that finer granularity cannot be avoidable according to different UE implementation for some features, study methods/principles and signalling reduction gain to 1) simplify reporting of capabilities with same value across bands/band combinations, 2) avoid using finer granularity for UE envelop limitation and 3) avoid overclassified capability. The basic concept of band/band combination (including BW class, FBG, etc), feature design, RF requirement, UE capability granularity of RAN1/4 features are up to RAN1/4, RAN2 to focus on signalling structure design;
-	Study how to reduce redundant capability reporting for capabilities with xDD/FRx difference, depending on whether feature(s) with xDD/FRx will be introduced in 6G by RAN1/2/4;
-	Study a unified spectrum aggregation capability framework (e.g., for CA, UL Tx switching, LBCA with switching, etc). The feasibility of unified framework of spectrum aggregation is up to RAN1/4.
-	Study methods to reuse reporting of capabilities if the same capability applies for both normal CA BC and UL Tx switching.
-	Study an efficient structure that can be extensively reused by multiple bands/band combinations whenever needed, where this structure represents a group of repeated FeatureSet, considering uplink and downlink separation in BC signalling and feature set combination.
4.	RAN2 agrees the following root causes identified for Problem 2 ‘Inefficient network filtering’
-	Root cause: 5G network filtering didn’t provide sufficient/appropriate information to UE for 1) filtering capabilities with common interests between network and UE and 2) reducing capability size effectively.
5.	For network filtering, RAN2 agrees the following study areas:
-	 Study proper finer filtering to reduce capability signalling size in single report, considering the balance between signalling size and re-enquiry: RAN2
-	Study the solutions to avoid UE omitting network interested capabilities when capability signalling size is more than UL RRC message (including when segmentation is supported): RAN2
-	RAN2 waits for clear definition of 1) 6G band/band combination, 2) features to be supported in 6G and 3) device type to be supported in 6G, and then studies on the above study areas.
6	RAN2 to study the benefit considering the followings:
-	Design principle in 6G (if supported):
	RACS-ID should be flexible to be reused and avoid covering all capabilities of a UE;
	RACS-like solution should reduce coordination challenges and maintenance burden;
-	Study areas (if supported):
	Proper granularity of RACS ID
	Retrieval framework of RACS-based capability
-	Coordination with SA2 if needed.
7	RAN2 agrees the following root causes identified for Problem 4 ‘Massive optional features that are not deployed/commercialized’:
-	Root cause: Multiple options are introduced to the same functionality and too many optional components defined for single feature/function.
-	To solve problem 4, RAN1/RAN2/RAN4 should strictly follow ‘minimizing the adoption of multiple options for the same functionality’ as in 6G SID
8	IODT and commercialization discussions are moved to the plenary, as they are outside of RAN2 scope.
9.	RAN2 will further discuss how and if to prioritize and how to proceed with the work…
10.	Based on progress decide to send LS to RAN1/4 once RAN2 has sufficient progress. RAN1/4 6G study should be taken into account based on RAN1/4
11	For problem 1, RAN2 prioritizes the following study areas:
-	Solution to simplify reporting of capabilities with same value across bands/band combinations;
-	Study a unified spectrum aggregation capability framework (e.g., for CA, UL Tx switching, LBCA with switching, etc)
-	Study an efficient structure that can be extensively reused by multiple bands/band combinations whenever needed, where this structure represents a group of repeated FeatureSet, considering uplink and downlink separation in BC signalling and feature set combination.
-	Study how to avoid using finer granularity for UE envelop limitation
The following study areas are deprioritized:
-	Solution to reduce redundant capability reporting for capabilities with xDD/FRx difference
-	Methods/principles to avoid overclassified capability
12	For problem 3, RAN2 will look into solutions to understand how capability ID/retrieval mechanism works (except proper granularity of RACS ID).
[POST133][004][6G] UE capability (xiaomi)
Scope:
1.	Collect the proposed signalling optimizations/solution for the prioritized study areas.
For Problem 1: UE capability signalling until Rel-19 is considered as baseline. For each solution, companies are welcome to provide:
-     Examples on how capability signalling is optimized (before and after), including encoding (if possible). Examples include at least examples collected for the prioritized study areas in R2-2600118.
-     	Signalling reduction gain
For Problem 3: collect solutions for how capability ID/retrieval mechanism works (except proper granularity of RACS ID).
2.	Discuss general principles to RAN1/4 to follow for 6G feature list and capability discussion. Discuss LS to other WGs.
Intended outcome: Discussion report
Deadline:  Long
Capability update
R2-2600836	Discussion on dynamic UE capability update	Ericsson, Qualcomm Incorporated, Charter Communications, Jio Platforms Limited, Verizon, T-Mobile USA, NTT DOCOMO INC, Turkcell	discussion
Proposal 1	RAN2 should define indications of reduced UE operation for critical use cases and simplify the indications where possible and appropriate for the intended use cases.
Proposal 2	The overheating indication can be sent in a UAI-like message. RAN2 should evaluate which fields to include considering real issues seen in field.
-	Samsung asks what is critical.  Ericsson thinks that overheating is critical but it should be done via UAI.
Proposal 3	For multi-SIM the UE can indicate an updated UE capability container.
Proposal 4	Prohibit timers should be used to avoid too frequent toggling of UE capabilities for MUSIM. And testcases should be defined to ensure the integrity of these features.
[2 mins]
Noted
R2-2600119	Necessity of Dynamic Capability Reporting	Xiaomi, Sharp, Ofinno, Apple, MediaTek Inc., Samsung, LG Electronics Inc., Fujitsu, Kyocera, Lenovo	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.1-p007`

### [6G/Rel-20 RAN2#133] `proposal` 10.2.1 UE capability framework

```text
Dynamic capability supports changes of UE’s capabilities for the use cases associated to overheating, power consumption constrains, and changes on the hardware requirements (e.g., MUSIM, IDC, AI/ML processing unit, etc). If so, Table 1 is used as starting point (baseline) for RAN2 to discuss/identify justification and requirements for capability change in 6G. FFS on other dynamic capability use case.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.1-p008`

### [6G/Rel-20 RAN2#133] `proposal` 10.2.1 UE capability framework

```text
RAN2 confirms UAI is not sufficient for UE’s capability change reporting considering the following pain points:
-	(1) UE reporting is controlled by network (i.e., UE is only allowed when configured by network),
-	(2) UE’s expectations of the network behaviour upon reception of UAI message is unclear (i.e., unspecified) and the concerned problem cannot be resolved,
-	(3) UAI provides preferences on RRC configurations instead of capability change,
-	(4) UAI reporting is per feature.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.1-p009`

### [6G/Rel-20 RAN2#133] `proposal` 10.2.1 UE capability framework

```text
Dynamic capability update needs to 1) consider track-off between network control and UE’s constrains/implications and 2) define behaviour for both network and UE, by addressing the above Study Areas 1-4:
-	Area 1: Expected network behaviour to reconfigure/de-configure according to UE updated capability, and consequence of not following dynamic capability change, including UE behaviour(s) if dynamic capability update is not respected/responded by network;
-	Area 2: Whether dynamic capability is reported to RAN only or CN as well;
-	Area 3: Procedure of dynamic capability and its retrieval framework during handover and cell-reselection;
-	Area 4: Reporting format of dynamic capability, e.g., separate parameter IEs, container, or UE radio capability ID.
[3 mins]
Noted
Discussion
-	Huawei thought the action point was to discuss the use cases and similar to ericsson overheating and MUSIM are the critical use cases.   UAI is technically feasible but we can address the problem of UAI.
-	Oppo also agrees that MUSIM and overheating are critical.  But we have AI/ML that we haven’t fully understood the problem.   Xiaomi explains that we have discussed applicability reporting and this we can consider sending this indication via capability.
-	Nokia thinks the focus should be on commercialized cases so we should understand the problems that led to commercialization.   We should not discuss AI/ML yet, so let’s focus on overheating and MUSIM.
-	CMCC thinks we should discuss the detailed parameters and whether it is AS or SA too.
-	Jio supports that this capability should be supported for CN.
-	Mediatek thinks that we shouldn’t narrow down the discussion on only two use cases as we should think of possible use cases in the future as we may run into the same problem as 5G in future.   Samsung agrees with Mediatek.
-	Xiaomi agrees that we have two categories – 1) scheduler related (e.g. UE overheating) and 2) hardware/RF change  (e.g. MUSIM).   Sony thinks we can start with use cases and separate the discussion on the mechanism needed for it.   Ideally we would have the same solution and not different ones for different use cases.
-	Qualcomm thinks that we need to discuss on what the UE expects from the network.
-	Apple understands the desire to limit but we should address the issues with UAI.
-	CATT agrees to limit the usecases and start with UAI.  We should discuss how we can verify what the UE is indicating.  Mediatek reminds everyone that the KPIs of the UE would suffer so it wouldn’t unnecessarily report things.  So we should trust the UE, we should categorize, what the UE can do and network has discretion and cases where the UE has a limitation on what it can support.
Agreements on dynamic UE capability
Start the study at least considering two main use cases, overheating and MUSIM.  This doesn’t mean that other use cases will not be studied.
[POST133][005][6G] Dynamic capability reporting (Mediatek)
Intended outcome:
1) Discuss for the two family of uses cases the pain points/requirements and attempt to categorize/define the two families.
2) Discuss for the two use cases what is the expected behavior from UE and network?
3) Identify new cases and attempt to categorize the two families
Deadline:  Long
Not treated
Capabilities specification
R2-2600924	Discussion on 6GR capability framework	Nokia	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.1-p010`

### [6G/Rel-20 RAN2#133] `proposal` 10.2.1 UE capability framework

```text
Study how to capture all capability aspects in one technical specification to simplify specification, maintenance, and implementation of the 6GR UE capabilities.
Signalling structure  (if time allows)
R2-2600924	Discussion on 6GR capability framework	Nokia	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.1-p011`

### [6G/Rel-20 RAN2#133] `proposal` 10.2.1 UE capability framework

```text
Study scalable design for UE capability signalling with the objective of ensuring the UE capability container fits into a single UL RRC message.
R2-2600263	On compact capability signaling design and reporting	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.1-p012`

### [6G/Rel-20 RAN2#133] `proposal` 10.2.1 UE capability framework

```text
RAN2 to study the flexible signaling design allowing the UE to report the typical/common capability in coarse granularity while using the optional signaling in finer granularity to indicate the differentiation (out of the common baseline).
R2-2600190	Considerations on 6GR UE Capability	CATT	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.1-p013`

### [6G/Rel-20 RAN2#133] `proposal` 10.2.1 UE capability framework

```text
RAN2 to study reducing the overhead of capability signaling via UE capability message compression.
R2-2600776	Design of 6GR UE capabilities	InterDigital, Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.1-p014`

### [6G/Rel-20 RAN2#133] `proposal` 10.2.1 UE capability framework

```text
6GR UE capability design should include a minimum baseline capability set supported by all UEs, and device-type specific mandatory capability sets.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.1-p015`

### [6G/Rel-20 RAN2#133] `proposal` 10.2.1 UE capability framework

```text
Optional feature indicators can be used to signal differences (“delta”) relative to the baseline device-type capability set.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.1-p016`

### [6G/Rel-20 RAN2#133] `proposal` 10.2.1 UE capability framework

```text
Support module-based capability reporting and configuration procedures using delta and reference profiles.
R2-2600072	Further discussion on 6GR UE capability framework	vivo	discussion	Rel-20
R2-2600108	UE Capability pain points and considerations	Xiaomi	discussion	Rel-20	FS_6G_Radio 	Withdrawn
R2-2600129	Discussion on 6G UE Capability	OPPO	discussion	Rel-20	FS_6G_Radio
R2-2600137	6G UE capability framework	Qualcomm Incorporated	discussion	Rel-20
R2-2600408	Data transfer design for 6GR Access Technology	Hanbat National University	discussion	Withdrawn
UE capability framework for 6G	Samsung	discussion	Rel-20	FS_6G_Radio
R2-2600475	Considerations on UE capability framework in 6G	Apple	discussion	Rel-20	FS_6G_Radio
R2-2600530	Discussion on 6G UE capability framework	NTT DOCOMO INC.	discussion	Rel-20
R2-2600592	Consideration on dynamic UE capability update	DENSO CORPORATION	discussion
R2-2600605	Discussion on UE capability aspects in 6G	Fujitsu	discussion	Rel-20	FS_6G_Radio
R2-2600619	Efficient 6G UE Capability Signalling	KT Corp.	discussion	Rel-20	FS_6G_Radio
R2-2600681	Discussion on 6G UE capability	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
R2-2600724	Discussion on dynamic UE capability change	NEC	discussion	Rel-20	FS_6G_Radio
R2-2600759	Discussion on 6GR UE capability	Sony	discussion	Rel-20	FS_6G_Radio
R2-2600813	6GR UE Capability Framework	SHARP Corporation	discussion
R2-2600851	UE capability framework in 6G	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2600889	UE Capability Focus Areas based on Identified Pain Points and Root Causes	AT&T	discussion	FS_6G_Radio
R2-2600912	UE Capability Signaling Considerations for Heterogeneous Deployments 	Jio Platforms	discussion	Rel-20	FS_6G_Radio
R2-2600913	Considerations on UE Capability Signaling and RACS for 6G	Jio Platforms	discussion	Rel-20	FS_6G_Radio
R2-2600914	Considerations on RACS Identifier Usage in Multi-PLMN Deployments	Jio Platforms	discussion	Rel-20	FS_6G_Radio
R2-2600932	Discussion on UE Capability Framework	Futurewei Technologies	discussion	Rel-20
R2-2600947	Considerations on UE capability framework for 6GR	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2601023	Perspectives on UE Capability for 6G	ETRI	discussion
R2-2601032	Consideration on 6G UE Capability	ZTE Corporation	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.1-p017`

### [6G/Rel-20 RAN2#132] `observation` 10.2.1 UE capability framework

```text
band and BCs are key factors in the increased UE capability signaling size, however the definition of band and BCs may be changed by new concept/feature in 6G (i.e., band group and single cell with multiple carrier) depending on discussion in RAN1/RAN4.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-o001`

### [6G/Rel-20 RAN2#132] `observation` 10.2.1 UE capability framework

```text
FS, FSPC and FSC are used to efficiently indicate band/BC dependent capabilities but couldn’t cover all baseband dependent capabilities in 5G.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-o002`

### [6G/Rel-20 RAN2#132] `observation` 10.2.1 UE capability framework

```text
optional capabilities especially in BC in each release/version increases UE capability signaling overhead. There might be room to reduce optional capabilities if we can consider differentiation per feature level or dependency between feature groups from WGs.
[2mins]
Noted
Filtering and RACS (Not treated)
R2-2509032	Discussion on UE capability framework	Deutsche Telekom AG	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-o003`

### [6G/Rel-20 RAN2#132] `observation` 10.2.1 UE capability framework

```text
Band combination capability information for CA/DC dominates capability information size, but current filtering (RAT/band/cell-group) are too coarse. Per-BC filtering is needed to avoid composing unused BCs on the current serving cell.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-o004`

### [6G/Rel-20 RAN2#132] `observation` 10.2.1 UE capability framework

```text
When capability enquiries including same band filtering which was required before, the UEs should re-compose identical band/feature-set information because feature set IDs and feature set combination IDs are report-instance scoped.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-o005`

### [6G/Rel-20 RAN2#132] `observation` 10.2.1 UE capability framework

```text
The network may request wide BC capability information upfront for future CA/DC configuration, but much of it is never used before the stored capability is discarded.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-o006`

### [6G/Rel-20 RAN2#132] `observation` 10.2.1 UE capability framework

```text
There are multiple different motivations to support dynamic UE capability updates during the connected state, and these should be studied separately by categorizing the reasons for capability changes.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-o007`

### [6G/Rel-20 RAN2#132] `observation` 10.2.1 UE capability framework

```text
RAN2 needs to ensure consistent interpretation of “dynamic UE Capabilities changes”: whether it relates to UE (in)ability to perform according to the applied configuration or previously declared capabilities.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-o008`

### [6G/Rel-20 RAN2#132] `observation` 10.2.1 UE capability framework

```text
The absence of RRC Reconfiguration in response to UAI does not preclude responsive network behaviour or adaptation at lower layers.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-o009`

### [6G/Rel-20 RAN2#132] `observation` 10.2.1 UE capability framework

```text
The use cases associated with UAI involve only temporary modification of the configuration in RAN without impacting CN.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-o010`

### [6G/Rel-20 RAN2#132] `observation` 10.2.1 UE capability framework

```text
NR already supports form factor changes (e.g. folding phones) at lower layers without change of UE capabilities.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-o011`

### [6G/Rel-20 RAN2#132] `observation` 10.2.1 UE capability framework

```text
The commercialization of capability restriction/updates based on UE Assistance Information (UAI) was not successful in 5G, due to the following issues:
	Lack of consideration of the mutual interests of both UEs and networks.
	The inability to verify the real cause of the UE’s behaviour when requesting capability restrictions, which could lead to misuse, where UEs improperly reduce their capabilities.
	Capability restriction/updates may significantly affect communication performance, making it difficult to meet the QoS requirements in some scenarios.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-o012`

### [6G/Rel-20 RAN2#132] `observation` 10.2.1 UE capability framework

```text
Per the current implementation, to verify the features through IODT test with some given vendors before the UE/chipset activate the features in operator’s deployed network is already supported in CMCC.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-o013`

### [6G/Rel-20 RAN2#132] `observation` 10.2.1 UE capability framework

```text
In commercial environments, problems exist that only occur on specific UE models and specific UE software versions.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-o014`

### [6G/Rel-20 RAN2#132] `observation` 10.2.1 UE capability framework

```text
Due to these specific problems, other users may be deprived of opportunities for quality improvement.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-o015`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
A globally aligned and normatively specified procedure should ensure features are not just declared as mandatory, but deployment of these (and other features) is tracked in 3GPP with a binding procedure for both the network and the user equipment.
-	LG asks what does binding mean.   ATT thinks that we now mandate the UE but not the network so the intention is to mandate features on the network side as well.
-	Xiaomi asks how the tracking will be done.  ATT thinks we need to define a framework.
-	Mediatek thinks that this can be beneficial if we find a good way to do it.
-	Samsung asks what is the role of RAN2 so we have to look at the whole procedure with all the other WGs.  Oppo agrees with Samsung.   ATT acknowledges that this a joint effort amongst the working groups.
-	Docomo supports these proposals.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p001`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
Basic feature groups should be defined to ensure implementation, certification, and deployment of large numbers of features as components of a single feature group, rather than specifying a myriad of individual feature groups for a small number, and often a single component. These basic feature groups together define a meaningful, minimum set of features that are globally aligned among operators.
-	Xiaomi asks what is the criteria to determine the basic feature group.   ATT thinks that this needs to be an effort to determine globally what is the minimum set of features.
-	Mediatek is concerned that this may imply that we make a lot of mandatory features, so we should be careful.
-	Samsung thinks that we need to do better with how we define capabilities, but it is not just for minimum capabilities.
Noted
Overhead
BC, FS, FSC, UL/DL decoupling, etc
R2-2508076	UE Capability pain points and considerations	Xiaomi	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p002`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
RAN2 to study solutions for the following pain points of 5G UE capability framework:
-	Pain point 1: Significant capability signalling size
	Root cause 1: complex BC signalling structure;
	Root cause 2: complex RF requirement;
-	Apple thinks that we can not assume that RAN1/4 will not have complex requirements.  Xiaomi agrees that in some cases it can’t fully be solved, but there are a few things/examples we can highlight to them.
	Root cause 3: redundant reporting
	BC capabilities for BC and BC-UplinkTxSwitch;
	Capabilities reported consistently across all/some bands;
	Capabilities with finer granularity repeatedly reported the same value across band/BC;
-	Pain point x - massive optional features and unnecessary introduction of capabilites
-	Qualcomm thinks that this is not related to signaling size but complexity.  Xiaomi thinks we can turn it into a pain point.
	Root cause 5: unnecessary introduction of capabilities
-	Pain point 2: Asymmetric UL/DL capability cannot be supported in 1:1 DL/UL mapping FeatureSet framework;
-	Pain point 3: Non-forward compatible signaling structure design, e.g., band combination, power class, etc;
-	Pain point 4: Duplicate retrieval framework with/without RACS;
-	Pain point 5: Impractical RACS ID;
-	Pain point 6: Mismatch between UE and NW supported features;
-	Pain point 7: Capability without corresponding network configuration.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p003`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
For pain point 1-4, RAN2 sends LS to RAN1/RAN4 and ask RAN1/4 to consider pain point 1-3 and root causes in 6G system design requirement for capability signaling size reduction. RAN2 to discuss capability signalling structure simplification in later phase of SI based on feedback from RAN1/4.
-	Lenovo asks what is the intention as painpoints come from other WGs.   Xiaomi agrees and the intention is to agree on the pain points and ask RAN1/4 to avoid them in 6G
-	Ericsson thinks that we can need to discuss the pain points a bit in more details and give them examples.    Xiaomi is hesitant for example but we should think on better way to demonstrate the pain points.
-	ZTE would like to identify which ones are RAN1/4 and we should also focus on the UL and DL.   CATT thinks 1-3 is RAN1/4 and the others can be focused in RAN2.
-	Oppo is reluctant to agree the pain points as they are.
-	Samsung thinks that we can group aspects to different categories, and we need to understand whether RAN4 will introduce new concept.   The granularity and structure can be discussed by RAN2 first.
-	Ofinno thinks that we can just tell RAN1/RAN4 that we have identified overhead issues.
-	Tmobile agrees that BC is a problem and NSA as well, and assume SA is the baseline.
-	Mediatek thinks that is important that RAN1/RAN4 understands that if the capabilities are complex we can’t compress them to a reasonable size.  So we have to influence on what comes to us so the task is easier.   We should target to have an LS by February.
-	ZTE thinks that some pain points have different level of impact to the complexity.  It is better to provide some suggested solutions.   Xiaomi thinks that it won’t work as they are considering different framework.
-	Oppo thinks that RAN4 has to worry about much more than signaling overhead.   We can capture the pain point and which WGs it impacts, but it doesn’t mean that it will change their solution.
-	Vivo thinks we should go one level lower and provide some requirements to them.
-	Ericsson thinks we can give them some detailed inputs and examples.
-	Nokia thinks that after the pain points we can decide what to focus on RAN2.
[3mins]
Noted
Identify and capture the pain point issues (including root causes).   Identify what RAN2 can focus on and which ones impact other WGs.   Find a way to provide examples or demonstrate the identified pain issues to other WGs
FFS next meeting if we send an LS to other WGs
[POST132][008][6G] UE capability pain points (Xiaomi)
Intended outcome: Identify and capture the pain point issues (including root causes).   Identify what RAN2 can focus on and which ones impact other WGs.   Find a way to provide examples or demonstrate the identified pain issues to other WGs.
Identify what contributes the most to the overhead/complexity
Deadline:  Long
R2-2508876	UE capability framework for 6G	Samsung	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p004`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
RAN2 check with RAN1/RAN4 on general timeline for CA/band/BC structures in order for RAN2 to plan for the enhancement of UE capability signaling structure.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p005`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
RAN2 discuss a general structure for band + BC dependent capabilities (e.g. FS, FSPC, FSC, etc.) for 6G and share with RAN1/RAN4 to get their feedback during study item.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p006`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
RAN2 discuss a general guidance in defining multiple UE capabilities for a feature in order to avoid too many optional UE capabilities.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p007`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
RAN2 should work on minimizing the number of options/features by avoiding duplications, merging subvariants, joining dependent features, etc.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p008`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
RAN2 should evaluate RACS solution and possible enhancements required for mobility case (i.e., shift of the “UCMF-like” functionalities to the Base Station).
[2mins]
R2-2508732	Improvements for UE capabilities	Ericsson	discussion
Observation 1	UE capability filtering is only useful if the UE implements a feature which no gNB in a given PLMN implements or uses. For operating bands this is often the case; for other features typically not.
Observation 2	Using per feature filters tend to increase UE capability re-enquiries.
Proposal 1	Introduce capability filters only for functionality that a) adds considerable signalling overhead and b) is likely supported by many UEs but c) used only by a subset of PLMNs (e.g. frequency bands).
Observation 3	RACS ID can reduce the number of UE capability enquires, but other aspects/solutions can have a higher impact on such reduction and should be prioritized.
[2mins]
R2-2508509	Consideration on 6G UE Capability	ZTE Corporation, Sanechips	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p009`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
The basic UE capability reporting procedure can be retained from 4G/5G, where the UE reports capabilities based on a network request. But RAN2 to study how to optimize the filtering mechanism to enable additional granularity for the filtering of UE capabilities.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p010`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
In addition to the explicit UE Capability report, RAN2 should also support UE Capability ID based reporting and should study optimizations for the UE capability ID based reporting (e.g. enhanced RACS mechanism by defining templates for parts of UE capability sets).
[2mins]
R2-2508610	6G UE Capability Framework	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p011`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
RAN2 to study defining per band combination filtering for UE capability retrieval including only particular band combination capabilities to reduce band combination related size.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p012`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
RAN2 to study an index-based linkage and delta reporting for previously reported feature set information to avoid duplication and support incremental updates. This allows the UE to reuse the reported feature set IDs and feature set combination IDs not only for identical band, but also for other bands when composing UE capability reports.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p013`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
RAN2 to study a UE initiated band combination reporting mechanism without explicit network enquiry, enabled by the network pre-provided conditions.
[2mins]
Dynamic capabilities
R2-2508422	On UE capability framework for 6G	NTT DOCOMO INC.	discussion	Rel-20	FS_6G_Radio
Dynamic capability change
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p014`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
For reasons which have a significant impact on user experience (e.g., overheating and power saving), study the framework of UE capability updates in which the UE can report it regardless of network configuration, and the network is required to respect those reports, while impact on network operation is minimized.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p015`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
For capability updates triggered by reasons other than overheating or power saving, we study them with a focus on minimizing CN involvement and reducing the impact on other procedures.
[2mins]
Noted
R2-2509073	Discussion on dynamic UE capability update	BT Plc, Ericsson, T-Mobile USA, Deutsche Telekom	discussion	Rel-20
Observation 1	In NR, “dynamic UE capabilities” is addressed by the UAI-framework but the way it is specified has caused market fragmentation and reduced its usability.
Observation 2	Dynamic capability update has several challenges and does not address the main issue regarding temporary problems and constrains in the UE.
Proposal 1	Study a unified framework to report temporary problems and constrains in the UE.
Proposal 2	Focus on solutions within UAI framework for temporary problems and constrains on the UE.
[2mins]
Noted
R2-2508322	6GR UE capability framework	Nokia	discussion	Rel-20	FS_6G_Radio
“Dynamic” capabilities:
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p016`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
Study commercialized 5G UAI issues (e.g. overheating) as the first use case, including identification of the specific requirements (e.g. when the changes need to take effect, permanency of the change, configuration handling).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p017`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
Analysis of “dynamic capability” use cases shall also consider whether other procedures, e.g. handling by RRC configuration or lower layers, can adequately meet the requirements.
[2mins]
Noted
R2-2508616	Discussion approach for 6G UE capability	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
UE capability update
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p018`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
For UE capability study at current stage, problems/issues identification are more important than debating on solutions/enhancements:
	RAN2 should initially focus on identifying issues observed in NR UE capabilities (see above 8 observations).
	Capability enhancement discussions can be postponed to a later phase in the 6G study, once 6G feature studies have made sufficient progress.
[2mins]
Noted
R2-2508445	Considerations on UE capability framework in 6G	Apple	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p019`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
For dynamic UE capability update, starting with the use cases supported by NR UAI and RRCReconfigurationComplete (NeedForGap). Other use cases identified with wide support can be considered as well.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p020`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
It is expected that network properly handles UE request on UE capability update within a defined timeline, to make sure that network and UE are synchronized in terms of the configuration during the transition period.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p021`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
If UE does not receive an updated configuration from the NW within the timeline, it could be further discussed what the UE behavior is.
[2mins]
Noted
Discussions
-	Qualcomm thinks that UAI is not a solution as it wasn’t a success in 5G, so we can’t fully rely on UAI, we need to understand the pain points.  Xiaomi agrees and there is limitation.   It is controlled by the network whether the UE can report UAI so it doesn’t work.   Also we don’t know what action the network will take.   Ericsson thinks the network control is a separate discussion as even with UEcapabilityenquiry the network is in control.   So we have discuss whether we update the UE capability container as the reconfig can be MAC CE, etc.
-	Oppo thinks that MUSIM is the most important use case.   There are some principles from UAI, for example it doesn’t impact CN capabilities.  But there are some problems with UAI.
-	Nokia thinks we should take a step back and look at what are the requirements of the use cases that require some form of capability change. And we shouldn’t preclude solutions that are based on lower layer.
-	Huawei would like to first understand the issues and should identified root cause.  There are cases where the network has no interest on the change of some of the UAI capabilities.
-	Apple also thinks in addition to overheating and power saving, MUSIM is important.  We should have expectations on how the network reacts.
-	CMCC thinks that the network should be able to control as sometimes the dynamic change may cause network performance degradation.  We should limit which capabilities can be enabled.
-	ZTE thinks that companies should elaborate on whether the reporting to the network indicates that the capability has changed or will change, what are the expectations from the network.   Xiaomi thinks that we also need to respect UE user experience so we have to consider both User and network impact.
-	Huawei thinks that we should limit the impact to RAN and no CN. Samsung thinks that we should keep it open as we may want to discuss the Idle mode as well.
For next meeting, identify important use cases for dynamic capability change.  Identify the requirements for the use cases (including the justification).  Identify pain points of UAI.
The framework should focus on RAN capability and not impact NAS capability
IODT
R2-2508044	Discussion on 6GR UE capability framework	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p022`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
To avoid the potential IODT issues crossing different regions and PLMNs, maintain the type of feature ‘mandatory with capability signalling’ in 6G.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p023`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
Study how to ensure alignment between network and UE support for mandatory features, e.g., include mandatory features of network in the specification, which should be treated as mandatory items in IODT.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p024`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
If RAN2 reaches a consensus on any IODT issue related to other WGs (e.g., RAN4, RAN5) to be addressed by 3GPP, RAN2 should trigger corresponding discussions within RANP.
[2mins]
Noted
R2-2508868	Considerations on UE capability framework in 6G	Qualcomm Incorporated	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p025`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
To address the “IODT issue”, solution where the network is provided with the served UE vendor name/ID should be avoided.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p026`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
RAN2 to study solutions where the UE is provided with the serving network vendor name/ID.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p027`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
RAN2 to study solutions where the UE reports “IOT-ed” network vendor names / IDs per main feature, within the UE radio capability.
[2mins]
-	Oppo would like to understand the issue.  Qualcomm thinks that of course the UE vendors want to IOT the feature, but the vendor doesn’t support it.   The UE supports it and all of the sudden the vendor implements.  Oppo thinks that it is not acceptable to have devices that don’t work with some UE and network vendor combinations.
-	Xiaomi shares the spirit but there are some issues that need to be addressed first like during mobility and handling of vendor ID reported.
Noted
R2-2508839	Considerations on UE capability framework for 6GR	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p028`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
Regarding the IODT issue, further enhancements are not needed.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p029`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
Inconsistency issue (e.g. RF capabilities do not match the 3GPP specification, etc.) between UE capabilities and the network needs further discussion.
[2mins]
Noted
R2-2508968	Discussion on IODT problems for 6G UE capability framework	KDDI Corporation
Discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p030`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
6G should study enabling the network to identify the UE's model and/or software version.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p031`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.1 UE capability framework

```text
6G should study enabling the network to control the applicability of a function (i.e., enable/disable) based on the UE's model and/or software version.
[2mins]
Noted
Discussion
-	Oppo would like to understand the issue.  Qualcomm thinks that of course the UE vendors want to IOT the feature, but the vendor doesn’t support it.   The UE supports it and all of the sudden the vendor implements.  Oppo thinks that it is not acceptable to have devices that don’t work with some UE and network vendor combinations.
-	Xiaomi shares the spirit but there are some issues that need to be addressed first like during mobility and handling of vendor ID reported.
-	Tmobile thinks that this is a problem in a field as there some mismatch and features are coming out before they can IODT-ed.
-	Apple thinks that this is really needed and we need two way communication.  BT agrees with TM and Apple.
-	LG is concerned that this will increase the size.
-	CMCC thinks that there is an implementation way.   Huawei agrees IMESV can be used by implementation but it is optional.  We can make it mandatory.    Lenovo explains that there is no guarantee that it has a link to capability, some vendors can do it but not guaranteed.  Huawei thinks that IMESV contains some UE vendor information and software version.   Apple thinks that this assumes that the network is good but the UEs have the problem.  But there are cases in the field where there is something that the network does, and the UE crashes.  ZTE thinks that this is more related to reconfiguration failure, so we can discuss it there.   ZTE agrees with CMCC and Huawei and if we can make it mandatory in 6G it would be great, but we still have implementation based solutions.
-	Mediatek wants to understand the root cause of the IODT issue and don’t understand what feature/function.
-	Vivo has some concerns with introducing 3GPP mechanisms as it may make us lazy as we have backup solution.
-	Samsung also would like to understand the root cause but would like to avoid vendor/implementation specific ID.
-	Ericsson thinks that IMESV is more for the case that the feature is not working for a UE and sometimes there are tons of IMESV that are effected.
-	Nokia thinks that this is a bigger discussion that RAN2 can have.   We have features that are mandatory without signaling and if there are issues with those these identification is quite useful.
-	KDDI thinks that there is a problem.
-	BT thinks that from operator point of view it is important to know what vendor is doing something so we can properly react to the problem.
Noted
Not treated
R2-2508073	Discussion on UE capability framework	Transsion Holdings	discussion
R2-2508097	Considerations on 6GR UE Capability	CATT	discussion	Rel-20	FS_6G_Radio
R2-2508145	UE capability framework considerations for 6GR	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
R2-2508113	Discussion on 6G UE Capability	OPPO	discussion	Rel-20	FS_6G_Radio
R2-2508209	6GR UE Capability Framework	SHARP Corporation	discussion
R2-2508356	Views on UE capability signaling in 6G	Charter Communications, Inc	discussion	Late
R2-2508459	Discussion on UE capability aspects in 6G	Fujitsu	discussion	Rel-20	FS_6G_Radio
R2-2508540	Discussion on 6GR UE capability	Sony	discussion	Rel-20	FS_6G_Radio
R2-2508622	Considerations on UE capability framework for 6GR	Lenovo	discussion	Rel-20	FS_6G_Radio
R2-2508624	UE Capability Framework in 6G	Ofinno	discussion	Rel-20
R2-2508668	Discussion on fundamentals of UE capability framework	NEC	discussion	Rel-20	FS_6G_Radio
R2-2508768	Design of 6GR UE capabilities	InterDigital, Inc.	discussion	Rel-20	FS_6G_Radio
R2-2508916	Discussion on UE Capability Framework	Futurewei Technologies	discussion
R2-2508937	Consideration on 6GR UE Capability	Spreadtrum, UNISOC	discussion	Rel-20
R2-2508939	Consideration on 6G UE capability framework	ETRI	discussion
R2-2508963	Discussion on UE capability framework	TCL	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.1-p032`

