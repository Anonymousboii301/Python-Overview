"""Example snippets showing simple class usage (kept as examples inside a
module-level string so they don't execute when importing/running the file).

Examples (not executed):

class Person:
    pass

class PersonWithInit:
    def __init__(self):
        print("A new person is being created")

    # examples of attaching attributes dynamically:
    # person_1 = PersonWithInit()
    # person_1.name = "Batman"
    # person_1.age = 23
    # person_1.city = "Gotham"

"""


class Person1:
    def __init__(self, Person_name, age, city):
        # `self` attributes can be named anything; parameter names must match
        # those used when calling the constructor.
        self.name = Person_name
        self.age = age
        self.city = city


p1 = Person1("Batman", 23, "Gotham")
print(type(p1))  # <class '__main__.Person1'>
print(p1.name)
print(p1.age)
print(p1.city)

# If you try to call Person1() with no arguments you'll get:
# TypeError: Person1.__init__() missing 3 required positional arguments: 'Person_name', 'age', and 'city'


class Person2:
    def __init__(self, Person_name, age, city, country='India'):
        # Make `country` optional by giving it a default value.
        # Or, if you expect the caller to always pass country, remove the default
        # and pass 4 arguments when creating the instance.
        self.name = Person_name
        self.age = age
        self.city = city
        self.country = country


p2 = Person2("Batman", 23, "Gotham")
print(type(p2))  # <class '__main__.Person2'>
print(p2.name, p2.age, p2.city, p2.country)


# `self` is a reference to the current instance of the class (object).








# Use default values for attributes

class Student:
    def __init__(self , math_marks , eng_marks , sci_marks , ss_marks=0 ):
        self.math_marks = math_marks
        self.eng_marks = eng_marks
        self.sci_marks = sci_marks
        self.ss_marks = ss_marks


student1 = Student(90 , 85 , 88)
print(student1.math_marks , student1.eng_marks , student1.sci_marks , student1.ss_marks)     



student2 = Student(78 , 80 , 82 , 79)
print(student2.math_marks , student2.eng_marks , student2.sci_marks , student2.ss_marks)



class Employee:
    def __init__(self , name , language , salary):
        self.name = name
        self.language = language
        self.salary = salary
        self.increment = 0

emp1 = Employee("Ayush" , "Py" , 12000000)
print(emp1.name , emp1.language , emp1.salary , emp1.increment)


emp2 = Employee("John" , "Java" , 15000000)
print(emp2.name , emp2.language , emp2.salary , emp2.increment)