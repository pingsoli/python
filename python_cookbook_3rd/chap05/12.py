# 5.12 Testing for the Existence of a File

import os
#print(os.path.exists('/etc/passwd'))  # True

# Is a regular file
#print(os.path.isfile('/etc/passwd'))  # True

# Is a directory
#print(os.path.isdir('/etc/passwd'))  # False

# Is a symbolic link
#print(os.path.islink('/usr/bin/python'))  # True

# Get the file linked to 
#print(os.path.realpath('/usr/bin/python'))  # /usr/local/python-3.6.3/bin/python3.6

#print(os.path.getsize('/etc/passwd'))  # 2354
#print(os.path.getmtime('/etc/passwd'))  # 1511954300.1717298

import time
print(time.ctime(os.path.getmtime('/etc/passwd')))
# Wed Nov 29 19:18:20 2017
