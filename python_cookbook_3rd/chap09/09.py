# 9.9 Defining Decorators As Classes

import types
from functools import wraps

class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)

@Profiled
def add(x, y):
    return x + y

class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)

#print(add(2, 3))  # 5
#print(add(4, 5))  # 9
#print(add.ncalls)  # 2

s = Spam()
#s.bar(1)  # <__main__.Spam object at 0x7f5b693762b0> 1
#s.bar(2)  # <__main__.Spam object at 0x7f5b693762b0> 2
#s.bar(3)  # <__main__.Spam object at 0x7f5b693762b0> 3
#print(Spam.bar.ncalls)  # 3


def profiled(func):
    ncalls = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal ncalls
        ncalls += 1
        return func(*args, **kwargs)
    wrapper.ncalls = lambda: ncalls
    return wrapper

@profiled
def add(x, y):
    return x + y

print(add(2, 3))  # 5
print(add(4, 5))  # 9
print(add.ncalls())  # 2
