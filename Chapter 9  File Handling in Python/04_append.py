'''
write mode = "w"
read mode = "r"
append mode = "a"

'''

st = "I Am dark knight , I am vengence"
f = open("myfile.txt" , "a")
f.write(st)
f.write("\n")
f.close()
