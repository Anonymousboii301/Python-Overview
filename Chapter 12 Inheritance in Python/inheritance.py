# EX 1 : 

class Person():
  def Display(self):
    print("From Person Class")


class Employee(Person):
  def Print(self):
    print("From Employee Class")


per = Person()
per.Display()
 
emp = Employee()
emp.Print()
emp.Display()

# output
'''
From Person Class
From Employee Class
From Person Class
'''



