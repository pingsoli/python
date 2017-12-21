# 4.14 Flattening a Nested Sequence

from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

items = [1, 2, 3, [4, 5, [7, 8, [9, 0] ] ] ]
print(list(x for x in flatten(items)))
# [1, 2, 3, 4, 5, 7, 8, 9, 0]
