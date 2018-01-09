# 12.3 Communicating Between Threads

# Queue instances already have all of the required locking.

from queue import Queue
from threading import Thread

def producer(out_q):
    # Produce some data
    # ...
    out_q.put(data)

def consumer(in_q):
    while True:
        # Get some data
        # ...
        data = in_q.get()
        # Process data
        # ...

q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()

# Problem
# shutdown the proceducer and consumer
# Put special sentinal value in queue, and cause comsumers to terminate.

from queue import Queue
from threading import Tread

# Object that signals shutdown
_sentinel = Object()

def producer(out_q):
    while running:
        # Produce some data
        # ...
        out_q.put(data)
    # Put the sentinnel on 
    out_q.put(_sentinel)

def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()

        # Check for termination
        if data is _sentinel:
            in_q.put(_sentinel)
            break

        # Process the data
        # ...

# Thread-safe priority queue
import headpq
import threading

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._count = 0
        self._cv = threading.Condition()

    def put(self, item, priority):
        with self._cv:
            headpq.heappush(self._queue, (-priority, self._count, item))
            self._coutn += 1
            self._cv.notify()

    def get(self):
        with self._cv:
            while len(self._queue) == 0:
                self._cv.wait()
            return heapq.headpop(self._queue)[-1]

# The same logic as other language, so we must make sure we have the
# basic concept of sychronization between threads.
