# M3.6 — Linux/K1 maker GPIO header

Status: **Rev-A requirement; exact B1 exposure pending**

RetroSBC shall expose a maker-friendly Linux-side expansion header in addition to the FPGA GPIO header and RetroBus.

## K1 capability basis

The K1 SoC provides 128 GPIO controller lines in four groups of 32. The SoC also provides multiple UART, I2C, SPI and PWM controllers. Many physical pads are multiplexed and most K1 I/O is 1.8 V; only a subset is 1.8/3.3 V capable. Therefore the SoC's 128-GPIO controller count must **not** be interpreted as 128 freely available 3.3 V header pins.

The actual header width is gated by what the B1 module exposes after mandatory RetroSBC functions are assigned.

## Rev-A target

Target a **40-pin, 2.54 mm through-hole Linux maker header** if B1 routing permits, with a Raspberry-Pi-like physical convenience but **not pin-compatible unless explicitly documented and qualified**.

Desired header services:
- at least 16 general-purpose Linux GPIO;
- target 24+ usable GPIO/alternate-function signals where practical;
- 2 x I2C buses or one I2C plus reserved alternate pair;
- 1 x SPI bus with at least two chip-selects where available;
- 1-2 UARTs;
- 2+ PWM-capable signals;
- 3.3 V;
- protected 5 V power;
- multiple GND pins.

## Voltage policy

Header-facing digital I/O should be **3.3 V logic** for maker friendliness.

Because most K1 GPIO pads are 1.8 V, RetroSBC shall use appropriate bidirectional/uni-directional level translation or buffering for header signals that originate from 1.8 V B1/K1 I/O.

5 V power on the header does not imply 5 V-tolerant GPIO.

## Domain separation

RetroSBC exposes three complementary expansion domains:
1. **Linux GPIO header** — Linux drivers, sensors, automation, SPI/I2C/UART/PWM.
2. **FPGA GPIO header** — direct deterministic FPGA/core I/O and HIL.
3. **RetroBus** — structured protected retro expansion.

Linux and FPGA GPIO shall be clearly labelled and electrically distinct. Optional internal bridges may connect domains under controlled ownership, but no shared output shall permit contention.

## Qualification gates

Before schematic lock:
1. obtain authoritative B1 module pinout/mux table;
2. subtract eMMC, SD, PCIe/NVMe, Ethernet, HDMI, USB, Linux RS-232, FPGA-control and board-management functions;
3. identify exposed 1.8 V vs 1.8/3.3 V pads;
4. select level translators/buffers;
5. lock actual GPIO/I2C/SPI/UART/PWM header mapping;
6. publish Linux pin names and device-tree mappings;
7. validate interrupt-capable GPIO where relevant;
8. confirm power/current limits.

The 40-pin connector is a mechanical target; useful, correctly translated signals take priority over cosmetic compatibility with another SBC.
