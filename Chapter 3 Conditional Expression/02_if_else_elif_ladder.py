# IF ELSE AND ELIF IN PYTHON 
# In python programming too, we must be able to execute instructions on a condition(s) 
# being met. 
# This is what conditionals are for! 

'''
If else and elif statements are a multiway decision taken by our program due to certain 
conditions in our code. 





Syntax: 
if (condition1): # if condition1 is True 
print ("yes") 

elif(condition2): # if condition2 is True  
print("no") 

else:             
# otherwise 
print("maybe")  


'''
a = int(input("Enter your age please :  "))

#  If elif else ladder 

if(a>=18):
    print("You are above the age of consent....")
    print("Good for you!!!!")


elif(a<0):
    print("Invalid age........... ")


elif(a==0):
    print("You are entering 0 which is invalid age  ")    


else: 
    print("You are below the age of consent... ")   




print("End of program!!!!!!!!!!........")




