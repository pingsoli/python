# 10.8 Reading Datafiles Within a Package

'''
mypackage/
    __init__.py
    somedata.dat
    spam.py
'''

# If you want to read the contents of the file somedata.dat

import pkgutil
data = pkgutil.get_data(__package__, 'somedata.dat')
