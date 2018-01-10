# 13.6 Executing an External Command and Getting Its Output

import subprocess
out_bytes = subprocess.check_output(['ls', '-a'])
out_text = out_bytes.decode('utf-8')

#print(out_text)
# .
# ..
# 01.py
# 02.py
# 03.py
# 04.py
# 05.py
# 06.py
# .06.py.swp

# Example of catching errors and getting the output created along with
# exit code.

# try:
#     out_bytes = subprocess.check_output(['cmd', 'arg1', 'arg2'])
# except subprocess.CalledProcessError as e:
#     out_bytes = e.output
#     code      = e.returncode

#out_bytes = subprocess.check_output('grep python | wc > out', shell=True)

# use subprocess.check_output is the easiest way to call external command.
# But we can use subprocess.Popen for high performance.

text = b'''
hello world
this is test
goodbye
'''

# Launch a command with pipes
p = subprocess.Popen(['wc'],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE)

# Send the data and get the output
stdout, stderr = p.communicate(text)

# To interpret as text, decode
out = stdout.decode('utf-8')
#err = stderr.decode('utf-8')
print(out)
#      4       6      34
