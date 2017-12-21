# 2.20 Performing Text Operations on Byte Strings

data = b'Hello world'
#print(data[0:5])  # b'Hello'
#print(data.startswith(b'Hello'))  # True
#print(data.split())  # [b'Hello', b'world']
#print(data.replace(b'Hello', b'Hello pingsoli'))  # b'Hello pingsoli world'

# byte arrays also work the same operation.
data = bytearray(b'Hello World')
#print(data[0:5])  # bytearray(b'Hello')
#print(data.startswith(b'Hello'))  # True
#print(data.split())  # [bytearray(b'Hello'), bytearray(b'World')]
#print(data.replace(b'Hello', b'Hello pingsoli'))  # bytearray(b'Hello pingsoli World')

data = b'FOO:BAR,SPAM'
import re

# Wrong usage
#print(re.split('[:,]', data))
# Traceback (most recent call last):
#   File "20.py", line 19, in <module>
#     print(re.split('[:,]', data))
#   File "/usr/local/python-3.6.3/lib/python3.6/re.py", line 212, in split
#     return _compile(pattern, flags).split(string, maxsplit)
# TypeError: cannot use a string pattern on a bytes-like object

# Notice: pattern as bytes
#print(re.split(b'[:,]', data))  # [b'FOO', b'BAR', b'SPAM']


# Text string and Byte string
a = 'Hello world'  # Text string
#print(a[0], a[1]) # H e
b = b'Hello world' # Byte string
#print(b[0], b[1])  # 72 101

# Difference with text string and byte string
# byte string don't provide a nice string representation.
s = b'Hello world'
#print(s)  # b'Hello world'
#print(s.decode('ascii'))  # Hello world

# formatting
#print('{:10s} {:10d} {:10.2f}'.format('ACME', 100, 488.0).encode('ascii'))
# b'ACME              100     488.00'


# Write a UTF-8 filename
with open('jalape\xf1o.txt', 'w') as f:
    f.write('spicy')

# Get a directory listing 
import os
#print(os.listdir('.'))  # Text string (names are decoded) 
# ['jalapeño.txt'] 

print(os.listdir(b'.')) # Byte string (names left as bytes)
# [b'jalape\xc3\xb1o.txt']
