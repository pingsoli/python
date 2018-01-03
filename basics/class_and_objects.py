# Class and Objects

class MyClass:
    name = "pingsoli"

    def print_info(self):
        print("this is a message inside the class.") 

myobj = MyClass()
#myobj.print_info()


# Exercise
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f" % (
            self.name, self.color, self.kind, self.value)

        return desc_str

car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.value = 60000.00

    
car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.value = 10000.00

#print(car1.description())
#print(car2.description())
# Fer is a red car worth $60000.00
# Jump is a blue car worth $10000.00

# @staticmethod and @classmethod difference
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_as_string):
        year, month, day = map(int, date_as_string.split('-'))
        date1 = cls(year, month, day)
        return date1

    @staticmethod
    def is_valid_date(date_as_string):
        year, month, day = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


date2 = Date.from_string('2018-01-02')
print(Date.is_valid_date('2018-01-02'))  # True
