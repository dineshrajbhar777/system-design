"""
Principle: O - Open / Closed Principle

    Open for Extension but Closed for Modification

Solution:

Now we extended the class InvoiceDao to save to DB and File.

And in future if we want to save to NoSQL we can extend the InvoiceDao class
"""

from abc import abstractmethod


class Invoice:
    pass


class InvoiceDao:
    @abstractmethod
    def save(self, invoice: Invoice):
        pass


class DatabaseInvoiceDao(InvoiceDao):
    def save(self, invoice: Invoice):
        pass


class FileInvoiceDao(InvoiceDao):
    def save(self, invoice: Invoice):
        pass
