# basics.py contains all examples about python 3.x syntax.

# print function is really helpful. output variable value to screen.
# print "hello world" # Python 2.x version 
# print("hello world") # Python 3.x version


# Basic data type
# int, float, string
int_val = 1
float_val = 7.0
my_float = float(7)
# sigle quote and double quotes is equal, can use them simultaneously
my_string = 'hello world'
my_string = "hello world"
my_string = "I'm pingosli"


# Simple operators on numbers and strings
one = 1
two = 2
three = one + two
#print(three)
hello = "hello"
world = "world"
hello_world = hello + " " + world
#print(hello_world)


# Assign simultaneously
a, b = 3, 4
#print(a, b) # output: 3 4


# Exercise 
mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Int: %d" % myint)
