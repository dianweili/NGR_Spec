# 6GR 通用设计与新业务

**当前进展** · 阶段：收敛中

RAN2 已明确 6GR Day 1 优先支持移动宽带与 Voice，并满足 emergency、positioning 和 PWS 的监管要求；IoT、sensing、AI 等其他服务需有明确市场需求和用例支撑。研究范围已涵盖沉浸式通信、ISAC、AI/ML、NTN、数字孪生及多类既有用例，并强调复用 5G 功能、采用共同设计和考虑不同计算资源部署。Tokenized AI 的流量特征、业务支持时机及 RAN2 与 SA4 的研究衔接仍在讨论；设备类型、需求归属和可扩展通用设计也有事项待后续全会指导。RAN2 已就 MAC CE 与系统信息安全形成面向 SA3 的分析和问题清单，但具体保护机制、适用范围、开销及时延影响仍待评估。

**未决问题**

- 是否及何时由 RAN2 研究 tokenized AI traffic，及其与 SA4 研究的衔接方式尚未确定。
- RAN、RAN1、RANP 对 device types、服务需求及具体要求的后续指导尚待明确；部分议题是否必须等待 device types 仍有不同意见。
- RAN 与 CN 等计算资源部署选项，以及数字孪生和垂直服务的支持要求仍需研究。
- MAC CE 与 system information 的安全保护机制、保护范围及适用的安全参数仍需 SA3 指导和跨组评估。
- MAC CE 安全处理的复杂度、开销和时延，以及 SIB 保护的开销、覆盖范围、认证信息大小与更新频率仍未确定。
- 潜在攻击后的恢复机制及部分 MAC CE 的时效性和安全需求仍需进一步分析。

## 6GR 演进

### [6G/Rel-20 RAN2#134] `observation` 9.2.2 Others

256-bit AEAD algorithm 有三种 operating modes：Confidentiality（仅 ciphering）、Integrity 和 Combined。

```text
The 256-bit AEAD algorithm has three operating modes:
-	Confidentiality (i.e. only ciphering),
-	Integrity,
-	Combined.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.2-o001`

### [6G/Rel-20 RAN2#134] `observation` 9.2.2 Others

combined mode AEAD 使用同一把 cryptographic key 进行 integrity protection 和 ciphering，并可将两者合并为一次操作。编码端先执行 ciphering，再执行 integrity protection（Encryption-then-MAC）。

```text
The combined mode AEAD has the following characteristics:
-	A single cryptographic key is used for both integrity protection and ciphering;
-	The encryption and integrity protection can be performed in a single combined operation;
-	First ciphering is applied and then integrity protection is applied (Encryption -then- MAC) at the encoding side.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.2-o002`

### [6G/Rel-20 RAN2#134] `observation` 9.2.2 Others

基于 5G NR 的 RRC configurations，BWP、CORESET 和 SearchSpace 的可能配置规模巨大。原文指出，在不了解专用 RRC configuration 的情况下，对 MAC CE 发起攻击会有较大挑战。

```text
Based on 5G NR’s RRC configurations, the enormous scale of possible configurations of BWP, CORESET and SearchSpace makes it substantially challenging to perform attacks to MAC CE without prior knowledge of the dedicated RRC configuration.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.2-o003`

### [6G/Rel-20 RAN2#134] `observation` 9.2.2 Others

RAN2 视角提供的技术事实和分析可支持 SA3 分析 MAC CEs 的 threat risks。原文提出仅保护 essential MAC CEs，以降低相应 processing overhead。

```text
The technical facts and analysis provided from RAN2 perspective are highly valuable for supporting SA3 to analyze the threat risks of MAC CEs, protecting only the essential MAC CEs to lower corresponding processing overhead.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.2-o004`

### [6G/Rel-20 RAN2#134] `observation` 9.2.2 Others

All MAC CEs 的 threat range 被分类为适用于“group of UEs”。原文指出，SA3 如何作出该分类尚不清楚。

```text
The threat range for All MAC CEs is classified as being applicable to “group of UEs” and it is unclear how such classification is done by SA3
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.2-o005`

### [6G/Rel-20 RAN2#134] `observation` 9.2.2 Others

所有 uplink MAC CEs 本质上都来自 single UE，因为每个 UE 都发送自己的 UL-SCH MAC PDU。

```text
All uplink MAC CEs are inherently from a single-UE since each UE transmits its own UL-SCH MAC PDU.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.2-o006`

### [6G/Rel-20 RAN2#134] `observation` 9.2.2 Others

DL MAC CEs 包含在发往 C-RNTI 或 T-CRNTI 的 DL transmission 中，且这些 transmission 面向 single UE。MSG2/MSGB 虽面向 group of UEs，但不包含 MAC CEs。

```text
In DL, MAC CEs are included either in a DL transmission addressed to a C-RNTI or a T-CRNTI and these are addressed to a single UE and although MSG2/MSGB are addressed to a group of UEs, these messages do not include any MAC CEs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.2-o007`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.2 Others

RAN2 表示，只要 COUNT 和 MAC-I 保持 5G 的长度，AEAD 对 PDCP PDU format 就没有影响；其理解是 SDU 为 plaintext、整个 PDCP header 为 associated data，ciphering 作用于不含 MAC-I 的 data 部分，而 integrity protection 覆盖 PDCP header 和 data 部分。RAN2 向 SA3 提出有关 AEAD 模式、算法共存、输入配置、MAC-I 长度及处理顺序等澄清问题。

```text
RAN2 provides the following replies to SA3：
-	The impact of AEAD on the PDCP PDU format depends on the inputs/outputs, e.g. COUNT and MAC-I. Based on RAN2’s understanding, there is no impact on the PDCP PDU format, provided that COUNT and MAC-I retain their legacy 5G lengths.
-	RAN2 understanding of the AEAD combined mode is the following:
o	Plaintext corresponds to SDU (data), while the associated data corresponds to the whole PDCP header.
o	Ciphering and deciphering apply only to the data part (excluding MAC-I) of the PDCP PDU, while integrity protection and verification apply to the PDCP header and data part of the PDCP PDU.
-	RAN2 asks SA3 the following questions for clarification:
o	Q1a: Can the combined mode of AEAD be used in a “cipher only” or “integrity only” manner?
o	Q1b: Would using AEAD in combined mode, e.g., just for “cipher only” or “integrity only” introduce any adverse effects to either transmitting or receiving side?
o	Q1c: Are all three operating modes (i.e. Confidentiality, Integrity and Combined) supported in 6G?
o	Q2a: Is AEAD expected to be the sole supported security algorithm in 6G?
o	Q2b: If the answer to Q2a is No, can AEAD co-exist with legacy (i.e., 5G-native) algorithms in 6G?
o	Q3a: Can a single common AEAD algorithm be configured for all RRC signalling (SRBs) and user data (DRBs) at the UE?
o	Q3b: In the above case, can the combined mode of AEAD be used in “cipher/integrity” manner for SRBs while, e.g., in “cipher only” manner for a DRB?
o	Q4: From security perspective, can the length of MAC-I (i.e. MAC_BYTES) remain in 4 bytes as in 5G or allow different lengths?
o	Q5: For the combined mode, does the ciphering and integrity protection at the encoder/decoder follow a normative processing sequencing (e.g. ciphering before integrity protection at the encoding side) or an implementation-specific sequencing?
Noted
R2-2603879	MAC CE security and AEAD analysis from RAN2	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.2-p001`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.2 Others

RAN2 反馈称，combined mode AEAD 采用单次调用和 Encryption-then-MAC 顺序，相较 5G 的 MAC-then-Encrypt 可在解密前进行完整性验证；并提出复用 5G-legacy 输入参数、将 PDCP Header 映射为 AAD、将 PDCP SDU 映射为 IBS/Plaintext。RAN2 倾向于将 6G AS-layer 的 MAC_BYTES 固定为 4 bytes，并就 Cipher-only/Integrity-only 配置和 48-bit EXTRA_IV 同步方式向 SA3 提问。

```text
Based on the technical evaluation of TR 33.771, RAN2 can provide the following feedback and clarification requests to SA3 for AEAD:
PDCP Security Procedure: RAN2 confirms that the AEAD combined mode, which utilizes a single invocation and an "Encryption-then-MAC" (EtM) order, provides a significant optimization over the legacy 5G "MAC-then-Encrypt" (MtE) flow. This enables early integrity verification at the receiver before decryption, reducing unnecessary processing.
Algorithm Inputs: RAN2 understand the 5G-legacy parameters (32-bit COUNT, 5-bit BEARER, 1-bit DIRECTION) can be reusing for AEAD inputs. For data mapping, RAN2 identifies that mapping the PDCP Header to Additional Authenticated Data (AAD) and the PDCP SDU to the Input Bit Stream (IBS/Plaintext) is the efficient protocol approach.
PDU Format: To maintain structural alignment with the legacy PDCP PDU format and minimize overhead, RAN2 prefers that the MAC length (MAC_BYTES) for 6G AS-layer operations remains fixed at 4 bytes (32 bits). Any adoption of variable MAC lengths will necessitate complex RRC signaling modifications and PDU format change.
Questions for SA3:
	Question A (Fallback Support): Does the AEAD combined mode support per-bearer "Cipher-only" or "Integrity-only" configurations under a single NCA algorithm identifier, managed purely via input parameter manipulation (e.g., setting MAC_BYTES=0)?
Question B (EXTRA_IV Sync): Will the new 48-bit EXTRA_IV parameter require explicit synchronization via RRC signaling (e.g., in the SecurityModeCommand), or will SA3 define an implicit derivation scheme (e.g., via KDF) to avoid additional air-interface overhead?
Discussion
-	Docomo thinks that the only question that matters for RAN2 is Q4 and it is not urgent
-	Xiaomi thinks that some RRC procedures, like re-establishment, are only integrity protected and that is a problem.
-	Lenovo thinks that AEAD is not a new algorithm in itself so we will continue supporting what we supported in 5G.   Is the AEAD only applicable for PDCP or also for MAC.
-	ZTE doesn’t see any impact of AEAD, what’s important is that the length is fixed there is no RAN2 impact.   Should support integrity only mode.    What is the associated data, just PDCP or SDAP header as well.
-	Huawei thinks that the most important part is the assumption that we make, that we try to reuse the 5G parameters.
-	LG thinks that we need to understand the co-existance of 5G and 6G and we don’t know if we can support integrity only, in 5G we can turn on and off and if they are combined we need to understand how it is handle without ciphering.   Also if they increase to 8 bytes it has impact to the format.  CMCC agrees that if it is not like legacy
-	Vivo thinks that we only have two question what is input and what is output, and Q4 in Oppo’s proposal is good.
-	Samsung explains that they are considering the different modes from the TR.
-	ZTE doesn’t think that having a different MAC-I length is a big problem as anyways even if you have to fallback to 5G MAC-I length, you anyways re-establish the PDCP.
Questions to SA3
Algorithm Inputs: RAN2 understand the 5G-legacy parameters (32-bit COUNT, 5-bit BEARER, 1-bit DIRECTION) can be reusing for AEAD inputs.
Indicate that there are RRC messages that are only integrity protected.  Ask if this will be possible AEAD
Is AEAD expected to be the sole supported security algorithm in 6G?
From security perspective, can the length of MAC-I (i.e. MAC_BYTES) remain in 4 bytes as in 5G or a different length.    From RAN2 perspective, it is important that the MAC-I length is not variable.
[AT134][12][6G security] LS to SA3 (Oppo)
Intended outcome: Respond to LS to SA3
Deadline:  Friday
R2-2604391	[DRAFT] Reply LS on the AEAD algorithm for PDCP security	OPPO	LS out	Rel-20	FS_6G_Radio, FS_AEAD	To:SA3
Delete option 1
The LS is approved in R2-2604401 with the change above
Handling of SA3's Threat and Risk Analysis on MAC CEs
R2-2603655	RAN2 aspects for MAC CE security analysis	Huawei, HiSilicon, CMCC, Vodafone, China Telecom, China Unicom, Turkcell, Xiaomi	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.2-p002`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.2 Others

RAN2 向 SA3 说明 MAC CE 安全分析应考虑网络处理复杂度、MSG3 的开销限制，以及篡改、重放和利用标识符的威胁复杂度与恢复方式。原文举例指出，MSG3/MSGA 中不匹配预分配 C-RNTI 的内容会被基站忽略，且 C-RNTI 是可经 RRC reconfiguration 更新的临时标识。

```text
Sent an LS to SA3 with the following aspects for MAC CE security analysis:
1) Processing complexity: From network side, a lot of MAC CEs for different UEs may need to be processed at the same time when the cell load is high or when the cell is for some special scenarios like HST (High Speed Train). To prevent adding unnecessary complexity regarding security processing to the network, a basic principle should be that information with low security risk does not require protection.
2) Overhead: To ensure UL coverage during RACH, there is a strict size constraint for MSG3. Currently in NR, C-RNTI MAC CE, BSR MAC CE and PHR MAC CE may need to be included in MSG3. Therefore, there may be no room to add more overhead for security. Besides, the C-RNTI MAC CE can only be transmitted in MSG3/MSGA. Adding security overhead may make it impossible to transmit C-RNTI MAC CE.
3) Threat complexity and recovery means for tampering with or replaying certain MAC CEs:
C-RNTI MAC CE: The contents of some uplink MAC CEs must match with the context in the base station; e.g., the C-RNTI in MSG3/MSGA must match with the pre-allocated C-RNTI by the base station. In this case, if the attacking C-RNTI carried in MSG3/MSGA doesn’t match with any pre-allocated C-RNTI, it will be ignored by the base station.
Uplink MAC CEs: For any uplink transmission, including that from an attacker, the corresponding uplink resources must be scheduled by the base station (otherwise the base station will not receive it). On the scheduled uplink resources, apart from fake MAC CEs (e.g., BSR/PHR), the attacker may not be able to transmit any other data or RRC signalling sub-PDUs in the MAC PDU, as these sub-PDUs needs to be protected in PDCP layer. The attacker can only insert padding to fill in the uplink resources, which the base station may easily identify as abnormal behaviour and perform further actions (e.g., RRC reconfiguration) to prevent further attack.
4) Threat complexity and recovery means for exploitation of identifiers in MAC CEs:
UE identifier in MAC CE refers to C-RNTI. However, the C-RNTI is a temporary identity on the Uu interface and is not permanent for any specific UE. Besides, in Uu interface, there is no explicit association between C-RNTI and any permanent UE ID. Furthermore, the C-RNTI for a UE can be updated via an RRC reconfiguration procedure. Therefore, it is difficult to target the attack to a specific UE with C-RNTI.
R2-2603048	Consideration on 6G security	ZTE Corporation, Sanechips	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.2-p003`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.2 Others

RAN2 提议告知 SA3，UL 或 DL 中都不存在面向或来自 group of UEs 的 MAC CEs，并请 SA3 在适当时据此修订 threat range classification。原文说明该确认针对 5G。

```text
Convey to SA3 that there are no MAC CEs that are addressed to/coming from a group of UEs either in UL or in DL and ask SA3 to revise the threat range classification if appropriate based on this information.
For 5G, RAN2 confirms that there are no MAC CEs that are addressed to/coming from a group of UEs either in UL or in DL and ask SA3 to revise the threat range classification if appropriate based on this information.
Noted
Scope and Configuration of MAC CE security
R2-2602945	Discussion on RAN2 security aspects	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.2-p004`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.2 Others

RAN2 旨在仅支持 RRC_CONNECTED 状态下使用的 MAC CE 安全保护。初始接入及其他连接失败（如 RLF 和 HO failure）过程中的 MAC CE 不在范围内。

```text
RAN2 aims to support MAC CE security protection only for those used in the RRC_CONNECTED state i.e., MAC CEs used during initial access and other connection failure (e.g., RLF and HO failure) procedures are excluded from the scope.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.2-p005`

### [6G/Rel-20 RAN2#134] `proposal` 9.2.2 Others

从 RAN2 signaling 角度，支持可配置的 MAC CE security 是可行的，以确保部署灵活性。最终安全方案仍取决于 SA3 的决定。

```text
From RAN2 singnaling perspective, it is feasible to support configurable MAC CE security to ensure deployment flexibility. The final security solution remains subject to SA3's decision.
R2-2602975	RAN2 impact analysis on AEAD based security	Xiaomi	discussion	Rel-20	FS_6G_Radio
R2-2603024	6G positioning Requirements and Potential RAN2 study areas	T-Mobile USA Inc., Ericsson	discussion	Rel-20	38.914	FS_6G_Radio
R2-2603081	6G Positioning Requirements and RAN2 Study Area	T-Mobile USA Inc.	discussion	Withdrawn
R2-2603207	Discussion on 6G security	CATT	discussion	Rel-20	FS_6G_Radio
R2-2603297	Discussion on L2 security	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2603346	Considerations on 6G AS security aspects	NTT DOCOMO	discussion	Rel-20	FS_6G_Radio
R2-2604047	Discussion on MAC CE Security	China Telecom	discussion
R2-2604060	Review of the risk analysis of MAC CEs	Samsung	discussion 	Rel-20	FS_6G_Radio
R2-2604165	MAC CE security analysis and procedural considerations	Nokia	discussion	FS_6G_Radio
R2-2604172	Reliability, Resilience and Security for 6G Control Information 	Ericsson, Turkcell	discussion	Rel-20	FS_6G_Radio
R2-2604398	RAN2 aspects for MAC CE security analysis	Huawei, HiSilicon	discussion		Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_134/) · `RAN2-134-9.2.2-p006`

### [6G/Rel-20 RAN2#133bis] `agreement` 9.2.3 Others

RAN2 将继续审查 TR 33.801-01 Annex-B 中的 security analysis，识别 RAN2 相关方面并在有结果时向 SA3 提供反馈；RAN2 不预计评估 SA3 的全部方案，SA3 可按需提出问题。潜在攻击恢复机制仍需 RAN2 进一步研究；记录还指出，MAC CEs 仅在符合 UE 配置的资源上发送时才会处理，其中部分配置由受安全保护的 dedicated RRC signalling 配置。

```text
Continue the review of the security analysis captured in Annex-B of TR 33.801-01 with a view to provide further input on RAN2 related aspects to SA3 in future.
R2-2601781	Draft-Reply LS on MAC CE security	ZTE Corporation(rapporteur)	LS out	Rel-20	FS_6G_SEC	To:SA3
Add the following to last question RAN2 agreed that we will continue the review of the security analysis captured in Annex-B of TR 33.801-01 with a view to provide further input and/or follow-up questions on RAN2 related aspects to SA3 in future.
Update whether there are means for potential recovery from the attacks captured in the TR  needs further RAN2 study.
It should be noted that MAC CEs will be processed only if they are sent using resources that match UE’s configuration (e.g. the correct searchspace, CORESET and BWP), some of which is configured using dedicated RRC signalling which is security protected.
The LS is approved with the changes above in R2-2602620
Joint RAN2-SA3 session on security
R2-2602629	MAC CE Security: SA WG3 Status	Orange, Nokia	discussion	Rel-20	FS_6G_SEC
Noted
-	ZTE asks if for the below the assumption is after AS security is established “ On #3, a comment has been made that SA3 should focus on MAC CE protection after the Security Mode Command”.   Orange confirms
-	Orange explains that there are discussions on securing a set of MAC CEs without having to understand what MAC CEs are included.
On discussion on joint solution evaluation RAN2 and SA3
-	Orange and Nokia think that it is important for RAN2 to review the risk assessment and provide any feedback (Annex B2).
-	ZTE thinks that RAN2 will provide feedback only on RAN2 specific aspects and SA3 can take those into account in their evaluation
-	Orange would like to be careful and not send everything to RAN2.
-	Apple thinks that it should be SA3 that tells us which information is important to protect and level/type of security.
-	Lenovo asks if there is a solution that protects all the MAC CEs.
On the hardware change
-	Huawei thinks that this is important because the NW has to process a lot of MAC CEs in a cell, so it is important to only protect the MAC CEs that really need to be protected.   If that is the case there wouldn’t be a problem.
-	ZTE highlights that we had this discussion in RAN2 and it was very difficult to converge.  This discussion is only for MAC CE and there is a general discussion in RAN Plenary for general hardware.  ZTE thinks that MAC CE protection will not lead to hardware change as this is not going to be sent too frequently.
-	ZTE asks if the mechanism can be disabled like the DRB concept.    Orange thinks that it depends on solution but good to know that would be desirable.
-	Ericsson also thinks that it depends on the processing timeline there may be.
-	Nokia also thinks that if the MAC CEs are infrequent we can avoid the hardware changes.
-	Xiaomi thinks that it would be good for the UE to not be required to use separate hardware
-	LG would like avoid SN requirement as currently MAC protocol doesn’t have Sequence numbers.  It would be important to not change the requirement on our protocols.
-	Tmobile thinks hardware discussion is not relevant, it is implementation dependent.
-	Orange and Verizon think it is important to understand the complexity and see if there are new requirements.
If the MAC CEs are infrequent and no strict processing requirements, this can remove some of the concerns on hardware impacts on the NW side in light of the solutions.
Recommendation:
RAN2 is not expected to evaluate all SA3 solution.   SA3 can send questions when needed
As agreed RAN2 will continue to review the risk assessment to identify RAN2 specific aspects and provide feedback to SA3 when available.  SA3 would appreciate it if it is done as soon as possible.
R2-2602620	Reply LS on MAC CE security	RAN2	LS out	Rel-20	FS_6G_SEC	To:SA3
Question 1: Nokia asks if we can’t change the mgs3 size.  Vodafone thinks it is a basic requirement and don’t want to change that.    ZTE explains that we can’t change as it has impact on coverage and explains that for initial message msg3 only includes CCCH message so it is not a MAC CE.
Question 4: Tmobile ask if there are size limitations for the group.   ZTE explains that it is dependent on grant the gNB provides to the UE.
Question 6: SA3 would appreciate inputs on recovery mechanism as soon as possible
Approved
R2-2602627	Reply LS on AS security aspects (S3-261696; contact: ZTE)	SA3	LS in	Rel-20	FS_6G_Radio	To:RAN2
-	ZTE would like to know when this would be decided as it has a lot of RAN2 impacts.
Noted
R2-2602628	SA#2 – KI#2.1 – MAC CE Security	Rapporteur (ORANGE), IIT Bombay, InterDigital, Nokia, Qualcomm Incorporated, Apple, NTT Docomo, Deutsche Telekom, OPPO, Samsung, vivo, Lenovo, Ericsson, ZTE, Rakuten, AT&T	discussion	Rel-20	FS_6G_SEC
Ericsson explains that we are discussing the information that will be sent, but how it is sent it is still for further discussion.
Huawei asks if the requirements are for all MAC CEs or only the MAC CEs that are at risk.   Orange indicates that we will have this discussion later.
LG asks what identifier are we referring to and what is non-cryptographic based solutions
R2-2602803	Meeting minutes for the joint RAN2-SA3 session on security	Chairlady	Report	Rel-20	FS_6G_SEC
Noted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.2.3-a001`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.2.3 Others

RAN2 将继续审查 TR 33.801-01 Annex-B 中记录的 security analysis，以便未来向 SA3 提供 RAN2 相关方面的进一步输入。

```text
Continue the review of the security analysis captured in Annex-B of TR 33.801-01 with a view to provide further input on RAN2 related aspects to SA3 in future.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.2.3-p001`

### [6G/Rel-20 RAN2#133bis] `proposal` 9.2.3 Others

同意将“Noted”作为对 SA3 LS（S3-260801 / R2-2601404）的回复文本。

```text
Agree the following text as reply to the SA3 LS in S3-260801 / R2-2601404
Noted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133bis/) · `RAN2-133bis-9.2.3-p002`

### [6G/Rel-20 RAN2#133] `observation` 10.2.3 Others

应用 MAC security 可能使 MAC PDU 增加约 1–5 octets；是否还需 encryption 带来的额外开销，应向 SA3 询问。

```text
Applying MAC security will likely add ~1-5 octets to the MAC PDU size, but whether any additional overhead from encryption is needed should be asked from SA3.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.3-o001`

### [6G/Rel-20 RAN2#133] `observation` 10.2.3 Others

RAN2 应告知 SA3 哪些 MAC CEs 对系统运行更为“fundamental”，例如与 connection setup and maintenance 相关的 MAC CEs。

```text
RAN2 should inform SA3 which MAC CEs are the most ”fundamental” to the system operation than others (e.g. MAC CEs related to connection setup and maintenance).
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.3-o002`

### [6G/Rel-20 RAN2#133] `observation` 10.2.3 Others

评估 MAC security 的影响时，需要考虑 MAC CE security 带来的 latency。

```text
The latency from MAC CE security needs to be accounted for when considering impact of MAC security.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.3-o003`

### [6G/Rel-20 RAN2#133] `observation` 10.2.3 Others

已规范的 real-time MAC CEs 很少，目前仅识别出 BSR、DSR 和 PHR。

```text
There are very few real-time MAC CEs specified: Only BSR/DSR/PHR are identified.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.3-o004`

### [6G/Rel-20 RAN2#133] `observation` 10.2.3 Others

实现 MAC security 有多种方式，且技术上均可行；应选择哪种选项组合取决于 RAN2 和 SA3 的分析。

```text
While there are several ways to realize MAC security, all of them are technically feasible and which combination of options to choose depends on analysis by both RAN2 and SA3
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.3-o005`

### [6G/Rel-20 RAN2#133] `observation` 10.2.3 Others

可识别一组 latency-critical MAC CEs，并应优先进行 security evaluation，以便在规范阶段推进时向 SA3 更新 5G 与 6G MAC CEs 的差异。

```text
A set of latency-critical MAC CEs can be identified and should be prioritised for security evaluation, with the intention to update SA3 on the differences between 5G and 6G MAC CEs as they develop in the normative phase.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.3-o006`

### [6G/Rel-20 RAN2#133] `observation` 10.2.3 Others

列出的 latency-sensitive MAC CEs 是可能制定安全要求的重点对象，包括 BSR、PHR、Timing Advance、Configured Grant Confirmation、LTM 命令、PUCCH Spatial Relation 和 UE-specific PDCCH/PDSCH 的 TCI 状态指示或激活/去激活。

```text
The following MAC CEs are of particular interest for possible security requirements due to their latency sensitivity:
•	BSR
•	PHR (multiple variations for single/multiple entry, multiple TRPs, etc.)
•	Timing Advance and Absolute Timing Advance (deadline based on the HARQ turnaround time)
•	Configured Grant Confirmation and Multiple Entry Configured Grant Confirmation
•	LTM Cell Switch Command and Enhanced LTM Cell Switch Command
•	LTM Candidate Timing Advance Command
•	PUCCH Spatial Relation Activation/Deactivation
•	TCI State Indication for UE-specific PDCCH
•	TCI States Activation/Deactivation for UE-specific PDSCH
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.3-o007`

### [6G/Rel-20 RAN2#133] `observation` 10.2.3 Others

部分 MAC CE（如 BSR、PHR、TA）需要在 security establishment 之前发送。

```text
Certain MAC CEs (e.g., BSR, PHR, TA) need to be sent before security establishment.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.3-o008`

### [6G/Rel-20 RAN2#133] `observation` 10.2.3 Others

RAN2 和实现团队需要了解 6G 中 MAC CE security protection 的预期复杂度，并确认 RRC connection 期间依赖 symmetric security algorithms 是否足够。

```text
RAN2 and implementation teams need to understand the anticipated complexity of MAC CE security protection in 6G, and in particular to know whether it is sufficient during an RRC connection to rely on symmetric security algorithms.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.3-o009`

### [6G/Rel-20 RAN2#133] `observation` 10.2.3 Others

在 TB construction 后期才可能确定是否将 MAC CE 纳入 transport block，这可能影响某些设计中的 security processing 时序。

```text
Inclusion of a MAC CE in a transport block may be determined late in the TB construction, which may affect the timing of security processing in some designs.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.3-o010`

### [6G/Rel-20 RAN2#133] `observation` 10.2.3 Others

小型 MAC CE 和尺寸受限场景引发了 security overhead 方面的顾虑（若相关 MAC CE 适用），该问题应提交 SA3 关注。讨论还提出梳理 MAC CE 是否 time critical、是否需在 security 前发送，并权衡其时限预算。

```text
Small MAC CEs and size-constrained cases raise a concern about security overhead (if applicable to the concerned MAC CEs), which should be brought to SA3’s attention.
[2 min]
Noted
Discussion
-	ZTE thinks that for DL there is no time-critical requirement MAC CE
-	CATT Thinks that we can send a table where we indicated whether it is time critical and sent before security.
-	LG asks what is a purpose of time criticality of certain MAC CEs.   Ericsson thinks that they need to take this into account and we need to do a tradeoff.
-	Xiaomi thinks that we would need to define budget for the time criticality.
R2-2600073	Security Considerations to SA3	vivo, NTT DOCOMO INC., SHARP Corporation	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.3-o011`

### [6G/Rel-20 RAN2#133] `observation` 10.2.3 Others

UL 发送侧的 MAC CE security operations（encryption 和/或 integrity protection）引入的处理时延应尽量降低，以避免相较现有 Uu timeline 造成性能影响。

```text
On the transmission side (UL), the processing latency introduced by MAC CE security operations (i.e., encryption and/or integrity protection) shall be minimized to avoid performance impact compared to the existing Uu timeline.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.3-o012`

### [6G/Rel-20 RAN2#133] `observation` 10.2.3 Others

DL 接收侧的 MAC CE security operations（integrity verification 和/或 decryption）引入的处理时延应尽量降低，以避免相较现有 Uu timeline 造成性能影响。

```text
On the receiving side (DL), the processing latency introduced by MAC CE security operations  (i.e., integrity verification and/or decryption) shall be minimized to avoid performance impact compared to the existing Uu timeline.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.3-o013`

### [6G/Rel-20 RAN2#133] `observation` 10.2.3 Others

RAN2 对 SIB security 的讨论聚焦于 SIB 的潜在开销；为 MIB 增加开销可能不可行，为其他 SIB 增加开销则需要仔细分析。

```text
SIB security discussion in RAN2 focuses on potential overhead for SIBs Adding overhead to MIB could be impossible and adding overhead to other SIBs requires careful analysis.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.3-o014`

### [6G/Rel-20 RAN2#133] `observation` 10.2.3 Others

从 RAN2 角度看，聚焦于对系统接入所需 system information 的 integrity protection 是合理的，目标是检测 false base station。

```text
From RAN2 perspective, it looks reasonable to focus on integrity protection of system information that is required for access to the system, targetting false base station detection.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.3-o015`

### [6G/Rel-20 RAN2#133] `observation` 10.2.3 Others

受 message space constraints 限制，部分基础 system information 在接收时可能不适合保护。RAN2 可询问 SA3，是否接受在后续 SIB 接收 signature 并事后校验等方法。

```text
Some fundamental system information may be impractical to protect at the time of reception due to message space constraints, but RAN2 can inquire if other methods such as receiving a signature in a later SIB and checking it after the fact would be acceptable for SA3.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.3-o016`

### [6G/Rel-20 RAN2#133] `observation` 10.2.3 Others

从 RAN2 角度看，可允许 UE 建立 temporary 或 provisional connection，以验证最初接收的 system information；但 RAN2 无法评估该方案从 SA3 角度是否有效。

```text
From RAN2 perspective, it may be feasible to allow a temporary or provisional connection for the UE to validate the initially received system information, but RAN2 cannot evaluate if such a solution is valid from SA3 perspective.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.3-o017`

### [6G/Rel-20 RAN2#133] `observation` 10.2.3 Others

从 RAN2 角度，dedicated delivery of SIBs 应由 connected mode security 覆盖，因此此情境无需特定的 SI protection scheme。

```text
From RAN2 perspective, dedicated delivery of SIBs should be covered by connected mode security, making any specific SI protection scheme unnecessary in this context.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.3-o018`

### [6G/Rel-20 RAN2#133] `observation` 10.2.3 Others

在 5G NR 中，system information broadcast 容易受到 False Base Stations 带来的潜在威胁。

```text
In 5G NR, system information broadcast is prone to potential threats from False Base Stations.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.3-o019`

### [6G/Rel-20 RAN2#133] `observation` 10.2.3 Others

有人希望离线询问 processing complexity、associated latency 等问题，因为这些可能影响 implementations；但目前不清楚具体应询问什么，且其中一些问题似乎也需要 RAN2 自行考虑。

```text
There is some interest offline to ask some question regarding processing complexity/associated latency etc as this may have impact on implementations, but it is unclear what exactly to ask and seems some of these questions are also for ourselves
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.3-o020`

### [6G/Rel-20 RAN2#133] `proposal` 10.2.3 Others

RAN2 将向 SA3 询问 encryption algorithms 的 input 和 output sizes 是否相同。

```text
RAN2 to ask from SA3 whether the input and output sizes will be the same for the encryption algorithms.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.3-p001`

### [6G/Rel-20 RAN2#133] `proposal` 10.2.3 Others

RAN2 将汇总与 connection setup（包括 random access）和 connection maintenance（例如 timing advance、beam management、scheduler inputs）相关的 MAC CEs，并将信息提供给 SA3。

```text
RAN2 to compile list of MAC CEs that are related to connection setup (including random access) and connection maintenance (e.g. timing advance, beam management, scheduler inputs) and provide the information to SA3.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.3-p002`

### [6G/Rel-20 RAN2#133] `proposal` 10.2.3 Others

RAN2 将告知 SA3，目前只有少数 5G MAC CEs（BSR/DSR/PHR）具有 real-time processing requirements。该事项已记录。

```text
RAN2 to indicate to SA3 that only few 5G MAC CEs (BSR/DSR/PHR) currently have real-time processing requirements.
Noted
R2-2600496	Coordination with SA3 on MAC CE and system information security	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.3-p003`

### [6G/Rel-20 RAN2#133] `proposal` 10.2.3 Others

需研究必要的 security parameters（例如 SN 和 MAC-I fields），以在 6G air interface 上平衡 robust protection 与 signaling efficiency。

```text
Investigate the necessary security parameters (e.g., SN and MAC-I fields) to achieve a balance between robust protection and signaling efficiency over the 6G air interface.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.3-p004`

### [6G/Rel-20 RAN2#133] `proposal` 10.2.3 Others

6G system 中的 MAC CE security protection mechanism 应设计得足够通用，以便在需要时支持后续 releases 引入的新 MAC CE(s)。

```text
The MAC CE security protection mechanism in the 6G system should be designed to be generic enough to accommodate new MAC CE(s) introduced in later releases if needed.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.3-p005`

### [6G/Rel-20 RAN2#133] `proposal` 10.2.3 Others

RAN2 将向 SA3 咨询 MAC CE security operations 的 processing latency 量级。该事项标记为 Not treated。

```text
RAN2 to consult SA3 on the order of magnitude of processing latency for MAC CE security operations.
[2 min]
Not treated
Coordination with SA3 wrt. SI security
R2-2601054	RAN2 inputs on AS security to SA3	Nokia	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.3-p006`

### [6G/Rel-20 RAN2#133] `proposal` 10.2.3 Others

RAN2 将告知 SA3，SIB overhead 可能是主要顾虑，向 MIB 增加开销可能不可行，而保护其他 SIBs 的开销需要分析；并请求 SA3 就可接受的 overhead 和考虑中的 protection mechanisms 提供指导，以便 RAN2 从 radio perspective 评估。

```text
Indicate to SA3 that SIB overhead could be a major concern for RAN2, and adding overhead to MIB could be impossible and adding overhead to protecting other SIBs would require analysis. Request SA3 guidance on what kind of overhead could be possible and what kinds of protection mechanisms are considered so RAN2 can assess them from radio perspective.
[2min]
R2-2600496	Coordination with SA3 on MAC CE and system information security	MediaTek Inc.	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.3-p007`

### [6G/Rel-20 RAN2#133] `proposal` 10.2.3 Others

拟向 SA3 发送 LS，协调 MAC CE 和 system information 安全问题相关观察的信息。

```text
Develop an LS to SA3 to coordinate information with them related to the group’s observations on MAC CE and system information security issues.
[3 min]
R2-2600695	Considerations for Access Stratum Security 	Samsung	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.3-p008`

### [6G/Rel-20 RAN2#133] `proposal` 10.2.3 Others

RAN2 将在联合会议向 SA3 询问 system information 保护所需 security information（digital signature）的预期大小、SIB 覆盖范围及其提供粒度。还将询问传输频率以及更新或刷新的时机和频率。

```text
RAN2 to request the following information from SA3in the joint session:
a.	What is the expected size of security information (digital signature) for the protection of system information?
b.	Is the SIB protection considered for all the SIBs or a subset of SIBs?
c.	Is the security information, provided per individual SIBs or common for all SIBs or a subset of SIBs?
d.	What is the expected frequency of the transmission of security information?
e.	When or how often does the security information need to be updated or refreshed?
[2 min]
R2-2600163	Radio considerations for 6G security	ZTE Corporation, Sanechips	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.3-p009`

### [6G/Rel-20 RAN2#133] `proposal` 10.2.3 Others

为协助 6G lower layer signalling 和 system information 设计，提出向 SA3 澄清哪些 system information 需要认证、authentication token 的可能大小，以及认证按单个 SIB 还是一组 SIB 进行。讨论还提出确认安全是否适用于 SIB 和 paging、预期开销，并在线下决定是否向 SA3 发送问题。

```text
In order to help RAN2 with the design of lower layer signalling and system information for 6G, the following questions should be clarified with SA3:
Questions for System information security:
Q8: Which parts of system information should be subject to authentication?
Q9: For security of system information what is the likely size of the authentication token (e.g. Digital signature/MAC-I)?
Q10: Will the authentication of the system information be per SIB or per a set of SIBs?
-	LG thinks whether it security will be applied to SIB and paging and what is the expected overhead.
[2 min]
[AT133][008][6G] Security (ZTE)
Intended outcome:
Discuss the CBs remaining from MAC CE and if they are any other questions.
Check if there are easy/generic questions for SIB security and determine after offline if we send the questions to SA3.
Draft LS will be post meeting
Deadline:  Thursday
R2-2601331	Offline discussion summary: [AT133][008][6G] Security (ZTE)	Offline Rapporteur (ZTE)	discussion	Rel-20	FS_6G_Radio
-	CMCC thinks that we should have operator control to disable it.
-	Verizon would like to understand what type of complexity to expect and whether we would need additional hardware.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.3-p010`

### [6G/Rel-20 RAN2#133] `proposal` 10.2.3 Others

商定向 SA3 的 LS 至少询问 PQC 是否适用于 UE air interface，并说明 MAC 没有 Sequence Number 和 in-sequence delivery、MAC CEs 可与其他 MAC CEs 或 MAC SDUs 组合，以及部分 MAC CEs 需在 security establishment 前发送；BSR/DSR/PHR 被认定为 time critical。RAN2 将继续研究其他 MAC CEs 的时效性，并与 SA3 合作评估安全算法对处理、复杂度和时延的影响；LS 获批为 R2-2601383。

```text
Continue to study the magnitude of processing complexity/associated latency etc that may impact implementations to identify any RAN2 input for the joint session.
-	Huawei understands that SA3 will provide us the possible algorithms and it is RAN2’s responsibility to analyse based on these algorithms, the processing, latency, complexity etc.
-	Oppo thinks that SA3 will ask us too so they have done some analysis.
-	Xiaomi thinks that SA3 will ask us what is the budget we have for this processing.
-	Futurewei thinks the complexity is particularly problematic for IoT.  We should state that we just need integrity protection.
-	Verizon, Vodafone, CMCC, TIM, ATT etc would like to state to SA3 that HW complexity is a consideration.   Today we only do security in PDCP and if we have a split there may be a problem to do in MAC as well.   Mediatek explains that we will have an analysis on HW impacts in June.   Huawei thinks that we will have a check point anywyas in June with SA3.
-	Chair confirms that the understanding is that complexity includes HW impact.
-
| Agreements on SA3 LS At least ask is PQC applicable to the UE air interface. Indicate that currently in 5G a. MAC layer has no Sequence Number and no in-sequence delivery. b. MAC CEs can be grouped together with other MAC CEs and/or MAC SDUs RAN2 will discuss based on new requirements coming from SA3 how to design the MAC Indicate to SA3 that certain MAC CEs (e.g., BSR, PHR, TA) need to be sent before security establishment. Agree that BSR/DSR/PHR are “time critical” MAC CEs. In LS explains what were the time criticality considerations for the agreed MAC CEs(e.g. TB construction timeline) Continue to study further the time criticality of all other MAC CEs in UL and DL considering that there are both TX side and RX side processing requirements with the aim to prepare ourselves with an answer if SA3 ask any questions for these. Indicate to SA3 that even if we don’t include some MAC CE as “time critical”, it doesn’t mean there are no other RAN2 concerns/considerations. For instance, overhead and complexity is still a strong consideration and may be an issue for MAC CEs in general. Ask SA3 are you considering security (integrity protection) for system information and if yes what is the associated overhead RAN2 will study the impact of MAC CE SA3 security algorithms (with early guidance to RAN2) on RAN2 areas like processing, complexity, latency etc. in close collaboration with SA3. From RAN2 point of view, it would be desirable that SA3 provides RAN2 with some understanding of the security algorithm complexity for the lower layer security |
| --- |
[POST133][014][6G] Security LS to SA3 (ZTE)
Intended outcome: Agree to LS to SA3 cc RANP
Deadline:  short
=> Approved in R2-2601383
Not treated
R2-2600053	Discussions on 6GR Security	SHARP Corporation	discussion	Rel-20
R2-2600110	General considerations on RAN2 6G design	Xiaomi	discussion	Rel-20	FS_6G_Radio	Withdrawn
R2-2600191	Considerations on 6G AS security	CATT	discussion	Rel-20	FS_6G_Radio
R2-2600205	Coordination on the security aspect between RAN2 and SA3	OPPO, Xidian University	discussion	Rel-20	FS_6G_Radio
R2-2600357	Questions to SA3 for the RAN2-SA3 joint session	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
R2-2600385	UE Autonomous Adaptation on Network Configured Parameters	MediaTek Inc.	discussion
R2-2600453	Views on 6G MAC secuirty	Apple	discussion	Rel-20	FS_6G_Radio
R2-2600606	Discussion on Access Stratum Security	Fujitsu	discussion	Rel-20	FS_6G_Radio
R2-2600771	Discussion on MAC CE protection and AS security requirements for IoT devices	Sony	discussion	Rel-20	FS_6G_Radio
R2-2600795	Considerations for a joint session with SA3	Lenovo	discussion	FS_6G_Radio
R2-2600852	Discussion on L2 security	Ofinno	discussion	Rel-20	FS_6G_Radio
R2-2600936	6G security with PQC	LG Electronics Inc.	discussion	Rel-20	FS_6G_Radio
R2-2600963	Discussion on Joint Session with SA3 of 6GR Security	CMCC	discussion	Rel-20	FS_6G_Radio
R2-2601011	MAC CE security	InterDigital Communications	discussion	Rel-20
R2-2601024	Further discussion on 6G lower layer security	NEC	discussion	Rel-20	FS_6G_Radio
R2-2601069	Initial Considerations for 6GR Access Technology	Hanbat National University	discussion
R2-2601103	Constant Whispers - Emerging GenAI Traffic and Potential RAN Impacts v2	TCL	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_133/) · `RAN2-133-10.2.3-p011`

### [6G/Rel-20 RAN2#132] `agreement` 10.2.3 Design approaches, New services, Others

确定 eMBB（包括 immersive communication）、Voice、ISAC 和 IoT 的需求需从 Day 1 得到满足和支持；Voice fallback 先在 plenary 讨论。假设 emergency calls、与 emergency call 相关的 positioning（如 ECID）及 PWS 的 regulatory requirements 从 Day 1 满足，并将移动 AI 流量特征列入研究，是否研究 tokenized traffic 尚未确定。

```text
1	As per RAN plenary, RAN2 will ensure that eMBB (including immersive communication), Voice, ISAC and IoT requirements are met and supported from Day1.   Voice fallback should first be discussed in plenary.
2	RAN2 assumes that regulatory requirements on emergency calls, positioning associated to emergency call requirement (e.g. ECID) and PWS  should be met from Day1.   RAN2 chair should highlight to plenary in status report that input may be required for the requirements and discuss whether to update SI description.    Wait for RAN input for further positioning requirements.
3	We will study the traffic characteristics of mobile AI traffic for both UL and DL (together with NR Rel-20).  FFS whether tokenized traffic is studied
4	Wait for RANP discussion on whether other services are supported.  The agreements from RANP will be taken as baseline for our RAN2 discussions
Device types
R2-2508617	Discussion on device types and forward compatible design	Huawei, HiSilicon	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-a001`

### [6G/Rel-20 RAN2#132] `observation` 10.2.3 Design approaches, New services, Others

确定 6G radio protocol 应将满足 mobile broadband services 的需求作为高优先级。

```text
6G radio protocol must meet the requirements of mobile broadband services as a high priority.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-o001`

### [6G/Rel-20 RAN2#132] `observation` 10.2.3 Design approaches, New services, Others

确定 Voice service 必须在 6G standalone architecture 中得到支持。IoT、sensing 和 AI applications 等其他服务从 Day 1 获得支持，需有明确的 market needs 和 use cases 作为依据。

```text
Voice service must be supported in 6G standalone architecture. For other services such as IoT, sensing and AI applications, clear market needs and use cases are required to justify their support from Day-1.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-o002`

### [6G/Rel-20 RAN2#132] `observation` 10.2.3 Design approaches, New services, Others

预计 token consumption 将快速增长。

```text
The token consumption is expected to grow rapidly.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-o003`

### [6G/Rel-20 RAN2#132] `observation` 10.2.3 Design approaches, New services, Others

6G study phase 中，RAN1、SA1 和 SA2 正在研究 tokenized AI 的 traffic characteristics，以及各工作组可能受到的 standard impacts。

```text
In the 6G study phase, RAN1, SA1 and SA2 are studying the traffic characteristics of the tokenized AI and the potential standard impacts in each working group.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-o004`

### [6G/Rel-20 RAN2#132] `observation` 10.2.3 Design approaches, New services, Others

Tokenized AI 被认为是 NTN network 的一项有前景的服务，其原因是 transmission bit rate 较低，并且对 voice 和 video 的 packet loss 具有 resilience。

```text
Tokenized AI is a promising service for NTN network due to the reduced transmission bit rate and the resilience to the packet loss for voice and video.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-o005`

### [6G/Rel-20 RAN2#132] `observation` 10.2.3 Design approaches, New services, Others

Tokenized AI 的 traffic pattern 中，一个 source file（如 video frame、picture 或 text）可用于生成多个 tokens。用于 tokenization 的 source files 至少包括 non-real-time 和 real-time audio/video、picture 与 text，token 的 arrival rate/interval 等 traffic pattern 依赖 source file 的 traffic pattern。

```text
The tokenized AI has the following traffic pattern:
o	One source file (e.g. video frame/ picture/ text) can be used to generate a number of tokens.
o	The source files for tokenization include at least non-real-time and real-time audio/video, picture and text.
o	The traffic pattern (e.g. arrival rate/interval) of token has dependency on the traffic pattern of the source file.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-o006`

### [6G/Rel-20 RAN2#132] `observation` 10.2.3 Design approaches, New services, Others

Tokenized AI 的 transmission requirements 包括 error-tolerance，即无需所有 tokens 都正确传输；不同 tokens 具有不同的 transmission reliability requirement，例如 token error rate。

```text
The tokenized AI has the following transmission requirements:
o	Error-tolerance: Not all tokens need to be transmitted correctly.
o	Importance: Different tokens have different transmission reliability requirement (e.g. token error rate)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-o007`

### [6G/Rel-20 RAN2#132] `observation` 10.2.3 Design approaches, New services, Others

提出 6G RAN computing resources deployment 有三种不同选项，并应进一步研究。

```text
There are three different options for computing resources deployment in 6G RAN. These three options should be further studied.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-o008`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.3 Design approaches, New services, Others

6GR 应从 Day-1 优先支持 mobile broadband 和 voice services，同时采用共同设计以支持广泛服务，避免要求单独解决方案。讨论中，Samsung 将“优先”解释为其他服务不影响 eMBB 性能。

```text
The 6GR study should prioritize mobile broadband and voice services from Day-1 while aiming for a common design that supports a wide range of services without requiring separate solutions.
[2 min]
-	Xioami asks what does prioritize mean.  Samsung clarifies that prioritize just means that eMBB performance is not impacted because of other services.
-	Vivo asks about voice fallback.  Xioami thinks that’s related to migration.    Qualcomm thinks that the fallback is part of the mobility and it is more related to handover.
-	Lenovo asks if this applies to NTN.
Noted
Regulatory and FWA
R2-2508237	6G Services	Nokia	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-p001`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.3 Design approaches, New services, Others

6GR 应满足 emergency voice calls、positioning 和 PWS 的所有 regulatory requirements。Nokia 提出至少支持 ECID 和 emergency broadcasts，且要求应来自 A1。

```text
6GR shall be able to fulfil all regulatory requirements on emergency voice calls, positioning and PWS.
-	Apple asks what are those requirements and who determines.   Nokia thinks that at least we should support ECID and emergency broadcasts and it should come from A1.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-p002`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.3 Design approaches, New services, Others

应向 6GR 提供 FWA devices 的特定特征（例如较大的 RF components、external power supply），并在设计中加以考虑，以优化对 FWA services 的支持。

```text
the specific characteristics of FWA devices (e.g. larger RF components, external power supply…) shall be made available to and taken into account by 6GR for an optimised support of FWA services.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-p003`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.3 Design approaches, New services, Others

RAN WGs 应等待 SA4 完成 Media Aspects for 6G Systems 研究后，再启动与 AI traffic 相关的讨论，其中包括但不限于 tokenization。

```text
RAN WGs should wait for SA4 to conclude its study on Media Aspects for 6G Systems before initiating any discussion related to AI traffic (including but not limited to tokenization).
[2 min]
Noted
Tokenized AI
R2-2508841	Guidelines and Views on 6G Design approaches and New services	CMCC	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-p004`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.3 Design approaches, New services, Others

RAN2 应研究对 ISAC、AI/ML-based services、token communication 和 immersive communication 等新服务的支持，并考虑 NW 与 UE energy consumption 以及 User experience (QoS/QoE) improvement。

```text
RAN2 should study the support of new services, e.g., ISAC, AI/ML-based services, token communication and immersive communication, taking NW & UE energy consumption and User experience (QoS/QoE) improvement into consideration.
[2 min]
R2-2508106	Traffic characteristics of tokenized AI	OPPO, CSCN, China Unicom	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-p005`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.3 Design approaches, New services, Others

关于 tokenized AI traffic 的研究存在不同意见：有观点主张等待 SA4 的结论，也有观点主张与非 tokenized AI traffic 一并研究。下次会议将了解是否存在 RAN2 specific requirement 及需向 SA4 提出的具体问题。

```text
RAN2 studies the traffic characteristics of tokenized AI service.
[2 min]
Discussion
-	Nokia, Ericsson, Samsung thinks that we shouldn’t discuss tokens until SA4 tells us otherwise.   The tokens are for application layer and it is not related to reliability of the air interfaces.  Lenovo agrees with Nokia and it is not even clear what the tokens will look like, so we should wait.
-	Xiaomi, Mediatek, Ericsson, thinks that we should just focus on AI traffic and not tokenization.   MEdiatek thinks that this is about future cases that don’t actually exist.  And we have other working groups that look into this and the topic is very immature at this point in time.
-	Vivo thinks that we can study tokenized together with non-tokenized as it is quite similar.  Even without SA4 reply RAN1 started the tokenized traffic study.   Apple agrees that it is just a sub-set of mobile AI and we should start it from SA.
-	Interdigital is not sure what SA4 is going to tell us as token data is opaque and we can’t use that to increase the granularity.   Need to ask the questions what would be the impact, would there be a different reliability requirement?  Can we for example drop some packets?  ZTE agrees and thinks we need to understand if it introduces any new requirement and some of this things are common like error tolerant transmissions and fast switching of QoS.  These are general and we will do them anyways.   What we would need to know if there is anything special.
-	Qualcomm thinks that we should ask SA4 about specific questions and before we go into solutions we should understand the requirements.
-	CMCC thinks that if we wait for SA4 we may have to wait for a long period so we should study both together.
On sending an LS to SA4
-	Offinno thinks we can send an LS to SA4.  Huawei agrees and wants to ask what are the requirement and characteristic.
-	Mediatek explains that SA4 is discussing based on RAN1 LS, so they will look into that themselves.
-	ZTE would like to understand if there are any RAN2 specific requirements
-	Apple thinks that we can ask if we can use the PDU Set.
For next meeting, understand if there is any RAN2 specific requirement and any specific SA4 questions.
Digital twins and computing serivces
R2-2508966	Considerations on 6G Services and Requirements	China Unicom	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-p006`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.3 Design approaches, New services, Others

RAN2 研究 AI 和 sensing services 支持时，应考虑不同的 computing resources deployment options，包括部署在 RAN 和 CN 的情形。

```text
During RAN2 study on support AI and sensing services, it should be considered different computing resources deployment options, both considering located at RAN and CN.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-p007`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.3 Design approaches, New services, Others

RAN2 应进一步研究 Digital twin service，例如其 traffic model 和潜在的 specification impacts。

```text
Digital twin service should be further studied (e.g. traffic model, potential specification impacts) by RAN2.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-p008`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.3 Design approaches, New services, Others

RAN2 需要进一步研究如何支持 6G vertical services，至少涵盖 protocol flexibility、suitability 和 simplification。该条目标记为 Not treated。

```text
RAN2 needs to further study how to support 6G vertical services, at least protocol flexibility, suitability and simplification.
Not treated
[2 min]
Other
R2-2508318	Design principles for 6G	ZTE Corporation, Sanechips	discussion
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-p009`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.3 Design approaches, New services, Others

6GR 的 RAN2 研究应覆盖所列 use cases，包括 NTN、HRLLC、SON/MDT、Slicing、Relays（包括 repeaters 和 RIS）、UAV、HST、AI/ML 及 Sensing scenarios。

```text
For 6GR, RAN2 study shall cover the use cases including NTN, HRLLC, SON/MDT, Slicing, Relays (including repeaters and RIS), UAV, HST, AI/ML and Sensing scenarios
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-p010`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.3 Design approaches, New services, Others

对 5G 现有用例，RAN2 study 应尽早识别可复用的 5G functionality 作为 baseline，以尽量减少这些领域的额外工作。示例包括 SON/MDT、TSN 和 Slicing，具体取决于 SA2 output。

```text
For the existing use cases in 5G, RAN2 study should identify at an early stage, functionality that can be reused from 5G as a baseline to minimize the additional work in these areas (e.g. for SON/MDT, TSN, Slicing – depending on SA2 output etc)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-p011`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.3 Design approaches, New services, Others

针对 AI 和 sensing 的新及增强 6G 用例，RAN2 study 应支持 AI based enhancements，同时确保有无这些增强时系统均能 optimal operation。待 RAN1 initial design 稳定后，应设计 signalling，以支持 UE based sensing modes 用于 sensing services 和 sensing assisted communication。

```text
For the new and enhanced 6G related use cases for AI and sensing, RAN2 study should focus on the following:
-	Enabling AI based enhancements for 6GR including existing and new use cases, whilst ensuring that the system operation is optimal both with and without these AI based enhancements
-	Signalling design to enable optimal support for UE based sensing modes for sensing services and sensing assisted communication once RAN1 initial design is stable
[2 min]
Noted
R2-2508078	General considerations on RAN2 6G design	Xiaomi	discussion	Rel-20	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-p012`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.3 Design approaches, New services, Others

RAN2 6G system design 应以 RedCap 和 eMBB requirements 为 baseline，包括 peak data rate（10Mbps-Gbps）、battery life（few years）、coverage 和 low cost。

```text
In RAN2 6G study, RedCap and eMBB requirements should be used as baseline for RAN2 system design, i.e., peak data rate (10Mbps-Gbps), battery life (few years), coverage, and low cost.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-p013`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.3 Design approaches, New services, Others

新旧 services 的 requirements 只应在 RANP 讨论；RAN2 应聚焦 RANP 已同意的 services，包括 Mobile broadband、Immersive Communication、Massive Communication (IoT)、Sensing、AI、Voice 和 Regulatory services。Digital twin、Non-Terrestrial Network、Aerial、FWA、Vehicles、Mission Critical Communication、Positioning and/or Navigation、TSN、HRLLC 等新 services 的 requirements 应在 RANP 讨论。

```text
Requirements of new and existing services shall only be discussed in RANP. RAN2 should focus on the services which have been agreed in RANP (Mobile broadband, Immersive Communication, Massive Communication (IoT), Sensing, AI, Voice, Regulatory services). Requirements on new services, e.g., Digital twin, Non-Terrestrial Network, Aerial, FWA, Vehicles, Mission Critical Communication, Positioning and/or Navigation, TSN, HRLLC, shall be discussed in RANP.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-p014`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.3 Design approaches, New services, Others

对于 network AI data collection、sensing、mobility、paging、UP、capability 等 E2E architecture 相关 features，RAN2 study 以 UE->RAN->CN 的 general architecture 为 baseline。无需重复讨论其他 WGs 涉及的 RAN/CN architecture，例如 CU/DU split、P2P、SBI 和 new core。

```text
For features related to E2E architecture, e.g., network AI data collection, sensing, mobility, paging, UP, capability etc, general architecture, i.e., UE->RAN->CN is used as baseline for RAN2 study without repeating the discussion in other WGs on RAN architecture/CN architecture, e.g., CU/DU split, P2P, SBI, new core, etc.
[3 min]
Noted
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-p015`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.3 Design approaches, New services, Others

RAN2 仅在 RAN 和 RAN1 定义 device types 后，才开始讨论各类型的具体 requirements 和 features；UE capability signalling、RRC signaling modular design 和 system information design 则待 RAN2 与其他 WG 完成各类型的 requirements 和 features 后再处理。原文同时记录 Xiaomi 认为许多相关议题与 device types 无关，并质疑为何要等待。

```text
The approach for device type discussion in RAN2 can be as follows:
-	RAN2 starts discussing specific requirements and features for each device type only after RAN and RAN1 define the device types.
-	UE capability signalling design, RRC signaling modular design, and system information design are only addressed after RAN2 and other WG completed the requirement and features for each device type.
-	Xiaomi thinks that a lot of these topics are not related to device types so why should we wait.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-p016`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.3 Design approaches, New services, Others

对 idle-mode features 的 forward-compatible design 应予以特别考虑，例如 system information scheduling/transmission 和 cell barring。

```text
Forward-compatible design should be given special consideration for idle-mode features, such as system information scheduling/transmission and cell barring.
[3 min]
Noted
R2-2509046	Initial RAN2 steps on scalability, extensibility and future proofness in view of diverse device types	MediaTek Inc.	discussion	Rel-20	R2-2508345
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-p017`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.3 Design approaches, New services, Others

RAN2 6GR design 假设所有 6GR devices 都支持一组 common minimum functionality，使其能从任何 6G network 获得 basic connectivity。

```text
RAN2 6GR design assumes that all 6GR devices will support a common minimum functionality allowing them to obtain basic connectivity from any 6G network, from a functional capability perspective.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-p018`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.3 Design approaches, New services, Others

RAN2 将遵循全会关于 common minimum functional capability 及相关参数和影响 device design envelope 的因素的决定。Scalability、extensibility 和 future-proofness 将以该 common minimum 为下限。

```text
RAN2 will align with plenary decisions regarding a common minimum functional capability and related parameters and factors affecting the device design envelope.  Scalability, extensibility, and future-proofness will be lower-bounded by this common minimum.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-p019`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.3 Design approaches, New services, Others

只有在明确需要时，才应在 connection time 引入 device differentiation，并将其对规范的影响降至最低。

```text
Device differentiation at connection time should be introduced only if clearly needed, and if so, with minimum spec impact.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-p020`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.3 Design approaches, New services, Others

从 RAN2 角度看，UE capability signalling 中捕获假设的“device type”概念的替代方式不受限制。推进这一方面的讨论前，等待 RAN plenary guidance。

```text
Alternative ways of capturing a hypothetical “device type” concept in UE capability signalling are not constrained from RAN2 perspective.  Await RAN plenary guidance before progressing this aspect of the device discussion.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-p021`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.3 Design approaches, New services, Others

6G 采用统一的 capability framework，不随潜在的“device type”概念而变化。该条目标记为 Noted。

```text
6G has a unified capability framework that does not vary according to any potential “device type” concept.
[3 min]
Noted
R2-2508046	6GR design approaches and new services	vivo	discussion	Rel-20
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-p022`

### [6G/Rel-20 RAN2#132] `proposal` 10.2.3 Design approaches, New services, Others

RAN2 角度提出研究适用于单一网络中所有设备类型的 scalable design，考虑降低对 eMBB devices 的性能影响、原生支持通用功能以及减少通用配置的 signalling overhead。后续会议等待 RANP 推进，并以 RANP agreements 为基线聚焦 RAN2 impacts。

```text
From RAN2 perspective, study a scalable design for all device types in one network considering following aspects:
-	Minimize performance impact on eMBB devices;
-	Natively support common features (e.g., power saving, coverage enhancement) applicable to all device types;
-	Minimize signalling overhead (e.g., SIBs) for common configurations for different device types.
[2 min]
Noted
Discussion
-	Interdigital thinks that we should highlight what we need first, the minimum capability needed, and given that we want something that is scalable how would the different device types would impact our design, for example differentiated access, access control, and signaling overhead etc.
-	Xiaomi thinks that most of the functionalities should be supported by both, so we should use a common design as much as possible and once plenary has some conclusions we can take them into account.
-	ZTE thinks that we should clearly separate the RAN1 and RAN2 aspects from this.   We should design system information and initial call connection/setup and this should work for all devices.
-	Ericsson thinks that mediatek proposals were good starting point.
-	Oppo thinks that we should discuss RAN2 specific like mobility.
-	Fraunhofer thinks that we should look at access barring and see how we can streamline and make it forward compatible.
-	CATT thinks that IoT has to be supported so we should take this into account.
-	Mediatek thinks that the proposals and RAN2 can be designed without the device types.
Wait for RANP to progress.  For next meetings, use RANP agreements as baseline and focus on RAN2 impacts.
Not treated
R2-2508143	Discussion on 6G IOT	Transsion Holdings	discussion
R2-2508149	Views on 6GR design approaches and services	CATT	discussion	Rel-20	FS_6G_Radio
R2-2508229	Design issues for 6GR study 	SHARP Corporation	discussion
R2-2508241	General aspects on RAN2 6G	OPPO	discussion	Rel-20	FS_6G_Radio
R2-2508345	Initial RAN2 steps on scalability, extensibility and future proofness in view of diverse device types	MediaTek Inc.	discussion	Rel-20	Revised
R2-2508350	Designing a Flexible 6GR Air Interface	National Spectrum Consortium	discussion	Late
R2-2508471	Enhancement of Public Safety Support	Fraunhofer IIS, Fraunhofer HHI	discussion	R2-2506975
R2-2508626	Deployments, migration, device types and new services in 6G	Ofinno	discussion	Rel-20
R2-2508640	Design of 6GR Radio Protocols	InterDigital	discussion	Rel-20	FS_6G_Radio
R2-2508648	Discussion supporting Broadcast and Multicast Services in 6G	CBN	discussion	Rel-20
R2-2508745	Day1 Services and Forward compatible design	Lenovo, Aumovio	discussion	FS_6G_Radio
R2-2509025	Forward compatible design considerations for 6GR User plane	CEWiT	discussion	Rel-20	FS_6G_Radio
R2-2509064	General considerations on 6G	LG Electronics Deutschland	discussion	FS_6G_Radio
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG2_RL2/TSGR2_132/) · `RAN2-132-10.2.3-p023`

