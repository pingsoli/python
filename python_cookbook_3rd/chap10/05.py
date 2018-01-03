# 10.5 Making Separate Directories of Code Import Under a Common Namespace

# Omit __init__.py

'''
foo-package/
    spam/
        blah.py

bar-package/
    spam/
        grok.py
'''

import sys
sys.path.extentd(['foo-package', 'bar-package'])
import spam.blah
import spam.grok
