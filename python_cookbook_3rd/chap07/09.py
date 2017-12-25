# 7.9 Replacing Single Method Classes with Functions

# Closure

from urllib.request import urlopen

# class UrlTemplate:
#     def __init__(self, template):
#         self.template = template
# 
#     def open(self, **kwargs):
#         return urlopen(self.template.format_map(kwargs))
# 
# yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&fs={fields}')
# for line in yahoo.open(names='IBM,AAPL,FB', fields='sl1c1v'):
#     print(line.decode('utf-8'))


# Simpler function with closure in Python.
def UrlTemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))
    return opener

yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&fs={fields}')
for line in yahoo(names='IBM,AAPL,FB', fields='sl1c1v'):
    print(line.decode('utf-8'))
