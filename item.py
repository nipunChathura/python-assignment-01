class Item:
    def __init__(self):
        self.command = ""
        self.params = ""

    def set_command_and_params(self, command, params):
        self.command = command
        self.params = params
        if command == "singup":
            print("User is sing up")
        elif command == "login":
            print("User login")
