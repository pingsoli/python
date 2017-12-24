# 7.2 Writing Functions That Only Accept Keyword Arguments

def recv(maxsize, *, block):
    'Receives a message'
    pass

#recv(1024, True)  # TypeError
#recv(1024, block=True)  # Ok

def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

a = minimum(1, 5, 2, -5, 10)
b = minimum(1, 5, 2, -5, 10, clip=0)
print(a)  # -5
print(b)  # 0
