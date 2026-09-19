# M3.7 — Management power, reset and service-USB electrical contract

Status: **Rev-A schematic contract**

## Power domain

The RP2354B management controller belongs to the board's always-available low-power service domain when practical.

Goals:
- management can operate before Linux boots;
- management remains available during K1/FPGA reset;
- service USB can provide diagnostics during recovery;
- management does not back-power unpowered K1/FPGA domains.

Use explicit isolation/series protection where a management signal crosses into a domain that may be powered down.

## 3.3 V management rail

Provide a documented 3.3 V management rail with:
- local bulk and high-frequency decoupling per vendor guidance;
- test point;
- power-good/reset supervision as needed;
- current margin for MCU, status LEDs and board-management peripherals;
- no assumption that exported maker 3.3 V is the same protected current path.

Exact regulator/source topology remains part of the board power-tree lock.

## Service USB

Provide a dedicated USB service connector for the management MCU.

Preferred connector: USB-C receptacle in USB 2.0 device configuration.

Requirements:
- USB D+/D- routed as a controlled differential pair;
- ESD protection near connector;
- correct USB-C CC resistors for device/UFP behavior;
- no accidental host-role advertisement;
- VBUS sensing/power behavior documented;
- prevent USB VBUS from back-powering main board rails;
- connector shell/chassis strategy documented;
- optional common-mode choke footprint only if SI/EMI qualification justifies it.

The service port is not the main high-speed K1 USB port.

## Power-source behavior

Two supported states should be considered:
1. RetroSBC main power present: management powered from board service rail; USB used for data.
2. Main power absent, service USB attached: optional service-only management power may be allowed if isolation guarantees K1/FPGA/main rails are not back-powered.

Whether state 2 is enabled in Rev-A must be explicitly decided during schematic capture. If not enabled, the USB data interface simply remains unavailable without board power.

## Reset architecture

Safe hardware defaults are mandatory.

### MCU reset
Expose RP2354B reset and SWD access. A service/recovery button may invoke MCU boot/recovery through the documented vendor mechanism.

### K1 reset/recovery
MCU-controlled K1 reset/recovery signals require:
- passive pull state that permits normal boot before MCU firmware is active;
- open-drain/open-collector style control where electrically appropriate;
- voltage-domain translation if B1 signal levels require it;
- no direct 3.3 V drive into a lower-voltage B1 input.

### FPGA reset
MCU FPGA reset/config-assist signals require:
- passive default allowing a defined FPGA boot state;
- no contention with FPGA configuration circuitry;
- management reset must not glitch FPGA reset.

## Cross-domain protection

For every MCU <-> K1/FPGA signal document:
- source voltage;
- destination voltage;
- direction;
- power-off behavior;
- pull-up domain;
- whether series resistor/buffer/level shifter is used.

Do not use a generic bidirectional level translator blindly for reset, clocks, SPI or UART.

## Watchdog behavior

Watchdogs must fail predictably:
- firmware crash may request/reset a target only according to an explicit policy;
- no infinite reset loop without a recovery override;
- service/recovery mode can disable automatic target reset;
- reset cause should be logged/readable where practical.

## LEDs and button

Minimum management UI:
- one status LED;
- one error/recovery indication (may be a second LED or multi-colour device);
- one service/recovery button.

LEDs must not consume boot-sensitive pins without qualification.

## Test points

Rev-A should expose labelled test points for:
- MGMT_3V3;
- GND;
- MCU reset;
- USB D+/D- where practical for bring-up;
- K1 reset/recovery;
- FPGA reset/status;
- management I2C;
- both debug UART TX/RX paths.

## Qualification

Before M3.7 electrical PASS:
- service USB enumerates reliably;
- no back-powering is measured in supported power states;
- MCU recovery works with K1/FPGA non-functional;
- K1 and FPGA boot normally if management firmware is absent/corrupt where architecture permits;
- reset defaults and voltage levels are measured;
- ESD/protection population is documented;
- current draw of service-only and normal modes is recorded.
