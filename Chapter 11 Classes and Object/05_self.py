# class Employee:
    # language = "Python" # This is a class attribute
    # salary = 12000000
# 
    # def getInfo(self):
        # print(f"THe language id {self.language} . The salary is {self.salary} .")
# 
    # def greet(self):
    #   print("Namaskar !!!!!!")
# 
# 
# 
# ayush = Employee()
# ayush.language = "Javascript"  # This is an instance attribute 
# 
# ayush.getInfo()
# Employee.getInfo(ayush)
# 
# 
# ayush.greet()




# Defining a class named Employee
class Employee:
    language = "Python"  # Class attribute (shared across all instances)
    salary = 12000000    # Another class attribute

    # Method to display employee information
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}.")

    # Method to print a greeting message
    def greet(self):
        print("Namaskar !!!!!!")

# Creating an instance of Employee named 'ayush'
ayush = Employee()        

# Assigning a new value to 'language' for the instance 'ayush'
# This creates an instance attribute that overrides the class attribute for 'ayush'
ayush.language = "Javascript"

# Calling getInfo() method using the instance 'ayush'
ayush.getInfo()  
# Output: The language is Javascript. The salary is 12000000.
# Even though 'salary' is a class attribute, it is accessed through 'self', 
# which first checks for an instance attribute and then the class attribute.

# Calling getInfo() using the class but passing the instance 'ayush'
Employee.getInfo(ayush)  
# This is equivalent to 'ayush.getInfo()' because 'self' refers to 'ayush' here.
# Output: The language is Javascript. The salary is 12000000.

# Calling greet() method for 'ayush'
ayush.greet()  
# Output: Namaskar !!!!!!



