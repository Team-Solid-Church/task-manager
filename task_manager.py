"""Maintains program loop."""

from display import Display
from user_input import UserInput
from input_handler import InputHandler

running = True


def main():
    task_list = []
    display = Display(task_list)
    user_input = UserInput()
    input_handler = InputHandler(user_input, display, task_list)

    while running:
        display.build_display()
        user_input.get_user_input()
        input_handler.menu_handler()


if __name__ == '__main__':
    main()
