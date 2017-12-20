# 1.12 Determining the Most Frequently Occuring Items in a Sequence

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
] 

from collections import Counter

word_counts = Counter(words)
top_three = word_counts.most_common(3)
# print(top_three)  # [('eyes', 8), ('the', 5), ('look', 4)]

# print(word_counts['not'])  # 1
# print(word_counts['eyes']) # 8


a = Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 'around': 2,
    "you're": 1, "don't": 1, 'under': 1, 'not': 1})

b = Counter({'eyes': 1, 'looking': 1, 'are': 1, 'in': 1, 'not': 1, 'you': 1,
    'my': 1, 'why': 1})

# Combine counts
c = a + b

# Counter({'eyes': 9, 'the': 5, 'look': 4, 'my': 4, 'into': 3, 'around': 2,
#     'not': 2, "you're": 1, "don't": 1, 'under': 1, 'looking': 1, 
#     'are': 1, 'in': 1, 'you': 1, 'why': 1})
# print(c)

# Subtract counts
d = a - b
# Counter({'eyes': 7, 'the': 5, 'look': 4, 'into': 3, 'my': 2, 'around': 2, "you're": 1, "don't": 1, 'under': 1})
print(d)
