# 2.8 Writing a Regular Expression for Multiline Patterns

import re
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is
            multiline comment */
        '''

#print(comment.findall(text1))  # [' this is a comment ']
#print(comment.findall(text2))  # []

comment = re.compile(r'/\*((?:.|\n)*?)\*/')
# [' this is\n            multiline comment ']
#print(comment.findall(text2))

# Another approach
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
# [' this is\n            multiline comment ']
print(comment.findall(text2))

# re.DOTALL works fine here, but not be suitable for 
# complicated situation. We should define own regular 
# expression instead.
