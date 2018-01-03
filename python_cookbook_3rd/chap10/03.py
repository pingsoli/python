# 10.3 Importing Package Submodules Using Relative Names

# mypackage.py
#     __init__.py
#     A/
#         __init__.py
#         spam.py
#         grok.py
#     B/
#         __init__.py
#         bar.py

# If the module mypackage.A.spam wants to import the module grok located
# in the same directory, it should include an import statement like this
# mypackage/A/spam.py
# from .import grok

# If the same module wants to import the module B.bar located in a 
# different directory, it can use an import statement like this:
# mypackage/A/spam.py
# from ..B import bar


# mypackage/A/spam.py

# from mypackage.A import grok  # OK
# from . import grok            # OK
# import grok                   # Error (not found)
