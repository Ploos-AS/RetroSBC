module retrocore_top(
    input  wire clk,
    input  wire reset_n,
    output wire alive
);
    reg [23:0] heartbeat = 24'd0;

    always @(posedge clk) begin
        if (!reset_n)
            heartbeat <= 24'd0;
        else
            heartbeat <= heartbeat + 1'b1;
    end

    assign alive = heartbeat[23];
endmodule
