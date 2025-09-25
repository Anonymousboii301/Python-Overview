# ✅ What is Dynamic Typing in Python?
# Dynamic Typing means you don't need to declare the data type of a variable when you create it.
# Python automatically detects the type of the variable at runtime based on the value you assign.


x = 10           # x is an integer
x = "Batman"     # now x is a string
x = 3.14         # now x is a float

# ➡️ The type of variable x changes depending on the value assigned.
# You don’t need to specify the type like you do in statically typed languages (like C, Java, etc.).

a = 42
print(type(a))      # <class 'int'>

a = "hello"
print(type(a))      # <class 'str'>

a = True
print(type(a))      # <class 'bool'>


# ✅ Advantages of Dynamic Typing:
# Easier to write and read code
# 
# Faster for prototyping and scripting
# 
# No need to worry about declaring types
# 
# ⚠️ Disadvantages:
# Type errors can occur at runtime
# 
# Harder to detect bugs in large programs
# 
# Can cause unexpected behavior if you're not careful



# 🔹 Example 1: Changing Variable Type
x = 10          # x is an integer
print(type(x))  # <class 'int'>

x = "Python"    # now x is a string
print(type(x))  # <class 'str'>

x = [1, 2, 3]   # now x is a list
print(type(x))  # <class 'list'>



# 🔹 Example 2: Same Variable Used for Different Types

data = True
print(data, type(data))  # True <class 'bool'>

data = 99.99
print(data, type(data))  # 99.99 <class 'float'>

data = {"name": "Batman"}
print(data, type(data))  # {'name': 'Batman'} <class 'dict'>


# 🔹 Example 3: Input from User is Always String


x = input("Enter something: ")  # Always string
print(x, type(x))

# You can convert it dynamically:
x = int(x)
print(x, type(x))




# 🔹 Example 4: Function Returns Different Types

def check(flag):
    if flag:
        return 123       # int
    else:
        return "hello"   # str

result = check(True)
print(result, type(result))  # 123 <class 'int'>

result = check(False)
print(result, type(result))  # 'hello' <class 'str'>



# 🔹 Example 5: Dynamic Typing in Lists

items = [1, "apple", 3.14, True, [1, 2]]
for item in items:
    print(item, type(item))



# 🔸 Summary:

# Python lets a variable change its type during execution.
# No need to declare type explicitly.
# This makes Python easy to use, but you need to be careful in big programs!