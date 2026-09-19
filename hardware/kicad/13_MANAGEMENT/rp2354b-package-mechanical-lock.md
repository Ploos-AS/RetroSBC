# M3.7 — RP2354B QFN-80 mechanical package lock

Status: **authoritative package facts locked; land-pattern implementation pending**

Source basis: current Raspberry Pi RP2350 datasheet and Hardware design with RP2350.

## Locked facts

- RP2354B uses the B-family QFN-80 package.
- Package body is 10 mm × 10 mm.
- Perimeter lead pitch is 0.4 mm.
- The QFN-80 variant uses the reduced exposed-pad geometry shown in the official package drawing.
- The centre exposed pad is GND and is the package's single external ground connection.
- RP2354B shares the QFN-80 package family with RP2350B; the integrated-flash distinction does not justify inventing a different mechanical footprint.

## RetroSBC implementation rule

The project footprint must be generated or transcribed from the dimensioned official QFN-80 package/land-pattern data. Do not substitute a generic 10×10 mm / 0.4 mm QFN-80 solely on nominal body and pitch.

Before committing the footprint, transcribe and independently check:
- perimeter lead width/length and span;
- exact exposed-pad dimensions;
- package tolerances;
- recommended PCB land dimensions, if explicitly supplied by the vendor;
- paste-window strategy;
- solder-mask expansion;
- pin-1 mark/orientation.

The official hardware-design guide notes that the 0.4 mm pitch drives the use of small passives/routing around the MCU. Layout should follow the vendor Minimal B example closely, particularly the switching-regulator and local-decoupling area.

## Qualification

A future footprint PR must include a machine-checkable pad-count/orientation test and a documented side-by-side review against the official dimensioned drawing. This lock alone is not footprint qualification.
