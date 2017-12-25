# 7.10 Carrying Extra State with Callback Functions

# callback functions, (event handles, completion callback, etc.)
# asynchronous processing.

def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)

def print_result(result):
    print('Got: ', result)

def add(x, y):
    return x + y

#apply_async(add, (2, 3), callback=print_result)
# Got:  5

# class ResultHandler:
#     def __init__(self):
#         self.sequence = 0
# 
#     def handler(self, result):
#         self.sequence += 1
#         print('[{}] Got: {}'.format(self.sequence, result))
# 
# r = ResultHandler()
#apply_async(add, (2, 3), callback=r.handler)
# [1] Got: 5
#apply_async(add, ('hello', 'world'), callback=r.handler)
# [2] Got: helloworld

# Using closure
def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))
    return handler

#handler = make_handler()
#apply_async(add, (1, 2), callback=handler)
#apply_async(add, ('hello', 'world'), callback=handler)
# [1] Got: 3
# [2] Got: helloworld

class SequenceNo:
    def __init__(self):
        self.sequence = 0

def handler(result, seq):
    seq.sequence += 1
    print('[{}] Got: {}'.format(seq.sequence, result))

seq = SequenceNo()
from functools import partial

apply_async(add, (2, 3), callback=partial(handler, seq=seq))
apply_async(add, ('hello', 'world'), callback=partial(handler, seq=seq))
# [1] Got: 5
# [2] Got: helloworld
