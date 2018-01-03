# 10.9 Adding Directories to sys.path

import sys
from os.path import abspath, join, dirname

sys.path.insert(0, abspath(dirname('__file__'), 'src'))
