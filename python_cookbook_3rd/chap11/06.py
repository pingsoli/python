# 11.6 Implementing a Simple Remote Procedure Call with XML-RPC

# Firstly, you should be familiar with RPC.
# In distributed system, RPC is used for distributed computing.
# There following graph is the model of RPC.
#
#      +--------+    call    +--------+
#      |        | ---------> |        |
#      | Client |            | Server |
#      |        | <--------- |        |
#      +--------+   return   +--------+

from xmlrpc.server import SimpleXMLRPCServer

class KeyValueServer:
    _rpc_methods_ = ['get', 'set', 'delete', 'exists', 'keys']
    def __init__(self, address):
        self._data = {}
        self._serv = SimpleXMLRPCServer(address, allow_none=True)
        for name in self._rpc_methods_:
            self._serv.register_function(getattr(self, name))

    def get(self, name):
        return self._data[name]

    def set(self, name, value):
        self._data[name] = value

    def delete(self, name):
        del self._data[name]

    def exists(self, name):
        return name in self._data

    def keys(self):
        return list(self._data)

    def serve_forever(self):
        self._serv.serve_forever()

if __name__ == '__main__':
    kvserv = KeyValueServer(('', 15000))
    kvserv.serve_forever()

# Testing
# >>> from xmlrpc.client import ServerProxy
# >>> s = ServerProxy('http://localhost:15000', allow_none=True)
# >>> s.set('foo', 'bar')
# >>> s.set('foo', 'bar')
# >>> s.set('spam', [1, 2, 3, 4])
# >>> s.keys()
# ['foo', 'spam']
# >>> s.get('foo')
# 'bar'
# >>> s.get('spam')
# [1, 2, 3, 4]
# >>> s.delete('spam')
# >>> s.exists('spam')
# False
