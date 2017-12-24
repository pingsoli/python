# 7.8 Making an N-Argument Callable Work As a Callable with Fewer Arguments

def spam(a, b, c, d):
    print(a, b, c, d)

from functools import partial

s1 = partial(spam, 1)
#s1(2, 3, 4)  # 1 2 3 4

#s1(4, 5, 6)  # 1 4 5 6


s2 = partial(spam, d=42)
#s2(1, 2, 3)  # 1 2 3 42

s3 = partial(spam, 1, 2, d=42)
# s3(3)  # 1 2 3 42

points = [(1, 2), (3, 4), (5, 6), (7, 8)]

import math
def instance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)
