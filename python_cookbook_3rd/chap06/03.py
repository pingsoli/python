# 6.3 Parsing Simple XML Data

from urllib.request import urlopen
from xml.etree.ElementTree import parse

# Download the RSS feed and parse it
u = urlopen('http://planet.python.org/rss20.xml')
doc = parse(u)

# Extract and output tags of interest
for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')

    print(title)
    print(date)
    print(link)
# Output:
# Peter Bengtsson: Fastest way to uniquify a list in Python &gt;=3.6
# Sat, 23 Dec 2017 01:23:26 +0000
# https://www.peterbe.com/plog/fastest-way-to-uniquify-a-list-in-python-3.6
# Davy Wybiral: Google Voice + Project Fi???
# Fri, 22 Dec 2017 17:58:40 +0000
# http://davywybiral.blogspot.com/2017/12/google-voice-project-fi.html
# Programiz: Python Matrix
# Fri, 22 Dec 2017 08:19:24 +0000
# https://www.programiz.com/python-programming/matrix
# pgcli: Release v1.8.2
# Fri, 22 Dec 2017 08:00:00 +0000
# http://pgcli.com/v1.8.2.html
# Mycli: Release v1.14.0
# Fri, 22 Dec 2017 08:00:00 +0000
# http://mycli.net/v1.14.0.html
# Programiz: Python Arrays
# Fri, 22 Dec 2017 07:56:40 +0000
# https://www.programiz.com/python-programming/array
# Programiz: Python List Comprehension
# Fri, 22 Dec 2017 07:35:23 +0000
# ....
