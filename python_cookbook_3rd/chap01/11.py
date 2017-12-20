# 1.11 Naming a Slice

######    0123456789012345678901234567890123456789012345678901234567890'
record = '....................100          .......513.25     ..........'
cost = int(record[20:32]) * float(record[40:48])

# print(cost)  # 51325.0

# Using slice() instead
SHARES = slice(20, 32)
PRICE = slice(40, 48)
cost = int(record[SHARES]) * float(record[PRICE])
# print(cost)  # 51325.0


items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
# print(items[2:4]) # [2, 3]
# print(items[a])   # [2, 3]

items[a] = [10, 11]
# print(items)  # [0, 1, 10, 11, 4, 5, 6]

del items[a]
# print(items)  # [0, 1, 4, 5, 6]


# Get slice attribute
a = slice(10, 50, 2)
print(a.start, a.stop, a.step)  # 10 50 2


