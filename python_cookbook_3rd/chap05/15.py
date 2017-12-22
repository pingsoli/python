# 5.15 Printing Bad Filenames

# filename contains special character, 
# and throw a UnicodeEncodeError

def bad_filename(filename):
    return repr(filename)[1:-1]

filenames = ['pam.py', 'bäd.txt', 'foo.txt']
    
for name in filenames:
    print(bad_filename(name))

# I don't try the example.
