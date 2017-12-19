
# define __eq__ methods

#if instance == other_instance:
#    # do something


# comparison magic methods
# __cmp__(self, other): implements behavior for all 
# comparasion operators(!, ==, !=, etc)

# __eq__(self, other): == 
# __ne__(self, other): !=
# __lt__(self, other): <
# __gt__(self, other): >
# __le__(self, other): <=
# __ge__(self, other): >=

# Example
class Word(str):
    ''' class for words, defining comparasion based on word length'''

    def __new__(cls, word):
        if ' ' in word:
            print("Value contains spaces. Truncating to first space")
            word = word[:word.index(' ')]
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __le__(self, other):
        return len(self) <= len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

#myStr = Word("helli")
#testStr = Word("hello")
#if myStr < testStr:
#    print("%s is less than %s" %(myStr, testStr))
#else:
#    print("%s is bigger than %s" %(myStr, testStr))


# Normal arithmetic operators
# implement +, -, *, etc
# __add__, __sub__, __mul__, __floordiv__, __div__,
# __mod__


# Type conversion magic methods
# __int__, __long__, __float__, __complex___, __oct__

