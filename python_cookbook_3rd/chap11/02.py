# 11.2 Creating a TCP Server

# from socketserver import BaseRequestHandler, TCPServer
# 
# class EchoHandler(BaseRequestHandler):
#     def handle(self):
#         print('Got connection from ', self.client_address)
#         while True:
#             msg = self.request.recv(8192)
#             if not msg:
#                 break
#             self.request.send(msg)
# 
# if __name__ == '__main__':
#     serv = TCPServer(('', 20000), EchoHandler)
#     serv.serve_forever()

# Test code
# from socket import socket, AF_INET, SOCK_STREAM
# 
# s = socket(AF_INET, SOCK_STREAM)
# s.connect(('localhost', 20000))
# s.send(b'Hello')
# s.recv(8191)

from socketserver import StreamRequestHandler, TCPServer

class EchoHandler(StreamRequestHandler):
    def handle(self):
        print('Got connection form', self.client_address)
        # self.rfile is a file-like object for reading
        for line in self.rfile:
            # self.wfile is a file-list object for reading
            self.wfile.write(line)

# Single thread
# if __name__ == '__main__':
#     serv = TCPServer(('', 20000)， EchoHandler)
#     serv.serve_forever()

# Multpile thread, using thread pool to manage allocated threads.
# if __name__ == '__main__':
#     from threading import Thread
#     NWORKERS = 16
#     serv = TCPServer(('', 20000), EchoHandler)
#     for n in range(NWORKERS):
#         t = Thread(target=serv.serve_forever)
#         t.daemon = True
#         t.start()
#     serv.serve_forever()

# Adjusting socket options.
# using bing_and_activate=False
# if __name__ == '__main__':
#     serv = TCPServer(('', 20000), EchoHandler, bind_and_activate=False)
#     
#     # Setup various socket options
#     serv.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
#     # Bind and active
#     serv.server_bind()
#     serv.server_activate()
#     serv.serve_forever()

# if __name__ == '__main__':
#     TCPServer.allow_reuse_address = True
#     serv = TCPServer(('', 20000), EchoHandler)
#     serv.serve_forever()

# For more flexible settings
import socket

# class EchoHandler(StreamRequestHandler):
#     # Optional settings (default shown)
#     timeout = 5                      # Timeout on all socket operations
#     rbufsize = -1                    # Read buffer size
#     wbufsize = 0                     # Write buffer size
#     disable_nagle_algorithm = False  # Sets TCP_NODELAY socket option
#     def handle(self):
#         print('Got connection form', self.client_address)
#         try:
#             for line in self.rfile:
#                 # self.rfile is a file-like object for writing
#                 self.wfile.write(line)
#         except socket.timeout:
#             print('Time out!')


# Regular socket server implementation
# from socket import socket, AF_INET, SOCK_STREAM
# 
# def echo_handler(address, client_sock):
#     print('Got connection from {}'.format(address))
#     while True:
#         msg = client_sock.recv(8192)
#         if not msg:
#             break
#         client_sock.sendall(msg)
#     client_sock.close()
# 
# def echo_server(address, backlog=5):
#     sock = socket(AF_INET, SOCK_STREAM)
#     sock.bind(address)
#     sock.listen(backlog)
#     while True:
#         client_sock, client_addr = sock.accpet()
#         echo_handler(client_addr, client_sock)
#
# if __name__ == '__main__':
#     echo_server(('', 20000))
