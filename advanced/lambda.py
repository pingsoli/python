# Lambda Expression Learning

# Map, Filter, Reduce

# Basic usage
f = lambda x, y : x + y
#print(f(1, 1))  # 2

# Map
# map(function_to_apply, list_of_inputs)
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, items))
#print(squared)  # [1, 4, 9, 16, 25]

def multiply(x):
    return (x*x)

def add(x):
    return (x+x)

# funcs = [multiply, add]
# for i in range(5):
#     value = list(map(lambda x: x(i), funcs))
#     print(value)
# Output:
# [0, 0]
# [1, 2]
# [4, 4]
# [9, 6]
# [16, 8]


# Filter
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
#print(less_than_zero)
# [-5, -4, -3, -2, -1]


# Reduce
product = 1
list = [1, 2, 3,  4]
for num in list:
    product = product * num

from functools import reduce 

product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(product)  # 24
