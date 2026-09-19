# 13_MANAGEMENT schematic

This directory contains the Rev-A KiCad capture for the RP2354B board-management subsystem.

The initial `13_MANAGEMENT.kicad_sch` is intentionally a capture scaffold, not a qualified electrical schematic. It establishes the real KiCad artifact and review boundary before symbols, package pads and component values are bound.

## Do not mark electrically complete until

- RP2354B QFN-80 symbol/package mapping is checked against authoritative current documentation.
- Vendor-required power/decoupling and integrated-flash requirements are captured.
- USB-C service port has CC, ESD and VBUS/back-power protection.
- SWD/RUN recovery is captured.
- All stable logical M3.7 nets are present.
- B1 crossings use verified voltage levels and selected translators.
- ERC is clean or exceptions are locally documented.

See `docs/M3_7_MANAGEMENT_KICAD_CAPTURE.md`.
