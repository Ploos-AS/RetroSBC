# M2 — Rev-A Schematic Architecture

Status: **IN PROGRESS — pre-capture specification**

M2 turns the M1 logical architecture into hierarchical schematic sheets and electrical contracts. No PCB may be called production-ready until the real KiCad schematic/PCB passes the centralized hardware-ci gates.

## Proposed KiCad hierarchy

1. `00_ROOT` — hierarchy, board identity and inter-sheet connectivity
2. `01_B1_COMPUTE` — SpacemiT B1 module, boot/debug and carrier interfaces
3. `02_POWER` — input protection, regulators, sequencing and measurement
4. `03_FPGA` — ECP5UM-45F, clocks, configuration and JTAG
5. `04_FPGA_RAM` — dedicated SDR SDRAM
6. `05_PCIE_STORAGE` — FPGA PCIe path and M.2 NVMe
7. `06_USB` — USB 3/2 routing and protection
8. `07_NETWORK` — primary GbE and optional second network interface
9. `08_VIDEO` — K1 HDMI and future FPGA video provisions
10. `09_DB9` — two protected retro controller ports
11. `10_SERIAL_MIDI` — RS-232 and MIDI IN/OUT
12. `11_RETROBUS` — expansion connector, translation and protection
13. `12_DEBUG_TEST` — JTAG/UART, recovery, test pads and manufacturing hooks

## Hard rules

- No 5 V external signal connects directly to K1/B1 or FPGA I/O.
- FPGA bank voltage is decided before pin binding.
- Differential pairs remain explicit named nets from source to destination.
- High-speed interfaces may not pass through generic level translators.
- Every external connector receives an ESD/protection review.
- Test points are designed in, not added after layout.
- FPGA PCIe is optional for first boot; SPI control remains available.
- Unqualified optional functions must be DNI-capable where practical.

## Capture sequence

Power and voltage domains are captured first, followed by B1 and FPGA core sheets. Only then are FPGA banks bound to SDRAM and retro I/O. High-speed interfaces are bound after the official B1 carrier constraints are verified.

## M2 exit criteria

- real KiCad project exists;
- hierarchy matches this document or records deviations;
- ERC passes with reviewed exceptions;
- all power rails and FPGA banks are assigned;
- all required external connectors have protection;
- preliminary BOM passes Ploos-AS maker/component policy;
- M2 qualification report records open layout-only risks.
