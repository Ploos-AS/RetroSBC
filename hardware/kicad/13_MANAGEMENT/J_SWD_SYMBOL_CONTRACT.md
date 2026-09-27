# J_SWD native symbol contract

Status: M3.7 — ready for native schematic materialization.

The management schematic shall use a project-local six-pin connector symbol
named `J_SWD`, bound to `RetroSBC:TC2030-IDC-FP`.

| Pin | Net | Function |
|---:|---|---|
| 1 | MGMT_3V3 | VTREF |
| 2 | MGMT_SWDIO | SWDIO |
| 3 | MGMT_RUN | nRESET / RUN |
| 4 | MGMT_SWCLK | SWCLK |
| 5 | GND | debugger ground / GNDDetect |
| 6 | SWO_RESERVED | SWO; reserved, not repurposed |

## Symbol rules

- Reference: `J_SWD`.
- Value: `TC2030-CTX SWD`.
- Footprint: `RetroSBC:TC2030-IDC-FP`.
- Pins 1..6 are passive connector pins; the MCU symbol retains the electrical
  pin types used for ERC.
- Pin 6 must remain explicitly named `SWO_RESERVED` until a source-backed
  RP2354B SWO policy is adopted.
- The footprint is DNL: it is a PCB contact/hole pattern, not a loaded part.

## Netlist acceptance

The exported native netlist must prove:

- J_SWD.1 shares MGMT_3V3.
- J_SWD.2 shares MGMT_SWDIO with U_MGMT pad 34.
- J_SWD.3 shares MGMT_RUN with U_MGMT pad 35.
- J_SWD.4 shares MGMT_SWCLK with U_MGMT pad 33.
- J_SWD.5 shares GND.
- J_SWD.6 is not silently repurposed.

Do not change checklist status to `CAPTURED_NATIVE` until these conditions
pass in CI.
