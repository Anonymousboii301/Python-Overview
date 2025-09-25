# What is .format() in Python?
# The .format() method is used to insert variables or values into a string using placeholders {}. 
# It provides more flexibility and readability than % formatting and works in Python 2.7+ and 3.x.

# Basic Syntax
# "string with {} placeholders".format(values)



#  Example:

name = "Batman"
print("Hello, {}!".format(name))
# Output:
# Hello, Batman!



# Multiple Placeholders

name = "Batman"
city = "Gotham"
print("I am {} and I protect {}.".format(name, city))





# Positional and Keyword Arguments


# Positional:
print("Hello, {0}. You are {1} years old.".format("Bruce", 35))


# Keyword:
print("Name: {name}, Age: {age}".format(name="Bruce", age=35))


# Reordering Values
print("{1} is older than {0}".format("Robin", "Batman"))
# Output:
# Batman is older than Robin





# Format Specifiers

# Floating point precision:
pi = 3.141592
print("Pi: {:.2f}".format(pi))  # Output: Pi: 3.14



# Integer padding:
num = 7
print("Padded: {:03}".format(num))  # Output: Padded: 007
# Alignment:

text = "Hero"
print("Center: {:^10}".format(text))  # Center aligned in 10 spaces
print("Left: {:<10}".format(text))    # Left aligned
print("Right: {:>10}".format(text))   # Right aligned

#  Accessing Data Structures
# List
heroes = ["Batman", "Superman"]
print("Hero 1: {0[0]}, Hero 2: {0[1]}".format(heroes))


# Dictionary
user = {"name": "Bruce", "age": 35}
print("Name: {0[name]}, Age: {0[age]}".format(user))


#  Using Objects with .format()
class Hero:
    def __init__(self, name, city):
        self.name = name
        self.city = city

batman = Hero("Batman", "Gotham")
print("Name: {0.name}, City: {0.city}".format(batman))









# .format() vs f-string vs %
# 
# Method	Version	Easy to Read	Supports Expressions	Performance
# .format()	2.7+	✅	❌	⚪ Medium
# f-string	3.6+	✅✅✅	✅✅✅	✅✅✅
# % operator	Legacy	⚪	⚪	⚪


#  Summary
# .format() uses {} to insert values into strings.
# 
# Supports positional, keyword, and mixed arguments.
# 
# Allows advanced formatting: padding, precision, alignment.
# 
# More readable than %, less concise than f-strings.





# book 

# Formatting using Format Method
pi = 22/7
print("x = {}, pi = {}".format(5, pi))       # Output: x = 5, pi = 3.142857142857143
 #the first {} is given the first argument .i.e 5 and the second {} took the value or variable pi


print("x = {0}, pi = {1}".format(5, pi))       # Output: x = 5, pi = 3.142857142857143
print("pi = {1}, x = {0}".format(5, pi))       #  Output: pi = 3.142857142857143, x = 5
 # {0}, {1} represent the first and the second argument passed to the method.


print("x = {0:5d}, pi = {1:.4f}".format(5, pi))       # Output: x = 5,pi=3.1429

print("pi = {0:8.3f}".format(pi))       # Output: pi = 3.143
 # In {0:8.3f}, ‘0’ before ‘:’ represents the argument no., as pi being 0th argument.
 # ‘8’ after ‘:’ specifies that integer will take up at least 8 characters. If it has fewer digits, it will be padded with spaces on the left.
 # ‘.3f’ for the 3 decimal places


print("x = {x}, pi = {0:.4f}".format(pi, x = 5))       # Output: x = 5, pi = 3.1429