# M3.7 QFN-80 binding correction

The complete authoritative QFN-80 transcription exposed that the earlier partial binding table contained multiple physical-pad offsets, not only the USB pair.

This change rebases every existing RetroSBC management assignment against the complete package table.

Notable corrections include:
- GPIO8/9: pads 6/7
- GPIO21/22/23: pads 21/22/23
- GPIO28..32: pads 36..40
- GPIO0/1: pads 77/78
- USB_DM/USB_DP: pads 66/67

The logical GPIO choices are unchanged; only the physical QFN-80 pad numbers are corrected.

The authoritative package table is now the primary package source. Partial hand-entered pad mappings must never be treated as authoritative again.
