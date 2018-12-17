"""
Example of how repr ans str works.
"""


class Pair(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Pair ({:f} - {:f})".format(self.x, self.y)

    def __str__(self):
        return "({x}, {y})".format(x=self.x, y=self.y)


p = Pair(3.4, 6.9)
p # __repr__
print(p) # __str__
