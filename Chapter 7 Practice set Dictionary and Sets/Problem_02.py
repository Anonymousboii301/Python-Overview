# 2. Write a program to input eight numbers from the user and display all the unique 
# numbers (once).

s = set()

num1 = int(input("enter 1st number : "))
s.add(num1)

num2 = int(input("enter 2nd number : "))
s.add(num2)
                 
num3 = int(input("enter 3rd number : "))
s.add(num3)

num4 = int(input("enter 4th number : "))
s.add(num4)

num5 = int(input("enter 5th number : "))
s.add(num5)

num6 = int(input("enter 6th number : "))
s.add(num6)
num7 = int(input("enter 7th number : "))
s.add(num7)
num8 = int(input("enter 8th number : "))
s.add(num8)

print(s)