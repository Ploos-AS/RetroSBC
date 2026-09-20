# M3.7 real KiCad management-power materialization

Status: **READY FOR ELECTRICAL MATERIALIZATION**

This defines the exact first native KiCad capture slice. The CSV remains the electrical source of truth.

## Slice A — regulator block

- U_MGMT = RP2354B_QFN80, project-local validated symbol and `RetroSBC:RP2354B_QFN80` footprint.
- L_MGMT_CORE = 3.3uH: U_MGMT VREG_LX pad 64 -> MGMT_1V1.
- C_MGMT_VREG_IN = 4.7uF: MGMT_3V3 -> GND.
- C_MGMT_VREG_OUT = 4.7uF: MGMT_1V1 -> GND.
- R_MGMT_VREG_AVDD = 33R: MGMT_3V3 -> VREG_AVDD pad 61.
- C_MGMT_VREG_AVDD = 4.7uF: VREG_AVDD -> GND.
- VREG_VIN pad 63 -> MGMT_3V3.
- VREG_PGND pad 62 -> GND.
- VREG_FB pad 65 -> MGMT_1V1 directly.
- EP -> GND.

No feedback divider is permitted.

## Slice B — MCU supply domains

Connect IOVDD pads 5/15/24/29/41/50/60/76, ADC_AVDD 59, USB_OTP_VDD 68 and QSPI_IOVDD 69 to MGMT_3V3; DVDD pads 10/32/51 to MGMT_1V1. Add locked-reference local 100nF-class bypassing and the 10uF-class MGMT_3V3 bulk capacitor.

## Capture acceptance gate

1. Real symbols, pins, labels and wires exist in `13_MANAGEMENT.kicad_sch`.
2. U_MGMT uses the validated project-local symbol and QFN-80 footprint.
3. Connectivity agrees with `rp2354b-power-netlist.csv`.
4. No MGMT_1V1_FB, feedback divider, provisional gate or guessed value exists.
5. KiCad parses the schematic.
6. ERC is run; every remaining warning/error is fixed or documented.
7. Netlist/package-binding validation passes.
8. Visual review confirms regulator current-loop intent and readable service/debug nets.

## Implementation rule

Do not hand-invent a large KiCad S-expression. Materialize small deterministic native KiCad slices, validate each with KiCad tooling, then commit the resulting `.kicad_sch`.
