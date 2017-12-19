# Dictionaries is like map in C++,
# one key maps to a value.

phonebook = {}
phonebook["John"] = 13012345678
phonebook["Jack"] = 13012345679
phonebook["Jill"] = 13012345670

# Output: {'John': 13012345678, 'Jack': 13012345679, 'Jill': 13012345670}
# print(phonebook)

phonebook = {
    "John": 13012345678,
    "Jack": 13012345679,
    "Jill": 13012345670
}

# print(phonebook)

# Iterating over dictionaries
#for name, number in phonebook.items():
#    print("Phone number of %s is %d" % (name, number))

# Operations over dictionaries
#phonebook.pop("John")
#print(phonebook)


# Exercise
phonebook = {
    "John": 13012345678,
    "Jack": 13012345679,
    "Jill": 13012345670
}

phonebook["Jake"] = 13012345670
phonebook.pop("Jill")

if "Jake" in phonebook:
    print("Jake is listed in the phonebook")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook")
