# M3.2 SDRAM timing basis

Primary part: **ISSI IS42S16320B-6TLI**

Qualification clock: **100 MHz** (10 ns period), CAS latency **2**.

The -6 device is specified for 166 MHz at CL3 and supports 100 MHz at CL2. Controller cycle parameters must be rounded upward from the exact datasheet minimum timings; no timing value may be made less conservative merely to pass simulation.

This step locks the part, clock and CAS-latency basis. The next controller change shall encode named timing parameters (including tRP, tRCD, tRFC, tMRD, tWR and 8K/64 ms refresh) with comments tying cycle counts to the datasheet. Physical qualification still requires ECP5 pin/bank constraints, post-route timing and board testing.
