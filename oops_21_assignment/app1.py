# 1. Using self
# Assignment 01:
# Create a class Student with attributes name and marks. 
# Use the self keyword to initialize these values via a constructor. 
# Add a method display() that prints student details.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(f"Student name is {self.name} and marks are {self.marks}") 

display = Student("hussain ali", 90)
display.display()

