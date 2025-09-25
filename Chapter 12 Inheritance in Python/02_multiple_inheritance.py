class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")


class Coder:
    languages = "Python"
    def printLanguage(self):
        print(f"Out of all the languages here is your language: {self.languages}")









class Programmer(Employee , Coder) :
    company = 'ITC Infotech'
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.showLanguage} language ")



a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showLanguage()