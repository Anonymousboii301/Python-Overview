# 2. Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the use

marks_sub1 = int(input("Enter your marks : "))
marks_sub2 = int(input("Enter your marks : "))
marks_sub3 = int(input("Enter your marks : "))

total_marks = marks_sub1 + marks_sub2 + marks_sub3

# check for total percentage 
total_percentage = (total_marks/300)*100

if(total_percentage>=40 and marks_sub1 >=33 and marks_sub2 >= 33 and marks_sub3>=33):
    print("congratulations , You have passed the exam :" , total_percentage)

else:
    print("sorry but You failed the exam , try again next year !" , total_percentage)