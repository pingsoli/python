# 8.22 Implementing the Visitor Pattern Without Recursion

import types

class Node:
    pass

class NodeVisitor:
    def visit(self, node):
        stack = [ node ]
        last_result = None
        while stack:
            try:
                last = stack[-1]
                if isinstance(last, types.GeneratorType):
                    stack.append(last.send(last_result))
                elif isinstance(last, node):
                    stack.append(self._visit(stack.pop()))
                else:
                    last_result = stack.pop()
            except StopIteration:
                stack.pop()
        return last_result
    
    def _visit(self, node):
        methmod_name = 'visit_' + type(node).__name__
        methmod = getattr(self, method_name, None)

        if method is None:
            method = self.generic_visit
        return method(node)

    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))

