# 10.10 Importing   Modules Using a Name Given in a String

import importlib

math = importlib.import_module('math')
#print(math.sin(2))  # 0.9092974268256817

mod = importlib.import_module('urllib.request')
u = mod.urlopen('https://www.python.org')
