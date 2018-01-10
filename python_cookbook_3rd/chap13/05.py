# 13.5 Getting the Terminal Size

import os
sz = os.get_terminal_size()

print(sz)
print(sz.columns)
print(sz.lines)

# os.terminal_size(columns=169, lines=39)
# 169
# 39

# There are many approaches for obtaining the terminal size.
# They executes low-level system calls involving ioctl()
# and TTYs
