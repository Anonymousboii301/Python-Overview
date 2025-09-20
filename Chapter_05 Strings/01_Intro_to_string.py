
a ='Ayush'       # Single quoted string 
b = "Ayush"      # Double quoted string 
c = '''Ayush'''  # Triple quoted string 




# Python strings are "immutable" which means
#  they cannot be changed after they are created (Java strings also use this immutable style)


# String slicing
a1 = a[0:3]    #The index in a sting starts from 0 to (length -1) in Python. In order to slice a string, (excluding 3)
print(a1)      # Ayu
print(a[1:3])  # yu



# Negative Indices: Negative indices can also be used as shown in the figure above. -1 
# corresponds to the (length - 1) index, -2 to (length - 2). 

a2 = a[-4:-1]   # Output = yus
print(a2)




# String length
print(len(a))
