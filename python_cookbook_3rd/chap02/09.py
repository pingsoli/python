# 2.9 Normalizing Unicode Text to a Standard Representation

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

# Spicy Jalapeño Spicy Jalapeño
#print(s1, s2)

#print(s1 == s2) # False
#print(len(s1))  # 14
#print(len(s2))  # 15

import unicodedata
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
#print(t1 == t2)  # True

#print(ascii(t1))
# 'Spicy Jalape\xf1o'

s = '\ufb01'  # A single character
#print(s)  # ﬁ

#print(unicodedata.normalize('NFD', s))  # ﬁ
#print(unicodedata.normalize('NFKD', s)  # fi
#print(unicodedata.normalize('NFKC', s)  # fi


# Remove all diacritical marks from text
t1 = unicodedata.normalize('NFD', s1)
print(''.join(c for c in t1 if not unicodedata.combining(c)))
# Spicy Jalapeno
