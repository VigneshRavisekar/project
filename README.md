# Custom Processor Design Exploration

> **A small processor, built to understand the architecture—not to imitate RISC-V.**

This repository documents an incremental digital-design project: begin by studying a reference 4-bit microprocessor, identify architectural and control-flow questions, then develop a custom 8-bit accumulator-based processor and work toward RTL, verification, synthesis, and eventually a small SoC.

The goal is not to claim that the reference design is definitively broken. It is to understand its documented behavior, identify ambiguities and limitations, test those observations against the diagrams and implementation, and make explicit design decisions for a new architecture.

## 1. Reference Design: 4-bit Microprocessor

The two diagrams below are the reference baseline for the 4-bit microprocessor. They are the starting point for the investigation, not the specification for the new 8-bit processor.

<!-- Keep the two reference-design images attached here. -->

## 2. Detective Work: Questions Raised by the Reference Design

While studying the ALU and instruction decoder, several questions emerged. These are recorded as design observations to investigate—not all are yet proven implementation bugs.

| # | Area | Observation / question |
|---|---|---|
| 1 | Instruction fetch | The documented FETCH state appears to read data from RAM rather than clearly fetching an instruction. The instruction-fetch path needs to be traced and explained. |
| 2 | ALU-to-decoder path | The ALU result appears to feed the instruction decoder as an address. For example, an ADD result could influence decoder addressing. The intended role of this path needs verification. |
| 3 | Control signals | The ALU appears to need multiple operation-select signals and carry input, while the decoder exposes a narrower control interface. The control encoding and its use by memory logic need clarification. |
| 4 | ALU/FSM timing | The relationship between registered ALU results and FSM state transitions is unclear. The design must establish when a result becomes valid and when the next state consumes it. |
| 5 | ALU input selection | The datapath's operand-selection and muxing behavior is not sufficiently clear from the available diagrams. |
| 6 | Operand flexibility | The second ALU operand appears constrained or effectively constant in the observed design, limiting operations that require two independently selected operands. Attempts to separate the ALU and memory datapaths also exposed the instruction-fetch question. |

These observations motivate a more explicit architecture specification: define instruction fetch, operand sources, datapath paths, control signals, and cycle-by-cycle behavior before implementing RTL.

## 3. Redesign Direction: A Custom 8-bit Accumulator Processor

The project subsequently moved from examining the 4-bit reference design to designing a separate custom 8-bit processor. This is an architectural redesign, not simply a width increase.

The design direction is a compact accumulator-oriented machine:
- **Data width:** 8 bits.
- **Registers:** X0–X6 are general-purpose registers; X7 is the implicit accumulator/default operand register.
- **Instruction memory:** 64K × 8, addressed by a 16-bit program counter.
- **Data memory:** 256 × 8 in the current architecture.
- **Instruction families under development:** arithmetic, logical operations, transfer/immediate operations, load/store, comparison, and unconditional/conditional branching.
- **Control:** an FSM whose state transitions and control signals must agree with the ISA, datapath, and timing diagrams.

The accumulator approach makes common instructions compact by using X7 implicitly. The trade-off is that some algorithms may require more instructions than an explicit multi-register-operand architecture. That is a design trade-off to measure and explain, not automatically an advantage.

## 4. Architecture Decisions and Review Trail

The GitHub issues preserve the design discussion and the reasons behind decisions:

- [Issue #1 — ISA proposal and review](https://github.com/VigneshRavisekar/project/issues/1): compact instruction encoding, accumulator-based operation, immediate forms, memory addressing, and the evolution of the ISA drafts.
- [Issue #2 — Architecture baseline](https://github.com/VigneshRavisekar/project/issues/2): the preliminary ISA and rough architecture baseline.
- [Issue #3 — Architecture, instruction tracing, and FSM control](https://github.com/VigneshRavisekar/project/issues/3): FSM and instruction timing evidence.
- [Issue #4 — Branch-target semantics](https://github.com/VigneshRavisekar/project/issues/4): branch target is defined relative to the current PC, using a signed offset held in the selected register.
- [Issue #5 — Branch-offset representation](https://github.com/VigneshRavisekar/project/issues/5): the offset is an 8-bit two's-complement value, sign-extended to 16 bits; the documented range is −128 to +127.
- [Issue #6 — CMP and E/GT flags](https://github.com/VigneshRavisekar/project/issues/6): comparison updates flags without writing the subtraction result back to X7; signed/unsigned comparison behavior is part of the review.
- [Issue #7 — ST write-enable behavior](https://github.com/VigneshRavisekar/project/issues/7): isMemWE is active-high during the store cycle; the address comes from Xn and write data from X7.
- [Issue #8 — LD timing and PC progression](https://github.com/VigneshRavisekar/project/issues/8): LD [Xn] reads DataMem[Xn] into X7; the one-byte instruction advances sequentially by one address.
- [Issue #9 — CMP and conditional-branch timing evidence](https://github.com/VigneshRavisekar/project/issues/9): timing evidence for comparison and conditional branch cases.
- [Issue #10 — Branch FSM terminology](https://github.com/VigneshRavisekar/project/issues/10): branch terminology aligned to B, BEQ (E condition), and BGT (GT condition).
- [Issue #11 — Final ISA/datapath/FSM/timing review](https://github.com/VigneshRavisekar/project/issues/11): the final cross-review gate before declaring the architecture ready for RTL.

The issue tracker is the decision history. If an older draft, diagram, or comment conflicts with a later ratified ISA, the ratified ISA and the final cross-review must take precedence.

## 5. Timing Before RTL

Instruction timing diagrams are being used to reason about what happens in each FSM state and on each clock edge. The review covers:
- register and immediate arithmetic;
- transfer and immediate-transfer operations;
- CMP, including flag updates without accumulator writeback;
- LD and ST, including memory control timing;
- unconditional and conditional branches, including taken and not-taken paths.

The architecture is not considered RTL-ready merely because individual diagrams exist. The instruction semantics, encoding, datapath, FSM, PC progression, memory timing, and flag behavior must describe the same machine.

## 6. Current Status

**Phase:** pre-RTL architecture closure.

Completed or documented in the issue tracker:
- initial ISA and architecture drafts;
- branch-target and branch-offset definitions;
- load/store control and PC-progression decisions;
- CMP/flag behavior decisions and branch terminology updates;
- a set of instruction timing diagrams.

**Remaining gate:** complete the final consistency review in [Issue #11](https://github.com/VigneshRavisekar/project/issues/11), using the ratified ISA as the source of truth. Do not treat the architecture as formally RTL-ready until the remaining acceptance criteria are checked.

## 7. Longer-Term Direction

Once the architecture is frozen, the intended progression is:
1. implement the processor in synthesizable RTL;
2. build a self-checking verification environment and test each instruction class and corner case;
3. debug and document failures rather than relying only on directed happy-path tests;
4. run synthesis and inspect the resulting hardware;
5. explore a small SoC as a separate, later track, then progressively investigate the broader ASIC flow.

RISC-V remains a possible future learning direction, but this processor is a custom educational architecture and is **not** a RISC-V implementation.
