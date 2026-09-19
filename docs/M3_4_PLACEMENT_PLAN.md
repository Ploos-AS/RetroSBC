# M3.4 — Rev-A bank placement plan

Status: **logical bank placement before exact package-ball import**

Target: LFE5UM-85F-7BG381I.

Official Lattice package data gives 205 single-ended user I/O across banks 0/1/2/3/6/7/8. Banks 2/3/6/7 additionally carry the high-speed differential and DQS resources. Exact ball names remain gated on the official ECP5UM-85 Pinout CSV.

## Proposed allocation

| Resource | Preferred bank class | Reason |
|---|---|---|
| x16 SDR SDRAM | bank 2 + adjacent compatible resources | preserve DQS/high-speed-capable locality and coherent routing |
| FPGA video / clocks | bank 3 and/or 6 | high-speed/differential-capable resources available |
| Host SPI/control | bank 0/1 | ordinary low-speed I/O; avoid consuming DQS-capable pins |
| DB9 joystick x2 | bank 0/1 | low-speed protected digital I/O |
| PS/2 keyboard/mouse | bank 0/1 | low-speed open-drain via protected mux |
| FPGA RS-232 | bank 0/1 | low-speed through transceiver |
| MIDI | bank 0/1 | low-speed through MIDI circuitry |
| Audio I2S | bank 0/1/8 | low-speed digital audio |
| RetroBus | remaining bank 6/7 + ordinary-bank capacity | flexible structured expansion |
| Maker GPIO | bank 0/1/7/8 leftovers | last-priority flexible allocation |

## Capacity policy

The complete logical inventory currently includes 32 optional maker GPIO. We keep the 32-pin target through exact placement.

A GPIO reduction is allowed only when an exact, documented package constraint requires it. Reduction order is 32 -> 24 -> 16; going below 16 requires explicit Rev-A architecture review.

## High-speed reservation

SERDES and associated reference-clock resources are reserved before generic placement for the K1/B1 high-speed host path. They are not counted as maker GPIO.

HDMI/DVI implementation remains an architectural choice. If native FPGA differential output is used, the required pair/clock resources are reserved before RetroBus/GPIO. If an external transmitter is selected, its parallel/serial interface is budgeted explicitly instead.

## Exact-binding procedure

When the official pinout CSV is imported:
1. normalize vendor ball/bank/function records;
2. mark dedicated, configuration, JTAG, power, ground, NC and reserved balls unavailable;
3. reserve SERDES/refclock resources;
4. choose a coherent SDRAM group;
5. bind video/clocks;
6. bind fixed low-speed I/O;
7. bind RetroBus;
8. fill GPIO0..GPIO31 from remaining compatible balls;
9. run duplicate/bank/VCCIO/capability checks;
10. publish actual remaining spare-pin count.

No package ball is to be guessed.
