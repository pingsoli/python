# 2.4 Matching and Searching for Text Patterns

# std.find(), str.endswith(), str.startswith()

text = 'yeah, but no, but yeah, but no, but yeah'

# Exact match
#print(text == 'yeah')  # False

# Match at start or end
#print(text.startswith('yeah'))  # True
#print(text.endswith('no'))      # False

# Search for the location of the first occurrence
#print(text.find('no'))  # 10


# For more complicated matching, use regular expression instead
text1 = '11/27/2017'

import re
#if re.match(r'\d+/\d+/\d+', text1):
#    print('yes')
#else:
#    print('no')

# Output: 
# yes

# Find all matching
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat = re.compile(r'\d+/\d+/\d+')
res = datepat.findall(text)
#print(res)  # ['11/27/2012', '3/13/2013']


# Extract the matching part from a group
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/28/2017')
#print(m.group(0))  # 11/28/2017
#print(m.group(1))  # 11
#print(m.group(2))  # 28
#print(m.group(3))  # 2017
#print(m.group())   # 11/28/2017
#print(m.groups())  # ('11', '28', '2017')
month, day, year = m.groups()
#print(month, day, year)  # 11 28 2017


# Find all matches 
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
# [('11', '27', '2012'), ('3', '13', '2013')]
#print(datepat.findall(text))

for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))

# Output:
# 2012-11-27
# 2013-3-13

for m in datepat.finditer(text):
    print(m.groups())

# Output:
# ('11', '27', '2012')
# ('3', '13', '2013')
