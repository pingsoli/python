# 3.11 Picking Things at Random

import random 
values = [1, 2, 3, 4, 5, 6]

#for i in range(10):
#    print(random.choice(values))

# Sampling N items
#print(random.sample(values, 2))  # [6, 5]
#print(random.sample(values, 3))  # [5, 3, 4]

# Producing random integers.
#print(random.randint(0, 10))  # 5

#for i in range(10):
#    print(random.randint(0, 10))
# Output:
# 7
# 1
# 10
# 1
# 0
# 6
# 9
# 1
# 6
# 9

# Producing floating-point values in the range 0 to 1.
#print(random.random())  # 0.7212350463268123

# Getting random bits
#print(random.getrandbits(200)) 
# 1109239836679532229599745806788955285626603837708015459117307

# NOTE: random() should not be used in programs related to cryptography.
# you can consider ssl module instead.
