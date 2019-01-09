

import collections


class Items(collections.MutableSequence):

    def __init__(self, initial=None):
        """
        Initializing item class parameters.
        """
        self._items = list(initial) if initial is None else []

    def __getitem__(self, index):
        """
        Getting an item based on index.
        """
        return self._items[index]

    def __setitem__(self, index, value):
        """
        Setting a value based on index.
        """
        self._items[index] = value

    def __delitem__(self, index):
        """
        Deleting an item, for specified index.
        """
        del self._items[index]

    def __insert__(self, index, value):
        """
        Inserting an item for specified, index.
        """
        self._items.insert(index, value)

    def __len__(self):
        """
        Returning an length of sequence.
        """
        return len(self._items)



i = Items([1, 2, 3, 4, 5])
print(len(i))
    
