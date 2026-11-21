# BOUNCE Deep-Dive Plan

**Document date:** November 20, 2026

**Scope:** A phased, non-certified research plan for using BOUNCE concepts alongside existing aviation systems
**Status:** Proposal and feasibility plan—not an implementation commitment or certification claim

## 1. Purpose

This document explains what BOUNCE does today and defines a feasible path for evaluating it as a supplemental data source for authorized aviation-related organizations.

The plan is responsive to a future policy concept described in the Nov. 18, 2026 Bastille Post report, [“Congress agrees on civilian plane-locator mandate after deadly American Airlines Black Hawk crash”](https://www.bastillepost.com/global/article/6370635-congress-agrees-on-civilian-plane-locator-mandate-after-deadly-american-airlines-black-hawk-crash). The report indicates congressional agreement but also says that provisions still need resolution and legislation passage. This plan therefore treats the proposal as an unfinalized policy context, not as enacted law.

No language in this plan should imply that a phone or BOUNCE becomes:

- an ADS-B Out broadcaster,
- an ADS-B In receiver,
- a transponder,
- an alternate means of compliance,
- a certified surveillance source,
- or a collision-avoidance system.

The FAA [Equip ADS-B](https://www.faa.gov/air_traffic/technology/equipadsb) reference describes ADS-B Out as broadcasting aircraft position and ADS-B In as providing aircraft and pilots with situational-awareness information.

## 2. Documented current state

The detailed BOUNCE articles and forensic histories document an Android WebView application using Java and JavaScript/Three.js.

### 2.1 Documented Android capabilities

- `MainActivity` receives GPS and sensor data.
- `WebView.addJavascriptInterface` creates a bidirectional Java/JavaScript bridge.
- Java sends Wi-Fi, BLE, GPS, orientation, broadcast, trail, and algorithm updates to HTML.
- JavaScript sends camera, fleet, vehicle, broadcast, and user-control requests back to Android.
- Android requests runtime permissions for location and radio access.
- A wake lock can support trail recording while the screen is off.

### 2.2 Documented visualization capabilities

- Three.js scene, reference grid, vehicle avatar, and beacon objects
- Orbit, fly-through, and chase-point-of-view camera modes
- GPS trail recording and 2000-point FIFO smoothing
- Wi-Fi node fields, BLE spatial objects, labels, and trails
- Fleet and vehicle mode controls

### 2.3 Documented positioning and radio concepts

- Wi-Fi RSSI and BLE RSSI zone/distance calculations
- RSSI Kalman filtering
- Trilateration and weighted least-squares concepts
- EKF and particle-filter concepts
- HMM zone classification
- Sensor-fusion orientation
- Wi-Fi RTT, UWB, or AP self-calibration as roadmap concepts where not already implemented

The project also documents Wi-Fi Direct and 4-slot SSID broadcast behavior. These mechanisms are separate from aviation ADS-B and are not evidence of standards-compliant aircraft surveillance.

### 2.4 Evidence status

The repository records historical versions and forensic analysis, but the documents contain claimed performance figures and intended behavior. Individual claims should not be treated as independent verification. Accuracy, battery use, latency, scan availability, background behavior, compatibility, and safety must be measured on representative hardware and software.

## 3. Boundaries and use cases

### 3.1 Personal phone—Option B

Only a participant who voluntarily opts in may share their own device or vehicle position. The participant must be able to view, pause, and revoke sharing. The service should support organization-approved apps or managed devices and should not scan, identify, or track unrelated passenger devices.

Potential uses:

- research on authorized low-speed or ground-movement telemetry,
- controlled airport events with enrolled participants,
- user-initiated emergency or assistance workflows approved by the responsible organization.

Phones must not be assumed to have reliable aviation accuracy or continuity. In particular, an airborne phone may lose view of GNSS, have poor time or sensor quality, or be used outside its defined scope.

### 3.2 Airport or taxi vehicles—Option C

This is the stronger near-term concept. An airport, taxi fleet, or ground-operator could authorize and issue devices to known vehicles. It would control:

- device identity and enrollment,
- driver or operator acknowledgment,
- maintenance and calibration,
- data retention,
- approved operational display,
- and revocation.

Authorized vehicle telemetry could be fused with existing airport systems, ADS-B services, ground radar or surface surveillance, fleet dispatch, and video or other approved sources. This data may support operational awareness or dispatch planning, but it should not be used as the sole source for movement control or separation decisions.

### 3.3 Future broadcasting assets

A later phase might integrate compatible broadcasts from authorized airport assets, land vehicles, vessels, or aircraft systems. This vision is standards-driven and requires:

- a compatible broadcast or service,
- a deployed receive and relay network,
- enough coverage and availability,
- a data contract and time source,
- secure identity,
- legal authority,
- accountable ownership,
- and methods to detect stale or falsified tracks.

Broad statements about “all vessels” are not technically achievable without these dependencies. Land and maritime data may require separate standards, authorities, interfaces, and safety cases.

## 4. Architectural proposal

```text
Participant or managed device
    |  explicit opt-in / managed enrollment
    v
BOUNCE capture and local validation
    |  GNSS, sensors, radio observations, timestamps
    v
Authenticated participant gateway
    |  transport encryption, identity, policy checks
    v
Data quality and correlation service
    |  timestamp, accuracy, freshness, duplicate/spoof checks
    v
Operator situational-awareness display
    |
    +--> existing ADS-B / certified aviation systems
    +--> airport or fleet tracking systems
    +--> audit, retention, and incident workflows
```

### 4.1 Core components

1. **Capture module:** GPS, sensors, and radio observations with source quality and timestamps.
2. **Local safety and privacy module:** consent state, sharing state, sensitive-field minimization, and fail-safe controls.
3. **Authenticated gateway:** organization-issued identities and transport security.
4. **Quality service:** reject stale, impossible, duplicate, or low-confidence observations.
5. **Correlation service:** fuse only when source identities and reference frames are trustworthy.
6. **Visualization:** Three.js or an operator-approved interface that clearly labels source, confidence, freshness, and limitations.
7. **Audit service:** immutable operational events, access controls, and incident investigation.

### 4.2 Information model

Each report should carry:

- a stable but appropriately scoped participant or asset ID,
- source type,
- latitude/longitude or a reference frame,
- altitude only when available and defined,
- uncertainty,
- timestamp and received time,
- heading and speed only when defined,
- provenance,
- consent or authorization state,
- and a validity or expiration window.

Raw IDs and personal identifiers should be minimized or separated from operational data. No endpoint or display should infer a person's identity from nearby Wi-Fi or BLE observations.

### 4.3 ADS-B integration

ADS-B feeds or certified operator systems should remain separate, authoritative sources. An integration should preserve source provenance and avoid merging a phone estimate into an ADS-B aircraft position as if it were identical.

The display could show:

- a certified track,
- a supplemental track,
- track correlation confidence,
- source freshness,
- and the distinction in labels and symbols.

Human operators must not interpret a phone-derived estimate as a certified aircraft position.

## 5. Phased implementation

### Phase 0: scope, governance, and baseline

**Work**

- appoint an accountable aviation/airport sponsor,
- define the exact non-safety use case,
- identify applicable laws and authorities,
- establish threat and privacy models,
- inventory current BOUNCE behavior,
- freeze a software baseline,
- select representative Android devices.

**Exit criteria**

- written use-case and anti-abuse rules,
- privacy and legal sign-off,
- data dictionary,
- system boundary,
- and independent reviewers named.

**No-go trigger:** no approved organization, no authority, or an intent to track arbitrary phones.

### Phase 1: offline and simulator demonstration

**Work**

- build recorded and synthetic data fixtures,
- test the WebView/Three.js display,
- verify trail rendering, source labels, stale-data handling, and failover,
- unit-test positioning algorithms,
- compare documented behavior with actual device measurements.

**Exit criteria**

- reproducible test scenarios,
- documented accuracy and limitations,
- no unrequested personal-data collection,
- audit and source provenance demonstrated,
- independent code review complete.

**No-go trigger:** the demo cannot distinguish supplemental tracks from certified tracks.

### Phase 2: controlled organizational vehicle pilot

**Work**

- enroll airport-owned or authorized fleet vehicles,
- deploy managed devices with cryptographic identities,
- collect telemetry only inside the approved route and operating area,
- run the gateway and quality service,
- display alongside, but clearly separate from, existing approved systems.

**Exit criteria**

- stable identity and revocation,
- demonstrated accuracy against survey or approved reference data,
- latency and availability metrics,
- incident response and maintenance processes,
- operator human-factors evaluation,
- no adverse operational conclusion based solely on BOUNCE.

**No-go trigger:** accuracy or authorization does not meet agreed pilot requirements.

### Phase 3: limited voluntary personal participation

**Work**

- permit explicit participant opt-in,
- expose sharing controls and retention,
- test on a narrowly approved research use case,
- provide clear consent language and stop controls,
- conduct privacy and security testing,
- restrict collection to the participating user's own device and vehicle.

**Exit criteria**

- successful consent and revocation tests,
- minimal data collection,
- secure identity separation,
- abuse and deletion procedures,
- legal and privacy approval,
- no arbitrary nearby-device identification.

**No-go trigger:** required consent or data minimization cannot be enforced.

### Phase 4: standards and authority integration

**Work**

- engage FAA, airport, fleet, and standards stakeholders,
- assess ADS-B and existing surveillance interfaces,
- conduct interoperability testing,
- define coverage, availability, and continuity requirements,
- evaluate whether land and maritime sources have relevant standards.

**Exit criteria**

- approved interface and test standard,
- formal data-quality and failure requirements,
- regulatory and spectrum/operating authority,
- independently verified safety case if safety use is proposed.

**No-go trigger:** a requirement depends on certification or authority that is unavailable.

### Phase 5: operational evaluation

**Work**

- conduct authorized, supervised field evaluation,
- monitor false, stale, duplicated, or missing tracks,
- execute degraded-mode and emergency stop tests,
- maintain fallback to certified systems,
- publish de-identified results and limitations.

**Exit criteria**

- measurable improvement to the approved use case,
- no unsafe reliance on supplemental data,
- operator training complete,
- lifecycle and incident ownership established.

Operational safety-critical adoption must receive the required certification or approval; this plan does not assume a fast track.

## 6. Safety and reliability

### 6.1 Required guarantees

BOUNCE-derived tracks must:

- include source, age, and uncertainty,
- fail visibly instead of silently,
- be excluded or downgraded when stale,
- be isolated from certified systems,
- support emergency disable,
- preserve fallback operations,
- and have a documented maintenance and update process.

### 6.2 Test categories

- GNSS loss or jump,
- phone OS position spoofing,
- radio noise and multipath,
- clock drift,
- network loss,
- replay and duplicate reports,
- device restart,
- permission revocation,
- tampering,
- denial of service,
- battery exhaustion,
- app crash,
- stale track on WebView display,
- conflict between sources,
- and operator misinterpretation.

### 6.3 Performance measures

At minimum, report:

- horizontal and vertical uncertainty,
- 95th-percentile update latency,
- stale-track rate,
- availability,
- false track rate,
- missed track rate,
- correlation error,
- battery cost,
- device compatibility,
- and degradation under RF and network stress.

No performance threshold should be copied from the project roadmap until it is independently measured.

## 7. Privacy and participant rights

The system must not provide a mechanism for covertly collecting or identifying:

- arbitrary passengers,
- unrelated pedestrians,
- nearby household or business devices,
- or any person who has not authorized sharing.

Required controls:

- explicit consent,
- purpose limitation,
- data minimization,
- short and defined retention,
- deletion and export paths,
- audit of access,
- tenant or organization separation,
- pseudonymous IDs,
- local sharing controls,
- and a visible indicator whenever collection or upload is active.

Airport or fleet participants should receive a device and role policy; personal users should receive a separate, plain-language privacy policy.

## 8. Security

Security requirements include:

- signed application builds,
- package integrity,
- secure storage for credentials,
- mutual or gateway-authenticated transport,
- certificate and key rotation,
- device enrollment and revocation,
- replay protection,
- server-side authorization,
- RBAC and least privilege,
- signed audit events,
- anomaly detection,
- rate limits,
- secure Android updates,
- and secure lifecycle and decommissioning.

Wi-Fi/BLE scanning permissions create additional privacy and abuse risk. The implementation should collect only necessary observations, avoid persistent identifiers where possible, and never infer or track arbitrary people.

## 9. Regulatory and interoperability plan

Before operational use, stakeholders must determine:

- whether the system is merely advisory or could influence decisions,
- which authority and rule set applies,
- whether any FCC, FAA, DOT, DOT/USCG, airport, or local obligations apply,
- which spectrum or transmission technologies are permitted,
- whether ADS-B or other aviation standards are involved,
- whether the data is sufficient for the stated use,
- and what assurance, testing, and certification is required.

ADS-B In and Out are aviation-specific functions. BOUNCE does not become ADS-B compliant by receiving or visualizing an approved third-party feed.

Interoperability work should prefer documented, standards-based interfaces and well-defined schemas. Proprietary SSIDs or direct device identifiers are not suitable as a universal air-ground or maritime standard.

## 10. Verification and stage gates

No phase advances without evidence in a test report.

| Gate | Required evidence | Decision |
|---|---|---|
| G0 Governance | Sponsor, authority, scope, privacy and security boundaries | Proceed or stop |
| G1 Software | Reproducible tests and code baseline | Proceed or stop |
| G2 Data quality | Independent accuracy and freshness measurements | Proceed or stop |
| G3 Fleet pilot | Authorized vehicles, audit, degraded-mode tests | Extend or stop |
| G4 Phone pilot | Consent, minimization, revocation, abuse review | Extend or stop |
| G5 Interoperability | Standards and authority approvals | Proceed or stop |
| G6 Operational evaluation | Independent validation, no unsafe sole-source reliance | Limited approval or stop |

## 11. Cost and dependency questions

Before implementation, sponsors should estimate:

- Android and device support matrix,
- airport or fleet integration effort,
- networking and coverage,
- identity and key lifecycle,
- privacy engineering,
- independent test and safety work,
- operator training,
- maintenance and updates,
- ADS-B or other approved feed licensing,
- and legal authority.

The project must avoid assuming that phone availability is free coverage. Cellular connectivity, GNSS, power, OS restrictions, hardware variation, and background behavior create operational gaps.

## 12. Long-term land, air, and sea vision

Land and maritime integration should remain a future standards effort:

- land assets may include authorized fleets, rail, or infrastructure;
- air assets must use approved aviation data sources and systems;
- sea assets require maritime broadcast, receive, and authority frameworks;
- every source needs compatible identity, format, coverage, quality, and time systems.

BOUNCE could provide a configurable visualization or experimental correlation layer, but it cannot itself make heterogeneous assets observable or interoperable.

## 13. Sources

### Primary project sources

- [Landolil/toys BOUNCE hosted repository and APKs](https://github.com/landolil/toys/tree/main/AppsGames/ANDROID/BOUNCE)
- [PrimeCarrPod/Seed BOUNCE root_articles](https://github.com/PrimeCarrPod/Seed/tree/main/CSMApps/Bounce/root_articles)
- [Landolil/Seed BOUNCE mirror](https://github.com/landolil/seed/tree/main/CSMApps/Bounce)
- [Seed work-in-progress README](https://github.com/PrimeCarrPod/Seed/blob/main/CSMApps/Bounce/work-in-progress/README.md), [feature history](https://github.com/PrimeCarrPod/Seed/blob/main/CSMApps/Bounce/work-in-progress/features-history.md), and [feature roadmap](https://github.com/PrimeCarrPod/Seed/blob/main/CSMApps/Bounce/work-in-progress/features-roadmap.md)
- [BOUNCE evolution documents](https://github.com/PrimeCarrPod/Seed/tree/main/CSMApps/Bounce/work-in-progress/BOUNCE_EVOLUTION) (excluding the `pieces` folder)
- [`CSMApps/Bounce/README.md`](../README.md)
- [`CSMApps/Bounce/root_articles/A1-01_HTML_Aspects_ThreeJS_Visualization.md`](../root_articles/A1-01_HTML_Aspects_ThreeJS_Visualization.md)
- [`CSMApps/Bounce/root_articles/A2-02_Android_Main_Features_Radio_Positioning.md`](../root_articles/A2-02_Android_Main_Features_Radio_Positioning.md)
- [`CSMApps/Bounce/root_articles/A3-03_Connection_Pathways_Bidirectional.md`](../root_articles/A3-03_Connection_Pathways_Bidirectional.md)
- [`CSMApps/Bounce/root_articles/A7-07_Future_Progress_Roadmap_P0_P3.md`](../root_articles/A7-07_Future_Progress_Roadmap_P0_P3.md)
- [`CSMApps/Bounce/work-in-progress/BOUNCE_EVOLUTION/A9-09_Working_Features_Versions_History.md`](../work-in-progress/BOUNCE_EVOLUTION/A9-09_Working_Features_Versions_History.md)

### External references

- [FAA Equip ADS-B](https://www.faa.gov/air_traffic/technology/equipadsb)
- [Bastille Post, Nov. 18, 2026, “Congress agrees on civilian plane locator mandate after deadly American Airlines Black Hawk crash”](https://www.bastillepost.com/global/article/6370635-congress-agrees-on-civilian-plane-locator-mandate-after-deadly-american-airlines-black-hawk-crash)
