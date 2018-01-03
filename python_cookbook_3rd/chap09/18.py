# 9.18 Defining Classes Programmatically

def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price

def cost(self):
    return self.shares * self.price

cls_dict = {
    '__init__': __init__,
    'cost': cost,
}

# Make a class
import types

Stock = types.new_class('Stock', (), {}, lambda ns: ns.update(cls_dict))
Stock.__module__ = __name__

s = Stock('ACME', 50, 90.1)
#print(s.cost())  # 4505.0

# __main__ and __name__
# if run current file, __name__ will be '__main__'
# if uses to be exported, __name__ is the module name.
#print(__name__)  # __main__
