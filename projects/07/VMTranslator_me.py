from Parser import Parser
from CodeWriter import CodeWriter

class VMTranslator:
    def __init__(self, input_file):
        self.parser = Parser(input_file)
        self.code_writer = CodeWriter(input_file)

    def translate_vm_to_hack(self):
        while self.parser.has_more_commands():
            self.parser.advance()
            command_type = self.parser.command_type()

            if command_type == "C_ARITHMETIC":
                self.code_writer.write_arithmetic(self.parser.arg1())
            elif command_type in ["C_PUSH", "C_POP"]:
                self.code_writer.write_push_pop(command_type, self.parser.arg1(), self.parser.arg2())
            # Add more conditions for other command types as needed

if __name__ == "__main__":
    input_file = "VMTranslator_me.py"  # Replace with your VM file name
    vm_translator = VMTranslator(input_file)
    vm_translator.translate_vm_to_hack()
    vm_translator.code_writer.close()  # Close the output file