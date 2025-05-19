#  Creating a Custom Exception
# Assignment: 20
# Create a custom exception InvalidAgeError. 
# Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.
class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    pass
def check_age(age):
    
     if age < 18 :
        raise InvalidAgeError("Age must be 18 or older")
     print("Age is valid")
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)

except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")
except ValueError:
    print("Please enter a valid integer for age.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    