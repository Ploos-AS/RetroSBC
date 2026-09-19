# M3.4 — Authoritative ECP5 pin-source record

Status: **ECP5 source gate satisfied; exact binding next**

## Device

RetroSBC Rev-A FPGA target:

- Family: Lattice ECP5
- Device: LFE5UM-85F
- Package: caBGA381 / BG381
- Speed grade: -7
- Temperature target: Industrial
- SERDES: required

## Authoritative source

The authoritative source for exact package binding is the Lattice Semiconductor ECP5 product documentation/download set, specifically:

- **ECP5UM-85 Pinout**, CSV, version 1.0, dated 2015-02-11.
- **ECP5UM caBGA381 Migration**, CSV, version 1.0, dated 2015-02-11.
- **ECP5 and ECP5-5G Family Data Sheet**, FPGA-DS-02012.
- **ECP5 and ECP5-5G sysIO Usage Guide**, FPGA-TN-02032.
- **ECP5 and ECP5-5G SerDes/PCS Usage Guide**, FPGA-TN-02206.
- **ECP5 and ECP5-5G sysCONFIG User Guide**, FPGA-TN-02039.
- **Package Diagrams**, FPGA-DS-02053.

Vendor landing page:
https://www.latticesemi.com/Products/FPGAandCPLD/ECP5

## Verified package capacity

Lattice's current family table lists the LFE5UM-85 in 381 caBGA with **205 user I/O and 4 SERDES channels**. This replaces the earlier approximate '~205 I/O' planning assumption with a vendor-documented package capacity.

## Binding policy

Exact package-ball values shall be imported/derived only from the official Lattice pinout CSV and checked against the supporting package and sysIO documentation. A copied third-party board pinout is not an authoritative source.

The project shall preserve source metadata alongside any normalized binding table so that generated LPF/KiCad artifacts remain traceable to the vendor data.

## Next artifact

Create:
`hardware/fpga/lfe5um85-bg381-binding.csv`

Columns:
`signal,domain,package_ball,bank,vccio,io_standard,direction,capability,destination,translator,notes,source`

Initial assignment order:
1. configuration/JTAG/clocks;
2. SDR SDRAM;
3. SERDES/PCIe;
4. FPGA video/audio;
5. joystick/PS2/serial/MIDI;
6. host control/management;
7. RetroBus;
8. maker GPIO.

B1/K1 remains a separate source gate and must not be inferred from the ECP5 data.
