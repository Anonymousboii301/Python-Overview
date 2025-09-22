
"""## Python Scope of Variable

**Python Local variable :** Local variables are initialised within a function and are 
unique to that function. It cannot be accessed outside of the function.
"""

def f():
  s = "I love Python" # local variable
  print(s)

f()
# print(s)        # this line throws an error as
                # local variable cannot be accessed outside of the function


# Output
# I love Python
# NameError: name 's' is not defined













"""**Python Global variables:** Global variables are the ones that are defined and declared 
outside any function and are not specified to any function. They can be used by any part of 
the program"""


def f():
  print(s)

# global scope
s = "I love Python"
f()
 # Output
 # I love Python








""" ##### **Global and Local Variables with the Same Name**

 If a global variable is reinitialized inside a function. It is considered as a local 
variable of that function and if any modification is done on that variable, the value of 
the global variable will remain
 unaffected. For example:
"""

def f():
  s = "Hello World"
  print(s)

# global scope
s = "I love Python"
f()
print(s)


# Output
# Hello World
# I love Python



""" To modify the value of the global variable we need to use the global keyword"""


def f():
  global s
  s = "Hello World"
  print(s)

# global scope
s = "I love Python"
f()
print(s)


# Output
# Hello World
# Hello World
