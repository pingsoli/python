# 8.17 Creating an Instance Without Invoking init

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

d = Date.__new__(Date)
#print(d)
# <__main__.Date object at 0x7f094c880198>
#print(d.__dict__)  # {}
#print(d.year)
# Traceback (most recent call last):
#   File "17.py", line 13, in <module>
#     print(d.year)
# AttributeError: 'Date' object has no attribute 'year'

data = {'year': 2017, 'month': 12, 'day': 27}
for key, value in data.items():
    setattr(d, key, value)

#print(d.year, d.month, d.day)
#print('%d/%d/%d' % (d.year, d.month, d.day))  # 2017/12/27

