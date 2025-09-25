class Person():
    def __init__(self, name, id):
        self.name = name
        self.__id = id   # making the variable private

    def Display(self):
        print("Name:", self.name, "ID:", self.__id)

    def showID(self):
        return self.__id

class Employee(Person):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def Display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        # following line throws an error as private variable is not accessible
        # print("ID:", self.__id)
        print("ID:", self.showID())  # access via parent method

        # parent class method can be accessed by 'self.methodName()'
        # if no other method is present in the child class with same name

emp = Employee("Dan", 123, 10000)
emp.Display()

# output
'''
Name: Dan
Salary: 10000
ID: 123
'''