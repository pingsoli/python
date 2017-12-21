# 4.10 Iterating Over the Index-Value Pairs of a Sequence

my_list = ['a', 'b', 'c']
#for idx, val in enumerate(my_list):
#    print(idx, val)
# Output:
# 0 a
# 1 b
# 2 c

# Set start number
#for idx, val in enumerate(my_list, 1):
#   print(idx, val)
# 1 a
# 2 b
# 3 c

def print_content_with_line_number(filename):
    with open(filename, 'rt') as f:
        for idx, line in enumerate(f, 1):
            print('{:<4d}: {}'.format(idx, line), end='')

print_content_with_line_number('02.py')
# Output:
# 1   : # 4.2 Delegating Iteration
# 2   : 
# 3   : # Defining __iter__() by yourself.
# 4   : 
# 5   : class Node:
# 6   :     def __init__(self, value):
# 7   :         self._value = value
# 8   :         self._children = []
# 9   :     
# 10  :     def __repr__(self):
# 11  :         return 'Node({!r})'.format(self._value)
# 12  : 
# 13  :     def add_child(self, node):
# 14  :         self._children.append(node)
# 15  : 
# 16  :     def __iter__(self):
# 17  :         return iter(self._children)
# 18  : 
# 19  : # Example
# 20  : if __name__ == '__main__':
# 21  :     root = Node(0)
# 22  :     child1 = Node(1)
# 23  :     child2 = Node(2)
# 24  :     root.add_child(child1)
# 25  :     root.add_child(child2)
# 26  : 
# 27  :     for ch in root:
# 28  :         print(ch)
# 29  : # Output:
# 30  : # Node(1)
# 31  : # Node(2)
