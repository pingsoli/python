# Decorators In Python

# =====================================================================

def my_decorator(some_function):

    def wrapper():
        print('something is happening before some_function() is called')
        some_function()
        print('something is happening after some_function() is called')

    return wrapper

def just_some_function():
    print('wheee!')

just_some_function = my_decorator(just_some_function)
#just_some_function()
# Output:
# something is happening before some_function() is called
# wheee!
# something is happening after some_function() is called

# =====================================================================
# Real World Examples
import time

def timing_function(some_function):

    '''
    Output the time a funtion takes
    '''

    def wrapper():
        start = time.time()
        some_function()
        end = time.time()
        return 'Time elapse: ' + str((end - start)) + '\n'
    return wrapper

@timing_function
def my_function():
    num_list = []
    # Do some job to comsume some time
    for num in range(0, 10000):
        num_list.append(num)
    
#print(my_function())  # Time elapse: 0.0017559528350830078

# =====================================================================

# Rating limit, make the main task slow down.
from time import sleep

def sleep_decorator(function):

    '''
    Limits how fast the function is called
    '''

    def wrapper(*args, **kwargs):
        sleep(2)
        return function(*args, **kwargs)
    return wrapper

@sleep_decorator
def print_number(num):
    return num

#print(print_number(222))  # 222     waits 2 seconds

# =====================================================================



# =====================================================================


