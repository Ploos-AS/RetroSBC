# M3.7 — Management schematic capture checklist

Status: **ready for KiCad capture**

This checklist converts the locked RP2354B management architecture into a reviewable schematic sheet without guessing package pads or electrical details.

## Sheet

Create/maintain the management circuitry as a dedicated hierarchical block, proposed name:

`13_MANAGEMENT`

Top-level ports should use the stable logical names already defined in the M3.7 resource and pin plans.

## MCU core

Capture the RP2354B QFN-80 from the authoritative current package documentation.

Required:
- every supply and ground pin;
- vendor-recommended local decoupling;
- required regulator/core-support components;
- integrated-flash-specific requirements;
- crystal/clock only if the final design requires it;
- RUN/reset network;
- SWDIO/SWCLK access;
- labelled test points.

Do not copy RP2350A/package-A pin numbers into the B-package design.

## USB-C service interface

Capture:
- USB-C receptacle;
- D+/D- routing nets;
- CC1/CC2 device/UFP resistors;
- low-capacitance ESD;
- VBUS sense/isolation;
- shield treatment;
- optional EMI footprint if justified;
- explicit no-back-power path.

## K1/B1 interface

Capture logical nets:
- MGMT_K1_UART_TX/RX;
- MGMT_K1_RESET_N;
- MGMT_K1_RECOVERY;
- MGMT_K1_STATUS;
- MGMT_K1_WDOG.

Each net must carry an annotation/table reference for:
- B1 voltage;
- direction;
- safe power-off state;
- translation/buffering choice.

Leave translator MPN as TBD until B1 authoritative electrical data is available.

## FPGA interface

Capture:
- MGMT_FPGA_UART_TX/RX;
- management SPI SCLK/MOSI/MISO/CS_N;
- MGMT_FPGA_RESET_N;
- MGMT_FPGA_DONE;
- MGMT_FPGA_IRQ;
- MGMT_FPGA_WDOG.

Use simple series-resistor footprints where they aid bring-up without compromising function. Reset/status defaults must remain deterministic before firmware starts.

## Telemetry and cooling

Capture:
- management I2C;
- fan PWM;
- fan tach;
- ADC divider/filter footprints for input, 5 V and 3.3 V monitoring;
- fourth analogue telemetry channel;
- optional digital current/voltage monitor footprint if later selected.

Divider values are not locked until ADC limits and rail tolerances are reviewed.

## Human interface

Capture:
- status LED;
- error/recovery LED;
- service/recovery button.

Prefer replaceable ordinary components and avoid unnecessarily tiny packages.

## Factory/service header

Provide SWD and recovery access through test pads/tag-connect-style footprint. A maker-friendly adapter must be documented; direct 2.54 mm service access may be added if board area permits.

## ERC policy

No-connect markers must be intentional and reviewed.

Do not suppress ERC globally to hide:
- unpowered domains;
- output contention;
- missing power pins;
- reset-net conflicts.

Document unavoidable exceptions locally.

## Capture completion gate

The management sheet is capture-complete only when:
1. RP2354B package pads are checked against authoritative documentation;
2. power/decoupling is complete;
3. USB-C service circuit is electrically reviewable;
4. all logical M3.7 signals are represented;
5. B1-unknown crossings are visibly marked TBD rather than guessed;
6. test/recovery access exists;
7. ERC passes or every exception is documented;
8. schematic PDF/SVG can be generated for review.

Physical PCB placement/routing is a later gate.
