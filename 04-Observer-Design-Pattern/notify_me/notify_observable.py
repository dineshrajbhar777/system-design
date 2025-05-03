"""
Design Notify Me -> Observable
"""
from abc import ABC, abstractmethod
from notify_me.notify_observer import NotificationObserver


class StockObservable(ABC):
    """
    The StockObservable interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: NotificationObserver):
        """
        Attach an observer to the StockObservable
        """
        pass

    @abstractmethod
    def detach(self, observer: NotificationObserver):
        """
        Detach an observer from the StockObservable
        """
        pass

    @abstractmethod
    def notify_subscriber(self):
        """
        Notify all observers about an event.
        """
        pass

    @abstractmethod
    def set_stock_quantity(self, new_quantity):
        """
        Set the stock quantity
        """
        pass

    @abstractmethod
    def get_stock_quantity(self):
        """
        Get the stock quantity
        """
        pass


class IphoneObservable(StockObservable):
    """
    The StockObservable owns some important stock_qty and notifies observers
    when the _stock_quantity changes.
    """

    """
    For the sake of simplicity, the StockObservable's stock_qty, essential to all
    subscribers, is stored in this variable.
    """
    _stock_quantity: int = 0

    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """
    _observer_list: list[NotificationObserver] = []

    """
    The subscription management methods.
    """

    def attach(self, observer: NotificationObserver):
        print(f"StockObservable: Attached and Observer {observer.__class__.__name__}")
        self._observer_list.append(observer)

    def detach(self, observer: NotificationObserver):
        print(f"StockObservable: Detached and Observer {observer.__class__.__name__}")
        self._observer_list.remove(observer)

    def notify_subscriber(self):
        """
        Trigger an update in each subscriber.
        """
        print("StockObservable: Notifying observers...")
        for observer in self._observer_list:
            observer.update()

    def set_stock_quantity(self, new_quantity):
        """
        Usually, the subscription logic is only a fraction of what a StockObservable can
        really do. StockObservable commonly holds some important business logic that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """
        print("\nStockObservable: I'm doing something important.")
        self._stock_quantity += new_quantity

        print(f"Subject: My stock quantity has just changed to: {self._stock_quantity}")
        self.notify_subscriber()

    def get_stock_quantity(self):
        return self._stock_quantity
