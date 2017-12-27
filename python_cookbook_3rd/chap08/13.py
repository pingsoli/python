# 8.13 Implementing a Data Model or Type System

# Base class. Use a descriptor to set a value
class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

# Descriptor for enforcing types
class Typed(Descriptor):
    expected_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expectd ' + str(self.expected_type))
        super().__set__(instance, value)
    
# Descriptor for enforcing values
class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        super().__set__(instance, value)

class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super().__init__(name, **opts)

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('size must be < ' + str(self.size))
        super().__set__(instance, value)

class Integer(Typed):
    expected_type = int

class UnsignedInteger(Integer, Unsigned):
    pass

class Float(Typed):
    expected_type = float

class UnsignedFloat(Float, Unsigned):
    pass

class String(Typed):
    expected_type = str

class SizedString(String, MaxSized):
    pass


class Stock:
    # Specify constrains
    name = SizedString('name', size=8)
    shares = UnsignedInteger('shares')
    price = UnsignedFloat('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

s = Stock('ACME', 50, 90.1)
#print(s.name)  # ACME
s.shares = 75

#s.shares = -10
# Traceback (most recent call last):
#   File "13.py", line 73, in <module>
#     s.shares = -10
#   File "13.py", line 20, in __set__
#     super().__set__(instance, value)
#   File "13.py", line 26, in __set__
#     raise ValueError('Expected >= 0')
# ValueError: Expected >= 0

#s.price = 'so much'
# Traceback (most recent call last):
#   File "13.py", line 82, in <module>
#     s.price = 'so much'
#   File "13.py", line 19, in __set__
#     raise TypeError('Expectd ' + str(self.expected_type))
# TypeError: Expectd <class 'float'>

#s.name = 'AAAAAAAAAAA'
# Traceback (most recent call last):
#   File "13.py", line 92, in <module>
#     s.name = 'AAAAAAAAAAA'
#   File "13.py", line 20, in __set__
#     super().__set__(instance, value)
#   File "13.py", line 37, in __set__
#     raise ValueError('size must be < ' + str(self.size))
# ValueError: size must be < 8


# Use decorator to apply constrains
def check_attributes(**kwargs):
    def decorate(cls):
        for key, value in kwargs.items():
            if isinstance(value, Descriptor):
                value.name = key
                setattr(cls, key, value)
            else:
                setattr(cls, key, value(key))
        return cls
    return decorate

# Example
@check_attributes(name=SizedString(size=8),
                  shares=UnsignedInteger,
                  price=UnsignedFloat)

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


# Another approach
# A metaclass that applies checking
class checkedmeta(type):
    def __new__(cls, clsname, bases, methods):
        # Attach attribute names to the descriptors
        for key, value in methods.items():
            if isinstance(value, Descriptor):
                value.name = key
        return type.__new__(cls, clsname, bases, methods) 

class Stock(metaclass=check_attributes):
    name = SizedString(size=8)
    shares = UnsignedInteger()
    price = UnsignedFloat()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

