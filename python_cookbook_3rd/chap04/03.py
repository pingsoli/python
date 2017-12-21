# 4.3 Creating New Iteration Patterns with Generators

# Generator:
# yield expression

def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

#for n in frange(0, 4, 0.5):
#    print(n)
# Output:
# 0
# 0.5
# 1.0
# 1.5
# 2.0
# 2.5
# 3.0
# 3.5

#print(list(frange(0, 4, 0.5)))
# [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]

# Understand generator underlying machanics.
def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done')

# Create the generator, notice no output appears
c = countdown(3)
print(c)
# <generator object countdown at 0x7fd38f672a40>

print(next(c))
print(next(c))
print(next(c))
print(next(c))
# Output:
# Starting to count from 3
# 3
# 2
# 1
# Done
# Traceback (most recent call last):
#   File "03.py", line 43, in <module>
#     print(next(c))
# StopIteration
