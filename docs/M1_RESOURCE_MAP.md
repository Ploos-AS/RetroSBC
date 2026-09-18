# M1 Rev-A Resource Map

| Resource | Primary allocation | Fallback / note |
|---|---|---|
| B1 PCIe/USB3 combo x1 | FPGA PCIe | SPI control path remains mandatory |
| B1 PCIe x2 | M.2 NVMe | may initially route/use x1 |
| B1 GMAC | GbE #1 | required |
| Additional network resource | GbE #2 | preferred, qualify in M2 |
| B1 HDMI | Linux video | required |
| B1 USB3 | host USB | subject to combo-lane allocation |
| B1 USB2 | host USB/debug | required |
| B1 SPI | FPGA bootstrap/control | required |
| B1 GPIO | FPGA IRQ/reset/status | required |
| FPGA SERDES | host PCIe | one lane baseline |
| FPGA GPIO bank(s) | SDRAM | dedicated |
| FPGA GPIO | RetroBus | translated/protected |
| FPGA GPIO | DB9 x2 | buffered/protected |
| FPGA GPIO | MIDI | through MIDI interface circuitry |
| FPGA GPIO/UART | debug/RS-232 | through transceiver |
| FPGA SPI/config | configuration flash | required |
| FPGA JTAG | debug/programming | dedicated header/test pads |

## Rule

This is a logical allocation, not a PCB pinout. M2 must bind each function to B1 balls, FPGA banks/pins, voltage rails and connector pins after checking official pin/package data.
