# 12.12 Using Generators As an Alternative to Threads

# Two simple generator functions
def countdown(n):
    while n > 0:
        print('T-minus', n)
        yield
        n -= 1

def countup(last):
    n = 0
    while n < last:
        print('Counting up', n)
        yield
        n += 1

from collections import deque

class TaskScheduler:
    def __init__(self):
        self._task_queue = deque()

    def new_task(self, task):
        self._task_queue.append(task)

    def run(self):
        while self._task_queue:
            task = self._task_queue.popleft()
            try:
                next(task)
                self._task_queue.append(task)
            except StopIteration:
                pass

# Example use
sched = TaskScheduler()
sched.new_task(countdown(10))
sched.new_task(countdown(5))
sched.new_task(countup(15))
sched.run()

# T-minus 10
# T-minus 5
# Counting up 0
# T-minus 9
# T-minus 4
# Counting up 1
# T-minus 1
# ....
# Counting up 9
# Counting up 10
# Counting up 11
# Counting up 12
# Counting up 13
# Counting up 14
