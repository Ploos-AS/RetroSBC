# M3.2 — ECP5 SDR SDRAM controller

Status: **FIRST RTL IMPLEMENTATION**

This adds the first native RetroSBC SDR SDRAM controller behind the qualified portable memory bridge.

Implemented controller phases:
- power-up wait and CKE enable;
- PRECHARGE ALL;
- two AUTO REFRESH commands;
- LOAD MODE REGISTER;
- ACTIVE / tRCD;
- READ / CAS latency;
- WRITE with byte masks;
- PRECHARGE / tRP;
- periodic AUTO REFRESH / tRFC.

The implementation is intentionally conservative: one request at a time and close-page operation. That is appropriate for first hardware bring-up and makes protocol/debug behavior easy to understand.

## Important qualification boundary

Timing parameters and address geometry are **provisional**. This RTL passing synthesis does not qualify a physical SDRAM interface. Production qualification requires the exact SDRAM MPN, controller clock, datasheet-derived cycle values, FPGA bank/pin assignment, board timing constraints, simulation, and hardware testing.

## Next

1. CI synthesis.
2. Add command-sequence simulation assertions.
3. Freeze SDRAM MPN and geometry.
4. Derive timing parameters from its datasheet.
5. Add ECP5 I/O/top-level physical wrapper and constraints.
6. Connect the portable bridge and representative AGA master.
