# M3.5 — FPGA microSD electrical contract

Rev-A reserves **7 FPGA I/O** for a dedicated microSD slot:

- CLK
- CMD
- DAT0
- DAT1
- DAT2
- DAT3
- card detect

This supports both the mandatory SPI bring-up path and the preferred native 4-bit SD path without changing the PCB.

In SPI mode the conventional mapping is:
- CLK -> CLK
- CMD -> MOSI
- DAT0 -> MISO
- DAT3 -> CS

DAT1/DAT2 remain available for native 4-bit mode.

## Pin-budget impact

The previous logical inventory contained 145 rows including 32 optional maker GPIO. Adding the dedicated FPGA microSD interface raises it to **152 logical rows**.

Against the package-level 205-user-I/O figure, raw arithmetic headroom becomes **53 positions** before package/bank/configuration/high-speed constraints.

Therefore the 32 maker-GPIO target remains in the design. No GPIO is removed at this stage.

## Electrical requirements

- 3.3 V SD power and I/O baseline.
- local decoupling.
- ESD protection at the socket.
- card detect preferred and reserved.
- series damping footprints on clock/command/data where signal-integrity review recommends them.
- FPGA slot electrically independent of the K1/Linux microSD slot.
- no Linux arbitration required for FPGA access.

Exact balls remain UNBOUND until the authoritative Lattice pinout is imported.
