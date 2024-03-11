// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

//// Replace this comment with your code.
@position
M=0
(INFINITE) // Infinite Loop
// Check Value of Keyboard Input
@KBD
D=M
@PRESSED1
D;JGT
// Scenarios
// 1. A key is pressed
    (PRESSED1) // Outermost Loop
    // 2. A key is pressed and then released 
        // Or 3. No key is pressed
        // Is there any pixels filled in with black?
        // Yes?
            // Find Last Most Pixel and Clear it
        // No?
            // Go back to INFINITE Loop 
@INFINITE
0;JMP