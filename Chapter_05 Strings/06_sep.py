# ✅ What is sep in Python?
# The sep parameter in the print() function is used to specify the separator between the items you are printing.
# 
# By default, Python puts a space between multiple values in print():


print("Batman", "is", "cool")
# Output:
# Batman is cool

# 🛠 Using sep to change the separator
# 🧪 Examples:

print("2025", "04", "17", sep="-")
# Output:
# 2025-04-17


print("Python", "is", "awesome", sep="🔥")
# Output:
# Python🔥is🔥awesome

print("B", "A", "T", "M", "A", "N", sep="-")
# Output:
# B-A-T-M-A-N


# 🤔 Syntax
# print(value1, value2, ..., sep="separator")



# sepparameter in print(): The separator between the arguments to print() function in Python is space by default which can be modified and made to any character using the ‘sep’ parameter.
print("11", "06", "24")              # Output: 11 06 24
print("11", "06", "24", sep = "/")   # Output: 11/06/24
print("11", "06", "24", sep = "S")   # Output: 11S06S24