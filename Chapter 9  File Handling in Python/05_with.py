# with statement

# f = open("file.txt")
# print(f.read())
# f.close()


# The same thing can be written using with statement like this 

with open("file.txt") as f:
    print(f.read())


# You don't have to explicity close the file 

