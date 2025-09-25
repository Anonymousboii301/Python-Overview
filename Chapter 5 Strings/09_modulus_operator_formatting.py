# formatting using  modulus (%) operator

# String formatting using the % operator (also known as printf-style formatting) is a method in Python where format specifiers like 
# %s, %d, and %f are used within a string to insert variables or values. It's an older formatting technique inspired by the C language's printf() function.


# string formatting using the % operator in Python — also known as printf-style formatting, because it’s similar to how formatting works in C's printf().

# Although f-strings and .format() are more modern and preferred today, % formatting is still useful and you'll encounter it in older codebases.

#  Basic Syntax
# "format string" % (values)

# Example:
name = "Batman"
print("Hello, %s!" % name)
# Output:
# Hello, Batman!

# Format Specifiers

# Format	Meaning	Example
# %s	String	"Name: %s" % "Batman"
# %d	Integer (decimal)	"Age: %d" % 30
# %f	Floating-point number	"Pi: %.2f" % 3.1415
# %x	Hexadecimal (lower)	"%x" % 255 → ff
# %o	Octal	"%o" % 10 → 12
# %%	Literal % character	"Discount: 10%%"



# Examples

# Multiple values
name = "Batman"
age = 35
print("Name: %s, Age: %d" % (name, age))


# Floating-point with precision
pi = 3.14159265
print("Pi rounded: %.2f" % pi)
# Output:
# Pi rounded: 3.14


# Padding and alignment
num = 42
print("Padded number: %5d" % num)   # Right-align in 5 spaces
print("Padded string: %-10s!" % "Hero")  # Left-align in 10 spaces


# Hexadecimal and Octal
num = 255
print("Hex: %x, Octal: %o" % (num, num))
# Output:
# Hex: ff, Octal: 377










# Common Mistakes
# Mismatch between placeholders and values:

# Too many values
# print("Name: %s" % ("Batman", 30))  # Error



# Incorrect type:
# Using %d with a string
# print("Age: %d" % "thirty")  # TypeError





# When to Use % Formatting?


# Useful in:
# Legacy Python 2 code
# 
# Simple one-liners
# 
# Developers coming from C background


# 
# Avoid for:
# 
# Complex formatting
# 
# Readability in modern Python (use .format() or f-strings)

#  Summary
# % formatting is old but still works

# Use %s, %d, %f, %x, etc. for type-specific formatting

# Always pass a tuple (...) when formatting multiple values



# book 

# Formatting using Modulo Operator (%)
x, pi = 5, 22/7
print("x = %d, pi = %f" % (x, pi))       #  Output: x = 5, pi = 3.142857
# %disreplaced by 5 and %f is replaced by 22/7. Here, floating point number is printed up to 6 decimal places


print("x = %5d, pi = %.4f" % (x, pi))      # Output: x = 5,pi=3.1429
 #.4 is used to limit the decimal places of pi to 4
 #5d, This specifies that the integer will take up at least 5 characters. If x has fewer digits, it will be padded with spaces on the left.


print("pi = %8.3f" % pi)                 # Output: pi = 3.143
#8 after mod, This specifies that the integer will take up at least 8 characters. If it has fewer digits, it will be padded with spaces on the left


