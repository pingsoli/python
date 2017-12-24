# 7.7 Capturing Variables in Anonymous Functions

x = 10
a = lambda y: x + y
#print(a(10))  # 20

x = 3
#print(a(12))  # 15

# NOTE:
funcs = [lambda x: x+n for n in range(5)]
# for f in funcs:
#     print(f(0))
# Ouput:
# 4
# 4
# 4
# 4
# 4

# Capturing the value of n at the time of definition.
funcs = [lambda x, n=n: x+n for n in range(5)]
for f in funcs:
    print(f(0))
# Output:
# 0
# 1
# 2
# 3
# 4
