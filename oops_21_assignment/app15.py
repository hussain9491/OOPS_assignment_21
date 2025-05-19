#  Method Resolution Order (MRO) and Diamond Inheritance
# Assignment: 15
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.

class A:
    def show(self):
        return "Class A"
class B(A):
    def show(self):
        return "Class B"
class C(A):
    def show(self):
        return "Class C"
class D(B, C):
    def show(self):
        return "Class D"
dis = D()
b = B()
c = C()
dis.show()  # Output: Class D
print(dis.show())  # Output: Class D
print(D.mro())  # Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

