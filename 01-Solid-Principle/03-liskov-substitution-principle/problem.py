"""
Principle: L - Liskov Substitution Principle

    If Class B is a subtype of Class A, then we should be able to replace
    object A with B without breaking the behavior of the program

    Subclass should extend the capability of parent class not narrow it down

Problem:
We have Vehicle interface with-below-method
    has_engine()
    get_number_of_wheels()

We can extend this Vehicle interface to a MotorCycle, a Car which has an engine

But if we extend this Vehicle interface to a Bicycle which doesn't have an engine,
and it will break the code, and also it narrows down the capability of parent
"""

from abc import abstractmethod, ABC


class Vehicle:
    @abstractmethod
    def has_engine(self): pass

    def get_number_of_wheels(self):
        return 2


class MotorCycle(Vehicle):

    def has_engine(self):
        return True


class Car(Vehicle):
    def has_engine(self):
        return True

    def get_number_of_wheels(self):
        return 4


class Bicycle(Vehicle):
    def has_engine(self):
        raise ValueError(f"{self.__class__.__name__} does not have engine.")


if __name__ == "__main__":
    vehicle_list: list[Vehicle] = [
        MotorCycle(),
        Car(),
        Bicycle()
    ]

    for vehicle in vehicle_list:
        print(f"{vehicle.__class__.__name__} has engine:= {vehicle.has_engine()}")
