# 10.4 Spliting a Module into Multi Files

'''
# mymodule.py

class A:
    def spam(self):
        print('A.spam')

class B:
    def bar(self):
        print('B.bar')

# ======================================================================

# Split mymodule.py into two files, one for each class definition.
# mymodule/
#     __init__.py
#     a.py
#     b.py

# a.py
class A:
    def spam(self):
        print('A.spam')

# b.py
class B:
    def bar(self):
        print('B.bar')

# __init__.py
from .a import A
from .b import B

# ======================================================================
'''

# outer.py
# import mymodule
# a = mymodule.A()
# a.spam()  # A.spam
# 
# b = mymodule.B()
# b.bar()  # B.bar
# 
# # Or there is another way
# from mymodule.a import A
# from mymodule.b import B

# More concration
from mymodule import A, B

a = A()
a.spam()  # A.spam

b = B()
b.bar()  # B.bar

# ======================================================================
