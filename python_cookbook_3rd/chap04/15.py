# 4.15 Iterating in Sorted Order Over Merged Sorted Iterables

import heapq

a = [1, 2, 3, 4]
b = [6, 7, 8, 9, 0]
#print(list(x for x in heapq.merge(a, b)))
# [1, 2, 3, 4, 6, 7, 8, 9, 0]

# Merge two sorted files
#with open('sorted_file_1', 'rt') as file1, \
#     open('sorted_file_2') 'rt' as file2, \
#     open('merged_file', 'wt') as outf:
#
#     for line in heapq.merge(file1, file2):
#         outf.write(line)

# NOTE: heapq.merge() requires that all the input sequences already be sorted.
# heapq.merge(a, b) just add b into the end of a.

x = [8, 2, 1, 3]
y = [9, 1, 2, 4]
#print(list(x for x in heapq.merge(x, y)))  # [8, 2, 1, 3, 9, 1, 2, 4]
