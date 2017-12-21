# 3.16 Manipulating Dates Involving Time Zones

# Involving time zones, you should use pytz module.
# I install pyhton from source code, so pip will prompt 
# python without SSL
# 
# Solution:
# Step1: entering Python/Modules and modify Setup file.
#        Uncommet SSL part code
# Step2: intalling libssl-dev
#        sudo apt-get install libssl-dev
# Step3: ./configure, make and make install
# Step4: sudo pip install --trusted-host pypi.python.org pytz

from datetime import datetime
from pytz import timezone

d = datetime(2012, 12, 21, 9, 30, 0)
print(d)  # 2012-12-21 09:30:00

# Localize the date for Chicago
central = timezone('US/Central')
loc_d = central.localize(d)
#print(loc_d)  # 2012-12-21 09:30:00-06:00

# Convert to Chongqing
chongqin_d = loc_d.astimezone(timezone('Asia/Chongqing'))
print(chongqin_d)  # 2012-12-21 23:30:00+08:00
