# 8.10 Using Lazily Computed Properties

class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        return 2 * math.pi * self.radius

#print(Circle.__dict__)
# {
#   '__module__': '__main__', 
#   '__init__': <function Circle.__init__ at 0x7f02045af840>, 
#   'area': <__main__.lazyproperty object at 0x7f02045bf358>, 
#   'perimeter': <__main__.lazyproperty object at 0x7f02045bf390>, 
#   '__dict__': <attribute '__dict__' of 'Circle' objects>, 
#   '__weakref__': <attribute '__weakref__' of 'Circle' objects>, 
#   '__doc__': None
# }

c = Circle(4.0)
#print(c.radius)  # 4.0
#print(c)
print(c.area)  # 50.26548245743669
print(c.perimeter)  # 25.132741228718345
print(c.__dict__)
# {'radius': 4.0, 'area': 50.26548245743669, 'perimeter': 25.132741228718345}
#print(dir(c))
