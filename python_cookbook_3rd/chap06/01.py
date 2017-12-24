# 6.1 Reading and Writing CSV Data

import csv
# with open('stocks.csv') as f:
#     f_csv = csv.reader(f)
#     headers = next(f_csv)
#     for row in f_csv:
#         # Process row
#         print(row)
# Output:
# ['AA', '39.48', '6/11/2007', '9:36am', '-0.18', '181800']
# ['AIG', '71.38', '6/11/2007', '9:36am', '-0.15', '195500']
# ['AXP', '62.58', '6/11/2007', '9:36am', '-0.46', '935000']
# ['BA', '98.31', '6/11/2007', '9:36am', '+0.12', '104800']
# ['C', '53.08', '6/11/2007', '9:36am', '-0.25', '360900']
# ['CAT', '78.29', '6/11/2007', '9:36am', '-0.23', '225400']

# Write data to CSV file
# headers = ['Symbol','Price','Date','Time','Change','Volume']
# rows = [
#     ('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
#     ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
#     ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
# ]
# 
# with open('test.csv', 'w') as f:
#     f_csv = csv.writer(f)
#     f_csv.writerow(headers)
#     f_csv.writerows(rows)

# Dictionary 
# headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
# rows = [
#     {'Symbol':'AA', 'Price':39.48, 'Date':'6/11/2007', 
#      'Time':'9:36am', 'Change':-0.18, 'Volume':181800},
#     {'Symbol':'AIG', 'Price': 71.38, 'Date':'6/11/2007',
#      'Time':'9:36am', 'Change':-0.15, 'Volume': 195500},
#     {'Symbol':'AXP', 'Price': 62.58, 'Date':'6/11/2007',
#      'Time':'9:36am', 'Change':-0.46, 'Volume': 935000},
#     ]
# 
# with open('stocks.csv', 'w') as f:
#     f_csv = csv.DictWriter(f, headers)
#     f_csv.writeheader()
#     f_csv.writerows(rows)

# with open('stocks.csv') as f:
#     for line in f:
#         row = line.split(',')
#         print(row)
# Output:
# ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume\n']
# ['"AA"', '39.48', '"6/11/2007"', '"9:36am"', '-0.18', '181800\n']
# ['"AIG"', '71.38', '"6/11/2007"', '"9:36am"', '-0.15', '195500\n']
# ['"AXP"', '62.58', '"6/11/2007"', '"9:36am"', '-0.46', '935000\n']
# ['"BA"', '98.31', '"6/11/2007"', '"9:36am"', '+0.12', '104800\n']
# ['"C"', '53.08', '"6/11/2007"', '"9:36am"', '-0.25', '360900\n']
# ['"CAT"', '78.29', '"6/11/2007"', '"9:36am"', '-0.23', '225400\n']

col_types = [str, float, str, str, str, float, int]
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # Apply conversion to the row items
        row = tuple(convert(value) for convert, value in zip(col_types, row))
        print(row)
# Output:
# ('AA', 39.48, '6/11/2007', '9:36am', '-0.18', 181800.0)
# ('AIG', 71.38, '6/11/2007', '9:36am', '-0.15', 195500.0)
# ('AXP', 62.58, '6/11/2007', '9:36am', '-0.46', 935000.0)
# ('BA', 98.31, '6/11/2007', '9:36am', '+0.12', 104800.0)
# ('C', 53.08, '6/11/2007', '9:36am', '-0.25', 360900.0)
# ('CAT', 78.29, '6/11/2007', '9:36am', '-0.23', 225400.0)

# NOTE: Use csv conversion should make use the csv file is error free.
# Or, maybe we get the corrupted data, and other issue.
