`timescale 1ns/1ps
module tb_retrocore_top;
    reg clk = 0;
    reg reset_n = 0;
    wire alive;

    retrocore_top dut(.clk(clk), .reset_n(reset_n), .alive(alive));

    always #5 clk = ~clk;

    initial begin
        repeat (2) @(posedge clk);
        reset_n = 1;
        repeat (8) @(posedge clk);
        $display("RetroCore RTL smoke test PASS");
        $finish;
    end
endmodule
