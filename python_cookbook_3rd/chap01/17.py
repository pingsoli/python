# 1.17 Extracting a Subset of Dictionary

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# Make a dictionary of all prices over 200
p1 = { key:value for key, value in prices.items() if value > 200 }
#print(p1)  # {'AAPL': 612.78, 'IBM': 205.55}

# Make a dictionary of tech stocks 
tech_name = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
p2 = { key:value for key, value in prices.items() if key in tech_name }
print(p2)  # {'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.2}

# Another way. 
p1 = dict((key, value) for key, value in prices.items() if value > 200)
# print(p1)  # {'AAPL': 612.78, 'IBM': 205.55}

# Make a dictionay of tech stocks 
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
p2 = { key:prices[key] for key in prices.keys() & tech_names }
# print(p2)  # {'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.2}
