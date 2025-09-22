# 1. . Write a program using functions to find greatest of three numbres :




# def greatest(a,b,c):
    #   a = int(input("Enter a number : "))
    #   b = int(input("Enter a number : "))
    #   c = int(input("Enter a number : "))
# 
    #   if(a>b and a > c):
            # print(f"{a} is greatest ......")
# 
# 
    #   elif(b>a and b > c):
            # print(f"{b} is greatest ......") 
# 
# 
    #   else:
            # print(f"{c} is greatest ........")
# 

# greatest()





def greatest(a,b,c):
    if(a>b and a > c):
           return a


    elif(b>a and b > c):
          return b  


    elif(c>b and c>a):
          return c
        

a = 23 
b = 35
c = 67

print(greatest(a,b,c))