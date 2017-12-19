# List comprehensions
# Creates a new list based on another list, in a single, readable line.

#sentence = "the quick brown fox jumps over the lazy dog"
#words = sentence.split()
#words_length = []
#
#for word in words:
#    if word != "the":
#        words_length.append(len(word))
#
#print(words)
#print(words_length)


# Simplify the above code.
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()

words_length = [len(word) for word in words if word != "the"]
print(words)
print(words_length)


# Exercise
# Filter a list, just keep positive number.
numbers = [ 34.6, -203.4, 44.9, 68.2, -12.2, 44.6, 13.8 ]
newlist = [number for number in numbers if number > 0]
print(numbers)
print(newlist)
