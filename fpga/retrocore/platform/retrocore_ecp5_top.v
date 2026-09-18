// SPDX-License-Identifier: CERN-OHL-P-2.0
module retrocore_ecp5_top(input wire clk_in,input wire reset_n,input wire host_req,output wire host_ack,output wire alive);
wire clk_sys,reset_sys; reg [23:0] heartbeat=0; reg ack=0;
retrocore_clock_reset u_clock_reset(.clk_in(clk_in),.reset_n(reset_n),.clk_sys(clk_sys),.reset_sys(reset_sys));
always @(posedge clk_sys) begin if(reset_sys) begin heartbeat<=0; ack<=0; end else begin heartbeat<=heartbeat+1'b1; ack<=host_req; end end
assign host_ack=ack; assign alive=heartbeat[23];
endmodule
