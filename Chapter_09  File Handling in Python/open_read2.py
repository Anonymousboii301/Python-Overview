# Example 2 : Here we are going to read a file and store all the lines in a list format.
file = open('example.txt', 'r')

# readlines() method reads all the lines of the file and
# returns in a list format where every line is an item of the list
l = file.readlines()
print(l)

file.close()

# Output
# ['Hello\n', 'How are you?\n', 'Hope you are enjoying Python.\n']




# Here you can observe the '\n' character present at the end of the lines.