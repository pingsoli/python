# 5.17 Writing Bytes to a Text File

import sys

#print(sys.stdout.write(b'hello\n'))
# Traceback (most recent call last):
#   File "17.py", line 5, in <module>
#     print(sys.stdout.write(b'hello\n'))
# TypeError: write() argument must be str, not bytes

#print(sys.stdout.buffer.write(b'hello\n'))
# hello
# 6
