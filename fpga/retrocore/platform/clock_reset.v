// SPDX-License-Identifier: CERN-OHL-P-2.0
module retrocore_clock_reset(input wire clk_in,input wire reset_n,output wire clk_sys,output reg reset_sys=1'b1);
reg [3:0] reset_pipe=4'b1111; assign clk_sys=clk_in;
always @(posedge clk_in or negedge reset_n) begin
 if(!reset_n) begin reset_pipe<=4'b1111; reset_sys<=1'b1; end
 else begin reset_pipe<={reset_pipe[2:0],1'b0}; reset_sys<=|reset_pipe; end
end
endmodule
