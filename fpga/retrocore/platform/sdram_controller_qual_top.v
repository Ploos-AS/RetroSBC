// SPDX-License-Identifier: CERN-OHL-P-2.0
module sdram_controller_qual_top(input wire clk,input wire reset,input wire req,input wire we,input wire [1:0] be,input wire [24:0] addr,input wire [15:0] wdata,input wire [15:0] dq_in,output wire ready,output wire [15:0] rdata,output wire cke,csn,rasn,casn,wen,output wire [1:0] ba,dqm,output wire [12:0] a,output wire [15:0] dq_out,output wire dq_oe);
retrocore_sdram_controller #(.POWERUP_CYCLES(8),.REFRESH_INTERVAL(32)) u(.clk(clk),.reset(reset),.req(req),.we(we),.be(be),.addr(addr),.wdata(wdata),.ready(ready),.rdata(rdata),.sdram_cke(cke),.sdram_cs_n(csn),.sdram_ras_n(rasn),.sdram_cas_n(casn),.sdram_we_n(wen),.sdram_ba(ba),.sdram_a(a),.sdram_dqm(dqm),.dq_out(dq_out),.dq_oe(dq_oe),.dq_in(dq_in));
endmodule
