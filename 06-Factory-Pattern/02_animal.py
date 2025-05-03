from abc import ABC, abstractmethod


# Product
class Animal(ABC):
    @abstractmethod
    def speak(self) -> str:
        pass


# Concrete Products
class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"


class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"


# Factory
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: str) -> Animal:
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")


# Client
if __name__ == "__main__":
    animal_type = input("Enter animal type (dog/cat): ").strip().lower()
    animal = AnimalFactory.create_animal(animal_type)
    print(f"The animal says: {animal.speak()}")
