# Python Memory Management

# Python use reference count system, if the reference of object is 0
# then free the space.

import sys

def show_sizeof(x, level=0):
    print('\t' * level, x.__class__, sys.getsizeof(x), x)

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_sizeof(xx, level + 1)
        else:
            for xx in x:
                show_sizeof(xx, level + 1)

#show_sizeof(None)
# <class 'NoneType'> 16 None

#show_sizeof(3)
# <class 'int'> 28 3

#show_sizeof(2 ** 63)
# <class 'int'> 36 9223372036854775808

#show_sizeof('')
# <class 'str'> 49 
#show_sizeof('My hovercraft is full of eels')


class Test:
    def __init__(self, name):
        self.name = name

t = Test('pingsoli')
show_sizeof(t)
# <class '__main__.Test'> 56 <__main__.Test object at 0x7f158f1220b8>
