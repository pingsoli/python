# 7.1 Writing Functions That Accept Any Number of Arguments

def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))

# Sample use 
# print(avg(3, 4))  # 3.5
# print(avg(1, 2, 3, 4))  # 2.5

import html

def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}'.format(
                 name = name, 
                 attrs = attr_str,
                 value = html.escape(value))
    return element

# Create '<item size="large" quantity="6">Albatross</item>'
#e = make_element('item', 'Albatross', size='large', quantity=6)
#print(e)
# <item size="large" quantity="6">Albatross</item

#print(make_element('p', '<spam>'))
# <p>&lt;spam&gt;</p

# Use * and ** both
def anyargs(*args, **kwargs):
    print(args)  # A tuple
    print(kwargs)  # A dict
