class Person():
    def __init__(self, name, id):
        self.name = name
        self.__id = id   # making the variable private

    def Display(self):
        print("Name:", self.name, "ID:", self.__id)

    def changeID(self, id):
        self.__id = id

# creating a object and show details
p = Person('Nobita', 1)
p.Display()

# changing the value of id directly
p.__id = 2
# it will not throw any error but nothing will be changed
# as private attributes are not directly accessible even if by own object
p.Display()

# if you want to change any private variables, you have to use
# some method that can access that private variables.
# Because private variables are accessible inside any method
# of that class, but not any child/sub class.
p.changeID(3)
p.Display()

# the following line throws an error as private methods are accessible by
# methods inside the class but not accessible by object.
# p.__privateMethod()

# output
'''
Name: Nobita ID: 1
Name: Nobita ID: 1
Name: Nobita ID: 3
'''