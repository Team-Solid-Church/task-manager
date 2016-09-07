import sys
import datetime

from task import Task

def sort_task_list(task_list):
    list_to_return = ''
    for index, item in enumerate(task_list):
        list_to_return += ("\t{} = {}\n".format(index, item))
    return list_to_return

class InputHandler():
    """Take input and return actions."""

    def __init__(self, user_input, display, task_list):
        self.user_input = user_input
        self.display = display
        self.task_list = task_list

    def wizard_add_task(self):
        self.user_input.input_string = input("What is the name of your task?")
        self.task = Task()
        self.task.name = self.user_input.input_string
        self.task.created_date = datetime.datetime.now()
        self.task_list.append(self.task)
        self.display.display_info = '\tTask created!'

    def wizard_remove_task(self):
        if self.task_list:
            self.display.display_info = sort_task_list(self.task_list)
        else:
            self.display.display_info = "No tasks to display."

    def menu_handler(self):
        #add task
        if self.user_input.input_string == "1":
            self.wizard_add_task()
        elif self.user_input.input_string == "2":
            self.wizard_remove_task()
        elif self.user_input.input_string == "3":
            pass
        elif self.user_input.input_string == "4":
            pass
        elif self.user_input.input_string == "5":
            pass
        elif self.user_input.input_string == "Q" or self.user_input.input_string == "q":
            sys.exit()