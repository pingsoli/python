# 1.18 Mapping Names to Sequence Elements

# A instance of namedtuple looks like a normal class instance.
# it is inter-changeable with a tuple and supports all of the 
# usual tuple operations such as indexing and unpacking.
# type name, fields

from collections import namedtuple

Subscriber = namedtuple('Subscriber', [ 'addr', 'joined' ])
sub = Subscriber('pingsoli@163.com', '2012-10-12')
#print(sub)  # Subscriber(addr='pingsoli@163.com', joined='2012-10-12')
#print(sub.addr, sub.joined)  # pingsoli@163.com 2012-10-12

#print(len(sub))      # 2
addr, joined = sub
#print(addr, joined)  # pingsoli@163.com 2012-10-12


# Major usage: 

# Here is a ordinary code
def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

# Use namedtuple instead
Stock = namedtuple('Stock', ['name', 'shares', 'price'])

def compute_cost_new(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

# Test 
s = Stock('ACME', 100, 123.45)
# s.shares = 75
# Error Message:
# Traceback (most recent call last):
#   File "18.py", line 41, in <module>
#     s.shares = 75
# AttributeError: can't set attribute

# Use _replace mothod to modify values of field
s._replace(shares = 75)
#print(s)  # Stock(name='ACME', shares=100, price=123.45)


Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)

# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)

a = {'name': 'ACME', 'shares': 1000, 'price': 123.45}
stock_a = dict_to_stock(a)
# Stock(name='ACME', shares=1000, price=123.45, date=None, time=None)
#print(stock_a)

b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2017'}
stock_b = dict_to_stock(b)
# Stock(name='ACME', shares=100, price=123.45, date='12/17/2017', time=None)
print(stock_b)

