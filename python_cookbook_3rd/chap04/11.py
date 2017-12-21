# 4.11 Iterating Over Multiple Sequences Simultaneously

# zip() function to combine multiple sequence.

xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
#for x, y in zip(xpts, ypts):
#    print(x, y)

# Outout:
# 1 101
# 5 78
# 4 37
# 2 15
# 10 62
# 7 99

# Merge two sequence to one, and use the shortest length of the two sequence.
a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
#for i in zip(a, b):
#    print(i)
# Output:
# (1, 'w')
# (2, 'x')
# (3, 'y')

a = [1, 2, 3]
b = ['x', 'y', 'z']
c = [10.0, 20.0, 30.0]
#for i in zip(a, b, c):
#    print(i)
# (1, 'x', 10.0)
# (2, 'y', 20.0)
# (3, 'z', 30.0)


# Create a dictionary with zip()
headers = ['name', 'shares', 'prices']
values = ['ACME', 100, 400.0]
s = dict(zip(headers, values))
#print(s)
# {'name': 'ACME', 'shares': 100, 'prices': 400.0}

#for name, value in zip(headers, values):
#    print(name, '=', value)
# Output:
# name = ACME
# shares = 100
# prices = 400.0
