import cocotb
import random
from cocotb.clock import Clock
from cocotb.triggers import Timer,RisingEdge,FallingEdge

@cocotb.test()
async def basic_test_arithmetic(dut):

        cocotb.start_soon(Clock(dut.clk,1,"ns").start())
        dut.rst_n = 0
        await Timer(2,"ns")
        dut.rst_n= 1
        for _ in range(10):

                dut.a = random.randint(0,5)
                dut.b = random.randint(0,5)
                dut.cin = random.randint(0,1)
                dut.select = random.randint(0,7)
                print(f"A:{dut.a} B:{dut.b} || OUT:{dut.f} Cout:{dut.cout}")
                await Timer(1,"ns")
                

                