

class Structure(object):

    _fields = ()

    def __init__(self, *args):
        if len(_fields) != len(args):
            raise TypeError(f"Expected {len(_fields)} arguments.")
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


if __name__ == '__main__':

    class Shares(Structure):

        _fields = ('name', 'share', 'price')


    class Point(Structure):

        _fields = ('x', 'y')


    class Circle(Structure):

        _fields = ('radius')
