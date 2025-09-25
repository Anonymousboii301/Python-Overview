# In Python, a string is a sequence of characters used to represent text. Strings can include letters, numbers, symbols, and even spaces. Strings in Python are enclosed in either single quotes (' ') or double quotes (" ").

# Example of Strings in Python:
# Using single quotes
# name = 'BATMAN'

# Using double quotes
# greeting = "Hello, World!"

# Using triple quotes for multi-line strings
# message = """This is a
# multi-line string."""
# Key Points about Strings in Python:
# Immutable: Strings in Python are immutable, meaning once a string is created, it cannot be changed. However, you can create a new string based on operations on the original one.



# text = "Hello"
# Trying to change a character will result in an error
# text[0] = "h"  # This will raise a TypeError
# Concatenation: You can concatenate (join) strings using the + operator.



# first_name = "Bat"
# last_name = "man"
# full_name = first_name + last_name
# print(full_name)  # Output: Batman
# Repetition: You can repeat a string using the * operator.



# laugh = "Ha"
# print(laugh * 3)  # Output: HaHaHa
# Indexing and Slicing: You can access characters of a string using indexing and slicing.


# word = "Python"
# print(word[0])    # Output: P (first character)
# print(word[-1])   # Output: n (last character)
# print(word[1:4])  # Output: yth (slice from index 1 to 3)
# String Methods: Python provides many built-in methods to manipulate strings.



# text = "hello world"
# print(text.upper())  # Output: HELLO WORLD
# print(text.capitalize())  # Output: Hello world
# print(text.replace("world", "BATMAN"))  # Output: hello BATMAN
# Creating Strings with Variables
# python
# Copy code
# name = "Batman"
# age = 35
# introduction = f"My name is {name}, and I am {age} years old."
# print(introduction)
# Output: My name is Batman, and I am 35 years old.
# Checking the Type
# You can check if a variable is a string using the type() function:


# text = "This is a string"
# print(type(text))  # Output: <class 'str'>
# Strings are one of the most commonly used data types in Python, making them crucial for text processing, user input, file handling, and many other tasks.



