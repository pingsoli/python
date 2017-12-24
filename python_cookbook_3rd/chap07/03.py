# 7.3 Attaching Informational Metadata to Function Arguments

def add(x:int, y:int) -> int:
    return x + y

print(add(1.0, 2.0))  # 3.0
print(add('1', '2'))  # 12
print(add('hello', 'world'))  # helloworld

# Though add attached annotations don't check, 
# but they might give useful hints to others
# reading the source code.
