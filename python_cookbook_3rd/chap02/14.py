# 2.14 Combining and Concatenating Strings

parts = ['Is', 'Chicago', 'Not', 'Chicago?']

#print(' '.join(parts))  # Is Chicago Not Chicago?

a = 'Is Chicago'
b = 'Not Chicago?'
#print('{} {}'.format(a, b))  # Is Chicago Not Chicago?
#print(a + ' ' + b)  # Is Chicago Not Chicago?

# no + operator
#a = 'hello' 'world'
#print(a)  # helloworld


# NOTE: + operator is grossly inefficient due to memory and garbage collection

data = ['ACME', 50, 91.1]
#print(','.join(str(d) for d in data))  # ACME,50,91.1

#print(a + ':' + b + ':' + c)  # Ugly
#print(':'.join([a, b, c]))    # Still ugly
#print(a, b, c, sep=':')       # Better
