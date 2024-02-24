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
// Test - Set R0 = 0; Zero out memory
// @R0
// M=0
// Test - Set R1 = 0; Zero out memory
// @R1
// M=0
// Test - Set R2 = 0; Zero out memory
// @R2
// M=0
// Test - Set Counter = 0; Zero out memory
@count
M=0
// Set Counter to value in R0
@R0
D=M
@count
M=D
(LOOP)
    @count
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

