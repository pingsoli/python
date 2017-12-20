# 1.19 Transforming and Reducing Date at Same Time

nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
#print(s)  # 55

# Determine if any .py files exist in a directory 
import os

# files = os.listdir('.')
# if any(name.endswith('.py') for name in files):
#     print('There be python!')
# else:
#     print('Sorry, no python!')


# Output a tuple as CSV
s = ('ACME', 50, 123.45)
# ACME,50,123.45
#print(','.join(str(x) for x in s))


# Data reduction across fields of a data structure 
portfolio = [
    {'name': 'GOOG', 'shares': 50}, 
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL',  'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]

min_shares = min(s['shares'] for s in portfolio)
#print(min_shares)  # 20


# The second way is more elegant, efficient approach.
# The first creating a temporary list.
s = sum((x * x for x in nums))
s = sum(x * x for x in nums)
