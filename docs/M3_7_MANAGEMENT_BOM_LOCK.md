# M3.7 — Management component/BOM lock

Status: **pre-schematic component-class lock**

This stage freezes component classes before detailed schematic capture while avoiding invented MPNs where electrical qualification is still required.

The machine-readable baseline is `hardware/kicad/13_MANAGEMENT/management-bom.csv`.

## Locked now

- RP2354B QFN-80 is the preferred management MCU candidate.
- USB-C is USB 2.0 device/service only.
- Two 5.1 kΩ Rd CC resistors are required.
- Low-capacitance USB2 ESD protection is required.
- Local MCU decoupling and management-rail bulk capacitance are required.
- SWD/test access and labelled rail/reset test points are required.
- Ordinary maker-repairable LED/button/fan support components are preferred.

## Intentionally not MPN-locked

USB-C receptacle, ESD array, VBUS isolation/load switch, fan transistor, fan connector and ADC-divider values remain TBD until mechanical, power and electrical constraints are checked.

B1-facing translators remain outside this BOM lock until authoritative B1 voltage/domain information is available.

## Selection policy

When exact parts are chosen:
1. prefer parts stocked by multiple mainstream distributors;
2. avoid exotic packages where an ordinary package works;
3. prefer 0603/0805 passives where density permits;
4. provide alternates for supply-risk parts;
5. record lifecycle and assembly constraints;
6. preserve hand-rework access for service-domain components where practical.
