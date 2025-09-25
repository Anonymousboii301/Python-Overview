# print("Hello world")

#  In terminal we write 
#  pip install flask 
#  Pip install pyjokes



import pyjokes

print("Printing jokes..........")

# this prints a random joke
joke = pyjokes.get_joke()
print(joke)


# 1. Built-in Modules
# Python has many built-in modules that provide functionality for different tasks.
# Example: Using the math module


import math
print(math.sqrt(16))  # Output: 4.0
print(math.pi)        # Output: 3.141592653589793
# 
# Example: Using the random module

import random
print(random.randint(1, 10))  # Output: Random number between 1 and 10




# 2. User-Defined Modules
# You can create your own modules by saving Python code in a .py file.



import my_module
print(my_module.greet("Batman"))  # Output: Hello, Batman!





# 3. External Modules
# External modules are installed using pip.   ( pip3 for Mac or Linux)
# Example: Installing and using numpy

# 1. 
# Install numpy:

# pip install numpy

# 2. 
# Use it in Python:

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)  # Output: [1 2 3 4 5]



