# M3.7 — KiCad power materialization checklist

This is the execution checklist for converting the validated RP2354B power connectivity into real KiCad objects in `13_MANAGEMENT.kicad_sch`.

## Required objects

- U_MGMT: validated `RP2354B_QFN80` symbol with `RP2354B_QFN80` footprint.
- L_MGMT_CORE: VREG_LX core-regulator inductor; value remains source-gated until checked against the official current reference.
- C_MGMT_BULK: 10 uF-class MGMT_3V3 bulk capacitor.
- Local IOVDD/ADC_AVDD/VREG_AVDD/USB_OTP_VDD/QSPI_IOVDD bypass capacitors.
- Local DVDD/core-rail regulator-support capacitors exactly per qualified reference topology.
- TP_MGMT_3V3 and core-rail test point where electrically appropriate.

## Required wiring

Materialize every row of `rp2354b-power-netlist.csv`. Do not replace explicit supply connectivity with prose labels only.

The schematic must visibly distinguish:
- MGMT_3V3
- MGMT_1V1
- MGMT_1V1_FB
- VREG_LX
- GND

EP/GND must be electrically captured, not merely represented in the footprint.

## Qualification sequence

1. Instantiate U_MGMT and bind the validated footprint.
2. Capture all supply pins.
3. Capture VREG_LX/FB network.
4. Add local bypass/bulk components.
5. Add RUN/SWD recovery wiring.
6. Run KiCad ERC.
7. Export/check netlist against `rp2354b-power-netlist.csv`.
8. Visually review schematic and package binding.
9. Record any ERC exception explicitly.

Do not mark CAPTURE PASS while source-gated component values or topology remain unresolved.
