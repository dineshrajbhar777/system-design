from abc import ABC, abstractmethod


# Product

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


# Concrete Products

class Circle(Shape):
    def draw(self):
        return "Circle"


class Rectangle(Shape):
    def draw(self):
        return "Rectangle"


class Triangle(Shape):
    def draw(self):
        return "Triangle"


# Factory


class ShapeFactory:
    shapes: dict[str: Shape] = {
        "circle": Circle(),
        "triangle": Triangle(),
        "rectangle": Rectangle()
    }

    @staticmethod
    def get_shape(shape_type: str):
        return ShapeFactory.shapes.get(shape_type.lower(), None)


if __name__ == "__main__":
    shape = ShapeFactory.get_shape("circle")
    print(f"The shape draw: {shape.draw()}")

    shape = ShapeFactory.get_shape("triangle")
    print(f"The shape draw: {shape.draw()}")

    shape = ShapeFactory.get_shape("rectangle")
    print(f"The shape draw: {shape.draw()}")

    shape = ShapeFactory.get_shape("dummy")
    if shape:
        print(f"The shape draw: {shape.draw()}")
