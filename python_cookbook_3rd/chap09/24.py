# 9.24 Parsing and Analyzing Python Source

# AST(Abstract Syntax Tree)
import ast
ex = ast.parse('2 + 3*4 + x', mode='eval')
#print(ex)
# <_ast.Expression object at 0x7feb70059160>
#print(ast.dump(ex))
# Expression(body=BinOp(left=BinOp(left=Num(n=2), op=Add(), right=BinOp(
# left=Num(n=3), op=Mult(), right=Num(n=4))), op=Add(),
# right=Name(id='x', ctx=Load())))

top = ast.parse('for i in range(10): print(i)', mode='exec')

# Not finish the whole example, check out from the book for more detail
