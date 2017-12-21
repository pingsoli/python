# 4.7 Taking a Slice of a Iterator

def count(n):
    while True:
        yield n
        n += 1

# itertools.islice() function is taking slices of 
# iterator and generators.

import itertools
c = count(0)
for x in itertools.islice(c, 10, 20):
    print(x)
# Output:
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
