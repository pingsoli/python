# 9.25 Disassembling Python Byte Code

def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
    print('end')

import dis
dis.dis(countdown)
#   4           0 SETUP_LOOP              30 (to 32)
#         >>    2 LOAD_FAST                0 (n)
#               4 LOAD_CONST               1 (0)
#               6 COMPARE_OP               4 (>)
#               8 POP_JUMP_IF_FALSE       30
# 
#   5          10 LOAD_GLOBAL              0 (print)
#              12 LOAD_CONST               2 ('T-minus')
#              14 LOAD_FAST                0 (n)
#              16 CALL_FUNCTION            2
#              18 POP_TOP
# 
#   6          20 LOAD_FAST                0 (n)
#              22 LOAD_CONST               3 (1)
#              24 INPLACE_SUBTRACT
#              26 STORE_FAST               0 (n)
#              28 JUMP_ABSOLUTE            2
#         >>   30 POP_BLOCK
# 
#   7     >>   32 LOAD_GLOBAL              0 (print)
#              34 LOAD_CONST               4 ('end')
#              36 CALL_FUNCTION            1
#              38 POP_TOP
#              40 LOAD_CONST               0 (None)
#              42 RETURN_VALUE
