# 1. Write a program to find the greatest of four numbers entered by the user.

num1 = int(input("Enter the number 1 please : "))
num2 = int(input("Enter the number 2 please : "))
num3 = int(input("Enter the number 3 please : "))
num4 = int(input("Enter the number 4 please : "))

if(num1>num2 and num1 > num3 and num1 > num4):
    print(f"{num1} is greatest all of them ")

elif(num2>num1 and num2 > num3 and num2 > num4):
    print(f"{num2} is greatest all of them ")

elif(num3>num2 and num3 > num1 and num3 > num4):
    print(f"{num3} is greatest all of them ")

else:
    print(f"{num4} is greatest all of them ")


print("End of program")