# RetroCore ECP5 platform layer

Native CERN-OHL-P-2.0 RetroSBC glue lives here. GPL upstream machine RTL is not copied into this directory.

The first adapter establishes a portable clock/reset and minimal host handshake boundary. Later commits extend this with ECP5 PLL, SDRAM and AGA machine adapters while keeping the native/upstream licensing boundary explicit.
