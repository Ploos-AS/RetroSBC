# M3.4 — Exact pin-binding source gate

Status: **BLOCKED pending authoritative package/module data**

M3.4 has established that the Rev-A I/O set is plausible by raw ECP5 I/O count and has defined the bank/resource allocation policy. The next step is exact package-ball binding. This step must not use guessed pin numbers.

## Required authoritative inputs

### ECP5
Exact binding requires the official Lattice data for:
- LFE5UM-85F;
- BG381 package;
- package-ball to bank mapping;
- VCCIO and dedicated supply pins;
- PCLK/clock-capable pins;
- SERDES lanes and reference clocks;
- configuration and JTAG pins;
- differential-pair capability;
- any package-specific restrictions.

### B1/K1
Exact host-side binding requires authoritative B1 module documentation for:
- module ball/pin assignment;
- multiplexed peripheral functions;
- USB3/PCIe combo-port routing;
- PCIe x2 routing;
- GMAC;
- HDMI;
- SDIO/eMMC;
- SPI/I2C/UART/PWM;
- boot/recovery/debug;
- power and sequencing.

## Binding artifact

Once source data is available, create a machine-readable table with one row per net:

`signal,domain,package_ball,bank,vccio,io_standard,direction,capability,destination,translator,notes,source`

The table shall be the source for:
- KiCad symbol/pin review;
- ECP5 LPF constraints;
- schematic ERC cross-checks;
- pin-budget CI;
- documentation.

## CI requirements

A pin-binding checker shall eventually reject:
- duplicate package-ball assignments;
- use of reserved/configuration pins as ordinary GPIO;
- incompatible VCCIO/I/O-standard combinations;
- accidental use of SERDES/refclock resources;
- missing source citation for exact physical pins;
- mandatory Rev-A interfaces with unbound signals.

## No-guess rule

Until the authoritative BG381 and B1 data is present in the project, exact ball numbers remain **UNBOUND**. Architecture and logical signal names may progress, but fabricated pin mappings must not enter schematics, LPF files, or manufacturing data.

## Next qualification gate

PASS requires:
1. authoritative ECP5 BG381 pin source identified and recorded;
2. authoritative B1/K1 pin source identified and recorded;
3. initial exact ECP5 binding table;
4. automated duplicate/reserved-pin validation;
5. bank/VCCIO review;
6. review of remaining GPIO count for the maker header.
