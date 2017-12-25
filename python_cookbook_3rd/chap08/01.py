# 8.1 Changing the String Representation of Instances

# java - toString()
# define your own __str__ and __repr__ method

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#    def __repr__(self):
#        return 'Pair({0.x!r}, {0.y!r})'.format(self)
    
    # Another implementation, is same as the above code.
    def __repr__(self):
        return 'Pair(%r, %r)' % (self.x, self.y)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)

# __repr__() method return the code representation of an instance.
# __str__() method converts the instance to a string.

p = Pair(3, 4)
print('p is {0!r}'.format(p))  # p is Pair(3, 4)
print('p is {0}'.format(p))  # p is (3, 4)

# 0.x!r   the 0 is actually the instance of self.
# Alternative implementation.
# def __repr__(self):
#     return 'Pair(%r, %r)' % (self.x, self.y)
