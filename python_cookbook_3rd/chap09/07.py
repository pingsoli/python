# 9.7 Enforcing Type Checking on a Function Using a Decorator

from inspect import signature
from functools import wraps

de typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        # If in optimized mode, disable type checking
        if not __debug__:
            return func

        # Map function argument names to suppplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            'Argument {} must be {}'.format(
                                                name, 
                                                bound_types[name])
                        )
            return func(*args, *kwargs)
        return wrapper
    return decorate

@typeassert(int, z=int)
def spam(x, y, z=42):
    print(x, y, z)

#spam(1, 2, 3)
# 1 2 3

#spam(1, 'hello', 3)
#1 hello 3

#spam(1, 'hello', 'world')
# Traceback (most recent call last):
#   File "07.py", line 40, in <module>
#     spam(1, 'hello', 'world')
#   File "07.py", line 26, in wrapper
#     bound_types[name])
# TypeError: Argument z must be <class 'int'>


from inspect import signature
def spam(x, y, z=42):
    pass

sig = signature(spam)
#print(sig)  # (x, y, z=41)
#print(sig.parameters)
# OrderedDict([('x', <Parameter "x">), ('y', <Parameter "y">), ('z', <Parameter "z=42">)])

#print(sig.parameters['z'].name)  # z
#print(sig.parameters['z'].default)  # 42
#print(sig.parameters['z'].kind)  # POSITIONAL_OR_KEYWORD

bound_types = sig.bind_partial(int, z=int)
#print(bound_types)
# <BoundArguments (x=<class 'int'>, z=<class 'int'>)>

#print(bound_types.arguments)
# OrderedDict([('x', <class 'int'>), ('z', <class 'int'>)])

bound_values = sig.bind(1, 2, 3)
#print(bound_values.arguments)
# OrderedDict([('x', 1), ('y', 2), ('z', 3)])

@typeassert(int, list)
def bar(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items

#print(bar(2))  # [2]

#print(bar(2, 3))
# Traceback (most recent call last):
#   File "07.py", line 83, in <module>
#     print(bar(2, 3))
#   File "07.py", line 26, in wrapper
#     bound_types[name])
# TypeError: Argument items must be <class 'list'>

#print(bar(4, [1, 2, 3]))  # [1, 2, 3, 4]
