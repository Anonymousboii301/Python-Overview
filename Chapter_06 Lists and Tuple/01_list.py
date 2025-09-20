# Lists - Python lists are containers to store a set of values of any data type.
'''
What is a List?
A list in Python is a collection of ordered, changeable (mutable) items. 
Lists can hold items of any data type (integers, strings, objects, etc.), 
and they are defined using square brackets [].
'''
# ex -  
friends = ["Apple" , 'banana' , 5 , 456.7 , "Ayush" , False , "Bruce wayne"]
print(friends[0])

friends[0] = 10
print(friends)

# unlike strings lists are mutable means we can change the value inside list like above ex

print(friends[6])   # indexing 
print(friends[1:6])   # Slicing 


# A list can be indexed just like a string. 


l1 = [7,9,"Batman"] 
l1[0] # 7 
print(l1[0])

l1[1] # 9 

print(l1[1])

# l1[70]  # error 

l1[0:2] # [7,9]  #list slicing  
print(l1[0:2])
