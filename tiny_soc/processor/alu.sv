module alu(input logic [3:0] a,b,input logic [2:0] select,input logic cin,output logic [3:0] f, output logic cout);

                // inner signals
                logic [3:0] b_sel,f_arth,f_logic;
                logic cin_sel;

                assign cin_sel = cin;

                always_comb begin

                    b_sel   = 0;
                    f_logic = 0;

                    case(select)

                        3'b000: 
                                begin
                                      if(cin_sel == 0)

                                            b_sel = 0;
                                      else
                                            b_sel = 1;
                                end
                        
                        3'b001: 
                                begin
                                        b_sel = b;
                                end
                        
                        3'b010: 
                                begin
                                        b_sel = ~ b;
                                end
                        
                        3'b011: 
                                begin
                                       if(cin_sel==1)
                                            b_sel = -1;
                                       else 
                                            b_sel = 15;
                                end
                        3'b100:
                                begin
                                        f_logic = a | b;
                                end
                        
                        3'b101:
                                begin 
                                        f_logic = a ^ b;
                                end

                        3'b110:
                                begin
                                        f_logic = a & b;
                                end
                                
                        3'b111:

                                begin
                                        f_logic = ~a;
                                end                  
                        
                        
                    endcase

                    
                end

                top_adder adder(.a(a),.b(b_sel),.cin(cin_sel),.sum(f_arth),.cout(cout));
                assign f = (select>3)? f_logic : f_arth ;



endmodule