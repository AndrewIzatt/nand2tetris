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
                print(line)

if __name__ == "__main__":
    # Remember to redo this
    hack = Parser("/home/orca/Documents/Coding/nand2tetris/projects/06/test.asm")
    while hack.hasMoreLines():
        hack.advance()
    print("This is the end.")