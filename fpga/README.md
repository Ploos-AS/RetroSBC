# RetroSBC FPGA

This directory is the board-neutral starting point for RetroCore RTL.

The current target is the Lattice ECP5UM family in the approximately 45K LUT class. The exact Rev A device, package and pin constraints remain consumer/board facts and are not guessed here.

## Current qualification

- RTL smoke simulation: available via `make test`
- ECP5 synthesis: available via `make synth`
- Place-and-route / bitstream: pending exact Rev A device/package/constraints
- Physical FPGA qualification: pending Rev A hardware

The eventual hardware-ci integration will use the generic `ecp5` profile while RetroSBC owns the exact device, package, constraints and bitstream build target.

## Synthetic CI target

The repository's existing 85K smoke check is a toolchain regression test only. It verifies that the CI environment exposes an ECP5 85K target; it is **not** the RetroSBC Rev A FPGA selection and does not qualify physical RetroSBC hardware.

The documented Rev A baseline remains ECP5UM, approximately 45K LUT class, until the exact device/package and board constraints are frozen.
