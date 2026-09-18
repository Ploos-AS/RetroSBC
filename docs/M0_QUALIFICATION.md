# M0 Qualification

## Scope

M0 qualifies the repository foundation and architecture documentation only. It does **not** qualify electrical hardware or production component choices.

## Required artifacts

- [x] Project README
- [x] Architecture document
- [x] Hardware baseline
- [x] RetroCore concept
- [x] RetroBus concept
- [x] Roadmap
- [x] Contribution policy
- [x] Repository hygiene
- [x] CERN-OHL-P-2.0 hardware license
- [x] MIT software license
- [x] Vendor-neutral MANUFACTURING.md and ORDERING.md
- [x] Fail-closed manufacturing workflow

## M0 decisions

- Product name: **RetroSBC**
- Product class: open RISC-V + FPGA retro development platform
- Leading compute candidate: SpacemiT K1/B1
- Leading FPGA candidate: Lattice ECP5UM 45K class
- Carrier-board approach preferred over routing LPDDR on Rev A
- RetroCore names the FPGA framework
- RetroBus names the expansion-interface concept
- Hardware-in-the-loop testing is a first-class architectural requirement
- Proprietary retro ROM/OS assets must not be committed

## Deferred to M1

- supplier/MOQ/lifecycle qualification;
- exact B1 module variant and RAM;
- exact FPGA ordering code/package/speed grade;
- FPGA resource and bank allocation;
- host/FPGA transport;
- PCIe lane allocation;
- power tree;
- voltage translation;
- detailed connector pinouts;
- thermal design;
- BOM estimate and risk register.

## Result

**M0: PASS**

The repository contains enough architecture and constraint information to begin M1 feasibility and component qualification without prematurely freezing the schematic.
