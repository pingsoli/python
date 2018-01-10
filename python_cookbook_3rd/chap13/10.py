# 13.10 Reading Configuration Files
'''
; config.ini
; Sample configuration file

[installation]
library=%(prefix)s/lib
include=%(prefix)s/include
bin=%(prefix)s/bin
prefix=/usr/local

# Setting related to debug configuration
[debug]
log_errors=true
show_warnings=False

[server]
port: 8080
nworkers: 32
pid-file=/tmp/spam.pid
root=/www/root
signature:
    =================================
    Brought to you by the Python Cookbook
    =================================
'''

from configparser import ConfigParser
cfg = ConfigParser()
cfg.read('config.ini')
# print(cfg.sections())
# print(cfg.get('installation', 'library'))
# print(cfg.getboolean('debug', 'log_errors'))
# print(cfg.getint('server', 'port'))
# print(cfg.getint('server', 'nworkers'))
# print(cfg.get('server', 'signature'))

# ['installation', 'debug', 'server']
# /usr/local/lib
# True
# 8080
# 32
# 
# =================================
# Brought to you by the Python Cookbook
# =================================

cfg.set('server', 'port', '9000')
cfg.set('debug', 'log_errors', 'False')
import sys
cfg.write(sys.stdout)
# [installation]
# library = %(prefix)s/lib
# include = %(prefix)s/include
# bin = %(prefix)s/bin
# prefix = /usr/local
# 
# [debug]
# log_errors = False
# show_warnings = False
# 
# [server]
# port = 9000
# nworkers = 32
# pid-file = /tmp/spam.pid
# root = /www/root
# signature = 
#   =================================
#   Brought to you by the Python Cookbook
#   =================================
