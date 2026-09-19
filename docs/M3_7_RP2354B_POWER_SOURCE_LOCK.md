# M3.7 — RP2354B power/reference-design source lock

Status: **authoritative source gate for schematic capture**

The RP2354B management circuit shall follow Raspberry Pi's current RP2350 hardware-design guidance and the official RP2350B Minimal KiCad design for the QFN-80 package.

## Authoritative sources

- RP2350 datasheet, current Product Information Portal release.
- *Hardware design with RP2350*, current Product Information Portal release.
- RP2350B Minimal KiCad, current Product Information Portal release.

The Product Information Portal showed the hardware-design guide updated 2026-08-24 and the RP2350B Minimal KiCad archive updated 2026-07-27 when this gate was created.

## RP2354B-specific rule

RP2354B is the QFN-80 B-package device with 48 GPIO and 2 MiB stacked flash. The official hardware guide states that the minimal RP2350B design can be used with RP2354B by omitting the external flash device (or retaining external flash only as an intentional secondary device).

RetroSBC Rev-A therefore uses the in-package 2 MiB flash as the default management firmware store. No external boot-flash IC is required in the baseline management design.

## Power implementation rule

RP235x does not reuse the RP2040 power circuit. It has an on-chip switching regulator and Raspberry Pi explicitly calls for the specified support circuitry and careful layout.

Therefore:
- do not invent inductor, capacitor, regulator-support or crystal values;
- use the current official reference BOM/layout as the source for the MCU power island;
- preserve the reference topology during schematic capture;
- deviations require a documented engineering reason and requalification;
- keep the management power island physically compact during PCB placement.

## Silicon stepping

Prefer A4-or-later qualified production silicon. Raspberry Pi states that A4 does not change the package pinout and that the hardware-design/reference component guidance remains applicable.

## Capture deliverables

Before the MCU block is marked CAPTURE PASS:
1. copy the required RP2350B reference power topology into the RetroSBC schematic using independently sourced symbols/footprints;
2. adapt flash population for RP2354B stacked flash;
3. record every reference-design component and value in the management BOM;
4. bind all supply, ground, regulator and exposed-pad pins;
5. capture RUN, SWD and dedicated USB;
6. run ERC;
7. review against the official Minimal B design side-by-side;
8. retain source revision/date in the qualification record.

This document is a source/control gate; it is not a substitute for the actual KiCad circuit.
