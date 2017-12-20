# 2.15 Interpolating Variables in Strings

s = '{name} has {n} messages.'
#print(s.format(name='pingsoli', n=23))  # pingsoli has 23 messages.

# Alternatively, use combination of format_map() and vars().
name = 'pingsoli'
n = 23
#print(s.format_map(vars()))  # pingsoli has 23 messages.

# vars() also works with instance.
class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info('pingsoli', 23)
#print(s.format_map(vars(a)))  # pingsoli has 23 messages.

# format() and format_map() do not deal gracefully with missing 
# values.
# print(s.format_map(name='pingsoli'))
#
# Error Message:
# Traceback (most recent call last):
#   File "15.py", line 22, in <module>
#     print(s.format_map(name='pingsoli'))
# TypeError: format_map() takes no keyword arguments

# One way to avoid this is to define an alternative dictionary class 
# with a __missing__() method, as in the following.
class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

del n
name = 'pingsoli'
#print(s.format_map(safesub(vars())))  # pingsoli has {n} messages.
