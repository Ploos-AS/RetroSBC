# M0 Hardware Baseline

This document records targets to investigate. It is not a frozen schematic specification.

## Compute

Leading candidate:

- SpacemiT K1 via B1-class compute module
- 64-bit RISC-V Linux
- 8 GiB RAM target for the standard configuration

M1 must verify module sourcing, lifecycle, carrier documentation, connector/package implementation, power requirements, boot flow and usable high-speed interfaces.

## FPGA

Leading candidate:

- Lattice ECP5UM family
- approximately 45K LUT class
- Rev A FPGA baseline: `LFE5UM-45F-7BG381C`
- CABGA-381 (17 x 17 mm), 203 user I/O
- commercial temperature grade (0 C to +85 C junction)
- SERDES-capable ECP5UM variant

The Rev A FPGA baseline is now locked at the device/package/speed-grade level. This does not freeze pin assignment, bank allocation, transceiver usage or board constraints; those remain schematic/PCB qualification work. Sourcing must be rechecked before procurement or a production release.

## Target interfaces

Modern:

- Gigabit Ethernet
- dual Ethernet preferred
- USB 3
- USB 2
- HDMI
- microSD
- eMMC
- PCIe/NVMe where resources permit

Retro/developer:

- 2 x DB9 configurable retro controller ports
- level-correct RS-232
- MIDI
- RetroBus expansion
- host debug UART/JTAG
- FPGA JTAG
- boot/reset controls
- accessible test points

## Power

Development-board targets:

- USB-C power input preferred
- optional barrel/DC input worth evaluating
- separately documented rails
- current measurement points where practical
- protection against common development mistakes

## PCB

Assume a six-layer board for feasibility planning. Final stack-up must follow the selected fabricator and signal-integrity requirements.

## M1 questions

1. Can the compute module be sourced predictably in prototype and small-production quantities?
2. Are the required design files and electrical specifications available?
3. Which PCIe resources remain after NVMe/USB choices?
4. Which FPGA package provides sufficient I/O and SERDES without unreasonable PCB complexity?
5. Which retro ports require 5 V tolerance or bidirectional level translation?
6. Can both DB9 ports safely support joystick and mouse use cases?
7. Should FPGA video receive a dedicated output or share/mux a connector?
8. What thermal solution is required under sustained Linux + FPGA load?
9. What is the realistic Rev-A BOM and assembly cost?
10. Which components represent single-source lifecycle risks?
