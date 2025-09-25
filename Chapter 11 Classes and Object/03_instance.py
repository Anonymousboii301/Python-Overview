''''
An instance attribute in Python is a variable that belongs to a specific instance of a class. It is defined inside the class but assigned using self, meaning each instance of the class can have different values for its instance attributes.
'''


# Example of Instance Attributes:

class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Instance attribute
        self.model = model  # Instance attribute

# Creating instances
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print(car1.brand)  # Output: Toyota
print(car2.brand)  # Output: Honda


'''
Key Points:
Defined inside the __init__ method (or other methods) using self.attribute_name.
Each instance has its own copy of instance attributes.
They can be modified independently for each instance.
'''