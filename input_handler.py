class InputHandler():
    """Take input and return actions."""

    def __init__(self, user_input):
        self.user_input = user_input

    def menu_handler(self):
        if self.user_input:
            print(self.user_input)
