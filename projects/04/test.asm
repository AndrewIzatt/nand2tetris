<<<<<<< HEAD
@SCREEN
D=A
M=-1
@32
A=D+A
M=-1
@SCREEN
D=A
M=0
@32
A=D+A
M=0
// @R0
// D=M
// @END
// D;JLE

// @16
// M=D
// @SCREEN
// D=A 
// @17
// M=D
// @17
// A=M
// M=-1
// @17
// D=M
// @32
// D=D+A
// @17
// M=D
// @16
// MD=M-1

// @MAIN
// D;JGT
// (END)
// @END
// 0;JMP

// //Starting at base address R0, 
// // Sets the first R1 words to -1
//     // n = 0
//     @n
//     M=0
// (LOOP)
//     // if (n == R1) goto END
//     @n
//     D=M
//     @R1
//     D=D-M
//     @END
//     D;JEQ
//     // *(R0 + n) = -1
//     @R0
//     D=M
//     @n
//     A=D+M
//     M=-1
//     // n = n + 1
//     @n
//     M = M+1
//     // go to LOOP
//     @LOOP
//     0;JMP
// (END)
//     @END
//     0;JMP

//WORKING LOOP 1
// @SCREEN
// M=0
// @n
// M=0
// (LOOP)
// @SCREEN
// D=A
// @n
// D=D+M
// A=D
// M=-1
// @n
// M=M+1
// @LOOP
// 0;JMP
=======
@SCREEN
D=A
M=-1
@32
A=D+A
M=-1
@SCREEN
D=A
M=0
@32
A=D+A
M=0
// @R0
// D=M
// @END
// D;JLE

// @16
// M=D
// @SCREEN
// D=A 
// @17
// M=D
// @17
// A=M
// M=-1
// @17
// D=M
// @32
// D=D+A
// @17
// M=D
// @16
// MD=M-1

// @MAIN
// D;JGT
// (END)
// @END
// 0;JMP

// //Starting at base address R0, 
// // Sets the first R1 words to -1
//     // n = 0
//     @n
//     M=0
// (LOOP)
//     // if (n == R1) goto END
//     @n
//     D=M
//     @R1
//     D=D-M
//     @END
//     D;JEQ
//     // *(R0 + n) = -1
//     @R0
//     D=M
//     @n
//     A=D+M
//     M=-1
//     // n = n + 1
//     @n
//     M = M+1
//     // go to LOOP
//     @LOOP
//     0;JMP
// (END)
//     @END
//     0;JMP

//WORKING LOOP 1
// @SCREEN
// M=0
// @n
// M=0
// (LOOP)
// @SCREEN
// D=A
// @n
// D=D+M
// A=D
// M=-1
// @n
// M=M+1
// @LOOP
// 0;JMP
>>>>>>> 3184509b3b90df5843c2b3cccf43fee134882202
