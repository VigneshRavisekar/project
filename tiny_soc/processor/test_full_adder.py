import cocotb
import random
from cocotb.triggers import Timer

@cocotb.test()
async def basic_test(dut):

    for _ in range(5):
        dut.a = random.randint(0,10)
        dut.b = random.randint(0,10)
        await Timer(1,units="ns")
        print(f"A:{int(dut.a)},B:{int(dut.b)} ||| SUM {int(dut.sum)} CARRY_OUT {dut.cout}")

