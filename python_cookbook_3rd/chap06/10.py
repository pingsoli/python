# 6.10 Decoding and Encoding Base64

# Some byte string
s = b'hello'

import base64

# Encode as base64
a = base64.b64encode(s)
#print(a)
# b'aGVsbG8='

# Decode from base64
#print(base64.b64decode(a))
# b'hello'

# NOTE: Base64 encoding is only meant to be used on byte-oriented data
# such as byte strings and byte arrays.
# When decode base64, both byte strings and Unicode text strings can be
# supplied. However, Unicode strings can only contain ASCII characters.

a = base64.b64encode(s).decode('ascii')
#print(a)
# aGVsbG8=
