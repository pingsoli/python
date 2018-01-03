# 9.19 Initializing Class Members at Definition Time

import operator

class StructTupleMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for n, name in enumerate(cls._fields):
            setattr(cls, name, property(operator.itemgetter(n)))

class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields = []
    def __new__(cls, *args):
        if len(args) != len(cls._fields):
            raise ValueError('{} arguments required'.format(cls._fields))
        return super().__new__(cls, args)

class Stock(StructTuple):
    _fields = ['name', 'shares', 'price']

class Point(StructTuple):
    _fields = ['x', 'y']

s = Stock('ACME', 50, 90.1)
#print(dir(s))
# print(s.name)  # ACME
# print(s.shares * s.price)  # 4505.0

# There is no setter and getter.
# s.name = 'GOOG'
#
# Traceback (most recent call last):
#   File "19.py", line 30, in <module>
#     s.name = 'GOOG'
# AttributeError: can't set attribute
