// SPDX-License-Identifier: CERN-OHL-P-2.0
// Transport-independent machine-side memory contract.
// This is deliberately not yet the physical SDR SDRAM controller.
module retrocore_sdram_bridge #(
    parameter ADDR_WIDTH = 25
) (
    input  wire                  clk,
    input  wire                  reset,
    input  wire                  req,
    input  wire                  we,
    input  wire [1:0]            be,
    input  wire [ADDR_WIDTH-1:0] addr,
    input  wire [15:0]           wdata,
    output reg                   ready = 1'b0,
    output reg  [15:0]           rdata = 16'h0000,

    output reg                   mem_req = 1'b0,
    output reg                   mem_we = 1'b0,
    output reg  [1:0]            mem_be = 2'b00,
    output reg  [ADDR_WIDTH-1:0] mem_addr = {ADDR_WIDTH{1'b0}},
    output reg  [15:0]           mem_wdata = 16'h0000,
    input  wire                  mem_ready,
    input  wire [15:0]           mem_rdata
);
    reg busy = 1'b0;
    always @(posedge clk) begin
        ready <= 1'b0;
        if (reset) begin
            busy <= 1'b0;
            mem_req <= 1'b0;
        end else if (!busy && req) begin
            busy <= 1'b1;
            mem_req <= 1'b1;
            mem_we <= we;
            mem_be <= be;
            mem_addr <= addr;
            mem_wdata <= wdata;
        end else if (busy && mem_ready) begin
            rdata <= mem_rdata;
            ready <= 1'b1;
            busy <= 1'b0;
            mem_req <= 1'b0;
        end
    end
endmodule
