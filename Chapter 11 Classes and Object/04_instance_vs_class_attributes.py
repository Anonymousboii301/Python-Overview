class Employee:
    language = "Py" # This is a class attribute
    salary = 12000000

ayush = Employee()
ayush.language = "Javascript" # This is an instance attribute
print(ayush.language,ayush.salary)
