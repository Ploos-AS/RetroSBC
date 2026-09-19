# M3.7 — Authoritative RP2354B package binding

Status: **QFN-80 package binding baseline**

The RP2354B uses the same 10×10 mm QFN-80 B-package pinout/I/O set as the RP2350B, with 2 MiB stacked flash added. Raspberry Pi publishes an RP2350B minimal KiCad design and the current hardware-design guide explicitly covers the QFN-80 B package.

The machine-readable binding is `rp2354b-binding.csv`.

## Important correction/verification rule

The GPIO-number plan is now mapped to QFN-80 pad numbers from the official RP2350 datasheet. This does **not** yet mean the full MCU symbol is capture-complete: every power, regulator, QSPI/stacked-flash, clock, ground, exposed-pad and debug pin must also be represented and checked against the current RP2354B requirements.

## Dedicated USB

Official QFN-80 pinout binds:
- pad 73: USB_DM
- pad 74: USB_DP

These are used for the dedicated management service USB.

## GPIO examples now physically bound

- GPIO0/1 -> pads 63/64 -> K1 debug UART
- GPIO4/5 -> pads 1/2 -> FPGA debug UART
- GPIO8/9 -> pads 7/8 -> management I2C
- GPIO16..19 -> pads 16..19 -> FPGA management SPI
- GPIO40..43 -> pads 49,52,53,54 -> analogue telemetry

The complete used-signal mapping is in the CSV.

## Source lock

Authoritative design sources for capture:
1. Raspberry Pi RP2350 datasheet, QFN-80 pinout and pin descriptions.
2. Raspberry Pi *Hardware design with RP2350*.
3. Raspberry Pi RP2350B Minimal KiCad reference design from the Product Information Portal.

Do not substitute a Pico 2 board schematic for the silicon/package source of truth.

## Next capture step

Import/construct the RP2354B QFN-80 symbol with all pins, then wire:
- power/regulator support exactly per hardware guide;
- integrated flash requirements for RP2354B;
- USB pads 73/74;
- RUN/SWD;
- the GPIO mappings in the CSV.

Only then can the KiCad sheet move from scaffold to electrical schematic.
