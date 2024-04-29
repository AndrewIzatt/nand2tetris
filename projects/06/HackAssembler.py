import os
import sys

class Parser:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        
        with open(self.file_path, 'r') as file:
            for line in file:
                if '//' in line:
                    print("Before splitting: ", line)
                    line = line.split('//')[0]
                    #line = line.split('//')[0]
                    print("After split: ", line)
                    print("This line is of type: ", type(line))
                line = line.strip()
                print("Stripped line: ", line)
                print("The line is of type: ", type(line))
                print("The line's bool value is: ", bool(line))
                if line:
                    print(line)

if __name__ == "__main__":
    hack = Parser(sys.argv[1])
    hack.parse()