# ISAC 通感一体

**当前进展** · 阶段：—

_尚无综述_

## 6GR 演进

### [6G/Rel-20 RAN1#126] `agreement` 10.8.1 Evaluations

```text
For Rel-20 6G ISAC performance evaluation, adopt the following minimum UE-UE (2D) distance evaluation assumption for baseline cases/configurations.
|  | Scenario | Minimum UE-UE (2D) distance |
| --- | --- | --- |
| Sensing UAV | UMa-AV | 1 m |
|  | SMa | 1 m |
| Sensing Human | UMa | 1 m |
|  | Indoor Hotspot (Indoor-office) | 1 m |
| Sensing Vehicle | Urban Grid | Determined by the agreed UE distribution |
|  | Highway | Determined by the agreed UE distribution |
| Sensing AGV | Indoor Factory (SH) | 1 m |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.1-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.1 Evaluations

```text
For Rel-20 6G ISAC performance evaluation, for baseline cases/combinations of sensing AGV in Indoor Factory (SH), the following parameters are assumed for clutters.
| Clutter density: | 20% |
| --- | --- |
| Clutter height: | 2 m |
| Clutter size: | 10 m |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.1-a002`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.1 Evaluations

```text
For Rel-20 6G ISAC performance evaluation, for object detection and/or tracking, the MDP (missed detection probability) and the FAP type 2 (false alarm probability type 2) are calculated as follows:
Missed detection probability
where,
-	 is the number of missed targets in the drop n, i.e., the true target not associated with any detected object.
-	 is the number of true targets in the drop n.
-	 is total number of drops with at least one target per drop.
FFS: same MDP definition as 5GA ISAC study should also be evaluated
False alarm probability Type-2
where,
-	 is the number of detected objects but not associated with any true targets in the drop n.
-	 is the total number of detected objects in the drop n.
-	 is number of drops with at least one detected object.
FFS: same FAP type-2 definition as 5GA ISAC study should also be evaluated
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.1-a003`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.1 Evaluations

```text
For Rel-20 6G ISAC performance evaluation, for object detection and/or tracking, when data fusion from multiple sensing nodes/pairs is applied:
Instead of using detected objects per sensing node/pair, the jointly determined object(s) fused from detected objects of multiple sensing nodes/pairs will be used for association between detected object(s) and true target(s), calculating MDP, FAP Type 2 and positioning/velocity accuracy.
Companies to report the method/algorithm to obtain the jointly fused object(s) from detected objects of multiple sensing nodes/pairs.
R1-2605743	Moderator summary #2 on ISAC evaluations	Moderator (CATT)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.1-a004`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.1 Evaluations

```text
For Rel-20 6G ISAC evaluation on SAC (sensing assisted communication), companies are encouraged to evaluate and report at least one of the following:
Scope 1: Evaluate performance of sensing measurement/result, which will be used to assist communication;
Scope 2: Evaluate performance of communication, with and without assistance of sensing measurement/result. The sensing measurement/result to assist communication can be:
Ideal sensing measurement/result
Non-ideal sensing measurement/result, and company to report how to model error/offset of non-ideal factors for non-ideal sensing measurement/result
Real sensing measurement/result, which is obtained from simulation
Note: companies to report which is used in their simulation.
For Rel-20 6G ISAC evaluation on SAC, for Scope 2:
The communication use case(s) in AI 10.8.2 are encouraged
Companies to report whether the location and/or velocity information of communication UE and/or TRP is needed or not in their SAC algorithm/mechanism
Note: this does not imply specifying exchange of location and/or velocity information between UE and TRP
Companies to report the time-frequency resource cost due to sensing for SAC and necessary details on the definition of the time-frequency resource cost based on TR38.765 as starting point
Comparison with benchmark and benchmark details should also be reported as well as other necessary details if any
Companies are encouraged to use communication-related performance metrics as agreed in communication agendas
Companies are encouraged to use baseline/benchmark mechanism as agreed in communication agendas for comparison; Use of state-of-the-art mechanism without assistance of sensing measurement/result for comparison is not precluded
Companies are encouraged to use additional communication-related evaluation assumptions (if necessary but not discussed/agreed in AI 10.8.1) as agreed in communication agendas
Note: How to draw conclusion/observation is a separate discussion.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.1-a005`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.1 Evaluations

```text
For Rel-20 6G ISAC evaluation on SAC, for Scope 1, the following sensing measurement/results and corresponding performance metrics are considered:
Delay/Doppler/angle/power/phase related information of the ISAC channel
Performance metric:
RMSE of delay of the path(s) used to assist communication
RMSE of Doppler the path(s) used to assist communication
RMSE of angles (one or more of AOD, ZOD, AOA, ZOA) of the path(s) used to assist communication
RMSE of power of the path(s) used to assist communication
FFS: details on the power of the path(s)
FFS: RMSE of phase of the path(s) used to assist communication
Companies to report how to select the path(s), how to derive RMSE from multiple paths and how such sensing measurement/result of the paths(s) is able to assist communication
Note: when evaluated, companies are not required to report every metric
Enrivonment (large surface, wall) that reconstructed by sensing
Performance metric:
Mean value of absolute perpendicular distance from the sensed specular reflection point to the ground-truth plane
Mean value of absolute perpendicular distance from the ground truth specular reflection point to the reconstructed plane
Note: when evaluated, companies are not required to report every metric
EO type-2 should be modeled in the simulation in this case
Companies are not required to evaluate and report every sensing measurement/result.
Note: In Scope 1, the performance metrics for detecting object for the purpose of SAC are the same as those for object detection and/or tracking, and thus already included in Rel-20 6G ISAC object detection and/or tracking study.
Note 2: How to draw conclusion/observation is a separate discussion.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.1-a006`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.1 Evaluations

```text
For Rel-20 6G ISAC evaluation on SAC, for evaluation assumptions, the evaluation assumptions of baseline cases/combinations of object detection and/or tracking are reused as starting point. In addition, one or more of the following adjustment may be considered:
Dropping of sensing target is optional
In case reconstruction of enrivonment (large surface, wall that modeled by EO type-2) is evaluated, additional sensing capable UEs can be dropped for reconstructing environment
Other adjustment is not precluded
Companies should report the adjustments (if any) with necessary details when reporting simulation results.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.1-a007`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.1 Evaluations

```text
Templates (excel files) in R1-2606863 are adopted to collect evaluation results of object detection and/or tracking in AI 10.8.1.
Additional tdoc file(s) will also be used to collect companies input in details, which may include but not limited to:
Details on sensing RS/resource
Details on method/algorithm for detection
Details on method/algorithm for tracking
Details on inter-site/intra-site interference modelling, if modelled
Details on method/algorithm to select sensing STx-SRx pair(s)
Details on method/algorithm to obtain the jointly fused object(s) from detected objects of multiple sensing nodes/pairs, if data fusion is applied
Details on the sensing capable UE dropping
Note: Further revision is not precluded, depending on future discussion
R1-2606863	Result collection templates for object detection and/or tracking		Moderator (CATT)
R1-2605744	Moderator summary #3 on ISAC evaluations	Moderator (CATT)
R1-2605745	Moderator summary #4 on ISAC evaluations	Moderator (CATT)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.1-a008`

### [6G/Rel-20 RAN1#126] `conclusion` 10.8.1 Evaluations

```text
No consensus to introduce UAV-UE as sensing capable UE in the baseline case/combination of sensing UAV in Rel-20.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.1-c001`

### [6G/Rel-20 RAN1#126] `conclusion` 10.8.1 Evaluations

```text
No consensus to remove CPE UE in Indoor-office (Indoor Hotspot) for the baseline case/combination of sensing Human in Rel-20.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.1-c002`

### [6G/Rel-20 RAN1#126] `conclusion` 10.8.1 Evaluations

```text
For Rel-20 6G ISAC performance evaluation, for baseline cases/combinations, it is clarified that ‘convex hull’ refers to ‘convex hull of the TRP deployment’ in Indoor Hotspot (Indoor office) and Indoor Factory evaluation assumptions.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.1-c003`

### [6G/Rel-20 RAN1#126] `conclusion` 10.8.1 Evaluations

```text
For Rel-20 6G ISAC performance evaluation of object detection and/or tracking, for baseline cases/combinations, it is clarified that the scenario Indoor Hotspot (Indoor-office) for sensing Human is ‘open office’, but not ‘mixed office’, as defined in TR 38.901.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.1-c004`

### [6G/Rel-20 RAN1#126] `conclusion` 10.8.1 Evaluations

```text
No consensus to remove CPE UE in Indoor Factory for the baseline case/combination of sensing AGV in Rel-20.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.1-c005`

### [6G/Rel-20 RAN1#126] `conclusion` 10.8.1 Evaluations

```text
No consensus to introduce AGV-UE as sensing capable UE in the baseline case/combination of sensing AGV in Rel-20.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.1-c006`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.2 Aspects of integration with communication

```text
In addition to theoretical characteristics analysis, companies are encouraged to do at least one of followings to evaluate RE pattern of sensing RS in 10.8.2
Full SLS with or without cooperative sensing as 10.8.1 (Option 1 from RAN1#125) for sensing performance evaluation
SLS with non-cooperative sensing (i.e., no fusion) (Option 2 from RAN1#125) at least for sensing measurement performance evaluation
LOS condition is always assumed for each STX-target-SRX link
Simplified SLS with single STX and single SRX (Option 3 from RAN1#125) at least for sensing measurement performance evaluation
LOS condition is always assumed for each STX-target-SRX link
Note: detailed modelling is up to company report
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.2-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.2 Aspects of integration with communication

```text
Study on a sensing RS resource consisting of one or multiple component RS.
Study the following options for component RS
Component RS can be RS for communication is reused for sensing
Component RS can be enhanced RS for sensing, taking reuse of RS for communication as starting point
Component RS can be dedicated RS for sensing
Note: The multiple component RS of a sensing RS resource can be of single or multiple RS types.
Companies to provide necessity, theoretical analysis, performance evaluation and specification impacts on the above options and the sensing RS resource in next RAN1 meetings.
Note: RE pattern of the sensing RS resource is union set of all REs of all component RS
FFS: details of component RS
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.2-a002`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.2 Aspects of integration with communication

```text
Study the following two options to generate a sensing RS resource
Option 1: A sensing RS resource has single antenna port, which can be precoded or non-precoded
Option 2: A sensing RS resource can have multiple antenna ports, which can be precoded or non-precoded
Companies to provide necessity, theoretical analysis, performance evaluation and specification impacts on the above options in next RAN1 meetings.
FFS impact on measurement reporting and assistance information
R1-2605587	Summary #3 on integration with communication for ISAC	Moderator (Xiaomi)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.2-a003`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.2 Aspects of integration with communication

```text
The following metrics for a path are to be studied in 6G ISAC
Delay information defined per path
Option 1: Receive time difference between a path and a reference path, e.g., RSTD like
Option 2: Receive time difference between a path and a reference time, e.g., RTOA like
FFS reference time
Option 3: Receive time of a path minus a transmission time, e.g., Rx-Tx time difference like
FFS transmission time
Doppler information defined per path
FFS absolute or relative/differential Doppler information
Angle information defined per path
FFS absolute or relative/differential angle information, implicit/indirect angle information
FFS how to derive angle
RSRP/SINR/amplitude/phase defined per path
FFS how to derive phase
Quality/uncertainty/confidence defined per path
FFS ambiguity handling of delay/Doppler/angle of a path
Further discuss the additional metrics for a path
Micro-Doppler
RCS
Association among paths
Other metrics are not precluded
FFS reference path
FFS definition of path
Note: the necessity, applicable sensing modes, achievable sensing performance, reporting aspects (e.g., overhead) of above metrics can be discussed separately
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.2-a004`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.2 Aspects of integration with communication

```text
The following metrics of a scattering point or an object are to be studied in 6G ISAC from RAN1 perspective
3D or 2D location
Option1: Absolute location
Option2: Relative location referred to a reference location
FFS reference location
3D or 2D velocity
Option1: Measured true 3D/2D velocity
Option2: Scalar of radial velocity
Uncertainty/confidence
association of measurements of a scattering point/object
FFS ambiguity handling of delay/Doppler/angle of a scattering point
Further discuss the additional metrics for a scattering point/object
Power related information if applicable, e.g., RCS
Micro-Doppler
Other metrics are not precluded
FFS definition of scattering point/object
Note: the necessity, applicable sensing modes, and achievable sensing performance, reporting aspects (e.g., overhead) of above metrics can be discussed separately
R1-2605588	Summary #4 on integration with communication for ISAC	Moderator (Xiaomi)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.2-a005`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.2 Aspects of integration with communication

```text
The metrics of consecutive samples in delay/Doppler/angle profiles are to be studied in 6G ISAC
FFS: whether/how to apply window(s) of consecutive samples in delay/Doppler/angle profile
Note: the necessity, applicable sensing modes, and achievable sensing performance, reporting aspects (e.g., overhead) of above metrics can be discussed separately
R1-2605589	Summary #5 on integration with communication for ISAC	Moderator (Xiaomi)
Final post-meeting summary for this agenda item.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.2-a006`

### [6G/Rel-20 RAN1#126] `conclusion` 10.8.2 Aspects of integration with communication

```text
On UE-side measurement report, measurement Level A from NR ISAC is not considered for 6G ISAC study in Rel-20.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.2-c001`

### [6G/Rel-20 RAN1#126] `working_assumption` 10.8.2 Aspects of integration with communication

```text
The following representative use cases for sensing assisted communication is/are selected for study in Rel-20 ISAC
Sensing assisted beam management
[Sensing assisted CSI acquisition and reporting]
Note: companies can also study other use cases for sensing assisted communication
Note: In AI10.8, physical layer design discussions are limited to sensing related aspects
R1-2605586	Summary #2 on integration with communication for ISAC	Moderator (Xiaomi)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.2-w001`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.3 Waveform and frame structure

```text
The following options are further studied for RS sequence enhancement for sensing based on ZC sequence based on CP-OFDM.
Opt. 1 ZC sequence optimization
Opt. 2 Frequency domain quadratic-phase RS sequence .
FFS: details of B, C, D
FFS: A as constant or whether/how to define A as function of m
Note: intention of A(m) here is different from FDSS
[Opt. 3 Time domain RS sequence generation based on transform precoding]
Opt. 4 Time domain spanning ZC sequence across OFDM symbols
RS sequence enhancement should identify:
the benefits/drawbacks based on comprehensive comparison with NR Gold sequence for TRP transmission and NR ZC sequence for UE transmission as benchmark for evaluation
applicability/necessity to TRP-transmission based sensing
applicability/necessity to UE-transmission based sensing
Discussion on the other solutions will continue.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.3-a001`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.3 Waveform and frame structure

```text
The following options are further studied for RS enhancement for sensing based on Gold sequence based on CP-OFDM.
Gold sequence optimization (e.g., initialization)
Gold sequence modulated by pi/2 BPSK with transform precoding for UE transmission
Gold sequence modulated by pi/2 BPSK for CP-OFDM
Time domain spanning Gold sequence across OFDM symbols
RS sequence enhancement should identify:
the benefits/drawbacks based on comprehensive comparison with NR Gold sequence for TRP transmission and NR ZC sequence for UE transmission as benchmark for evaluation
applicability/necessity to TRP-transmission and/or UE-transmission based sensing
Other solutions are not precluded.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.3-a002`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.3 Waveform and frame structure

```text
For effective CP length extension for sensing, further study the necessity (including whether implementation based solution can solve the issue or not) and the following candidate solutions.
Transmission of successive N OFDM symbols that carries sensing RS
FFS: details of generation method
FFS: value N
Freq. domain comb pattern for sensing RS
FFS: details of generation method including comb size
FFS: combination of successive N OFDM symbols and freq. comb pattern
Time gap after/before/within OFDM symbol carrying sensing RS, without changing OFDM symbol duration/structure of 6GR communication design
FFS: location of the time gap
FFS: duration of the time gap
FFS: benefits/drawbacks/spec impact
FFS: applicable sensing mode and scenario
FFS: supported excess delay
FFS: other solutions are not precluded
R1-2606565	Summary #3 on waveform and frame structure for 6G ISAC	Moderator (LGE)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.3-a003`

### [6G/Rel-20 RAN1#126] `agreement` 10.8.3 Waveform and frame structure

```text
Peak-to-Sidelobe Ratio (PSLR), Integrated Sidelobe Ratio (ISLR), and Main lobe width are defined based on AF as follows.
Definition of power
Opt 1. Power is defined in delay-Doppler domain
Opt 2. Power is defined in delay domain with zero or non-zero Doppler cut
Main lobe width is defined as the width of AF measured at the points where the power drops to half (-3 dB) of the peak main lobe power (3dB width).
Main lobe region (M) is the region corresponding to the first ‘null-to-null’ region from the main lobe.
Side lobe region (S) is defined as the entire region except the first ‘null-to-null’ region from the main lobe
, where PML=maximum power within the main lobe region, PSL=maximum power within the sided lobe region
Opt 1.  ,
Opt 2.  ,
, where IML=power integrated within the main lobe region, ISL=power integrated within the sided lobe region
Opt 1. ,
Opt 2. ,
R1-2606566	Summary #4 on waveform and frame structure for 6G ISAC	Moderator (LGE)
R1-2606567	Summary #5 on waveform and frame structure for 6G ISAC	Moderator (LGE)
Final post-meeting summary for this agenda item.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.3-a004`

### [6G/Rel-20 RAN1#126] `working_assumption` 10.8.3 Waveform and frame structure

```text
Linear Ambiguity Function (AF) is defined as:
Opt 1.  in delay-Doppler domain
where  is the delay shift,  is the Doppler frequency,  is the sampling interval
Opt 2.  in delay-Doppler domain,
where  is the delay shift,  is the Doppler frequency,  is the sampling interval, ,  is the number of samples in CP, N is the number of samples in OFDM symbol without CP, M is the number of OFDM symbols.
Circular Ambiguity Function (AF) is defined as:
Opt 1.  in delay-Doppler domain,
where  is the delay shift,  is the Doppler frequency,  is the sampling interval, N is the number of samples in OFDM symbol without CP
Opt 2a.
where p is Doppler index,  is delay index, ,  is the number of samples in CP, N is the number of samples in OFDM symbol without CP, M is the number of OFDM symbols, X is the spectrum of x.
Opt 2b.  in delay-Doppler domain,
where  is the delay shift,  is the Doppler frequency,  is the sampling interval, ,  is the number of samples in CP, N is the number of samples in OFDM symbol without CP, M is the number of OFDM symbols.
Opt 3.  in delay domain of single symbol
where  is the delay shift,  is the Doppler frequency,  is the sampling interval, N is the number of samples in OFDM symbol without CP, x’ is the received signal
Note: down-selection on Linear/Circular AF and options for evaluation will be discussed separately.
Note: companies should report assumption about receiver processing and observation window.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.3-w001`

### [6G/Rel-20 RAN1#126] `working_assumption` 10.8.3 Waveform and frame structure

```text
Linear Cross Ambiguity Function(CAF) is defined as:
Opt 1.  in delay-Doppler domain,
where  is the delay shift,  is the Doppler frequency,  is the sampling interval
Opt 2.  in delay-Doppler domain,
where  is the delay shift,  is the Doppler frequency,  is the sampling interval, ,  is the number of samples in CP, N is the number of samples in OFDM symbol without CP, M is the number of OFDM symbols.
Circular Cross Ambiguity Function(CAF) is defined as:
Opt 1.  in delay-Doppler domain,
where  is the integer delay shift,  is the Doppler frequency,  is the sampling interval, N is the number of samples in OFDM symbol without CP
Opt 2a.   in delay-Doppler domain,
where p is Doppler index,  is delay index, ,  is the number of samples in CP, N is the number of samples in OFDM symbol without CP, M is the number of OFDM symbols, X and Y are the spectrums of x and y respectively.
Opt 2b.  in delay-Doppler domain,
where  is the delay shift,  is the Doppler frequency,  is the sampling interval, ,  is the number of samples in CP, N is the number of samples in OFDM symbol without CP, M is the number of OFDM symbols.
Opt 3.  in delay domain of single symbol
where  is the delay shift,  is the Doppler frequency,  is the sampling interval, N is the number of samples in OFDM symbol without CP, y’ is the received signal
Note: down-selection on Linear/Circular CAF and options for evaluation will be discussed separately.
Note: companies should report assumption about receiver processing and observation window.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/) · `RAN1-126-10.8.3-w002`

### [6G/Rel-20 RAN1#124b] `agreement` 10.8.1 Evaluations

```text
For Rel-20 6G sensing performance evaluation of object detection and/or tracking, the following cases/combinations are considered as baseline cases/combinations.
| Sensing target | Indoor or outdoor | Scenario | Carrier frequency |
| --- | --- | --- | --- |
| UAV | Outdoor | UMa-AV, SMa | 4 GHz, ~7 GHz, 30 GHz (for UMa-AV only) |
| Human | Outdoor | UMa | 4 GHz, ~7 GHz, 30 GHz |
|  | Indoor | Indoor Hotspot | 4 GHz, ~7 GHz, 30 GHz |
| Vehicle | Outdoor | Urban Grid, Highway | 4 GHz, ~7 GHz, 30 GHz (for Urban Grid only) |
| AGV | Indoor | Indoor factory (SH) | 4 GHz, ~7 GHz, 30 GHz |
Note: sensing mode(s) for each row will be discussed
Other cases/combinations can also be evaluated, reported and collected from companies.
Note: In this agreement, no intention to de-prioritize other scenarios or carrier frequencies.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.8.1-a001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.8.1 Evaluations

```text
Companies are encouraged to bring input to the evaluation on communication assistance in next meeting, including but not limited to:
Necessity of evaluation on communication assistance
For proponents, provide: what to sense and, if necessary, what/how to assist communication
What metric of sensing is to be defined
Whether/what metric related to communication is to be defined
Whether performance target/KPI is to be defined, for either sensing metric or communication metric
Necessary channel model extension
Necessary update of evaluation methodology on top of 5G NR sensing evaluation methodology
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.8.1-a002`

### [6G/Rel-20 RAN1#124b] `agreement` 10.8.1 Evaluations

```text
Companies are encouraged to bring input to the sensing mode related evaluation assumptions in next meeting, using the following table as starting point. The values in current table are example values based on the input and discussion in RAN1#125.
Note1: This is not intended to specify all sensing modes.
Note2: This does not mean any sensing mode is applicable to any scenario/use case.
Note3: Other parameters/values for each sensing mode can also be discussed.
| Sensing mode | Parameter | Value |
| --- | --- | --- |
| TRP mono-static | Sensing Tx/Rx operating simultaneously or not | Simultaneously, or not simultaneously (FFS: with/without switching time and value if any) |
|  | BS antenna isolation | For Around 7 GHz and below 7 GHz: Option 1: 80 dB Option 2: 65 dB For 30 GHz: Option 1: 100 dB Option 2: 72 dB Option 3: 85 dB |
|  | BS transmit power | Simultaneously: min { BS transmit power in Table of ISAC system configuration, BS Rx saturation power + BS antenna isolation}, assuming the BS Rx saturation power = -28 dBm Not simultaneously: Follow BS transmit power in the table of general evaluation assumption |
|  | BS self-interference impact | The residual leakage interference/noise is modelled e.g., by additional additive white Gaussian noise, -174 + 10log10(BW) + X dBm in BW Hz, BW is simulated bandwidth, X = {-Infinity, 0, 5} is up to company report. Note: X = -Infinity corresponds to not modelling self-interference. |
| UE mono-static | UE type for sensing | Companies to report |
|  | Sensing Tx/Rx operating simultaneously or not | FFS |
|  | UE transmit power | FFS |
|  | UE Antenna isolation | FFS |
|  | UE Self-interference impact | FFS |
|  | Availability of UE location, velocity and orientation | Option 1: Known, ideally (baseline) Option 2: Known, with error. FFS distribution of error in each aspect (e.g. location, speed, orientation). Option 3: Unknown, rely on actual measurement Note: UE location, velocity and orientation are individually determined |
| TRP-TRP bi-static | Timing/frequency error | Option 1: Ideal (baseline) Option 2: With error, FFS value range and model of the distribution Note: timing error and frequency error are individually determined |
|  | Coherency and phase continuity among symbols within a CPI | Option 1: Always coherent Option 2: Coherency is assumed under some conditions; FFS: Conditions |
| UE-UE bi-static | UE type for sensing | Companies to report |
|  | Timing/frequency error | Option 1: Ideal (baseline) Option 2: With error, FFS value range and model of the distribution Note: timing error and frequency error are individually determined |
|  | Availability of UE location, velocity and orientation | Option 1: Known, ideally (baseline) Option 2: Known, with error. FFS distribution of error in each aspect (e.g. location, speed, orientation). Option 3: Unknown, rely on actual measurement Note: UE location, velocity and orientation are individually determined |
|  | Coherency and phase continuity among symbols within a CPI | Option 1: Always coherent Option 2: Coherency is assumed under some conditions; FFS: Conditions |
| TRP-UE bi-static | UE type for sensing | Companies to report |
|  | Timing/frequency error | Option 1: Ideal (baseline) Option 2: With error, FFS value range and model of the distribution Note: timing error and frequency error are individually determined |
|  | Availability of UE location, velocity and orientation | Option 1: Known, ideally (baseline) Option 2: Known, with error. FFS distribution of error in each aspect (e.g. location, speed, orientation). Option 3: Unknown, rely on actual measurement Note: UE location, velocity and orientation are individually determined |
|  | Coherency and phase continuity among symbols within a CPI | Option 1: Always coherent Option 2: Coherency is assumed under some conditions; FFS: Conditions |
| UE-TRP bi-static | UE type for sensing | Companies to report |
|  | Timing/frequency error | Option 1: Ideal (baseline) Option 2: With error, FFS value range and model of the distribution Note: timing error and frequency error are individually determined |
|  | Availability of UE location, velocity and orientation | Option 1: Known, ideally (baseline) Option 2: Known, with error. FFS distribution of error in each aspect (e.g. location, speed, orientation). Option 3: Unknown, rely on actual measurement Note: UE location, velocity and orientation are individually determined |
|  | Coherency and phase continuity among symbols within a CPI | Option 1: Always coherent Option 2: Coherency is assumed under some conditions; FFS: Conditions |
Final summary in R1-2602522.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.8.1-a003`

### [6G/Rel-20 RAN1#124b] `conclusion` 10.8.1 Evaluations

```text
For Rel-20 6G ISAC evaluation, the attributes (e.g. antenna pattern, mobility, etc.) of different UEs are for the purpose of evaluation discussion. No intention to study or specify diverse device type.
R1-2602519	FL summary #2 on ISAC evaluations	Moderator (CATT)
R1-2602520	FL summary #3 on ISAC evaluations	Moderator (CATT)
R1-2602521	FL summary #4 on ISAC evaluations	Moderator (CATT)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.8.1-c001`

### [6G/Rel-20 RAN1#124b] `working_assumption` 10.8.1 Evaluations

```text
For Rel-20 6G ISAC performance evaluation,
evaluate object detection and/or tracking for the following sensing targets/objects: UAV, human, vehicle, AGV;
discuss further on evaluation on communication assistance.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.8.1-w001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.8.2 Aspects of integration with communication

```text
On RS for ISAC, study at least the following aspects, considering sensing performance, resource overhead and impact to communication
RS for communication is reused for sensing
Enhanced RS for sensing, taking reuse of RS for communication as starting point
Note: Part of or all of the RS may be used for communication purpose, and it does not mean the final decision on whether the enhanced RS is used for communication purpose is to be made in this agenda.
Dedicated RS for sensing
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.8.2-a001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.8.2 Aspects of integration with communication

```text
Study RE patterns of RS for sensing, considering sensing performance, resource overhead and impact to communication.
Note: enhancements on RS sequence if any will be discussed in agenda 10.8.3.
R1-2602591	Summary #3 on integration with communication for ISAC	Moderator (Xiaomi)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.8.2-a002`

### [6G/Rel-20 RAN1#124b] `agreement` 10.8.2 Aspects of integration with communication

```text
On measurement for ISAC, study at least the following aspects.
Measurement definitions/levels for TRP-side measurement, taking the measurement Levels studied in NR ISAC as starting point
Measurement definitions/levels for UE-side measurement
Impacts of non-ideal factors on measurement
Other aspects are not precluded
Note: this discussion may or may not mean there is specification impact
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.8.2-a003`

### [6G/Rel-20 RAN1#124b] `agreement` 10.8.2 Aspects of integration with communication

```text
On measurement report for ISAC, study at least the following aspects and applicable scenarios (e.g., sensing modes, targets, etc.) from RAN1 perspective.
Measurement reporting mechanism from UE
Option 1A: The UE measurements and/or assistance information if needed from UE can be directly sent to aNB
Option 1B: The UE measurements and/or assistance information if needed from UE can be sent to SF
Measurement reporting mechanism from aNB
Option 2A: The aNB measurements and/or assistance information if needed from aNB can be directly sent to UE
Option 2B: The aNB measurements and/or assistance information if needed from aNB can be sent to SF
The study may require cross-WG coordination.
Note: combination of multiple options is not precluded.
Note: measurements in each option may be different
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.8.2-a004`

### [6G/Rel-20 RAN1#124b] `agreement` 10.8.2 Aspects of integration with communication

```text
On measurement report for ISAC, study impacts from at least the following aspects from RAN1 perspective
Measurement reporting mechanism
E.g., Periodic, semi-persistent, aperiodic, event-triggered report as starting point
Reporting signaling e.g., L1, L2, higher layer, etc.
Other aspects are not precluded
The study may require cross-WG coordination.
Final summary in R1-2602592.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.8.2-a005`

### [6G/Rel-20 RAN1#124b] `agreement` 10.8.3 Waveform and frame structure

```text
CP-OFDM waveform as defined for 6GR is the starting point for 6G ISAC waveform study.
Study on enhancements on CP-OFDM or other waveforms is not precluded.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.8.3-a001`

### [6G/Rel-20 RAN1#124b] `agreement` 10.8.3 Waveform and frame structure

```text
6GR communication frame structure is the starting point for 6G ISAC frame structure study, in at least the following aspects.
Frame/sub-frame/slot/symbol structure
CP length
SCS
Enhancements on frame structure/above aspects are not precluded.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.8.3-a002`

### [6G/Rel-20 RAN1#124b] `agreement` 10.8.3 Waveform and frame structure

```text
Companies are encouraged to provide views on necessity/pros/cons/metrics of LLS and/or SLS and pros/cons/metrics of theoretical waveform characteristics analysis, for evaluation of ISAC waveform and/or integration with communication, to RAN1#125 meeting.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.8.3-a003`

### [6G/Rel-20 RAN1#124b] `agreement` 10.8.3 Waveform and frame structure

```text
CP-OFDM is used as the benchmark for evaluating the benefits of sensing waveforms.
R1-2602984	Summary #4 on waveform and frame structure for 6G ISAC	LG Electronics
Presented in Thursday session.
Final summary in R1-2602985.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/) · `RAN1-124b-10.8.3-a004`

### [6G/Rel-20 RAN1#124] `agreement` 10.8.1 Evaluations

```text
For Rel-20 study, adopt the updated TP in Moderator’s evaluation summary attached in R1-2600466 into TR38.769.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.8.1-a001`

### [6G/Rel-20 RAN1#124] `agreement` 10.8.1 Evaluations

```text
In addition to energy harvesting/storage assumptions used to obtain the reported data rates from companies are provided and agreed in RAN1#123, the followings (highlighted in red) are further provided during the Rel-20 study,
| Source | Energy harvesting/storage assumptions |
| --- | --- |
| Source [NEC] | Energy source: Solar energy Energy storage capacity: 10~100µF with voltage of 3V For device 2b, 10~100µF with voltage of 3V, i.e., 30~300uJ; For device C, 0.5~5mF with voltage of 3V, i.e., 1.5~15mJ; Reported data rate: 1 kbps or 5 – 7 kbps Other information: Device 2b and Device C harvest energy at similar rate. |
| Source [FUTUREWEI] | Energy sources: Solar, thermal, vibration etc. Energy storage capacity: For device 2b with 500uW peak power consumption: 0.5 milli-joules or 500 F using 2V power supply Low rate: 0.1kbps: ~5000 J /~5000 F Middle rate: 1kbps: ~500 J /~500 F High rate: 5kbps: ~100 J /~100 F For device C with 10mW peak power consumption: 10 milli-joules or 10000 F using 2V power supply Low rate: 0.1kbps: ~100 mJ /~100 mF Middle rate: 1kbps: ~10mJ /~10 mF High rate: 5kbps: ~1 mJ /~1000 F Reported data rate: 0.1kbps, 1kbps, 5kbps Other information: It is observed that using RF energy harvesting is challenging as the energy source for Device 2b based on the following description. Typical leakage current for 500 F capacitors is at least higher than 3 A. With a supply voltage of 2 volts, the leakage current translates to ~ -22.2 dBm leakage power. Using RF harvesting is challenging in this case. For the maximum message size, 1000 bits is assumed for single PRDCH/PDRCH transmission. The rated voltage is 2V and min voltage is 1.4V (70% of the rated voltage). It should be noted that the reported capacity is for single PRDCH/PDRCH transmission. To sustain whole procedure of DT, DO-DTT, DO-A, larger capacity is required. |
| Source [CATT] | Energy source: Solar Energy storage capacity: ~100mF Reported data rate: 0.1kbps, 1kbps, 5~7kbps, 48~60kbps Other information: Assumptions of power consumption: 100uW and 1mW for R2D reception 200uW and 5mW for D2R transmission |
| Source [Samsung] | Energy source: Solar Energy storage capacity: >10μJ5μJ for device 2b, 100μJ30μJ for device C Reported data rate: 5.3 kbps for DL 20 bits, 6.7 kbps for UL 20 bits, 7.2 kbps for DL 96 bits, 8.4 kbps for UL 96 bits; with an average of 40% charging time |
| Source [Ericsson] | Energy source: RF signal/ Solar Energy storage capacity: Device 2b: 10s µF to a few 100 µF Device C: a few mF Reported data rates: 1kbps, 7kbps, and 50 kbps Other information: For device 2b: with tx power of -10dBm we considered the power consumption of 400 µW, to transmit 400 bits with the data rate of 1 kbps, the needed storage capacity is around 140 µF. For device C: with tx power of 5dBm we considered the power consumption of 12.6 mW, to transmit 400 bits with the data rate of 1 kbps, the needed storage capacity is around 4.5 mF. |
R1-2600463	FL summary #2 for Ambient IoT: “9.3.1 Evaluations”	Moderator (Huawei)
From Tuesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.8.1-a002`

### [6G/Rel-20 RAN1#124] `agreement` 10.8.1 Evaluations

```text
For Rel-20 study, adopt the following TPs into section 7.3 of TR38.769.
| ------ Start of TP------ RAN1 has evaluated the coverage for Device 2b and Device C respectively. Evaluation results from companies in terms of different achievable cell edge data rate and achievable maximum distance under different scenarios, penetration margins and Tx power have been observed for R2D and D2R in the tables of following sub-sections. For R2D coverage, based on evaluation results, the achievable cell edge data rate and achievable maximum distance are observed at least for the following scenarios For cell edge data rate around 1 kbps, For UMa NLOS pathloss model, penetration margin 0 dB Device 2b: the achievable maximum distance is at least 500 meters at BLER 10% when BS Tx power is from 33dBm to 43dBm and at BLER 1% when BS Tx power is from 38dBm to 43dBm. The achievable maximum distance can be smaller or larger than 500 meters at BLER 1% (about 370~1800 meters) when BS Tx power is 33dBm Device C: the achievable maximum distance is at least 500 meters at BLER 10% and 1% when BS Tx power is from 33dBm to 43dBm For UMa NLOS pathloss model, penetration margin 20 dB Device 2b: the achievable maximum distance can be smaller or larger than 500 meters at BLER 10% (about 190~1340 meters) and at BLER 1% (about 110~1000 meters) when BS Tx power is from 33dBm to 43dBm Device C: the achievable maximum distance is at least 500 meters at BLER 10% and 1% when BS Tx power is from 33dBm to 43dBm For cell edge data rate around 5~7 kbps, For UMa NLOS pathloss model, penetration margin 0 dB Device 2b: the achievable maximum distance is at least 500 meters at BLER 10% when BS Tx power is from 38dBm to 43dBm and at BLER 1% when BS Tx power is 43dBm. The achievable maximum distance can be smaller or larger than 500 meters at BLER 10% (about 480~2300 meters) when BS Tx power is 33dBm and at BLER 1% (about 210~1700 meters) when BS Tx power is from 33dBm to 38dBm Device C: the achievable maximum distance is at least 500 meters at BLER 10% when BS Tx power is from 33dBm to 43dBm and at BLER 1% when BS Tx power is from 38dBm to 43dBm. The achievable maximum distance can be smaller or larger than 500 meters at BLER 1% (about 430~1500 meters) when BS Tx power is 33dBm For UMa NLOS pathloss model, penetration margin 20 dB Device 2b: the achievable maximum distance can be smaller or larger than 500 meters at BLER 10% (about 150~1280 meters) and at BLER 1% (about 70~710 meters) when BS Tx power is from 33dBm to 43dBm Device C: the achievable maximum distance is at least 500 meters at BLER 10% when BS Tx power is 43dBm. The achievable maximum distance can be smaller or larger than 500 meters at BLER 10% (about 280~1070 meters) when BS Tx power is from 33dBm to 38dBm and at BLER 1% (about 130~810 meters) when BS Tx power is from 33dBm to 43dBm For D2R coverage, based on evaluation results, the achievable cell edge data rate and achievable maximum distance are observed at least for the following scenarios For cell edge data rate around 0.1 kbps, For UMa NLOS pathloss model, penetration margin 0 dB Device 2b: the achievable maximum distance is smaller than 500 meters at BLER 10% (about 80~370 meters) and BLER 1% (about 40~300 meters) when device Tx power is -20dBm. The achievable maximum distance can be smaller or larger than 500 meters at BLER 10% (about 150~660 meters) and at BLER 1% (about 80~540 meters) when device Tx power is -10dBm Device C: the achievable maximum distance is at least 500 meters at BLER 10% and 1% when device Tx power is from -3dBm to 5dBm For UMa NLOS pathloss model, penetration margin 20 dB Device 2b: the achievable maximum distance is smaller than 500 meters at BLER 10% (about 20~200 meters) and at BLER 1% (10~160 meters) when device Tx power is from -20dBm to -10dBm Device C: the achievable maximum distance is at least 500 meters at BLER 10% when device Tx power is 5dBm. The achievable maximum distance can be smaller or larger than 500 meters at BLER 10% (about 320~680 meters) when device Tx power is from -3dBm to 0dBm and at BLER 1% (about 260~730 meters) when device Tx power is from -3dBm to 5dBm For cell edge data rate around 1 kbps, For UMa NLOS pathloss model, penetration margin 0 dB Device 2b: the achievable maximum distance can be smaller or larger than 500 meters at BLER 10% (about 110~810 meters) and at BLER 1% (about 50~600 meters) when device Tx power is -10dBm. The achievable maximum distance is smaller than 500 meters at BLER 10% (about 60~450 meters) and BLER 1% (about 30~230 meters) when device Tx power is -20dBm. Device C: the achievable maximum distance is at least 500 meters at BLER 10% when device Tx power is from 0dBm to 5dBm and at BLER 1% when device Tx power is 5dBm. The achievable maximum distance can be smaller or larger than 500 meters at BLER 10% (about 460~1230 meters) when device Tx power is -3dBm and at BLER 1% (about 310~1090 meters) when device Tx power is from -3dBm to 0dBm For UMa NLOS pathloss model, penetration margin 20 dB Device 2b: the achievable maximum distance is smaller than 500 meters at BLER 10% (about 20~250 meters) and at BLER 1% (about 10~180 meters) when device Tx power is from -20dBm to -10dBm Device C: the achievable maximum distance can be smaller or larger than 500 meters at BLER 10% (about 230~600 meters) when device Tx power is 5dBm. The achievable maximum distance is smaller than 500 meters at BLER 10% (about 140~450 meters) when device Tx power is from -3dBm to 0dBm and at BLER 1% (about 100~450 meters) when device Tx power is from -3dBm to 5dBm. For cell edge data rate around 5~7 kbps, For UMa NLOS pathloss model, penetration margin 0 dB Device 2b: the achievable maximum distance can be smaller or larger than 500 meters at BLER 10% (about 100~680 meters) when device Tx power is -10dBm. The achievable maximum distance is smaller than 500 meters at BLER 10% (about 60~270 meters) when device Tx power is -20dBm and at BLER 1% (about 40~390 meters) when device Tx power is from -20dBm to -10dBm Device C: the achievable maximum distance can be smaller or larger than 500 meters at BLER 10% (about 300~1220 meters) and at BLER 1% (about 240~960 meters) when device Tx power is from -3dBm to 5dBm For UMa NLOS pathloss model, penetration margin 20 dB Device 2b: the achievable maximum distance is smaller than 500 meters at BLER 10% (about 20~150 meters) and at BLER 1% (10~120 meters) when device Tx power is from -20dBm to -10dBm Device C: the achievable maximum distance is smaller than 500 meters at BLER 10% (about 90~380 meters) and at BLER 1% (70~300 meters) when device Tx power is from -3dBm to 5dBm ------ End of TP ------ |
| --- |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.8.1-a003`

### [6G/Rel-20 RAN1#124] `agreement` 10.8.1 Evaluations

```text
For Rel-20 study, RAN1 has identified the followings
Device C achieves better coverage than Device 2b for both R2D and D2R
Device 2b is applicable to outdoor scenarios for short distance e.g. 50-200m
Device C is applicable to outdoor scenarios for both short and large distance e.g. 50-500m
Note: Necessity of Device 2b and C in terms of aspects other than coverage is up to RAN decision
R1-2600464	FL summary #3 for Ambient IoT: “9.3.1 Evaluations”	Moderator (Huawei)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.8.1-a004`

### [6G/Rel-20 RAN1#124] `agreement` 10.8.1 Evaluations

```text
RAN1 observes 5 dBm as the maximum transmit power for Device C to achieve maximum coverage in outdoor scenarios.
Values between -3dBm and 5dBm are feasible to achieve different coverage.
This does not preclude RAN to select any value(s) between -3 dBm and 5 dBm as maximum transmit power for Device C.
Final summary in R1-2601637.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-10.8.1-a005`

## 5G-A 历史事件

<details><summary>展开（原文，无中文摘要）</summary>

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
The definition on time stamp from existing specifications, e.g., TS 38.455, TS 38.355, TS 37.355 are reused as baseline.
No more discussion on time stamp is expected from RAN1 study perspective.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a001`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
From RAN1 perspective, the measurement of Level D reported from RAN is per gNB.
Note: RAN1’s understanding is that gNB can associate with one or multiple TRPs.
R1-2601381	Summary #2 on evaluations for NR ISAC	Moderator (Xiaomi)
From Tuesday session
R1-2601594	TP on Reference_6.2_6.3.0_6.3.1_AnnexB in TR 38.765	Moderator (Xiaomi)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a002`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
The Text Proposal to TR 38.765 in R1-2601594 is endorsed.
R1-2601595	TP on 6.3.2 in TR 38.765	Moderator (Xiaomi)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a003`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
The Text Proposal to TR 38.765 in R1-2601595 is endorsed.
R1-2601596	TP on 6.3.3 in TR 38.765	Moderator (Xiaomi)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a004`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
The Text Proposal to TR 38.765 in R1-2601596 is endorsed
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a005`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
From RAN1 perspective, on measurement quantization of Level C/D for position/velocity measurement, quantization methods in existing specifications, e.g., TS 23.032, TS 38.455, TS 38.355, TS 37.355 can be considered.
From RAN1 perspective, on measurement quantization of Level C for delay/angle measurement, quantization methods in existing specifications, e.g., TS 38.133 can be considered.
For Doppler measurement, same number of quantized bits as radial velocity can be considered.
Note: above does not take into account the potential impact from measurement quantization on the sensing performance.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a006`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
The velocity measurement of Option C1/C3/C4 is radial velocity.
R1-2601382	Summary #3 on evaluations for NR ISAC	Moderator (Xiaomi)
From Wednesday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a007`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
The following Text Proposal to Conclusion section in TR 38.765 is endorsed.
| The performance for UAV sensing use case with gNB monostatic sensing is evaluated based on the evaluation assumptions in Annex A (including UMa-AV, Sensing Tx/Rx operating simultaneously, FR1), with detailed assumptions and modelling reported by the companies as captured in Annex B. Among all the reported evaluation results as captured in Annex B, Baseline 1 (high BS TX power 52dBm with 80dB antenna isolation) By utilizing measurements from multiple or all TRPs, results from 9/10 sources achieve the performance objectives. By utilizing measurements from single TRP, results from 3/11 sources achieve the performance objectives. Baseline 2 (low BS TX power 37dBm with 65dB antenna isolation) By utilizing measurements from multiple or all TRPs, results from 7/9 sources achieve the performance objectives. By utilizing measurements from single TRP, results from 2/9 sources achieve the performance objectives |
| --- |
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a008`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
The velocity measurement of Option D1/D4 is 3D velocity, optional radial velocity.
Note: in the deployment where 3D velocity cannot be reported, Level D should not be reported.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a009`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
The velocity measurement of Option C2/C5 is radial velocity.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a010`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
Confirm the definition of measurement Level B by removing the square brackets
Level B: Amplitude and phase profile of delay, and/or Doppler, and/or angle per TRP for a given time stamp by using window(s) of the [consecutive] samples in at least one profile of delay, and/or Doppler and/or angle domain
R1-2601383	Summary #4 on evaluations for NR ISAC	Moderator (Xiaomi)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a011`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
From RAN1 perspective, the following methods can be considered to define the quantization for the measurements of Level A/B,
e.g., floating point, uniform scalar, non-uniform scalar
other quantization method is not precluded.
Note: above doesn’t take into account the potential impact from the measurement quantization on sensing performance.
Note: No more discussion on measurement quantization on Level A/B is expected in the study item from RAN1 perspective.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a012`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
From RAN1 perspective, the metric related to power can be considered for Level C measurement report.
From RAN1 perspective, the metric related to power (if applicable) can be considered for Level D measurement report.
Note: metric related to power may be different from those defined for communication and between Level C and Level D.
From RAN1 perspective, confidence metrics for the measurements can be considered for Level C/D measurement report.
No more discussion on the metric related to power and confidence metrics is expected in the study item from RAN1 study perspective.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a013`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
For Level C, at least the following examples of assistance information are identified as needed to assist the further processing at Sensing Function. The assistance information may or may not be provided by RAN.
Location of TRP if at least delay/range, Doppler/radial velocity or angle is reported.
If a measurement is reported in LCS, LCS to GCS transformation information.
For level D, if radial velocity is not reported, no assistance information is identified from RAN1 perspective.
No more discussion on the assistance information on Level C/D from RAN to SF is expected in the study item from RAN1 perspective.
R1-2601384	Summary #5 on evaluations for NR ISAC	Moderator (Xiaomi)
From Thursday session
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a014`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
From RAN1 perspective, on measurement quantization of Level C/D for confidence metric, the existing specifications, e.g., TS 23.032, TS 38.455, TS 38.355, TS 37.355 can be considered.
Note: above does not take into account the potential impact from measurement quantization on the sensing performance.
Note: No more discussion on measurement quantization on Level C/D for the metric related to power and confidence metric is expected in the study item from RAN1 perspective
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a015`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
For Level A/B, at least the following examples of assistance information are identified as needed to assist the further processing at Sensing Function. The assistance information may or may not be provided by RAN.
Level A
Location of TRP
Step size in delay domain if samples in delay domain is reported
Time information related to OFDM symbols used for measurement
Antenna configuration and/or beam information
Level B
Location of TRP
LCS to GCS transformation information
Information related to sampling of delay, doppler and/or angle profile
Additional assistance information is not precluded
No more discussion on the assistance information on Level A/B from RAN to SF is expected in the study item from RAN1 perspective
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a016`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
The payload size estimation of each measurement level/option for NR ISAC can be done by the following formulas
Level A: Msubcarrier* Ncpi *Mtxport*Nrxport*Ntrp*(Nquan1+ Nquan2)
Where,
Msubcarrier: number of subcarriers in a OFDM symbols
Ncpi: number of OFDM symbols within CPI
Mtxport: number of reference signal antenna port for sensing purpose
Nrxport: number of Rx antenna ports
Ntrp: number of TRPs for payload size calculation
Nquan1: number of quantized bits for amplitude
Nquan2: number of quantized bits for angle
Level B:
Delay-Doppler Profile: Mdelay *Ndoppler *Mtxport* Nrxport *Ntrp *(Nquan1+ Nquan2)
Delay-angle Profile: Mdelay * Ncpi *Mtxport*Nangle *Ntrp *(Nquan1+ Nquan2)
Delay-Doppler-angle Profile: Mdelay *Ndoppler *Mtxport*Nangle *Ntrp *(Nquan1+ Nquan2)
Delay Profile: Mdelay *Ncpi*Mtxport*Nrxport *Ntrp *(Nquan1+ Nquan2)
Where,
Mdelay: number of delay samples in the window
Ndoppler: number of Doppler samples in the window
Nangle: number of angle samples in the window
Level C:
C1/C2/C3: Np1*Ntrp *
C4/C5: Np2*Ntrp *
Where,
Np1 is total number of paths
Np2 is total number of points
Nparam is 5 including e.g.,
C1/C3/C4: delay, Doppler, horizontal angle, vertical angle, power measurement
C2/C5: position (x, y, z), radial velocity, power measurement
Nquan,i: number of quantized bits
Ntrp: number of TRPs for payload size calculation
Level D:
Nobject*Ngnb * for options D1/2
Mpoints* Ngnb * for options D3/4
Where,
Nobject is total number of targets
Mpoints is total number of scattering points of all targets
Ngnb is fixed to 1
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a017`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
The following assumptions on the parameters can be used to estimate payload size of different Levels/Options of measurements for NR ISAC for calculation purpose
| Parameters | Assumptions | Relation to maximum payload calculation |
| --- | --- | --- |
| Nsubcarriers | 3276 for 100MHz, 30kHz SCS |  |
| Ncpi | Min 64, medium 160, max 320 symbols per CPI |  |
| Mtxport | 1, medium 4, max 9 | Note: value obtained based on evaluation assumptions |
| Nrxport | 64 |  |
| Ntrp | 3 |  |
| Ngnb | 1 |  |
| Nquan1, i.e., amplitude | Min 16, medium 16, max 32 |  |
| Nquan2, i.e., phase | Min 16, medium 16, max 32 |  |
|  | Min 16, medium 16, max 32 |  |
| Mdelay | Min 288 (CP length, UMa) Medium/max: 467 for 2*570m (UMa) Max: 1436 for 2*1732m (RMa) |  |
| Ndoppler | same as Ncpi |  |
| Nangle | B2/B3: 32, 360 | Note: value obtained based on evaluation assumptions Note: 32 assumes non-uniform sampling Note: 360 assumes uniform oversampling |
| Np | 30, 60, 120 | to calculate min/medium/max for Level-C Note: value obtained based on evaluation assumptions |
| Nobject for D1/D2 | 15 | Note: value obtained based on evaluation assumptions |
| Mpoints for D3/D4 | 20 | Note: value obtained based on evaluation assumptions |
For Level C
Nparam=5 parameters for measurements
For Level D
Nparam=7 parameters for measurements
for D2/D3/D4, one more parameter of target ID is assumed
Note: for B2/B3, minimum value and maximum value can be different between non-uniform sampling case and uniform oversampling case
Note: RAN1 does not require all the parameters to take the minimum values at the same time or the maximum values at the same time
Note: above does not take into account the potential impact from measurement quantization on the sensing performance.
Note: above does not take into account the potential impact of different Levels/Options on the sensing performance.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a018`

### [5G-A/Rel-19 RAN1#124] `agreement` 9.5.1 Evaluation assumptions and performance evaluation

```text
The following Text Proposal to Conclusion section in TR 38.765 is endorsed.
| The study in physical layer has identified a number of Levels/Options for measurement report as described in Clause 5. Different Levels/Options for measurement report are associated with different payload overhead, assistance information and other higher layer aspects. |
| --- |
R1-2601668	Updated evaluation results of NR ISAC	Moderator (Xiaomi)
R1-2601669	Updated evaluation details on NR ISAC reported by companies	Moderator (Xiaomi)
R1-2601385	Summary #6 on evaluations for NR ISAC	Moderator (Xiaomi)
R1-2601701	Summary #7 on evaluations for NR ISAC	Moderator (Xiaomi)
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-a019`

### [5G-A/Rel-19 RAN1#124] `conclusion` 9.5.1 Evaluation assumptions and performance evaluation

```text
From RAN1 perspective, the issue on ambiguity handling in delay/range, Doppler/radial velocity, angle, position and 3D velocity measurements is identified, but not further discussed in Rel-20 NR ISAC.
Note: it does not prevent further discussion in future.
Note: this issue may or may not be addressed by NW implementation.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-c001`

### [5G-A/Rel-19 RAN1#124] `conclusion` 9.5.1 Evaluation assumptions and performance evaluation

```text
No further discussion on the assistance information from SF to RAN is expected in Rel-20 NR ISAC from RAN1 study perspective.
```
[原文出处](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/) · `RAN1-124-9.5.1-c002`

</details>

