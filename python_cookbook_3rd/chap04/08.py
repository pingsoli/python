# 4.8 Skipping the First Part of Iterable

from itertools import islice

items = ['a', 'b', 'c', 1, 2, 3, 4]
#print(items[:-3]) 
#print(items[3:])  # start - 3, stop - None
#print(items[:3])  # start - 0, stop - 3
# Output:
# ['a', 'b', 'c', 1]
# [1, 2, 3, 4]
# ['a', 'b', 'c']

#for x in islice(items, 3, None):
#    print(x)
# Output:
# 1
# 2
# 3
# 4

#with open('02.py') as f:
#    # Skip over initial comments
#    while True:
#        line = next(f, '')
#        if not line.startswith('#'):
#            break
#    
#    # Process remaining lines
#    while line:
#        # Replace with useful processing
#        # Ignore the following comment content.
#        if not line.startswith('#'):
#            print(line, end='')
#        line = next(f, None)
    

# Simplest way to remove all comments.
with open('02.py') as f:
    lines = (line for line in f if not line.startswith('#'))

    for line in lines:
        print(line, end='')

# Output:
# class Node:
#     def __init__(self, value):
#         self._value = value
#         self._children = []
#     
#     def __repr__(self):
#         return 'Node({!r})'.format(self._value)
# 
#     def add_child(self, node):
#         self._children.append(node)
# 
#     def __iter__(self):
#         return iter(self._children)
# 
# if __name__ == '__main__':
#     root = Node(0)
#     child1 = Node(1)
#     child2 = Node(2)
#     root.add_child(child1)
#     root.add_child(child2)
# 
#     for ch in root:
#         print(ch)
