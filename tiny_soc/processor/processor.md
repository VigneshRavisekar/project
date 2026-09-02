**4-bit processor**
----------------------

<img width="747" height="546" alt="image" src="https://github.com/user-attachments/assets/2d31c46c-4c7f-4109-88cc-c50dd9113958" />
                                      

<img width="580" height="255" alt="image" src="https://github.com/user-attachments/assets/c41977b6-6fe8-476b-b36c-43721f95dc6e" />

These two images form the baseline for this 4 bit microprocessor

## Detective Work 

During the implementation of the ALU and while brainstorming about Instruction Decoder, several
architectural/design issues were identified in the existing 4-bit processor.

**Design Flaw Bucket**
| # | Design Issue | Observation |
|---|---|---|
| 1 | **FETCH state / instruction fetching** | The `FETCH` state in the state diagram does not appear to fetch the instruction. Instead, it fetches data from a RAM location. The instruction-fetch mechanism therefore needs to be reconsidered. |
| 2 | **ALU → Instruction Decoder feedback loop** | The ALU generates a data output which is fed back to the Instruction Decoder as an address. For example, for `ADD 5 3`, the ALU produces `8`, which then becomes an address to the decoder. This data path does not make architectural sense for instruction execution. |
| 3 | **Insufficient / inconsistent control signals** | The ALU requires multiple select signals and a `Cin` input, while the Instruction Decoder provides a control signal which is only one bit. Attempting to use this signal to control both the ALU and memory creates an inconsistency in the control architecture. |
| 4 | **ALU registration and FSM synchronization** | Operations are executed within a state and clock cycle, but the registered ALU output does not appear to be properly synchronized with the FSM state transitions. The ALU result may therefore not be available at the point where the next state expects it. |
| 5 | **Inconsistent ALU multiplexing** | The signal selection/muxing around the ALU is inconsistent, making the intended datapath and selection of operands/results unclear. |
| 6 | **Operand 2 limitation** | Operand 2 is effectively constant, limiting the processor's ability to perform operations involving two independently selected operands, such as register-to-register operations. An attempt was made to redesign the ISA by separating the memory and ALU datapaths, but this exposed the instruction-fetch issue again. |
                                      
## Proposed Design Changes

Working on finding even more interesting design flaws (hoping to add more as a
Verif Engineer in the design flaw bucket) and then improvising the design
changes.

**WORK IN PROGRESS**


