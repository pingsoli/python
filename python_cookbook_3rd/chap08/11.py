# 8.11 Simplifying the Initialization of Data Structures

class Structure:
    # Class variable that specifies expected fields
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

# Example class definitions
if __name__ == '__main__':
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']

    class Point(Structure):
        _fields = ['x', 'y']

    class Circle(Structure):
        _fields = ['radius']

        def area(self):
            return math.pi * self.radius ** 2

    s = Stock('ACME', 50, 90.1)
    p = Point(2, 3)
    c = Circle(4.0)
    
    s1 = Stock('ACME', 90)
# Traceback (most recent call last):
#   File "11.py", line 32, in <module>
#     s1 = Stock('ACME', 90)
#   File "11.py", line 8, in __init__
#     raise TypeError('Expected {} arguments'.format(len(self._fields)))
# TypeError: Expected 3 arguments
