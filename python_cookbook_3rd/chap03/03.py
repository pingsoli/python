# 3.3 Formatting Numbers for Output

x = 1234.56789
#print(format(x, '0.2f'))  # 1234.57
#print(format(x, '>10.1f'))  #    1234.6
# >, <, ^ is right, left, center alignment.

# Inclusion of thousands separator
#print(format(x, ','))  # 1,234.56789
#print(format(x, '0,.1f'))  # 1,234.6

#print(format(x, 'e'))  # 1.234568e+03
#print(format(x, '0.2E'))  # 1.23E+03
