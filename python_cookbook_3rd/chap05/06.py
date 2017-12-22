# 5.6 Performing I/O Operations on a String

# io.StringIO() and io.BytesIO() classes to create 
# file-like objects that operate on string data.

import io
s = io.StringIO()
s.write('hello world\n')
print('this is a test', file=s)
