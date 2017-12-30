# 9.4 Defining a Decorator That Takes Arguments

from functools import wraps
import logging

def logged(level, name=None, message=None):
    '''
    Add logging to a function 
    '''
    def decorate(func):
        logname = name if name else func.__name__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

@logged(logging.DEBUG)
def add(x, y):
    return x + y

print(add(2, 3))  # 5

@logged(logging.CRITICAL, 'example', 'test')
def spam():
    print('spam')

#print(spam())
