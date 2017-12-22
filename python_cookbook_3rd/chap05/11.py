# 5.11 Manipulating Pathnames

import os
path = '/usr/local/python-3.6.6/bin/python3.6'

# Get the last component of the path
#print(os.path.basename(path))  # python3.6

# Get the directory name
#print(os.path.dirname(path))  # /usr/local/python-3.6.6/bin

# Join path components together
#print(os.path.join('tmp', 'data', os.path.basename(path)))  # tmp/data/python3.6

# Expand the user's home directory
path = '~/Data/data.csv'
#print(os.path.expanduser(path))  # /home/pingsoli/Data/data.csv

# Split the file extension
print(os.path.splitext(path))  # ('~/Data/data', '.csv')
