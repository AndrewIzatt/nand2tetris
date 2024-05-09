import os
import sys
import io

class Parser:
    def __init__(self, file_path):
        self.file = io.BufferedReader(open(file_path, 'rb'))

    def hasMoreLines(self):
        return bool(self.file.peek(1))

    def advance(self):
            line = self.file.readline().decode('utf-8')
            if '//' in line:
                line = line.split('//')[0]
            line = line.strip()
            if line:
                return line
    
    def instructionType(self, input):
            if input[0] == "@":
                return "A_INSTRUCTION\n"
            elif "=" in input or ";" in input: # Just for testing, everything should be a C_Instruction
                return "C_INSTRUCTION\n"
            elif input[0] == "(":
                return "L_INSTRUCTION\n" # Or an L Instruction
            else:
                 raise SyntaxError("Invalid Instruction")
    
    def symbol(self, symbolic_instruction):
         # Skipping Labels for right now
         print(f"The symbolic instruction: {symbolic_instruction}")
         return symbolic_instruction[1:]
    
    def dest(self, dest_instruction):
         pass
    
    def comp(self, comp_instruction):
         pass
         
    def jump(self, jump_instruction):
         pass

if __name__ == "__main__":
    # Remember to redo this
    hack = Parser("/home/orca/Documents/Coding/nand2tetris/projects/06/test.asm")
    output = open("/home/orca/Documents/Coding/nand2tetris/projects/06/test.hack", "w")
    while hack.hasMoreLines():
        instruction = hack.advance()
        if instruction is not None:
            instruction_type = hack.instructionType(instruction)
            if instruction_type[0] == "A" or instruction_type[0] == "L":
                parsed_instruction = hack.symbol(instruction) 
                output.write(parsed_instruction + "\n") # Move out of "If" when finished
