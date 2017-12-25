# 8.6 Creating Managed Attributes

class Person:

    def __init__(self, first_name):
        self.first_name = first_name

    # Getter function
    @property
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Excepted a string')
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't be delete attribute")

a = Person('Guido')
#print(a.first_name)  # Guido
#a.first_name = 42
# Traceback (most recent call last):
#   File "06.py", line 27, in <module>
#     a.first_name = 42
#   File "06.py", line 17, in first_name
#     raise TypeError('Excepted a string')
# TypeError: Excepted a string

#del a.first_name
# Traceback (most recent call last):
#   File "06.py", line 35, in <module>
#     del a.first_name
#   File "06.py", line 23, in first_name
#     raise AttributeError("Can't be delete attribute")
# AttributeError: Can't be delete attribute

# class Person:
#     def __init__(self, first_name):
#         self.set_first_name(first_name)
# 
#     # Getter function
#     def get_first_name(self):
#         return self._first_name
# 
#     # Setter function
#     def set_first_name(self, value):
#         if not isinstance(value, str):
#             raise TypeError('Excepted a string')
#         self._first_name = value
# 
#     # Deleter function  (optional)
#     def del_first_name(self):
#         raise AttributeError("can't be delete attribute")
# 
#     # Make a property from existing get/set methods
#     name = property(get_first_name, set_first_name, del_first_name)

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

c = Circle(4.0)
print(c.radius)  # 4.0
# Notice lack of ()
print(c.area)  # 50.26548245743669
print(c.perimeter)  # 25.132741228718345
