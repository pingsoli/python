# 5.21 Serializing Python Objects

# import pickle
# data = ... # Some Python object
# f = open('somefile', 'wb')
# pickle.dump(data, f)

# Dump an object to a string, use pickle.dumps()
#s = pickle.dumps(data)

# Restore from a file
f = open('somefile', 'rb')
data = pickle.load(f)

# Restore from a string
data = pickle.load(s)
