# 8.25 Creating Cached Instances

import logging

a = logging.getLogger('foo')
b = logging.getLogger('bar')
c = logging.getLogger('foo')

#print(a is b)  # False
#print(a is c)  # True


class Spam:
    def __init__(self, name):
        self.name = name

import weakref
_spam_cache = weakref.WeakValueDictionary()

def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]
    return s

a = get_spam('foo') 
b = get_spam('bar')
c = get_spam('foo')
#print(a is b)  # False
#print(a is c)  # True


class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            s = Spam(name)
            self._cache[name] = s
        else: 
            s = self._cache[name]
        return s
    
    def clear(self):
        self._cache.clear()

class Spam:
    manager = CachedSpamManager()

    def __init__(self, name):
        self.name = name

    def get_spame(name):
        return Spam.manager.get_spam(name)

a = Spam('foo')
b = Spam('foo')
print(a is b)  # False
