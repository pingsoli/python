# 3.15 Converting Strings into Datetimes

from datetime import datetime
text = '2017-12-21'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
#print(y, z)  # 2017-12-21 00:00:00 2017-12-21 11:50:25.373673

# datetime.strptime() support a host of formatting codes.
def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))

print(parse_ymd('2017-12-22'))  # 2017-12-22 00:00:00
