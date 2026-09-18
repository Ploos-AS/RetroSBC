# M2 — B1 Interface Binding

This is the Rev-A carrier allocation contract. Physical BGA ball numbers are not guessed; they are bound only from the current official B1 hardware design resources during schematic capture.

| B1 interface class | Rev-A use | Priority |
|---|---|---|
| module power/grounds | carrier power tree | mandatory |
| boot/recovery | switches/test pads | mandatory |
| debug UART | debug header/test pads | mandatory |
| SPI | FPGA control/bootstrap | mandatory |
| GPIO | FPGA IRQ/reset/status | mandatory |
| GMAC | Ethernet #1 PHY/magnetics | mandatory |
| HDMI 1.4 | Linux display | mandatory |
| eMMC | system storage | mandatory |
| SDIO | microSD / qualified storage path | mandatory |
| USB 2.0 | external USB/debug allocation | mandatory |
| USB3/PCIe2.1 x1 combo | FPGA high-speed candidate | high |
| PCIe2.1 x2 | M.2 NVMe | high |
| I2C | board management/EEPROM/RTC | high |
| UART | auxiliary serial | medium |
| PWM | fan/control | medium |
| CAN-FD/I2S/MIPI | expansion/future | reserved where economical |

## Binding rule

Every schematic net touching a B1 ball must cite the source table/page or machine-readable pin source used for that binding in the engineering notes. No pin assignment may be inferred from another K1 board.
