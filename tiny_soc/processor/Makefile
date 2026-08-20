SIM ?= verilator
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/*.sv

TOPLEVEL = top_adder
MODULE = test_full_adder


include $(shell cocotb-config --makefiles)/Makefile.sim

