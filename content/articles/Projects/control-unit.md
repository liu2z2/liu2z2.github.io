---
Title: Gate-Level Control Unit Design
Date: 2021-04-26
Status: published
Tags: project, hardware, class
---

[TOC]

This article talks about the technical aspects and takeaway from two inter-connecting projects from Intro to Computer Architecture and Organization Class.
The detail about the class is explained in my [Spring 2021 Remark](../Discussion/spring-2021.md).
More info about the projects is available at my [class-files repo](https://github.com/liu2z2/class-files/tree/main/spring2021-comp-org).

### Non-Pipelined Control Unit

A single-bus processing unit was designed capable of executing a set of instructions specified as in Fig. 1.
The design was implemented at the gate level. Some restrictions of the assignment include:

- Design should be restricted to single-bus paradigm. No point-to-point connections.
- Read-only memory (ROM) may be used to contain up to 8 constants. Its design can be specified descriptively.
- Main memory (MM) design can be specified descriptively and performs asynchronously
- Gate level design must only use MUX, DEMUX, encoder, decoder, flip-flop and gates.
- Detailed count-down timer design can be specified descriptively.

<figure>
  <img src="/images/project-control-unit/instr-table.png"/>
  <figcaption> <small> Fig. 1: Instruction set </small> </figcaption>
</figure>

#### Solution Brief

We presented our design in a modular structure, which of which is used extensively by the CPU to meet the design requirements and achieve optimization.
An abstract overview of the CPU is shown in Fig. 2.
Data used in the instructions is pushed to a 16-bit bus as the only conveyance before being delivered to the intended locations.

<figure>
  <img src="/images/project-control-unit/data-path.png"/>
  <figcaption> <small> Fig. 2: Abstract view of the data path </small> </figcaption>
</figure>

We started the Control Unit design by firstly defining the control signals needed in each instructions, during which we also discussed necessary changes and possible optimizations in the data path.
The common fetch-decode-execute sequence was adopted as a general guideline.
Afterwards, the control signals are collapsed into groups such that states can be determined, as well as the state transition.
With the aforementioned state information narrowed down, the gate-level circuit was implemented as a Moore machine whose input is Opcode and various control flags from other components on the data bus, and whose output is to enable tri-state buffers on data paths.

<figure>
  <img src="/images/project-control-unit/state-trans.png"/>
  <figcaption> <small> Fig. 3: State transition diagram </small> </figcaption>
</figure>

<figure>
  <img src="/images/project-control-unit/control-unit.png"/>
  <figcaption> <small> Fig. 4: Control unit block component view </small> </figcaption>
</figure>

Detail on other components is explained in the [project report](https://github.com/liu2z2/class-files/tree/main/fall2021-comp-org/project-3-report.pdf). Related optimizations include:

- We use Y and Z as pre- and post- buffer for the ALU operations, respectively, by statically writing in common register values.
- Insead of sending six different control signals to dictate ALU functions for Opcode 0-5, whose operands are in similar format, the control unit commences a master signal which lets the ALU requests the Opcode directly to decide on the specific logical/arithmetic operations.
- The ALU utilizes a carry lookahead adder-subtractor circuit in order to add or subtract two 16-bit values and output a single 16-bit value.
  The carry lookahead generator, while it utilizes more gates than the
  ripple-carry adder design, results in a significant decrease in propagation delay and performance time through the operations.

<figure>
  <img src="/images/project-control-unit/data-path-block.png"/>
  <figcaption> <small> Fig 5: Data path block diagram </small> </figcaption>
</figure>

#### Takeaway

In this project, we went through the design and part of the implementation phase of a digital/register level project.
We broke down the specification, explored possible solution, discussed possible optimization and eventually documented our solution within the time constraints.
As a class assignment, we have scored the highest grade with a few points taken off due to formatting inconsistency.
The project also gave us a chance to reflect on our understanding of the material, and luckily we were given enough time to clarify some questions over the discussion of the project.

### Pipelined Control Unit

In this project, we were assigned to design a CPU with almost the same functionality, except the operation can be pipelined, and that the gate-level implementation is not required.
Other limitations include I/O constraints, register space capacity, etc, are listed below.

- No hard restriction on data path, but all paths should be used reasonably.
- Main memory (MM) has separate instruction and data ports that can be used simultaneously.
- Register file (GPR) has 3 read ports and 2 write ports and all can be accessed simultaneously.
- The pipeline should include at least three stages, corresponding to the fetch/decode/execute cycle.
- Read-only memory (ROM) may be used to contain up to 8 constants.

#### Solution Brief

As the functionality of this machine has many parts that overlap with the previous project, the detailed design and implementation were only briefly covered, whereas the pipeline is mainly discussed in the solution.

Our pipeline design consists of four unique stages: F1, F2, D1 and E1, matching the fetch/decode/execute cycle instruction cycle (Figure 6).
Although some states share hardware resources, each has its own portion of the data path and dedicated portion of the control unit.
By this design, each state only uses 1 clock cycle to finish, resulting in an ideal instruction completion time of 4 clock cycles - with a possible 4 instructions in the pipeline.
Though it was hard to implement such system, this was a firm decision we made at the very beginning and we were determined to resolve the hazards from it.

<figure>
  <img src="/images/project-control-unit/pipeline-timing.png"/>
  <figcaption> <small> Fig. 6: Four stage pipeline </small> </figcaption>
</figure>

Before we decipher the hazards individually, we designed a hardware queue system that dispatches instruction register (IR) and PC data to each stages, ensuring the correct flow of the pipeline.
The implementation of the queuing on IR and PC is 16 stacks of 4-bit and 3-bit shift registers, respectively, shown in Fig. 7.
The memory organization of them can be seen in Fig. 8, where each row is a shift register that can be controlled to shift, keep, or clear on each element, whereas a column represents a full IR/PC data.
Additionally, by having a digitally controlled buffer from the clock to the RESET of the flip-flops, the register can also be cleared synchronously with the rest of the machine.

<figure>
  <img src="/images/project-control-unit/q-mem-org.png"/>
  <figcaption> <small> Fig. 7: Memory organization of the queues </small> </figcaption>
</figure>

<figure>
  <img src="/images/project-control-unit/shift-reg.png"/>
  <figcaption> <small> Fig. 8: Partial demonstration of shift register control </small> </figcaption>
</figure>

Thus, to reflect this queue transition, the control unit commences command for various event during runtime.
The control unit on the top level is demonstrated in Fig. 9.

<figure>
  <img src="/images/project-control-unit/pipeline-control-unit.png"/>
  <figcaption> <small> Fig. 9: Control unit top level design </small> </figcaption>
</figure>

The Stage Controller enables and disables the stages of the pipeline. The Queue Controller keeps the queue in synchronization with the stage behavior by moving forward the shift registers.
At this level, the machine can be seen repeating on a normal state so long as there are no hazards or exceptions.
In the event when they appear, the control unit enters states where it resolves the issue, then go back to looping state.
These states are listed in Fig. 10, along with the GO state when the machine operates normally.
The table also specifies whether to enable specific stages and the control over the queue, which will be justified in sections on hazards and exceptions.

<figure>
  <img src="/images/project-control-unit/pipeline-states.png"/>
  <figcaption> <small> Fig. 10: States </small> </figcaption>
</figure>

Structural hazards, data hazards and control hazards are addressed separately.
The main idea in our solution is stalling, or descriptively, prioritize execution (E1), and keep other stages from moving, until the hazard is unflagged.
The analysis of each can be found in the project report.
A summary is we exhaust all possible hazards, determined the true conditions, such that the implementation could be as simple as combinatorial gates.
As for control hazards, we were well aware that a dynamic branch predictor is more popular and normally more efficient.
However, since the data path design is determined before considering the control hazards, a limitation is placed to only update PC at execution (E1), making it ineffective even if the predictor predicts “taken”.
Thus, it was decided to use a branch predictor that statically predicts “not taken”.

<figure>
  <img src="/images/project-control-unit/hazard-timing.png"/>
  <figcaption> <small> Fig. 11: Hazard delay example </small> </figcaption>
</figure>

#### Takeaway

Compared to the previous assignment, though not requiring a gate-level implementation, this project was more analytically challenging for us as it requires deeper and applicable understanding of pipeline design.
Plus, we also decided on a even more ambitious goal of only allows one step in each stage.
Luckily, with the collective effort of trials and errors, we were able to make sense of everything and deliver the project in time.

Continuing the project, though not required as an assignment, we hope with capable hardware such as FPGA, we could actually implement both machines to reality.