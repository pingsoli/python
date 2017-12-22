# 5.1 Reading and Writing Text Date

# Use open() function with mode rt to read a text file.

# Read the entire file as a single string
#with open('01.py', 'rt') as f:
#    data = f.read()

# Iterate over the lines of the file
#with open('01.py', 'rt') as f:
#    for line in f:
#        # Process line
#        # ....

# Write use 'wt' mode

# By default, files are read/written using the default text encoding.
# as can be found in sys.getdefaultencoding().
#with open('01.py', 'rt', encoding='latin-1') as f:
#    # Process file


# When control leaves the with block, the file will be closed automatically.
# If we don't use with, make sure close the file.
#f = open('01.py', 'rt')
#data = f.read()
#f.close()

# Supply the newline='' arguments to open()
# Windows use '\r\n' as a newline, but unix-like 
# os use '\r'. We can use newline to specify it.
with open('01.py', 'rt', newline='') as f:
    print(f.read())

# NOTE: check encoding of every file is complicated.
# We should keep a uniform encoding(such as UTF-8).
