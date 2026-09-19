# M3.4 — GPIO expansion policy

Status: **Rev-A allocation policy**

Unused FPGA I/O after all mandatory platform functions are assigned shall not be left inaccessible by default. RetroSBC shall expose a useful subset on a maker-friendly GPIO/expansion header.

## Priority

FPGA pins are allocated in this order:

1. configuration, JTAG, reset and mandatory clocks;
2. dedicated SDR SDRAM;
3. SERDES/high-speed host transport;
4. mandatory video/audio;
5. DB9 joystick, PS/2, FPGA serial and MIDI;
6. Linux/FPGA control and management;
7. RetroBus baseline;
8. **general-purpose FPGA GPIO header**;
9. reserve/test-only pins.

GPIO never displaces a mandatory Rev-A function.

## FPGA GPIO header

Target: expose **at least 16 general-purpose FPGA I/O** if the final BG381 bank allocation permits it; **24-32 GPIO** is preferred when practical.

The header should include:
- FPGA GPIO;
- multiple GND pins interspersed for signal integrity;
- protected 3.3 V supply;
- protected 5 V supply for external modules where power budget permits;
- one or more clock-capable GPIO when genuinely spare;
- optional IRQ/handshake labels only as aliases, not hard-wired semantics.

External header GPIO shall be 3.3 V logic unless an explicitly documented translated subset is provided. 5 V power on the header does **not** imply 5 V-tolerant GPIO.

A conventional 2.54 mm through-hole header is preferred for maker friendliness.

## Linux GPIO

Linux/K1 spare low-speed I/O should also be exposed where the B1 interface and muxing permit it. Prefer a **separate Linux GPIO header or clearly partitioned section** rather than silently mixing K1 and FPGA pins.

Useful Linux header functions may include:
- GPIO;
- I2C;
- SPI;
- UART;
- PWM;
- 3.3 V;
- 5 V protected supply;
- GND.

Exact availability remains gated on the official B1/K1 interface documentation.

## Relationship to RetroBus

RetroBus is the structured retro expansion interface. The GPIO header is the maker/prototyping interface. They are complementary:
- RetroBus: defined bus signals, expansion boards, stable platform contract;
- GPIO: flexible experiments, HIL, breadboards, logic interfaces and education.

Where a physical FPGA pin can only serve one connector, the frozen RetroBus baseline has priority over optional GPIO.

## Qualification

Final schematic qualification shall publish:
- FPGA GPIO count actually exposed;
- Linux GPIO/peripheral count actually exposed;
- voltage and current limits;
- 5 V tolerance status;
- clock-capable pins;
- alternate functions;
- reserved/do-not-use pins;
- header pinout diagram.
