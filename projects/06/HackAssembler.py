import sys
import fileinput

class Parser(self, input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        read_data = f.read()
        print(read_data)

    # def hasMoreLines(self, input_file):


    

def main():
    hack = Parser()
    hack.hasMoreLines(sys.argv[1]) 
    

if __name__ == "__main__":
    main()