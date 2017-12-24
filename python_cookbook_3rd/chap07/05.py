# 7.5 Defining Functions with Default Arguments

def spam(a, b = 42):
    print(a, b)

#spam(1)  # 1 42
#spam(1, 2)  # 1 2

_no_value = object()
def spam_new(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')
    else:
        print(a, b)

spam_new(1)  # No b value supplied
spam_new(1, 2)  # 1 2
spam_new(1, None)  # 1 None

# Idioms 
# def spam(a, b=None):
#     if b is None:
#         ...
