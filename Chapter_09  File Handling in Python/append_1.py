file = open('example.txt', 'a')

# Append a new line at the end of the file
file.write('a new line will be added')

file.close()

# The content of the file becomes
'''
Hello
How are you?
Hope you are enjoying Python.
a new line will be added
'''