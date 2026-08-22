import cocotb
import random
from cocotb.triggers import Timer

@cocotb.test()
async def basic_test_arithmetic(dut):

        for _ in range(10):

                dut.a = random.randint(0,5)
                dut.b = random.randint(0,5)
                dut.cin = random.randint(0,1)
                dut.select = random.randint(0,7)
                print(f"A:{dut.a} B:{dut.b} || OUT:{dut.f} Cout:{dut.cout}")
                await Timer(1,"ns")
                

                