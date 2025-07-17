class CommandsForJarvis:
    def __init__(self, name, command):
        self.name = name
        self.command = command

    def greetings(self):
        return f"Hello {self.name}, my name is Jarvis."

    def farewell(self):
        return f"{self.name}, Good afternoon\nGood evening\nAnd Good night!"

    def commands_for_jarvis(self):
        self.command = {
            'Hello': {
                'function': self.greetings,
                'description': 'Greetings'
            },
            'Bye': {
                'function': self.farewell,
                'description': 'Farewell'
            },
        }