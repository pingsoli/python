# 12.4 Locking Cirtical Sections

import threading

class SharedCounter:
    '''
    A counter object that can be shared by multiple threads
    '''
    def __init__(self, initial_value = 0):
        self._value = initial_value
        self._value_lock = threading.Lock()

    def increment(self, delta=1):
        '''
        Increment the counter with locking
        '''
        with self._value_lock:
            self._value_lock += delta

    def decrement(self, delta=1):
        '''
        Decrement the counter with locking
        '''
        with self._value_lock:
            self._value_lock -= delta

# With expression has a advantage, lock the scope when entering,
# and release lock when leaving the scope.

# We can also lock explicitly acquired and released.
#
# self._value_lcok.acquire()
# self._value += delta
# self._value_lock.release()

# BTW, with is more elegant and less prone to error.
