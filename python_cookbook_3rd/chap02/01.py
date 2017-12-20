# 2.1 Splitting Strings on Any of Multiple Delimiters

# split() method does not allow for multiple delimeters
# use re.split() instead.
line = 'asdf fjkd; afed, fje,asdf,     foo'
import re

result = re.split(r'[;,\s]\s*', line)
#print(result)  # ['asdf', 'fjkd', 'afed', 'fje', 'asdf', 'foo']

fields = re.split(r'(;|,|\s)\s*', line)
# ['asdf', ' ', 'fjkd', ';', 'afed', ',', 'fje', ',', 'asdf', ',', 'foo']
#print(fields)

# Extract values and delimiters
values = fields[::2]
delimiters = fields[1::2] + ['']
#print(values)  # ['asdf', 'fjkd', 'afed', 'fje', 'asdf', 'foo']
#print(delimiters)  # [' ', ';', ',', ',', ',', '']

# Reform the line using the same delimiters
reformed = ''.join(v+d for v, d in zip(values, delimiters))
# asdf fjkd;afed,fje,asdf,foo
#print(reformed)

# Use regular expression noncapture group, (?:...)
res = re.split(r'(?:,|;|\s)\s*', line)
# ['asdf', 'fjkd', 'afed', 'fje', 'asdf', 'foo']
print(res)
