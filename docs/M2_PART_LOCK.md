# M2 — Part Lock and Datasheet Gate

Status: **PARTIAL LOCK**

## Compute

Rev-A schematic target remains **SpacemiT B1** with K1 and LPDDR4X integrated in the 23 x 33 mm BGA module.

Verified interface classes from the current B1 datasheet include HDMI 1.4, SDIO 3.0, eMMC 5.1, QSPI, SPI, I2S, I2C, CAN-FD, PWM, UART, USB 2.0, USB 3.0/PCIe 2.1 x1 combo, PCIe 2.1 x2 and GMAC.

The exact B1 memory/order code remains a procurement gate; Rev A targets 8 GiB.

## FPGA

Rev-A planning device is locked to:

**LFE5UM-45F-7BG381I**

Rationale:
- ECP5UM, not ECP5U, preserves SERDES;
- 45K class is the established capacity baseline;
- BG381 provides substantially more board I/O flexibility than the smallest packages;
- industrial grade is appropriate for a development platform;
- -7 is a balanced speed-grade baseline rather than assuming the fastest grade is necessary.

This ordering code is a design baseline until distributor availability is checked immediately before BOM/release freeze. A footprint-compatible speed/temperature substitution may be permitted only if electrical/timing constraints remain satisfied.

## Authoritative design inputs

Before physical pin binding/capture, use:
- current ECP5/ECP5-5G family datasheet;
- ECP5UM-45 pinout;
- BG381 package drawing;
- ECP5 hardware checklist;
- sysIO guide;
- sysCONFIG guide;
- SERDES/PCS guide;
- PCIe guidance where PCIe is populated;
- current SpacemiT B1 datasheet and carrier hardware design resources.

Copies of vendor-controlled documents should not be vendored into the repository unless redistribution terms clearly permit it; record document identifiers/revisions instead.

## Still open

- exact B1 8 GiB order code;
- FPGA SDRAM MPN;
- regulator MPNs;
- clock oscillator MPNs;
- connector MPNs;
- current distributor/second-source status.

These are resolved through the project component policy before production qualification.
