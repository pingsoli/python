# 11.3 Creating a UDP Server

from socketserver import BaseRequestHandler, UDPServer
import time

class TimeHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        # Get message and client socket
        msg, sock = self.request
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), self.client_address)

if __name__ == '__main__':
    serv = UDPServer(('', 20000), TimeHandler)
    serv.serve_forever()

# Test code
# >>> from socket import socket, AF_INET, SOCK_DGRAM
# >>> s = socket(AF_INET, SOCK_DGRAM)
# >>> s.sendto(b'', ('', 20000))
# 0
# >>> s.recvfrom(8192)
# (b'Fri Jan  5 11:38:08 2018', ('127.0.0.1', 20000))

# We can see the difference between TCP and UDP interface
# TCP usually use send() and recv(), however UDP
# use sendto() and recvfrom(), tcp is oriend-connection,
# but udp is point-to-point, do not comfirm the transferring.

# The above code is single thread example.
# If we want to use multi-thread in UDP server, the
# ForkingUDPServer and ThreadingUDPServer will statisfy us.
