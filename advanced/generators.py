# Generators, a bit difficult to understand.

import random

def lottery():
    # return 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 45
    yield random.randint(1, 45)

#for random_number in lottery():
#    print("And the next number is: %d" %(random_number))


# Exercise
# Fabonacci, only use two variables 
def fib():
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a + b

import types
if type(fib()) == types.GeneratorType: 
    print("Good, The fib function is a generator")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break
