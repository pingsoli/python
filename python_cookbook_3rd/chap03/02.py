# 3.2 Performing Accurate Decimal Calculations

a = 4.2
b = 2.1
#print(a + b)  # 6.300000000000001
# This error are a 'feature' of the underlying CPU and
# IEEE 754 arithmetic performed by its floating-point unit.

# Use decimal module instead when required.
from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
#print(a + b)  # 6.3
#print((a + b) == 6.3)  # False
#print((a + b) == Decimal('6.3'))  # True

from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
#print(a / b)  # 0.7647058823529411764705882353

# with localcontext() as ctx:
#     ctx.prec = 3
#     print(a / b)  # 1.765
# 
# with localcontext() as ctx:
#     ctx.prec = 50
#     print(a / b)
# 0.76470588235294117647058823529411764705882352941176
