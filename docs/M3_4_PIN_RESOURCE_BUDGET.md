# M3.4 — FPGA pin and resource budget

Status: **pre-pin-binding budget**

Target FPGA: **LFE5UM-85F-7BG381I** (~205 user I/O). This document checks whether the Rev-A external-I/O contract is structurally compatible with the FPGA before exact package-ball assignment.

## Dedicated FPGA interfaces

| Interface | Approx. FPGA I/O | Notes |
|---|---:|---|
| x16 SDR SDRAM | 39 | DQ16 + A13 + BA2 + control/clock/DQM |
| DB9 joystick 1 | 7 | directions/buttons; protected interface |
| DB9 joystick 2 | 7 | directions/buttons; protected interface |
| PS/2 keyboard | 2 | clock/data through protected mux |
| PS/2 mouse | 2 | clock/data through protected mux |
| FPGA RS-232 | 4 | TX/RX + RTS/CTS target |
| MIDI | 2 | IN + OUT |
| Stereo audio | 3 | representative I2S: BCLK/LRCLK/DATA |
| Analog RGBHV | 17 | representative RGB 4:4:4 + HSYNC/VSYNC; DAC implementation may change count |
| Linux/K1 control SPI | 6 | SCLK/MOSI/MISO/CS + IRQ/reset |
| Board management | 4 | status/config/ID/aux estimate |
| RetroBus baseline | 24 | initial protected expansion allocation |
| FPGA debug/JTAG | 4 | dedicated/config resources where available |

Representative subtotal: **121 I/O**.

This is intentionally conservative but is **not a final package pin count**. Dedicated configuration/JTAG pins, SERDES, differential resources, clock-capable pins and bank-voltage restrictions cannot be treated as generic GPIO.

## High-speed resources

PCIe/host high-speed transport should use ECP5UM SERDES rather than consuming ordinary GPIO. HDMI/DVI output may require differential pairs and a transmitter/bridge depending on the final architecture. These must be budgeted by resource class, not merely by pin count.

## Linux/K1-owned connectors

The following do not need to consume ordinary FPGA GPIO unless optional monitoring/cross-connect is implemented:
- Linux RS-232;
- Linux HDMI;
- Ethernet;
- USB;
- microSD/eMMC/NVMe;
- Linux debug UART.

Cross-connects should preferentially use small muxes/bridges rather than duplicate every host signal into the FPGA.

## Preliminary result

The Rev-A contract is **plausible on the 85F/BG381 from a raw I/O-count perspective**. A representative 121-pin allocation leaves roughly 80 nominal user-I/O positions before exact bank/package constraints.

This is not yet a PASS for physical pinout. The real gate is exact bank assignment:
1. lock SDRAM to a compatible 3.3 V bank grouping;
2. reserve SERDES lanes/refclocks for PCIe;
3. determine FPGA HDMI implementation and differential resources;
4. assign RGB/audio/PS2/DB9/MIDI/serial to compatible banks;
5. allocate RetroBus only from remaining safe GPIO;
6. reserve clocks, JTAG/configuration and manufacturing test access;
7. verify every selected package ball against the official Lattice pinout.

## Design rule

RetroBus is the elastic consumer. Core platform functions (SDRAM, host control, video, audio, joystick, PS/2, serial, MIDI) are allocated first. RetroBus width may be adjusted before sacrificing first-class Rev-A interfaces.
