#  What is end in Python print()?
# By default, every print() statement in Python ends with a newline (\n). That’s why each print() call goes to the next line.

# The end parameter lets you change what gets printed at the end instead of the newline.

#  Default Behavior:

print("Hello")
print("World")

# Output:
# Hello
# World



#  With end Parameter:
print("Hello", end=" ")
print("World")
# Output:
# Hello World


#  Syntax:
# print(value1, value2, ..., end="your_custom_ending")


# More Examples:
# Print numbers on the same line:

for i in range(1, 6):
    print(i, end=" ")

# Output:
# 1 2 3 4 5


# Print with custom endings:

print("Loading", end="...")
print(" Done!")

# Output:
# Loading... Done!



# Combine sep and end:

print("Batman", "Robin", sep=" & ", end=" 💥 ")
print("Dynamic Duo!")

# Output:
# Batman & Robin 💥 Dynamic Duo!




# endparameter in print(): By default Python‘s print() function ends with a newline(\n) which can be modified and made to any character using the ‘end’ parameter.

print("Hello")
print("python")
# Output: Hello 
        # python

print("Hello", end = " ")
print("python", end = ". ^_^ ")
#  Output: Hello python. ^_^

print("Hello", "python", end = ".", sep = ", ")
# Output: Hello, python.

