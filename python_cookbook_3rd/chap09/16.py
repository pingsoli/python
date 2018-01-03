# 9.16 Enforcing an Argument Signature on *args and **kwargs

from inspect import Signature, Parameter

params = [
           Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
           Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42),
           Parameter('z', Parameter.KEYWORD_ONLY, default=None)
         ]
sig = Signature(params)
#print(sig)   # (x, y=42, *, z=None)

def func(*args, **kwargs):
    bound_values = sig.bind(*args, **kwargs)
    for name, value in bound_values.arguments.items():
        print(name, value)

# Try various examples
#func(1, 2, z=3)
# x 1
# y 2
# z 3

#func(1)
# x 1

#func(1, z=3)
# x 1
# z 3

#func(y=1, x=2)
# x 2
# y 1

#func(1, 2, 3, 4)
# Traceback (most recent call last):
#   File "16.py", line 35, in <module>
#     func(1, 2, 3, 4)
#   File "16.py", line 14, in func
#     bound_values = sig.bind(*args, **kwargs)
#   File "/usr/local/python-3.6.3/lib/python3.6/inspect.py", line 2965, in bind
#     return args[0]._bind(args[1:], kwargs)
#   File "/usr/local/python-3.6.3/lib/python3.6/inspect.py", line 2892, in _bind
#     'too many positional arguments') from None
# TypeError: too many positional arguments

#func(1, y=2, x=3)
# Traceback (most recent call last):
#   File "16.py", line 47, in <module>
#     func(1, y=2, x=3)
#   File "16.py", line 14, in func
#     bound_values = sig.bind(*args, **kwargs)
#   File "/usr/local/python-3.6.3/lib/python3.6/inspect.py", line 2965, in bind
#     return args[0]._bind(args[1:], kwargs)
#   File "/usr/local/python-3.6.3/lib/python3.6/inspect.py", line 2906, in _bind
#     arg=param.name)) from None
# TypeError: multiple values for argument 'x'
