# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.

class ModelCar:
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def increase_speed(self):
        self.max_speed += 5

    def print_details(self):
        print(f"Model: {self.model}, Year: {self.year}, Max Speed: {self.max_speed} km/h")

car1 = ModelCar("Toyota Corolla", 2020, 180)
car2 = ModelCar("Ford Mustang", 2022, 250)

car1.print_details()     
car1.increase_speed()
car1.print_details()

car2.print_details()    
car2.increase_speed()
car2.increase_speed()


car2.print_details()  