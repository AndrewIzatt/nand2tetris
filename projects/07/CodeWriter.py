<<<<<<< HEAD
class Parser:
    def __init__(self, input_file):
        self.output_file = input_file.replace(".vm", ".asm")

    def write_arithmetic(self, command):
        # Translate arithmetic VM commands to Hack assembly
        pass

    def write_push_pop(self, command_type, segment, index):
        # Translate push/pop VM commands to Hack assembly
        pass

    def close(self):
        # Close the output file/stream
=======
class Parser:
    def __init__(self, input_file):
        self.output_file = input_file.replace(".vm", ".asm")

    def write_arithmetic(self, command):
        # Translate arithmetic VM commands to Hack assembly
        pass

    def write_push_pop(self, command_type, segment, index):
        # Translate push/pop VM commands to Hack assembly
        pass

    def close(self):
        # Close the output file/stream
>>>>>>> 3184509b3b90df5843c2b3cccf43fee134882202
        self.file.close()