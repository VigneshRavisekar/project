module ram(input logic rst_n,clk,csn,rwn,input logic [3:0] addr, input logic [3:0] data_in, output logic [3:0] data_out);

                logic [3:0] mem [0:15];

                assign data_out = (!csn && rwn) ? mem[addr] : 4'bz;

                always @(posedge clk)begin
                    if (!rwn && !csn)
                            mem[addr] <= data_in; 
                            
                end

endmodule