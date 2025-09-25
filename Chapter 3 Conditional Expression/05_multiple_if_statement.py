a = int(input("Enter your age please :"))



# if statement - 1 

if(a%2==0):
    print("Even number ....")

# end of if statement - 1

# if statement - 2

if(a>=18):
    print("You are above the age of consent....")
    print("Good for you!!!!")


elif(a<0):
    print("Invalid age........... ")


elif(a==0):
    print("You are entering 0 which is invalid age  ")    


else: 
    print("You are below the age of consent... ")   


print("ENd of program!!!!!!!!!!........")


# else and elif - alone nhi honge code me 
# if ho sakta hai 



# IMPORTANT NOTES: 
# 1. There can be any number of elif statements. 
# 2. Last else is executed only if all the conditions inside elifs fail.


