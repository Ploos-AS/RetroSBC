# M3.1 — Minimig-AGA Upstream Audit

Status: **PASS — upstream pinned; adapter work identified**

## Pinned reference

Repository: MiSTer-devel/Minimig-AGA_MiSTer  
Branch family: MiSTer  
Pinned commit: `c1134acf81f3b2ec624b22c8bc6a28465ec093db`  
Commit date: 2026-09-17  
Commit subject: `Add real floppy drive support (#245)`

The pin prevents capacity results from silently changing when upstream changes.

## Provenance/licensing boundary

Minimig-AGA remains an external upstream reference with its own GPL licensing. RetroSBC does not relicense imported upstream RTL as CERN-OHL-P-2.0.

Any future CI fetch must checkout the exact SHA above and record it in build artifacts.

## Portability classification

### Machine/core RTL — candidate for ECP5 adaptation
- 68k/CPU-facing machine logic
- Agnus/Alice/AGA-style chipset logic
- Denise/Lisa/video machine logic
- Paula/audio/floppy logic
- CIA and machine glue
- memory-controller logic that is not tied to Intel hard IP

### MiSTer/platform integration — replace/adapt
- MiSTer top-level/HPS integration
- Intel/Altera PLL and clocking primitives
- Cyclone-V DDR/HPS paths
- MiSTer framework buses and configuration plumbing
- platform-specific video/audio wrappers
- Quartus project/constraint files
- vendor-specific RAM/ROM primitives that Yosys cannot infer portably

## ECP5 adapter layers

RetroSBC should create clean adapter boundaries for:
1. clocks/reset;
2. SDR SDRAM controller;
3. host register/control bridge;
4. video output/capture;
5. audio;
6. floppy/storage abstraction;
7. physical joystick/mouse;
8. configuration/ROM loading;
9. optional PCIe transport beneath a transport-independent host ABI.

## Qualification meaning

M3.1 does **not** claim the AGA core already synthesizes for ECP5. It proves that the reference revision and migration boundary are explicit enough to begin an auditable port.
