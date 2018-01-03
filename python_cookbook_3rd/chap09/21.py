# 9.21 Avoiding Repetitive Property Methods

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# 
#     @property
#     def name(self):
#         return self._name
# 
#     @name.setter
#     def name(self, value):
#         if not isinstance(value, str):
#             raise TypeError('name must be a string')
#         self._name = value
# 
#     @property
#     def age(self):
#         return self._age
# 
#     @age.setter
#     def age(self, value):
#         if not isinstance(value, int):
#             raise TypeError('age must be a int')
#         self._age = value
# 
# p = Person('pingsoli', 50)
# #print(p.name, p.age)  # pingsoli 50
# p.name = 'test'
# p.age = 30
# #print(p.name, p.age)  # test 30

def typed_property(name, expected_type):
    storage_name = '_' + name

    @property
    def prop(self):
        return getattr(self, storage_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError(
                    '{} must be a {}'.format(name, expected_type)
                    )
            setattr(self, storage_name, value)
    return prop

# class Person:
#     name = typed_property('name', str)
#     age = typed_property('age', int)
# 
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#p = Person('pingsoli', 50)
#print(p.name, p.age)  # pingsoli 50
#p.name = 'test'
#p.age = 30
#print(p.name, p.age)  # test 30
#print(p.__dict__)
# {'_name': 'test', '_age': 30}


# class Foo:
#     def meth(self):
#         self.name = 'test'
# 
# foo = Foo()
# print(foo.meth() == Foo.meth(foo))  # True

# class C:
#     pass
# 
# def meth(myself, arg):
#     myself.val = arg
#     return myself.val
# 
# C.meth = meth
# c = C()
#print(c.meth('test'))

from functools import partial

String = partial(typed_property, expected_type=str)
Integer = partial(typed_property, expected_type=int)

class Person:
    name = String('name')
    age = Integer('age')

    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person('pingsoli', 100)
print(dir(p))
# No getter and setter function
#print(p.name, p.age)  # Will get an error
