def Good_day(name):
    print("Good day, " + name)


Good_day("Ayush")
Good_day("Dogggesh")
Good_day("Batman")

# name - argument 

def Good_day(name , ending):
    print("Good day, " + name)
    print(ending)

Good_day("Ayush" ,"Thanks for your help ")
Good_day("Dogggesh" , "Thank you")
Good_day("Batman" ,"Thanks ")




# return 
def Good_day(name):
    print("Good day, " + name)
    return "done"

a= Good_day("Batman")
print(a)


'''
FUNCTIONS WITH ARGUMENTS 
A function can accept some value it can work with. We can put these values in the 
parentheses. 
A function can also return value as shown below: 
30 
def greet(name): 
gr = "hello"+ name  
return gr  
a = greet ("harry") 
# a will now contain "hello harry" 
# '''