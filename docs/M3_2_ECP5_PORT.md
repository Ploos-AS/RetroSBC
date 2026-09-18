# M3.2 — ECP5 AGA Port Bring-up

Status: **IN PROGRESS**

M3.2 now executes the pinned upstream fetch in CI and generates a machine-produced inventory of HDL plus files containing Intel/Altera/Cyclone/Quartus/HPS dependencies.

## First objective

Do not attempt a misleading one-command synthesis of the MiSTer top level. First identify the portable machine RTL boundary, then provide ECP5-native adapters around it.

## CI artifacts

The FPGA qualification workflow now retains:
- pinned upstream revision;
- candidate HDL inventory;
- Intel/Altera/MiSTer portability-blocker inventory;
- Yosys smoke synthesis logs;
- nextpnr target/tool information.

## Adapter implementation order

1. clocks/reset;
2. portable RAM/ROM inference wrappers;
3. SDR SDRAM interface;
4. minimal host/config bridge;
5. machine-core top wrapper;
6. video/audio;
7. physical I/O;
8. optional PCIe transport.

## PASS gate

M3.2 becomes PASS only when a representative AGA machine build completes Yosys synthesis and nextpnr for the ECP5UM-85F target and reports utilization/timing. Until then, capacity remains strongly plausible but unproven on ECP5.
