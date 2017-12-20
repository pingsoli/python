# 1.13 Sorting a List of Dictionaries by a Common Key

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

# [
#     {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}, 
#     {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}, 
#     {'fname': 'David', 'lname': 'Beazley', 'uid': 1002}, 
#     {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}
# ]
#print(rows_by_fname)

# [
#     {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}, 
#     {'fname': 'David', 'lname': 'Beazley', 'uid': 1002}, 
#     {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}, 
#     {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
# ]
#print(rows_by_uid)

# itemgetter can accept multiple keys.
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))

# [
#     {'fname': 'David', 'lname': 'Beazley', 'uid': 1002}, 
#     {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}, 
#     {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}, 
#     {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}
# ]
#print(rows_by_lfname)

# Sometimes, we can use min() and max() to find out the min and max.
min_rows = min(rows, key=itemgetter('uid'))
print(min_rows)  # {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}
max_rows = max(rows, key=itemgetter('uid'))
print(max_rows)  # {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
