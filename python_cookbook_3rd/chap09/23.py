# 9.23 Executing Codes with Local Side Effects

# a = 13
# exec('b = a + 1')
#print(b)  # 14

def test():
    a = 13
    exec('b = a + 1')
    print(b)

#test()
# Traceback (most recent call last):
#   File "23.py", line 12, in <module>
#     test()
#   File "23.py", line 10, in test
#     print(b)
# NameError: name 'b' is not defined

# locals() function can obtain a dictionary of the local variable prior
# to call to exec()

def test():
    a = 13
    loc = locals()
    exec('b = a + 1')
    b = loc['b']
    print(b)

#test()  # 14

# Take care of the locals() funciton.
# each time to call it, locals() will take the current value of local
# varialbes and overwrite the corresponding entries in the dictionary.

def test3():
    x = 0
    loc = locals()
    print(loc)
    exec('x += 1')
    print(loc)
    locals()
    print(loc)

#test3()
# {'x': 0}
# {'x': 1, 'loc': {...}}
# {'x': 0, 'loc': {...}}

def test4():
    a = 13
    loc = {'a': a}
    glb = {}
    exec('b = a + 1', glb, loc)
    b = loc['b']
    print(b)

#test4()  # 14
