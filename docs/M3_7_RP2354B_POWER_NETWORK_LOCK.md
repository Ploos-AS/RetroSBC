# M3.7 — RP2354B management power-network lock

Status: **authoritative electrical contract; schematic capture still pending**

This locks the RP2354B management MCU power topology before electrical KiCad wiring.

## Rails

- `MGMT_3V3`: IOVDD, USB_OTP_VDD, ADC_AVDD, QSPI_IOVDD and VREG_AVDD.
- `MGMT_1V1`: filtered internal-regulator output feeding DVDD.
- `GND`: normal ground reference.
- `VREG_PGND`: regulator power ground, tied externally to ground using the vendor reference topology.

The RP2350 datasheet defines IOVDD and QSPI_IOVDD as 1.8–3.3 V domains, USB_OTP_VDD/ADC_AVDD/VREG_AVDD as nominal 3.3 V, and DVDD as nominal 1.1 V.

## Internal regulator

Rev-A uses the RP2354B internal core regulator unless later qualification proves a reason not to.

- VREG_VIN is supplied from the qualified management input rail.
- VREG_LX drives the external inductor from the official reference topology.
- the filtered regulator output is `MGMT_1V1`;
- VREG_FB senses the filtered output;
- DVDD is supplied from `MGMT_1V1`;
- VREG_PGND returns to ground according to the reference layout.

Exact inductor/capacitor values and placement shall be copied from the current Raspberry Pi RP2350 hardware-design reference/Minimal B design, not inferred.

## Decoupling

Default rule: 100 nF local ceramic decoupling per power pin, placed close to the package.

Vendor-documented exceptions/layout compromises must be reproduced deliberately. The official guide specifically recommends additional 4.7 uF capacitance on the core rail and shows the regulator/decoupling network as the reference for placement.

RetroSBC additionally retains a 10 uF-class local bulk capacitor on `MGMT_3V3`.

## Capture gate

The power block may only move to CAPTURE PASS after:

1. every supply pad in the validated QFN-80 table is connected;
2. package ground/exposed-pad requirements are independently verified and captured;
3. VREG_VIN/LX/FB/PGND/AVDD match the current vendor reference;
4. DVDD is connected to the filtered 1.1 V rail;
5. all required local decoupling is present;
6. RUN and SWD remain accessible;
7. ERC passes or each local exception is documented;
8. the completed block is compared side-by-side with the current official RP2350B Minimal design.

This document does not itself mark electrical capture PASS.
