f = open("ayush'stext.txt", "r")   # for read mode default value of 2nd parameter is "r"
# s = f.read()
# print(s)


# READLINES
# lines = f.readlines()  # readlines - return list jo lines ki list hoti hai 
# print(lines , type(lines))



# READLINE

# line1 = f.readline()
# print(line1, type(line1))
# line2 = f.readline()
# print(line2, type(line2))
# line3 = f.readline()
# print(line3, type(line3))

# line4 = f.readline()
# line5 = f.readline()
# line6 = f.readline()
# line7 = f.readline()
# line8 = f.readline()
# line9 = f.readline()
# line10 = f.readline()
# print(line10)

# line11 = f.readline()
# print(line11 == "")   # file empty
# f.close()


# same work by while loop 

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()


f.close()