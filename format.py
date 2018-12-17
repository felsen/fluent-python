"""
custom string formating, and how it works.
"""


from datetime import datetime


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

    # def __format__(self, code):
    #     """
    #     Supports custom date formats as defined.
    #     """
    #     if code == "":
    #         code = "ymd"
    #     fmt = self._formats[code]
    #     return fmt.format(d=self)

    def __format__(self, code):
        """
        Supports generic date formats.
        """
        dfmt = "-".join((str(self.day), str(self.month), str(self.year)))
        d = datetime.strptime(dfmt, "%Y-%m-%d")
        if code == "":
            code = "%A, %B %d, %Y"
        return format(d, code)


d = Date(2018, 2, 12)
# print(format(d))
# print(format(d, "dmy"))
# print(format(d, "mdy"))
print(format(d))
print(format(d, "%Y-%m-%d"))
