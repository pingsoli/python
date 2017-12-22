# 5.5 Writing to a File That Doesn't Already Exist

# Use x mode to open() instead of the usual w mode.
# x mode: if file not exists, will create the file.
# but, if the file exits, we will get an exception.
#
# w mode: if file not exists, open() create the file.
# if exists, do nothing.

#with open('somefile', 'wt') as f:
#    f.write('Hello\n')

with open('somefile', 'xt') as f:
    f.write('Hello\n')
# Traceback (most recent call last):
#   File "05.py", line 7, in <module>
#     with open('somefile', 'xt') as f:
# FileExistsError: [Errno 17] File exists: 'somefile'
