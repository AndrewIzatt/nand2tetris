// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

//// Replace this comment with your code.
@8192
D=A
@max
M=D
@position
M=0
(LOOP)
    @KBD // Check if key is pressed
    D=M
    @FILL // If key is presed, fill the screen   
    D;JGT
    @position // If it gets to here, we automatically know that no key is pressed
    D=M // Check if screen is filled in at all
    @ERASE
    D;JGE
    @NOTPRESSED
    0;JMP
(FILL)
    @SCREEN // A = 16384
    D=A
    @position // Select position counter
    A=D+M // A = 16384 + position
    M=-1 // Set memory at that location to -1
    // Check if screen is totally filled
    @max
    D=M
    @position
    D=D-M
    @LOOP // If screen is totally filled (D=0), restart loop (nothing will get filled in anymore, even if pressed)
    D;JEQ
    @position // select position
    M=M+1 // add 1 to position memory
    @LOOP // restart loop
    0;JMP
(ERASE)
    @SCREEN
    D=A
    @position
    A=D+M // This can't be bigger that 24577
    M=0
    @position
    M=M-1
(NOTPRESSED)
    @LOOP
    0;JMP