# 7.6 Defining Anonymous or Inline Functions

# lambda expression
add = lambda x, y: x + y
#print(add(2, 3))  # 5
#print(add('hello', 'world'))  # helloworld

names = [
            'David Beazley', 'Brian Jones', 
            'Raymond Hettinger', 'Ned Batchelder'
        ]
print(sorted(names, key=lambda name: name.split()[-1].lower()))
# ['Ned Batchelder', 'David Beazley', 'Raymond Hettinger', 'Brian Jones']
