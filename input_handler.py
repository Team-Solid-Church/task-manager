import sys
import datetime

from task import Task

class InputHandler():
    """Take input and return actions."""

    def __init__(self, user_input, display):
        self.user_input = user_input
        self.display = display

    def wizard_add_task(self):
        self.user_input.input_string = input("What is the name of your task?")
        self.task = Task()
        self.task.name = self.user_input.input_string
        self.task.created_date = datetime.now()








    def menu_handler(self):
        #add task
        if self.user_input.input_string == "1":
            self.wizard_add_task()
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