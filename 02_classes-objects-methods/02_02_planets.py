# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

# Base class
class Planet():
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def describe(self):
         return (f"I am {self.name}, the {self.position} planet from the Sun.")

    def __str__(self):
         return f"{self.name} is the {self.position} planet from the sun"    

# Objects for each planet
mercury = Planet("Mercury", "1st")
venus = Planet("Venus", "2nd")
earth = Planet("Earth", "3rd")
mars = Planet("Mars", "4th")
jupiter = Planet("Jupiter", "5th")
saturn = Planet("Saturn", "6th")
uranus = Planet("Uranus", "7th")
neptune = Planet("Neptune", "8th")

#Planet list
solar_system = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

# Panet data
for planet in solar_system:
     print(planet.describe())
     print(planet)
     print("---")