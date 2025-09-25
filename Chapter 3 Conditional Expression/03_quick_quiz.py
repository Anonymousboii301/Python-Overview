# Quick Quiz: Write a program to print yes when the age entered by the user is greater 
# than or equal to 18. 

age = int(input("Enter yuor age please : "))

if age < 18 and age > 0 :
    print("False")

elif age <= 0:
    print("Please Enter a valid age ........")
else :
    print("True")