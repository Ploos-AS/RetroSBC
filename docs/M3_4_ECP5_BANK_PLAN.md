# M3.4 — ECP5 bank allocation plan

Status: **pre-ball-assignment**

Target: LFE5UM-85F-7BG381I.

This document converts the raw I/O budget into voltage/resource classes before assigning exact BG381 package balls.

## Allocation classes

### Class A — dedicated external SDR SDRAM
The x16 3.3 V SDR SDRAM interface gets first priority and shall be kept within the smallest practical set of compatible 3.3 V FPGA banks. Data, DQM, address, bank-address, command and clock signals must be placed with timing and routing locality in mind. Do not scatter SDRAM across spare pins simply to simplify connector routing.

### Class B — SERDES/high-speed
Reserve ECP5UM SERDES resources and required reference-clock resources before ordinary GPIO assignment. Initial target is the K1/B1 high-speed host link/PCIe. These resources are not available to RetroBus or general connectors.

### Class C — video
FPGA video has two resource classes:
- analog RGBHV: ordinary GPIO feeding the selected DAC/resistor/driver stage;
- HDMI/DVI-compatible path: differential/high-speed resources or a dedicated transmitter/bridge.

The final HDMI circuit decides whether FPGA pins are TMDS-facing or feed an external transmitter. Do not bind generic GPIO until that decision is locked.

### Class D — fixed low-speed retro I/O
Allocate protected low-speed I/O next:
- 2 x DB9 joystick;
- PS/2 keyboard;
- PS/2 mouse;
- FPGA RS-232 UART including target RTS/CTS;
- MIDI IN/OUT;
- audio digital interface;
- Linux/K1 control SPI + IRQ/reset/status;
- board management signals.

These should use banks whose VCCIO is compatible with the chosen level translators and board logic. External 5 V interfaces never set FPGA VCCIO to 5 V.

### Class E — RetroBus
RetroBus receives remaining compatible ordinary GPIO after Classes A-D. Its logical contract remains stable even if Rev-A exposes fewer parallel signals than the theoretical maximum.

## Voltage-domain policy

Preferred FPGA GPIO domains are 3.3 V where compatible with the ECP5 device and selected peripherals, with explicit translators/buffers for external 5 V retro interfaces. Any bank requiring another VCCIO is isolated as a deliberate design choice and documented before pin binding.

No connector voltage is allowed to dictate an unsafe FPGA bank voltage.

## Clock-capable resources

Reserve clock-capable pins before ordinary allocation for:
- FPGA reference/fabric clock;
- SDRAM clocking path as required by implementation;
- video pixel/reference clock inputs if external;
- SERDES reference clock;
- optional external/core clock inputs on RetroBus only after platform clocks are satisfied.

## Configuration/debug reservation

Configuration flash, mode/config pins, JTAG and reset/programming resources are reserved before connector GPIO. Manufacturing access must remain possible on an assembled board.

## Pin-binding gate

Exact LPF constraints shall not be committed as a production pinout until they are checked against the official LFE5UM-85F BG381 package pin table. The next binding artifact shall contain, for every FPGA signal:
- package ball;
- bank;
- VCCIO;
- direction;
- I/O standard;
- clock/differential/SERDES capability where relevant;
- destination sheet/connector/device;
- protection/translator reference.

## Current result

The Rev-A architecture remains feasible at the bank-planning level. No first-class interface is removed. The remaining hard dependencies are the exact BG381 ball map, the FPGA HDMI implementation choice, and the B1/K1 high-speed-link binding.
