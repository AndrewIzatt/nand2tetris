<<<<<<< HEAD
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
=======
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
// i = 0
// if (R1 - i == 0) go to end
//Set R0 = 5
// @5
// D=A
// @R0
// M=D
//Set R1 = 7
// @7
// D=A
// @R1
// M=D
// Set i = 0
// Set R2 = 0; Zero out memory
@R2
M=0
(LOOP)
    @R1
    D=M
    @END
    D;JLE
    //Add value of R0 into R2
    @R0
    D=M
    @R2
    M=M+D
    // Decrement R1
    @R1
    M=M-1
    // If R1 == 0, go to end
    @LOOP
    0;JMP
(END)
    @END
    0;JMP

>>>>>>> 3184509b3b90df5843c2b3cccf43fee134882202
