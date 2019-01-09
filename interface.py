

class Descriptors(object):

    def __init__(self, name, **opts):
        self.name = name

        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Typed(Descriptors):

    expected_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Expected type {self.expected_type}")
        super().__set__(instance, value)


class Unsigned(Descriptors):

    def __set__(self, instance, value):
        if value < 0:
            raise TypeError("Expected more than zero.")
        super().__set__(instance, value)


class MaxSized(Descriptors):

    def __init__(self, name=None, **opts):
        if 'size' in opts:
            raise TypeError("missing: size options.")
        super().__init__(name, **opts)

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError(f"Expected {self.size}")
        super().__set__(instance, value)


class Integer(Typed):

    expected_type = int


class UnsignedInteger(Integer, Unsigned):

    pass


class Float(Typed):

    expected_type = float


class UnsignedFloat(Float, Unsigned):

    pass


class String(Typed):

    expected_type = str


class SizedString(String, MaxSized):

    pass


class Stock(object):

    name = SizedString('name', size=10)
    share = UnsignedInteger('share')
    price = UnsignedFloat('price')

    def __init__(self, name, share, price):
        self.name = name
        self.share = share
        self.price = price

        

    
