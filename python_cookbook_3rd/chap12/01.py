# 12.1 Starting and Stopping Threads

# thread library can be used execute any Python callable in its own
# thread.

# Code to execute in an indepentdent thread
import time
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)

# Create and lanuch a thread
from threading import Thread
t = Thread(target=countdown, args=(10,))
t.start()

# t.is_alive()
# t.join()
