import os

class Parser:
    def __init__(self, file_path):
        self.file_object = open(file_path, 'r', encoding='utf-8')
        self.current_instruction = None

    def hasMoreLines(self):
        current_position = self.file_object.tell()
        self.file_object.seek(0, os.SEEK_END)
        end_position = self.file_object.tell()
        self.file_object.seek(current_position)
        return current_position != end_position

    def advance(self):
        line = self.file_object.readline()
        instruction, _, comment = line.partition('//')  # Split the line into instruction and comment parts
        trimmed_instruction = instruction.strip()  # Remove leading and trailing whitespace from the instruction
        if trimmed_instruction == "":  # Check if the instruction part is empty after stripping whitespace
            return None
        self.current_instruction = trimmed_instruction
        return self.current_instruction

def main():
    hack = Parser("/home/orca/Documents/Coding/nand2tetris/projects/06/test.asm")
    while hack.hasMoreLines():
        cleanedline = hack.advance()
        if cleanedline is None:
            continue
        print(cleanedline)


if __name__ == "__main__":
    main()