# 12.8 Performing Simple Parallel Programming

# Some function
def work(x):
    # ...
    return result

with ProcessPollExecutor() as pool:
    # ...
    future_result = pool.submit(work, arg)

    # Obtaining the result (blocks until done)
    r = future_result.result()

    # ....

# Instead of blocking, you can also arrange to have a callback function
# triggered upon completion instead.

def when_done(r):
    print('Got:', r.result)

with ProcessPollExecutor() as pool:
    future_result = pool.submit(work, arg)
    future_result.add_done_callback(when_done)
