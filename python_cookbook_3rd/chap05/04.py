# 5.4 Reading and Writing Binary Data

# rb, wb mode to read and write a binary file
# Read the entire file as a single byte string
#with open('somfile.bin', 'rb') as f:
#    data = f.read()

# Text string and byte string are different
# Text string
t = 'Hello world'
print(t[0])  # H

# Byte string
b = b'Hello world'
print(b[0])  # 72

# Decode and encode a byte string.
with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')

with open('somefile.bin', 'wb') as f:
    text = 'Hello world'
    f.write(text.encode('utf-8'))
