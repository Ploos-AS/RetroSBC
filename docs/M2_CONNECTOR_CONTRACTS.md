# M2 — External Connector Contracts

## DB9 x2

Purpose: Amiga/Atari-style digital joystick baseline, with mouse/paddle extensions only after electrical qualification.

Requirements:
- two physical DB9 connectors;
- protected 5 V supply where required;
- ground;
- directional/button inputs;
- bidirectional signals only through suitable buffers/translators;
- ESD protection;
- no claim of paddle/analog compatibility until ADC path is designed and tested.

## RS-232

A real level-shifted RS-232 interface is required. FPGA/B1 UART logic must connect through a qualified RS-232 transceiver. Connector pinout and DTE/DCE role will be explicit on schematic and silkscreen.

## MIDI

Provide 5-pin DIN MIDI IN and OUT. Electrical circuitry must follow the applicable MIDI electrical interface requirements; do not wire FPGA UART pins directly to DIN connectors.

## RetroBus

RetroBus is a Ploos-AS expansion interface, not a Raspberry Pi header clone.

Target classes:
- protected 5 V;
- 3.3 V;
- ground;
- FPGA digital I/O;
- clock;
- IRQ;
- chip select;
- read/write/direction control;
- data/address-style signals;
- optional UART/SPI/I2C alternate functions.

Final pin count and connector family remain an M2 mechanical/BOM decision.

## Debug

Dedicated access is required for:
- FPGA JTAG;
- B1/K1 debug UART;
- K1 JTAG if available and practical;
- recovery/boot selection;
- reset;
- FPGA configuration/recovery.

Production test pads may duplicate these signals for a bed-of-nails fixture.


## Rev-A DB9 retro controller ports

Rev-A shall provide **2 x DE-9 (DB9) controller ports** as first-class FPGA-facing interfaces. Baseline mode is Atari/Amiga/C64-compatible digital joystick signalling (directions + fire), through protected level translation rather than raw FPGA I/O. Core-specific mouse, paddle, extra-button or bidirectional modes require explicit electrical mapping and qualification. See `M3_3_CORE_COMPATIBILITY.md`.


## Rev-A serial ports

Rev-A shall expose independent external serial interfaces for **Linux/K1** and **FPGA/ECP5**. Both user-facing paths shall support real RS-232 through appropriate transceivers; neither may expose RS-232 levels directly to logic I/O. Linux shall additionally retain a 3.3 V TTL debug UART/header. FPGA serial must be directly core-ownable; an optional internal Linux↔FPGA bridge/cross-connect is supplementary, not a replacement for the two independent serial paths.


## Rev-A PS/2 input

Rev-A shall provide **2 x mini-DIN-6 PS/2 connectors**, one keyboard and one mouse. Both Linux/K1 and FPGA/ECP5 domains shall be able to consume PS/2 input through controlled mux/bridge ownership; FPGA must support direct PS/2 clock/data ownership without Linux forwarding. USB keyboard/mouse/gamepad on the Linux host remains a fallback and may also be forwarded to FPGA cores. PS/2 electrical implementation must preserve open-collector behavior, provide protected 5 V peripheral power and level translation, and prevent simultaneous bus driving.


## Rev-A audio, MIDI and video

- **Audio:** 2 x RCA/phono stereo line output (L/R) is mandatory. FPGA direct audio generation and Linux audio routing shall both be supported. A 3.5 mm stereo convenience output is preferred if practical.
- **MIDI:** 5-pin DIN MIDI IN + MIDI OUT, routable to both Linux and FPGA, with direct FPGA ownership supported.
- **Video:** HDMI is mandatory. Linux/K1 native HDMI and FPGA-generated video must each have a defined display path. Rev-A shall also provide or reserve an analog RGB path for retro monitors/upscalers; exact connector (e.g. DE-15 RGBHV vs dedicated RGB expansion) is an M3.3 schematic decision. Composite/S-Video remain optional.
