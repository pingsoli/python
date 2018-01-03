# 9.8 Defining Decorators As Part of a Class

from functools import wraps

class A:
    # Decorator as an instance method
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 1')
            return func(*args, **kwargs)
        return wrapper

    # Decorator as a class method
    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 2')
            return func(*args, **kwargs)
        return wrapper

a = A()

@a.decorator1
def spam():
    pass

@a.decorator2
def grok():
    pass

#spam()
# Decorator 1

#grok()
# Decorator 2


class Person:
    # Create a property instance
    first_name = property()

    # Apply decorator methods
    @first_name.getter
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Excepted a string')
        self._first_name = value
        
p = Person()
p.first_name = 'pingsoli'
print(p.first_name)  # pingsoli
