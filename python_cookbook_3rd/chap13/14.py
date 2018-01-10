# 13.14 Putting Limits on Memory and CPU Usage

import signal
import resource
import os

def time_exceeded(signo, frame):
    print('time is up!')
    raise SystemExit(1)

def set_max_runtime(seconds):
    soft, hard = resource.getrlimit(resource.getrlimit(resource.RLIMIT_CPU))
    resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
    signal.signal(signal.SIGXCPU, time_exceeded)

if __name__ == '__main__':
    set_max_runtime(14)
    while True:
        pass
