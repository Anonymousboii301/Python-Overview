# Ex3 : 

class Student:
    # class variable
    count = 0

    def __init__(self, name, age):
        # instance variable
        self.name = name
        self.age = age
        Student.count += 1

    def __str__(self):
        return f"Name: {self.name}, age: {self.age}"


s1 = Student("John", 18)
print(s1)
print("Student count:", Student.count)

s2 = Student("Smith", 19)
s3 = Student("Alex", 17)

print(s2)
print(s3)
print("Student count:", Student.count)

# output
'''
Name: John, age: 18
Student count: 1
Name: Smith, age: 19
Name: Alex, age: 17
Student count: 3
'''

