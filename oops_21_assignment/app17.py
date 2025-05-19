# Class Decorators
# Assignment: 17
# Create a class decorator add_greeting that modifies a class to add a greet()
#  method returning "Hello from Decorator!". Apply it to a class Person.


def add_greeting(cls):
   def greet(self):
         return "Hello from Decorator!"
   cls.greet = greet
   return cls


@add_greeting
class Person:
     def __init__(self, name):
          self.name = name
     def display(self):
          return f"Name: {self.name}"
          

show = Person("Alice")
show.display()
print(show.greet())