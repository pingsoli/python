# Strings In Python

# Features:
# 1) iterable
# 2) sequence immutable container

# Exercise 1: Calculate string length
test_str = 'hello world'
# print(len(test_str))  # 11

# Exercise 2: Character frequency
# Sample string: 'hello world'
# Expected result: { '' }
test_str = 'hello world'
frequency_statistic = {i: test_str.count(i) for i in test_str}
# print(frequency_statistic)
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# Exercise 3: Replace all occurences to specific charaters
test_str = 'restart'
# print(test_str[0] + test_str[1:].replace(test_str[0], '$'))  # resta$t

# Exercise 4: Swap first two characters of each string
str_one = 'abc'
str_two = 'xyz'
new_str = str_two[:2] + str_one[2:] + ' ' + str_one[:2] + str_two[2:]
# print(new_str)  # xyc abz

# Exercise 5: Replace and appending
# Sample string: 'abc'
# Expected result: 'abcing'
# Sample string: 'string'
# Expected result: 'stringly'
test_str = 'string'
new_str = ''
if test_str.endswith('ing'):
    new_str = test_str + 'ly'
else:
    new_str = test_str + 'ing'
# print(new_str)  # stringly

# Exercise 6: Finding and Subsitiute
test_str = 'The lyrics is not that bad'
# Expected output: 'the lyrics is good'
def not_poor(string):
    snot = string.find('not')
    sbad = string.find('bad')

    if sbad > snot:
        string = string.replace(string[snot:(sbad+4)], 'good')
    return string

# print(not_poor(test_str))
# The lyrics is good

# Exercise 7: Return the longest string of a list
list_s =  ['hello', 'world', 'test', 'pingsoli']
# print(max(list_s, key=len))  # pingsoli

# Exercise 8: alphanumberically
test_str = 'red, green, blue, pink, white'
words = [word for word in test_str.split(',')]
# print(','.join(sorted(list(set(words)))))
# blue, green, pink, white,red

# Exercise 9: reverse string if length is a multiple of 4
def reverse_string(string):
    print(len(string))
    if len(string) % 4 == 0:
        return string[::-1]
    else:
        return string
test_str = 'hello hahaha'
# print(reverse_string(test_str))
