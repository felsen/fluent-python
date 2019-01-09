"""
Python Descriptors.

Reference: https://www.youtube.com/watch?v=ZdvpNaWwx24
           https://www.youtube.com/watch?v=FPuq-9B0OqE

           https://www.youtube.com/watch?v=v2WTVCyTYMw
"""


class Square(object):

    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        return self.side ** self.side

    @area.setter
    def area(self, value):
        print("Cannot set any value")

    @area.deleter
    def area(self):
        print("Cannot del any value")


s = Square(4)
print(s.area)
s.area = 200
print(s.area)
del s.area


