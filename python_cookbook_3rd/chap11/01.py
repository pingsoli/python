# 11.1 Interacting with HTTP Services As a Client

# Using urllib.request module for simple HTTP server
from urllib import request, parse

# Base URL being accessed
url = 'http://httpbin.org/get'

# Dictionary of query parameters (if any)
parms = {
    'name1' : 'value1',
    'name1' : 'value1'
}

# Encode the query string
querystring = parse.urlencode(parms)

# Make a GET request and read the response
#u = request.urlopen(url+'?' + querystring)
#resp = u.read()
#print(resp)
# b'{\n  "args": {\n    
#             "name1": "value1"\n  
#        }, \n
#        "headers": {\n
#             "Accept-Encoding": "identity", \n
#             "Connection": "close", \n
#             "Host": "httpbin.org", \n
#             "User-Agent": "Python-urllib/3.6"\n
#        }, \n
#        "origin": "120.239.67.82", \n
#        "url": "http://httpbin.org/get?name1=value1"\n
# }\n'

# Providing custome HTTP header
# from urllib import request, parse
#
# # Extra headers
# headers = {
#     'User-Agent': 'none/ofyourbusiness',
#     'Spam': 'Eggs'
# }
# 
# req = request.Request(url, querystring.encode('ascii'), headers=headers)
# 
# # Make a request and read the response
# u = request.urlopen(req)
# resp = u.read()

import requests  # need installed by yourself

# Base URL being accessed
url = 'http://httpbin.org/post'

# Dictionary of query parameters (if any)
parms = {
    'name1' : 'value1',
    'name2' : 'value2'
}

# Extra headers
headers = {
    'User-agent': 'none/ofyourbusiness',
    'Spam': 'Eggs'
}

resp = requests.post(url, data=parms, headers=headers)

# Encode text returned by the request
text = resp.text
#print(text)
# {
#   "args": {}, 
#   "data": "", 
#   "files": {}, 
#   "form": {
#     "name1": "value1", 
#     "name2": "value2"
#   }, 
#   "headers": {
#     "Accept": "*/*", 
#     "Accept-Encoding": "gzip, deflate", 
#     "Connection": "close", 
#     "Content-Length": "25", 
#     "Content-Type": "application/x-www-form-urlencoded", 
#     "Host": "httpbin.org", 
#     "Spam": "Eggs", 
#     "User-Agent": "none/ofyourbusiness"
#   }, 
#   "json": null, 
#   "origin": "120.236.165.12", 
#   "url": "http://httpbin.org/post"
# }

# Extract a few fields in header data
import requests

#resp = requests.head('http://www.python.org/index.html')

#status = resp.status_code
#last_modified = resp.headers['last-modified']
#content_type = resp.headers['Content-Type']
#content_length = resp.headers['Content-Length']

#print(status)  # 301


# Basic authentication
import requests

#resp = requests.get('http://pypi.python.org/pypi?:action=login', 
#                    auth=('user', 'password'))


# HTTP Cookie
import requests

# First request
#resp1 = requests.get(url)
#...
# Second request with cookies received on first requests
#resp2 = requests.get(url, cookies=resp1.cookies)


# Uploading content
# import request
# url = 'http://httpbin.org/post'
# files = ( 'file': ('data.csv', open('data.csv', 'rb')))
# 
# r = requests.post(url, files=files)

import urllib.request

auth = urllib.request.HTTPBasicAuthHandler()
auth.add_password('pypi', 'http://www.python.org', 'username', 'password')
opener = urllib.request.build_opener(auth)

r = urllib.request.Request('http://pypi.python.org/pypi?:action=login')
u = opener.open()
resp = u.read()

# From here, you can access more pages using opener
# ...

import requests
r = requests.get('http://httpbin.org/get?name=Dave&n=37',
            headers = { 'User-Agent': 'goaway/1.0'} )
resp = r.json
# print(resp['headers'])
# print(resp['args'])
