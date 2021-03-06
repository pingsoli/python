# Python Closure Tutorial

# Nested function & Non-Local Variable

# def print_msg(msg):
# # This is the outer enclosing function
#     
#     def printer():
#     # This is the nested function
#         print(msg)
# 
#     printer()
# 
# print_msg('hello')  # hello

#def print_msg(msg):
#
#    def printer():
#        print(msg)
#    
#    return printer
#
#another = print_msg('Hello')
#del print_msg
#another()  # Hello
#print_msg('hello')
# Traceback (most recent call last):
#   File "closure.py", line 27, in <module>
#     print_msg('hello')
# NameError: name 'print_msg' is not defined


# How to create a closure?
# 1) We must have a nested function(function inside a function)
# 2) The nested function must refer to a value defined in the enclosing function
# 3) The enclosing function must return the nested function

# When to use closure?
# Avoid the use of global values and provides some form of data hiding.
# Closure can provide an alternative and more elegant solution.

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

# Multiplier
times3 = make_multiplier_of(3)
#print(times3(9))  # 27
#print(times3(10))  # 30

times5 = make_multiplier_of(5)
#print(times5(5))  # 25

#print(times3.__closure__)
# (<cell at 0x7f891181a8e8: int object at 0x921ba0>,)

# The cell object has the attribute cell_contents which stores the closed value.
#print(times3.__closure__[0].cell_contents)  # 3
#print(times5.__closure__[0].cell_contents)  # 5


# Define a function
def foo(x):
    # inner function 'bar'
    def bar(y):
        q = 100
        # inner function 'baz'
        def baz(z):
            print("Locals: ", locals())
            print("Vars: ", vars())
            return x + y + q + z
        return baz
    return bar

f = foo(10)(20)
# Locals:  {'z': 30, 'y': 20, 'x': 10, 'q': 100}
# Vars:  {'z': 30, 'y': 20, 'x': 10, 'q': 100}
#print(f(30))  # 160
#for closure in f.__closure__:
#    print(closure.cell_contents)
# 100
# 10
# 20


# The following examples are not closure
# def f1(x):
#     def f2():
#         pass
#     return f2
# 
# f = f1(10)
# print(f.__closure__)  # None

#def f1(x):
#    def f2(x=x):
#        print(x)
#    return f2
#
#f = f1(10)
#print(f.__closure__)  # None
