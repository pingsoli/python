# 10.2 Controlling the Import of Everything


# Define a variable __all__ in your module that explicitly list the
# exported names.

# somemodule.py

def spam():
    pass

def grok():
    pass

blah = 42
# Only export 'spam' and 'grok'
__all__ = ['spam', 'grok']
