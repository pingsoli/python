# 8.2 Customizing String Formatting

# format() function
# __format__() method.

_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)

d = Date(2017, 12, 25)
#print(format(d))
# 2017-12-25
#print(format(d, 'mdy'))
# 12/25/2017
#print('The date is {:ymd}'.format(d))
# The date is 2017-12-25
#print('The date is {:mdy}'.format(d))
# The date is 12/25/2017

from datetime import date

d = date(2017, 12, 25)
# print(format(d))  # 2017-12-25
# print(d.today())  # 2017-12-25

print(format(d, '%A, %B %d, %Y'))
# Monday, December 25, 2017
