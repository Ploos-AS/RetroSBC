# M3.6 — Maker-first dual-domain policy

RetroSBC shall make **both compute domains first-class maker platforms**:

- Linux/K1 host
- ECP5 FPGA / RetroCore

Neither domain is merely an internal implementation detail.

## Common maker principles

Where electrically and mechanically practical, both domains shall provide:

- 2.54 mm through-hole headers;
- clearly printed signal names on the PCB;
- 3.3 V maker-facing logic;
- multiple GND pins distributed through headers;
- protected 3.3 V and 5 V power rails with documented current limits;
- GPIO usable as ordinary digital I/O;
- exposed serial/UART;
- SPI and I2C where available;
- PWM/timer-capable signals where available;
- interrupt-capable inputs where available;
- documented alternate functions;
- test points for important clocks/reset/power/control signals;
- simple command-line examples and diagnostic programs;
- pinout diagrams in Markdown/PDF documentation;
- stable symbolic signal names across PCB revisions where practical.

5 V supply pins never imply 5 V-tolerant logic.

## Linux/K1 maker domain

Target:
- 40-pin 2.54 mm header;
- >=16 GPIO mandatory target, 24+ preferred after B1 qualification;
- I2C, SPI, UART and PWM;
- maker-facing 3.3 V translation where K1/B1 signals are 1.8 V;
- Linux GPIO character-device/libgpiod examples;
- device-tree overlays or equivalent configuration examples for common buses;
- clearly documented Linux line names rather than requiring users to reason from raw SoC ball numbers.

## FPGA maker domain

Target:
- expose **32 maker GPIO** if exact BG381 placement permits;
- 24 remains acceptable only if mandatory platform functions consume constrained pins;
- 16 is the minimum without an explicit architecture review;
- 2.54 mm header(s);
- selected clock-capable pins exposed where practical;
- direct deterministic access from loaded FPGA cores;
- example Verilog modules for GPIO, PWM, SPI, I2C-style open-drain and interrupts/event capture;
- example LPF constraints generated from the final board pin map.

The dedicated FPGA microSD, DB9, PS/2, MIDI, serial, audio/video and RetroBus interfaces complement rather than replace general maker GPIO.

## Cross-domain experimentation

The PCB should reserve a small, explicitly controlled **K1 <-> FPGA maker link** in addition to the normal host-control interface where routing permits.

Useful capabilities:
- a few bidirectional GPIO/status lines;
- interrupt/event line;
- timestamp/trigger experiments;
- Linux-to-FPGA and FPGA-to-Linux educational examples.

Any cross-domain line must have defined ownership/direction or safe bidirectional buffering so two outputs cannot contend.

## Human-friendly board design

Silkscreen should make the board usable without repeatedly opening the schematic:
- header/domain names on both sides where possible;
- pin 1 obvious;
- power pins visually/textually distinguished;
- voltage printed beside maker headers;
- UART TX/RX direction labelled from the board perspective;
- I2C SDA/SCL and SPI SCLK/MOSI/MISO/CS named;
- no unexplained connector abbreviations.

## Documentation deliverables

Before Rev-A qualification:
1. Linux maker-header pinout.
2. FPGA maker-header pinout.
3. RetroBus pinout.
4. voltage/current table.
5. Linux GPIO/I2C/SPI/UART/PWM quick-start.
6. FPGA GPIO starter design.
7. cross-domain K1/FPGA demo.
8. loopback/self-test procedure usable during manufacturing and by makers.

This policy is subordinate only to electrical safety, signal integrity and mandatory platform functionality.
