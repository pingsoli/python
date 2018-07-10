thistuple = ("apple", "banana", "cherry")
print(thistuple) # ('apple', 'banana', 'cherry')
print(thistuple[1]) # banana

#  thistuple[1] = "blackcurrant" # got error
#  print(thistuple)
#  Traceback (most recent call last):
#    File "tuple.py", line 5, in <module>
#      thistuple[1] = "blackcurrant"
#  TypeError: 'tuple' object does not support item assignment

# how to change values in tuple ?
# Actually, we cannot change the values of tuple.
# but we can construct a list from the tuple, and change the values from list
# at last, construct a new tuple and assign to the original tuple varialbe.
lst = list(thistuple)
lst[0] = "hello"
thistuple = tuple(lst)
print(thistuple) # ('hello', 'banana', 'cherry')
