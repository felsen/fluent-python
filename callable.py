"""
__call__ -> will act as a variable and also function calls.
"""


import random


class BingoCall(object):

    def __init__(self, items):
        if items is None:
            raise ValueError(items)
        self._items = items
        random.shuffle(self._items)

    def pick(self):
        try:
            self._items.pop()
        except IndexError:
            raise LookupError("pick from empty Bingo!")

    def __call__(self):
        return self.pick()

b = BingoCall([1, 2, 3, 4, 5, 6])
print(b._items)

b.pick()
print(b._items)

b()
print(b._items)


