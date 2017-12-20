# 1.16 Filtering Sequence Elements

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# [1, 4, 10, 2, 3]
#print([n for n in mylist if n > 0])

pos = (n for n in mylist if n > 0)
for x in pos:
    print(x)

# Output:
# 1
# 4
# 10
# 2
# 3


# Exception handling
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, values))
#print(ivals)  # ['1', '2', '-3', '4', '5']

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
import math
newlist = [math.sqrt(n) for n in mylist if n > 0]
# [1.0, 2.0, 3.1622776601683795, 1.4142135623730951, 1.7320508075688772]
# print(newlist)

clip_neg = [n if n > 0 else 0 for n in mylist]
#print(clip_neg)  # [1, 4, 0, 10, 0, 2, 3, 0]



addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK'
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

# compress() function picks out the items corresponding to True values.
# Like filter(), compress() normally return an iterator. Thus, we need to 
# use list() to turn the result into a list if desired.

counts = [ 0, 3, 10, 4, 1, 7, 6, 1 ]

from itertools import compress
more5 = [n > 5 for n in counts]
filter_addr = list(compress(addresses, more5))

# ['5800 E 58TH', '4801 N BROADWAY', '1039 W GRANVILLE']
print(filter_addr)
