# 2.2 Matching Text at the Start or End of a String

# usage: filename extensions, URL schemes and so on.
# str.startswith() and str.endswith()

filename = 'sample.txt'
#print(filename.endswith('.txt'))  # True
url = 'http://www.python.org'
#print(url.startswith('http:'))    # True

# Check multiple choice
import os

filenames = os.listdir('.')
filter_filenames = [name for name in filenames if name.endswith(('.c', '.h'))]
contains_py = any(name.endswith('.py') for name in filenames)

#print(filter_filenames)  # []
#print(contains_py)       # True


choices = ['http:', 'ftp:']
url = 'http://www.python.org'
# url.startswith(choices)
# Error Message:
# Traceback (most recent call last):
#   File "02.py", line 24, in <module>
#     url.startswith(choices)
# TypeError: startswith first arg must be str or a tuple of str, not list

# Correct way uses tuple to wrap up.
#print(url.startswith(tuple(choices)))  # True


# The behind code can achieve this too, but the former is more elegant.
filename = 'sample.txt'
#print(filename[-4:] == '.txt')  # True

url = 'https://www.google.com'
#print(url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:')  # True
