"""
Principle: O - Open / Closed Principle

    Open for Extension but Closed for Modification

Problem:
Class InvoiceDao is tested and already running in live

Now new requirement is to save to file also, and we added new method
save_to_file() in the same class which is already running in production
which break the principle.

It will be prone to bug.

"""

"""
class InvoiceDao:
    def __init__(self, invoice: Invoice):
        self.invoice = invoice

    def save_to_db(self):
        pass
"""


class Invoice:
    pass


class InvoiceDao:
    def __init__(self, invoice: Invoice):
        self.invoice = invoice

    def save_to_db(self):
        pass

    def save_to_file(self, filename):
        pass
