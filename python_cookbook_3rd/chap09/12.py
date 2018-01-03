# 9.12 Using Decorators to Path Class Definitions

def log_getattribute(cls):
    # Get the original implementation
    orig_getattribute = cls.__getattribute__

    # Make a new definition
    def new_getattribute(self, name):
        print('gettting:', name)
        return orig_getattribute(self, name)

    # Attach to the class and return
    cls.__getattribute__ = new_getattribute
    return cls

# Example use
@log_getattribute
class A:
    def __init__(self, x):
        self.x = x

    def spam(self):
        pass

a = A(42)
#print(a.x)
# gettting: x
# 42
a.spam()  # gettting: spam
