class Person():
    def Display(self):
        print("From Person Class")

class Employee(Person):
    def Display(self):
        print("From Employee Class")
        super().Display()
        # Person.Display(self)              # alternate way

per = Person()
per.Display()

emp = Employee()
emp.Display()

# output
'''
From Person Class
From Employee Class
From Person Class
'''
