# M2 — FPGA Device Lock

## Baseline OPN

`LFE5UM-45F-7BG381I`

Family: ECP5UM (SERDES)
Logic class: 45K
Package: 381-ball caBGA
Grade: Industrial
Speed grade: -7 baseline

## Why UM matters

The plain LFE5U family does not provide the SERDES resources required by the planned FPGA PCIe path. The schematic/BOM must therefore reject accidental substitution of an `LFE5U-45F` for an `LFE5UM-45F`.

## Configuration

Rev A shall provide:
- external SPI configuration flash;
- dedicated JTAG;
- recovery-friendly configuration straps;
- accessible PROGRAMN/INITN/DONE-style configuration status/control as applicable to the final pin binding;
- test pads suitable for manufacturing programming.

## Clocking

Provide dedicated low-jitter clock source footprints for FPGA fabric and SERDES requirements rather than relying on an improvised GPIO clock from the compute module.

Exact frequencies are frozen after PCIe/SDRAM/video clock plans are completed.

## Power

All required core, auxiliary, I/O and SERDES supplies/decoupling must follow the current ECP5 hardware checklist and datasheet. No rail values are inferred from generic FPGA practice.
