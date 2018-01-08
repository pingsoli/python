# 11.7 Communicating Simply Between Interpreters

# It's a simple example. If you needed to support low-level control over
# aspect of the connection. For example, timeouts, nonblocking I/O,
# or anything similar, you'd better off using a different library or
# implementing such features on top of sockets instead.

from multiprocessing.connection import Listener
import traceback

def echo_client(conn):
    try:
        while True:
            msg = conn.recv()
            conn.send(msg)
    except EOFError:
        print('Connection closed')

def echo_server(address, authkey):
    serv = Listener(address, authkey=authkey)
    while True:
        try:
            client = serv.accept()
            echo_client(client)
        except Exception:
            traceback.print_exc()

echo_server(('', 20000), authkey=b'pingsoli')

# >>> from multiprocessing.connection import Client
# >>> c = Client(('localhost', 20000), authkey=b'pingsoli')
# >>> c.send('hello')
# >>> c.recv()
# 'hello'
# >>> c.send(42)
# >>> c.recv()
# 42
# >>> c.send([1, 2, 3, 4])
# >>> c.recv()
# [1, 2, 3, 4]
