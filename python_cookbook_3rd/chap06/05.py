# Turning a Dictionary into XML

from xml.etree.ElementTree import Element

def dict_to_xml(tag, d):
    '''
    Turn a simple dict of key/value pairs into XML
    '''
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem

s = {'name': 'GOOG', 'shares': 100, 'price': 490.0}
e = dict_to_xml('stock', s)
# print(e)
# <Element 'stock' at 0x7f9d82f88a48>

from xml.etree.ElementTree import tostring
#print(tostring(e))
# b'<stock><name>GOOG</name><shares>100</shares><price>490.0</price></stock>'

e.set('_id', '1234')
#print(tostring(e))
# b'<stock _id="1234"><name>GOOG</name><shares>100</shares><price>490.0</price></stock>'

def dict_to_xml_str(tag, d):
    '''
    Turn a simple dict of key/value pairs into XML
    '''
    parts = ['<{}>'.format(tag)]
    for key, val in d.items():
        parts.append('<{0}>{1}<{0}>'.format(key, val))
    parts.append('</{}>'.format(tag))
    return ''.join(parts)

d = {'name': '<spam>'}

#print(dict_to_xml_str('item', d))
# <item><name><spam><name></item>

from xml.sax.saxutils import escape, unescape

e = escape('<spam>')
print(e)
print(unescape(e))
# Output:
# &lt;spam&gt;
# <spam>
