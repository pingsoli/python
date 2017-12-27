# 8.15 Delegating Attribute Access

class A:
    def spam(self, x):
        pass

    def foo(self):
        pass

class B:
    def __init__(self):
        self._a = A()
            
    def spam(self, x):
        # Delegate to the internal self._a instance
        return self._a.spam()

    def foo(self):
        # Delegate to the internal self._a instance
        return self._a.foo()

    def bar(self):
        pass

class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        print('getattr: ', name)
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, name, value):
        print('setattr: ', name, value)
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            setattr(self._obj, name, value)
    
    # Delegate attribute deletion
    def __delattr__(self, name):
        print('delattr: ', name)
        if name.startswith('_'):
            super().__delattr__(name)
        else:
            delattr(self._obj, name)

class Spam:
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print('Spam.bar', self.x, y)

s = Spam(2)
p = Proxy(s)
# setattr:  _obj <__main__.Spam object at 0x7f7fda4a2898>

#print(p.x)
# getattr:  x
# 2

#p.bar(3)
# getattr:  bar
# Spam.bar 2 3

#p.x = 37
# setattr:  x 37
