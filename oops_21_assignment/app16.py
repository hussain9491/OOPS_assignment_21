#  Function Decorators
# Assignment: 16
# Write a decorator function log_function_call that prints "Function is being called" 
# before a function executes. Apply it to a function say_hello().
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper
@log_function_call
def say_hello():
    return "Hello, World!"
print(say_hello())  