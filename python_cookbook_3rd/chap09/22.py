# 9.22 Defining Context Managers the Easy Way

import time
from contextlib import contextmanager

@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}: {}'.format(label, end - start))


# with timethis('counting'):
#     n = 1000000
#     while n > 0:
#         n -= 1
# counting: 0.10411858558654785

# Transaction

@contextmanager
def list_transaction(orig_list):
    working = list(orig_list)
    yield working
    orig_list[:] = working

items = [1, 2, 3]
with list_transaction(items) as working:
    working.append(4)
    working.append(5)
#print(items)  # [1, 2, 3, 4, 5]

with list_transaction(items) as working:
    working.append(6)
    working.append(7)
    raise RuntimeError('oops')

#print(items)  # [1, 2, 3, 4, 5]
# Traceback (most recent call last):
#   File "22.py", line 39, in <module>
#     raise RuntimeError('oops')
# RuntimeError: oops

import time

class timethis:
    def __init__(self, label):
        self.label = label

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_ty, exc_val, exc_tb):
        end = time.time()
        print('{}: {}'.format(self.label, end - self.start)))

# It do the same job, but is more tedious than using @contextmanager
