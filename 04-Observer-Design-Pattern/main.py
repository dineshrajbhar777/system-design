from notify_me.notify_observer import EmailNotificationObserver, SMSNotificationObserver
from notify_me.notify_observable import StockObservable, IphoneObservable


if __name__ == "__main__":
    iphone_observable: StockObservable = IphoneObservable()

    iphone_observable.attach(
        EmailNotificationObserver("dinesh@test.com", iphone_observable))
    iphone_observable.attach(
        EmailNotificationObserver("demo@test.com", iphone_observable))

    iphone_observable.attach(
        SMSNotificationObserver("9988776655", iphone_observable))

    iphone_observable.set_stock_quantity(20)
