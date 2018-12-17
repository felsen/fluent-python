"""
property, getter, setter, deleter
"""


class Person(object):

    def __init__(self, first_name):
        self._first_name = first_name

    # Getter
    @property
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('expected sting')
        self._first_name = value

    # Deleter function
    @first_name.deleter
    def first_name(self):
        raise AttributeError('cannot be deleted')


name = Person("Felix Stephen")
print(name.first_name)
name.first_name = "Stephen"
print(name.first_name)
# name.first_name = 23 # Exception as raised
# del name.first_name  # Exception as raised
