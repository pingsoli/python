# 4.1 Mannually Consuming an Iterator

# next() function
#with open('/etc/passwd') as f:
#    try:
#        while True:
#            line = next(f)
#            print(line, end='')
#    except StopIteration:
#        pass

# Normally, StopIteration is used to signal the end 
# of iteration.

items = [1, 2, 3]
it = iter(items)
#print(next(it))  # 1
#print(next(it))  # 2
#print(next(it))  # 3
#print(next(it))  # Throw StopIteration
# Traceback (most recent call last):
#   File "01.py", line 20, in <module>
#     print(next(it))
# StopIteration
