# 9.3 Unwrapping a Decorator

@somedecorator
def add(x, y):
    return x + y

orig_add = add.__wrapped__
print(orig_add)
