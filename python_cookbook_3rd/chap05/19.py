# 5.19 Making Temporary Files and Directories

from tempfile import TemporaryFile

with TemporaryFile('w+t') as f:
    # Read/write to the file
    f.write('hello world\n')
    f.write('Tesing\n')

    # Seek back to beginning and read the data
    f.seek(0)
    data = f.read()
#    print(data)
# Temporary file is destoryed.


# f = TemporaryFile('w+t')
# 
# ... 
# f.close()

# NamedTemporaryFile

from tempfile import NamedTemporaryFile

with NamedTemporaryFile('w+t') as f:
    print('filename is: ', f.name)
# filename is:  /tmp/tmpv26v5nxy
