# 1.10 Removing duplicates from a Sequence whlie Maintaining Order

# eliminate the duplicate values in sequence, but preserve the 
# order of the remaining items.

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
b = list(dedupe(a))
print(b)  # [1, 5, 2, 9, 10]


# If you want to eliminate duplicates, just use set.

b = set(a)
print(b)  # {1, 2, 5, 9, 10}
