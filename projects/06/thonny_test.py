import sys
import fileinput

def main():
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        print(f.readlines())
        print("hello world")    

if __name__ == "__main__":
    main()