file = open('example3.txt', 'w')

# writelines() writes a list of strings into the file
file.writelines(["Item 1\n", "Item 2 ", "Item 3\n", "Item 4"])

file.close()

# The content of the file becomes
'''
Item 1
Item 2 Item 3
Item 4
'''