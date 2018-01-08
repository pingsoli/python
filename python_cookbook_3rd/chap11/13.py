# 11.13 Sending and Receiving Large Arrays

def send_from(arr, dest):
    view = memoryview(arr).cast('B')
    while len(view):
        nsent = dest.send(view)
        view = view[nsent:]

def recv_into(arr, source):
    view = memoryview(arr).cast('B')
    while len(view):
        nrecv = source.recv_into(view)
        view = view[nrecv:]

# view = memoryview(arr).cast('B')
# It takes an array and casts into a memoryview of unsigned bytes.
# One issue here is the receiver has to know in advance how much 
# data will be sent so that it can either preallocate an array or
# verify that it can receive the data into an existing array.
