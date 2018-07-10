# Create a thread, and pass a argument to thread function.
# the main thread wait for the thread function finish.

# wait for a thread to finish
#   join() method, block and wait for the execution finished.
#
# kill or stop a running thread
#   no offical support
# if you use <Ctrl-C> to terminate the thread, that action will trigger a except
# called KeyBoardInterupt.
#
# Is it possible to make the thread stoppable ?

from time import sleep
from threading import Thread
from _thread import start_new_thread

def thread_func(arg):
    for i in range(arg):
        sleep(1)

def start_high_level_thread():
    thread = Thread(target = thread_func, args = (10, ))
    thread.start()
    #  thread.join()
    print("high level thread finished...exiting\n")

def start_low_level_thread():
    start_new_thread(thread_func, (10, ))
    print("low level thread finished...exiting\n")

if __name__ == "__main__":
    try:
        #  start_high_level_thread()
        start_low_level_thread()
    except:
        print("Error")

    input("press any key to continue...")

# high-level thread and high-lvel thread
# more detail: https://docs.python.org/3/library/threading.html?highlight=threading#module-threading
#
# If we use low-level thread, main process will destory the main thread and
# other child threads.
#
# If we use high-level thread, the task on child thread is not finished, the
# main process will wait for child thread finished, though we don't call
# `thread.join()`.
#
# Conlusion
# Prefer low-level thread, because we can control the execution of child thread.
