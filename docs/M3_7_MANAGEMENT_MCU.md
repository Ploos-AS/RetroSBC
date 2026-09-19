# M3.7 — Board management controller

Status: **Rev-A preferred subsystem; footprint/routing should be reserved**

A small independent management MCU makes RetroSBC substantially more maker-friendly and easier to recover, manufacture and qualify.

## Responsibilities

The management controller may provide:
- board power/reset sequencing assistance;
- K1 reset and recovery/boot-mode control;
- FPGA reset/configuration assistance;
- fan PWM and tachometer monitoring;
- board temperature/voltage/current telemetry;
- board-revision/identity access;
- USB-to-UART bridge functions for Linux and FPGA debug;
- manufacturing/self-test coordination;
- watchdog/recovery support;
- status LEDs and user/service button handling.

It must **not** become a mandatory real-time path for normal FPGA retro I/O.

## Maker-facing behavior

A maker should be able to connect one USB cable and obtain a useful service/debug interface even when Linux does not boot.

Preferred USB service functions:
- Linux debug UART;
- FPGA debug UART;
- management console;
- optional firmware-update interface.

A composite USB device is preferred if the selected MCU and firmware stack support it cleanly.

## Interfaces

Candidate internal connections:
- MCU <-> K1/B1: UART, reset/recovery, I2C/SMBus-style management signals.
- MCU <-> FPGA: UART/SPI or low-speed control, reset/status.
- MCU <-> board sensors: I2C/ADC/tach/PWM.
- MCU <-> USB-C/service connector: USB device.

All ownership and reset behavior must be deterministic. The MCU must not unexpectedly drive maker GPIO or core-owned interfaces.

## Open implementation

Management firmware is software and follows the Ploos-AS software licensing policy (MIT unless inherited constraints require otherwise).

Firmware source, build instructions, update/recovery procedure and protocol documentation must be in the repository.

Use an MCU with a mature open toolchain. Avoid a design that requires proprietary IDE-only development.

## Failure policy

RetroSBC should degrade gracefully:
- FPGA direct I/O remains functional without management firmware after normal configuration.
- Linux normal operation should not depend on a continuously healthy management MCU unless required for safe power sequencing.
- a failed firmware update must have a documented recovery mechanism.
- hardware reset/recovery paths remain available.

## Qualification gate

Before selecting the exact MCU:
1. count required UART/SPI/I2C/ADC/PWM/USB resources;
2. verify open compiler/debug/programming support;
3. define voltage domains;
4. define bootloader/update path;
5. define factory programming header/test pads;
6. estimate BOM/PCB impact;
7. confirm service USB topology;
8. decide whether the MCU is fitted on every Rev-A board or is DNI-capable.

Reserve schematic/PCB space now so the decision does not require a major redesign later.
