# M3.7 — RP2354B QFN-80 footprint transcription record

Status: **source transcription in progress — do not generate production footprint yet**

Authoritative source: Raspberry Pi RP2350 datasheet, QFN-80 package drawing, cross-checked with *Hardware design with RP2350*.

## Verified family-level values

| Parameter | Value | Status |
|---|---:|---|
| package | QFN-80 | VERIFIED |
| body X | 10 mm | VERIFIED |
| body Y | 10 mm | VERIFIED |
| perimeter pitch | 0.4 mm | VERIFIED |
| numbered perimeter pads | 80 | VERIFIED |
| centre exposed pad | GND / EP | VERIFIED |
| RP2354B internal flash | 2 MB | VERIFIED |

RP2350B and RP2354B share the QFN-80 package family. The official hardware-design guide explicitly treats the two QFN-80 variants together.

## Values still requiring dimension-callout transcription

Do not infer these from a generic library footprint:

- perimeter lead width and tolerance;
- perimeter lead length and tolerance;
- terminal span / seating geometry;
- exact exposed-pad X/Y dimensions and tolerance;
- pin-1 corner/chamfer dimensions;
- recommended PCB copper-land dimensions, if separately specified;
- solder-mask expansion;
- exposed-pad paste-window geometry.

## Review procedure

1. Read each dimension directly from the official dimensioned QFN-80 drawing.
2. Record the drawing callout/figure next to the value.
3. Perform an independent second read of the source.
4. Only then move the numeric value into the footprint generator input.
5. CI must regenerate the committed `.kicad_mod` byte-for-byte.

The 10×10 mm body and 0.4 mm pitch are sufficient to identify the package family, but **not sufficient to manufacture a qualified land pattern**.

## Layout note

Raspberry Pi's hardware-design guide recommends closely following the Minimal-B reference layout/component selections, particularly around the switching regulator, and notes that the 0.4 mm QFN pitch makes some 0402 passives unavoidable when exposing all GPIOs.

This record deliberately preserves the distinction between verified package-family facts and untranscribed manufacturing dimensions.
