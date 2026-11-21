# BOUNCE: A Nontechnical Overview

**Document date:** November 20, 2026
**Purpose:** Explain what BOUNCE is, what it can demonstrate today, and how it might be considered alongside certified aviation services.

## Executive summary

BOUNCE is an Android application that combines phone sensors and radio information with a 3D on-screen view. It can show a user's or an authorized vehicle's GPS position, travel trail, orientation, Wi-Fi access points, and Bluetooth devices. It uses an Android WebView to connect Java-based phone features to a Three.js interface.

BOUNCE is an experimental situational-awareness and visualization project. It is **not** an ADS-B system, an aviation transponder, an ADS-B In receiver, a certified collision-avoidance system, or a substitute for approved FAA equipment.

The project could potentially serve as:

1. A **personal participant option** for people who voluntarily opt into sharing the position of their own phone or vehicle.
2. A **digital taxi or airport fleet option** for organizationally authorized vehicles that send managed telemetry.
3. A future interface for approved, compatible broadcasts from ground and, later, maritime or aeronautical assets.

These would be supplemental options, not replacements for existing certified equipment.

## What BOUNCE documents as current capabilities

The repository's detailed documentation describes the following implemented or historically documented features:

- An Android WebView bridge between Java and JavaScript
- A Three.js 3D scene with reference grids, vehicle markers, trails, and camera modes
- GPS latitude, longitude, altitude, heading, speed, and timestamp updates
- Wi-Fi scanning and RSSI/distance or zone indicators
- Bluetooth Low Energy scanning and spatial/trajectory displays
- Accelerometer, magnetometer, and gyroscope orientation
- Sensor filtering and described positioning algorithms, including Kalman, EKF, particle, HMM, trilateration, and sensor-fusion concepts
- A Wi-Fi Direct broadcast function and 4-slot SSID rotation
- Visual trails with a limited 2000-point history

These descriptions come from project articles and forensic histories of app versions; they are claims in repository documentation. They do **not** establish aviation-grade accuracy, reliability, cybersecurity, certification, or field performance.

The distributed BOUNCE project also includes APKs in the [Landolil/toys BOUNCE path](https://github.com/landolil/toys/tree/main/AppsGames/ANDROID/BOUNCE). Detailed source articles are in the [PrimeCarrPod/Seed BOUNCE root_articles](https://github.com/PrimeCarrPod/Seed/tree/main/CSMApps/Bounce/root_articles).

## What ADS-B means

The FAA [Equip ADS-B](https://www.faa.gov/air_traffic/technology/equipadsb) reference distinguishes between:

- **ADS-B Out:** broadcasts an aircraft's position and other information.
- **ADS-B In:** provides participating aircraft and pilots with situational-awareness information.

ADS-B use is part of a separate aviation equipment and service ecosystem. BOUNCE can potentially display position data supplied by an approved source, but it does not itself provide ADS-B Out or ADS-B In capability.

## The plane-locator policy context

A Nov. 18, 2026 [Bastille Post article](https://www.bastillepost.com/global/article/6370635-congress-agrees-on-civilian-plane-locator-mandate-after-deadly-american-airlines-black-hawk-crash) reports that Congress agreed on a civilian plane-locator mandate following the deadly American Airlines–Black Hawk crash. The report says that provisions still need resolution and that legislation must pass. Therefore, this proposal should not describe the reported agreement as enacted law or presume a final rule.

Within a future authorized policy, the senators named in the request—Sen. Ted Cruz and Sen. Maria Cantwell—could evaluate options for a broader civilian plane-locator requirement. BOUNCE could inform the analysis only as an exploratory data or user-interface concept. It should not be represented as an existing solution to the mandate.

## Options B and C

### Option B: voluntary personal cell-phone telemetry

The phone could send its own location if and only if the participant explicitly opts in, sees what is shared, chooses whether sharing is active, and can stop it. This is supplemental data for research or authorized applications.

It does not justify detecting or identifying nearby passenger phones, collecting location without consent, or inferring activity from arbitrary radio scans. Personal participation would require transparent permissions, retention limits, accountable operators, and protection against misuse.

### Option C: authorized airport and taxi vehicles

Digital taxi-cell phones or airport-owned devices could be issued to participating vehicles by an airport or fleet operator. The organization would have to define ownership, authorization, and control of each telemetry stream. Position data could complement certified ground-radar, ADS-B, airport equipment, and established fleet systems.

Airport vehicles and taxis are more suitable participants than arbitrary phones because they have:

- an accountable organization,
- a known vehicle asset,
- defined use and operating rules,
- opportunities for maintenance and calibration,
- and a managed security lifecycle.

## The broader broadcasting-assets vision

Future situational awareness might include:

- authorized airport and ground-fleet vehicles,
- vessels with compatible broadcast and receiver infrastructure,
- aircraft and their certified ADS-B or other approved systems,
- and approved land or sea assets participating in standards-based networks.

This “all vessels and vehicles” vision is not technically achievable simply by adding an app. It requires compatible broadcasts, deployed receivers, network coverage, participation, legal authority, secure identities, reliable time and position, and trustworthy data fusion. Ground and maritime integration would therefore come later, after relevant standards and operator requirements are established.

## Why a staged approach is necessary

The first goal should be to demonstrate software and operational value under controlled conditions. The next goal should be independent accuracy and safety verification. Only after a regulator or operator has approved a use case should the concept move toward operational trials.

Stage gates should cover:

- accuracy and latency,
- availability and failover,
- privacy and consent,
- cyber and radio security,
- interoperability,
- legal authority,
- human factors,
- and independent certification or approval where applicable.

Until those gates are passed, BOUNCE should be labeled as an experimental visualization and supplemental telemetry tool—not as an aviation safety service.

## Source links

- [BOUNCE hosted repository and APKs](https://github.com/landolil/toys/tree/main/AppsGames/ANDROID/BOUNCE)
- [Detailed BOUNCE source articles](https://github.com/PrimeCarrPod/Seed/tree/main/CSMApps/Bounce/root_articles)
- [FAA Equip ADS-B](https://www.faa.gov/air_traffic/technology/equipadsb)
- [Nov. 18, 2026 Bastille Post report](https://www.bastillepost.com/global/article/6370635-congress-agrees-on-civilian-plane-locator-mandate-after-deadly-american-airlines-black-hawk-crash)

Repository sources reviewed:

- [`CSMApps/Bounce/README.md`](../README.md)
- [`CSMApps/Bounce/root_articles/A1-01_HTML_Aspects_ThreeJS_Visualization.md`](../root_articles/A1-01_HTML_Aspects_ThreeJS_Visualization.md)
- [`CSMApps/Bounce/root_articles/A2-02_Android_Main_Features_Radio_Positioning.md`](../root_articles/A2-02_Android_Main_Features_Radio_Positioning.md)
- [`CSMApps/Bounce/root_articles/A3-03_Connection_Pathways_Bidirectional.md`](../root_articles/A3-03_Connection_Pathways_Bidirectional.md)
- [`CSMApps/Bounce/root_articles/A7-07_Future_Progress_Roadmap_P0_P3.md`](../root_articles/A7-07_Future_Progress_Roadmap_P0_P3.md)
- [`CSMApps/Bounce/work-in-progress/BOUNCE_EVOLUTION/A9-09_Working_Features_Versions_History.md`](../work-in-progress/BOUNCE_EVOLUTION/A9-09_Working_Features_Versions_History.md)
