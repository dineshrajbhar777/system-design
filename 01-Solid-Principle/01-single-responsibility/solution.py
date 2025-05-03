"""
Principle
    S - A class should have only 1 reason to change

Solution:

    Now each class has single responsibility
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
        self.qty = qty

    def calculate_total(self):
        price = self.marker.price * self.qty
        return price


class InvoiceDao:
    def __init__(self, invoice: Invoice):
        self.invoice = invoice

    def save_to_db(self):
        pass


class InvoicePrinter:
    def __init__(self, invoice: Invoice):
        self.invoice = invoice

    def print(self):
        pass

