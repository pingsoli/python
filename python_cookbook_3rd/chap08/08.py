# 8.8 Extending a Property in a Subclass

class Person:
    def __init__(self, name):
        self.name = name

    # Getter function
    @property
    def name(self):
        return self._name
    
    # Getter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Excepted a string')
        self._name = value
    
    # Deleter function
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")

class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to ', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)

#s = SubPerson('Guido')
# Setting name to  Guido
#print(s.name)
# Getting name
# Guido

#s.name = 'Larry'  # Setting name to  Larry
#s.name = 42
# Traceback (most recent call last):
#   File "08.py", line 47, in <module>
#     s.name = 42
#   File "08.py", line 33, in name
#     super(SubPerson, SubPerson).name.__set__(self, value)
#   File "08.py", line 16, in name
#     raise TypeError('Excepted a string')
# TypeError: Excepted a string

print([method for method in dir(object) if callable(getattr(object, method))])
# ['__class__', '__delattr__', '__dir__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
