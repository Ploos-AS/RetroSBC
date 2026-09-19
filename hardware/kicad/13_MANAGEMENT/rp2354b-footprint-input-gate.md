# M3.7 — QFN-80 footprint input gate

Status: **mechanical transcription gate**

The RP2354B footprint must be based on the dimensioned official Raspberry Pi RP2350B/RP2354B QFN-80 package data, not nominal package-name matching.

Authoritative facts already locked:
- QFN-80 B-family package;
- 10 mm × 10 mm body;
- 0.4 mm perimeter pitch;
- centre exposed pad is GND;
- RP2350B and RP2354B share this package family.

## Required numeric transcription

Before a generated `.kicad_mod` is accepted, record the official dimensioned values for:
- lead width;
- lead length;
- lead-to-lead span;
- exposed-pad X/Y size;
- body tolerances;
- recommended PCB land dimensions where supplied;
- pin-1/chamfer/orientation geometry.

Each numeric value must carry its source figure/table identifier. A reviewer must independently compare the transcription with the source.

## Generator acceptance

The future footprint generator must:
- emit exactly 80 perimeter pads plus one exposed `EP` pad;
- use 0.4 mm pitch;
- map pin 1 orientation to the symbol/package drawing;
- name the exposed pad `EP` to match the project symbol;
- provide F.Paste/F.Mask treatment intentionally, not as a generic-library default;
- produce deterministic output suitable for CI diff checking.

No footprint is generated in this change because the remaining land-pattern dimensions have not yet been transcribed and independently checked.
