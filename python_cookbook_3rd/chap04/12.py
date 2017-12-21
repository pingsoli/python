# 4.12 Iterating on Items in Separate Containers

from itertools import chain 
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
print(list(x for x in chain(a, b)))
# [1, 2, 3, 4, 'x', 'y', 'z']


# Variable working sets of items
active_items = set()
inactive_items = set()

# Iterate over all items.
#for item in chain(active_items, inactive_items):
    # Processing item


# Inefficent
#for x in a + b:

# Better
#for x in chain(a, b):
