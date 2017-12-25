# 8.9 Creating a New Kind of Class or Instance Attribute

class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Excepted a int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

#print(Integer.__dict__)
# {
#   '__module__': '__main__', 
#   '__init__': <function Integer.__init__ at 0x7f0cfbeb06a8>, 
#   '__get__': <function Integer.__get__ at 0x7f0cfbeb0730>, 
#   '__set__': <function Integer.__set__ at 0x7f0cfbeb07b8>, 
#   '__delete__': <function Integer.__delete__ at 0x7f0cfbeb0840>, 
#   '__dict__': <attribute '__dict__' of 'Integer' objects>, 
#   '__weakref__': <attribute '__weakref__' of 'Integer' objects>, 
#   '__doc__': None
# }

class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

#print(Point.__dict__)
# {
#   '__module__': '__main__', 
#   'x': <__main__.Integer object at 0x7f815810c1d0>,   
#   'y': <__main__.Integer object at 0x7f815810c208>, 
#   '__init__': <function Point.__init__ at 0x7f81580fc8c8>, 
#   '__dict__': <attribute '__dict__' of 'Point' objects>, 
#   '__weakref__': <attribute '__weakref__' of 'Point' objects>, 
#   '__doc__': None
# }
p = Point(2, 3)
#print(p.x, p.y)  # 2 3
p.x = 5
#p.x = 5.2
# Traceback (most recent call last):
#   File "09.py", line 54, in <module>
#     p.x = 5.2
#   File "09.py", line 15, in __set__
#     raise TypeError('Excepted a int')
# TypeError: Excepted a int
