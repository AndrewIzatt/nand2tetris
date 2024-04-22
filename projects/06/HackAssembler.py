import sys
import fileinput

class Parser:
    def __init__(self, input_file):
        self.file = open(input_file, 'r', encoding='utf-8')
    
    def hasMoreLines(self):
        for line in self.file:
            if line[-1] == '\n':
                return True
        return False
    
    def advance(self):
        for line in self.file:
            instruction, _, comment = line.partition('//')  # Split the line into instruction and comment parts
            trimmed_instruction = instruction.strip()  # Remove leading and trailing whitespace from the instruction
            if not trimmed_instruction:  # Check if the instruction part is empty after stripping whitespace
                continue
            return trimmed_instruction

def main():
    hack = Parser(sys.argv[1])
    while True:
        hack_boolean = hack.hasMoreLines()
        print(hack_boolean)
        if not hack_boolean:
            break
        next_line = hack.advance()
        print(next_line)

if __name__ == "__main__":
    main()