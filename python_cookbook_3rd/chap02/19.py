# 2.19 Writing a Simple Recursive Descent Parser

import re
import collections

# Token specification
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>-)'
TIMES = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([ NUM, PLUS, MINUS, TIMES, 
                                DIVIDE, LPAREN, RPAREN, WS])) 

# Tokenizer 
Token = collections.namedtuple('Token', ['type', 'value'])

def generate_tokens(text):
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match, None):
        tok = Token(m.lastgroup, m.group())
        if tok.type != 'WS':
            yield tok

# Parser
class ExpressionEvaluator:
    def parse(self, text):
        self.tokens = generate_tokens(text)
        self.tok = None         # Last symbol consumed
        self.nexttok = None     # Next symbol tokenized
        self._advance()         # Load first lookahead token  
        return self.expr()
    
    def _advance(self):
        self.tok, self.nexttok = self.nexttok, next(self.tokens, None)

    def _accept(self, toktype):
        if self.nexttok and self.nexttok.type == toktype:
            self._advance()
            return True
        else:
            return False
    
    def _except(self, toktype):
        'Comsume next token if it matches toktype or raise SyntaxError'
        if not self._accpet(toktype):
            raise SyntaxError('Excepted ' + toktype)

    def expr(self):
        "expression ::= term { ('+'|'-') term} *"
        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval += right
            elif op == 'MINUS':
                exprval -= right
        return exprval

    def term(self):
        "term ::= factor {('*'|'/') factor }*"

        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == 'TIMES':
                termval *= right 
            elif op == 'DIVIDE':
                termval /= right
        return termval

    def factor(self):
        "factor ::= NUM | (expr)"

        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._accept('RPAREN')
            return exprval
        else:
            raise SyntaxError('Excepted NUMBER or LPAREN')

e = ExpressionEvaluator()
#print(e.parse('2'))      # 2
#print(e.parse('2 + 3'))  # 5
#print(e.parse('2 + 3 * 4'))  # 14
#print(e.parse('2 + (3 + 4) * 5'))  # 37

print(e.parse('2 + (3 + * 4'))
# Traceback (most recent call last):
#   File "19.py", line 96, in <module>
#     print(e.parse('2 + (3 + * 4)'))
#   File "19.py", line 36, in parse
#     return self.expr()
#   File "19.py", line 58, in expr
#     right = self.term()
#   File "19.py", line 68, in term
#     termval = self.factor()
#   File "19.py", line 84, in factor
#     exprval = self.expr()
#   File "19.py", line 58, in expr
#     right = self.term()
#   File "19.py", line 68, in term
#     termval = self.factor()
#   File "19.py", line 88, in factor
#     raise SyntaxError('Excepted NUMBER or LPAREN')
# SyntaxError: Excepted NUMBER or LPAREN
