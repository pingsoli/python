# 1.5 Implementing a Priority Queue

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    
    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

# Output:
# Item('bar')
# Item('spam')
# Item('foo')
# Item('grok')
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())


# Question 1:
# Why (-prority, index, item) composed?
# A: same prority must use index to sort the order. 
# such as (1, 0, Item('foo')) and (1, 1, Item('bar')). 
