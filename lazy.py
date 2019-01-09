

class LazyProperty(object):

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        value = self.func(instance)
        setattr(self.instance, self.func.__name__, value)
        return value


class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    @LazyProperty
    def area(self):
        return math.pi * self.radius ** 2

    @LazyProperty
    def perimeter(self):
        return 2 * math.pi * self.radius

