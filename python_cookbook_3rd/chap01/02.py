# 1.2 Unpacking Elements from Interables of Arbitrary Length

# Keyword: star expresson, '*'

record = ('pingsoli', 'pingsoli@163.com', '123456789', '123456789')
name, email, *phone_number = record

# pingsoli pingsoli@163.com ['123456789', '123456789']
# print(name, email, phone_number)

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

# foo 1 2
# bar hello
# foo 3 4
# for tag, *args in records:
#     if tag == 'foo':
#         do_foo(*args)
#     if tag == 'bar':
#         do_bar(*args)

items = [1, 20, 7, 4, 5, 9]
head, *tail = items
# 1 [20, 7, 4, 5, 9]
# print(head, tail)
