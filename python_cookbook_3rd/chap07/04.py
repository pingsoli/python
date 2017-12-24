# 7.4 Returning Multiple Values from a Function

def myfunc():
    return 1, 2, 3

#print(myfunc())  # (1, 2, 3)
a, b, c = myfunc()
#print(a, b, c)  # 1 2 3

# Consider the above situation,
# myfunc() function return a tuple.
# With parentheses,
a = (1, 2)  # With parentheses
#print(a)  # (1, 2)
b = 1, 2  # Withoud parenttheses
#print(b)  # (1, 2)

d = myfunc()
#print(d)
# (1, 2, 3)

e, f = myfunc()
print(e, f)
# Traceback (most recent call last):
#   File "04.py", line 22, in <module>
#     e, f = myfunc()
# ValueError: too many values to unpack (expected 2)
