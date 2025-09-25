class Employee:
    language = "Py" # This is a class attribute
    salary = 12000000

ayush = Employee()
print(ayush.language,ayush.salary)

rohan = Employee()
rohan.name = "Vishal"  # This is an object tribute or Instance attributes
print(rohan.language,rohan.salary)


# CLASS ATTRIBUTES 
# An attribute that belongs to the class rather than a particular object. 

# Here name is object/instance tribute and salary and language are class attribute
#  as they are directly belongs to the class







'''
Key Points:
Defined inside the __init__ method (or other methods) using self.attribute_name.
Each instance has its own copy of instance attributes.
They can be modified independently for each instance.
'''



# Example of Class Attributes:


class Car:
    wheels = 4  # Class attribute

    def __init__(self, brand, model):
        self.brand = brand  # Instance attribute
        self.model = model  # Instance attribute

# Creating instances
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print(car1.wheels)  # Output: 4
print(car2.wheels)  # Output: 4

# Changing the class attribute
Car.wheels = 6

print(car1.wheels)  # Output: 6
print(car2.wheels)  # Output: 6


