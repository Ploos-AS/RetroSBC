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
