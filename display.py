class Display():
    """What the user will actually see on the screen."""

    def __init__(self):
        pass

    MENU = {
        "1" : "1 = Add Task",
        "2" : "2 = Remove Task",
        "3" : "3 = Mark Complete",
        "4" : "4 = List Completed Tasks",
        "5" : "5 = List Unfinished Tasks",
        "Q" : "Q = Exit",
    }    

    def title (self):
        print("Task Manager")        

    def menu(self):
        for value in sorted(self.MENU.values()):
            print (value)

    def wizard (self):
        pass        



    def build_display(self):
        # import pdb; pdb.set_trace()    	
        self.title()

        self.menu()

        self.wizard()

        
