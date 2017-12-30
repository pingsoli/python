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

def get_next(name):
    return 'lorem ipsum, {0} dolor sit meat'.format(name)

def p_decorate(func):
    def func_wrapper(name):
        return '<p>{0}</p>'.format(func(name))
    return func_wrapper

my_get_text = p_decorate(get_next)
#print(my_get_text('John'))
# <p>lorem ipsum, John dolor sit meat</p>

# =====================================================================

# Use Python Decorator
def p_decorate(func):
    def func_wrapper(name):
        return '<p>{0}</p>'.format(func(name))
    return func_wrapper

@p_decorate
def get_next(name):
    return 'lorem ipsum, {0} dolor sit meat'.format(name)

#print(get_next('pingsoli'))
# <p>lorem ipsum, pingsoli dolor sit meat</p>

# =====================================================================

# Next Example Using Multiple Decorator
def p_decorate(func):
    def func_wrapper(name):
        return '<p>{0}</p>'.format(func(name))
    return func_wrapper

def strong_decorate(func):
    def func_wrapper(name):
        return '<strong>{0}</strong>'.format(func(name))
    return func_wrapper

def div_decorate(func):
    def func_wrapper(name):
        return '<div>{0}</div>'.format(func(name))
    return func_wrapper

@div_decorate
@strong_decorate
@p_decorate
def get_next(name):
    return 'lorem ipsum, {0} dolor sit meat.'.format(name)

#print(get_next('pingsoli'))
# <div><strong><p>lorem ipsum, pingsoli dolor sit meat.</p></strong></div>

# =====================================================================

# Decorating Methods
def p_decorate(func):
    def func_wrapper(name):
        return '<p>{0}</p>'.format(func(name))
    return func_wrapper

class Person:
    def __init__(self):
        self.name = 'pingsoli'
        self.family = 'Lee'

    @p_decorate
    def get_fullname(self):
        return self.name + ' ' + self.family

my_person = Person()
#print(my_person.get_fullname())
# <p>pingsoli Lee</p>

# =====================================================================

# A much better approach 
def p_decorate(func):
    def func_wrapper(*args, **kwargs):
        return '<p>{0}</p>'.format(func(*args, **kwargs))
    return func_wrapper

class Person:
    def __init__(self):
        self.name = 'pingsoli'
        self.family = 'Lee'

    @p_decorate
    def get_fullname(self):
        return self.name + ' ' + self.family

my_person = Person()
#print(my_person.get_fullname())
# <p>pingsoli Lee</p>

# =====================================================================

# Passing arguments to decorators
def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return '<{0}>{1}</{0}>'.format(tag_name, func(name))
        return func_wrapper
    return tags_decorator

@tags('div')
@tags('strong')
@tags('p')
def get_next(name):
    return 'hello ' + name

print(get_next('pingsoli'))
# <div><strong><p>hello pingsoli</p></strong></div>

# =====================================================================
