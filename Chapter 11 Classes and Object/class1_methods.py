class Instructor:
    # classs Object Variable 
    followers = 0
    def __init__(self , name , address):
        self.name = name 
        self.address = address
        # self.followers = 0      # instance variable


    def display(self):             # instance method
        return f"{self.name} from {self.address} has {self.followers} followers"
    
    def add_followers(self):
        self.followers += 1
        return self.followers      # Without return it will return None
    
    def remove_followers(self):
        if self.followers > 0:
            self.followers -= 1
        return self.followers

instructor1 = Instructor("John" , "USA")
print(instructor1.name , instructor1.address , instructor1.followers)

instructor2 = Instructor("Emma" , "UK")
print(instructor2.name , instructor2.address , instructor2.followers)


print(instructor1.display())
print(instructor2.display())

print("After adding followers")
print(instructor1.add_followers())

print(instructor2.add_followers())
print(instructor2.add_followers())

print(instructor1.remove_followers())
print(instructor2.remove_followers())