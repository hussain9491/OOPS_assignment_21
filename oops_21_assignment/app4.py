# Class Variables and Class Methods
# Assignment: 04
# Create a class Bank with a class variable bank_name.
#  Add a class method change_bank_name(cls, name) that allows changing the bank name.
#  Show that it affects all instances.
class Bank:
    bank_name = "ABC Bank"  # Class variable
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        return f"{cls.bank_name} is the new bank name."
# Create instances of the Bank class
bank1 = Bank()

bank1.change_bank_name("Meezan Bank") 
 # Change the bank name using class method
print(bank1.bank_name)  # Accessing class variable through instance