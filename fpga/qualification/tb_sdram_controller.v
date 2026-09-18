// SPDX-License-Identifier: MIT
`timescale 1ns/1ps
module tb_sdram_controller;
reg clk=0,reset=1,req=0,we=0; reg [1:0] be=2'b11; reg [24:0] addr=0; reg [15:0] wdata=0,dq_in=16'hCAFE;
wire ready; wire [15:0] rdata; wire cke,csn,rasn,casn,wen; wire [1:0] ba,dqm; wire [12:0] a; wire [15:0] dq_out; wire dq_oe;
integer refresh_count=0,pre_count=0,mrs_count=0,read_count=0,write_count=0;
retrocore_sdram_controller #(.POWERUP_CYCLES(4),.TRP(2),.TRCD(2),.TRFC(3),.CAS_LATENCY(2),.REFRESH_INTERVAL(12)) dut(
.clk(clk),.reset(reset),.req(req),.we(we),.be(be),.addr(addr),.wdata(wdata),.ready(ready),.rdata(rdata),
.sdram_cke(cke),.sdram_cs_n(csn),.sdram_ras_n(rasn),.sdram_cas_n(casn),.sdram_we_n(wen),.sdram_ba(ba),.sdram_a(a),.sdram_dqm(dqm),.dq_out(dq_out),.dq_oe(dq_oe),.dq_in(dq_in));
always #5 clk=~clk;
always @(posedge clk) if(!csn) begin
 if(!rasn && casn && !wen) pre_count=pre_count+1;
 if(!rasn && !casn && wen) refresh_count=refresh_count+1;
 if(!rasn && !casn && !wen) mrs_count=mrs_count+1;
 if(rasn && !casn && wen) read_count=read_count+1;
 if(rasn && !casn && !wen) write_count=write_count+1;
end
task wait_ready; integer n; begin n=0; while(!ready && n<100) begin @(posedge clk); #1; n=n+1; end if(!ready) $fatal(1,"timeout waiting for ready state=%0d refresh=%0d req=%0b",dut.state,dut.refresh,req); end endtask
initial begin
 repeat(3) @(posedge clk); reset=0;
 wait(dut.state==8); @(posedge clk); #1;
 if(!cke) $fatal(1,"CKE not enabled");
 if(pre_count<1) $fatal(1,"missing PRECHARGE ALL");
 if(refresh_count<2) $fatal(1,"missing initialization refreshes");
 if(mrs_count<1) $fatal(1,"missing mode register set");
 addr=25'h12345; be=2'b11; we=0; @(negedge clk); req=1; @(negedge clk); req=0; wait_ready();
 if(read_count<1) $fatal(1,"READ command missing");
 if(rdata!==16'hCAFE) $fatal(1,"read data mismatch");
 addr=25'h23456; wdata=16'hBEEF; be=2'b01; we=1; @(negedge clk); req=1; @(negedge clk); req=0; wait_ready();
 if(write_count<1) $fatal(1,"WRITE command missing");
 if(dqm!==2'b10) $fatal(1,"byte mask mismatch");
 repeat(25) @(posedge clk);
 if(refresh_count<3) $fatal(1,"periodic refresh missing");
 $display("PASS init=%0d refresh=%0d read=%0d write=%0d",mrs_count,refresh_count,read_count,write_count);
 $finish;
end
endmodule
