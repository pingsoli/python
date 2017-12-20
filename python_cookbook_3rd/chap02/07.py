# 2.7 Specifying a Regular Expression for the Shortest Match

import re
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer say "no."'
#print(str_pat.findall(text1))
# ['no.']

text2 = 'Computer say "no." Phone says "yes."'
print(str_pat.findall(text2))
# ['no." Phone says "yes.']

# Why did this happend ? Regular expression is greedy.
# How to fix it ?
str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text2))
# ['no.', 'yes.']
