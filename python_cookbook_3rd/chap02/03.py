# 2.3 Matching String Using Shell Willcard Patterns

from fnmatch import fnmatch, fnmatchcase

#print(fnmatch('foo.txt', '*.txt'))   # True
#print(fnmatch('foo.txt', '?oo.txt')) # True
#print(fnmatch('Dat45.csv', 'Dat[0-9]*'))  # True

# fnmatchcase matches the lower and uppercase you provide.
#print(fnmatchcase('foo.txt', '*.TXT'))  # False

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

street_addrs = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
# ['5412 N CLARK ST', '1060 W ADDISON ST', '2122 N CLARK ST']
#print(street_addrs)

specific_addr = [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
# ['5412 N CLARK ST']
#print(specific_addr)
