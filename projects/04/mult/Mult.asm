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
// Initialize R2
@R2
M=0
// Enter Value of R0
// Initialize R0
@3
D=A
@R0
M=D
// Enter Value of R1
// Initialize R1
@5
D=A
@R1
M=D
// Counter as value of R0
(LOOP)
// Loop R0 times (if R0 == 0, stop)
@R0
D=M

// Value of R1 into R2
@R2
   // Subtract 1 from R0