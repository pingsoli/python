# 5.13 Getting a Directory Listing

import os
dirs = os.listdir('.')
#print(dirs)
# ['04.py', '06.py', '11.py', '12.py', '03.py', '01.py', '07.py', 
#  '05.py', '09.py', '02.py', 'data', '08.py', '.13.py.swp', '10.py', '13.py']

# Get all regular files
names = [name for name in os.listdir('..')
         if os.path.isfile(os.path.join('..', name))]

# Get all dirs
dirnames = [name for name in os.listdir('..')
            if os.path.isdir(os.path.join('..', name))]

#print(names)
#print(dirnames)
# ['readme.md', 'toc.sh']
# ['chap03', 'chap04', 'chap01', 'chap02', 'chap05']
