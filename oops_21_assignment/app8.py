#  The super() Function
# Assignment: 08
# Create a class Person with a constructor that sets the name.
#  Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person created with name: {self.name}")

class Teaher(Person):   
    def __init__(self,subject, name):
        super().__init__(name)
        self.subject = subject
        print(f"Teacher created with subject: {self.subject}")
dis = Teaher("Math", "John Doe")
print(dis.name)  # Output: John Doe        

         
        