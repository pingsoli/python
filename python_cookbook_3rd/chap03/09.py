# 3.9 Calculating with Large Numberical Arrays

# Python lists
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

#print(x * 2)  # [1, 2, 3, 4, 1, 2, 3, 4]
#print(x + 10)  # Wrong
#print(x + y)  # [1, 2, 3, 4, 5, 6, 7, 8]

# Numpy arrays
# Is not installed as default.
import numpy as np
ax = np.array([1, 2, 3, 4])
ay = np.array([5 ,6, 7, 8])
print(ax * 2)
