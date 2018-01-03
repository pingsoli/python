# 10.1 Making a Hierarchical Package of Modules

# graphics/
#     __init__.py
#     primitive/
#         __init__.py
#         line.py
#         fill.py
#         text.py
#     formats/
#         __init__.py
#         png.py
#         jpg.py

# import graphics.primitive.line
# from graphics.primitive import line
# import graphics.formats.jpg as jpg

# The purpose of the __init__.py files is to include optional
# initialization code that runs as different levels of a
# package are encountered.

# an __init__.py file can be used to automatically load submoudles like
# from . import jpg
# from . import png
