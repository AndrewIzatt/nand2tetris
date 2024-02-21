<<<<<<< HEAD
// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/07/MemoryAccess/PointerTest/PointerTestVME.tst

load PointerTest.vm,
output-file PointerTest.out,
compare-to PointerTest.cmp,
output-list RAM[256]%D1.6.1 RAM[3]%D1.6.1 RAM[4]%D1.6.1
            RAM[3032]%D1.6.1 RAM[3046]%D1.6.1;

set RAM[0] 256,   // initializes the stack pointer

repeat 15 {       // PointerTest.vm has 15 instructions
  vmstep;
}

// outputs the stack base, this, that, and
// some values from the the this and that segments
output;
=======
// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/07/MemoryAccess/PointerTest/PointerTestVME.tst

load PointerTest.vm,
output-file PointerTest.out,
compare-to PointerTest.cmp,
output-list RAM[256]%D1.6.1 RAM[3]%D1.6.1 RAM[4]%D1.6.1
            RAM[3032]%D1.6.1 RAM[3046]%D1.6.1;

set RAM[0] 256,   // initializes the stack pointer

repeat 15 {       // PointerTest.vm has 15 instructions
  vmstep;
}

// outputs the stack base, this, that, and
// some values from the the this and that segments
output;
>>>>>>> 3184509b3b90df5843c2b3cccf43fee134882202
