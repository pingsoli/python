# 1.20 Combining Multiple Mappings into a Single Mapping

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

from collections import ChainMap
c = ChainMap(a, b)
# print(c['x'])  # 1
# print(c['y'])  # 2
# print(c['z'])  # 3
#print(c, len(c))  # ChainMap({'x': 1, 'z': 3}, {'y': 2, 'z': 4}) 3

#print(list(c.keys()))  # ['y', 'x', 'z']
#print(list(c.values()))  # [3, 1, 2]

# If there are duplicate keys, the values from the first mapping get used.


values = ChainMap()
values['x'] = 1
# Add a new mapping
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3

#print(values)  # ChainMap({'x': 3}, {'x': 2}, {'x': 1})

# Discard last mapping 
values = values.parents
#print(values['x'])  # 2

# Discard last mapping 
values = values.parents
#print(values['x'])  # 1


# ChainMap, use the original data, and don't change it.
# we must change the original data, and the chainmap will get affected.
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = ChainMap(a, b)
print(merged['x'])  # 1
a['x'] = 31
print(merged['x'])  # 31
