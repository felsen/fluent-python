

class Integer(object):

    def __init__(self, name):
        """
        Initializing the attribute,
        """
        self.name = name

    def __get__(self, instance, cls):
        """
        p.x
        p.y
        instance is class object of Point.
        cls - referenced class Point without object.
        """
        print("Getting data..")
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        """
        p.x = 2
        p.y = 3
        instance is class object of Point.
        value is setting the value to instance of an attribute.
        """
        print("Setting data...")
        if not isinstance(value, int):
            raise TypeError("Expected integer")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        """
        del p.x
        del p.y
        instance - is class object and deleting the value of x or y.
        """
        print("Deleting data..")
        del instance.__dict__[self.name]


class Point(object):

    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(2, 3)
print(p.x)
print(p.y)
