# 8.4 Saving Memory When Creating a Large Number of Instances

class Date:
    __slots__ = ['year', 'month', 'day']
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
# If not using __slots__(), Date instance will requires 428 bytes.
# with __slots__(), it's only 156 bytes.
