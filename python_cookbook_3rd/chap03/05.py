# 3.5 Packing and Unpacking Large Integers from Bytes

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
#print(len(data))  # 16
#print(int.from_bytes(data, 'little'))  # 69120565665751139577663547927094891008
#print(int.from_bytes(data, 'big'))  # 94522842520747284487117727783387188

x = 94522842520747284487117727783387188
#print(x.to_bytes(16, 'big'))  # b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
#print(x.to_bytes(16, 'little'))  # b'4\x00#\x00\x01\xef\xcd\x00\xab\x90x\x00V4\x12\x00'

# Bit endian and little endian.
x = 0x01020304
#print(x.to_bytes(4, 'big'))  # b'\x01\x02\x03\x04'
#print(x.to_bytes(4, 'little'))  # b'\x04\x03\x02\x01'

x = 523 ** 23
#print(x)  # 335381300113661875107536852714019056160355655333978849017944067
#print(x.bit_length())  # 208

nbytes, rem = divmod(x.bit_length(), 8)
if rem:
    nbytes += 1

print(x.to_bytes(nbytes, 'little'))
# b'\x03X\xf1\x82iT\x96\xac\xc7c\x16\xf3\xb9\xcf\x18\xee\xec\x91\xd1\x98\xa2\xc8\xd9R\xb5\xd0'
