#  Static Methods
# Assignment: 12
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        """
        Convert Celsius to Fahrenheit.
        
        :param c: Temperature in Celsius
        :return: Temperature in Fahrenheit
        """
        return (c * 9/5) + 32
    
temp = TemperatureConverter()
print(temp.celsius_to_fahrenheit(25))  # 25 degrees Celsius is 77 degrees Fahrenheit