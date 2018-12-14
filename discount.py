

from collections import namedtuple
from abc import ABC, abstractmethod


"""
class Customer(object):

    def __init__(self, name, fidelity):
        self.name = name
        self.fidelity = fidelity
"""

Customer = namedtuple("Customer", "name fidelity")


class LineItem(object):

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.quantity * self.price


class Order(object):

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = "<Order total: {:.2f} due: {:.2f}>"
        return fmt.format(self.total(), self.due())


class Promotion(ABC):

    @abstractmethod
    def discount(self, order):
        return 0


class FidelityPromo(Promotion):

    def discount(self, order):
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total()
        return discount


class LargeOrderPromo(Promotion):

    def discount(self, order):
        dict_item = {item.product for item in order.cart}
        if len(dict_item) >= 10:
            return order.total() * 0.07
        return 0


