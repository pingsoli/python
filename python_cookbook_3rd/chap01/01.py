# 1.1 Unpacking a Sequence into separate Variables

# Any sequence (or iterable) can be unpacked into variables using
# a simple assignment operation.
p = (4, 5)
x, y = p

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data

# ACME 50 91.1 (2012, 12, 21)
# print(name, shares, price, date)

name, shares, price, (year, mon, day) = data

# ACME 50 91.1 2012 12 21
# print(name, shares, price, year, mon, day)

# What is iterable ?
# Answer: strings, files, iterators, generators.

s = 'hello'
a, b, c, d, e = s
print(a, b, c, d, e)  # h e l l o

# Discard certain values when unpacking.
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
_, shares, price, _ = data
# 50 91.1
#print(shares, price)
# 50 91.1


