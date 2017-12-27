# 8.18 Extending Classes with Mixins

class LoggedMappingMixin:
    '''
    Add logging to get/set/delete operations for debugging.
    '''
    __slotr__ = ()

    def __getitem__(self, key):
        print('Gettring ' + str(key))
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        print('Deleting ' + str(key))
        return super().__delitem__(key)

class SetOnceMappingMixin:
    '''
    Only allow a key to be set once.
    '''
    __slots__ = ()
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key, value)

class StringKeysMappingMixin:
    '''
    Restrict keys to string only
    '''
    __slots__ = ()
    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError('key must be strings')
        return super().__setitem__(key, value)

class LoggedDict(LoggedMappingMixin, dict):
    pass

d = LoggedDict()
#d['x'] = 23  # Setting x = 23
#print(d['x'])
# Gettring x
# 23
#del d['x']  # Deleting x

from collections import defaultdict

class SetOnceDefaultDict(SetOnceMappingMixin, defaultdict):
    pass

d = SetOnceDefaultDict(list)
#d['x'].append(12)
#d['y'].append(23)
#d['x'].append(10)
#d['x'] = 23
# Traceback (most recent call last):
#   File "18.py", line 60, in <module>
#     d['x'] = 23
#   File "18.py", line 28, in __setitem__
#     raise KeyError(str(key) + ' already set')
# KeyError: 'x already set'
