module ecp5_85k_smoke(
    input  wire clk,
    input  wire host_req,
    output reg  host_ack = 1'b0,
    output reg [7:0] trace = 8'h00
);
    reg [23:0] counter = 24'h0;
    always @(posedge clk) begin
        counter <= counter + 1'b1;
        host_ack <= host_req;
        trace <= counter[23:16];
    end
endmodule
