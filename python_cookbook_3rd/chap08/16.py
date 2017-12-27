# 8.16 Defining More Than One Constructor in a Class

import time

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

    def __repr__(self):
        return '{}/{}/{}'.format(self.year, self.month, self.day)

d1 = Date(2017, 12, 22)
d2 = Date.today()
print(d1)  # 2017/12/22
print(d2)  # 2017/12/27
