# Write a python program to print the contents of a directory using the os module. 
# Search online for the function which does that.  


import os

contents = os.listdir()
print(contents)

path = '/'
contents = os.listdir(path)
print(contents)
