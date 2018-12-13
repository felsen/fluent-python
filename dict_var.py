"""
Variations of dictionary items.

collections.OrderedDict
    This will store the dict item, beased on the order user is give.
    dict.popitem(last=True) - by default it will remove from the first item.

collections.ChainMap
    ChainMap updates(writes / deletes) for the first mapping of chain.
    __setitem__ -> updating the key / value to the dict.
    __delitem__ -> deleting the key from the dict.

collections.Counter
collections.UserDict

"""

from collections import ChainMap, OrderedDict, Counter, UserDict


class DeepChainMap(ChainMap):

    def __setitem__(self, key, item):
        for mapping in self.maps:
            if key in mapping:
                mapping[key] = item
                return
        self.maps[0][key] = item

    def __delitem__(self, key):
        for mapping in self.maps:
            if key in mapping:
                del mapping[key]
                return
        raise KeyError(key)

d = DeepChainMap({'zebra': 'black'}, {'elephant': 'blue'}, {'lion': 'yellow'})
print(d['zebra'])
print(d['elephant'])
print(d['lion'])

d['snake'] = 'black'
print(d)


print(Counter(['red', 'blue', 'red', 'green', 'blue', 'blue']))
print(Counter('asdfghjkllhgfdsasdfghjkl'))
print(Counter(cats=4, dogs=5))


class SrtUserDict(UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(str(key))
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data
    
    def __setitem__(self, key, item):
        self.data[key] = item
