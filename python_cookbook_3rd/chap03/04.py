# 3.4 Working with Binary, Octal, and Hexadecimal

x = 1234
#print(bin(x))  # 0b10011010010
#print(oct(x))  # 0o2322
#print(hex(x))  # 0x4d2

# Alternatively, you can use format()
#print(format(x, 'b'))  # 10011010010
#print(format(x, 'o'))  # 2322
#print(format(x, 'x'))  # 4d2

#print(int('4d2', 16))  # 1234
#print(int('10011010010', 2))  # 1234

import os
os.chmod('toc.sh', 0o700)
