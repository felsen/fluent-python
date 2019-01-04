

class Person(object):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected string")
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError("name cannot be deleted")


class SubPerson(Person):

    @property
    def name(self):
        print("Getting name")
        return super().name

    @name.setter
    def name(self, value):
        print(f"setting name to {value}")
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print("deleting name")
        super(SubPerson, SubPerson).name.__delete__(self)



p = Person("Felix")
print(p.name)
p.name = "Stephen"
print(p.name)
# del p.name
print("")
sp = SubPerson("Felix Stephen")
print(sp.name)
sp.name = "Stephen Felix"
print(sp.name)


