# M2 — Rev-A Component Matrix

| Function | Baseline | Lock |
|---|---|---|
| Compute | SpacemiT B1/K1, 8 GiB target | family locked; SKU open |
| FPGA | LFE5UM-85F-7BG381I | design baseline locked |
| FPGA RAM | >=256 Mbit x16 3.3 V SDR SDRAM | class locked; MPN open |
| FPGA config | 128 Mbit 3.3 V SPI/QSPI NOR | class locked; MPN open |
| FPGA core regulator | 1.1 V | rail locked; MPN open |
| FPGA aux regulator | 2.5 V | rail locked; MPN open |
| Logic/peripheral | 3.3 V | rail locked; MPN open |
| peripheral power | protected 5 V | rail locked; switch/eFuse open |
| RS-232 | MAX3232-class | class locked; MPN open |
| MIDI | compliant isolated/current-loop circuitry | architecture locked |
| Ethernet | GbE PHY + magnetics | interface locked; MPN open |
| RTC | I2C RTC footprint | optional/high priority |
| board identity | I2C EEPROM | required |
| FPGA clock | low-jitter oscillator | class locked; frequency/MPN open |
| USB-C input | PD/power-path controller | architecture locked; MPN open |

## Selection rule

Production MPNs require lifecycle/availability review and should have a realistic substitute or documented single-source rationale. Maker-friendly sourcing and hand-repair considerations remain part of selection, but high-speed/BGA components are accepted where the architecture requires them.
