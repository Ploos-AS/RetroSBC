# M3.7 — RP2354B QFN-80 footprint contract

Status: **footprint requirements locked; physical footprint implementation/DRC pending**

This contract binds the validated RP2354B QFN-80 symbol to the physical package requirements before schematic capture is called complete.

## Package

- Device: RP2354B / RP2350 B-package family.
- Package class: QFN-80 with centre exposed pad.
- Numbered perimeter pads: 1..80.
- Centre exposed pad: `EP`, electrical function `GND`.
- The exposed pad is mandatory and is the package's single external ground connection; it must not be omitted from the footprint or left floating.

## Symbol ↔ footprint contract

The project-local symbol exposes:
- pads `1` through `80` exactly as validated by the package CSV;
- one additional logical pin `EP` named `GND`.

The selected/generated footprint therefore MUST provide a matching `EP` pad number for the centre thermal/ground pad. If a vendor/library footprint uses a numeric exposed-pad identifier instead, RetroSBC must either adapt the footprint to `EP` or update symbol + validators together. Silent mismatch is forbidden.

## Layout requirements

The footprint implementation must be checked against the current official Raspberry Pi RP2350 mechanical/package drawing before release.

Requirements:
- exact body dimensions, perimeter pitch, pad dimensions and exposed-pad dimensions from the official drawing;
- solder-mask and paste apertures suitable for the centre exposed pad;
- ground-via strategy under/adjacent to the exposed pad documented before fabrication;
- pin-1 orientation unambiguous on copper/assembly documentation and silkscreen where practical;
- courtyard and assembly outlines present;
- no generic QFN-80 footprint is accepted solely because pitch/pad count appear similar.

## Qualification gate

Footprint qualification requires:
1. mechanical dimensions checked against the official package drawing;
2. pads 1..80 and EP checked for numbering/orientation;
3. EP has GND connectivity in schematic/netlist;
4. paste/mask strategy reviewed;
5. thermal/ground via strategy reviewed;
6. KiCad DRC passes;
7. generated fabrication outputs visually checked around U_MGMT.

Until these pass, management MCU capture remains **not physically qualified**.
