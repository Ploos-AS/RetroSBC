# RP2354B management power capture manifest

This manifest is the machine-readable handoff for the first electrical capture block.

## U_MGMT power mapping

| Pad | Function | Net |
|---:|---|---|
| 5 | IOVDD | MGMT_3V3 |
| 10 | DVDD | MGMT_1V1 |
| 15 | IOVDD | MGMT_3V3 |
| 24 | IOVDD | MGMT_3V3 |
| 29 | IOVDD | MGMT_3V3 |
| 32 | DVDD | MGMT_1V1 |
| 41 | IOVDD | MGMT_3V3 |
| 50 | IOVDD | MGMT_3V3 |
| 51 | DVDD | MGMT_1V1 |
| 59 | ADC_AVDD | MGMT_3V3 |
| 60 | IOVDD | MGMT_3V3 |
| 61 | VREG_AVDD | VREG_AVDD |
| 62 | VREG_PGND | GND |
| 63 | VREG_VIN | MGMT_3V3 |
| 64 | VREG_LX | VREG_LX |
| 65 | VREG_FB | MGMT_1V1 |
| 68 | USB_OTP_VDD | MGMT_3V3 |
| 69 | QSPI_IOVDD | MGMT_3V3 |
| 76 | IOVDD | MGMT_3V3 |
| EP | GND | GND |

## Power block — official reference locked

The on-chip switching regulator is used for Rev A. The values/topology below are locked to the current Raspberry Pi RP2350 hardware-design guide and datasheet application circuit:

- `L_MGMT_CORE` = **3.3 uH**, from VREG_LX to the filtered `MGMT_1V1` rail.
- `VREG_FB` senses `MGMT_1V1` directly; no invented resistor divider is used.
- `C_MGMT_VREG_IN` = **4.7 uF** from the VREG input / MGMT_3V3 side to GND, placed for the switching-current loop.
- `C_MGMT_VREG_OUT` = **4.7 uF** from MGMT_1V1 to GND.
- `R_MGMT_VREG_AVDD` = **33 ohm** feeding VREG_AVDD from MGMT_3V3.
- `C_MGMT_VREG_AVDD` = **4.7 uF** from VREG_AVDD to GND.
- `MGMT_1V1` feeds DVDD pads 10/32/51.
- `MGMT_3V3` feeds the remaining 3.3 V supply-domain pads.
- VREG_PGND and EP connect to GND with regulator switching-current layout kept local to PGND.
- Local bypassing normally uses **100 nF per power pin**; the official reference guide documents layout-driven exceptions and a **4.7 uF** core-rail decoupling capacitor.

Authoritative sources:
- Raspberry Pi, *Hardware design with RP2350*, Chapter 2 (Power), especially the regulator application schematic and decoupling guidance.
- Raspberry Pi, *RP2350 Datasheet*, section 6.3 core voltage regulator/application circuit.

RP2354B is the QFN-80 RP235x variant with stacked flash; the regulator guidance applies to the RP235x family. Package-pad mapping remains controlled separately by the validated QFN-80 binding data.

## Recovery

- Pad 35 RUN -> MGMT_RUN.
- Pad 33 SWCLK -> SWCLK.
- Pad 34 SWDIO -> SWDIO.

## Capture gate

The regulator value/topology source gate is now closed. This manifest is still not ERC PASS: the next KiCad capture must instantiate the electrical components and wiring, then run ERC, netlist/package-binding and visual checks. Component MPN/footprint selection remains a separate BOM/DFM qualification gate.
