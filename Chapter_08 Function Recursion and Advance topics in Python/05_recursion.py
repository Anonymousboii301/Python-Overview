'''
RECURSION 
Recursion is a function which calls itself.


It is used to directly use a mathematical formula as function.  
Example: 
factorial(n) = n x factorial (n-1) 
This function can be defined as follows: 
def factorial(n) 
if i == 0 or i==1: # base condition which doesn’t call the function 
any further 
return 1 
else: 
return n*factorial(n-1) # function calling itself
'''
# factorial(1) =1
# factorial(2) =2x1
# factorial(3) =3x2x1
# factorial(4) =4x3x2x1
# factorial(5) =5x4x3x2x1
#  Factorial(n) = nx (n-1) x n-2 x .........x 2x1
#  Factorial(n) = n x factorial(n-1)

def factorial(n):
    # Base case for recursion
    if n == 1 or n == 0:
        return 1
    # Recursive call
    return n * factorial(n - 1)

# Taking input from the user
n = int(input("Enter a number: "))
# Printing the result of factorial function call
print(f'The factorial of this number is {factorial(n)}')
