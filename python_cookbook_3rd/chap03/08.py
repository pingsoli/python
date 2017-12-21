# 3.8 Calculating with Fractions

from fractions import Fraction
a = Fraction(5, 4)
b = Fraction(7, 16)
#print(a + b)  # 27/16
#print(a * b)  # 35/64

# Getting numberator/denominator
c = a * b
#print(c.numerator, c.denominator)  # 35 64

# Converting to a float
#print(float(c))  # 0.546875

# Converting a float to a fraction
x = 3.75
y = Fraction(*x.as_integer_ratio())
#print(y)  # 15/4
