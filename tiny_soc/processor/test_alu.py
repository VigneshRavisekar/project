import cocotb
import random
from cocotb.clock import Clock
from cocotb.triggers import Timer,RisingEdge,FallingEdge
import logging

log = logging.getLogger("cocotb")



def arithmetic_block(in_1,in_2,select,cin):

        print(select,cin)   
        opcode = int(str(select) + str(cin),2)
        print(f"OPCODE:{opcode}")     
        if opcode == 0:
              
              f = in_1
     
        elif opcode == 1:
              
              f = in_1 + 1
              
     
        elif opcode == 2:
              
              f = in_1 + in_2 
     
        elif opcode == 3:
              
              f = in_1 + in_2 + 1
     
        elif opcode == 4:
              
              f = in_1 + (~in_2)

        elif opcode == 5:
              
              f = in_1 + (~in_2) + 1 

        elif opcode == 6:
              
              f = in_1- 1

        elif opcode == 7:
              
              f = in_1
        else:
              log.error("INCORRECT OPCODE")
              

        return int(f)

def logical_block(in_1,in_2,select):

        if int(select) == 4:
              
              f = in_1 or in_2
     
        elif int(select) == 5:
              
              f = in_1 ^ in_2
     
        elif int(select) == 6:
              
              f = in_1 and in_2 
     
        elif int(select) == 7:
              
              f =  not in_1 
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

                 result = arithmetic_block(self.a.value,self.b.value,self.select.value,self.cin.value)

            else:

                 result = logical_block(self.a.value,self.b.value,self.select.value)

            return result
                
         
         
    
    
@cocotb.test()
async def test_arithmetic_operation(dut):

    alu = alu_base(dut)
    cocotb.start_soon(Clock(alu.clk,1,"ns").start())
    alu.rst_n.value = 0
    await Timer(2,"ns")
    alu.rst_n.value = 1
    for _ in range(10):
        alu.select.value = random.randint(0,3)
        alu.a.value = random.randint(0,15)
        alu.b.value = random.randint(0,15)
        alu.cin.value = random.randint(0,1)
        await Timer(1,"ns")
        print(f"A_VALUE:{int(alu.a.value)}")
        print(f"B_VALUE:{int(alu.b.value)}")
        print(f"CIN_VALUE:{alu.cin.value}")
        print(f"SELECT_VALUE:{int(alu.select.value)}")
        output = await alu.selector()
        print(f"OUTPUT:{output}")
        if(output == alu.f.value):
              log.info("TEST PASSED!!")
        else:
              log.error("TEST FAILED!!")

@cocotb.test()
async def test_logical_operation(dut):

         alu = alu_base(dut)
         cocotb.start_soon(Clock(alu.clk,1,"ns").start())
         alu.rst_n.value = 0
         await Timer(2,"ns")
         alu.rst_n.value = 1
         for _ in range(10):
             alu.select.value = random.randint(4,7)
             alu.a.value = random.randint(0,15)
             alu.b.value = random.randint(0,15)
             alu.cin.value = random.randint(0,1)
             await Timer(1,"ns")
             print(f"A_VALUE:{int(alu.a.value)}")
             print(f"B_VALUE:{int(alu.b.value)}")
             print(f"CIN_VALUE:{alu.cin.value}")
             print(f"SELECT_VALUE:{int(alu.select.value)}")
             output = await alu.selector()
             print(f"OUTPUT:{output}")
             if(output == alu.f.value):
                   log.info("TEST PASSED!!")
             else:
                   log.error("TEST FAILED!!")
      

      


    # alu.a.value = 9
    # alu.b.value = 15
    # alu.select.value = 2
    # alu.cin.value = 1
    # await Timer(1,"ns")
    # print(f"A_VALUE:{int(alu.a.value)}")
    # print(f"B_VALUE:{int(alu.b.value)}")
    # print(f"CIN_VALUE:{alu.cin.value}")
    # print(f"SELECT_VALUE:{int(alu.select.value)}")
    # output = await alu.selector()
    # print(f"OUTPUT:{output}")
    # if(output == alu.f.value):
    #       log.info("TEST PASSED!!")
    # else:
    #       log.error("TEST FAILED!!")



  



     


     

