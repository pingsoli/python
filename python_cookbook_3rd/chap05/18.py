# 5.18 Wrapping an Existing File Descriptor As a File Object

# Open a low-level file descriptor
import os
fd = os.open('somefile.txt', os.O_WRONLY | os.O_CREAT)

# Turn into a proper file
f = open(fd, 'wt')
f.write('hello world\n')
f.close()

# Create a file object, but don't close underlying fd when done.
#f = open(fd, 'wt', closefd=False)
