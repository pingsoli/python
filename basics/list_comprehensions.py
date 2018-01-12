# List comprehensions

# What is list conprehensions?
# Creates a new list based on another list, in a single, readable line.

# Regular code
# sentence = "the quick brown fox jumps over the lazy dog"
# words = sentence.split()
# words_length = []
#
# for word in words:
#     if word != "the":
#         words_length.append(len(word))
#
# print(words)
# print(words_length)

# Simplify the above code using list comprehension
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
words_length = [len(word) for word in words if word != "the"]

# print(words)
# ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
# print(words_length)
# [5, 5, 3, 5, 4, 4, 3]

# Exercise 1
# Filter a list, just keep positive number.
numbers = [ 34.6, -203.4, 44.9, 68.2, -12.2, 44.6, 13.8 ]
newlist = [number for number in numbers if number > 0]

# print(numbers)
# [34.6, -203.4, 44.9, 68.2, -12.2, 44.6, 13.8]
# print(newlist)
# [34.6, 44.9, 68.2, 44.6, 13.8]

# listcomps versus map and filter
another_list = list(filter(lambda number: number > 0, numbers))
#print(another_list)
# [34.6, 44.9, 68.2, 44.6, 13.8]

# Exercise 2
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
# print(tshirts)
# [
#   ('black', 'S'),
#   ('black', 'M'),
#   ('black', 'L'),
#   ('white', 'S'),
#   ('white', 'M'),
#   ('white', 'L')
# ]
