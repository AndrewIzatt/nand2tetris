# ruff: noqa: E501
import sys

# Define the predefined symbols for the Hack computer architecture
SYMBOLS = {
    # Predefined symbols for general-purpose registers
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
    "SCREEN": 16384,
    "KBD": 24576,
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "R4": 4,
    "R5": 5,
    "R6": 6,
    "R7": 7,
    "R8": 8,
    "R9": 9,
    "R10": 10,
    "R11": 11,
    "R12": 12,
    "R13": 13,
    "R14": 14,
    "R15": 15,
}

# Global tables for mapping mnemonics to binary representation
COMP_TABLE = {
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",
    "!D": "0001101",
    "!A": "0110001",
    "-D": "0001111",
    "-A": "0110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "D+A": "0000010",
    "D-A": "0010011",
    "A-D": "0000111",
    "D&A": "0000000",
    "D|A": "0010101",
    "M": "1110000",
    "!M": "1110001",
    "-M": "1110011",
    "M+1": "1110111",
    "M-1": "1110010",
    "D+M": "1000010",
    "D-M": "1010011",
    "M-D": "1000111",
    "D&M": "1000000",
    "D|M": "1010101"
}



DEST_TABLE = {
    "null": "000",
    "M": "001",
    "D": "010",
    "DM": "011",
    "MD": "011",
    "A": "100",
    "AM": "101",
    "MA": "101",
    "AD": "110",
    "DA": "110",
    "ADM": "111",
    "AMD": "111",
    "DAM": "111",
    "DMA": "111",
    "MAD": "111",
    "MDA": "111",
}

JUMP_TABLE = {
    "null": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111",
}

def parse_instruction(instruction):
    # Implement the parsing logic to break down an assembly instruction
    # Remove any whitespace and comments
    print("Calling parse_instruction() Function")
    instruction = instruction.strip()
    if "//" in instruction:
        print("instruction contains '//' and/or 'whitespace'") # Debug statement
        instruction = instruction.split("//")[0].strip()
    print("instruction: ", instruction) # Debug statement

    # A-instruction
    if instruction.startswith("@"):
        print("instruction starts with '@'") # Debug statement
        parsed_instruction = ("A", instruction[1:]) # creates A-instruction tuple
    # Label declaration
    elif instruction.startswith("(") and instruction.endswith(")"):
        print("instruction starts with '(' and ends with ')'") # Debug statement
        parsed_instruction = ("LABEL", instruction[1:-1])
    # C-instruction
    else:
        print("instruction is C-instruction") # Debug statement
        dest = ""  # Default value for dest
        jump = ""  # Default value for jump
        comp = instruction

        if "=" in instruction:
            print("instruction contains '='") # Debug statement
            dest, comp = instruction.split("=")

        if ";" in comp:
            print("comp contains ';'") # Debug statement
            comp, jump = comp.split(";")

        parsed_instruction = ("C", dest.strip(), comp.strip(), jump.strip())

        print("dest: ", dest) # Debug statement
        print("jump: ", jump) # Debug statement

    return parsed_instruction



def assemble(assembly_code):
    print("Calling Assemble() Function")
    binary_code = []
    #symbol_table = {}
    next_available_address = 16  # Start assigning memory addresses to variables from RAM address 16

    # First pass: Handle label declarations and variable symbols
    print("First pass: Handle label declarations and variable symbols")
    line_number = 0
    print("line_number: ", line_number) # Debug statement
    for instruction in assembly_code:
        # Remove leading/trailing whitespace and comments
        instruction = instruction.strip()
        print("instruction: ", instruction) # Debug statement
        print(f"instruction boolean value: {bool(instruction)}")
        if not instruction or instruction.startswith("//"):
            continue  # Skip empty lines and comments

        parsed_instruction = parse_instruction(instruction)
        print("parsed_instruction: ", parsed_instruction) # Debug statement

        if parsed_instruction[0] == 'LABEL':
            label_name = parsed_instruction[1]
            print("label_name: ", label_name) # Debug statement
            # Add the label and its associated memory address to the symbol table
            SYMBOLS[label_name] = line_number
            print("SYMBOLS[label_name]: ", SYMBOLS[label_name])
        else:
            # Only count lines that are not label declarations
            line_number += 1
            print("line_number: ", line_number) # Debug statement

    # Second pass: Translate assembly instructions to machine code
    print("Second pass: Translate assembly instructions to machine code")
    for instruction in assembly_code:
        # Remove leading/trailing whitespace and comments
        print("Removing leading/trailing whitespace and comments") # Debug statement
        print("Instruction before instruction.strip(): ", instruction) # Debug statement
        instruction = instruction.strip()
        print("instruction: ", instruction) # Debug statement
        if not instruction or instruction.startswith("//"):
            continue  # Skip empty lines and comments

        parsed_instruction = parse_instruction(instruction)

        print("parsed_instruction: ", parsed_instruction) # Debug statement
        if parsed_instruction[0] == 'A':
            # Handle A-instruction
            print("Handling A-instruction")
            address = parsed_instruction[1]
            print("address: ", address) # Debug statement
            if address.isdigit():
                # Direct address
                print("address is digit") # Debug statement
                binary_code.append(f"0{int(address):015b}")
            else:
                # Symbolic address or variable
                if address not in SYMBOLS:
                    print("address not in SYMBOLS") # Debug statement
                    # New variable, assign the next available address
                    SYMBOLS[address] = next_available_address
                    print("next_available_address: ", next_available_address) # Debug statement
                    next_available_address += 1
                binary_code.append(f"0{SYMBOLS[address]:015b}")

        elif parsed_instruction[0] == 'C':
            # Handle C-instruction
            print("Handling C-instruction")
            dest = parsed_instruction[1]
            comp = parsed_instruction[2]
            jump = parsed_instruction[3]

            # Ensure empty mnemonics are handled with defaults
            dest = dest if dest else "null"
            comp = comp if comp else "null"
            jump = jump if jump else "null"

            print("dest: ", dest) # Debug statement
            print("comp: ", comp) # Debug statement
            print("jump: ", jump) # Debug statement
            # Translate the C-instruction into binary representation
            binary_code.append(f"111{COMP_TABLE[comp]}{DEST_TABLE[dest]}{JUMP_TABLE[jump]}")

    print("binary_code: ", binary_code) # Debug statement
    return binary_code


def main():
    if len(sys.argv) != 3:
        print("Usage: python assembler.py <input_file.asm> <output_file.hack>")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, "r") as file:
        assembly_code = file.readlines()

    binary_code = assemble(assembly_code)

    with open(output_file, "w") as file:
        for line in binary_code:
            file.write(line + "\n")

if __name__ == "__main__":
    main()
