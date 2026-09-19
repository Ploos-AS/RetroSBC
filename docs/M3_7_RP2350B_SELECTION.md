# M3.7 — Management MCU selection

Status: **Rev-A candidate lock**

## Selected candidate

**RP2350B (QFN-80), A4-or-later stepping**

RP2350B is the preferred RetroSBC management controller.

Why the B variant:
- 48 GPIO versus 30 on the A package;
- 8 analogue inputs;
- USB 1.1 host/device controller and PHY;
- 2 UART, 2 SPI, 2 I2C;
- 24 PWM channels;
- 12 PIO state machines;
- 520 KiB SRAM;
- Arm Cortex-M33 or Hazard3 RISC-V execution option;
- mature open C/C++ SDK and broad maker ecosystem.

The extra pins provide comfortable margin for dual debug UART, reset/recovery, fan/tach, telemetry, LEDs/buttons, manufacturing signals and future board-management functions.

## Stepping policy

Use **A4 or later** for production qualification. Earlier launch silicon is not the preferred Rev-A baseline.

## Firmware policy

Default firmware architecture should use the RP2350 open C/C++ SDK and remain MIT-licensed unless dependencies require otherwise.

The board may use the Hazard3 RISC-V cores where useful, aligning the management domain with RetroSBC's RISC-V educational character, but firmware must not depend on this as a marketing-only constraint if Arm execution gives a materially simpler qualification path.

## USB service target

One dedicated service USB connector should expose a composite device where practical:
- CDC ACM: Linux/K1 debug console;
- CDC ACM: FPGA debug console;
- CDC ACM or vendor-class: management shell/status;
- optional firmware update/recovery function.

Exact endpoint/interface count is a firmware qualification item.

## Initial resource budget

Reserve approximately:
- 2 UART channels or PIO UART equivalents for K1 + FPGA debug;
- USB device;
- I2C for telemetry/board management;
- SPI or PIO link to FPGA if required;
- K1 reset/recovery/status GPIO;
- FPGA reset/config/status GPIO;
- fan PWM + tach;
- status LEDs;
- service/user buttons;
- ADC inputs for selected voltage/current/temperature sensing;
- SWD/test/programming pads.

PIO may implement additional serial/control functions when fixed peripherals are exhausted.

## Electrical policy

Management logic is a 3.3 V domain unless a connected target requires translation. Do not rely on GPIO 5 V tolerance as a substitute for proper protection on externally accessible or cross-domain signals.

## Recovery

Provide:
- SWD pads/header;
- documented USB/boot recovery;
- hardware-accessible reset/boot selection;
- firmware image and reproducible build instructions.

## Remaining gates

Before final MPN/BOM lock:
1. verify A4-or-later sourcing/lifecycle;
2. select RP2350B vs RP2354B (integrated flash variant) based on BOM and recovery simplicity;
3. select external QSPI flash if RP2350B is retained;
4. lock service USB connector and ESD/power topology;
5. produce a concrete management pin map;
6. prototype composite USB dual-console operation;
7. qualify fan/telemetry/reset functions.
