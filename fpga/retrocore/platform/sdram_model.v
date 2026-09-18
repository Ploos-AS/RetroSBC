// SPDX-License-Identifier: CERN-OHL-P-2.0
// Tiny synthesizable handshake target for CI qualification only.
// It proves the bridge contract without pretending to be a DRAM controller.
module retrocore_sdram_model(
 input wire clk,input wire reset,input wire req,input wire we,
 input wire [1:0] be,input wire [24:0] addr,input wire [15:0] wdata,
 output reg ready=0,output reg [15:0] rdata=0);
 reg pending=0;
 always @(posedge clk) begin
  ready<=0;
  if(reset) pending<=0;
  else if(req && !pending) begin pending<=1; rdata<=addr[15:0] ^ (we ? wdata : 16'hA120); end
  else if(pending) begin pending<=0; ready<=1; end
 end
endmodule
