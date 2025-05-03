from abc import ABC, abstractmethod


class DriveStrategy(ABC):
    @abstractmethod
    def drive(self):
        pass


class NormalDriveStrategy(DriveStrategy):
    def drive(self):
        print("Normal drive capability.")


class SportsDriveStrategy(DriveStrategy):
    def drive(self):
        print("Sports drive capability")


class Vehicle:
    def __init__(self, drive_strategy: DriveStrategy):
        self._drive_strategy = drive_strategy

    @property
    def drive_strategy(self):
        return self._drive_strategy

    @drive_strategy.setter
    def drive_strategy(self, drive_strategy: DriveStrategy):
        self._drive_strategy = drive_strategy

    def drive(self):
        self._drive_strategy.drive()


class OffRoadVehicle(Vehicle):
    def __init__(self):
        super().__init__(NormalDriveStrategy())


class SportsVehicle(Vehicle):
    def __init__(self):
        super().__init__(SportsDriveStrategy())


if __name__ == "__main__":
    print("Client: SportsVehicle")
    vehicle = SportsVehicle()
    vehicle.drive()

    print("Client: OffRoadVehicle")
    vehicle.drive_strategy = OffRoadVehicle()
    vehicle.drive()
