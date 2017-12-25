# 8.7 Calling a Method on a Parent Class

class A:
    def spam(self):
        print('A.spam')

class B(A):
    def spam(self):
        print('B.spam')
        super().spam()  # Call parent spam()

#b = B()
#b.spam()
# Output:
# B.spam
# A.spam

# super() is the handling of the __init__() method to make sure that
# parents are properly initialized.

class A:
    def __init__(self):
        self.x = 0

class B(A):
    def __init__(self):
        super().__init__()
        self.y = 0

b = B()
#print(b.x, b.y)  # 0 0


# Mutiple inheritance
class Base:
    def __init__(self):
        print('Base.__init__()')

class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__()')

class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__()')

class C(A,B):
    def __init__(self):
        super().__init__()
        print('C.__init__()')

c = C()
# Base.__init__()
# B.__init__()
# A.__init__()
# C.__init__()
