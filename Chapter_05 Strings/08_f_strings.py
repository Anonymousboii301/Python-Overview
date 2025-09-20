# What is an f-string?
# An f-string (formatted string literal) is a way to format strings in Python using expressions inside {}.
# Introduced in Python 3.6, it’s the fastest and most readable way to build strings with dynamic content.
# 
# Basic Syntax
# f"some text {expression}"

# You just put an f before the string and insert variables or expressions inside {}.

#  Example:
name = "Batman"
print(f"Hello, {name}!")
# Output:
# Hello, Batman!


name = "Batman"
age = 30
print(f"My name is {name} and I am {age} years old.")

# Output:
# My name is Batman and I am 30 years old.

a = 5
b = 10
print(f"The sum of {a} and {b} is {a + b}.")
# Output:
# The sum of 5 and 10 is 1

pi = 3.1415926535
print(f"Value of pi: {pi:.2f}")
# Output:
# Value of pi: 3.14
# .2f means format the float with 2 digits after the decimal.



# Embedding Variables and Expressions
# Variables
age = 25
print(f"I am {age} years old.")


# Expressions
x = 10
y = 20
print(f"{x} + {y} = {x + y}")


# Multiline f-strings
# Use triple quotes:

name = "Batman"
city = "Gotham"
intro = f"""
Hello, my name is {name}.
I protect the city of {city}.
"""
print(intro)



# Formatting Numbers
# Decimal places:

pi = 3.14159265
print(f"Pi rounded to 2 decimals: {pi:.2f}")

# Output:
# Pi rounded to 2 decimals: 3.14




# Padding & Alignment:

for x in range(1, 6):
    print(f"{x:<3} | {x**2:<3}")  # Left align


# Thousand separator:

num = 1000000
print(f"{num:,}")  # Output: 1,000,000


# f-strings and Expressions
# You can write actual Python expressions inside {}:


print(f"The result of 2 * 5 is {2 * 5}")



# Even function calls:

def greet(name):
    return f"Hi, {name}"

print(f"Greeting: {greet('Batman')}")


# f-strings with Dictionaries

user = {"name": "Bruce", "age": 35}
print(f"Name: {user['name']}, Age: {user['age']}")


# Using f-strings with Class Objects
class Hero:
    def __init__(self, name, power):
        self.name = name
        self.power = power

batman = Hero("Batman", "Stealth")
print(f"Hero: {batman.name}, Power: {batman.power}")


# Using =, Debugging with f-strings (Python 3.8+)
x = 10
y = 5
print(f"{x=}, {y=}, {x+y=}")
# Output:
# x=10, y=5, x+y=15

# This is super useful for debugging!



# Things You CANNOT Do with f-strings


# You can’t use backslashes inside expressions:
# Invalid
f"{'Hello\nWorld'}"  # will work but don’t use \ inside {}




# You can’t nest f-strings:

# Invalid
f"{f'Hello {name}'}"



# Performance
# Fastest method compared to .format() and % formatting.

# Efficient for large-scale string formatting.

# f-string vs .format() vs % formatting

# Method	Python Version	Readability	Performance
# f-string	3.6+	⭐⭐⭐⭐⭐	⭐⭐⭐⭐⭐
# .format()	2.7+	⭐⭐⭐	⭐⭐⭐
# % formatting	Legacy	⭐⭐	⭐⭐


# Summary
# ✔ f-strings are easy, fast, and powerful
# ✔ Use {} to insert variables or expressions
# ✔ Supports formatting numbers, dates, objects, functions
# ✔ Introduced in Python 3.6










# ❖Formatting using f-string
x =5
print(f"value of x is {x}")         # Output: value of x is 5
print(f"value of x is {x:5d}")      # Output: value of x is 5
# Above print statement prints the value of the variable x with a field width of 5 characters, right-aligned. 'd' represents decimal number, 'f' represents float


pi = 22/7
print(f"value of pi is {pi}")        # Output: value of pi is 3.142857142857143
print(f"value of pi is {pi:.3f}")    # Output: value of pi is 3.143
# If we want afloat number to nth decimal place we’ve to write '.nf'

print(f"value of pi is {pi:8.3f}")    # Output: value of pi is 3.143