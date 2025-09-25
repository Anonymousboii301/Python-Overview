'''
TYPES OF FUNCTIONS IN PYTHON 
There are two types of functions in python: 
• Built in functions (Already present in python) 
• User defined functions (Defined by the user) 
Examples of built in functions includes len(), print(), range() etc. 
The func1() function we defined is an example of user defined function.
'''


'''
DEFAULT PARAMETER VALUE 
We can have a value as default as default argument in a function. 
If we specify name = “stranger” in the line containing def, this value is used when no 
argument is passed. 
Example: 
def greet(name = "stranger"): 
# function body 
greet() # name will be "stranger" in function body (default) 
greet("harry") # name will be "harry" in function body (passed)

'''

def Good_day(name , ending = "Have a nice day "):
    print("Good day, " + name)
    print(ending)

Good_day("Ayush" ,"Thanks for your help ")
Good_day("Dogggesh" , "Thank you")
Good_day("Batman" ,"Thanks ")
Good_day("Jack ")




