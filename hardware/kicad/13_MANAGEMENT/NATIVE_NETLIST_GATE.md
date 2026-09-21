# Native Slice A post-capture gate

This validator is intentionally added **before** the native electrical edit so
the acceptance target is executable and reviewable in advance.

After Slice A is materialized, CI must replace the temporary empty-netlist
baseline with:

```
python3 tools/check_management_native_netlist.py /tmp/retrosbc-kicad/13_MANAGEMENT.net
```

The validator requires U_MGMT and the five locked regulator support components,
the locked values, and MGMT_3V3 / MGMT_1V1 / VREG_AVDD / GND. It also rejects
the obsolete MGMT_1V1_FB / FB_MGMT_CORE topology.

This checker is necessary but not sufficient: KiCad parse, ERC, source/netlist
comparison and visual review remain required for CAPTURE PASS.
