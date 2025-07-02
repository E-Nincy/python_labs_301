# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title}, by {self.author}, {self.pages} pages"


class Laptop:
    def __init__(self, brand, ram, storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage

    def __str__(self):
        return F"{self.brand} Laptop, {self.ram} GB RAM, {self.storage} GB Storage "
    
class Backpack:
    def __init__(self, color, size, contents):
        self.color = color
        self.size = size
        self.contents = contents 

    def __str__(self):
        return f"{self.color} backpack ({self.size}) with: {', '.join(self.contents)}"

    def __add__(self, other):
        combined_color = f"{self.color}-{other.color}"
        combined_size = "combined"
        combined_contents = self.contents + other.contents
        return Backpack(combined_color, combined_size, combined_contents)

    
# CREATE INTANCES 
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("1984", "George Orwell", 328)

laptop1 = Laptop("Apple", 16, 512)
laptop2 = Laptop("Lemovo", 8, 256)

backpack1 = Backpack("Red", "Medium", ["notebook", "pen", "bottle"])
backpack2 = Backpack("Black", "Large", ["snack", "charger", "mouse"])

# CHANGE SOME ATTRIBUTES VALUES
book2.pages = 320
laptop1.ram = 32
backpack1.contents.append("wallet")

# USE OVERLOADES + OPERATOR
combined_backpack = backpack1 + backpack2

# PRINT EVERYTHING 
print(book1)
print(book2)
print("----------")

print(laptop1)
print(laptop2)
print("----------")

print(backpack1)
print(backpack2)
print(combined_backpack)