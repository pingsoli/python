# 9.1 Putting a Wrapper Around a Function

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
        print(func.__name__, end-start)
        return result 
    return wrapper

@timethis
def countdown(n):
    '''
    Counts down
    '''
    while n > 0:
        n -= 1

countdown(100000)
# countdown 0.007547616958618164
#                    +-------+
#                    | start |
#                    +-------+
#                    
# +-------+          +-------+
# | logic | - wrap ->| logic |
# +-------+          +-------+
#                    
#                    +-------+
#                    |  end  |
#                    +-------+
