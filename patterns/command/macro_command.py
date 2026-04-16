class MacroCommand:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def execute(self):
        results = []
        for command in self.commands:
            results.append(command.execute())
        return results