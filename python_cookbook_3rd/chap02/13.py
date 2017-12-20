# 2.13 Aligning Text Strings

text = 'Hello World'
#print(text.ljust(20))  # 'Hello World        ' 
#print(text.rjust(20))  # '        Hello World'
#print(text.center(20)) # '    Hello World    '

#print(text.rjust(20, '='))  # =========Hello World
#print(text.ljust(20, '*'))  # Hello World*********

# Easiest way to align, and it's more powerful.
print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))
# '         Hello World'
# 'Hello World         '
# '    Hello World     '
