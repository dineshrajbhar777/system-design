from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from notify_me.notify_observable import StockObservable  # Avoid circular import at runtime


def send_email(email: str, message: str):
    print(f"Email sent to {email}, message: {message}")


def send_sms(mobile_number: str, message: str):
    print(f"SMS sent to {mobile_number}, message: {message}")


class NotificationObserver(ABC):
    @abstractmethod
    def update(self): pass


class EmailNotificationObserver(NotificationObserver):

    def __init__(self, email: str, observable: "StockObservable"):
        self._email = email
        self._observable = observable

    def update(self):
        message = f"{self._observable.get_stock_quantity()} stocks are available"
        send_email(self._email, message)


class SMSNotificationObserver(NotificationObserver):

    def __init__(self, mobile_number: str, observable: "StockObservable"):
        self._mobile_number = mobile_number
        self._observable = observable

    def update(self):
        message = f"{self._observable.get_stock_quantity()} stocks are available"
        send_sms(self._mobile_number, message)
