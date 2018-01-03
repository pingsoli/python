# 9.11 Writing Decorators That Add Arguments to Wrapped Functions

# from functools import wraps
# 
# def optional_debug(func):
#     @wraps(func)
#     def wrapper(*args, debug=False, **kwargs):
#         if debug:
#             print('Calling ', func.__name__)
#         return func(*args, **kwargs)
#     return wrapper
# 
# @optional_debug
# def spam(a, b, c):
#     print(a, b, c)
# 
# #spam(1, 2, 3)  # 1 2 3
# spam(1, 2, 3, debug=True)
# # Calling  spam
# # 1 2 3


from functools import wraps
import inspect

def optional_debug(func):
    if 'debug' in inspect.getargspec(func).args:
        raise TypeError('debug argument already defined')

    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling ', func.__name__)
        return func(*args, **kwargs)

    sig = inspect.signature(func)
    parms = list(sig.parameters.values())
    parms.append(inspect.Parameter('debug', 
                                    inspect.Parameter.KEYWORD_ONLY,
                                    default=False))
    wrapper.__signature__ = sig.replace(parameters=parms)
    return wrapper

@optional_debug
def add(x, y):
    return x + y

#print(inspect.signature(add))
# (x, y, *, debug=False)
#print(add(2, 3))  # 5
