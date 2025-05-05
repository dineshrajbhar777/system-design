class Component:
    def operation(self):
        pass


class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent"


class Decorator(Component):
    _component: Component = None

    def __init__(self, component: Component):
        self._component = component

    @property
    def component(self):
        return self._component

    def operation(self):
        return self._component.operation()


class ConcreteComponentA(Decorator):
    def operation(self):
        return f"ConcreteDecoratorA({self.component.operation()})"


class ConcreteComponentB(Decorator):

    def operation(self):
        return f"ConcreteDecoratorB({self.component.operation()})"


def client_code(component: Component):
    print(f"RESULT: {component.operation()}", end="")


if __name__ == "__main__":
    simple = ConcreteComponent()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")

    # ...as well as decorated ones.
    #
    # Note how decorators can wrap not only simple components but the other
    # decorators as well.

    decorator1 = ConcreteComponentA(simple)
    decorator2 = ConcreteComponentB(decorator1)
    print("Client: I've got a decorated component:")
    client_code(decorator2)
