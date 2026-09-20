# RetroSBC Roadmap

## Current status

**Active engineering milestone: M3.7 — Rev A schematic capture / management subsystem qualification.**

The original milestone sequence below remains the project-level roadmap. Development has crossed the M2/M3 boundary iteratively: architecture and interface contracts are being converted into real KiCad Rev A artifacts before PCB placement/routing begins. A milestone is not considered physically qualified merely because its contracts, generators or CI checks exist.

Current M3.7 gate: materialize the machine-checked RP2354B management power network as actual KiCad symbols/wiring, then obtain schematic/netlist/visual review and ERC qualification. Full-board PCB Rev A routing has not started.

## M0 — Foundation — PASS

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

## M2 — Schematic architecture — ADVANCED / feeding M3 capture

- Hierarchical KiCad structure and subsystem contracts established.
- Compute-module interface work.
- FPGA device/package, configuration, clocks and bank/resource planning.
- Power-tree and sequencing contracts.
- Ethernet, USB, HDMI and storage architecture.
- DB9, RS-232, MIDI and RetroBus contracts.
- Debug/test interfaces.
- Electrical review gates and ERC requirements.

Remaining M2-class work is completed alongside concrete Rev A capture rather than as a separate paper-design phase.

## M3 — PCB Rev A — IN PROGRESS (M3.7 schematic-capture gate)

Current M3.7 work includes:

- RP2354B QFN-80 authoritative pin transcription and semantic binding validation.
- Deterministically generated project-local RP2354B KiCad symbol.
- Explicit exposed GND-pad modelling.
- Source-derived QFN-80 footprint dimensions, deterministic footprint generation and structural validation.
- Management USB pad/termination correction against authoritative source data.
- Management power-network contract and machine-checked capture netlist.
- CI gates for package bindings, generated artifacts and power connectivity.
- **Next gate:** materialize management power as real KiCad objects/wiring and obtain ERC/netlist/visual-review PASS.

PCB Rev A work still to follow:

- Complete full-board schematic capture and ERC.
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
