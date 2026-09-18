# RetroSBC Roadmap

## M0 — Foundation

- Define project identity and use cases.
- Define RISC-V + FPGA architecture.
- Establish open-hardware and maker-friendly design principles.
- Record preliminary compute-module and FPGA candidates.
- Define qualification gates before schematic freeze.
- Establish repository documentation structure.

**Exit criterion:** architecture and constraints are documented without pretending that unqualified component choices are final.

## M1 — Component and interface qualification — PASS (open procurement gates)

- Qualify SpacemiT B1/K1 sourcing and documentation.
- Confirm compute-module electrical and mechanical integration requirements.
- Qualify ECP5UM device/package, availability and open toolchain.
- Allocate host high-speed interfaces.
- Select initial host/FPGA bring-up interconnect.
- Define power tree and estimated rail budgets.
- Define voltage domains and level shifting.
- Produce initial pin/resource allocation.
- Decide storage, Ethernet and USB topology.
- Produce preliminary BOM and risk register.

## M2 — Schematic architecture — IN PROGRESS

- Capture hierarchical KiCad schematic.
- Compute-module interface.
- FPGA, configuration and clocks.
- Power tree and sequencing.
- Ethernet, USB, HDMI and storage.
- DB9, RS-232, MIDI and RetroBus.
- Debug/test interfaces.
- Electrical review and ERC.

## M3 — PCB Rev A

- Board stack-up and constraints.
- Placement and thermal review.
- High-speed routing.
- Power integrity review.
- DFM/DFT review.
- Generate fabrication and assembly outputs.

## M4 — Rev A bring-up

- Power-only validation.
- Compute-module boot.
- UART/debug validation.
- Linux baseline.
- FPGA configuration.
- Basic host/FPGA register transport.
- Ethernet/USB/storage validation.
- Retro-I/O electrical qualification.

## M5 — RetroCore

- Stable FPGA register/control ABI.
- Clock/reset infrastructure.
- Interrupts and DMA strategy.
- Core loading workflow.
- Initial simple CPU/peripheral demonstration.
- Open FPGA build flow.

## M6 — Host SDK

- retroctl CLI.
- Userspace library.
- FPGA discovery and management.
- Capture/control APIs.
- Automated test harness.
- Container-friendly SDK.

## M7 — Retro platform qualification

- Amiga development/runtime workflows.
- C64 development/runtime workflows.
- Atari development/runtime workflows.
- Serial/BBS/terminal workflows.
- Hardware-in-the-loop CI examples.
- Preservation/media workflows.

## M8 — Rev B / production candidate

- Incorporate Rev A findings.
- PCIe host/FPGA path if not already qualified.
- BOM optimization without compromising repairability.
- Compliance/pre-compliance review.
- Manufacturing test fixture.
- Production documentation.
