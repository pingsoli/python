# 1.8 Calculating with Dictionaries

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# It's very useful to invert the keys and values of the dictionary
# using zip().

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))

# (10.75, 'FB') (612.78, 'AAPL')
print(min_price, max_price)

# Using zip() and sorted() to rank the data.
prices_sorted = sorted(zip(prices.values(), prices.keys()))
# [(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')]
print(prices_sorted)
