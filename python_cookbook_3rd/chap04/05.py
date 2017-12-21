# 4.5 Iterating in Reverse

a = [1, 2, 3, 4, 5]
for x in reversed(a):
    print(x)
# Output:
# 5
# 4
# 3
# 2
# 1

# Implementing __reversed__.
class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward interator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1
    
    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n 
            n += 1
