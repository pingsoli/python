# 2.12 Sanitizing and Cleaning Up Text

s = 'pýtĥöñ\fis\tawesome\r\n'

remap = {
    ord('\t'): ' ', 
    ord('\f'): ' ',
    ord('\r'): None  # Deleted
}

a = s.translate(remap)
#print(a)
# pýtĥöñ is awesome
# 

import unicodedata
import sys

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))

b = unicodedata.normalize('NFD', a)
print(b.translate(cmb_chrs))
# python is awesome
#


# The fastest approach is use str.replace()
def clean_spaces(s):
    s = s.replace('\r', '')    
    s = s.replace('\t', ' ')
    s = s.replace('\f', ' ')
    return s
