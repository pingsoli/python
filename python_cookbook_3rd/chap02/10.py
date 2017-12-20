# 2.10 Working with Unicode Characters in Regular Expression

import re
num = re.compile('\d+')

# Usually normalize and sanitize all text to a standard form.


pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
#print(pat.match(s))
# <_re.SRE_Match object; span=(0, 6), match='straße'>

#print(pat.match(s.upper()))  # None
