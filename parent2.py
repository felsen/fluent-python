

class Base(object):

    def __init__(self):
        print("Base.__init__")


class A(Base):

    def __init__(self):
        super().__init__()
        print("A.__init__")


class B(Base):

    def __init__(self):
        super().__init__()
        print("B.__init__")


class C(A, B):

    def __init__(self):
        super().__init__()
        print("C.__init__")


a = Base()
a
print("")
b = A()
b
print("")
c = B()
c
print("")
d = C()
d # this works based on the MRO(C3 Linearization technique) - Method Resolution Order.
print("")
print(C.__mro__)
