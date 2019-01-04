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

c = C()
c # 1
d = D()
d # 1
  # 2

