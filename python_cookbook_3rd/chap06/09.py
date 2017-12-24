# 6.9 Decoding and Encoding Hexademical Digits

# byte string => hexadmical string or
# hexadmical string => byte string

s = b'hello'
import binascii

# Encode as hex
h = binascii.b2a_hex(s)
#print(h)
# b'68656c6c6f'

# Decode back to bytes
s_new = binascii.a2b_hex(h)
#print(s_new)
# b'hello'


# Base64 module
import base64
h = base64.b16encode(s)
print(h)
# b'68656C6C6F'

print(base64.b16decode(h))
# b'hello'
