#  Public Variables and Methods
# Assignment: 03
# Create a class Car with a public variable brand and a public method start().
# Instantiate the class and access both from outside the class.
class Car:
    def __init__(self, brand):
        self.brand = brand
    def start(self):
        print( f"{self.brand} , the car is starting.")
car = Car("Toyota")  # Calling public method
car.start()  # Accessing public method
print(car.brand)  # Accessing public variable     