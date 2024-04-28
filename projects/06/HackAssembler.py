import os
import sys

class Parser:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        with open(self.file_path, 'r') as file:
            for line in file:
                if '//' in line:
                    line = line.split('//')[0]
                line = line.strip()
                if line:
                    print(line)

if __name__ == "__main__":
    parser = Parser(sys.argv[1])
    parser.parse()