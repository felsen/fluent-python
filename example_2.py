"""
__add__, __mul__, __abs__, __repr__

__add__  -> normal addition
__mul__  -> normal multiplication
__repr__ -> official string representation of an objects.
__abs__  -> abs buit-in function that returns absolute value of int, float, complex numbers

"""

from math import hypot


class Vector(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector({x}, {y})".format(x=self.x, y=self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x*scalar, self.y*scalar)



v = Vector(2, 3)
v1 = Vector(5, 6)
print(abs(v))
print(v + v1)
print(v * 3)
