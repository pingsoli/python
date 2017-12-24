# 6.2 Reading and Writing JSON Data

import json

data = {
    'name': 'ACME', 
    'shares': 100,
    'price': 234.22
}

json_str = json.dumps(data)
#print(json_str)
# {"name": "ACME", "shares": 100, "price": 234.22}

data_new = json.loads(json_str)
#print(data_new)
# {'name': 'ACME', 'shares': 100, 'price': 234.22}

# Writing JSON data
with open('data.json', 'w') as f:
    json.dump(data, f)

# Reading JSON file
with open('data.json', 'r') as f:
    data = json.load(f)
#    print(data)
# {'name': 'ACME', 'shares': 100, 'price': 234.22}

# Pay attention to converting dictionary, list, and etc to json


# Converting JSON dicrectory to a Python object.
s = '{"name": "ACME", "shares": 50, "price": 490.1}'
class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

data = json.loads(s, object_hook=JSONObject)
#print(data.name)  # ACME

data = {
    'name': 'ACME', 
    'shares': 100,
    'price': 234.22
}
#print(json.dumps(data, indent=4))
# Output:
# {
#     "name": "ACME",
#     "shares": 100,
#     "price": 234.22
# }

#print(json.dumps(data, sort_keys=True))
# {"name": "ACME", "price": 234.22, "shares": 100}

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def serialize_instance(obj):
    d = { '__classname__': type(obj).__name__ }
    d.update(vars(obj))
    return d

# Dictionary mapping names to known classes
classes = {
    'Point': Point
}

def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)  # Make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d

p = Point(1, 2)
s = json.dumps(p, default=serialize_instance)
#print(s)
# {"__classname__": "Point", "x": 1, "y": 2}
a = json.loads(s, object_hook=unserialize_object)
#print(a)
# <__main__.Point object at 0x7f1e44073da0>

print(a.x, a.y)  # 1 2
