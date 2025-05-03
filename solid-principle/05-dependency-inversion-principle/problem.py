"""
Principle: D - Dependency Inversion Principle

    Class should depend on interfaces rather than concrete classes

Problem:

In the below code example, we are assigning the object of Concrete class

In the future, if we want to add a bluetooth mouse or keyboard, we cannot do it
because we have used concrete class

"""


class WiredKeyboard:
    pass


class WiredMouse:
    pass


class MackBook:
    def __init__(self, keyboard: WiredKeyboard, mouse: WiredMouse):
        self.keyboard = keyboard
        self.mouse = mouse
