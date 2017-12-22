# 5.3 Printing with a Different Separator or Line Ending

# print('ACME', 50, 91.5)  # ACME 50 91.5
# print('ACME', 50, 91.5, sep=',')  # ACME,50,91.5
# print('ACME', 50, 91.5, sep=',', end='!!\n')  # ACME,50,91.5!!

# print() function default separator is newline character.
#for i in range(5):
#    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4

# for i in range(5):
#     print(i, end=' ')
# 0 1 2 3 4 

row = ('ACME', 50, 91.5)
#print(','.join(str(x) for x in row))
# ACME,50,91.5

print(*row, sep=',')
# ACME,50,91.5
