# 9.14 Capturing Class Attribute Definition Order

from collections import OrderedDict

# A set of descriptors for various types
class Typed:
    _expected_type = type(None)
    def __init__(self, name=None):
        self._name = name

    def __set__(self, instance, value):
        if not isinstance(value, self._expected_type):
            raise TypeError('Expected ' + str(self._expected_type))
        instance.__dict__[self._name] = value

class Integer(Typed):
    _expected_type = int

class Float(Typed):
    _expected_type = float

class String(Typed):
    _expected_type = str

class OrderedMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        d = dict(clsdict)
        order = []
        for name, value in clsdict.items():
            if isinstance(value, Typed):
                value._name = name
                order.append(name)
        d['_order'] = order
        return type.__new__(cls, clsname, bases, d)
    
    @classmethod
    def __prepare__(cls, clsname, bases):
        return OrderedDict()

class Structure(metaclass=OrderedMeta):
    def as_csv(self):
        return ','.join(str(getattr(self, name)) for name in self._order)

class Stock(Structure):
    name = String()
    shares = Integer()
    price = Float()
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

s = Stock('GOOG', 100, 490.1)
# print(s.name)  # GOOG
# print(s.as_csv())  # GOOG,100,490.1

#t = Stock('AAPL', 'a lot', 610.23)
# Traceback (most recent call last):
#   File "14.py", line 57, in <module>
#     t = Stock('AAPL', 'a lot', 610.23)
#   File "14.py", line 50, in __init__
#     self.shares = shares
#   File "14.py", line 13, in __set__
#     raise TypeError('Expected ' + str(self._expected_type))
# TypeError: Expected <class 'int'>
