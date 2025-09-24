'''
a = "a very long string with emails 
emails = []
3 seconds 

'''
'''
TYPE OF FILES. 
There are 2 types of files: 
1. Text files (.txt, .c, etc) 
2. Binary files (.jpg, .dat, etc) 
Python has a lot of functions for reading, updating, and deleting files.
'''



f = open("file.txt" ,"r")  # open 
data = f.read()      # read f
print(data)     # print
f.close()   # close

'''
OPENING A FILE 
Python has an open() function for opening files. It takes 2 parameters:  filename and 
mode. 
# open("filename", "mode of opening(read mode by default)") 
open("this.txt", "r") 

'''
