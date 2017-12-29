# 8.23 Managing Memory in Cyclic Data Structures

import weakref

#class Node:
#    def __init__(self, value):
#        self.value = value
#        self._parent = None
#        self.children = []
#
#    def __repr__(self):
#        return 'Node({!r:})'.format(self.value)
#
#    # property that manages that parent as a weak-reference
#    @property
#    def parent(self):
#        return self._parent if self._parent is None else self._parent()
#
#    @parent.setter
#    def parent(self, node):
#        self._parent = weakref.ref(node)
#
#    def add_child(self, child):
#        self.children.append(child)
#        child.parent = self
#
#root = Node('parent')
#c1 = Node('child')
#root.add_child(c1)

#print(root)
#print(root.__dict__)
# {'value': 'parent', '_parent': None, 'children': [Node('child')]}


# Python don't provide garbage collection.
class Data:
    def __del__(self):
        print('Data.__del__')

# Node clas involving a cycle
class Node:
    def __init__(self):
        self.data = Data()
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

#a = Data()
#del a  # Data.__del__
#a = Node()
#del a  # Data.__del__
a = Node()
a.add_child(Node())
#Data.__del__
#Data.__del__

# Python apply reference count, when reaching 0, it will be deleted
# immediately.
