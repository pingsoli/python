# 13.11 Adding Logging to Simple Scripts

import logging

def main():
    # Configure the logging system
#    logging.basicConfig(
#        filename='app.log',
#        level=logging.ERROR
#    )

    # If we want to change the format
    logging.basicConfig(
        filename='app.log',
        level=logging.WARNING,
        format='%(levelname)s:%(asctime)s:%(message)s'
    )

    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'

    # Example logging calls (insert into your program)
    logging.critical('Host %s unknow', hostname)
    logging.error("Counld't find %r", item)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode=%r', filename, mode)
    logging.debug('Got here')

if __name__ == '__main__':
    main()

# First test
# app.log
# CRITICAL:root:Host www.python.org unknow
# ERROR:root:Counld't find 'spam'

# Second test
# CRITICAL:2018-01-09 17:19:28,323:Host www.python.org unknow
# ERROR:2018-01-09 17:19:28,324:Counld't find 'spam'
# WARNING:2018-01-09 17:19:28,324:Feature is deprecated
