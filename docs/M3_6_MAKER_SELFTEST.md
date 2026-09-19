# M3.6 — Maker I/O bring-up and self-test

Status: **Rev-A qualification requirement**

The maker headers must be testable, not merely exposed.

## Linux/K1 self-test

Provide a host-side diagnostic utility or script that can:
- report board revision;
- enumerate documented GPIO lines;
- exercise safe output/input loopback pairs;
- scan documented I2C buses;
- perform SPI loopback when a test fixture is fitted;
- exercise UART loopback;
- test PWM output where measurable;
- report power/voltage-monitor data where hardware supports it.

Use modern Linux GPIO interfaces (GPIO character device / libgpiod), not deprecated sysfs GPIO as the primary interface.

## FPGA self-test core

Provide a small open RetroCore qualification bitstream/design that can:
- toggle every safe maker GPIO;
- sample every maker GPIO input;
- perform walking-one/walking-zero patterns;
- test UART loopback;
- exercise SPI signals;
- exercise I2C-style open-drain behavior;
- generate PWM/test clocks on designated capable pins;
- test the dedicated FPGA microSD interface;
- expose status to the Linux host-control interface.

The self-test core must avoid driving signals that can conflict with attached peripherals unless explicitly enabled.

## Dual-header loopback fixture

Design a simple passive/open-hardware fixture or cable map connecting selected Linux and FPGA header pins.

It should enable:
- Linux -> FPGA GPIO test;
- FPGA -> Linux GPIO test;
- interrupt/event test;
- UART cross-domain test;
- SPI master/slave experiment;
- timing/latency measurements.

The fixture belongs under the RetroSBC hardware license and should be cheap enough for hobbyist assembly.

## Educational value

The same self-test infrastructure should double as starter examples:
1. Linux GPIO blink/read.
2. FPGA GPIO blink/read.
3. Linux sends an event to FPGA.
4. FPGA interrupts Linux.
5. Linux SPI master -> FPGA SPI peripheral.
6. FPGA-generated PWM measured/read by Linux.

This turns manufacturing diagnostics into reusable maker tutorials rather than maintaining two unrelated systems.

## CI/HIL path

Host-side tests should run in ordinary CI where hardware is not required. Hardware-dependent tests should have explicit skip/report behavior and later integrate with Ploos-AS hardware CI/HIL runners.

## Rev-A gate

Before declaring the maker subsystem qualified:
- published header pin maps exist;
- voltage/current limits are documented;
- Linux self-test passes on hardware;
- FPGA self-test core passes on hardware;
- cross-domain loopback passes;
- no unsafe simultaneous-drive condition is observed;
- results are recorded in the Rev-A qualification report.
