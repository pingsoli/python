# 4.9 Iterating Over All Possible Combination or Permutations

items = [1, 2, 3]
from itertools import permutations

#for x in permutations(items):
#    print(x)
# Output: 3 * 2 = 6
# (1, 2, 3)
# (1, 3, 2)
# (2, 1, 3)
# (2, 3, 1)
# (3, 1, 2)
# (3, 2, 1)

# Give permutation a length
#for p in permutations(items, 2):
#    print(p)
# Output:
# (1, 2)
# (1, 3)
# (2, 1)
# (2, 3)
# (3, 1)
# (3, 2)

#for x in permutations(items, 1):
#    print(x)
# Output:
# (1,)
# (2,)
# (3,)

from itertools import combinations_with_replacement
for c in combinations_with_replacement(items, 3):
    print(c)
# Output: 
# (1, 1, 1)
# (1, 1, 2)
# (1, 1, 3)
# (1, 2, 2)
# (1, 2, 3)
# (1, 3, 3)
# (2, 2, 2)
# (2, 2, 3)
# (2, 3, 3)
# (3, 3, 3)
