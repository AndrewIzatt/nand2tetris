// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
// Make sure "no animation" is selected
//Listen to the keyboard

//To blacken/clear the screen, write code that fills the entire screen memory map with either "white" or "black" pixels

// Addressing the memory requires working with pointers

// Use symbolic variables and labels
// Use sensible variable and label names
// Variables: lower case
// Labels: upper case
// Use indentation
// Start with Pseudo code

// Pseudo code
// Infinite loop
// Check if key is pressed
// If key is pressed, blacken the screen
// If key is not pressed, clear the screen
@SCREEN
M=0
@counter
M=0
@currentaddress
M=0
(INFINITE)
// Probe value of KBD
    @KBD
    D=M
    // If key is pressed, blacken the screen
    @PRESSED
    D;JGT
    // Key is not pressed, clear the screen
    @SCREEN
    D=A
    M=0
    @32
    A=D+A
    M=0
    @INFINITE
    D;0JMP
(PRESSED)
        @SCREEN
        D=A
        @n
        D=D+M
        A=D
        M=-1
        @n
        M=M+1
        @KBD
        D=M
        @INFINITE
        D;JEQ



