#Function in Python

#Call the function

#Arguments


def greet(name):
  print("Hello,", name)
greet("Python") # Output: Hello, Python

"""## Default Arguments"""
# 1. 

def add(x, y=100):
  return x + y
print(add(10, 10)) # Output: 20
print(add(10))     # Output: 110


# 2. 
def greet(name="Guest"):
    return f"Hello {name}"
print(greet())         # Hello Guest
print(greet("Ayush"))  # Hello Ayush





"""## Keyword Arguments"""

def student(name, age):
    return f"{name} is {age} years old"
print(student(age=20, name="Bruce"))





"""## Positional Arguments"""

def power(x, y):
    return x ** y
print(power(2, 3))  # 8
print(power(3, 4))  # 27

def sub(x, y):
  return x- y
print(sub(x=30, y=10))     # Output: 20
print(sub(y=10, x=30))     # Output: 20
print(sub(30, 10))         # Output: 20
print(sub(10, 30))         # Output: -20






"""## Returning multiple values:"""

def square_point(x, y, z):
 x_squared = x * x
 y_squared = y * y
 z_squared = z * z
 return x_squared, y_squared, z_squared          # Return all three values


three_squared, four_squared, five_squared = square_point(3, 4, 5)
print(three_squared, four_squared, five_squared)       # output: 9 16 2
