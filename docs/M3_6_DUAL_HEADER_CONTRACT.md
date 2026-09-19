# M3.6 — Dual maker-header physical contract

Status: **Rev-A mechanical/electrical contract; exact signal assignment remains gated by B1 and ECP5 pin binding**

RetroSBC uses a deliberately consistent maker experience across the Linux/K1 and FPGA domains.

## Physical format

Both maker domains target a **2x20, 40-pin, 2.54 mm through-hole header**.

The two headers should:
- use the same orientation convention;
- place pin 1 consistently;
- use matching mechanical footprint and shrouding/clearance policy;
- have domain-specific silkscreen: `LINUX GPIO` and `FPGA GPIO`;
- reserve multiple ground positions distributed across the connector;
- expose protected power at predictable positions where practical.

They are **not electrically pin-compatible by default**. Consistency is for maker ergonomics, not to create unsafe interchangeable hats.

## Common logical roles

Where final routing permits, both headers should present similar categories:
- 3.3 V power
- protected 5 V power
- GND
- general GPIO
- UART TX/RX
- I2C SDA/SCL
- SPI SCLK/MOSI/MISO/CS
- PWM/timer-capable signals
- interrupt/event-capable signals

Linux signals use K1 peripherals and Linux drivers. FPGA signals are direct programmable fabric I/O and may implement equivalent buses in RTL.

## Proposed pin-role skeleton

This is a **role skeleton**, not an electrical pinout:

| Pins | Preferred role |
|---|---|
| 1-2 | power |
| 3-6 | I2C / GPIO |
| 7-10 | GPIO / GND |
| 11-16 | GPIO / UART / PWM |
| 17-20 | power / SPI |
| 21-26 | SPI / GPIO / GND |
| 27-32 | GPIO / identification / event |
| 33-40 | GPIO / PWM / GND |

Exact per-pin assignments are intentionally deferred.

## Protection

Header signals should use inexpensive replaceable protection where useful without destroying high-speed/alternate-function capability:
- series resistor footprints on exposed digital lines where appropriate;
- ESD protection at externally accessible connectors;
- current-limited/protected 5 V export;
- documented 3.3 V current budget;
- no 5 V-tolerant claim unless the actual signal path is designed and qualified for it.

## Board identification

Reserve a small identification mechanism so software and examples can identify board revision:
- board ID EEPROM on management I2C, and/or
- readable strap/revision signals.

A maker add-on identification EEPROM convention may be defined later but is not required for Rev-A.

## Compatibility policy

Do not label either connector “Raspberry Pi compatible” unless an eventual mapping is electrically and software compatible.

Documentation may describe familiar 40-pin mechanics, but RetroSBC owns its pinout and prioritizes:
1. electrical correctness;
2. useful K1/FPGA functions;
3. maker friendliness;
4. stable revision-to-revision naming.

## Mechanical qualification

Before PCB lock:
- verify two 2x20 headers fit with DB9, PS/2, MIDI, VGA, HDMI, storage and cooling;
- ensure jumper-wire access when an M.2 2280 device is fitted;
- keep headers accessible with common heatsink/fan arrangements;
- allow logic-analyzer clips and individual Dupont leads;
- print voltage/domain labels on the PCB.
