import sys

class InputHandler():
    """Take input and return actions."""

    def __init__(self, user_input):
        self.user_input = user_input

    def menu_handler(self):
    	if self.user_input.input_string == "1":
    		pass
    	elif self.user_input.input_string == "2":
            pass
    	elif self.user_input.input_string == "3":
    		pass
    	elif self.user_input.input_string == "4":
    		pass
    	elif self.user_input.input_string == "5":
    		pass
    	elif self.user_input.input_string == "Q" or self.user_input.input_string == "q":
    		sys.exit()