import cocotb
import random
from cocotb.clock import Clock
from cocotb.triggers import Timer,RisingEdge,FallingEdge
from cocotb.binary import BinaryValue
import logging

log = logging.getLogger("cocotb")


def comparsion_block(output,dut_out,dut_cout):

            tb_out = int(output.binstr[-4:], 2)
            tb_cout = int(output.binstr[-5],2)
            print(f"ALU_OUTPUT:{int(dut_out)} || TB_OUTPUT:{tb_out}")
            if tb_out == dut_out and tb_cout == dut_cout :
                  log.info("COMPARISON PASSED!!!")
            else:
                  log.error("COMPARISON FAILED!!!")
            
      



def arithmetic_block(in_1,in_2,select,cin,cout):

        print(select,cin)   
        opcode = int(str(select) + str(cin),2)
        print(f"OPCODE:{opcode}")     
        if opcode == 0:
              
              f = BinaryValue(in_1,n_bits=5,bigEndian=False)
     
        elif opcode == 1:
              
              f = BinaryValue(in_1 + 1,n_bits=5,bigEndian=False)
              
     
        elif opcode == 2:
              
             
              f = BinaryValue(in_1 + in_2,n_bits = 5,bigEndian=False)
                  
        elif opcode == 3:

              f = BinaryValue(in_1 + in_2+1,n_bits = 5,bigEndian=False)
              
        elif opcode == 4:

              f = BinaryValue(in_1 + ~in_2,n_bits = 5,bigEndian=False)
             
        elif opcode == 5:

              f = BinaryValue(in_1 + (~in_2) + 1 ,n_bits = 5,bigEndian=False)

        elif opcode == 6:
              
              f = BinaryValue(in_1 - 1,n_bits=5,bigEndian=False)
              print(in_1)
              print(f)

        elif opcode == 7:
              
              f = BinaryValue(in_1,n_bits=5,bigEndian=False)
        else:
              log.error("INCORRECT OPCODE")
              

        return f

def logical_block(in_1,in_2,select):
        
        print(f"OPCODE:{int(select)}")
        if int(select) == 4:
              
              f = in_1 | in_2
      
        elif int(select) == 5:
              
              f = in_1 ^ in_2
     
        elif int(select) == 6:
              
              f = in_1 & in_2 
     
        elif int(select) == 7:
              
              f =  int(~ in_1,2) 
             
        else:
              log.error("INCORRECT OPCODE")

        return f
              


class alu_base:

    def __init__(self,dut):

        self.a = dut.a
        self.b = dut.b
        self.select = dut.select
        self.cin  = dut.cin
        self.clk  = dut.clk
        self.rst_n = dut.rst_n
        self.cout  = dut.cout
        self.f = dut.f

    async def selector(self):

            await Timer(1,"ns")
            if int(self.select.value) < 4:

                 result = arithmetic_block(self.a.value,self.b.value,self.select.value,self.cin.value,self.cout.value)

            else:

                 result = logical_block(self.a.value,self.b.value,self.select.value)
                 print(result)

            return result
                
         
         
    
    
# @cocotb.test()
# async def test_arithmetic_operation(dut):

#     alu = alu_base(dut)
#     cocotb.start_soon(Clock(alu.clk,1,"ns").start())
#     alu.rst_n.value = 0
#     await Timer(2,"ns")
#     alu.rst_n.value = 1
#     for _ in range(10):
#         alu.select.value = random.randint(0,3)
#         alu.a.value = random.randint(0,15)
#         alu.b.value = random.randint(0,15)
#         alu.cin.value = random.randint(0,1)
#         await Timer(1,"ns")
#         print(f"A_VALUE:{int(alu.a.value)}")
#         print(f"B_VALUE:{int(alu.b.value)}")
#         print(f"CIN_VALUE:{alu.cin.value}")
#         print(f"SELECT_VALUE:{int(alu.select.value)}")
#         output = await alu.selector()
#         comparsion_block(output,alu.f.value,alu.cout.value)

# @cocotb.test()
# async def test_logical_operation(dut):

#          alu = alu_base(dut)
#          cocotb.start_soon(Clock(alu.clk,1,"ns").start())
#          alu.rst_n.value = 0
#          await Timer(2,"ns")
#          alu.rst_n.value = 1
#          for _ in range(10):
#              alu.select.value = random.randint(4,7)
#              alu.a.value = random.randint(0,15)
#              alu.b.value = random.randint(0,15)
#              alu.cin.value = random.randint(0,1)
#              await Timer(1,"ns")
#              print(f"A_VALUE:{int(alu.a.value)}")
#              print(f"B_VALUE:{int(alu.b.value)}")
#              print(f"CIN_VALUE:{alu.cin.value}")
#              print(f"SELECT_VALUE:{int(alu.select.value)}")
#              output = await alu.selector()
#              comparsion_block(output,alu.f.value,alu.cout.value)
      

      
@cocotb.test()
async def individual(dut):

    alu = alu_base(dut)
    cocotb.start_soon(Clock(alu.clk,1,"ns").start())
    alu.rst_n.value = 0
    await Timer(2,"ns")
    alu.rst_n.value = 1
    alu.a.value = 12
    alu.b.value = 11
    alu.select.value = 3
    alu.cin.value = 0
    await Timer(1,"ns")
    print(f"A_VALUE:{int(alu.a.value)}")
    print(f"B_VALUE:{int(alu.b.value)}")
    print(f"CIN_VALUE:{alu.cin.value}")
    print(f"SELECT_VALUE:{int(alu.select.value)}")
    output = await alu.selector()
    print(f"AAA:{output}")
    comparsion_block(output,alu.f.value,alu.cout.value)



  



     


     

