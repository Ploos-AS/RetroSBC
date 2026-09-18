# M2 Qualification

Status: **PARTIAL / PRE-CAPTURE**

## Completed

- [x] hierarchical schematic architecture defined
- [x] power-domain architecture defined
- [x] FPGA functional bank allocation defined
- [x] connector electrical contracts defined
- [x] protection and 5 V rules defined
- [x] SPI fallback retained independently of PCIe
- [x] debug/manufacturing-test requirements included

## Hard blockers before M2 PASS

- [ ] obtain/verify current B1 carrier design documentation
- [ ] freeze exact B1 SKU
- [ ] freeze exact ECP5UM ordering code/package/speed grade
- [ ] choose FPGA SDRAM MPN
- [ ] calculate rail load/current budget
- [ ] bind B1 interface pins
- [ ] bind FPGA physical pins/banks
- [ ] create real KiCad schematic
- [ ] run ERC
- [ ] run maker-friendly BOM/component-policy checks

## Result

**M2 is not yet PASS.** The pre-capture architecture is ready, but claiming schematic qualification before the official module/package constraints and actual KiCad ERC are verified would be premature.
