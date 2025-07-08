# Build on your freeform exercise from the previous section.
# Create child classes of two of the existing classes. Create a child class
# of one of the child classes so that the hierarchy is at least three levels.
#
# Build these classes out step-by-step like you did in the previous exercises.
# Use your notebook to brainstorm ideas and scribble down ideas.
#
# If you cannot think of a way to build on your freeform exercise,
# you can start with a new class from scratch.
# Try to make up your own example for this exercise, but if you are stuck,
# you could start working on the following:
#
# - A `Vehicle()` parent class, with `Truck()` and `Motorcycle()` child classes.
# - A `Restaurant()` parent class, with `Gourmet()` and `FastFood()` child classes.


# Parent class
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

# Child class
class Truck(Vehicle):
    def __init__(self, brand, year, cargo_capacity):
        super().__init__(brand, year)
        self.cargo_capacity = cargo_capacity

# Subclass Truck - ElectrickTruck
class ElectricTruck(Truck):
    def __init__(self, brand, year, cargo_capacity, battery_range):
        super().__init__(brand, year, cargo_capacity) 
        self.battery_range = battery_range

# Subclass Vehicle - Motorcycle
class Motorcicle(Vehicle):
    def __init__(self, brand, year, cc):
        super().__init__(brand, year)
        self.cc = cc
        