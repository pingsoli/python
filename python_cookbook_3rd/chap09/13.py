# 9.13 Using a Metaclass to Control Instance Creation

class NoInstances(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly")

# Example
class Spam(metaclass=NoInstances):
    @staticmethod
    def grok(x):
        print('Spam.grok')

#Spam.grok(42)  # Spam.grok
# s = Spam()  # It's impossible to create an instance directly
# Traceback (most recent call last):
#   File "13.py", line 14, in <module>
#     s = Spam()
#   File "13.py", line 5, in __call__
#     raise TypeError("Can't instantiate directly")
# TypeError: Can't instantiate directly


class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)
    
    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance

class Spam(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam')

a = Spam()  # Creating Spam
b = Spam()
#print(a is b)  # True
c = Spam()
#print(c is a)  # True


import weakref

class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj

# Example
class Spam(metaclass=Cached):
    def __init__(self, name):
        print('Creating Spam({!r})'.format(name))
        self.name = name

a = Spam('Guido')
b = Spam('Diana')
c = Spam('Guido')
#print(a is c)
# Creating Spam
# Creating Spam('Guido')
# Creating Spam('Diana')
# True
