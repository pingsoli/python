# 8.5 Encapsulating Names in a Class

# single underscore(_) and double underscore(__)

class A:
    def __init__(self):
        self._internal = 0  # An internal attribute
        self.public = 1     # A public attribute

    def public_method(self):
        '''
        A public method
        '''
        print(self.public)

    def _internal_method(self):
        print(self._internal) 

a = A()
print(a._internal)
print(a.public)
# 0
# 1

# Conventions, single undersocre(_) is assumed to be internal implementation.
# Python don't actually prevent someone from accessing internal names.
