# M3.2 controller timing implementation

The native controller now encodes the Rev-A **IS42S16320B-6TLI** 100 MHz / CL2 timing basis directly in RTL.

Default guards:

| Parameter | Default | 100 MHz interpretation |
|---|---:|---|
| POWERUP_CYCLES | 20000 | 200 us |
| TRP | 2 | 20 ns |
| TRCD | 2 | 20 ns |
| TRFC | 7 | 70 ns |
| TMRD | 2 | 2 clocks |
| TWR | 2 | 20 ns |
| CAS_LATENCY | 2 | CL2 |
| REFRESH_INTERVAL | 780 | 7.80 us |

The refresh interval is deliberately below the 7.8125 us average implied by 8192 refreshes / 64 ms.

The controller now has explicit post-MRS and write-recovery states. These defaults are qualification parameters for the selected part and clock; board-level timing and post-route timing remain separate gates.
