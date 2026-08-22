SIM ?= verilator
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/*.sv

TOPLEVEL = alu
MODULE = test_alu

EXTRA_ARGS += --trace --trace-structs 


include $(shell cocotb-config --makefiles)/Makefile.sim

