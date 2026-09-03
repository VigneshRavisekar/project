import cocotb
import random
from cocotb.clock import Clock
from cocotb.triggers import Timer,RisingEdge,FallingEdge,ReadOnly
import logging

log = logging.getLogger("cocotb")

@cocotb.test()
async def test_write_read(dut):

           
            cocotb.start_soon(Clock(dut.clk,1,"ns").start())
            dut.rst_n.value = 0
            dut.csn.value = 1
            await Timer(3,"ns")
            dut.rst_n.value = 1
            dut.csn.value = 0
            dut.rwn.value = 0
            for addr in range(16):
                    await RisingEdge(dut.clk)
                    dut.addr.value = addr
                    dut.data_in.value = random.randint(0,15)
            await RisingEdge(dut.clk)
            dut.rwn.value = 1
            for addr in range(15,0,-1):
                    await RisingEdge(dut.clk)
                    dut.addr.value = addr
                    await ReadOnly()
                    log.info(dut.data_out.value)
            await Timer(100,"ns")
