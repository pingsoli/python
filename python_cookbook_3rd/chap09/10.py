# 9.10 Applying Decorators to Class and Static Methods

import time
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, *kwargs)
        end = time.time()
        print(end-start)
        return r
    return wrapper

# Class illustrating application of the decorator to different kinds of 
# methods
class Spam:
    @timethis
    def instance_method(self, n):
        print(self, n)
        while n > 0:
            n -= 1

    @classmethod
    @timethis
    def class_method(cls, n):
        print(cls, n)
        while n > 0:
            n -= 1

    @staticmethod
    @timethis
    def static_method(n):
        print(n)
        while n > 0:
            n -= 1

s = Spam()

#s.instance_method(100000)
# <__main__.Spam object at 0x7ff79e5d98d0> 100000
# 0.006466388702392578

#Spam.class_method(100000)
# <class '__main__.Spam'> 100000
# 0.00569915771484375

#Spam.static_method(100000)
# 100000
# 0.0057566165924072266

from abc import ABCMeta, abstractmethod

class A(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def method(cls):
        pass
