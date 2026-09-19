# KiCad project state

This directory is now a standalone KiCad project for the Rev-A management block.

- `RetroSBC-13-MANAGEMENT.kicad_pro` — project container.
- `13_MANAGEMENT.kicad_sch` — schematic capture sheet.
- `RetroSBC-management.kicad_sym` — project-local symbol library.

## Safety rule

The local RP2354B symbol is deliberately named `RP2354B_QFN80_PLACEHOLDER` and has no electrical pins. It must **not** be used for PCB/netlist generation.

This prevents an incomplete hand-authored 80-pin MCU symbol from silently becoming hardware.

The next implementation step is to transcribe all QFN-80 pads/functions from the locked official Raspberry Pi sources into a reviewable machine-readable table, validate that table for exactly one occurrence of each package pad, and only then generate/commit the electrical KiCad symbol.

Existing GPIO bindings in `rp2354b-binding.csv` remain the RetroSBC logical assignment overlay.
