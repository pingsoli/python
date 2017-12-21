# 3.7 Working with Infinity and NaNs

# infinity and negative infinity.
# NaN (Not a Number)

a = float('inf')
b = float('-inf')
c = float('nan')
#print(a, b, c)  # inf -inf nan

# Test
import math
#print(math.isinf(a))  # True
#print(math.isnan(c))  # True

d = float('nan')
print(c == d)  # False
