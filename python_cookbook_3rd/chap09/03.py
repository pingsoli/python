# 9.3 Unwrapping a Decorator

# @somedecorator
# def add(x, y):
#     return x + y
# 
# orig_add = add.__wrapped__
# print(orig_add)


from functools import wraps

def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator1')
        return func(*args, **kwargs)
    return wrapper

def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator2')
        return func(*args, **kwargs)
    return wrapper

@decorator1
@decorator2
def add(x, y):
    return x + y

#print(add(2, 3))
# Decorator1
# Decorator2
# 5
