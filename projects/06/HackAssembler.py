import sys
import fileinput

class Parser:
    def __init__(self, file_path):
            self.file_path = file_path
            self.file_object = None  # Placeholder for the file object
            
            # Open the file
            try:
                self.file_object = open(file_path, 'r', encoding='utf-8')
            except FileNotFoundError:
                print(f"File '{file_path}' not found.")
    
    def hasMoreLines(self, entry):
        if entry[-1] == "\n":
            return True
        self.file_object.close()
        return False

    
    def advance(self, second_entry):
            instruction, _, comment = second_entry.partition('//')  # Split the line into instruction and comment parts
            trimmed_instruction = instruction.strip()  # Remove leading and trailing whitespace from the instruction
            if trimmed_instruction == "":  # Check if the instruction part is empty after stripping whitespace
                return None    
            return trimmed_instruction

def main():
    hack = Parser("/home/orca/Documents/Coding/nand2tetris/projects/06/test.asm")
    print(type(hack.file_object))
    # hack2 = open("/home/orca/Documents/Coding/nand2tetris/projects/06/test.asm", 'r', encoding='utf-8')
    # hack = Parser(sys.argv[1])
    # Lines = hack.file_object.readlines()
    # for line in Lines:
    #     if hack.hasMoreLines(line):
    #         cleanedline = hack.advance(line)
    #         if cleanedline is None:
    #             continue
    #         print(cleanedline)
    while hack.hasMoreLines():
        line = hack.file_object.readline()
        cleanedline = hack.advance(line)
        if cleanedline is None:
            continue
        print(cleanedline)


if __name__ == "__main__":
    main()