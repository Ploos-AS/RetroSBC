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
| 61 | VREG_AVDD | MGMT_3V3 |
| 62 | VREG_PGND | GND |
| 63 | VREG_VIN | MGMT_3V3 |
| 64 | VREG_LX | VREG_LX |
| 65 | VREG_FB | MGMT_1V1_FB |
| 68 | USB_OTP_VDD | MGMT_3V3 |
| 69 | QSPI_IOVDD | MGMT_3V3 |
| 76 | IOVDD | MGMT_3V3 |
| EP | GND | GND |

## Power block

- `VREG_LX` connects only through the selected reference inductor to the filtered core rail.
- `VREG_FB` senses the filtered core rail.
- `MGMT_1V1` feeds DVDD pads 10/32/51.
- `MGMT_3V3` feeds every 3.3 V supply-domain pad listed above.
- VREG_PGND and EP connect directly into GND.
- C_MGMT_BULK = 10 uF class on MGMT_3V3.
- C_MGMT_DECOUPLING = 100 nF class local bypasses for required supply groups.
- Exact VREG support components must match the current official reference design; no inferred value is permitted.

## Recovery

- Pad 35 RUN -> MGMT_RUN.
- Pad 33 SWCLK -> SWCLK.
- Pad 34 SWDIO -> SWDIO.

## Capture gate

This manifest is not ERC PASS. The next KiCad capture must instantiate U_MGMT with the validated symbol/footprint, attach these nets, add the reference regulator components and decoupling, then run ERC and package-binding checks.
