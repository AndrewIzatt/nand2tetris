import sys
import fileinput

class Parser:
    def __init__(self, input_file):
        self.file = open(input_file, 'r', encoding='utf-8')
        
    def hasMoreLines(self):
        print(self.file.readline())

    

def main():
    hack = Parser("test.asm")
    hack.hasMoreLines()
    

if __name__ == "__main__":
    main()