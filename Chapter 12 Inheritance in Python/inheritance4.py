class Person():
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def Display(self):
        print("Name:", self.name, "ID:", self.id)

class Employee(Person):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def Display(self):
        print("Name:", self.name, "ID:", self.id, "Salary:", self.salary)

emp = Employee("Dan", 123, 10000)
emp.Display()

emp.salary = 15000
emp.Display()

# output
'''
Name: Dan ID: 123 Salary: 10000
Name: Dan ID: 123 Salary: 15000
'''