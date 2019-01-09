
"""
Writing more than one constructor.
"""


class Date(object):

    """
    Creating more than one constructor.
    """
    
    def __init__(self, year, month, date):
        self.year = year
        self.month = month
        self.date = date

    # Alternative Constructor.
    @classmethod
    def today(cls):
        import datetime
        t = datetime.datetime.now()
        return cls(t.year, t.month, t.day)


d = Date.today()
print(d.year)
print(d.month)
print(d.date)

