"""
custom string formating, and how it works.
"""


class Date(object):

    _formats = {
        "ymd": "{d.year}-{d.month}-{d.day}",
        "mdy": "{d.month}/{d.day}/{d.year}",
        "dmy": "{d.day}/{d.month}/{d.year}",
    }
    
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __format__(self, code):
        if code == "":
            code = "ymd"
        fmt = self._formats[code]
        return fmt.format(d=self)


d = Date(2018, 12, 12)
print(format(d))
print(format(d, "dmy"))
print(format(d, "mdy"))
