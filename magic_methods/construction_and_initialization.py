# __init__, __new__, __del__ methods

# __new__ used rarely, and not so much useful, when a object is created, 
# __new__ method is frist to be called.

# __init__ is very useful to initialize a object.

# __del__ is used to comtome your own deleter.

from os.path import join

class FileObject:
    def __init__(self, filepath='.', filename='sample.txt'):
        # open a file filename in filepath in read and write mode
        self.file = open(join(filepath, filename), 'r+')

    def __del__(self):
        self.file.close()
        del self.file

test = FileObject()


