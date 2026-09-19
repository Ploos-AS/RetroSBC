# M3.4 — LFE5UM-85 caBGA381 bank capacity

Status: **vendor data reconciled**

The Lattice ECP5 family data sheet lists **205 total single-ended user I/O** for LFE5UM/LFE5UM5G-85 in the 381 caBGA package.

The user-I/O count is distributed across more banks than the earlier planning note implied:

| Bank | Single-ended user I/O |
|---|---:|
| 0 | 27 |
| 1 | 33 |
| 2 | 34 |
| 3 | 33 |
| 4 | 0 |
| 6 | 33 |
| 7 | 32 |
| 8 | 13 |
| **Total** | **205** |

High-speed differential I/O and DQS capabilities are concentrated in banks 2, 3, 6 and 7. That does **not** mean banks 0, 1 and 8 have no ordinary user I/O.

## Design consequence

The Rev-A placement strategy is updated:

- Banks 2/3/6/7 are protected for interfaces that benefit from their differential/DQS capabilities, especially SDRAM and video/high-speed-capable I/O.
- Banks 0/1 and suitable bank-8 pins become valuable candidates for ordinary control, retro I/O and maker GPIO, subject to configuration/shared-function restrictions in the exact pinout.
- SERDES remains a separate dedicated resource.
- No exact ball is assigned until the official ECP5UM-85 pinout CSV is normalized.

This correction improves the flexibility of the 32-pin maker-GPIO target rather than reducing it.

Source authority: Lattice ECP5/ECP5-5G Family Data Sheet FPGA-DS-02012 and the official ECP5UM-85 Pinout CSV.
