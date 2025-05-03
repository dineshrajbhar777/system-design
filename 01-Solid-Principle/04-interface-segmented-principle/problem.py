"""
Principle: I - Interface Segmented Principle

    Interface should be such that client should not implement
    unnecessary function they do not needed

Problem:

In the below example, we have RestaurantEmployee interface with following methods
    wash_dishes()
    serve_customer()
    cook_food()

Now we extend this to Waiter class whose primary job is to serve the customer,
so he needs to implement only serve_customer() method but interface design
it forcing to implement all methods that are not needed.
"""

from abc import abstractmethod


class RestaurantEmployee:
    @abstractmethod
    def wash_dishes(self): pass

    @abstractmethod
    def serve_customer(self): pass

    @abstractmethod
    def cook_food(self): pass


class Waiter(RestaurantEmployee):

    def wash_dishes(self):
        raise ValueError("Not my job")

    def serve_customer(self):
        print("serving the customer")

    def cook_food(self):
        raise ValueError("Not my job")
