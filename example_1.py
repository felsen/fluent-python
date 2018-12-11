"""
__len__, __getitem__ magic methods examples.
"""


import collections


Card = collections.namedtuple("Card", ['rank', 'suite'])


"""

class Card(object):

    def __init__(self, rank, suite):
        self.rank = rank
        self.suite = suite

"""


class FrenchDeck(object):

    ranks = list(map(str, range(2, 11))) + list('JQKA')
    suites = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suite) for suite in self.suites for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


fd = FrenchDeck()
print(len(fd))
print(fd[0])
print(fd[-1])

