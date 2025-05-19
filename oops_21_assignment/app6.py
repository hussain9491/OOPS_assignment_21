# Constructors and Destructors
# Assignment: 06
# Create a class Logger that prints a message
#  when an object is created (constructor) and another message when it is destroyed (destructor).
class Logger:
    def __init__(self):
        print("Logger object created.")

    def __del__(self):
        print("Logger object destroyed.")
display  = Logger()
# print(display.__del__())
# The constructor message will be printed when the object is created.
# # The destructor message will be printed when the object is destroyed.       
