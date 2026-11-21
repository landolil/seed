# Subject: A supplemental, opt-in role for BOUNCE in aviation and airport situational awareness

Hello,

BOUNCE is an Android-based visualization and radio-positioning project that combines GPS, Wi-Fi, Bluetooth Low Energy (BLE), sensors, and an Android WebView/Three.js interface. It can display device or vehicle position, movement trails, nearby radio environments, and 3D spatial views. The hosted source and APKs are available at [the Landolil/toys BOUNCE repository](https://github.com/landolil/toys/tree/main/AppsGames/ANDROID/BOUNCE), and the detailed design articles are maintained in [the PrimeCarrPod/Seed BOUNCE root_articles](https://github.com/PrimeCarrPod/Seed/tree/main/CSMApps/Bounce/root_articles).

The FAA [Equip ADS-B](https://www.faa.gov/air_traffic/technology/equipadsb) reference explains the difference clearly: ADS-B Out broadcasts an aircraft's position and other information, while ADS-B In provides aircraft and pilots with situational-awareness data. BOUNCE should not be described as an ADS-B transponder, ADS-B In receiver, certified collision-avoidance system, or replacement for existing FAA equipment.

A Nov. 18, 2026 Bastille Post report, [“Congress agrees on civilian plane locator mandate after deadly American Airlines Black Hawk crash”](https://www.bastillepost.com/global/article/6370635-congress-agrees-on-civilian-plane-locator-mandate-after-deadly-american-airlines-black-hawk-crash), says Sens. Ted Cruz and Maria Cantwell announced an agreement on civilian aircraft locator provisions. The report also says some provisions still need resolution and legislation passage, so this should not be described as enacted law.

In a standards-driven pilot, BOUNCE could be considered an additional data layer:

- **Option B — personal cell phones:** only for voluntary, opt-in participants who choose to broadcast their own authorized device or vehicle position. Passenger phones should not be detected, identified, or tracked without consent.
- **Option C — digital taxi and airport vehicles:** authorized vehicles could share managed telemetry with an airport or operating organization, alongside certified aviation equipment and existing ADS-B services.
- **Future broadcasting assets:** compatible ground vehicles and vessels could contribute authorized position reports, subject to standards, spectrum, coverage, cybersecurity, and legal authority.

The near-term goal is not “locating every plane or vehicle by phone.” It is to test whether a limited, governed, independently verified supplement could improve local situational awareness during a controlled exercise. BOUNCE's current cell-GPS and radio features can support a proof of concept, but documented values and roadmaps are not proof of operational accuracy or safety.

A phased plan would start with desktop and simulator validation, then an organizationally authorized airport-vehicle pilot, and only later consider approved participant phones or integrations with ADS-B feeds. Safety-critical use would require formal aviation review, independent verification, standards and regulatory approval, and a clear separation from certified systems.

Thank you for considering this as a possible complementary research and development concept.

Sincerely,

[Sender name]

---

## Sources reviewed

- [BOUNCE hosted repository and APKs](https://github.com/landolil/toys/tree/main/AppsGames/ANDROID/BOUNCE)
- [Detailed Seed root_articles source](https://github.com/PrimeCarrPod/Seed/tree/main/CSMApps/Bounce/root_articles)
- [Landolil/Seed BOUNCE mirror](https://github.com/landolil/seed/tree/main/CSMApps/Bounce)
- [Seed work-in-progress history](https://github.com/PrimeCarrPod/Seed/blob/main/CSMApps/Bounce/work-in-progress/features-history.md) and [roadmap](https://github.com/PrimeCarrPod/Seed/blob/main/CSMApps/Bounce/work-in-progress/features-roadmap.md)
- [BOUNCE evolution documents](https://github.com/PrimeCarrPod/Seed/tree/main/CSMApps/Bounce/work-in-progress/BOUNCE_EVOLUTION) (excluding the `pieces` folder)
- [`CSMApps/Bounce/README.md`](../README.md)
- [`CSMApps/Bounce/root_articles/A1-01_HTML_Aspects_ThreeJS_Visualization.md`](../root_articles/A1-01_HTML_Aspects_ThreeJS_Visualization.md)
- [`CSMApps/Bounce/root_articles/A2-02_Android_Main_Features_Radio_Positioning.md`](../root_articles/A2-02_Android_Main_Features_Radio_Positioning.md)
- [`CSMApps/Bounce/root_articles/A3-03_Connection_Pathways_Bidirectional.md`](../root_articles/A3-03_Connection_Pathways_Bidirectional.md)
- [`CSMApps/Bounce/root_articles/A7-07_Future_Progress_Roadmap_P0_P3.md`](../root_articles/A7-07_Future_Progress_Roadmap_P0_P3.md)
- FAA: [Equip ADS-B](https://www.faa.gov/air_traffic/technology/equipadsb)
- Bastille Post, Nov. 18, 2026: [Congressional plane-locator mandate report](https://www.bastillepost.com/global/article/6370635-congress-agrees-on-civilian-plane-locator-mandate-after-deadly-american-airlines-black-hawk-crash)
