def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# The performance is really bad, when the n is larger and 
# larger, the calculation is slower and slower, finnaly
# we can't bear the speed of executing.

# Next, we gonna to use 
