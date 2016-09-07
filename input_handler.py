import sys
import datetime

from task import Task
from display import MENU


def sort_task_list(task_list):        
    return {index + 1 : item for index, item in enumerate(task_list)}


class InputHandler():
    """Take input and return actions."""

    def __init__(self, user_input, display, task_list):
        self.user_input = user_input
        self.display = display
        self.task_list = task_list
        self.sub_menu_dict = {}
        self.sub_menu = False


    def wizard_add_task(self):
        self.user_input.input_string = input("What is the name of your task?")
        self.task = Task()
        self.task.name = self.user_input.input_string
        self.task.created_date = datetime.datetime.now()
        self.task_list.append(self.task)
        self.display.display_info = '\tTask created!'


    def create_sub_menu(self):
        sorted_sub_menu = sort_task_list(self.task_list)
        sorted_sub_menu["Q"] = "Q = Back"
        self.sub_menu_dict = sorted_sub_menu


    def wizard_remove_task(self):
        if self.task_list:
            self.create_sub_menu()
            self.display.current_menu = self.sub_menu_dict
        else:
            self.display.display_info = "No tasks to display."


    def menu_handler(self):
        if self.display.current_menu == MENU and self.sub_menu == False:
            #add task
            if self.user_input.input_string == "1":
                self.wizard_add_task()
            elif self.user_input.input_string == "2":
                self.wizard_remove_task()
                self.sub_menu = True
            elif self.user_input.input_string == "3":
                pass
            elif self.user_input.input_string == "4":
                pass
            elif self.user_input.input_string == "5":
                pass
            elif self.user_input.input_string == "Q" or self.user_input.input_string == "q":
                sys.exit()
        else:
            self.display.current_menu = self.sub_menu_string







