# 8.12 Defining an Interface or Abstract Base Class

from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass

#a = IStream()
# Traceback (most recent call last):
#   File "12.py", line 14, in <module>
#     a = IStream()
# TypeError: Can't instantiate abstract class IStream with abstract methods read, write

class SocketStream(IStream):
    def read(self, maxbytes=-1)
        pass
            
    def write(self, data):
        pass
