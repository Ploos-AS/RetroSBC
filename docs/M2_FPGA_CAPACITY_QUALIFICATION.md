# M2 — FPGA Capacity Qualification: A1200/AGA Reference Core

Status: **PASS — baseline upgraded to ECP5UM-85F**

## Qualification target

RetroSBC uses an Amiga 1200 / AGA-class machine as the capacity reference because it combines a 68020-class CPU, AGA chipset, Paula/CIA/Gayle-style logic, memory control, storage and substantial video timing while still being a realistic open retro FPGA workload.

This is a capacity reference, not a promise of cycle-perfect compatibility.

## Evidence

The upstream Minimig-AGA project states that its core targets boards with about **25,000 logic elements** plus 16-bit SDRAM and supports AGA-class Amiga systems. An independent Cyclone-V UnAmiga design also documents an AGA Amiga implementation on a **25K logic-cell** Cyclone V with 256-Mbit SDRAM.

This demonstrates that an AGA implementation can fit well below the capacity of either candidate, but RetroSBC needs additional fabric for its host bridge, instrumentation, capture, RetroBus and other platform services.

## Device comparison

| Resource | LFE5UM-45 | LFE5UM-85 |
|---|---:|---:|
| LUTs | 44K | 84K |
| 18-Kbit sysMEM blocks | 108 | 208 |
| Embedded RAM | 1,944 Kbit | 3,744 Kbit |
| 18x18 multipliers | 72 | 156 |
| SERDES channels | 4 | 4 |
| BG381 I/O | 203 | 205 |

The 85F almost doubles logic, embedded memory and DSP capacity while retaining four SERDES channels and the same 17 x 17 mm BG381 package class.

## Decision

**Rev-A primary FPGA becomes LFE5UM-85F-7BG381I.**

The previous LFE5UM-45F-7BG381I is demoted to a possible cost-reduced variant only after actual synthesis proves that the selected RetroCore profile plus mandatory platform logic fits with acceptable timing and reserve.

## Resource policy

For the primary production profile:
- target <=70% LUT utilization for the representative AGA build;
- preserve >=20% post-route logic reserve where practical;
- platform/debug fabric is first-class and must not be stripped merely to make a 45F fit;
- external SDRAM remains mandatory;
- PCIe/SERDES and SPI fallback remain part of the architecture.

## Why 85F

RetroSBC is a development/instrumentation platform, not a single-purpose Minimig board. Capacity is intentionally reserved for:
- Linux/FPGA host bridge;
- trace and logic-analyzer style capture;
- debug registers and inspection;
- RetroBus;
- controller/MIDI/serial interfaces;
- video/capture/scaler experiments;
- future cores and compatibility work.

## Next proof gate

M3 must import or adapt a legally compatible AGA reference core and run synthesis/place-and-route for ECP5. Actual utilization and timing reports replace estimates. No proprietary Kickstart ROM is required for synthesis qualification.
