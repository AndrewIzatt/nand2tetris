// This is a comment
// Compute the sum of 42 + 19 and store the result in RAM[0]
@42
D=A          // D = 42
@19
D=D+A        // D = D + 19
@0
M=D          // RAM[0] = D (the sum)
// Infinite loop
(LOOP)
@LOOP
0;JMP        // Jump to the LOOP instruction indefinitely
