# M3.3 — Rev-A external I/O matrix

Status: **connector contract freeze candidate**

This matrix freezes the intended user-facing Rev-A interfaces before schematic capture and pin binding.

| Function | Physical interface | Linux/K1 | FPGA/ECP5 | Notes |
|---|---|---:|---:|---|
| Video | HDMI | direct | direct/bridge path | HDMI mandatory; FPGA must not require Linux capture |
| Retro video | DE-15 VGA/RGBHV | optional route | direct | baseline analog RGB connector |
| Audio | 2 x RCA/phono L/R | yes | direct | stereo line output; shared DAC/codec routing |
| Audio convenience | 3.5 mm stereo | yes | yes | preferred, space/BOM permitting |
| Joystick 1 | DE-9 | bridge/monitor optional | direct | Atari/Amiga/C64 digital baseline |
| Joystick 2 | DE-9 | bridge/monitor optional | direct | Atari/Amiga/C64 digital baseline |
| Keyboard | mini-DIN-6 PS/2 | selectable | direct/selectable | protected mux ownership |
| Mouse | mini-DIN-6 PS/2 | selectable | direct/selectable | protected mux ownership |
| Serial Linux | DE-9 RS-232 | direct | optional cross-connect | real RS-232 transceiver |
| Serial FPGA | DE-9 RS-232 | optional cross-connect | direct | core-owned real RS-232 |
| Linux debug | header | direct | no | 3.3 V TTL UART |
| FPGA debug | header | optional | direct | 3.3 V TTL UART where practical |
| MIDI IN | DIN-5 | yes | direct/selectable | isolated/standards-appropriate input |
| MIDI OUT | DIN-5 | yes | direct/selectable | standards-appropriate current loop |
| USB | USB-A/C as architecture assigns | direct | host-forwarded | keyboard/mouse/gamepad fallback |
| Ethernet | RJ45 | direct | host bridge | GbE baseline |
| Storage | microSD/eMMC/NVMe | direct | host/bridge | FPGA images/assets may be host-served |
| Expansion | RetroBus | bridge | direct | protected retro expansion interface |
| Debug | JTAG/test | host tooling | direct | development/manufacturing |

## Connector decisions

Rev-A baseline connector choices:
- 2 x DE-9 joystick;
- 2 x DE-9 RS-232 (one Linux, one FPGA);
- 2 x mini-DIN-6 PS/2 (keyboard, mouse);
- 2 x DIN-5 MIDI (IN, OUT);
- 2 x RCA/phono analog audio (L, R);
- HDMI;
- DE-15 analog RGBHV/VGA;
- RJ45 Ethernet;
- USB connectors according to the B1/board USB architecture;
- RetroBus expansion connector.

Composite and S-Video are not baseline Rev-A connectors. A future adapter/header may provide them.

## Ownership rule

A physical interface assigned as FPGA-direct must remain usable by a loaded machine core without Linux being in its real-time data path. Shared interfaces require explicit electrical arbitration/muxing so Linux and FPGA cannot drive the same bus simultaneously.

## Schematic gate

Before schematic capture is called complete:
1. allocate every connector to a sheet and power domain;
2. account for every FPGA GPIO and K1 peripheral used;
3. select all level translators/transceivers/muxes/protection;
4. check 5 V peripheral power budgets;
5. verify ECP5 bank voltages and pin availability;
6. verify B1/K1 peripheral mux availability;
7. perform mechanical edge-placement/keepout review.
