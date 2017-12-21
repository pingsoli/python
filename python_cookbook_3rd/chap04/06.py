# 4.6 Defining Generator Functions with Extra State


from collections import deque

class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)
    
    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()

with open('02.py') as f:
    lines = linehistory(f)
    for line in lines:
        if 'self' in line:
            print(line, end='')
            #for lineno, hline in lines.history:
            #    print('{}:{}'.format(lineno, hline), end='')

# Defining __iter__() by yourself.
#    def __init__(self, value):
#        self._value = value
#        self._children = []
#    def __repr__(self):
#        return 'Node({!r})'.format(self._value)
#    def add_child(self, node):
#        self._children.append(node)
#    def __iter__(self):
#        return iter(self._children)
