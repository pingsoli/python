# 13.2 Terminating a Program With an Error Message

import sys
sys.stderr.write('It failed\n')
raise SystemExit(100)

# python 02.py
# It failed
# echo $?
# 100
