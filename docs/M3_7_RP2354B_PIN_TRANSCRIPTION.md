# RP2354B QFN-80 pin transcription workflow

The electrical KiCad symbol must be generated only from a complete, reviewed transcription of the official Raspberry Pi QFN-80 package table.

Files:
- `rp2354b-qfn80.csv` — 80-row transcription workspace.
- `tools/check_rp2354b_qfn80.py` — structural validator.
- `rp2354b-binding.csv` — RetroSBC logical GPIO assignment overlay.

The initial CSV intentionally contains `UNTRANSCRIBED/TBD` markers. The structural validator proves only pad coverage/uniqueness; it does **not** prove the pin names are correct.

Before symbol generation, a second semantic gate must reject every TBD/UNTRANSCRIBED row and cross-check the known GPIO/USB assignments against `rp2354b-binding.csv`.

This split prevents a syntactically complete but electrically invented pin table from being treated as qualified.
