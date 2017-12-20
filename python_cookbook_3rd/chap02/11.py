# 2.11 Stripping Unwanted Characters from Strings


# Whitespace stripping
s = '     hello world  \n'
#print(s.strip())  # 'hello world'

# Character stripping
t = '-------hello========'
print(t.lstrip('-'))
# hello========
print(t.rstrip('='))
# -------hello
