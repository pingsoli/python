# 13.13 Making a Stopwatch Timer

import time

class Timer:
    def __init__(self, func=time.perf_counter):
        self.elapsed = 0.0
        self._func = func
        self._start = None

    def start(self):
        if self._start is not None:
            raise RuntimeError('Already started')
        self._start = self._func()

    def stop(self):
        if self._start is None:
            raise RuntimeError('Not started')
        end = self._func()
        self.elapsed = end - self._start
        self._start = None

    def restart(self):
        self.elapsed = 0.0

    @property
    def running(self):
        return self._start is not None

    def __enter__(self):
        self.start()

    def __exit__(self, *args):
        self.stop()

def countdown(n):
    while n > 0:
        n -= 1

# Use 1: Explicit start/stop
t = Timer()
t.start()
countdown(100000)
t.stop()
#print(t.elapsed)  # 0.006792546000042421

# Use 2: As a context manager
with t:
    countdown(100000)
#print(t.elapsed)  # 0.006198686000061571

# with Timer() as t2:
#     countdown(100000)
# print(t2.elapsed)

# CPU time
t = Timer(time.process_time)
with t:
    countdown(100000)
#print(t.elapsed)  # 0.005274879000000003
