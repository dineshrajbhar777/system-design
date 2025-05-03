"""
Principle: S - Single Responsibility Principle

    A class should have only 1 reason to change

    Marker class has HAS-A relation with Invoice class

Problem:
    - calculate_total() -> to calculate price with discounts, GST and more
    - print_invoice()   -> to change the printing logic
    - save_to_db()      -> to save to file

    Note: here we have 3 reason to change the class which break the principle
"""

from datetime import datetime


class Marker:
    def __init__(self, name: str, color: str, price: float, mfg: datetime):
        self.name = name
        self.color = color
        self.price = price
        self.mfg = mfg


class Invoice:
    def __init__(self, marker: Marker, qty: int):
        self.marker = marker
        self.quantity = qty

    def calculate_total(self):
        price = self.marker.price * self.quantity
        return price

    def print_invoice(self):
        pass

    def save_to_db(self):
        pass
