"""
Calling parent class methods and attributes.
"""


class A(object):

    def spam(self):
        print("spam A")


class B(A):

    def spam(self):
        print("spam B")
        super().spam()


b = B()
b.spam()


class C(object):

    def __init__(self):
        self.x = 0


class D(C):

    def __init__(self):
        super().__init__()
        self.y = 1

d = D()
print(d.x)
print(d.y)


class Proxy(object):

    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            setattr(self._obj, name, value)


p = Proxy({"name": "felix", "last_name": "stephen"})
print(p.get('name'))
p


