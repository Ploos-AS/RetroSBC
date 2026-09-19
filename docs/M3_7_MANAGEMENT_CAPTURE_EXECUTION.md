# M3.7 management capture execution checklist

This file turns the source-lock and architecture documents into a concrete completion gate for the actual KiCad sheet.

The official Raspberry Pi Product Information Portal currently lists the RP2350 hardware-design guide and RP2350B Minimal KiCad design as the authoritative current references. The repository records their source dates in `rp2354b-source-lock.csv`.

## Rule

Documentation milestones do not advance M3.7 to CAPTURE PASS. Only the actual `13_MANAGEMENT.kicad_sch` plus this checklist can do that.

Each PENDING item must be replaced by BOUND/IMPLEMENTED/VERIFIED with the evidence used. Values and topology for the RP235x SMPS/power island must come from the official current reference design, not memory or an RP2040/Pico design.

## Immediate capture order

1. U_MGMT full QFN-80 symbol and all non-GPIO pins.
2. power/ground/exposed-pad and SMPS support network.
3. decoupling and MGMT_3V3 test/bulk network.
4. RUN + SWD recovery.
5. USB D+/D-, CC and ESD.
6. VBUS sense/isolation.
7. management GPIO interfaces already bound in `rp2354b-binding.csv`.
8. ERC and side-by-side reference review.

Machine-readable state: `management-capture-checklist.csv`.
