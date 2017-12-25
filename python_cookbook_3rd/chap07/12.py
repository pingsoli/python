# 7.12 Accessing Variables Defined Inside a Closure

def sample():
    n = 0
    # Closure function
    def func():
        print('n =', n)

    # Accessor method for n
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # Attach as function attributes
    func.get_n = get_n
    func.set_n = set_n
    return func
    
f = sample()
#f()  # n = 0
f.set_n(10)
#f()  # n = 10
#print(f.get_n())  # 10

# Inner variable, nonlocal.
# funtion attributes allow the accessor method to be attached to the closure
# function in a straight-forward manner.

import sys
class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            # Return the top frame object from the call stack
            locals = sys._getframe(1).f_locals
        
        # Update instance dictionary with callables
        self.__dict__.update((key, value) for key, value in locals.items()
                              if callable(value))
        print(self.__dict__)

    # Redirect special methods
    def __len__(self):
        return self.__dict__['__len__']()

# Example use
def Stack():
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()

s = Stack()
#print(s)
# <__main__.ClosureInstance object at 0x7f94b1bba8d0>
s.push(10)
s.push(20)
s.push('hello')
#print(len(s))  # 3
# print(s.pop())
# print(s.pop())
# print(s.pop())
# hello
# 20
# 10

# {'__len__': <function Stack.<locals>.__len__ at 0x7eff8024aae8>, 'pop': <function Stack.<locals>.pop at 0x7eff8024aa60>, 'push': <function Stack.<locals>.push at 0x7eff8024a9d8>}
