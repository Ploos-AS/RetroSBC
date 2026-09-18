# M2 — FPGA Bank Planning

Target family: Lattice ECP5UM-85F, BG381 planning package.

This file defines functional ownership before assigning physical pins.

| Function | Requirement | Planning rule |
|---|---|---|
| SERDES/PCIe | differential high speed | use dedicated SERDES resources only |
| FPGA SDRAM | wide synchronous bus | dedicate contiguous compatible I/O bank resources |
| RetroBus | mixed external digital | translated/protected bank |
| DB9 A/B | low-speed retro I/O | buffered/protected; do not share timing-critical SDRAM pins |
| SPI host control | low-speed B1 link | retain independent of PCIe |
| IRQ/reset/status | host control GPIO | dedicated simple pins |
| MIDI | low speed | interface circuitry isolates electrical standard |
| RS-232 | UART | behind RS-232 transceiver |
| JTAG/config | programming | preserve dedicated access |
| optional video | timing/differential dependent | allocate only after required paths are proven |

## Constraints

- No bank is assigned a VCCIO until all functions in that bank are voltage-compatible.
- SDRAM gets priority over optional expansion GPIO.
- PCIe resources get priority over optional FPGA video.
- RetroBus must expose useful signals without consuming every spare FPGA pin.
- Reserve pins for clocks, recovery and board revision identification.

A physical ball/pin table is intentionally deferred until the exact ordering code and official package pinout are locked.
