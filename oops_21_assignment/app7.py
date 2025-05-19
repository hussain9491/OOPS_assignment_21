# . Access Modifiers: Public, Private, and Protected
# Assignment: 07
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self,name, salary, humble):
        self.name = name
        self._salary = salary # protected variable
        self.__ssn = humble # private variable
    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")
result = Employee("John Doe", 50000, "123-45-6789")
result.display()          