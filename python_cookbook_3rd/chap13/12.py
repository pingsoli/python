# 13.12 Adding Logging to Libraries

# 12.py

import logging
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

def func():
    log.critical('A Critical Error!')
    log.debug('A debug message')

