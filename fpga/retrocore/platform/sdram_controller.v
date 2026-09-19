// SPDX-License-Identifier: CERN-OHL-P-2.0
// Generic single-data-rate SDR SDRAM controller skeleton for RetroSBC Rev-A.
// Timing values are expressed in controller clock cycles and remain provisional
// until the production SDRAM MPN and clock frequency are frozen.
module retrocore_sdram_controller #(
 parameter ADDR_WIDTH=25,
 parameter POWERUP_CYCLES=20000,
 // IS42S16320B-6TLI conservative 100 MHz / CL2 timing basis.
 parameter TRP=2,       // tRP >= 18 ns -> 2 cycles
 parameter TRCD=2,      // tRCD >= 18 ns -> 2 cycles
 parameter TRFC=7,      // tRFC >= 60 ns; 7 cycles keeps margin
 parameter TMRD=2,      // mode-register-set to next command
 parameter TWR=2,       // write recovery before PRECHARGE
 parameter CAS_LATENCY=2,
 parameter REFRESH_INTERVAL=780 // 64 ms / 8192 = 7.8125 us -> <=781 cycles
)(
 input wire clk,input wire reset,
 input wire req,input wire we,input wire [1:0] be,
 input wire [ADDR_WIDTH-1:0] addr,input wire [15:0] wdata,
 output reg ready=0,output reg [15:0] rdata=0,
 output reg sdram_cke=0,output reg sdram_cs_n=1,output reg sdram_ras_n=1,
 output reg sdram_cas_n=1,output reg sdram_we_n=1,
 output reg [1:0] sdram_ba=0,output reg [12:0] sdram_a=0,
 output reg [1:0] sdram_dqm=2'b11,
 output reg [15:0] dq_out=0,output reg dq_oe=0,input wire [15:0] dq_in
);
localparam ST_POWER=0,ST_PRE=1,ST_TRP=2,ST_REF1=3,ST_RFC1=4,ST_REF2=5,ST_RFC2=6,
 ST_MRS=7,ST_IDLE=8,ST_ACT=9,ST_TRCD=10,ST_READ=11,ST_CAS=12,ST_WRITE=13,
 ST_PRECHARGE=14,ST_WAITRP=15,ST_REFRESH=16,ST_WAITRFC=17,ST_MRD=18,ST_WR=19;
reg [4:0] state=ST_POWER; reg [31:0] timer=0,refresh=0; reg [ADDR_WIDTH-1:0] la=0;
reg lwe=0; reg [1:0] lbe=0; reg [15:0] lwd=0;
task nop; begin sdram_cs_n<=0;sdram_ras_n<=1;sdram_cas_n<=1;sdram_we_n<=1; end endtask
always @(posedge clk) begin
 ready<=0; dq_oe<=0; nop();
 if(reset) begin state<=ST_POWER;timer<=0;refresh<=0;sdram_cke<=0;sdram_cs_n<=1; end
 else case(state)
 ST_POWER: begin sdram_cke<=1;if(timer>=POWERUP_CYCLES) begin timer<=0;state<=ST_PRE;end else timer<=timer+1;end
 ST_PRE: begin sdram_ras_n<=0;sdram_we_n<=0;sdram_a[10]<=1;timer<=0;state<=ST_TRP;end
 ST_TRP: if(timer>=TRP-1) begin timer<=0;state<=ST_REF1;end else timer<=timer+1;
 ST_REF1: begin sdram_ras_n<=0;sdram_cas_n<=0;timer<=0;state<=ST_RFC1;end
 ST_RFC1: if(timer>=TRFC-1) begin timer<=0;state<=ST_REF2;end else timer<=timer+1;
 ST_REF2: begin sdram_ras_n<=0;sdram_cas_n<=0;timer<=0;state<=ST_RFC2;end
 ST_RFC2: if(timer>=TRFC-1) begin timer<=0;state<=ST_MRS;end else timer<=timer+1;
 ST_MRS: begin sdram_ras_n<=0;sdram_cas_n<=0;sdram_we_n<=0;sdram_a<=13'b0000000100000;refresh<=0;timer<=0;state<=ST_MRD;end
 ST_MRD: if(timer>=TMRD-1) begin timer<=0;state<=ST_IDLE;end else timer<=timer+1;
 ST_IDLE: begin
   if(refresh>=REFRESH_INTERVAL) begin refresh<=0;state<=ST_REFRESH;end
   else begin refresh<=refresh+1;if(req) begin la<=addr;lwe<=we;lbe<=be;lwd<=wdata;state<=ST_ACT;end end
 end
 ST_ACT: begin sdram_ras_n<=0;sdram_ba<=la[24:23];sdram_a<=la[22:10];timer<=0;state<=ST_TRCD;end
 ST_TRCD: if(timer>=TRCD-1) begin timer<=0;state<=lwe?ST_WRITE:ST_READ;end else timer<=timer+1;
 ST_READ: begin sdram_cas_n<=0;sdram_ba<=la[24:23];sdram_a<={3'b000,la[9:0]};sdram_dqm<=~lbe;timer<=0;state<=ST_CAS;end
 ST_CAS: if(timer>=CAS_LATENCY-1) begin rdata<=dq_in;timer<=0;state<=ST_PRECHARGE;end else timer<=timer+1;
 ST_WRITE: begin sdram_cas_n<=0;sdram_we_n<=0;sdram_ba<=la[24:23];sdram_a<={3'b000,la[9:0]};sdram_dqm<=~lbe;dq_out<=lwd;dq_oe<=1;timer<=0;state<=ST_WR;end
 ST_WR: if(timer>=TWR-1) begin timer<=0;state<=ST_PRECHARGE;end else timer<=timer+1;
 ST_PRECHARGE: begin sdram_ras_n<=0;sdram_we_n<=0;sdram_a[10]<=1;timer<=0;state<=ST_WAITRP;end
 ST_WAITRP: if(timer>=TRP-1) begin ready<=1;timer<=0;state<=ST_IDLE;end else timer<=timer+1;
 ST_REFRESH: begin sdram_ras_n<=0;sdram_cas_n<=0;timer<=0;state<=ST_WAITRFC;end
 ST_WAITRFC: if(timer>=TRFC-1) begin timer<=0;state<=ST_IDLE;end else timer<=timer+1;
 default: state<=ST_POWER;
 endcase
end
endmodule
