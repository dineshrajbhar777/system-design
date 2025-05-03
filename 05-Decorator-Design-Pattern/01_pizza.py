"""
This pattern helps to add more functionality to an existing object,
without changing its structure

Class BasePizza and ToppingDecorator have both relationships
    IS-A and Has-A

"""

from abc import ABC, abstractmethod

"""
Pizza base
"""


class BasePizza(ABC):
    @abstractmethod
    def cost(self): pass


class FarmHouse(BasePizza):
    def cost(self):
        return 200


class VegDelight(BasePizza):
    def cost(self):
        return 120


class Margherita(BasePizza):
    def cost(self):
        return 100


"""
    Pizza Topping Decorator
"""


class ToppingDecorator(BasePizza, ABC):
    pass


class ExtraCheese(ToppingDecorator):
    def __init__(self, pizaa: BasePizza):
        self._pizaa = pizaa

    def cost(self):
        return self._pizaa.cost() + 10


class Mushroom(ToppingDecorator):
    def __init__(self, pizaa: BasePizza):
        self._pizaa = pizaa

    def cost(self):
        return self._pizaa.cost() + 15


def display_cost(pizaa: BasePizza):
    print(f"{pizaa.__class__.__name__} cost:= {pizaa.cost()}")


if __name__ == "__main__":
    print(f"{'-' * 10} Decorator Design Pattern {'-' * 10}")

    pizaa = Margherita()
    display_cost(pizaa)

    print("Add extra cheese")
    pizaa = ExtraCheese(pizaa)
    display_cost(pizaa)

    print("Add mushroom cheese")
    pizaa = Mushroom(pizaa)
    display_cost(pizaa)

    print("Add extra cheese")
    pizaa = ExtraCheese(pizaa)
    display_cost(pizaa)
