"""
Initializing parent class methods and attributes.
"""


class A(object):

    def spam(self):
        print("spam A")


class B(A):

    def spam(self):
        print("spam B")
        # here, parents class method is overidden in subclass. this will call the parent class spam. 
        super().spam() # super will always look for the parent class attr & methods


a = A()
a.spam() # spam A

b = B()
b.spam() # spam B
         # spam A




class C(object):

    def __init__(self):
        self.x = 1
        print(self.x)


class D(C):

    def __init__(self):
        # Whenever the class D is called, first super will initialize the C class __init__, then self.y will be printed.
        super().__init__()
        self.y = 2
        print(self.y)

print("----------")
c = C()
c # 1
d = D()
d # 1
  # 2


class E(D, C):

    def __init__(self):
        super().__init__()
        self.z = 3
        print(self.z)

print("------------")
e = E()
e # 1
  # 2
  # 3


class Proxy(object):

    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        # another usage of super is override the any magic methods.
        # this will call the original __setattr__
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            setattr(self._obj, name, value)


  
