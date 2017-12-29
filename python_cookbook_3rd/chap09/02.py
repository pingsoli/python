# 9.2 Preserving Function Metadata When Writing

# When you write a decorator, the metadata contains 
# the name, doc string, annotations, and calling signature.

import time
from functools import wraps

def timethis(func):
    '''
    Decorator that reports the execution time
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper

@timethis
def countdown(n:int):
    '''
    Counts down
    '''
    while n > 0:
        n -= 1

countdown(10000)  # countdown 0.0005674362182617188
#print(countdown.__name__)  # countdown
#print(countdown.__doc__)   # '\n\tCounts down\n\t'
#print(countdown.__annotations__)  # {'n': <class 'int'>}
#print(countdown.__wrapped__)

from inspect import signature
print(signature(countdown))  # (n:int)
