"""
sorting dictionary using magic methods.

__missing__ -> this will be called if any key missing from the dict, after calls(__getitem__)
__contains__-> this will check weather the key is present in the dict or not
__getitem__ -> this will get the value based on key, if not exists it will calls(__missing__) 

"""



class SrtKeyDict(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError("Key not found!")
        return self[str(key)]

    def __getitem__(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


if __name__ == '__main__':
    sk = SrtKeyDict({"felix": "first_name", 2: "second_name"})
    print(sk['felix'])
    print(sk.get(2))
    print(sk.get(4, 4))
    # print(sk['test'])
