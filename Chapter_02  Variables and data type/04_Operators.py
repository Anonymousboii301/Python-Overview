''' 

OPERATORS IN PYTHON 
Following are some common operators in python: 
1. Arithmetic operators: +, -, *, / etc. 
2. Assignment operators:  =, +=, -= etc. 
3. Comparison operators: ==, >, >=, <,  != etc. 
4. Logical operators: and, or, not.

'''

#  Arithmetic operators 
a = 34
b = 4
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print("//////////////////////////////////////")

#  Assignment operators
a = 4-2  # Assign 4-2 in a
print(a)

print("//////////////////////////////////////")


b = 6
b += 3   # Increment the value of b by 3 and then assign it to b 
print(b)

print("//////////////////////////////////////")

b -= 3   # decrement the value of b by 3 and then assign it to b 
print(b)

print("//////////////////////////////////////")



# Comparison operators 

d1 = 4<3
print(d1)

d2 = 67>=6
print(d2)

d3 = 67==67
# d3 = 67=67   Error here 
print(d3)

d4 = 56!=67
print(d4)

# Always gives boolean value ......

# Logical operators 

e1 = True or False 
e2 = True and False 
e3 = not False 
print(e1)




print("//////////////////////////////////////")




# truth table of 'or'
print("True or False is" , True or False )
print("True or True is" , True or True )
print("False or False is" , False or False )
print("False or True is" , False or True )










print("//////////////////////////////////////")





#  truth table of 'and'
print("True and False is" , True and  False )
print("True and True is" , True and True )
print("False and False is" , False and False )
print("False and True is" , False and True )




print("//////////////////////////////////////")





#  truth table of 'not'

print(not(True))
print(not False)
