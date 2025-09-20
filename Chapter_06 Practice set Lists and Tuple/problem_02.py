# 2. Write a program to accept marks of 6 students and display them in a sorted 
# manner. 

list1 = []

studnet1_marks = int(input("Enter your marks : "))
list1.append(studnet1_marks)

studnet2_marks = int(input("Enter your marks : "))
list1.append(studnet2_marks)

studnet3_marks = int(input("Enter your marks : "))
list1.append(studnet3_marks)

studnet4_marks = int(input("Enter your marks : "))
list1.append(studnet4_marks)

studnet5_marks = int(input("Enter your marks : "))
list1.append(studnet5_marks)

studnet6_marks = int(input("Enter your marks : "))
list1.append(studnet6_marks)

list1.sort()    # for sorting 

print(list1)  # for printing 