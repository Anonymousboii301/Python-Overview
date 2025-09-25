# Ex1 : 

class Person:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # methods
    def display(self):
        print(self.name, self.age)


# creating object of the class
p1 = Person("John", 36)

# accessing the attribute of the object
print(p1.name)

# using the method of the object
p1.display()


# Output
'''
John
John 36
'''
