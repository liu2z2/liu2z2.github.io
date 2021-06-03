---
Title: A Chiptune Music System with OPL2 and Reality Adlib Tracker
Date: 2019-12-02
Status: published
Tags: project
---
[TOC]


The source of the project can be found at my GitHub [repo](https://github.com/liu2z2/opl2-chiptune).

The objective of the project is to build a system with the old-school electronic components that plays Chiptune music, as well as composing the music with compatible software. This is a project for the class Japanese Music Online during Fall 2019 semester.  Dr. Kazuaki Shiota was really nice to let me do this for the final project of the class. The project helped me understand the theory behind Chiptune Music from a musical and engineering standpoint. 

### How Chiptune Music Works

#### Beeper Speakers
In embedded systems, I have experimented generating music made by square-waves with a piezoelectric speaker. The tone of the music is adjusted by the frequency of the square waves, as a method called "Frequency Modulation (FM)". Such "beeper speaker" system is how early home computers generate sounds, except the CPU also handles other processes as a normal PC does (Figure 1). Different tones can be played by varying the frequency of the square waves, however, it requires all of the CPU's run-time to implement advanced sound of music. 

#### FM Synthesizer
To solve this issue, computers in the early 1980's use dedicated sound chip (Figure 2), which is the early form of the sound cards in today's computers. Except for taking the processing load away from the CPU, this method also creates possibility to develop more advanced sound generation and even synthesis. Three examples can be examined as examples.

<figure>
  <img src="/images/project-chiptune/fm-synth.png"/>
  <figcaption> <small> Figure 1 (Left) - Non-Dedicated Sound Chip; Figure 2 (Right) - Dedicated Sound Chip </small> </figcaption>
</figure>

#### Nintendo Entertainment System (NES)
The sound chip in NES is able to generate five channels, each of which features different types of waveforms (Figure 3). Channel #1 and #2 gives square waves, Channel #3 gives triangle waves, Channel #4 gives noise and Channel #5 is PCM sample, which modulate pre-recorded sound waves. Though the tone can be different, this method makes the music sounds like being played by the same set of instruments. 

<figure>
  <img src="/images/project-chiptune/NES.png"/>
  <figcaption> <small> Figure 3 - NES Sound Chip </small> </figcaption>
</figure>

#### Commodore 64
Commodore uses a different approach to synthesize music. The chip has 3 channels, each of which can produce waveforms among square, triangle and sawtooth wave (Figure 4) . Initially, engineers assign used to assign one waveform to a channel and write the tone associated with the wave. This seems inferior to the NES system as it only has 3 channels, despite that the combination of the waveforms can be variable. However, later engineers realized that waveform can be reassigned to channels on the fly, which has opened a great amount of variability to the music. This methods have been proved successful and extended to the next generation of sound card in PC. 

<figure>
  <img src="/images/project-chiptune/C64.png"/>
  <figcaption> <small> Figure 4 - Commodore 64 Sound Chip </small> </figcaption>
</figure>

#### Adlib/Sound-Blaster Card
As an improved version of the Commodor 64 sound chip, the Adlib Sound Card is used in the later IBM PC. The Card is replaced with Sound Blaster later due to the market loss,  but the key component - YM3812 FM Operator chip is used in both boards. This chip is considered the foundation of computer music on IBM PC for a decade, and can even found in some Yamaha electronic piano keyboards. 

**YM3812** is an Frequency Modulation Operator Type-L2 (OPL2) integrated chip that can simultaneously generate 9 channels of different types of waveforms. Since this chip was widely used in early computer systems, there are still supporting documents, software, and projects related to it, so it has been determined as the core of this project as well. 

### Hardware Setup
Figure 5 is the hardware setup of the system in block diagram. The music file stored in the SD card is read by the microcontroller (μC). The OPL2 chip uses 4-line bus for control signal and 8-line bus for data transfer. To reduce the load on the microcontroller, the data is sent in serial first to a shift register, and then transmitted to the OPL2 chip after the conversion. The digital output of the FM operation is thereafter transferred to a DAC, whose analog output is amplified to become the eventual sound that can be played by a speaker. 

<figure>
  <img src="/images/project-chiptune/block.png"/>
  <figcaption> <small> Figure 5 - Block Diagram </small> </figcaption>
</figure>

The detailed schematic of the system is in Figure 9. It is made in KiCAD, a free CAD software for PCB design. In order to reduce the cross-talk and noise of the system, it was decided to make the system into a PCB. After a few hours' layout design, the final version of the board (Figure 10) is submitted to OSH Park Proto-PCB Service. 

The KiCAD files are available in the GitHub repository attached at the begining of the post. 

<figure>
  <img src="/images/project-chiptune/schematic.png"/>
  <figcaption> <small> Figure 6 - Circuit Schematic </small> </figcaption>
</figure>

<figure>
  <img src="/images/project-chiptune/pcb.png"/>
  <figcaption> <small> Figure 7 - PCB Demo </small> </figcaption>
</figure>

### Software
The software portion of the project consists of the controlling program on the microcontroller and the music composing software. 

Since the microcontroller is determined to be Arduino Uno as it's the most available option, the controlling program is written in C++ in Arduino IDE. In addition to an external OPL2 library that handles the communication protocol, libraries such as SD and SPI are included too for the SD module board. The Arduino code is available in the GitHub repository attached at the end of the post. 

Reality Adlib Tacker II (Figure 11) is the software for me to compose the music. It is a music tracker with an old-school GUI but an extensive documentation. 

<figure>
  <img src="/images/project-chiptune/reality.png"/>
  <figcaption> <small> Figure 8 - Reality Adlib Tracker </small> </figcaption>
</figure>

### Result Demonstration
Before the PCB design is manufactured, an alpha prototype is made on a breadboard, in order to test the functionality of the design. The video below demonstrates the alpha system playing a sample test music.

<iframe width="560" height="315" src="https://www.youtube.com/embed/rFG_2tbkUiI" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Knowing that the design is functional, the next phase was a hardware and software upgrade. Hardware-wise, the PCB was sent to the manufacturer and assembled later. Software-wise, a specific piece of music was chosen to be recreated with the Tracker by myself. The video below is the final version of the system, playing Megalovania from the game Undertale.

### Summary and Recommendation

To me, this multi-disciplinary project was not only successful but also meaningful. 

In a music standpoint, I learned how early electronic/computer music works and experienced the same method of composing it as the early 1900s game designed did. I am amazed too by the ingenuity of them making a variety of music with such limited system. Luckily, chiptune (or 8-bit) music remains as a featured style of music nowadays, which, to some extent, pays a tribute to those who used to work on electronic music composition. 

In an electrical engineering standpoint, this is a thorough embedded system engineering project starting from an idea, to research, design, assembly, testing and eventually realization. A lot of effort was used in designing the circuit, which is one of reasons of deciding to make a PCB. I also gained experience in audio engineering, such as signal amplification and reducing noise. 


Finally, some recommendations are listed for future improvement.

1. Instead of using Arduino Uno board, the system can be simpler by integrating Teensy board into the PCB. Thus, the system will become an actual sound card. 
2. The OPL2 library was used, but not fully understood yet. Reading through the code may help understanding the theories of operation even more.
3. The process of loading the sound file in the SD card is time-consuming. It can be improved by developing a direct interface with PC and the system. 