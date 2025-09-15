# What is Multiple Assignment?
# Multiple assignment means assigning values to multiple variables in a single line.

# 🔹 Basic Syntax:
a, b, c = 1, 2, 3
print(a)  # 1
print(b)  # 2
print(c)  # 3
# ➡️ The number of variables on the left must match the number of values on the right.



# 🔸 Assigning Same Value to Multiple Variables:

x = y = z = 100
print(x, y, z)  # 100 100 100



#  Swapping Values (without temp variable):
a = 5
b = 10
a, b = b, a
print(a, b)  # 10 5


# 🔸 Using with Lists or Tuples:
data = [10, 20, 30]
x, y, z = data
print(x, y, z)  # 10 20 30



# ❗ Error Example (Unequal Values):

# a, b = 1, 2, 3  # ❌ Error: too many values to unpack