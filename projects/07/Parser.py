<<<<<<< HEAD
class Parser:
    def __init__(self, input_file):
        self.file = open(input_file, "r")
        self.current_command = None

    def has_more_commands(self):
        # Check if there are more commands in the input file
        while True:
            line = self.file.readline()
            if not line:
                return False
            # Remove leading and trailing whitespace and ignore comments
            clean_line = line.strip()
            if clean_line and not clean_line.startswith("//"):
                self.current_command = clean_line
                return True

    def advance(self):
        # Read the next command from the input file
        self.current_command = self.file.readline().strip()

    def command_type(self):
        # Determine the type of the current command (C_ARITHMETIC, C_PUSH, C_POP, etc.)
        if self.current_command.startswith("push"):
            return "C_PUSH"
        elif self.current_command.startswith("pop"):
            return "C_POP"
        elif self.current_command.startswith("label"):
            return "C_LABEL"
        elif self.current_command.startswith("goto"):
            return "C_GOTO"
        elif self.current_command.startswith("if-goto"):
            return "C_IF"
        elif self.current_command.startswith("function"):
            return "C_FUNCTION"
        elif self.current_command.startswith("return"):
            return "C_RETURN"
        elif self.current_command.startswith("call"):
            return "C_CALL"
        else:
            return "C_ARITHMETIC"

    def arg1(self):
        # Get the first argument of the current command
        pass

    def arg2(self):
        # Get the second argument of the current command (for C_PUSH and C_POP)
        pass
=======
class Parser:
    def __init__(self, input_file):
        self.file = open(input_file, "r")
        self.current_command = None

    def has_more_commands(self):
        # Check if there are more commands in the input file
        while True:
            line = self.file.readline()
            if not line:
                return False
            # Remove leading and trailing whitespace and ignore comments
            clean_line = line.strip()
            if clean_line and not clean_line.startswith("//"):
                self.current_command = clean_line
                return True

    def advance(self):
        # Read the next command from the input file
        self.current_command = self.file.readline().strip()

    def command_type(self):
        # Determine the type of the current command (C_ARITHMETIC, C_PUSH, C_POP, etc.)
        if self.current_command.startswith("push"):
            return "C_PUSH"
        elif self.current_command.startswith("pop"):
            return "C_POP"
        elif self.current_command.startswith("label"):
            return "C_LABEL"
        elif self.current_command.startswith("goto"):
            return "C_GOTO"
        elif self.current_command.startswith("if-goto"):
            return "C_IF"
        elif self.current_command.startswith("function"):
            return "C_FUNCTION"
        elif self.current_command.startswith("return"):
            return "C_RETURN"
        elif self.current_command.startswith("call"):
            return "C_CALL"
        else:
            return "C_ARITHMETIC"

    def arg1(self):
        # Get the first argument of the current command
        pass

    def arg2(self):
        # Get the second argument of the current command (for C_PUSH and C_POP)
        pass
>>>>>>> 3184509b3b90df5843c2b3cccf43fee134882202
