# Instance Methods
# Assignment: 10
# Create a class Dog with instance variables name and breed.
#  Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self, name, bread):
        self.name = name
        self.breed = bread
    def bark(self):
        print(f"{self.name} says Woof!")
        print(f"{self.name} is a {self.breed} breed.")

bark = Dog("Buddy", "Golden Retriever")
bark.bark()        
        