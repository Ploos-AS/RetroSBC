# RetroSBC

**An open RISC-V + FPGA development platform for retro computing.**

RetroSBC is designed as a bridge between modern Linux development and classic computer hardware, with first-class support for FPGA experimentation, retro I/O, software qualification, hardware-in-the-loop testing, education, BBS/terminal use, and preservation workflows.

> **Status:** M3.7 — Rev A schematic capture and management subsystem qualification in progress.
>
> M0 and M1 are complete. M2 architecture/interface work has advanced into concrete Rev A KiCad capture. The current gate is materializing and qualifying the RP2354B management power network in KiCad; full-board ERC, PCB routing and physical Rev A qualification have not yet been claimed.

## Current Rev A baseline

- **Compute:** SpacemiT K1-class RISC-V via the B1 compute module
- **Memory:** 8 GiB LPDDR4X baseline
- **FPGA:** Lattice ECP5UM 45K-class baseline
- **Management:** RP2354B QFN-80, with project-local generated symbol/footprint and machine-checked package bindings
- **PCB:** carrier-board architecture, expected to require at least six layers
- **Storage:** microSD and eMMC; PCIe/NVMe planned
- **Networking:** Gigabit Ethernet; dual Ethernet preferred
- **Modern I/O:** USB 3, USB 2 and HDMI
- **Retro I/O:** two DB9 ports, real RS-232, MIDI and RetroBus
- **Debug:** host UART/JTAG, FPGA JTAG, management SWD, reset/boot controls and test points

These remain engineering baselines until their corresponding schematic, ERC, PCB and physical qualification gates pass.

## Architecture

```text
RISC-V compute module
        |
   Linux / SDK / CI
        |
 host/FPGA transport
        |
      FPGA
   RetroCore
    /      \
retro I/O  RetroBus
```

See `docs/ARCHITECTURE.md`, `docs/HARDWARE.md`, `docs/RETROCORE.md`, `docs/RETROBUS.md` and `ROADMAP.md`.

## Design principles

- Purpose-built for retro development rather than a generic SBC.
- Open hardware and open software by default.
- Maker-friendly, inspectable and repairable.
- Hardware-in-the-loop qualification is a first-class requirement.
- Electrical/package facts are source-gated and machine-checked where practical; unresolved values remain explicit rather than guessed.
- No proprietary retro ROM or OS images are committed to the repository.

## Manufacturing

For fabrication files, release-package conventions, manufacturer choices, and funding/affiliate disclosure, see [MANUFACTURING.md](MANUFACTURING.md). Released hardware remains vendor-neutral and may be manufactured by any suitable PCB manufacturer. For project-specific PCB ordering options, see [ORDERING.md](ORDERING.md).

Manufacturing releases are qualified by `.github/workflows/manufacturing.yml`. The workflow intentionally fails closed until a single qualified KiCad PCB exists.

## License

Hardware design materials — including schematics, PCB layouts, manufacturing files, and HDL/RTL that describes hardware — are licensed under the **CERN Open Hardware Licence Version 2 - Permissive (CERN-OHL-P-2.0)**. See [LICENSE-HARDWARE](LICENSE-HARDWARE).

Software — including firmware, drivers, host tools and other executable code unless explicitly stated otherwise — is licensed under the **MIT License**. See [LICENSE-SOFTWARE](LICENSE-SOFTWARE).

Files that incorporate third-party material remain subject to their respective licences and notices.
