# STATIC METHOD 

# Sometimes we need a function that does not use the self-parameter. We can define a 
# static method like this: 


@staticmethod   
# decorator to mark greet as a static method  
def greet(): 
 print("Hello user")



'''
Static Method in Python
A static method in Python is a method that belongs to a class but does not operate on an instance (self) or the class (cls). It behaves like a regular function but is defined inside a class.

Static methods are declared using the @staticmethod decorator. They are used when you don’t need to access or modify instance or class attributes.'''



# Syntax & Example


class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

# Calling the static method
result = MathOperations.add(5, 10)
print(result)  # Output: 15

'''
Key Points About Static Methods
✅ No self or cls parameter (doesn't depend on instance or class).
✅ Acts like a regular function but is inside a class for better organization.
✅ Used for utility/helper functions (e.g., mathematical operations, validations).'''


'''
When to Use a Static Method?

When the method doesn’t modify class or instance data.
When functionality is related to the class but doesn’t require instance variables.
For utility functions inside a class (e.g., date/time operations, validators).
'''


# Example: Using Static Method for Validation


class Validator:
    @staticmethod
    def is_even(number):
        return number % 2 == 0

# Calling the static method
print(Validator.is_even(10))  # Output: True
print(Validator.is_even(7))   # Output: False


# Summary

# 🔹 Static methods are independent of class and instance but are placed inside a class for logical grouping.
# 🔹 They act as helper functions that don’t modify class or instance data.
# 🔹 Use @staticmethod to define them.