# 5.2 Printing to a File

# Redirect output to a file
# If file doesn't exist, make sure we have writing permission.
with open('test.txt', 'wt') as f:
    print('hello world!', file=f)

