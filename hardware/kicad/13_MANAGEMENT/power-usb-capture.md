# M3.7 — RP2354B power and service-USB capture block

Status: **electrical capture specification — implementation-ready, final symbol/package verification required**

This is the first detailed electrical sub-block for `13_MANAGEMENT`.

## MCU power block

Capture the RP2354B exactly per the current authoritative RP2350/RP2354 hardware-design guidance and QFN-80 package table.

Required implementation:
- all RP2354B supply pins connected to their specified rails;
- all grounds connected to the uninterrupted local ground reference;
- 100 nF local ceramic decoupling at each required supply group/pin vicinity;
- local bulk capacitance on MGMT_3V3;
- any required internal-regulator support capacitor(s) exactly as specified by the vendor;
- RUN/reset passive default and accessible reset point;
- SWD remains accessible;
- integrated-flash-specific supply requirements included.

**Do not infer RP2354B power pins from RP2350A/Pico schematics.**

## MGMT_3V3

The management rail is `MGMT_3V3`.

Add:
- 10 µF-class local bulk footprint;
- labelled test point `TP_MGMT_3V3`;
- local decoupling network;
- optional 0 Ω/current-measurement link or shunt footprint between source and management load if it does not compromise regulation.

The source regulator/load switch remains part of the board power-tree design and is not invented here.

## Service USB-C

The management service port is USB 2.0 device/UFP only.

Logical nets:
- `MGMT_USB_DP`
- `MGMT_USB_DM`
- `SERVICE_VBUS`
- `USB_CC1`
- `USB_CC2`
- `GND`
- connector shield net/chassis strategy TBD at board EMC review.

### CC

Populate:
- CC1 -> 5.1 kΩ 1% -> GND
- CC2 -> 5.1 kΩ 1% -> GND

These advertise a USB-C sink/device role. RetroSBC management must not advertise source/host power from this connector.

### D+/D-

For a USB-C receptacle:
- tie the duplicated receptacle D+ contacts into `MGMT_USB_DP` as required by the connector pinout;
- tie duplicated D- contacts into `MGMT_USB_DM`;
- route D+/D- as a short matched USB2 differential pair;
- place low-capacitance ESD protection adjacent to the connector;
- fit 27 Ω series termination on both USB D+ and D- as required by the RP2350 hardware design guidance;\n- place both 27 Ω resistors close to the RP2354B USB pins.

Do not add arbitrary capacitance to D+/D-.

### VBUS

`SERVICE_VBUS` must be sensed/handled without back-powering MGMT_3V3 or main rails.

Rev-A schematic should support two population policies:
- **normal:** board powers RP2354B; service VBUS is sensed only;
- **service-only option:** VBUS may power only the isolated management service domain through reverse-current-protected power-path circuitry.

The service-only option remains DNI until its power path is qualified.

## Protection placement

Place USB ESD protection physically close to J_SERVICE. Keep the ESD return path short and direct.

CC resistors should be near the connector. Power-path protection should be placed so connector VBUS cannot bypass it.

## Named components

Use stable schematic references/functions:
- `U_MGMT` — RP2354B
- `J_SERVICE` — USB-C service
- `D_USB_ESD` — USB2 ESD array
- `R_CC1`, `R_CC2` — 5.1 kΩ
- `C_MGMT_BULK` — 10 µF class
- `TP_MGMT_3V3`
- `TP_MGMT_RESET`
- `J/TP_SWD`

Exact supplier MPNs remain controlled by `management-bom.csv`.

## Review gate

This sub-block is electrically reviewable when:
1. exact RP2354B QFN-80 power/pad mapping is cited and checked;
2. required regulator-support capacitors match current vendor guidance;
3. USB-C receptacle pinout is checked against selected connector;
4. CC1/CC2 each have independent 5.1 kΩ Rd;
5. USB ESD is present;
6. VBUS cannot back-power main rails;
7. D+/D- each have the required 27 Ω series termination close to the MCU, with no accidental stubs or inappropriate translator;
8. SWD/RUN recovery remains usable;
9. ERC passes or local exceptions are documented.

Only after those checks should this block be marked **CAPTURE PASS**.
