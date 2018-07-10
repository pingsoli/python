# 12.2 Determining If a Thread Has Started

from threading import Thread, Event
import time

def countdown(n, started_event):
    print('countdown starting')
    started_event.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(2)

# Create the event object that will be used to signal startup
started_event = Event()

# Lanuch the thread and pass the startup event
#print('Lanuching countdown')
#t = Thread(target=countdown, args=(10, started_event))
#t.start()

# Wait for the thread to start
#started_event.wait()
#print('countdown is running')

import threading
import time

class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()

    def start(self):
        t = threading.Thread(target=self.run)
        t.daemon = True
        t.start()

    def run(self):
        while True:
            time.sleep(self._interval)
            with self._cv:
                self._flag ^= 1
                self._cv.notify_all()

    def wait_for_tick(self):
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()

# Example use of the timer
ptimer = PeriodicTimer(5)
ptimer.start()

def countdown(nticks):
    while nticks > 0:
        ptimer.wait_for_tick()
        print('T-miuns', nticks)
        nticks -= 1

def countup(last):
    n = 0
    while n < last:
        ptimer.wait_for_tick()
        print('Counting', n)
        n += 1

threading.Thread(target=countdown, args=(10,)).start()
threading.Thread(target=countup, args=(5,)).start()