import sys
import fileinput

class Parser:
    def __init__(self, input_file):
        self.file = open(input_file, 'r', encoding='utf-8')
    
    def hasMoreLines(self):
        for line in self.file:
            # if line[-1] == '\n':
                # return True
            if line[-1] != '\n':
                return True
        return False
    
    # def advance(self):
    #         instruction, _, comment = self.line.partition('//')  # Split the line into instruction and comment parts
    #         trimmed_instruction = instruction.strip()  # Remove leading and trailing whitespace from the instruction
    #         if trimmed_instruction:  # Check if the instruction part is empty after stripping whitespace
    #             return trimmed_instruction
# def main():
#     hack = Parser(sys.argv[1])
#     for instruction in hack.advance():
#         print(instruction)

# def main():
#     hack = Parser(sys.argv[1])
#     while hack.hasMoreLines():
#         next_line = hack.advance()
#         print(type(next_line))


# Original main()
def main():
    hack = Parser(sys.argv[1])
    while hack.hasMoreLines():
        next_line = hack.advance()
        if next_line:
            print(next_line)

if __name__ == "__main__":
    main()