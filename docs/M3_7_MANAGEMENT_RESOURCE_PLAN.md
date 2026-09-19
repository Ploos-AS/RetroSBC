# M3.7 — RP2354B management resource plan

Status: **logical allocation; exact GPIO numbers remain unbound until schematic capture**

This document allocates management functions before physical pin binding.

## Fixed peripheral allocation

| Resource | Function | Priority |
|---|---|---|
| USB device | service/debug composite USB | mandatory |
| UART0 | K1/B1 debug console | mandatory |
| UART1 | FPGA debug console | mandatory |
| I2C0 | board telemetry / sensors / board ID | mandatory |
| SPI0 | FPGA management/config assistance | preferred |
| PWM | fan control | mandatory |
| GPIO IRQ | fan tach | mandatory |
| ADC | voltage/current/temperature telemetry | preferred |
| SWD | factory programming/debug/recovery | mandatory |

PIO remains available for additional serial/control functions and must not be consumed without documenting why a fixed peripheral is insufficient.

## Logical GPIO allocation

Physical GPIO numbers are intentionally **UNBOUND**.

| Logical signal | Direction from MCU | Purpose |
|---|---|---|
| MGMT_K1_UART_TX | out | K1 debug RX |
| MGMT_K1_UART_RX | in | K1 debug TX |
| MGMT_FPGA_UART_TX | out | FPGA debug RX |
| MGMT_FPGA_UART_RX | in | FPGA debug TX |
| MGMT_K1_RESET_N | out/open-drain as qualified | K1 reset |
| MGMT_K1_RECOVERY | out | boot/recovery request |
| MGMT_K1_STATUS | in | host status |
| MGMT_FPGA_RESET_N | out | FPGA reset |
| MGMT_FPGA_DONE | in | FPGA configuration/status |
| MGMT_FPGA_IRQ | in | FPGA management event |
| MGMT_FPGA_SPI_SCLK | out | management SPI |
| MGMT_FPGA_SPI_MOSI | out | management SPI |
| MGMT_FPGA_SPI_MISO | in | management SPI |
| MGMT_FPGA_SPI_CS_N | out | management SPI |
| MGMT_I2C_SCL | bidirectional OD | sensors/ID |
| MGMT_I2C_SDA | bidirectional OD | sensors/ID |
| MGMT_FAN_PWM | out | fan control |
| MGMT_FAN_TACH | in | fan tachometer |
| MGMT_LED_STATUS | out | board status |
| MGMT_LED_ERROR | out | fault/recovery |
| MGMT_BUTTON_SERVICE_N | in | service/user button |
| MGMT_BOARD_REV0..2 | in | optional revision straps |
| MGMT_PWR_GOOD | in | aggregate/selected rail status |
| MGMT_K1_WDOG | in/out as qualified | watchdog handshake |
| MGMT_FPGA_WDOG | in/out as qualified | watchdog handshake |

## ADC budget

Prefer at least four telemetry channels:
1. input supply sense;
2. 5 V rail sense;
3. 3.3 V rail sense;
4. board/thermal analogue sensor or current monitor.

Digital I2C monitors may replace some ADC channels when they improve accuracy and simplify scaling.

## USB composite target

The service connector should enumerate without Linux:
- CDC ACM #1 — K1 console;
- CDC ACM #2 — FPGA console;
- management/status interface;
- firmware update/recovery path where practical.

The management interface may initially be CDC ACM for simplicity; a vendor-specific protocol can be added only when it provides clear value.

## Reset safety

Reset/recovery outputs must power up in benign states. Pull resistors define safe defaults before MCU firmware executes.

No MCU crash or reset may unintentionally hold K1 or FPGA permanently in reset without a hardware recovery route.

## Debug and factory access

Expose:
- SWDIO;
- SWCLK;
- MCU reset;
- GND;
- reference 3.3 V.

A compact tag-connect/test-pad pattern is preferred, with an optional 2.54 mm adapter footprint or documented adapter for maker/service use.

## Pin-binding rules

When physical pins are assigned:
- preserve USB pins required by the RP2354B package;
- use valid hardware-UART mappings for both consoles where practical;
- preserve ADC-capable GPIO for telemetry;
- keep SWD accessible;
- avoid assigning boot-sensitive signals to loads that can disturb recovery;
- document every alternate-function choice;
- leave spare GPIO/PIO capacity for Rev-A bring-up.

Exact RP2354B GPIO numbers must come from the authoritative Raspberry Pi RP2350/RP2354 documentation and the final schematic, not from assumptions in this logical plan.
