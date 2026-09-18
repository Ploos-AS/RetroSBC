# M1 — Component and Interface Qualification

Status: **PASS WITH OPEN PROCUREMENT GATE**

M1 converts the M0 concept into a concrete Rev-A engineering baseline. It does not authorize PCB production.

## Compute module

**Baseline: SpacemiT B1 / K1, 8 GiB LPDDR4X target.**

The B1 integrates K1, LPDDR4X and passive components in a 23 x 33 mm BGA module and exposes HDMI 1.4, eMMC 5.1, SDIO 3.0, USB 2.0, USB 3.0 combo/PCIe 2.1 x1, PCIe 2.1 x2, GMAC, QSPI, SPI, I2C, UART, PWM and CAN-FD.

Decision: retain B1 for Rev-A schematic planning because it avoids direct LPDDR routing.

Gate before schematic freeze: verify purchasable SKU, prototype quantity, lead time, lifecycle statement and current hardware-design package.

## FPGA

**Baseline: Lattice LFE5UM-45F, SERDES-capable variant.**

Target package: **BG381** for Rev-A planning. Do not substitute LFE5U-45F: the U variant lacks SERDES.

Resources used as planning baseline:
- ~44K LUTs
- 108 x 18-Kbit sysMEM blocks / 1,944 Kbit embedded RAM
- 72 18x18 multipliers
- up to four SERDES channels in the 45K UM family

BG381 is selected provisionally over the smaller package to preserve I/O margin for RetroBus, DB9, external memory, debug and future video work.

## Host/FPGA transport

Rev A uses two tiers:

1. **Bring-up/control path:** SPI + interrupt/reset/status GPIO.
2. **High-performance target:** one PCIe 2.x lane between K1/B1 and ECP5UM.

The RetroCore host ABI must remain transport-independent. PCIe failure therefore does not block initial board bring-up.

## PCIe allocation

Planning allocation:
- B1 PCIe x2: reserve for M.2 NVMe (x1 electrically is acceptable for initial implementation; preserve routing options).
- B1 USB3/PCIe combo x1: candidate FPGA PCIe link.

Exact mux/PHY constraints must be checked against the B1 design guide before schematic freeze.

## FPGA external memory

ECP5 embedded RAM is insufficient for full-machine retro cores. Rev A therefore requires dedicated FPGA memory.

Baseline: **32 MiB or greater SDR SDRAM** on a dedicated FPGA bus, chosen for open-controller support and deterministic timing. M2 must select an actively available part and confirm bandwidth against planned Amiga/Atari/C64-class cores. PSRAM/HyperRAM may be evaluated but must not replace SDRAM merely to reduce pin count without qualification.

## Voltage domains and protection

- No raw 5 V retro signal may connect directly to B1 or FPGA GPIO.
- DB9 and RetroBus require explicit level translation/buffering/protection where 5 V interaction is possible.
- External connectors require ESD/TVS review.
- RS-232 uses a proper transceiver (MAX3232-class or qualified equivalent).
- MIDI uses standards-appropriate current-loop input/output circuitry.
- FPGA bank voltages are assigned only after the final pin map.

## Rev-A interface budget

Required:
- B1 compute module
- ECP5UM-45F
- FPGA configuration flash
- dedicated FPGA SDRAM
- GbE
- microSD
- eMMC support from module/carrier as applicable
- USB 3 + USB 2
- HDMI from K1
- 2 x DB9
- RS-232
- MIDI IN/OUT
- RetroBus
- FPGA JTAG
- K1 debug UART/JTAG where exposed
- boot/recovery/reset controls
- board identity EEPROM
- RTC footprint
- fan header / thermal provision
- manufacturing test pads

Preferred, resource permitting:
- second GbE
- M.2 NVMe
- FPGA-generated video output
- onboard management/debug MCU

## Board philosophy

Maker friendly first. The board may be larger than Raspberry-Pi format. DB9, DIN, RJ45 and debug access must not be compromised merely to hit a small outline.

## M1 gates

PASS:
- architecture remains feasible;
- compute module removes DDR routing from carrier;
- SERDES-capable FPGA identified;
- fallback SPI control path defined;
- external FPGA RAM requirement recognized;
- 5 V translation/protection requirement defined;
- interface priorities defined.

OPEN:
- B1 commercial sourcing/lifecycle;
- exact B1 ordering code;
- exact ECP5UM speed grade;
- final FPGA SDRAM part;
- exact PCIe mux/resource validation;
- final power tree and rail current budget.

These OPEN items become hard gates in M2 before schematic freeze.
