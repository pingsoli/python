# 2.16 Reforming Text to a Fixed Number of Columns

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

import textwrap
#print(textwrap.fill(s, 70))
# Look into my eyes, look into my eyes, the eyes, the eyes, the eyes,
# not around the eyes, don't look around the eyes, look into my eyes,
# you're under.

#print(textwrap.fill(s, 40))
# Look into my eyes, look into my eyes,
# the eyes, the eyes, the eyes, not around
# the eyes, don't look around the eyes,
# look into my eyes, you're under.

#print(textwrap.fill(s, 40, initial_indent='    '))
#     Look into my eyes, look into my
# eyes, the eyes, the eyes, the eyes, not
# around the eyes, don't look around the
# eyes, look into my eyes, you're under.

#print(textwrap.fill(s, 40, subsequent_indent='      '))
# Look into my eyes, look into my eyes,
#       the eyes, the eyes, the eyes, not
#       around the eyes, don't look around
#       the eyes, look into my eyes,
#       you're under.


# Get terminal size
# class os.terminal_size is tuple (columns, lines)
import os
import shutil
# os.get_terminal_size() is low-level implementation.
#print(os.get_terminal_size())
# Traceback (most recent call last):
#   File "16.py", line 35, in <module>
#     print(os.get_terminal_size().columns)
# OSError: [Errno 25] Inappropriate ioctl for device

# shutil.get_terminal_size() is high-level funciton.
print(shutil.get_terminal_size().columns)  # 80
print(shutil.get_terminal_size())  # os.terminal_size(columns=80, lines=24)
