import os

MENU = {
    "1" : "1 = Add Task",
    "2" : "2 = Remove Task",
    "3" : "3 = Mark Complete",
    "4" : "4 = List Completed Tasks",
    "5" : "5 = List Unfinished Tasks",
    "Q" : "Q = Exit",
}    

class Display():
    """What the user will actually see on the screen."""

    def __init__(self, task_list):
        self.display_info = ""
        self.task_list = task_list
        self.current_menu = MENU

    def menu(self):
        print("\n")
        try:
            for value in sorted(self.current_menu.values()):
                print ("\t" + str(value))
        except TypeError:
            self.current_menu = {str(key): value for key, value in self.current_menu.items()}
            for key in sorted(self.current_menu):
                print("\t{} = {}".format(key, self.current_menu[key]))

    def title (self):
        print("\tTASK MANAGER")        

    #information sent back to user from the input_handler        
    def handler_output (self):
        print("\n")
        print("\t" + self.display_info)



    def build_display(self):
        # import pdb; pdb.set_trace()    	
        
        os.system('clear')
        # print("*" * 10)

        self.title()

        self.menu()

        self.handler_output()

        
