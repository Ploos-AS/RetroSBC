# M3.4 logical I/O inventory

The machine-readable binding CSV now expands the Rev-A logical signal inventory before physical package-ball assignment.

Current inventory contains **145 logical rows**, including **32 optional maker GPIO rows**. The GPIO rows are deliberately last-priority and may be reduced after exact bank, clock, SERDES, configuration and video constraints are applied.

The inventory models:
- x16 SDR SDRAM with 13 row/address lines, 2 bank lines, 2 DQM, command/control and clock;
- K1/B1 SPI control plus IRQ/reset;
- two 7-signal DB9 controller interfaces;
- PS/2 keyboard and mouse;
- FPGA RS-232 with RTS/CTS;
- MIDI IN/OUT;
- I2S-style stereo audio;
- 5:5:5 RGB plus HSYNC/VSYNC baseline analog video;
- 24-signal RetroBus baseline;
- up to 32 maker GPIO.

High-speed SERDES/PCIe and any TMDS/HDMI resources are intentionally not counted as generic LVCMOS GPIO rows. Configuration/JTAG/dedicated clock resources likewise require package-specific binding.

This is a **logical inventory**, not proof that every row can be simultaneously placed. Physical qualification occurs only after official BG381 capability/bank data is applied.
