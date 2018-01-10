# 13.1 Accepting Script Input via Redirection, Pipes, or Input Files

# ls | ./filein.py           # Print a directory listing to stdout
# ./filein.py /etc/passwd    # Reads /etc/passwd to stdout
# ./filein.py < /etc/passwd  # Reads /etc/passwd to stdout 

import fileinput

# with fileinput.input() as f_input:
#     for line in f_input:
#         print(line, end='')

with fileinput.input('/etc/passwd') as f:
    for line in f:
        print(f.filename(), f.lineno(), line, end='')
# /etc/passwd 1 root:x:0:0:root:/root:/bin/bash
# /etc/passwd 2 daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
# /etc/passwd 3 bin:x:2:2:bin:/bin:/usr/sbin/nologin
# /etc/passwd 4 sys:x:3:3:sys:/dev:/usr/sbin/nologin
# ...
# /etc/passwd 42 mysql:x:122:129:MySQL Server,,,:/nonexistent:/bin/false
