"""
Principle: D - Dependency Inversion Principle

    Class should depend on interfaces rather than concrete classes

Solution:

In constructor, we have assigned an object of interface i.e., Mouse and Keyboard

So we can pass any combination of mouse and keyboard i.e., wired or bluetooth
our code should be capable of handling it.
"""


class Keyboard:
    pass


class Mouse:
    pass


class WiredKeyboard(Keyboard):
    pass


class WiredMouse(Mouse):
    pass


class BluetoothKeyboard(Keyboard):
    pass


class BluetoothMouse(Mouse):
    pass


class MackBook:
    def __init__(self, keyboard: Keyboard, mouse: Mouse):
        self.keyboard = keyboard
        self.mouse = mouse
