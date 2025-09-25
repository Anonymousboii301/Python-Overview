
a1 = 10
a2 = 10.0
a3 = '10.0'
a4 = bool(10)
a5 = bool(0)
a6 = bool(-10)   
s = complex(8,2)  #complex number
print(s)

print(type(a1), a1)
print(type(a2), a2)
print(type(a3), a3)
print(type(a4), a4)
print(type(a5), a5)
print(type(a6), a6)


a = "31.2"
b = float(a)  # a but type should be float
t = type(b)
print(t)


str(31)   # "31"   integer to string conversion 
int("32") # 32     string to integer conversion 
float(32)  # 32.0   integer to float conversion




# In Python, there are two types of type casting:

# 
# 🔹 1. Implicit Type Casting (Automatic)
# Python automatically converts one data type to another when it makes sense.
# 
# ✅ Example:


a = 10        # int
b = 3.5       # float
c = a + b     # float, because Python converts 'a' to float automatically

print(c)      # Output: 13.5
print(type(c))  # Output: <class 'float'>





# 
# 
# 🔹 2. Explicit Type Casting (Manual)
# You manually convert data from one type to another using built-in functions:


'''
Function	Converts to...
int()	Integer
float()	Float
str()	String
bool()	Boolean
list()	List
tuple()	Tuple

'''


# ✅ Examples:


x = "100"
y = int(x)       # Convert string to integer

print(y)         # Output: 100
print(type(y))   # Output: <class 'int'>




a = 5
b = float(a)     # Convert integer to float

print(b)         # Output: 5.0





n = 10
s = str(n)       # Convert integer to string

print(s)         # Output: '10'
print(type(s))   # Output: <class 'str'>


# ❗Note:
# If the value cannot be converted properly, Python will throw an error.
# x = "abc"
# y = int(x)  # ❌ Error: invalid literal for int()