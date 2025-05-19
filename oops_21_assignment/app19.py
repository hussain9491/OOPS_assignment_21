
# callable() and __call__()
# Assignment: 19
# Create a class Multiplier with an __init__() to set a factor. 
# Define a __call__() method that multiplies an input by the factor. 
# Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    def __call__(self, x):
        return x * self.factor
show = Multiplier(3)
print(callable(show))  # Check if the object is callable
print(show(5))  # Call the object like a function
