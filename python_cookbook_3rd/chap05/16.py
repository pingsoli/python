# 5.16 Adding or Changing the Encoding of an Already Open File

import urllib.request
import io

u = urllib.request.urlopen('http://www.baidu.com')
f = io.TextIOWrapper(u, encoding='utf-8')
text = f.read()
#print(text)

import sys
#print(sys.stdout.encoding)  # UTF-8

# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
# print(sys.stdout.encoding) # latin-1
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
print(sys.stdout.encoding) # utf-8
