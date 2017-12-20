# 1.9 Finding Commonalities in Two Dictionaries

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10, 
    'x': 11,
    'y': 2
}

# Find keys in common
key_comm = a.keys() & b.keys()

# Find keys in a that are not in b
key_diff = a.keys() - b.keys()

# Find (key, value) pairs in common
item_comm = a.items() & b.items()

print(key_comm)   # {'x', 'y'}
print(key_diff)   # {'z'}
print(item_comm)  # {('y', 2)}
