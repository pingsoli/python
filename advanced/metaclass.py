# Python Metaclass

# Pay attention to Python 2.x and 3.x difference
# Python 2.x use __metaclass__
#   class MyClass:
#       __metaclass__ = MyMetaClass
#       pass
#
# Python 3.x use metaclass= as a arguments
#   class MyClass(metaclass=MyMetaClass):
#       pass
#
# NOTE:
# Python 2.x and 3.x is not compatible.

# A quick overview
class Foobar:
    pass


#print(type(Foobar))
# <class 'type'>
foo = Foobar()
#print(type(foo))
# <class '__main__.Foobar'>


# Simple metaclass use
MyClass = type('MyClass', (), {})
#print(MyClass)
# <class '__main__.MyClass'>

class Meta(type):
    pass

class Complex(metaclass=Meta):
    pass

#print(type(Complex))
# <class '__main__.Meta'>


# Magic methods
class Funky:
    def __call__(self):
        print('Look at me, I work like a function.')

f = Funky()
#f()
# Look at me, I work like a function.

class InterfaceMeta(type):
    def __new__(cls, name, parents, dct):
        # Create a lass_id if it's not specified
        if 'class_id' not in dct:
            dct['class_id'] = name.lower()

        # Open the specified file for writing
        if 'file' in dct:
            filename = dct['file']
            dct['file'] = open(filename, 'w')

        # We need to call type.__new__ to complete the initialization
        return super(InterfaceMeta, cls).__new__(cls, name, parents, dct)

#Interface = InterfaceMeta('Interface', (), dict(file='tmp.txt'))
# print(Interface.class_id)  # interface
# print(Interface.file)
# <_io.TextIOWrapper name='tmp.txt' mode='w' encoding='UTF-8'>

# Another approach
class Interface(metaclass=InterfaceMeta):
    file = 'tmp.txt'

# print(Interface.class_id)  # interface
# print(Interface.file)
# <_io.TextIOWrapper name='tmp.txt' mode='w' encoding='UTF-8'>

class UserInterface(Interface):
    file = 'foo.txt'

print(UserInterface.file)
# <_io.TextIOWrapper name='foo.txt' mode='w' encoding='UTF-8'>
print(UserInterface.class_id)  # userinterface
