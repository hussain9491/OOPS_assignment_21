
#  Property Decorators: @property, @setter, and @deleter
# Assignment: 18
# Create a class Product with a private attribute _price. Use @property to get the price,
#  @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self.__price = price
        @property
        def price(self):
            return self.__price
        @price.setter
        def price(self, new_price):
            if new_price < 0:
             raise ValueError ("Price cannot be negative")  
            self.__price = new_price
        @price.deleter
        def price(self):
         print("Deleting price...")
         del self.__price 
d = Product(100)
print(f"Old price was{d._Product__price}")  # Accessing the price using the property
d.price = 150
print(f"Now price is {d.price}")
# del d.price
