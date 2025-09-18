# In Python, variables are used to store data that can be referenced and manipulated throughout a program. Here’s a quick guide on variables in Python:

# 1. Creating Variables
# You create a variable by assigning a value using the = operator.



# Example
name = "BATMAN"   # String
age = 35          # Integer
height = 1.88     # Float
is_hero = True    # Boolean



# 2. Variable Naming Rules
# Must start with a letter (a-z, A-Z) or an underscore (_).
# Cannot start with a number.
# Can only contain letters, numbers, and underscores.
# Are case-sensitive (Name and name are different variables).
# Valid names:


my_var = 10
user_name = "BATMAN"
_age = 35
# Invalid names:



# 2var/ = 5      # Starts with a number
# user-name = "BATMAN"   # Contains a hyphen
# my var = 100  # Contains a space
# 3. Variable Types
# Python is dynamically typed, so you don’t need to declare the type of a variable. It can hold different data types:

# Integers (int): Whole numbers (e.g., 10, -5)
# Floats (float): Decimal numbers (e.g., 3.14, -0.01)
# Strings (str): Text (e.g., "Hello", 'Python')
# Booleans (bool): True/False values (e.g., True, False)
# Lists (list): Ordered, mutable collections (e.g., [1, 2, 3])
# Tuples (tuple): Ordered, immutable collections (e.g., (1, 2, 3))
# Dictionaries (dict): Key-value pairs (e.g., {"name": "BATMAN", "age": 35})
# 4. Type Checking
# To check the type of a variable, use the type() function:


# age = 35
# print(type(age))  # Output: <class 'int'>
# 5. Changing Variable Types (Type Casting)
# You can change the type of a variable using type casting:



x = "123"           # x is a string
y = int(x)          # y is an integer
z = float(x)        # z is a float
print(type(y))      # Output: <class 'int'>
print(type(z))      # Output: <class 'float'>
# 6. Multiple Assignment
# You can assign multiple variables at once:


x, y, z = 1, 2, 3
print(x, y, z)      # Output: 1 2 3
# You can also assign the same value to multiple variables:


a = b = c = 10
print(a, b, c)      # Output: 10 10 10
# 7. Updating Variables
# Variables can be updated by reassigning a new value:



count = 5
count = count + 1   # count is now 6
count += 1          # count is now 7 (shorthand for count = count + 1)
# 8. Deleting Variables
# You can delete a variable using the del keyword:



num = 100
del num
# print(num)   # This will raise an error since num is deleted

name = "BATMAN"
age = 35
is_hero = True

print(f"My name is {name}, and I am {age} years old.")
print(f"Am I a hero? {is_hero}")


# My name is BATMAN, and I am 35 years old.
# Am I a hero? True
# Would you like more information on a specific aspect of variables in Python?


# source - https://chatgpt.com/share/672f3ea6-1b0c-8000-af61-87b4e83fe85f



print('ayush')

__ffkfio__= 67
print(__ffkfio__)