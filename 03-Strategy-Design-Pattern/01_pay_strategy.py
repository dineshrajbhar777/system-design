from abc import ABC, abstractmethod


class PayStrategy(ABC):
    """
    The PayStrategy interface declares operations common to all supported versions
    of some algorithm.

    The ShoppingCart uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def pay(self):
        pass


"""
Concrete Strategies implement the algorithm while following the base Strategy
interface. The interface makes them interchangeable in the Context.
"""


class CashStrategy(PayStrategy):
    def pay(self):
        print("Payment through cash.")


class CreditCardStrategy(PayStrategy):
    def pay(self):
        print("Payment through credit card.")


class UPIStrategy(PayStrategy):
    def pay(self):
        print("Payment through UPI.")


class ShoppingCart:
    def __init__(self, pay_strategy: PayStrategy):
        """
        Usually, the ShoppingCart accepts a PayStrategy through the constructor,
        but also provides a setter to change it at runtime.
        """
        self._pay_strategy = pay_strategy

    @property
    def pay_strategy(self) -> PayStrategy:
        """
        The ShoppingCart maintains a reference to one of the PayStrategy objects. The
        ShoppingCart does not know the concrete class of a pay strategy. It should work
        with all strategies via the Strategy interface.
        """
        return self._pay_strategy

    @pay_strategy.setter
    def pay_strategy(self, pay_strategy: PayStrategy):
        """
        Usually, the ShoppingCart allows replacing a PayStrategy object at runtime.
        """
        self._pay_strategy = pay_strategy

    def payment_option(self):
        """
        The ShoppingCart delegates some work to the PayStrategy object instead of
        implementing multiple versions of the algorithm on its own.
        """
        self._pay_strategy.pay()


if __name__ == "__main__":
    # The client code picks a concrete strategy and passes it to the context.
    # The client should be aware of the differences between strategies
    # to make the right choice.

    shopping_cart = ShoppingCart(UPIStrategy())
    print("Client: UPIStrategy")
    shopping_cart.payment_option()

    shopping_cart.pay_strategy = CreditCardStrategy()
    print("Client: CreditCardStrategy")
    shopping_cart.payment_option()

    shopping_cart.pay_strategy = CashStrategy()
    print("Client: CashStrategy")
    shopping_cart.payment_option()
