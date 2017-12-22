# 5.10 memory Mapping Binary Files

# Using mmap to map files into memory can be an efficient and 
# elegant means for randomly accessing the contents of a file.

import os
import mmap

def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)

# Write some data for testing
size = 100000
with open('data', 'wb') as f:
    f.seek(size-1)
    f.write(b'\x00')

m = memory_map('data')
print(len(m))  # 100000

print(m[0:11])  # b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

# Reassign a slice
m[0:11] = b'Hello world'
m.close()

# Verify changes
with open('data', 'rb') as f:
    print(f.read(11))
# b'Hello world'
