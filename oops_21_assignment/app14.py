# Assignment:
# Create a class Department and a class Employee.
# Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.


# aggression
# Aggregation mein ek class (e.g., Department) doosri class (e.g., Employee) ka reference use karti hai,
#  lekin wo doosri class ka object independent hota hai — 
# matlab agar Department delete ho jaye, Employee ka object still zinda rahega.


# ✅ Task:
# Employee class banana hai (independent object).
# Department class banao jo Employee ka reference store kare. 
# Employee ka object pehle se exist kare, phir wo Department ko diya jaye.
# Department us employee ka data access kare.

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    def get_info(self):
        return f"Employee Name: {self.name}, Position: {self.position}"
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []
    def add_employee(self, employee):
        self.employees.append(employee)
    def show_employees(self):
        print(f"Department: {self.name}")
        for emp in self.employees:
            print(emp.get_info())

c = Employee("John Doe", "Software Engineer")
d = Department("IT")
d.add_employee(c)
print(d.show_employees())
# print(d.employees[0].get_info())  # Accessing employee info directly from the department   

    
                
        