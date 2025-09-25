# Example 1: Here we are reading a file and printing each line.

# Opening file in read mode
file = open('example.txt', 'r')

# Iterating line by line
for line in file:
    print(line)

# Closing the file
file.close()         # it is a good practice to close a file

# -------------------------------
# Example Output (with extra blank lines because of \n in file):
'''
Hello

How are you?

Hope you are enjoying Python.
'''


# Here you can notice there is an extra line after each of the lines. Because in the file system, there is a '\n' character that gets included when we press enter to go to the new line to write