// SPDX-License-Identifier: CERN-OHL-P-2.0
module sdram_qual_top(input wire clk,input wire reset,input wire req,input wire we,input wire [1:0] be,input wire [24:0] addr,input wire [15:0] wdata,output wire ready,output wire [15:0] rdata);
wire mr,mw,mready; wire [1:0] mbe; wire [24:0] ma; wire [15:0] mwd,mrd;
retrocore_sdram_bridge b(.clk(clk),.reset(reset),.req(req),.we(we),.be(be),.addr(addr),.wdata(wdata),.ready(ready),.rdata(rdata),.mem_req(mr),.mem_we(mw),.mem_be(mbe),.mem_addr(ma),.mem_wdata(mwd),.mem_ready(mready),.mem_rdata(mrd));
retrocore_sdram_model m(.clk(clk),.reset(reset),.req(mr),.we(mw),.be(mbe),.addr(ma),.wdata(mwd),.ready(mready),.rdata(mrd));
endmodule
