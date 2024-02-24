// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.
//Set R0 = 3
@3
D=A
@R0
M=D
//Set R1 = 5 
@5
D=A
@R1
M=D
// Set R2 = 0; Zero out memory
@R2
M=0
(LOOP)
    @R0
    M=M-1
    D=M
    @STOP
    D;JLT
    @R1
    D=M
    @R2
    M=D+M
    @LOOP
    0;JMP
(STOP)
    @STOP
    0;JMP

