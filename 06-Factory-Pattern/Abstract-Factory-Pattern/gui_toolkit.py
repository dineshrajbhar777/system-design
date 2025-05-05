"""
Summary
Abstract Factory groups related objects (e.g., Button + Checkbox)
under a single interface.

It makes switching product families easy, and client code remains
agnostic of platform-specific classes.

Promotes loose coupling and adherence to the Open/Closed Principle.
"""

from abc import ABC, abstractmethod


# 1. Abstract Product Interfaces
class Button(ABC):
    @abstractmethod
    def render(self):
        pass


class CheckBox(ABC):
    @abstractmethod
    def render(self):
        pass


# 2. Concrete Products

class WindowsButton(Button):
    def render(self):
        return "Rendering Windows Button"


class MacButton(Button):
    def render(self):
        return "Rendering Mac Button"


class WindowsCheckBox(CheckBox):
    def render(self):
        return "Rendering Windows CheckBox"


class MacCheckBox(CheckBox):
    def render(self):
        return "Rendering Mac CheckBox"


# 3. Abstract Factory


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> CheckBox:
        pass


# 4. Concrete Factories

class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> CheckBox:
        return WindowsCheckBox()


class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> CheckBox:
        return MacCheckBox()


# 5. Client Code
def client_code(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.render())
    print(checkbox.render())


# 6. Usage
if __name__ == "__main__":
    print("Using Windows Factory:")
    client_code(WindowsFactory())

    print("\nUsing Mac Factory:")
    client_code(MacFactory())
