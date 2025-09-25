# 1 -  ✅ if Statement Syntax

# if condition:
    # code to run if condition is True

# Example:
x = 5
if x > 0:
    print("x is positive")  
print("This is outside of If statement!!!!!!")


# 2 - ✅ if...else Statement Syntax

# if condition:
    # code to run if condition is True
# else:
    # code to run if condition is False

# Example:
x = -3
if x >= 0:
    print("x is non-negative")
else:
    print("x is negative")
print("This is outside of If - Else Statement !!!!!!!")


#  3 - ✅ if...elif...else Statement Syntax

# if condition1:
    # code if condition1 is True
# elif condition2:
    # code if condition2 is True
# elif condition3:
    # code if condition3 is True
...
# else:
    # code if all above conditions are False


# Example:
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
print("This is outside of If - Elif - Else Statement !!!!!!!")




#  4 - ✅ Nested if Statement Syntax
# (Using if inside another if)

# if condition1:
    # if condition2:
        # code if both condition1 and condition2 are True

# Example:
x = 10
y = 20
if x > 5:
    if y > 15:
        print("Both conditions are true")
print("This is outside of Nested If Statement !!!!!!!")



# 5 - ✅ Syntax of Nested if...else

# if condition1:
    # if condition1 is True, check another condition
    # if condition2:
        # code block if both condition1 and condition2 are True
    # else:
        # code block if condition1 is True but condition2 is False
# else:
    # code block if condition1 is False


# 🧪 Example:
x = 15

if x > 10:
    print("x is greater than 10")
    if x < 20:
        print("x is less than 20")
    else:
        print("x is greater than or equal to 20")
else:
    print("x is 10 or less")
print("This is outside of Nested If - Else Statement !!!!!!!")


# 🚀 Real Life Example: Voting System
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("You can vote")
    else:
        print("You need an ID to vote")
else:
    print("You are not eligible to vote")






# 6 - ✅ Nested if...elif...else
# It means using if...elif...else inside another if, elif, or else block.

# ✅ Syntax:

# if condition1:
    # outer if block
    # if condition2:
        # inner if block
    # elif condition3:
        # inner elif block
    # else:
        # inner else block
# elif condition4:
    # outer elif block
    # ...
# else:
    # outer else block

# 🧪 Example:

x = 15
y = 8

if x > 10:
    print("x is greater than 10")
    if y < 5:
        print("y is less than 5")
    elif y < 10:
        print("y is between 5 and 10")
    else:
        print("y is 10 or more")
else:
    print("x is 10 or less")



# Real Life Example: Student Grade and Attendance

marks = 85
attendance = 75

if marks >= 50:
    print("Passed the exam")
    if attendance >= 75:
        print("Eligible for certificate")
    elif attendance >= 60:
        print("Attend makeup classes to get certificate")
    else:
        print("Not eligible due to low attendance")
else:
    print("Failed the exam")


