# M2 — Rev-A Power Tree

This is the electrical planning contract. Exact regulator MPNs and current limits require B1 carrier documentation and load-budget verification before schematic freeze.

## Inputs

Primary: USB-C power input with negotiated high-current capability.

Development alternative: protected DC/barrel input, if retained after mechanical review.

Inputs must not be hard-paralleled. Reverse-current/backfeed protection is required.

## Planned rails

```text
POWER INPUT
   |
 protection / eFuse / TVS
   |
 main intermediate rail
   +--> B1 module input
   +--> +5V_PERIPH
   |      +--> USB VBUS switching
   |      +--> DB9/RetroBus protected 5 V
   |      +--> MIDI/other 5 V loads if required
   |
   +--> +3V3
   |      +--> FPGA I/O banks as assigned
   |      +--> configuration flash
   |      +--> level translators
   |      +--> board management/peripherals
   |
   +--> FPGA core/aux rails
          +--> VCC
          +--> VCCAUX
          +--> SERDES rails where required
```

The selected ECP5UM implementation must follow the vendor power-up, decoupling and SERDES rail requirements.

## Instrumentation

Provide:
- input-current measurement option;
- test points for every generated rail;
- regulator enable/status access where useful;
- clearly labelled grounds;
- thermal test points near major regulators;
- optional current-shunt footprints on development-critical rails.

## Safety

External 5 V is treated as a separate peripheral domain. RetroBus and DB9 power require current limiting or a resettable/protected switch rather than an unrestricted connection to the main 5 V rail.

## Open gate

No regulator MPN is frozen until B1 peak/transient current requirements and FPGA/SDRAM load estimates are verified.
