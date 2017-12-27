# String Formatting

# Main two ways:
# 1) Old C-style String Formatting
# 2) format() 

#print('%s %s' % ('one', 'two'))  # one two
#print('{} {}'.format('one', 'two'))  # one two

# Old C-Sytle Formatting Arguments
# %s - string
# %d - digital integer
# %f - float, %.8f
# %x/%X - hex

#print('{1} {0}'.format('one', 'two'))  # two one

# Value conversion
# new-style simple formatter calls by default the __format__() method
# of an object for its representation. If you just want to render 
# the output of str(...) or repr(...) you can use the !s or !r conversion
# flags.

class Data(object):
    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'

d = Data()
#print('%s %r' % (d, d))  # str repr
#print('{0!s} {0!r}'.format(d))  # str repr


# Padding and aligning strings
# Align right, left and center
# C-style default right align, '-' stands for left alignment
# 
# new-style
# :>   right alignment
# :<   left alignment
# :^   center alignment
# :*<  choose '*' as padding character

#print('%10s' % ('test'))  #       test
# print('{:*>10}'.format('test'))  # ******test
# print('{:*<10}'.format('test'))  # test******
# print('{:*^10}'.format('test'))  # ***test***


# Truncating long strings
#print('%.5s' % ('abcdefghi'))  # abcde
#print('{:.5}'.format('abcdefghi'))  # abcde

# Combinint truncating and padding
#print('-10.5s' % ('abcdefghi')) # Get error message
#print('{:*<10.5}'.format('abcdefghi'))   # abcde*****

# Numbers
#print('%d' % (42,))  # 42
#print('{:d}'.format(42))  # 42

# Padding numbers
#print('%4d' % (42,))  #  42
#print('{:*>4d}'.format(42))  # **42

#print('06.2f' % (3.14159265358,))
#print('{:06.2f}'.format(3.14159265358))  # 003.14


# Signed numbers
#print('%+d' % (42,))  # +42
#print('{:+d}'.format(42))  # +42
#print('{: d}'.format((- 42)))  # -42


# Named placeholders
data = {'first': 'Hodor', 'last': 'Hodor!'}
#print('{first} {last}'.format(**data))  # Hodor Hodor!
#print('{first} {last}'.format(first='Hodor', last='Hodor!'))  # Hodor Hodor!

# Getitem and Getattr
pingsoli = {'first': 'pingsoli', 'last': 'haha'}
#print('{p[first]} {p[last]}'.format(p=pingsoli))  # pingsoli haha

d = [1, 2, 3, 4, 5]
#print('{d[2]} {d[4]}'.format(d=d))  # 3 5

# Datetime
from datetime import datetime
#print('{:%Y-%m-%d %H:%M:%S}'.format(datetime.today()))  # 2017-12-27 10:10:34

# Custome objects
class Test(object):
    def __format__(self, format):
        if format == 'hello':
            return 'world'
        return 'test'

t = Test()
# print('{:hello}'.format(t))  # world
# print('{:foo}'.format(t))  # test
