# 8.14 Implementing Custon Containers

# import collections
# 
# class A(collections.Iterable):
#     pass

import collections
import bisect

class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial)

    # Required sequence methods
    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    # Method for adding an item in the right location
    def add(self, item):
        bisect.insort(self._items, item)

items = SortedItems([5, 1, 2])
#print(list(items))  # [1, 2, 5]
items.add(3)
#print(list(items))  # [1, 2, 3, 5]
items.add(-10)
print(list(items))  # [-10, 1, 2, 3, 5]
