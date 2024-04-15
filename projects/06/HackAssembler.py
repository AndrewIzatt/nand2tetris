import sys
import fileinput

def parser(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        read_data = f.read()
        print(read_data)

    

def main():
    parser(sys.argv[1]) 
    

if __name__ == "__main__":
    main()