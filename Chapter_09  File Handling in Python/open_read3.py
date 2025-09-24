# Example 3: Here we are going to read one line at a time.

file = open('example.txt', 'r')

# readline() method reads a line from a file and returns it as a string
first_line = file.readline()
print(first_line.strip())   # strip() removes '\n'

# Read the next line
second_line = file.readline()
print(second_line.strip())

# We can also print directly without storing it
print(file.readline())

file.close()

# Output
'''
Hello
How are you?
Hope you are enjoying Python.
'''