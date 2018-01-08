# 11.12 Understanding Event-Driven I/O

class EventHandler:
    def fileno(self):
        'Return the associated file descriptor'
        raise NotImplemented('must implement')

    def wants_to_receive(self):
        'Return True if receving is allowed'
        return False

    def handle_receive(self):
        'Perform the receive operation'
        pass

    def wants_to_send(self):
        'return the sending is required'
        pass

    def handle_send(self):
        'Send outgoing data'
        pass

import select

def event_loop(handlers):
    while True:
        wants_recv = [h for h in handlers if h.wants_to_receive()]
        wants_send = [h for h in handlers if h.wants_to_send()]
        can_recv, can_send, _ = select.select(wants_recv, wants_send, [])
        for h in can_recv:
            h.handle_receive()
        for h in can_send:
            h.handle_send()

import socket
import time

class UDPServer(EventHandler):
    def __init__(self, address):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(address)

    def fileno(self):
        return self.sock.fileno()

    def wants_to_receive(self):
        return True

class UDPTimeServer(UDPServer):
    def handle_receive(self):
        msg, addr = self.sock.recvfrom(1)
        self.sock.sendto(time.ctime().encode('ascii'), addr)

class UDPEchoServer(UDPServer):
    def handle_receive(self):
        msg, addr = self.sock.recvfrom(8192)
        self.sock.sendto(msg, addr)

if __name__ == '__main__':
    handlers = [ UDPTimeServer(('', 14000)), UDPEchoServer(('', 15000)) ]
    event_loop(handlers)

# >>> from socket import *
# >>> s = socket(AF_INET, SOCK_DGRAM)
# >>> s.sendto(b'', ('localhost', 14000))
# 0
# >>> s.recvfrom(128)
# (b'Mon Jan  8 11:10:40 2018', ('127.0.0.1', 14000))
# >>> s.sendto(b'hello', ('localhost', 15000))
# 5
# >>> s.recvfrom(128)
# (b'hello', ('127.0.0.1', 15000))


