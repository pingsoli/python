# 3.12 Converting Days to Seconds, and Other Basic Time Conversions

from datetime import timedelta
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
#print(c)  # 2 days, 10:30:00
#print(c.days)  # 2
#print(c.seconds)  # 37800
#print(c.seconds / 3600)  # 10.5

# Representing specific dates and times.
from datetime import datetime

a = datetime(2017, 10, 27)
#print(a + timedelta(days=10))  # 2017-11-06 00:00:00

b = datetime(2017, 12, 12)
c = b - a
#print(c.days)  # 46

print(datetime.today())  # 2017-12-21 11:28:41.918161
