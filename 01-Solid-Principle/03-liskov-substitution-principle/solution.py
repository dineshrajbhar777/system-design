"""
Principle: L - Liskov Substitution Principle

    If Class B is a subtype of Class A, then we should be able to replace
    object A with B without breaking the behavior of the program

    Subclass should extend the capability of parent class not narrow it down

Solution:

In parent class keep only generic methods which are common for all
"""

from abc import abstractmethod, ABC


class Vehicle:
    def get_number_of_wheels(self):
        return 2


class EngineVehicle(Vehicle):
    def has_engine(self):
        return True


class MotorCycle(EngineVehicle):
    pass


class Car(EngineVehicle):
    def get_number_of_wheels(self):
        return 4


class Bicycle(Vehicle):
    pass


if __name__ == "__main__":

    # Example 1

    print(f"{'-' * 20} Example 1 {'-' * 20}")
    vehicle_list: list[Vehicle] = [
        MotorCycle(),
        Car(),
        Bicycle()
    ]

    for vehicle in vehicle_list:
        print(f"{vehicle.__class__.__name__} "
              f"has engine:= {vehicle.get_number_of_wheels()}")

    # Below code will give compile time error
    # because the Vehicle is not aware of has_engine() method

    for vehicle in vehicle_list:
        print(f"{vehicle.__class__.__name__} "
              f"has engine:= {vehicle.has_engine()}")

    # Example 2

    print(f"{'-' * 20} Example 2 {'-' * 20}")
    engine_vehicle_list: list[EngineVehicle] = [
        MotorCycle(),
        Car(),
        Bicycle()   # compile time error
    ]

    # Below code will give compile time error
    # because the Vehicle is not aware of has_engine() method

    for vehicle in engine_vehicle_list:
        print(f"{vehicle.__class__.__name__} "
              f"has engine:= {vehicle.has_engine()}")
