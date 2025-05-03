"""
Principle: L - Liskov Substitution Principle

    If Class B is subtype of Class A, then we should be able to replace
    object A with B without breaking the behaviour of the program

    Subclass should extend the capability of parent class not narrow it down

Problem:
We have Bike interface with below method
    turn_on_engine()
    accelerate()

we can extend this Bike interface to MotorCycle which has engine

but if we extend this Bike interface to Bicycle which don't have an engine,
so it narrow down the capability of parent
"""

from abc import abstractmethod, ABC


class Bike:
    @abstractmethod
    def turn_on_engine(self): pass

    @abstractmethod
    def accelerate(self): pass


class MotorCycle(Bike):
    def __init__(self, is_engin_on: bool = False, speed: float = 0):
        self.is_engin_on = is_engin_on
        self.speed = speed

    def accelerate(self):
        self.speed += 10

    def turn_on_engine(self):
        self.is_engin_on = True


class Bicycle(Bike):
    def __init__(self, speed: float = 0):
        self.speed = speed

    def turn_on_engine(self):
        raise ValueError("There is no engine")

    def accelerate(self):
        self.speed += 10
