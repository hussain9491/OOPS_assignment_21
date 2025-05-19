# Composition
# Assignment: 13
# Create a class Engine and a class Car. Use composition by passing an Engine
#  object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    def start(self):
        return f"Engine with {self.horsepower} HP started."
class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def set_engine(self, engine):
        self.engine = engine
    def start(self):
        return f"{self.color} {self.make} {self.model} started with {self.engine.start()}"
start = Engine(150)
car = Car("Toyota", "Corolla", "Red")    
car.set_engine(start)
print(car.start())
print(car.engine.start())
          