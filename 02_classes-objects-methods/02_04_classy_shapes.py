# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.

import math 

class Rectangle:
    def __init__(self, length , width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2* (self.length + self.width)
    
    def __repr__(self,):
        return f"Rectangle(length={self.length}, width={self.width})"
    
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius **2
    
    def circumference(self):
        return 2 * math.pi * self.radius
    
    def __repr__(self):
        return f"Circle(radius={self.radius})"
    
# EXAMPLE USAGE.
my_rectangle = Rectangle(15, 3)
my_circle= Circle(9)

print(my_rectangle) 
print("Rectangle area:", my_rectangle.area())
print("Rectangle perimeter:", my_rectangle.perimeter())
print("----------------------------------------")

print(my_circle) 
print("Circle area:", my_circle.area())
print("Circle circumference:", my_circle.circumference())