"""
Principle: I - Interface Segmented Principle

    Interface should be such that client should not implement
    unnecessary function they do not need

Solution:
    Divide the interface into small-small segment
"""

from abc import abstractmethod


class WaiterInterface:
    @abstractmethod
    def serve_customers(self): pass

    @abstractmethod
    def take_order(self): pass


class ChefInterface:
    @abstractmethod
    def cook_food(self): pass

    @abstractmethod
    def decide_menu(self): pass


class HelperInterface:
    @abstractmethod
    def wash_dishes(self): pass


class Waiter(WaiterInterface):
    def serve_customers(self):
        print("serving the customer")

    def take_order(self):
        print("taking orders")
