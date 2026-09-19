# M3.7 — RP2354B preliminary pin-function plan

Status: **authoritative function-plan baseline; package-ball binding remains for KiCad capture**

Source basis: Raspberry Pi RP2350 family documentation for the QFN-80/B variant. RP2354B uses the B-package I/O set with 48 user GPIO and eight analogue-capable GPIO.

This plan binds *GPIO numbers/functions*, not QFN package pad numbers. Package pads must be taken directly from the official RP2350/RP2354 package table/reference design during schematic capture.

## Allocation

| GPIO | Function | RetroSBC signal | Notes |
|---:|---|---|---|
| 0 | UART0 TX | MGMT_K1_UART_TX | hardware UART0 |
| 1 | UART0 RX | MGMT_K1_UART_RX | hardware UART0 |
| 4 | UART1 TX | MGMT_FPGA_UART_TX | hardware UART1 |
| 5 | UART1 RX | MGMT_FPGA_UART_RX | hardware UART1 |
| 8 | I2C0 SDA | MGMT_I2C_SDA | board management bus |
| 9 | I2C0 SCL | MGMT_I2C_SCL | board management bus |
| 16 | SPI0 RX | MGMT_FPGA_SPI_MISO | management SPI |
| 17 | SPI0 CSn | MGMT_FPGA_SPI_CS_N | management SPI |
| 18 | SPI0 SCK | MGMT_FPGA_SPI_SCLK | management SPI |
| 19 | SPI0 TX | MGMT_FPGA_SPI_MOSI | management SPI |
| 20 | SIO | MGMT_K1_RESET_N | safe default pull required |
| 21 | SIO | MGMT_K1_RECOVERY | voltage translation per B1 |
| 22 | SIO | MGMT_K1_STATUS | input |
| 23 | SIO | MGMT_K1_WDOG | direction finalized with B1 contract |
| 24 | SIO | MGMT_FPGA_RESET_N | safe default pull required |
| 25 | SIO | MGMT_FPGA_DONE | input |
| 26 | SIO | MGMT_FPGA_IRQ | input |
| 27 | SIO | MGMT_FPGA_WDOG | direction finalized with FPGA contract |
| 28 | PWM/SIO | MGMT_FAN_PWM | fan control |
| 29 | SIO | MGMT_FAN_TACH | tach input |
| 30 | SIO | MGMT_LED_STATUS | B-package GPIO |
| 31 | SIO | MGMT_LED_ERROR | B-package GPIO |
| 32 | SIO | MGMT_BUTTON_SERVICE_N | service/recovery button |
| 33 | SIO | MGMT_BOARD_REV0 | optional strap |
| 34 | SIO | MGMT_BOARD_REV1 | optional strap |
| 35 | SIO | MGMT_BOARD_REV2 | optional strap |
| 36 | SIO | MGMT_PWR_GOOD | aggregate/selected rail status |
| 40 | ADC/SIO | MGMT_ADC_INPUT | input supply sense |
| 41 | ADC/SIO | MGMT_ADC_5V | 5 V rail sense through divider |
| 42 | ADC/SIO | MGMT_ADC_3V3 | 3.3 V rail sense through divider |
| 43 | ADC/SIO | MGMT_ADC_THERMAL | analogue thermal/current channel |

## Reserved/spare

Keep GPIO 2-3, 6-7, 10-15, 37-39 and 44-47 uncommitted initially. This preserves:
- alternate UART/SPI/I2C mappings;
- additional ADC channels on 44-47;
- PIO experiments/service functions;
- late Rev-A fixes;
- manufacturing-test hooks.

Do not consume all spare pins during schematic cleanup.

## USB

Use the RP2354B dedicated USB D+/D- pins for the service USB device. Do not repurpose them as ordinary GPIO in Rev-A.

## SWD

Keep dedicated SWD access available for factory programming, debug and recovery.

## Binding rules

Before schematic lock:
1. verify every GPIO alternate function against the current official datasheet;
2. bind each GPIO to the exact QFN-80 package pad from the official pinout;
3. cross-check against the official minimal RP2350B KiCad design and current hardware-design guide;
4. validate RP2354B-specific flash-in-package power/decoupling requirements;
5. run an electrical review of every K1/B1 crossing before assigning translator parts;
6. retain safe passive reset defaults;
7. keep ADC dividers within ADC input range across worst-case rail tolerance.

## Rationale

The plan intentionally groups fixed peripherals into clean hardware blocks and leaves a substantial spare-pin pool. RP2354B has enough I/O that the management controller does not need aggressive pin multiplexing for normal operation. That improves debug visibility and makes Rev-A changes less risky.
